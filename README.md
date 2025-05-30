echo "# TaskMind" > README.md
echo "AI-based task management system built with FastAPI." >> README.md
# TaskMind – AI-Powered Personal Task Assistant 🚀

**TaskMind** is a personal task assistant that helps you create, organize, and manage tasks intelligently. It uses **AI-powered CrewAI agents** to automatically suggest sub-tasks, relevant tags, and deadlines based on your task descriptions.

---

## 🌟 Features

✅ User registration and login with **JWT-based authentication**  
✅ Create, read, update, and delete tasks  
✅ AI suggestions for sub-tasks, tags, and deadlines  
✅ Manage sub-tasks, priorities, and task statuses  
✅ Secure and scalable backend built with **FastAPI**  
✅ Database support: **SQLite** for dev/testing and optional **PostgreSQL** for production  
✅ Tested and published using **Postman**

---

## ⚙️ Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite / PostgreSQL
- **ORM**: SQLModel / SQLAlchemy
- **AI Agents**: CrewAI framework
- **Authentication**: JWT
- **API Testing**: Postman

---

---

## 🔑 Key API Endpoints

- **POST /register** – Register a new user  
- **POST /login** – User login (returns JWT)  
- **POST /tasks** – Create a task  
- **GET /tasks** – List all tasks  
- **GET /tasks/{id}** – Get task by ID  
- **PUT /tasks/{id}** – Update task  
- **DELETE /tasks/{id}** – Delete task  
- **POST /tasks/{id}/suggestions** – Generate AI-based suggestions (sub-tasks, tags, deadline)  

---

## 🧪 Testing with Postman

We used **Postman** to test and publish all API endpoints.  
- Collection includes:
  - User registration & login flow
  - Full CRUD for tasks
  - Testing the AI-powered `/suggestions` endpoint

---

## 🚀 How to Run

1️⃣ **Clone the repo**  
```
git clone https://github.com/YOUR_USERNAME/TaskMind.git
cd TaskMind

---
2️⃣ Create a virtual environment and install dependencies


python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

pip install -r requirements.txt

---
---
3️⃣ Run the FastAPI server

uvicorn app.main:app --reload

---

---

4️⃣ Access the API docs
Visit: http://127.0.0.1:8000/docs
---

---

📄 License
This project is licensed under the MIT License.
---
