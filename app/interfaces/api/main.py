from fastapi import FastAPI
from app.interfaces.api.routers import customers

app = FastAPI()
app.include_router(customers.router)
