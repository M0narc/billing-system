from app.application.customers.commands.create_customer import CreateCustomerCommand
from app.infrastructure.db.repositories.customer_repository import CustomerRepository

class CreateCustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self, command: CreateCustomerCommand):
        return self.repository.create(
            name=command.name,
            email=command.email,
            address=command.address,
            tax_id=command.tax_id
        )
