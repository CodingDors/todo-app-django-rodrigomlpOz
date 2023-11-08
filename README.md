# ToDo App Exercise - Django
Welcome to the ToDo App Exercise with Django! In this assignment, you'll create a basic ToDo application using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The goal is to understand how to handle web requests, render dynamic content, and perform CRUD operations.

This exercise is designed to be straightforward, where you'll need to work on the views.py and index.html to bring the ToDo application to life.

Once you have completed your version of the ToDo app, you can compare it with our sample solution, which is available in the files views_answer.py and answer.html.

## Objective:
Your task is to build a Django-based web application that allows users to:

1. Enter a task using a form.
2. View the tasks they've added in a list that gets updated with each new entry.

## Specific Tasks:
You will be responsible for the following:
### Update views.py:
- Create a view to display tasks and handle the submission of new tasks.
- Ensure that new tasks are added to the list and displayed in the index.html template.
### Design index.html:
- Create a form to submit new tasks.
- Ensure there is a list (`<ul>` or `<ol>`) to display the tasks dynamically as they are added.

## Sample Solutions:
If you're stuck or would like to compare your implementation with our version, check the views_answer.py for the view logic and answer.html for the template structure.

## How to Run Your Application:
1. Install the required packages: `pip install -r requirements.txt`
2. Start the Django development server: `python manage.py runserver`
3. Access the application via your web browser at http://127.0.0.1:8000/ or the URL provided by your development environment.

## How to Run Tests:
To make sure your application is working as expected:

1. Stop the server if it's still running (you can use Ctrl+C in the terminal for that).
2. In the root directory of the project, run the following command: `python manage.py test`
