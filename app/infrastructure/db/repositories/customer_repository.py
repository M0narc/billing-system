from app.infrastructure.db.models.customer_models import CustomerModel
from sqlalchemy.orm import Session


class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> CustomerModel | None:
        return self.db.query(CustomerModel).filter(CustomerModel.email == email).first()

    def create(self, name: str, email: str, address: str, tax_id: str) -> CustomerModel:
        customer = CustomerModel(name=name, email=email, address=address, tax_id=tax_id)
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer

    def get_all(self) -> list:
        return self.db.query(CustomerModel).all()
