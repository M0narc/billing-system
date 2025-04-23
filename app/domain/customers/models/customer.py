from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    id: int
    name: str
    email: str
    address: str
    tax_id: str
    is_active: bool = True
    created_at: datetime = None
