from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base, SessionLocal
from .routers import auth, patients, checkins, analytics, education
from . import crud, config

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DischargeGuard API")

# CORS
origins = config.settings.CORS_ORIGINS.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seed data on startup
db = SessionLocal()
crud.seed_data(db)
db.close()

app.include_router(auth.router, prefix="/api")
app.include_router(patients.router, prefix="/api")
app.include_router(checkins.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(education.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "DischargeGuard API is running"}