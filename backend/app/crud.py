from sqlalchemy.orm import Session
from . import models, schemas, security
import datetime

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = security.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_patients(db: Session, hospital_id: int):
    return db.query(models.Patient).filter(models.Patient.hospital_id == hospital_id).all()

def create_patient(db: Session, patient: schemas.PatientCreate, hospital_id: int):
    db_patient = models.Patient(**patient.model_dump(), hospital_id=hospital_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def create_checkin(db: Session, checkin: schemas.CheckInCreate):
    db_checkin = models.CheckIn(**checkin.model_dump())
    db.add(db_checkin)
    
    # Update patient risk score based on checkin
    patient = db.query(models.Patient).filter(models.Patient.id == checkin.patient_id).first()
    score = 0.0
    if checkin.pain_level > 7: score += 40
    if checkin.temperature > 38.5: score += 30
    if checkin.redness: score += 20
    if checkin.shortness_of_breath: score += 50
    patient.risk_score = min(score, 100.0)
    
    db.commit()
    db.refresh(db_checkin)
    return db_checkin

def get_education(db: Session, procedure_type: str = None):
    query = db.query(models.EducationMaterial)
    if procedure_type:
        query = query.filter(models.EducationMaterial.procedure_type == procedure_type)
    return query.all()

def seed_data(db: Session):
    if db.query(models.EducationMaterial).count() == 0:
        materials = [
            models.EducationMaterial(title="Knee Replacement Recovery", procedure_type="Orthopedic", video_url="https://www.youtube.com/embed/dQw4w9WgXcQ", content="Keep the incision dry and perform daily exercises."),
            models.EducationMaterial(title="Post-Cardiac Care", procedure_type="Cardiac", video_url="https://www.youtube.com/embed/dQw4w9WgXcQ", content="Monitor your heart rate and avoid heavy lifting."),
            models.EducationMaterial(title="General Wound Care", procedure_type="General", video_url="https://www.youtube.com/embed/dQw4w9WgXcQ", content="Change bandages every 24 hours.")
        ]
        db.add_all(materials)
        db.commit()