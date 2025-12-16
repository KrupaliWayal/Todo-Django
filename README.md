# Multi User Todo Application using Django
A simple and efficient multi-user Todo application built using **Django**, where each user can manage their own tasks securely with full CRUD functionality and persistent data storage.

## Screenshots
![Screenshot 1](https://github.com/KrupaliWayal/Todo-Django/blob/main/todo/static/js/Screenshot%20(24).png) 
![Screenshot 2](https://github.com/KrupaliWayal/Todo-Django/blob/main/todo/static/js/Screenshot%20(25).png)
![Screenshot 3](https://github.com/KrupaliWayal/Todo-Django/blob/main/todo/static/js/Screenshot%20(26).png)

## Project Overview
- This project is a **multi-user Todo management system** developed using the Django framework.  
It allows users to **sign up, log in, and manage their personal todo list independently**.
- Each user has access only to their own tasks, and all data is securely stored in the database, ensuring that task history is preserved even after logging out and logging in again.

## Description
This project is a multi-user todo application built using Django. It allows users to create, manage, and track their tasks in a collaborative environment. 

## Features
- User registration and authentication
- Create, edit, and delete tasks
- Assign tasks to specific users
- Mark tasks as completed
- Filter tasks based on status, priority, etc.


## Installation
1. Clone the repository: `git clone https://github.com/KrupaliWayal/Todo-Django.git`
2. Navigate to the project directory: `cd todo`
3. Install dependencies: `pip install django`
4. Apply database migrations: `python manage.py makemigrations`and `python manage.py migrate`
5. Create a superuser(optional): `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## Usage
1. Open your browser and go to: `http://localhost:8000/`
2. Sign up as a new user or log in with existing credentials
3. Create, update, or delete your todo tasks
4. Log out and log in again — your task history remains intact

## Project Highlights
1. Clean separation of user data
2. Beginner-friendly Django project structure
3. Real-world CRUD functionality
4. Suitable for internships and learning backend fundamentals

## Contributing
If you'd like to contribute to this project, follow these steps:
1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes
4. Push to the branch
5. Create a pull request

## Author
Developed as a hands-on Django project to understand authentication, database operations, and CRUD functionality.

