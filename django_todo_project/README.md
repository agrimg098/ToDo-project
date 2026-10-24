# Taskflow — Todo List Web App (Django)

A beginner-friendly task management web application built with **Python and Django**. It is based on the Todo Web Application project listed in the GeeksforGeeks Django Projects collection, with a custom interface and a few extra features. The reference project describes creating, editing, and deleting tasks with Django views, templates, static CSS, and CSRF-protected POST forms. [GeeksforGeeks Django Projects](https://www.geeksforgeeks.org/python/django-projects/)

## Features

- Add a task and validate that its title is not blank.
- View all tasks and when each task was created.
- Edit a task title.
- Mark tasks complete or incomplete.
- Delete an individual task.
- Clear all completed tasks at once.
- View total, pending, and completed task counts.
- Use Django's SQLite database and CSRF protection.
- Load example data using a custom Django management command.
- Responsive layout for desktop and mobile screens.

## Technology used

- Python
- Django
- SQLite (Django's default local database)
- HTML and CSS
- Django Template Language

## Project structure

```text
django_todo_project/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── todo/
│   ├── migrations/
│   ├── management/commands/seed_tasks.py
│   ├── templates/todo/list.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
└── static/css/style.css
```

The `migrations/` folder is created after running `makemigrations` for the first time. The local `db.sqlite3` database is intentionally excluded from Git; run migrations and seed the sample data on the computer where the project is demonstrated.

## Setup and run (Windows PowerShell)

Make sure Python is installed. Open PowerShell in the folder that contains `manage.py`.

1. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

2. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can use Command Prompt instead and run `.venv\Scripts\activate.bat`, or continue with `.venv\Scripts\python.exe` for each Python command.

3. Install Django:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create the database tables:

   ```powershell
   python manage.py makemigrations todo
   python manage.py migrate
   ```

5. Add demonstration tasks:

   ```powershell
   python manage.py seed_tasks
   ```

   Run the seed command again safely if needed; it avoids adding duplicate example titles.

6. Start the local server:

   ```powershell
   python manage.py runserver
   ```

7. Open **http://127.0.0.1:8000/** in your browser. Keep the terminal running while demonstrating the app. Press `Ctrl+C` in the terminal to stop the server.

## Upload to GitHub

1. Create a new **public** repository on GitHub, for example `django-taskflow-todo`. Do not initialize it with a README because this project already has one.
2. Open a terminal in this project folder (the same folder as `manage.py`).
3. Run the following commands, replacing the example URL with your repository's actual URL:

   ```powershell
   git init
   git add .
   git commit -m "Build Django Taskflow todo app"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/django-taskflow-todo.git
   git push -u origin main
   ```

If Git asks you to identify yourself, set your Git name and email using `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`. GitHub may ask you to sign in through your browser. Never upload passwords, tokens, or private credentials.

Before pushing, check `git status`. The `.gitignore` excludes your local virtual environment and database file; the source code, templates, CSS, and README should be committed.

## How the application works

1. **URL routing:** `todo_project/urls.py` sends the root URL to `todo.urls`.
2. **Model:** `Todo` in `todo/models.py` defines the database fields: task title, completion status, and creation timestamp.
3. **View:** `todo/views.py` receives browser requests, validates form values, and uses Django's ORM to create, update, query, or delete records.
4. **Template:** `todo/templates/todo/list.html` displays task data using Django Template Language and submits forms to the views.
5. **Static CSS:** `static/css/style.css` controls the page layout and visual design.
6. **Database:** SQLite stores tasks locally. Django migrations create the table from the model.
7. **CSRF protection:** Each POST form includes `{% csrf_token %}` so Django can verify form submissions.

## Suggested classroom demonstration

1. Open the app and point out the task summary and empty state (if no tasks exist).
2. Add a task, such as `Study Django models`.
3. Edit the task title.
4. Mark it complete and show the summary counts changing.
5. Add another task and delete it.
6. Use **Clear completed** to remove completed tasks.
7. Refresh the page to show that tasks persist in the database.

## Viva / oral questions to prepare

**1. What is Django?**  
Django is a Python web framework that helps build web applications with features such as URL routing, database models, templates, and security middleware.

**2. What is an app in Django?**  
A project is the overall website configuration; an app is a module that handles one area of functionality. Here, `todo` handles task management.

**3. What is a model?**  
A model is a Python class that describes stored data. Django maps the `Todo` model to a database table.

**4. What is a migration?**  
A migration records a change to the database schema. `makemigrations` creates migration files and `migrate` applies them.

**5. What is a view?**  
A view processes a request and returns a response, often by reading or changing model data and rendering a template.

**6. What is the Django ORM?**  
The Object-Relational Mapper lets Python code query and change database records without writing raw SQL for ordinary operations.

**7. Why use POST for changing data?**  
POST is used for actions that change server-side data. GET requests should generally be safe and not delete or update records.

**8. What does `{% csrf_token %}` do?**  
It adds a token that Django checks on POST requests to help protect against cross-site request forgery.

**9. What does `get_object_or_404()` do?**  
It retrieves an object by its identifier, or returns an HTTP 404 response if it does not exist.

**10. Why use SQLite?**  
SQLite is easy to set up and works well for a small local demonstration because it stores the database in a file.

**11. What is the purpose of `seed_tasks`?**  
It is a custom management command that inserts example tasks so the application can be demonstrated with sample data.

**12. What would you improve next?**  
Add user accounts so each user has a private task list, task due dates and priorities, automated tests, and deployment configuration with production security settings.

## Important note

This is a local classroom project, not a production deployment. Before deploying publicly, use an environment variable for `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and review Django's deployment checklist.
