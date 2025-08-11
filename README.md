Todo App with FastAPI 🌟
Welcome to the Todo App, a sleek and efficient task management application built with FastAPI, SQLAlchemy, and SQLite. This project helps you manage your tasks with user authentication, priority settings, and a clean API interface.
✨ Features

User registration and secure login
Create, read, update, and delete (CRUD) todo items
Set task priorities (0-6) and track completion status
Health check endpoint for system monitoring

🛠️ Prerequisites

Python 3.8 or higher
Pip (for installing dependencies)

🚀 Installation
Follow these steps to get the app running on your local machine:

Clone the repository:
git clone https://github.com/Soheilll-2006/todo_fastapi.git
cd todo_fastapi


Set up a virtual environment:
python -m venv venv


Activate the virtual environment:

On Unix/Mac: source venv/bin/activate
On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Run the application:
uvicorn main:app --reload

Visit http://127.0.0.1:8000 in your browser or API client!


📋 API Endpoints

POST /auth/: Register a new user
POST /auth/token: Login and get token
GET /todos/: List all todos
GET /todos/{todo_id}: Get a specific todo
POST /create_todo: Add a new todo
PUT /update_todo/{todo_id}: Update a todo
DELETE /delete_todo/{todo_id}: Delete a todo
GET /health: Check app health

