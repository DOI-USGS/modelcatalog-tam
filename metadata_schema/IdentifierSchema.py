from pydantic import BaseModel, HttpUrl, EmailStr
from typing import Optional
from enum import Enum


class IdentifierTypeEnum(str, Enum):
    doi = "Digital Object Identifier"
    custom = "Custom"
    persistent_id = "Persistent Identifier"


class Identifier(BaseModel):
    """Identifier specification

    Identifier information related to the model, such as the model identifier assigned by the USGS identifier tool. Model identifiers are assigned by the USGS Model Catalog team. Digital Object Identifiers for software, data, or publications do not belong here because they are included in the Software, Data, and Publications schemas. Other identifiers used in related systems (Github, Gitlab, other model catalogs) may be implemented in the future.  

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
