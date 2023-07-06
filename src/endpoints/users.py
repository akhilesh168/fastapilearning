from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.users import User

import src.rules.users as users

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED,
             response_model=User)
def create_user(request: Request, user: User = Body(...)):
    return users.create_user(request, user)


@router.get("/", response_description="List user", response_model=List[User])
def list_user(request: Request):
    return users.list_users(request, 100)


@router.get("/{user_id}", response_description="Get user", response_model=List[User])
def find_user(request: Request, user_id: str):
    return users.find_user(request, user_id)

@router.delete("/{id}", response_description="Delete user")
def delete_user(request: Request, id: str):
    return users.delete_user(request, id)
