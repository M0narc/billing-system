from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound
from app.infrastructure.db.repositories.customer_repository import CustomerRepository
from app.application.customers.commands.update_customer import UpdateCustomerCommand
from app.infrastructure.db.models.customer_models import CustomerModel

class UpdateCustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, customer_id: int, command: UpdateCustomerCommand) -> CustomerModel:
        try:
            existing_email = self.repository.get_by_email(command.email)
            if existing_email:
                raise HTTPException(status_code=400, detail="Email already exists")
            return self.repository.update(
                customer_id=customer_id,
                name=command.name,
                email=command.email,
                address=command.address,
                tax_id=command.tax_id
            )
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Customer not found")
