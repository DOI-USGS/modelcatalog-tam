from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class RelatedCatalogItemTypeEnum(str, Enum):
    related_model = "Related Model"
    related_framework = "Related Framework"
    related_tool = "Related Tool"
    related_testbed = "Related Testbed"


class RelatedCatalogItem(BaseModel):
    """

    Fields
    ------
    related_catalog_url: Optional[HttpUrl]
    related_catalog_id: Optional[str]
    component_of: Optional[str]
    type: Optional[RelatedCatalogItemTypeEnum]

    """

    _version: str = "v1.0.1"

    related_catalog_url: Optional[HttpUrl]
    related_catalog_id: Optional[str]
    component_of: Optional[str]
    type: Optional[RelatedCatalogItemTypeEnum]
