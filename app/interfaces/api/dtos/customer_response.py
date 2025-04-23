from pydantic import BaseModel

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    address: str
    tax_id: str

    class Config:
        orm_mode = True
