from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(prefix="/education", tags=["education"])

@router.get("/", response_model=List[schemas.EducationMaterial])
def get_materials(procedure_type: str = None, db: Session = Depends(database.get_db)):
    return crud.get_education(db, procedure_type)