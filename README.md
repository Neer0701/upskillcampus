# upskillcampus

# URL Shortener

A simple URL shortening web application built with **Python** and **Flask**. It takes a long URL, generates a short, unique code for it, stores the mapping in a SQLite database, and redirects visitors from the short link to the original URL.

## Features

- Convert any long URL into a short, shareable link
- Random 6-character alphanumeric short code generation
- Persistent storage using SQLite
- Automatic redirection from the short URL to the original URL
- Lightweight — no external services or accounts required

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite3
- **Frontend:** HTML (Flask templating via Jinja2)

## Project Structure

```
url-shortener/
├── app.py              # Main Flask application (routes, short code generation, redirection)
├── database.py         # Database setup script (creates the urls table)
├── requirements.txt    # Python dependencies
├── urls.db             # SQLite database (auto-generated)
└── templates/
    └── index.html       # Home page template (URL submission form)
```

## Database Schema

The application uses a single table, `urls`:

| Column     | Type    | Description                          |
|------------|---------|---------------------------------------|
| `id`       | INTEGER | Primary key, auto-incremented         |
| `original` | TEXT    | The original long URL                 |
| `short`    | TEXT    | The generated short code (unique)     |

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/url-shortener.git
   cd url-shortener
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python database.py
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Paste a long URL into the input field on the home page and submit it.
2. The app generates a short URL (e.g. `http://127.0.0.1:5000/aZ3x9K`) and displays it.
3. Visiting the short URL automatically redirects you to the original long URL.
4. If a short code doesn't exist in the database, the app returns `URL Not Found`.

## How It Works

1. **Submit:** The user submits a long URL via the home page form (`POST /`).
2. **Generate:** `generate_code()` creates a random 6-character alphanumeric short code.
3. **Store:** The original URL and its short code are saved in the `urls` table in SQLite.
4. **Redirect:** When someone visits `/<code>`, the app looks up the code in the database and redirects to the matching original URL.

## Future Improvements

- Click analytics to track how many times each short link is visited
- Custom aliases so users can choose their own short code
- Link expiry dates
- User accounts to manage personal links
- Migration to a more scalable database (e.g. PostgreSQL) for production use

## License

This project is open source and available under the [MIT License](LICENSE).
