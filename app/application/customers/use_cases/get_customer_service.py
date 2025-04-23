from typing import List
from app.infrastructure.db.models.customer_models import CustomerModel
from app.infrastructure.db.repositories.customer_repository import CustomerRepository

class GetCustomersService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def execute(self) -> List[CustomerModel]:
        return self.repository.get_all()
