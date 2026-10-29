from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models
from ..dependencies import get_current_user
from ..schemas import AnalyticsSummary

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/summary", response_model=AnalyticsSummary)
def get_summary(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    patients = db.query(models.Patient).filter(models.Patient.hospital_id == current_user.id).all()
    total = len(patients)
    high_risk = len([p for p in patients if p.risk_score > 50])
    
    # Mocked metrics for demo
    return {
        "total_patients": total,
        "high_risk_count": high_risk,
        "adherence_rate": 84.5 if total > 0 else 0.0,
        "readmission_estimate": 12.2 if total > 0 else 0.0
    }