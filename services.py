from typing import TYPE_CHECKING

import database as _database
import models as _models
import schemas as _schemas

from sqlalchemy.orm import Session
from fastapi import HTTPException

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try: 
        yield db
    finally:
        db.close()

async def create_contact(
        contact: _schemas.CreateContact, 
        db: "Session"
) -> _schemas.Contact:
    contact = _models.Contact(**contact.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)

    return _schemas.Contact.model_validate(contact)

def list_contacts(db: "Session"):
    return db.query(_models.Contact).order_by(_models.Contact.id.desc()).all()

def _get_contact_or_404(contact_id: int, db: "Session") -> _models.Contact:
    obj = db.get(_models.Contact, contact_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Contact not found")
    return obj

def get_contact(contact_id: int, db: "Session") -> _schemas.Contact:
    obj = _get_contact_or_404(contact_id, db)
    return _schemas.Contact.model_validate(obj)