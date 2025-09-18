from fastapi import FastAPI
from .routers import trips, travellers
from .database import init_db
app = FastAPI(title="MomDadGo")

# routers include karna
app.include_router(trips.router)
app.include_router(travellers.router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to MomDadGo!"}

