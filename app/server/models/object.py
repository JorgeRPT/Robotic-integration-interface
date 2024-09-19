from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ObjectSchema(BaseModel):
    name: str = Field(...)
    x: float | None = None
    y: float | None = None
    z: float | None = None
    qx: float | None = None
    qy: float | None = None
    qz: float | None = None
    qw: float | None = None
    mesh: str | None = None
    urdf_reference_frame: str | None = None
    mode: str | None = None

    class Config:
        schema_extra = {
            "example": {
                "name": "object01",
                "x": 123.0,
                "y": 321.9,
                "z": 30.5,
                "qx": 1.0,
                "qy": 3.9,
                "qz": 3.5,
                "qw": 1.0,
                "mesh": "<base64 encoded file>",
                "urdf_reference_frame": "name of the object defined in the urdf file",
                "mode": "absolute or relative"
            }
        }


class UpdateObjectModel(BaseModel):
    name: Optional[str]
    x: Optional[float]
    y: Optional[float]
    z: Optional[float]
    qx: Optional[float]
    qy: Optional[float]
    qz: Optional[float]
    qw: Optional[float]
    mesh: Optional[str]
    urdf_reference_frame: Optional[str]
    mode: Optional[str]


    class Config:
        schema_extra = {
            "example": {
                "name": "object01",
                "x": 123.0,
                "y": 321.9,
                "z": 30.5,
                "qx": 1.0,
                "qy": 3.9,
                "qz": 3.5,
                "qw": 1.0,
                "mesh": "<base64 encoded file>",
                "urdf_reference_frame": "name of the object defined in the urdf file",
                "mode": "absolute or relative"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
