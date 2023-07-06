import uuid
from pydantic import BaseModel, Field
from typing import Optional


class UserAddress(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    addr_name: str
    user_id: str
    street: str
    number: str
    city: str
    state: str
    code: str

    class Config:
        schema_extra = {
            "example": {
                "addr_name": "House",
                "user_id": "49897787",
                "street": "Bablalal st",
                "number": "53",
                "city": "New Delhi",
                "state": "Delhi",
                "code": "121212"
            }
        }


class UpdateAddress(BaseModel):
    addr_name: Optional[str]
    street: Optional[str]
    number: Optional[float]
    city: Optional[str]
    state: Optional[str]
    code: Optional[str]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "addr_name": "House",
                "street": "Bablalal st",
                "number": "53",
                "city": "New Delhi",
                "state": "Delhi",
                "code": "121212"
            }
        }
