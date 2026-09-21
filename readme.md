Productivity Tracker

A lightweight command-line productivity tracker built with Python and SQLite.

The goal of this project is to practice Python fundamentals, SQL CRUD operations, database design, Git/GitHub, Linux development, and basic software engineering while building something that can eventually evolve into a real productivity-tracking application.

Project Status

Version: V1 — Manual Session Tracking
Status: In Development

V1 is intentionally simple. The application works as a manual stopwatch:

1. The user starts a session.
2. The application records the start timestamp.
3. The user works on the selected task.
4. The user stops the session.
5. The application records the end timestamp.
6. The duration is calculated from the two timestamps.
7. The session is stored in SQLite.

The application does not attempt to determine whether the user is actually working.

---

Objectives

This project is being developed to practice:

- Python fundamentals
- Functions and modular programming
- Object-oriented programming where appropriate
- Exception handling
- SQLite and SQL
- CRUD operations
- Database relationships
- Date and time handling
- Input validation
- Git and GitHub
- Linux command-line development
- Project organization
- Testing and debugging

---

Planned Features

V1 — Manual Tracking

- Start a productivity session
- Stop a productivity session
- Record start and end timestamps
- Calculate session duration
- Assign a category to a session
- Add a task description
- Store sessions in SQLite
- View previous sessions
- Update session information
- Delete sessions
- View basic productivity statistics

Future Versions

The project is designed to be extended beyond the initial CLI application.

Possible future features include:

- Automatic Linux activity tracking
- Active-window detection
- Application and website tracking
- Automatic activity classification
- Background tracking daemon
- Productivity dashboard
- FastAPI REST API
- PostgreSQL support
- Web interface
- User authentication
- Goals and productivity streaks
- Weekly/monthly reports
- Data export
- Cloud synchronization
- Multi-device support

---

Example Workflow

$ productivity

========================================
        PRODUCTIVITY TRACKER
========================================

1. Start Session
2. View Sessions
3. Statistics
4. Manage Categories
5. Exit

Enter choice: 1

Category: Python
Task: Practice OOP

Session started.

Elapsed: 00:32:17

Press Ctrl+C to stop...

After stopping:

Session stopped.

Started : 2026-09-21 22:15:31
Ended   : 2026-09-21 22:47:48
Duration: 32m 17s

Save session? [Y/n]

---

How Duration Is Calculated

The application uses timestamps rather than relying on a continuously incremented counter.

duration = ended_at - started_at

For example:

Started : 22:15:31
Ended   : 23:02:43
Duration: 47m 12s

The displayed stopwatch is only for user feedback. The database timestamps are the source of truth.

---

Technology Stack

Current

- Python
- SQLite
- SQL
- Git
- GitHub
- Linux

Planned

- FastAPI
- PostgreSQL
- HTML/CSS/JavaScript or another frontend
- Linux system services/background processes

---

Database

The initial version uses SQLite because it is lightweight and requires no separate database server.

Planned entities include:

Users

Stores user information.

id
username
email
password
created_at

Categories

Stores productivity categories.

id
name
description

Sessions

Stores productivity sessions.

id
user_id
category_id
task
started_at
ended_at
duration
created_at

The exact schema may change during development.

---

CRUD Operations

The application will practice CRUD operations on its database entities.

Operation| Example
Create| Add a productivity session
Read| View previous sessions
Update| Modify session details
Delete| Remove a session

SQL will initially be written and understood directly rather than hiding database operations behind a complex abstraction.

---

Project Structure

The project structure will evolve as development progresses.

The planned initial structure is:

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
│   ├── sessions.py
│   ├── categories.py
│   └── statistics.py
│
└── tests/

The structure may be modified when there is a technical reason to do so.

---

Installation

Clone the repository:

git clone <repository-url>
cd productivity-tracker

Create a Python virtual environment:

python -m venv .venv

Activate it on Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python src/main.py

«Installation and execution instructions will be updated as the project develops.»

---

Development Workflow

Development is performed primarily through the Linux terminal.

Git is used to track development history.

Example commits:

initial project setup
add database schema
implement session creation
implement session listing
add session update
add session deletion
add statistics
improve input validation
update documentation

The repository should contain the development history rather than only the final version.

---

Testing

The application should be tested against normal and invalid input.

Examples:

- Starting a session
- Stopping a session
- Saving a session
- Cancelling a session
- Invalid menu selections
- Invalid session IDs
- Invalid category IDs
- Empty task names
- Database errors
- Updating existing sessions
- Deleting existing sessions
- Viewing sessions when no data exists

Testing will initially be performed manually, with automated tests added as the project matures.

---

Design Philosophy

The first version intentionally avoids unnecessary complexity.

The development strategy is:

Simple CLI
    ↓
Correct Python logic
    ↓
Correct database design
    ↓
CRUD
    ↓
Statistics
    ↓
API
    ↓
Automatic Linux tracking
    ↓
Web application
    ↓
Production-ready product

The objective is to understand each layer before adding the next one.

---

Future Product Direction

The long-term goal is to explore whether the project can evolve from a learning project into a useful productivity product.

Potential users could include:

- Students
- Developers
- Freelancers
- Remote workers

Potential product capabilities could include automatic activity tracking, productivity analytics, goals, reports, synchronization, and multi-device support.

These features are future possibilities, not commitments for V1.

---

License

License to be decided.

---

Author

Ritesh

GitHub: "PlayerRS21" (https://github.com/PlayerRS21)
