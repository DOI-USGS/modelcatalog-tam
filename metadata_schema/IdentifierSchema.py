from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional
from enum import Enum


class IdentifierTypeEnum(str, Enum):
    doi = "Digital Object Identifier"
    custom = "Custom"
    persistent_id = "Persistent Identifier"


class Identifier(BaseModel):
    """Identifier specification

    Fields
    ------
    name: str
    id: Optional[str]
    url: Optional[HttpUrl]

    """

    _version: str = "v1.0.3"

    name: str
    id: Optional[str]
    url: Optional[HttpUrl]
    type: Optional[IdentifierTypeEnum]
