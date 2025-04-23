from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.application.customers.use_cases.update_customer_service import UpdateCustomerService
from app.core.dependencies import get_db
from app.application.customers.commands.create_customer import CreateCustomerCommand
from app.infrastructure.db.repositories.customer_repository import CustomerRepository
from app.application.customers.use_cases.create_customer_service import CreateCustomerService
from typing import List
from app.application.customers.use_cases.get_customer_service import GetCustomersService
from app.interfaces.api.dtos.customer_response import CreateCustomerDTO
from app.application.customers.commands.update_customer import UpdateCustomerCommand

router = APIRouter()

@router.get("/api/get_customers", response_model=List[CreateCustomerDTO])
def get_customers(db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = GetCustomersService(repo)
    customers = service.execute()
    return customers


@router.post("/api/create_customers")
def create_customer(command: CreateCustomerCommand, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = CreateCustomerService(repo)
    customer = service.execute(command)
    return {"id": customer.id, "message": "Customer created successfully"}

@router.put("/api/customers/{customer_id}")
def update_customer(customer_id: int, command: UpdateCustomerCommand, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    service = UpdateCustomerService(repo)
    customer = service.execute(customer_id, command)
    return {"id": customer.id, "message": "Customer updated successfully"}
