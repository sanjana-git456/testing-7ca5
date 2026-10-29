from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access: str
    user: User

class LoginRequest(BaseModel):
    username: str
    password: str

class CheckInBase(BaseModel):
    pain_level: int
    temperature: float
    redness: bool
    shortness_of_breath: bool
    notes: Optional[str] = None

class CheckInCreate(CheckInBase):
    patient_id: int

class CheckIn(CheckInBase):
    id: int
    timestamp: datetime
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    scheduled_time: datetime
    location: str

class Appointment(AppointmentBase):
    id: int
    status: str
    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    mrn: str
    procedure_type: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    discharge_date: datetime
    risk_score: float
    checkins: List[CheckIn] = []
    appointments: List[Appointment] = []
    class Config:
        from_attributes = True

class EducationMaterial(BaseModel):
    id: int
    title: str
    procedure_type: str
    video_url: str
    content: str
    class Config:
        from_attributes = True

class AnalyticsSummary(BaseModel):
    total_patients: int
    high_risk_count: int
    adherence_rate: float
    readmission_estimate: float