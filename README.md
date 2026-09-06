# Trading Journal

A Django-based options trading journal for recording, reviewing, and analyzing trades.

## Stack

- Django
- Django REST Framework
- SQLite
- Ollama for local AI-assisted trade summaries

## Local Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set your local environment values as needed.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## API

- `GET /api/trades/` - list trades
- `POST /api/trades/` - create a trade
- `GET /api/trades/<id>/` - retrieve a trade
- `PUT/PATCH /api/trades/<id>/` - update a trade
- `DELETE /api/trades/<id>/` - delete a trade
- `GET /api/strategy-rules/` - list strategy rules
- `POST /api/strategy-rules/` - create a strategy rule
- `POST /api/ai/summary/` - generate an Ollama trade summary

## Project Structure

- `config/` - Django project configuration
- `trades/` - Core trading journal application
- `ai_assist/` - Ollama integration
- `templates/` - HTML templates
- `static/` - Static assets
