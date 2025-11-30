# Bristol Hackspace Website CMS

This is the repository for the headless CMS used for managing content in the Hackspace website. The CMS uses Django CMS with media uploads provided by the Pillow library.

## Prerequisites

To run this code locally it is assumed you have installed:

- git
- pyenv (to allow selection of virtual python environments)
- pip

## Running Locally

### Clone the repo

```bash
git clone https://github.com/bristolhackspace/website-django-cms.git

cd website-django-cms
```

### Set virtual environment

Ensure you are in the project root and create a virtual environment.

Select a Python 3.11 version, first check what versions are installed:

```bash
pyenv versions
  system
  3.10.13
* 3.11.8 (set by /Users/username/.pyenv/version)
  3.12.2
```

Install a Python 3.11 version if one is not listed:

```bash
pyenv local 3.11.8
python --version
```

create the virtual environment:

```bash
python -m venv .venv

# Activate it (macOS/Linux)
source .venv/bin/activate

# or on Windows PowerShell
# .venv\Scripts\Activate.ps1

# Update pip
pip install --upgrade pip
```

### Install the project

From the project root:

```bash
pip install -r requirements.txt
```

### Configure CMS environment variables

```bash
# On macOS/Linux (bash/zsh)
export DJANGO_SECRET_KEY="mysupersecretkeyremainsjustthat"

# On Windows PowerShell
# $env:DJANGO_SECRET_KEY = "mysupersecretkeyremainsjustthat"
```

### Run the development server

Ensure you are in the root of the project (the same folder as manage.py) and your virtual environment is activated.

First apply database migrations (Django CMS needs these on first run):

```bash
python manage.py migrate
```

Then start the development server:

```bash
python manage.py runserver
```

With the server running, open a browser and navigate to:

```bash
http://127.0.0.1:8000/
```

To access the Django CMS admin panel:

```bash
http://127.0.0.1:8000/admin/
```

If this is the first time running the CMS, you may need to create a super user:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin login.
