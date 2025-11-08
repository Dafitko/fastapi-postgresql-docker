# schemas.py
from pydantic import BaseModel, EmailStr, ConfigDict  # pridaj ConfigDict

class CreateContact(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str

class Contact(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str

    # dôležité: umožní validáciu z ORM inštancie
    model_config = ConfigDict(from_attributes=True)
