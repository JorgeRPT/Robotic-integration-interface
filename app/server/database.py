import motor.motor_asyncio # type: ignore
from bson.objectid import ObjectId
from fastapi import HTTPException
from typing import List

MONGO_DETAILS = "mongodb://mongodb:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.test

object_collection = database.get_collection("objects")




# helpers


def object_helper(object) -> dict:
    return {
        "id": str(object["_id"]),
        "name": object["name"],
        "x": object["x"],
        "y": object["y"],
        "z": object["z"],
        "qx": object["qx"],
        "qy": object["qy"],
        "qz": object["qz"],
        "qw": object["qw"],
        "mesh": object["mesh"],
        "urdf_reference_frame": object["urdf_reference_frame"],
        "mode": object["mode"]
    }


# Retrieve all objects present in the database
async def retrieve_objects():
    objects = []
    async for object in object_collection.find():
        objects.append(object_helper(object))
    return objects


# Add a new object into to the database
async def add_object(object_data: dict) -> dict:
    object = await object_collection.insert_one(object_data)
    new_object = await object_collection.find_one({"_id": object.inserted_id})
    return object_helper(new_object)


# Retrieve objects with a matching name
async def retrieve_object(name: str) -> List[dict]:
    objects = []
    async for object in object_collection.find({"name": str(name)}):
        objects.append(object_helper(object))
    return objects


# Update a object with a matching ID
async def update_object(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    object = await object_collection.find_one({"_id": ObjectId(id)})
    if object:
        updated_object = await object_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_object:
            return True
        return False


# Delete a object from the database
async def delete_object(id: str):
    object = await object_collection.find_one({"_id": ObjectId(id)})
    if object:
        await object_collection.delete_one({"_id": ObjectId(id)})
        return True
