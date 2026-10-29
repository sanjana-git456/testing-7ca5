from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    mrn = Column(String, unique=True) # Medical Record Number
    discharge_date = Column(DateTime, default=datetime.datetime.utcnow)
    procedure_type = Column(String)
    risk_score = Column(Float, default=0.0)
    hospital_id = Column(Integer, ForeignKey("users.id"))
    
    checkins = relationship("CheckIn", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")

class CheckIn(Base):
    __tablename__ = "checkins"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    pain_level = Column(Integer) # 1-10
    temperature = Column(Float)
    redness = Column(Boolean, default=False)
    shortness_of_breath = Column(Boolean, default=False)
    notes = Column(Text, nullable=True)
    
    patient = relationship("Patient", back_populates="checkins")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    scheduled_time = Column(DateTime)
    status = Column(String, default="scheduled") # scheduled, completed, missed
    location = Column(String)
    
    patient = relationship("Patient", back_populates="appointments")

class EducationMaterial(Base):
    __tablename__ = "education_materials"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    procedure_type = Column(String)
    video_url = Column(String)
    content = Column(Text)