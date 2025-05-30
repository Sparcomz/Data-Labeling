# Data Labeling Project

This is a Django-based web application for managing data annotation workflows. The application supports different user roles, including uploaders, annotators, reviewers, and admins, each with specific functionalities.

## Features

- **User Roles**: Manage different user roles with specific permissions.
- **Data Management**: Upload and manage data for annotation tasks.
- **Annotation and Review**: Annotate data and review annotations.
- **Statistics**: Track statistics for tasks completed, approved, and rejected.
- **Admin Actions**: Admins can manage users and override reviews.

## Prerequisites

- Python 3.6+
- Django 3.2+
- PostgreSQL (or SQLite for development)

## Setup Instructions

1. **Clone the Repository**

(please note to update `yourusername` in the url below)

   ```bash
   git clone https://github.com/yourusername/data-labeling.git
   cd data-labeling
   ```

**Project is in development, make sure to switch to the branch - sprint1 before continuing.**

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**

   In the root directory of your project (where manage.py is located), create a file named .env and add the following content, replacing the placeholders with your actual database credentials:
   ```
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   ```

5. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser(Optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application**

   Open your web browser and go to http://127.0.0.1:8000/.

## Usage

- Login and Register: Use your credentials to log in or create new account.
- Upload Data: Navigate to the uploader section to upload new data.
- Annotate and Review: Annotators can annotate data, and reviewers can review annotations.
- Admin Actions: Admins can manage users and perform administrative actions.
