# Tubaraozinho Project Setup Guide

This guide will help you set up the Tubaraozinho project on both Windows and Linux distributions using Pipenv.

## Prerequisites

1. **Python 3.12 or later**
2. **Pip**
3. **Pipenv**

## Setting Up the Project

### Windows

1. **Install Python 3.12 or later**

   Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. **Install Pipenv**

   Open Command Prompt and run:

   ```bash
   pip install pipenv
   ```

3. **Clone the Repository**

   Navigate to the directory where you want to clone the repository and run:

   ```bash
   git clone https://github.com/lucapcf/tubaraozinho.git
   cd tubaraozinho
   ```

4. **Install Dependencies**

   ```bash
   pipenv install
   ```

5. **Activate the Virtual Environment**

   ```bash
   pipenv shell
   ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

### Linux

1. **Install Python 3.12 or later**

   On Ubuntu or Debian-based distributions:

   ```bash
   sudo apt update
   sudo apt install python3.12 python3.12-venv python3.12-dev
   ```

   On Fedora-based distributions:

   ```bash
   sudo dnf install python3.12 python3.12-venv python3.12-dev
   ```

2. **Install Pipenv**

   ```bash
   pip install pipenv
   ```

3. **Clone the Repository**

   Navigate to the directory where you want to clone the repository and run:

   ```bash
   git clone https://github.com/your-username/tubaraozinho.git
   cd tubaraozinho
   ```

4. **Install Dependencies**

   ```bash
   pipenv install
   ```

5. **Activate the Virtual Environment**

   ```bash
   pipenv shell
   ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

## Notes

- Ensure that your database configuration is correctly set up in `settings.py`.
- If you encounter any issues, please refer to the Django documentation or open an issue on the project's GitHub repository.

---