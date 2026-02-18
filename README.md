# School Management System — FastAPI

Small, modular REST API for managing a school's users, students, profiles, classes, exams, fees, parents, attendance and timetables built with FastAPI and SQLAlchemy.

**Status:** Prototype / Development

**Key ideas:** simple, modular routers in `app/routes`, SQLAlchemy models in `app/models`, Pydantic schemas in `app/schemas`, and JWT helpers in `app/utils`.

**Table of Contents**

- **Overview**: What this project provides
- **Tech Stack**: libraries and components used
- **Quickstart**: steps to run locally
- **Configuration**: environment variables and .env example
- **Database**: how the DB is created and default URI
- **API**: where to find interactive docs and main endpoints
- **Development**: common tasks and notes
- **Contributing & License**n+
  **Overview**
- A FastAPI-based backend for a school management system exposing REST endpoints to manage users, students, profiles, classes & subjects, exams, fees, parents, attendance and timetables.
- Router modules are in `app/routes` and are included automatically by `app/main.py`.

**Tech Stack**

- **Framework:** FastAPI
- **DB / ORM:** SQLAlchemy (models in `app/models`) with SQLite by default
- **Data validation:** Pydantic / pydantic-settings
- **Server:** Uvicorn (recommended for development)
- See `requirements.txt` for complete dependency list.

**Quickstart (local)**

1. Create a virtual environment and activate it:

- On Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

2. Create a `.env` file in the project root (see Configuration below).

3. Start the server for development:

- `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

4. Open the interactive API docs in your browser:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

**Configuration (.env)**

- The project uses `pydantic-settings` and reads environment variables from a `.env` file located at the project root.
- Minimum variables required:

- `SQLALCHEMY_DATABASE_URI`: SQLAlchemy connection string (example below)
- `SECRET_KEY`: a secret string for signing tokens
- `ALGORITHM`: JWT algorithm (e.g. `HS256`)

Example `.env` (development)

SQLALCHEMY_DATABASE_URI=sqlite:///./db.sqlite3
SECRET_KEY=replace-this-with-a-secure-random-string
ALGORITHM=HS256

Notes:

- The `app/config.py` looks for `.env` at the repo root.
- If you prefer PostgreSQL or another DB, update `SQLALCHEMY_DATABASE_URI` accordingly. The engine is created in `app/database.py`.

**Database**

- By default the project is configured to use SQLite (`sqlite:///./db.sqlite3`).
- On startup `app/main.py` runs `Base.metadata.create_all(bind=engine)` which creates tables from the SQLAlchemy models automatically. For production or schema migrations, consider integrating Alembic explicitly.

**API Routes (overview)**

- Auth: `/auth` — register, login, password reset/change endpoints
- Users: `/users` — user CRUD and listing (see `app/routes/users.py`)
- Students: `/students` — student management
- Profiles: `/profiles` — profile endpoints
- Classes & Subjects: `/classes-subjects` — classes and subjects management
- Exams: `/exams` — exam records and grades
- Fees: `/fees` — fee records and payments
- Parents: `/parents` — parent records
- Attendance: `/attendance` — record & query attendance
- Timetable: `/timetable` — class timetable endpoints

Each router is defined in `app/routes/*.py` and registered by `app/main.py`.

Authentication

- The project uses JWT-based auth helpers in `app/utils/jwt_handler.py`. Endpoints which require authentication use FastAPI `Depends` to pull the current user.

**Development Notes**

- Use `uvicorn` with `--reload` for rapid development.
- To open an interactive shell against the app models, you can create a small script that imports `app.database` and the model classes.
- If you switch from SQLite to a server-based DB (Postgres/MySQL), update `SQLALCHEMY_DATABASE_URI` and remove `connect_args` if not required.

**Testing**

- The repository includes `pytest` in `requirements.txt`. Add tests under a `tests/` folder and run `pytest` to execute them.

**Contributing**

- Fork the repo, create a feature branch, add tests, and open a pull request describing the change.

**Files of interest**

- App entry: [app/main.py](app/main.py)
- Config: [app/config.py](app/config.py)
- Database setup: [app/database.py](app/database.py)
- Routers: [app/routes](app/routes)
- Models: [app/models](app/models)

**License**

- This project does not include a license by default. Add a `LICENSE` file if you intend to open-source the project.

---

If you want, I can also:

- Add a simple `Makefile` or `docker-compose.yml` for local development
- Add an example Postman / OpenAPI collection
- Add Alembic migration scaffolding and sample migration commands

File: [README.md](README.md)
