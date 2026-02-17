from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base

# import routers
from app.routes import auth, users, students, profiles, classes_subjects, exams, fees, parents, attendance, timatable

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/")
def root():
	return {"message": "School Management System API"}


def include_routers():
	app.include_router(auth.router, prefix="/auth", tags=["Auth"])
	app.include_router(users.router)
	app.include_router(students.router)
	app.include_router(profiles.router)
	app.include_router(classes_subjects.router)
	app.include_router(exams.router)
	app.include_router(fees.router)
	app.include_router(parents.router)
	app.include_router(attendance.router)
	app.include_router(timatable.router)


include_routers()

# create DB tables
Base.metadata.create_all(bind=engine)
