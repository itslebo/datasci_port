# Data Science Portfolio (Flask)

## Setup

```
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt
```

## Run

```
python app.py
```

Visit http://127.0.0.1:5000

## Structure

- `app.py` — routes: `/` (home), `/project/<slug>` (case study), `/contact` (form POST)
- `projects.py` — project and skill data (edit this to add/change case studies)
- `templates/` — Jinja templates (`base.html` layout, `index.html`, `project.html`, `404.html`)
- `static/css/style.css` — all styling, light/dark theme via CSS variables
- `static/js/main.js` — theme toggle only

## Before going live

- Drop your real resume PDF at `static/resume.pdf` (the header button links there).
- Replace the placeholder email/GitHub/LinkedIn links in `templates/index.html`'s contact section.
- The `/contact` route only logs submissions (`app.logger.info`) — wire it up to a real mailer or forms API in `app.py`.
- Set a real `app.secret_key` (currently a dev placeholder) via an environment variable before deploying.
- Run with a production WSGI server (e.g. gunicorn/waitress), not `python app.py`.
