# PetClinic — Veterinary Clinic Management System

A Django-based veterinary clinic management system inspired by Spring PetClinic. Built as part of the AI-Assisted Software Engineering Boot Camp challenge.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.14 + Django 6.0 |
| Database | SQLite (file-based, zero config) |
| Frontend | Django Templates + Bootstrap 5 |
| Testing | Django TestCase (unittest) |

## Features

- **Owner Management** — Create, search, update, and view pet owners
- **Pet Management** — Register pets, associate with owners, view history
- **Pet Types** — Configurable types (Dog, Cat, Bird, Hamster, etc.)
- **Veterinarian Management** — Vet profiles with specialties
- **Visit Management** — Schedule visits, record notes, view full history
- **Search** — Search owners by first or last name

## Setup Instructions

### Prerequisites
- Python 3.10+ installed
- pip available

### Steps

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd Doc_Assist

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run database migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

## Run Instructions

```bash
# Activate venv first, then:
python manage.py runserver
```

Open browser at: `http://127.0.0.1:8000`

Admin panel: `http://127.0.0.1:8000/admin`

## Testing Instructions

```bash
# Run all tests
python manage.py test clinic --verbosity=2
```

Expected output: **17 tests, all passing**

## Project Structure

```
Doc_Assist/
├── config/              # Project settings, master URLs
│   ├── settings.py
│   └── urls.py
├── clinic/              # Main application
│   ├── models.py        # Database models
│   ├── views.py         # Page logic
│   ├── urls.py          # URL routes
│   ├── forms.py         # Form definitions
│   ├── admin.py         # Admin panel config
│   ├── tests.py         # Test suite
│   └── templates/clinic # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Technology Choices

**Python + Django** was chosen because:
- Readable syntax — easy to understand and maintain
- "Batteries included" — built-in admin, ORM, auth, forms
- SQLite requires zero database setup for local development
- Large community and extensive documentation
- Rapid development for a time-constrained project
