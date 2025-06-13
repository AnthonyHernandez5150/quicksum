from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_cors import CORS
from flask_migrate import Migrate
from db import db
from auth import auth_bp
from models import User, Note
from ai import call_ai_api  # Make sure this function is implemented
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add this line
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/profile_pics'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        flash('Username or email already exists.')
        return redirect(url_for('register'))

    # Create and save new user
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    user.save()
    flash('Registration successful! Please log in.')
    return redirect(url_for('login'))

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        flash('Login successful!')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password.')
        return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    notes = Note.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', user=user, notes=notes)

@app.route('/summarize', methods=['POST'])
def summarize():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    note_text = request.form['note']
    source = request.form.get('source', '')
    summary = call_ai_api(note_text)

    # Save the note and summary
    note = Note(
        user_id=user_id,
        original=note_text,
        summary=summary,
        source=source
    )
    db.session.add(note)
    db.session.commit()

    notes = Note.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', summary=summary, notes=notes, user=user)

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    user_id = session.get('user_id')
    note = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if note:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()  # or session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    user_id = session.get('user_id')
    note = Note.query.filter_by(id=note_id, user_id=user_id).first()
    if not note:
        flash('Note not found.')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        note.original = request.form['original']
        note.summary = request.form['summary']
        note.source = request.form.get('source', '')
        db.session.commit()
        flash('Note updated successfully!')
        return redirect(url_for('dashboard'))
    return render_template('edit_note.html', note=note)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.bio = request.form.get('bio', '')
        file = request.files.get('profile_pic')
        if file and allowed_file(file.filename):
            filename = f"user_{user.id}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            user.profile_pic = filename

        # Handle password change
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password:
            if new_password == confirm_password:
                user.password = generate_password_hash(new_password)
                flash('Password changed successfully!')
            else:
                flash('Passwords do not match.', 'danger')
                return redirect(url_for('profile'))

        db.session.commit()
        flash('Profile updated!')
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)