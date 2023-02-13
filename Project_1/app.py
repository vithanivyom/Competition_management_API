#Import all routes

from fastapi import FastAPI
from Project_1.Competition.routes import competition
from Project_1.Entry.routes import entry
from Project_1.User.routes import user

app = FastAPI()

app.include_router(competition, tags = ["competition"])
app.include_router(entry, tags = ["entry"])
app.include_router(user, tags = ["user"])