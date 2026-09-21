⚡ Productivity Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</p><p align="center">
  <b>A lightweight productivity and task-tracking application built with Python and SQLite.</b>
</p><p align="center">
  Built from the ground up as a practical project for learning Python, SQL, Git, Linux, software architecture, and eventually production deployment.
</p>---

📌 About The Project

Productivity Tracker is a lightweight productivity management application designed to help users organize tasks, track their work, search previous tasks, and view productivity statistics.

The project started as a Python + SQL learning project, but it is intentionally designed with a longer-term goal:

«Turn the initial CLI application into a complete, production-ready productivity platform.»

The current version focuses on the fundamentals:

- Python programming
- SQL and CRUD operations
- Database design
- User authentication
- Searching and filtering
- Application logic
- Git/GitHub workflow
- Linux development

Future versions will gradually introduce APIs, automatic Linux activity tracking, dashboards, analytics, cloud infrastructure, and potentially a SaaS model.

---

✨ Current Features — V1

The first version is currently functional and includes:

👤 User Management

- User registration
- User login
- Logout
- User-specific task management

📝 Task Management

- Add tasks
- View tasks
- Update task name
- Update task category
- Delete tasks

🔎 Search

- Search tasks by name
- Search tasks by category

📊 Statistics

- View productivity/task statistics
- Calculate useful information from stored data

🗄️ Database

- SQLite database
- Persistent data storage
- CRUD operations
- Relational data handling

---

🖥️ Current Workflow

The current V1 workflow is intentionally simple:

                ┌──────────────┐
                │     User     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    Login /   │
                │   Register   │
                └──────┬───────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Productivity    │
              │     Tracker     │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Add Task     View Tasks    Statistics
          │            │            │
          ▼            ▼            ▼
       Update        Search       Analysis
          │
          ▼
       Delete

---

🛠️ Tech Stack

Technology| Purpose
🐍 Python| Application logic
🗄️ SQLite| Database
🐧 Linux| Development environment
🔀 Git| Version control
🐙 GitHub| Source code management

More technologies will be introduced as the project evolves.

---

🚀 Getting Started

Prerequisites

You need:

- Python 3.x
- Git
- SQLite
- A terminal

Linux is currently the primary development environment.

---

📥 Clone the Repository

git clone https://github.com/PlayerRS21/productivity-tracker.git
cd productivity-tracker

---

🐍 Create a Virtual Environment

python -m venv .venv

Activate it:

source .venv/bin/activate

---

📦 Install Dependencies

If the project has dependencies:

pip install -r requirements.txt

If there are no external dependencies, this step can be skipped.

---

▶️ Run the Application

python main.py

«The exact command may change as the project architecture evolves.»

---

📂 Project Structure

The structure may evolve as new versions are introduced.

A typical structure for the current project is:

productivity-tracker/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── database/
│   └── schema.sql
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── users.py
│   ├── tasks.py
│   └── statistics.py
│
└── tests/

«The actual repository structure may differ depending on implementation decisions.»

---

🗺️ Development Roadmap

The project is being developed incrementally.

The goal is not to jump directly from a CLI application to a massive SaaS platform.

Each version introduces new engineering concepts.

---

✅ V1 — Core Productivity Tracker

Status: Completed

The objective of V1 was to build a functional Python + SQL application and practice fundamental programming concepts.

Completed

- [x] User registration
- [x] User login
- [x] Logout
- [x] Add task
- [x] View tasks
- [x] Update task name
- [x] Update task category
- [x] Delete task
- [x] Search task by name
- [x] Search task by category
- [x] View statistics
- [x] SQLite database
- [x] CRUD operations
- [x] Basic error handling
- [x] Git version control

---

🔨 V2 — Time Tracking

Status: Planned

V2 will introduce actual productivity session tracking.

Instead of simply storing tasks, users will be able to start and stop work sessions.

Planned Features

- [ ] Start productivity session
- [ ] Stop productivity session
- [ ] Record "started_at"
- [ ] Record "ended_at"
- [ ] Calculate session duration
- [ ] Associate sessions with tasks/categories
- [ ] View today's total working time
- [ ] View historical sessions
- [ ] Daily productivity statistics
- [ ] Weekly productivity statistics

Basic Architecture

START SESSION
      │
      ▼
started_at
      │
      ▼
    WORK
      │
      ▼
STOP SESSION
      │
      ▼
ended_at
      │
      ▼
duration = ended_at - started_at
      │
      ▼
   SQLite

The application will initially behave like a database-backed productivity stopwatch.

---

🐧 V3 — Linux Activity Tracking

Status: Planned

The project will eventually become useful as an actual Linux productivity tool.

Instead of requiring the user to manually record everything, the application will be able to observe system activity.

Potential data sources:

- Active application
- Active window
- Window title
- Workspace
- Idle time
- Project directory
- Timestamp

Example:

22:00 → VS Code
22:25 → Firefox
22:40 → Terminal
23:10 → VS Code

The application could then build an activity timeline.

Important

The system will initially record observable computer activity, not pretend that it knows exactly what the user is doing.

For example:

Firefox + Python documentation

does not prove that the user is studying Python.

Later versions may introduce configurable classification rules.

---

🧠 V4 — Activity Classification

Status: Planned

Introduce configurable rules for automatically categorizing detected activity.

Example:

VS Code
PyCharm
Neovim
        ↓
Programming

docs.python.org
github.com
stackoverflow.com
        ↓
Development / Learning

Steam
        ↓
Gaming

Users should eventually be able to create and modify their own rules.

Example:

Domain: youtube.com
Category: Learning

This avoids hard-coding assumptions into the application.

---

📊 V5 — Advanced Analytics

Status: Planned

The statistics system will become significantly more powerful.

Potential features:

- [ ] Daily productivity charts
- [ ] Weekly productivity charts
- [ ] Monthly reports
- [ ] Category distribution
- [ ] Productivity trends
- [ ] Most productive hours
- [ ] Most productive days
- [ ] Time spent per project
- [ ] Time spent per category
- [ ] Productivity streaks
- [ ] Goal completion percentage
- [ ] Historical comparisons

Example:

Weekly Productivity

Mon  ████████████  6h 20m
Tue  █████████     4h 45m
Wed  ███████████   5h 30m
Thu  █████████████ 7h 05m
Fri  ████████      4h 10m

---

🎯 V6 — Goals & Habit System

Status: Planned

Users will be able to create measurable productivity goals.

Example:

Goal: Python
Target: 10 hours/week

Progress:
████████░░  8 / 10 hours

Completion: 80%

Potential features:

- [ ] Daily goals
- [ ] Weekly goals
- [ ] Monthly goals
- [ ] Productivity streaks
- [ ] Goal progress
- [ ] Custom targets
- [ ] Achievement system
- [ ] Reminders

---

🌐 V7 — FastAPI Backend

Status: Planned

The CLI application will eventually evolve into a backend service.

Planned architecture:

                 Client
                   │
                   ▼
              ┌─────────┐
              │ FastAPI │
              └────┬────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Application         Database
        Logic          PostgreSQL/SQLite

Potential API endpoints:

POST   /auth/register
POST   /auth/login

GET    /tasks
POST   /tasks
PATCH  /tasks/{id}
DELETE /tasks/{id}

GET    /sessions
POST   /sessions/start
POST   /sessions/{id}/stop

GET    /statistics
GET    /statistics/daily
GET    /statistics/weekly

---

🖥️ V8 — Web Dashboard

Status: Planned

Build a proper web interface.

Potential dashboard:

┌─────────────────────────────────────────┐
│          PRODUCTIVITY DASHBOARD         │
├─────────────────────────────────────────┤
│                                         │
│  TODAY        THIS WEEK       TOTAL     │
│  4h 32m       27h 15m        183h      │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│        PRODUCTIVITY GRAPH               │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  Programming       ███████████  62%     │
│  Learning          ██████       24%     │
│  Other             ███          14%     │
│                                         │
└─────────────────────────────────────────┘

---

☁️ V9 — Cloud & Multi-Device Support

Status: Planned

Move beyond local-only storage.

Potential features:

- [ ] PostgreSQL
- [ ] Cloud deployment
- [ ] User accounts
- [ ] Secure authentication
- [ ] Data synchronization
- [ ] Multi-device support
- [ ] Backup and restore
- [ ] Account settings

Potential architecture:

Linux Client ──────┐
                   │
Web Dashboard ─────┼──→ API ──→ PostgreSQL
                   │
Mobile Client ─────┘

---

💼 V10 — Production / SaaS Version

Status: Long-term Goal

The ultimate goal is to determine whether this project can become a real product rather than remaining a learning project.

Potential features:

- [ ] Production authentication
- [ ] Secure password hashing
- [ ] Session management
- [ ] Rate limiting
- [ ] API security
- [ ] PostgreSQL
- [ ] Docker
- [ ] CI/CD
- [ ] Automated testing
- [ ] Logging
- [ ] Monitoring
- [ ] Error tracking
- [ ] Cloud deployment
- [ ] Subscription system
- [ ] Free/Pro plans
- [ ] Data export
- [ ] Privacy controls

Possible product model:

FREE
├── Task tracking
├── Basic statistics
└── Limited history

PRO
├── Advanced analytics
├── Unlimited history
├── Automatic activity tracking
├── Goals
├── Reports
├── Cloud synchronization
└── Multi-device support

This is a future product direction, not a current feature.

---

🔐 Privacy

Automatic productivity tracking can involve sensitive information.

Future versions will therefore need to take privacy seriously.

Potential privacy controls:

- Local-only mode
- User-controlled tracking
- Application exclusions
- Domain exclusions
- Pause tracking
- Data deletion
- Data export
- Transparent data collection
- No hidden tracking

The application should never silently collect information that the user did not explicitly agree to provide.

---

🧪 Testing Strategy

Testing will become more comprehensive as the project evolves.

Future testing may include:

- Unit tests
- Integration tests
- Database tests
- API tests
- Authentication tests
- Edge-case testing
- Automated CI testing

Example cases:

Register duplicate user
Invalid login
Invalid task ID
Empty task name
Invalid category
Delete nonexistent task
Unauthorized task access
Invalid database input

---

🐛 Bug Reports & Contributions

If you visit this repository and discover a bug, unexpected behavior, or something that could be improved, please report it.

You can open a GitHub Issue with:

Bug Report Template

## Bug Description

Describe what happened.

## Steps to Reproduce

1.
2.
3.

## Expected Behavior

What should have happened?

## Actual Behavior

What actually happened?

## Environment

OS:
Python version:
Project version:

## Additional Information

Logs, screenshots, or other useful information.

Constructive feedback, bug reports, feature ideas, and technical suggestions are welcome.

If you want to contribute code, feel free to open a Pull Request.

---

🧑‍💻 Development Philosophy

This project is intentionally being developed incrementally.

The philosophy is:

Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Refactor
  ↓
Test
  ↓
Deploy
  ↓
Improve

The project started as a way to practice:

- Python fundamentals
- Logic building
- SQL
- CRUD
- Git
- GitHub
- Linux

The long-term objective is to use the same project to learn:

- Software architecture
- Backend development
- REST APIs
- FastAPI
- PostgreSQL
- Authentication
- Linux system integration
- Testing
- Docker
- CI/CD
- Cloud deployment
- SaaS development

---

📈 Project Evolution

V1
│
├── Python
├── SQLite
├── CRUD
└── CLI
     │
     ▼
V2
│
├── Time Tracking
└── Session Management
     │
     ▼
V3
│
├── Linux Integration
└── Automatic Activity Detection
     │
     ▼
V4
│
└── Activity Classification
     │
     ▼
V5
│
└── Advanced Analytics
     │
     ▼
V6
│
└── Goals & Streaks
     │
     ▼
V7
│
└── FastAPI Backend
     │
     ▼
V8
│
└── Web Dashboard
     │
     ▼
V9
│
└── Cloud + Multi-device
     │
     ▼
V10
│
└── Production / SaaS

---

📜 License

This project is currently under development.

A formal open-source license will be added when the project reaches a stable release.

---

👨‍💻 Author

Ritesh Saini

BSc Artificial Intelligence & Machine Learning Student

GitHub: "@PlayerRS21" (https://github.com/PlayerRS21)

---

<p align="center">
  <b>Built with Python. Powered by curiosity. Evolving one version at a time. ⚡</b>
</p><p align="center">
  ⭐ If you find the project interesting, consider giving the repository a star.
</p>
