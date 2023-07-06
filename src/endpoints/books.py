from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.books import Books, BooksUpdate

import src.rules.books as books

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_description="Create a new books", status_code=status.HTTP_201_CREATED,
             response_model=Books)
def create_book(request: Request, user_book: Books = Body(...)):
    return books.create_book(request, user_book)


@router.get("/", response_description="List books", response_model=List[Books])
def list_book(request: Request):
    return books.list_books(request, 100)

@router.get("/{author}", response_description="Get books by author", response_model=List[Books])
def find_book(request: Request, author: str):
    return books.list_books_by_author(request, author)

@router.put("/{id}", response_description="Update books", response_model=BooksUpdate)
def update_book(request: Request, id: str, book: BooksUpdate = Body(...)):
    return books.update_book(request, id, book)


@router.delete("/{id}", response_description="Delete books")
def delete_book(request: Request, id: str):
    return books.delete_book(request, id)
