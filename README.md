# QuickSum

QuickSum is a Flask web app for AI-powered note summarization. Users can register, log in, create notes, and get concise AI-generated summaries. Features include user profiles, profile pictures, dark mode, and more.

## Features

- User registration and login (secure password hashing)
- AI-powered note summarization (OpenRouter API)
- Edit and delete notes
- User profile with bio and profile picture upload
- Dark mode toggle
- Responsive Bootstrap UI

## Setup

1. **Clone this repo:**
   ```sh
   git clone https://github.com/YOUR_USERNAME/quicksum.git
   cd quicksum
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Copy `.env.example` to `.env`
   - Get your own [OpenRouter API key](https://openrouter.ai/)
   - Add it to your `.env` file:
     ```
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     ```

5. **Initialize the database:**
   ```sh
   flask db upgrade
   ```

6. **Run the app:**
   ```sh
   flask run
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Deployment

You can deploy this app to [Render](https://render.com/), [Railway](https://railway.app/), [Fly.io](https://fly.io/), or [Heroku](https://heroku.com/).  
Make sure to set your environment variables and use a production-ready database.

## Security

- **Never share your `.env` file or API keys.**
- Passwords are securely hashed.
- Profile pictures are stored in `static/profile_pics`.

## License

MIT

---

**Built with ❤️ using Flask and OpenRouter AI.**