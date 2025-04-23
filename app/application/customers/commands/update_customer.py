from pydantic import BaseModel, EmailStr
from typing import Optional

class UpdateCustomerCommand(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    tax_id: Optional[str] = None
