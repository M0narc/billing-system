from pydantic import BaseModel

class CreateCustomerDTO(BaseModel):
    id: int
    name: str
    email: str
    address: str
    tax_id: str

    class Config:
        from_attributes = True
