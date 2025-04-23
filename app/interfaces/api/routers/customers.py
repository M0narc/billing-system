from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.application.customers.commands.create_customer import CreateCustomerCommand
from app.infrastructure.db.repositories.customer_repository import CustomerRepository
from app.application.customers.use_cases.create_customer_service import CreateCustomerService

router = APIRouter()

@router.post("/customers")
def create_customer(command: CreateCustomerCommand, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CreateCustomerService(repo)
    customer = service.execute(command)
    return {"id": customer.id, "message": "Customer created successfully"}
