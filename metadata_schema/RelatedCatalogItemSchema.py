from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class RelatedCatalogItemTypeEnum(str, Enum):
    related_model = "related model"
    related_framework = "related framework"
    related_tool = "related tool"
    related_testbed = "related testbed"


class RelatedCatalogItem(BaseModel):
    """

    Fields
    ------
    related_catalog_url: Optional[HttpUrl]
    related_catalog_id: Optional[str]
    component_of: Optional[str]
    type: Optional[RelatedCatalogItemTypeEnum]

    """

    _version: str = "v1.0.0"

    related_catalog_url: Optional[HttpUrl]
    related_catalog_id: Optional[str]
    component_of: Optional[str]
    type: Optional[RelatedCatalogItemTypeEnum]
