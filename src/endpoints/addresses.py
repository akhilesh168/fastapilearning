from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.addresses import UserAddress, UpdateAddress

import src.rules.addresses as addresses

router = APIRouter(prefix="/address", tags=["Address"])


@router.post("/", response_description="Create a new user address", status_code=status.HTTP_201_CREATED,
             response_model=UserAddress)
def create_addrs(request: Request, user_addrs: UserAddress = Body(...)):
    return addresses.create_address(request, user_addrs)


@router.get("/", response_description="List addresses", response_model=List[UserAddress])
def list_addrs(request: Request):
    return addresses.list_address(request, 100)


@router.get("/{user_id}", response_description="Get user address", response_model=List[UserAddress])
def find_addrs(request: Request, user_id: str):
    return addresses.find_address(request, user_id)


@router.put("/{id}", response_description="Update user address", response_model=UpdateAddress)
def update_addrs(request: Request, id: str, addrs: UpdateAddress = Body(...)):
    return addresses.update_address(request, id, addrs)


@router.delete("/{id}", response_description="Delete user address")
def delete_addrs(request: Request, id: str):
    return addresses.delete_address(request, id)
