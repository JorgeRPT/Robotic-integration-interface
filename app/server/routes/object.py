from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_object,
    delete_object,
    retrieve_object,
    retrieve_objects,
    update_object,
)

from server.models.object import (
    ErrorResponseModel,
    ResponseModel,
    ObjectSchema,
    UpdateObjectModel,
)

router = APIRouter()

@router.post("/", response_description="Object data added into the database")
async def add_object_data(object: ObjectSchema = Body(...)):
    object = jsonable_encoder(object)
    new_object = await add_object(object)
    return ResponseModel(new_object, "object added successfully.")

@router.get("/", response_description="objects retrieved")
async def get_objects():
    objects = await retrieve_objects()
    if objects:
        return ResponseModel(objects, "objects data retrieved successfully")
    return ResponseModel(objects, "Empty list returned")


@router.get("/{name}", response_description="object data retrieved")
async def get_object_data(name):
    object = await retrieve_object(name)
    if object:
        return ResponseModel(object, "object data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "object doesn't exist.")


@router.put("/{id}")
async def update_object_data(id: str, req: UpdateObjectModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_object = await update_object(id, req)
    if updated_object:
        return ResponseModel(
            "Object with ID: {} update is successful".format(id),
            "Object name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the object data.",
    )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_object_data(id: str):
    deleted_object = await delete_object(id)
    if deleted_object:
        return ResponseModel(
            "Object with ID: {} removed".format(id), "Object deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Object with id {0} doesn't exist".format(id)
    )
