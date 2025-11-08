import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

app = _fastapi.FastAPI()

@app.post("/api/contacts", response_model=_schemas.Contact)
async def create_contact(
    contact: _schemas.CreateContact, 
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_contact(contact=contact, db=db)

@app.get("/api/contacts/{contact_id}", response_model=_schemas.Contact)
def get_contact(
    contact_id: int, 
    db: Session = Depends(_services.get_db)
):
    return _services.get_contact(contact_id, db)

@app.get("/api/contacts", response_model=List[_schemas.Contact])
def get_contacts(db: Session = Depends(_services.get_db)):
    rows = _services.list_contacts(db)
    return [_schemas.Contact.model_validate(r) for r in rows]


