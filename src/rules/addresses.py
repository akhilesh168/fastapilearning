from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.addresses import UserAddress, UpdateAddress
from bson import ObjectId


def get_collection_address(request: Request):
    return request.app.database["address"]


def create_address(request: Request, address: UserAddress = Body(...)):
    address = jsonable_encoder(address)
    new_user = get_collection_address(request).insert_one(address)
    created_user = get_collection_address(request).find_one({"_id": new_user.inserted_id})
    return created_user


def list_address(request: Request, limit: int):
    address = list(get_collection_address(request).find(limit=limit))
    return address


def find_address(request: Request, id: str):
    if address := get_collection_address(request).find_one({"_id": ObjectId(id)}):
        return address
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")


def delete_address(request: Request, id: str):
    deleted_user = get_collection_address(request).delete_one({"_id": ObjectId(id)})

    if deleted_user.delete_count == 1:
        return f"User with id {id} deleted successfully"

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")


def update_address(request: Request, id: str, address: UpdateAddress):
    address = {k: v for k, v in address.dict().items() if v is not None}
    if len(address) >= 1:
        update_result = get_collection_address(request).update_one({"_id": ObjectId(id)}, {"$set": address})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address not found")

    if existing_address := get_collection_address(request).find_one({"_id": ObjectId(id)}) is not None:
        return existing_address

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Address not found")
