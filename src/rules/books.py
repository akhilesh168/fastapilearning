from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.books import Books, BooksUpdate
from bson import ObjectId


def get_collection_books(request: Request):
    return request.app.database["books"]


def create_book(request: Request, book: Books = Body(...)):
    book = jsonable_encoder(book)
    new_user = get_collection_books(request).insert_one(book)
    created_user = get_collection_books(request).find_one({"_id": new_user.inserted_id})
    return created_user


def list_books(request: Request, limit: int):
    books = list(get_collection_books(request).find(limit=limit))
    return books


def list_books_by_author(request: Request, author: str):
    books = list(get_collection_books(request).aggregate([{"$match": {"author": author}}]))
    return books


def find_books(request: Request, id: str):
    if book := get_collection_books(request).find_one({"_id": ObjectId(id)}):
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")


def delete_book(request: Request, id: str):
    deleted_user = get_collection_books(request).delete_one({"_id": ObjectId(id)})

    if deleted_user.delete_count == 1:
        return f"User with id {id} deleted successfully"

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")


def update_book(request: Request, id: str, book: BooksUpdate):
    book = {k: v for k, v in book.dict().items() if v is not None}
    if len(book) >= 1:
        update_result = get_collection_books(request).update_one({"_id": ObjectId(id)}, {"$set": book})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found")

    if existing_book := get_collection_books(request).find_one({"_id": ObjectId(id)}) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book not found")
