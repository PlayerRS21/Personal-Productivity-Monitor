🚀 Personal Productivity Monitor

A lightweight CLI-based productivity tracking application built with Python and MySQL/MariaDB.

The goal of this project is to build a real productivity tool while progressively learning and applying:

- 🐍 Python
- 🗄️ SQL & Database Design
- 🔐 Authentication & Security
- 🧠 Logic Building
- 🐙 Git & GitHub
- 🐧 Linux
- 🏗️ Software Architecture
- 📊 Data Analysis
- 🌐 Backend Development

This project is being developed progressively from a simple CLI application toward a more complete productivity platform.

---

📌 Current Status

V1 — Completed ✅

V2 — Time & Session Tracking 🚧

The application currently provides user authentication, task management, SQL CRUD operations, searching, task updates/deletion, and productivity statistics.

---

✨ V1 Features

👤 User Management

- User registration
- User login
- Logout
- Unique username validation
- Unique email validation
- Last-login tracking

«⚠️ Passwords are currently stored without hashing. Secure password hashing is intentionally planned for a later security-focused stage.»

---

📋 Task Management

Users can:

- Create tasks
- Assign categories
- View previous tasks
- Update task names
- Change task categories
- Delete tasks
- Search tasks by name
- Search tasks by category

📚 Available Categories

Python
DSA
SQL
C++
Projects
Linux
College Work
Other

---

⏱️ Basic Time Tracking

V1 already records the time spent working on a task.

The application:

1. Starts a task timer
2. Records the start time
3. Waits for the user to finish
4. Records the end of the session
5. Calculates the elapsed duration
6. Stores the duration in the database

Time is measured using Python's timing functionality rather than relying on a manually incremented counter.

---

📊 Productivity Statistics

The application can calculate productivity time based on task categories.

Example:

--------------------------------
Total Productivity

Python        2h 35m
DSA           1h 20m
SQL             45m
Projects      3h 10m
--------------------------------
Total         7h 50m

---

🛠️ Tech Stack

Technology| Purpose
Python| Application logic
MySQL / MariaDB| Database
mysql-connector-python| Python → MySQL connection
Git| Version control
GitHub| Source control & project management
Linux| Development environment

---

🏗️ Project Structure

Personal-Productivity-Monitor/
│
├── main.py
│
├── database.py
├── login.py
├── register.py
├── router.py
├── startTask.py
├── viewTask.py
├── updateTask.py
├── deleteTask.py
├── searchTask.py
├── statistics.py
│
├── README.md
└── ...

«The exact file structure may evolve as the project grows.»

The application is intentionally divided into separate modules instead of keeping the entire program inside a single Python file.

---

🗄️ Current Database Design

The current version uses a relational database with tables for users and tasks.

Users

users
----------------
id
username
email
password
created_at
last_login

Tasks

tasks
----------------
id
task_name
category
user_id
created_at
total_time

The task records are associated with the user who created them.

---

🔐 Security

Security is an ongoing part of the project.

Currently implemented

- Parameterized SQL queries in the application
- User-specific task association
- Database-level uniqueness for usernames/emails

Not implemented yet

- Password hashing
- Password reset system
- Strong password policy
- Session/token-based authentication
- Advanced authorization

Password hashing will be implemented in a later stage using an appropriate password-hashing algorithm.

---

🚧 V2 — Time & Session Tracking

Status: Planned

V2 will improve the current basic timing system by introducing a proper session-based data model.

The main idea is to separate:

«Task = What you are working on»

from:

«Session = When you actually worked on it»

Planned V2 Features

- [ ] Create productivity sessions
- [ ] Start a session
- [ ] Stop a session
- [ ] Store "started_at"
- [ ] Store "ended_at"
- [ ] Store "duration_seconds"
- [ ] Associate sessions with tasks
- [ ] Associate sessions with categories
- [ ] View session history
- [ ] View today's productivity
- [ ] Daily statistics
- [ ] Weekly statistics
- [ ] Prevent multiple active sessions
- [ ] Recover interrupted sessions
- [ ] Edit sessions
- [ ] Delete sessions
- [ ] Improved date/time handling
- [ ] SQL aggregation using "SUM()", "GROUP BY", "ORDER BY", etc.

---

🗃️ Planned V2 Database Model

V2 is expected to introduce a dedicated session table.

users
  │
  ├──────── tasks
  │            │
  │            └──────── sessions
  │
  └──────── sessions

Possible session structure:

sessions
----------------
id
user_id
task_id
started_at
ended_at
duration_seconds
status
created_at

This will allow one task to have multiple independent work sessions.

Example:

Task: Learn Python

Session 1 → 18:00 - 19:00 → 60 min
Session 2 → 20:00 - 20:45 → 45 min
Session 3 → 21:30 - 22:15 → 45 min

Total → 2h 30m

---

🐧 V3 — Automatic Linux Activity Tracking

Status: Planned

The application will eventually be able to detect activity on the Linux desktop rather than requiring everything to be manually started.

Possible features:

- [ ] Active-window detection
- [ ] Application detection
- [ ] Background monitoring
- [ ] Linux daemon/service
- [ ] Automatic activity logging
- [ ] Manual override
- [ ] Idle-time detection

The automatic tracking system will be designed only after the manual session system is reliable.

---

🤖 V4 — Activity Classification

Status: Planned

The application may eventually classify detected activity into productivity categories.

Example:

VS Code
    ↓
Programming
    ↓
Python

Possible features:

- [ ] Application classification
- [ ] Website classification
- [ ] User-defined rules
- [ ] Custom categories
- [ ] Classification history
- [ ] Manual correction

---

📊 V5 — Advanced Analytics

Status: Planned

The statistics system will eventually become more advanced.

Possible features:

- [ ] Daily productivity trends
- [ ] Weekly productivity trends
- [ ] Monthly productivity trends
- [ ] Category distribution
- [ ] Productivity averages
- [ ] Most productive hours
- [ ] Productivity streaks
- [ ] Long-term historical analysis
- [ ] Charts and visualizations

---

🎯 V6 — Goals & Habits

Status: Planned

Users will eventually be able to set productivity goals.

Possible features:

- [ ] Daily goals
- [ ] Weekly goals
- [ ] Category-specific goals
- [ ] Streak tracking
- [ ] Goal progress
- [ ] Achievement system
- [ ] Productivity reminders

---

🌐 V7 — FastAPI Backend

Status: Planned

The CLI application may eventually be converted into a backend service.

Possible technologies:

- FastAPI
- REST API
- Pydantic
- SQLAlchemy
- Authentication
- API documentation

Possible endpoints:

POST   /auth/register
POST   /auth/login

GET    /tasks
POST   /tasks
PUT    /tasks/{id}
DELETE /tasks/{id}

GET    /sessions
POST   /sessions
PUT    /sessions/{id}
DELETE /sessions/{id}

GET    /statistics

---

🖥️ V8 — Web Dashboard

Status: Planned

A web interface can eventually be built on top of the backend.

Possible features:

- [ ] Dashboard
- [ ] Task management
- [ ] Live session timer
- [ ] Session history
- [ ] Productivity charts
- [ ] Daily/weekly/monthly analytics
- [ ] Goal tracking
- [ ] Account settings

---

☁️ V9 — Cloud & Multi-Device Support

Status: Planned

Potential future features:

- [ ] Cloud database
- [ ] User accounts
- [ ] Multi-device synchronization
- [ ] Secure API authentication
- [ ] Backup and restore
- [ ] Mobile-friendly interface

---

🏢 V10 — Production / SaaS

Status: Long-Term Goal

The long-term goal is to turn the project into a production-quality productivity platform.

Potential areas:

- [ ] Production deployment
- [ ] Secure authentication
- [ ] Password hashing
- [ ] Role-based authorization
- [ ] Automated testing
- [ ] CI/CD
- [ ] Logging
- [ ] Monitoring
- [ ] Error tracking
- [ ] Database migrations
- [ ] API rate limiting
- [ ] Privacy controls
- [ ] Data export
- [ ] Subscription/business model

---

🧪 Development Philosophy

This project is intentionally being developed in stages.

Instead of immediately building a large application, each version focuses on a specific set of engineering concepts.

V1
Python + SQL + CRUD
        ↓
V2
Database Modeling + Time Tracking
        ↓
V3
Linux + System Monitoring
        ↓
V4
Classification + Automation
        ↓
V5
Analytics
        ↓
V6
Goals + Habits
        ↓
V7
FastAPI + Backend
        ↓
V8
Web Application
        ↓
V9
Cloud + Multi-device
        ↓
V10
Production / SaaS

The purpose is not just to add features.

Each version should introduce new engineering concepts and improve the quality of the previous version.

---

🧠 What I'm Learning Through This Project

This project is being used as a practical learning environment for:

Python

- Functions
- Classes
- Modules
- Exceptions
- File structure
- Application state
- Date/time handling
- Database integration

SQL

- CRUD
- SELECT
- INSERT
- UPDATE
- DELETE
- WHERE
- LIKE
- JOIN
- GROUP BY
- ORDER BY
- Aggregate functions
- Relational database design

Software Engineering

- Modular architecture
- Separation of concerns
- Input validation
- Error handling
- Security
- Maintainability
- Refactoring
- Version control
- Documentation

Linux

- CLI applications
- Shell usage
- Process management
- System monitoring
- Background services
- Desktop activity detection

---

🐛 Known Limitations

This project is still under active development.

Current limitations include:

- Passwords are not hashed yet
- CLI-only interface
- No automatic activity detection
- No cloud synchronization
- No web dashboard
- Limited automated testing
- Authentication is not production-grade yet

These limitations are intentionally being addressed progressively through future versions.

---

🔮 Future Direction

The ultimate goal is to evolve this from a simple CLI learning project into a complete productivity platform.

The project may eventually combine:

Manual Tracking
      +
Automatic Activity Detection
      +
Task Management
      +
Analytics
      +
Goals
      +
FastAPI
      +
Web Dashboard
      +
Cloud Sync

while keeping the application lightweight and privacy-conscious.

---

🐙 Git Workflow

Development is managed using Git and GitHub.

Typical workflow:

git status

git add .

git commit -m "Describe your change"

git push

Major versions will be developed incrementally rather than rebuilding the project from scratch.

---

🤝 Contributing

This is currently a personal learning project, but suggestions, bug reports, and constructive feedback are welcome.

If you find a bug:

1. Check whether it has already been reported.
2. Open an issue.
3. Explain the steps to reproduce it.
4. Include the expected and actual behavior.
5. Include relevant error messages if available.

---

📜 License

License information will be added as the project moves toward a more mature release.

---

👨‍💻 Author

Ritesh Saini

BSc Artificial Intelligence & Machine Learning Student

GitHub: "PlayerRS21" (https://github.com/PlayerRS21)

---

⭐ Project Status

V1  ████████████████████  COMPLETE
V2  █████░░░░░░░░░░░░░░░  PLANNED
V3  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V4  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V5  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V6  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V7  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V8  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V9  ░░░░░░░░░░░░░░░░░░░░  PLANNED
V10 ░░░░░░░░░░░░░░░░░░░░  LONG-TERM

«Build it. Break it. Understand it. Refactor it. Repeat.»
