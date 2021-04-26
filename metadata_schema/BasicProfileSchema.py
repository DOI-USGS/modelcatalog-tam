from ResourceSchema import Resources
from ReferenceSchema import References
from PersonSchema import Person
from IdentifierSchema import Identifier
from RelatedCatalogItemSchema import RelatedCatalogItem

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class ModelTypeEnum(str, Enum):
    model = "Model"
    framework = "Framework"
    tool = "Tool"
    testbed = "Testbed"

class MissionAreaKeywordEnum(str, Enum):
    core-science-systems = "Core Science Systems"
    ecosystems = "Ecosystems"
    energy-minerals = "Energy and Minerals"
    natural-hazards = "Natural Hazards"
    water = "Water Resources"

class TypeKeywordEnum(str, Enum):
    analytical = "Analytical" 
    conceptual = "Conceptual"
    data-driven = "Data-driven" 
    deterministic = "Deterministic"  
    empirical = "Empirical"
    geospatial = "Geospatial"
    mathematical = "Mathematical" 
    mechanistic = "Mechanistic"
    numerical = "Numerical"
    physics-based = "Physics-based"
    process-based = "Process-based"
    statistical = "Statistical"
    stochastic = "Stochastic"
    theoretical = "Theoretical"

class BasicProfile(BaseModel):
    """Basic metadata profile

    Fields
    ------
    item_type: ModelTypeEnum
        model, tool, framework, testbed
    name: str
        title
    description: str
        abstract or general description
    organization: bool = True
        True = usgs ; False = external
    external_organization_name: Optional[List[str]]
    release_date: str
        Date
    last_update: str
        Date
    person: Optional[List[Person]]
        The author(s) or point(s) of contact for the model
    version: str
        Latest release version v1.0.0
    how_to_cite: Optional[str]
        Preferred citation format - ideally a USGS Software Release for USGS models
    usgs_missionarea: Optional[List[[MissionAreaKeywordEnum]]
        USGS mission area
    identifier: Optional[List[Identifier]]
        Identifiers related to the model
    programming_language: Optional[List[str]]
        Primary programming language(s) used for the modeling
    license: Optional[str]
       CC0 see: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    resources: Optional[Resources]
        Custom object containing advanced resource section
    references: Optional[References]
        Custom object containing advanced reference section
    science_keywords: Optional[List[[str]]
        Topical science keywords that will help for discovering the item. Must be in the USGS Thesaurus, please see: https://apps.usgs.gov/thesaurus/
    type_keywords: Optional[List[[TypeKeywordEnum]]
    other_keywords: Optional[List[str]]
        For example, platform and mode (Jupyter, Graphical User Interface, etc). or other science keywords that are not in the USGS Thesaurus
    image: Optional[HttpUrl]
        Header image for the model profile page
    related_catalog_item: Optional[List[[RelatedCatalogItem]]

    Example
    -------
    >>> BasicProfile(item_type="Model",
    ...              name="COAWST",
    ...              description="sample description")
    BasicProfile(item_type=<ModelTypeEnum.model: 'Model'>, name='COAWST', description='sample description', organization=True, external_organization_name=None, release_date=None, last_update=None, subtitle=None, author=None, contact=None, version=None, how_to_cite=None, usgs_missionarea=None, identifier=None, programming_language=None, license='CC0', resources=None, references=None, science_keywords=None, type_keywords=None, other_keywords=None, image=None, related_catalog_item=None)
    """

    _version: str = "v1.1.0"

    item_type: ModelTypeEnum = "Model"
    name: str
    description: str
    organization: bool = True
    external_organization_name: Optional[List[str]]
    release_date: Optional[str]
    last_update: Optional[str]
    subtitle: Optional[str]
    person: Optional[List[Person]]
    version: Optional[str]
    how_to_cite: Optional[str]
    usgs_missionarea: Optional[List[MissionAreaKeywordEnum]]
    identifier: Optional[List[Identifier]]
    programming_language: Optional[List[str]]
    license: Optional[str] = "CC0"
    resources: Optional[Resources]
    references: Optional[References]
    science_keywords: Optional[List[str]]
    type_keywords: Optional[List[TypeKeywordEnum]]
    other_keywords: Optional[List[str]]
    image: Optional[HttpUrl]
    related_catalog_item: Optional[List[RelatedCatalogItem]]
