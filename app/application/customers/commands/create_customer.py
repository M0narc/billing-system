from pydantic import BaseModel, EmailStr

class CreateCustomerCommand(BaseModel):
    name: str
    email: EmailStr
    address: str
    tax_id: str
