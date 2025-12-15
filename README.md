# Blog App - Django
## Introduction
This is a simple blog application built with *Django* as part of a personal study project. \
The goal of this project was to learn and implement the core concepts of Django, \
including models, views, templates, forms, and the Django admin interface.

## Features
- **Post Creation**: Create, edit, and delete blog posts.
- **Post Listing**: View a list of all blog posts.
- **Post Detail**: View the details of a specific blog post.
- **User Authentication**: Register, login, and logout for user management.
- **Admin Interface**: Easy management of posts via Django’s built-in admin interface (I haven't turned off debug mode because this is a learning oriented project).

## Technologies Used
- **Django**
- **SQLite**
- **Bootstrap 5**
- **HTML, CSS, JS (ECMAScript)**

## Requirements and Installation Guide
To run this project, you need to have the following installed:
- Python 3.13

To setup the project from this repo:
1. Clone the repository:
  ```git clone https://github.com/Rohak-Git-Gud/Blog-App-2-Django.git```
2. Navigate into the project directory:
  ```cd first_django_project```
3. Set up the virtual environment (optional but recommended):
  ```python -m venv .venv```
4. Activate the virtual environment:
    - On **Windows**:
      ```.venv\Scripts\activate```
    - On **macOS/Linux**:
      ```source .venv/bin/activate```
5. Install the project dependencies:
    ```pip install -r REQUIREMENTS.txt```
6. Apply database migrations:
    ```python manage.py migrate```
7. Run the development server:
    ```python manage.py runserver [-p <PORT_NUMBER>]```
8. Open your browser and go to `http://127.0.0.1:<PORT_NUMBER>/` to see the blog app in action.

## Implementable Improvements

- Adding Email Verification and Password Reset flows.
- Addition of a comment model with integration to the existing blog model.
- Enhancing the UI with TailwindCSS and/or ShadCN.

---
> **Courtesy**: [Corey Schafer](https://www.youtube.com/@coreyms).
---
