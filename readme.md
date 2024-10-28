# Verifyer 

Verificador para entrada a partidos de BasketUC

## Archivos:

manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
verifyer_site/: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. verifyer_site.urls).
verifyer_site/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
verifyer_site/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
verifyer_site/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
verifyer_site/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
verifyer_site/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


django_app/
│
├── verifyer_site/               # Main project folder (created by Django)
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── app/                     # App folder (contains actual logic for your feature)
│   ├── __init__.py
│   ├── models.py            # Models for ID storage (if using database)
│   ├── views.py             # Handles logic and rendering
│   ├── urls.py              # URL routing for the app
│   ├── templates/           # HTML templates
│   │   └── index.html       # Home page
│   └── static/              # Static files (CSS, JS)
│       ├── css/
│       ├── js/
│       └── img/
│
├── manage.py                # Django management commands
├── db.sqlite3               # SQLite database (if using one)
└── requirements.txt         # Dependencies (Django, pyzbar, etc.)
