# ai-notes-flask README

# AI Notes Flask

This is a Flask backend application for the AI Notes project, which provides user authentication and a simple dashboard interface. The backend connects to a SQLite database and exposes RESTful API endpoints for user registration and login.

## Project Structure

- `app.py`: Main application entry point, initializes the Flask app and sets up routes.
- `auth.py`: Contains authentication routes for user registration and login.
- `models.py`: Defines the User model for the SQLite database.
- `db.py`: Sets up the SQLite database connection and initializes the database schema.
- `requirements.txt`: Lists the dependencies required for the Flask application.
- `templates/`: Contains HTML templates for the application, including login, registration, and dashboard views.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ai-notes-flask
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app.py
   ```

5. **Access the API:**
   The API will be available at `http://localhost:5000/api`.

## API Endpoints

- `POST /api/register`: Register a new user.
- `POST /api/login`: Log in an existing user.

## License

This project is licensed under the MIT License.