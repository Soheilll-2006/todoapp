Todo App with FastAPI 🚀
Welcome to the Ultimate Todo App – a blazing-fast, feature-packed task management tool built with FastAPI, SQLAlchemy, and SQLite. This project is your go-to solution for organizing tasks with style and efficiency! 🌟
🌈 Features

Secure User Authentication: Register and log in with ease.
CRUD Power: Create, Read, Update, and Delete todos like a pro.
Priority Levels: Set priorities (0-6) to tackle tasks smartly.
Completion Tracking: Mark tasks as done with a single click.
Health Check: Monitor your app’s heartbeat with /health.

🛠️ Tech Stack

FastAPI: For a lightning-fast API.
SQLAlchemy: Robust database management.
SQLite: Lightweight and reliable storage.
Pydantic: Data validation done right.

🚀 Getting Started
Ready to roll? Follow these steps to launch your own Todo App:

Clone the Repo:
git clone https://github.com/Soheilll-2006/todo-fastapi-new.git
cd todo-fastapi-new


Set Up Environment:
python -m venv venv


Activate it:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate




Install Dependencies:
pip install -r requirements.txt


Run the App:
uvicorn main:app --reload

Open your browser or API client at http://127.0.0.1:8000! 🎉


📋 API Endpoints



Method
Endpoint
Description



POST
/auth/
Register a new user


POST
/auth/token
Login and get token


GET
/todos/
List all todos


POST
/create_todo
Add a new todo


PUT
/update_todo/{id}
Update a todo


DELETE
/delete_todo/{id}
Delete a todo


GET
/health
Check app health


🎨 Contributing
Wanna make this app even cooler? Fork it, tweak it, and send a pull request! Check out our Contribution Guidelines (coming soon).
📜 License
This project is licensed under the MIT License – free to use, modify, and share! (Add your own license file if needed.)
🙌 Acknowledgments
Thanks to the open-source community and the awesome tools that power this project! 💪
