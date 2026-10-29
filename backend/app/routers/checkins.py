from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/checkins", tags=["checkins"])

@router.post("/", response_model=schemas.CheckIn)
def create_checkin(checkin: schemas.CheckInCreate, db: Session = Depends(database.get_db)):
    return crud.create_checkin(db, checkin)