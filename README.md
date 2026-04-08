# django-sylabus-wi-pb

A Django-based web application for managing university syllabus and academic programs at Bialystok University of
Technology.

## Prerequisites

- Python >=3.12.0

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd django-sylabus-wi-pb
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

```bash
touch .env
echo .env >> DEBUG=True
echo .env >> SECRET_KEY=<paste-your-secret-key-here>
```

Remember to replace `<paste-your-secret-key-here>` with your own secret key.
Never include this file in your commits.

## Running the application

```bash
python manage.py runserver 8000
```

To stop the application send CONTROL-C to terminal. And then run:

```bash
deactivate
```

to deactivate the virtual environment.
