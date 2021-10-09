# django-todo-app

Install and Create New Virtual Environment
    
    pip install virtualenv 
    virtualenv myenv (your virtual name)

    go to project directory: 
    .\myenv\Scripts\active.ps1 (on Windows)

Install Django 
   
     pip install django

Start Project

    django-admin startproject todo_project

Start Django App

    python manage.py startapp todo_app

Create todo_app Database

    python manage.py makemigrations
    python manage.py migrate
    python manage.py showmigrations

Starting the web server
    
    python manage.py runserver











