from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserProfileCreate):
    db_user = models.UserProfile(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.UserProfile).filter(models.UserProfile.id == user_id).first()

def delete_user(db: Session, user_id: int):
    db.query(models.UserProfile).filter(models.UserProfile.id == user_id).delete()
    db.commit()
