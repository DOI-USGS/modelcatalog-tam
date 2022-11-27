from DataSchema import Data
from SoftwareSchema import Software
from PublicationsSchema import Publications
from OtherLinksSchema import OtherLinks
from PersonSchema import Person
from IdentifierSchema import Identifier

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class ModelTypeEnum(str, Enum):
    model = "Model"
    framework = "Framework"
    tool = "Tool"
    testbed = "Testbed"


class TypeKeywordEnum(str, Enum):
    analytical = "Analytical"
    conceptual = "Conceptual"
    data_driven = "Data-driven"
    deterministic = "Deterministic"
    empirical = "Empirical"
    geospatial = "Geospatial"
    mathematical = "Mathematical"
    mechanistic = "Mechanistic"
    numerical = "Numerical"
    physics_based = "Physics-based"
    process_based = "Process-based"
    statistical = "Statistical"
    stochastic = "Stochastic"
    theoretical = "Theoretical"


class MissionAreaKeywordEnum(str, Enum):
    core_science_systems = "Core Science Systems"
    ecosystems = "Ecosystems"
    energy_minerals = "Energy and Minerals"
    natural_hazards = "Natural Hazards"
    water = "Water Resources"


class BasicProfile(BaseModel):
    """Basic metadata profile

    Fields
    ------
    item_type: ModelTypeEnum
        Model, tool, framework, testbed
    name: str
        Title, recommended format: "ACRONYM/Short name - longer description"
    description: str
        General description, recommended format of a short paragraph, 4-5 sentences. HTML is allowed.
    organization: bool = True
        True = usgs ; False = external
    external_organization_name: Optional[List[str]]
    release_date: str
        Date, in YYYY-MM-DD format. May be year only.
    last_update: str
        Date, in YYYY-MM-DD format. May be year only.
    person: Optional[List[Person]]
        Person(s) (author(s) or developer(s)) responsible for maintenance of the model or item or content.
    version: str
        Latest release version, ex. v1.0
    how_to_cite: Optional[str]
        Preferred citation format: Authors, Year, Title, Publisher, DOI.
    usgs_missionarea: Optional[List[MissionAreaKeywordEnum]]
        USGS mission area
    identifier: Optional[List[Identifier]]
        Identifiers related to the model, especially the identifier assigned by the USGS identifier tool.
    programming_language: Optional[List[str]]
        Primary programming language(s) used for the modeling
    license: Optional[str]
        Default to CC0 see: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    data: Optional[Data]
        Custom object containing advanced data section
    software: Optional[Software]
        Custom object containing advanced software section
    publications: Optional[Publications]
        Custom object containing advanced publications section
    other_links: Optional[OtherLinks]
        Custom object containing advanced other links section
    science_keywords: Optional[str]
        Topical science keywords that will help for discovering the item. Terms must come from the USGS Thesaurus please see: https://apps.usgs.gov/thesaurus/
    type_keywords: Optional[List[TypeKeywordEnum]]
        Keywords describing the type of model. For example "Numerical"
    other_keywords: Optional[str]
        Other keywords that are not in the USGS Thesaurus or other controlled keyword lists. For example, platform and mode (Jupyter, Graphical User Interface, etc).
    image: Optional[HttpUrl]
        Header image for the model profile page
    related_modelcatalog_assets: Optional[List[str]]
        Related catalog items for the model, formatted as the full URL for the Model Catalog landing page.

    Example of a working python instance of the data model
    ------------------------------------------------------
    >>> BasicProfile(item_type="Model",
    ...              name="COAWST",
    ...              description="sample description")
    BasicProfile(item_type=<ModelTypeEnum.model: 'Model'>, name='COAWST', description='sample description', organization=True, external_organization_name=None, release_date=None, last_update=None, person=None, version=None, how_to_cite=None, usgs_missionarea=None, identifier=None, programming_language=None, license='CC0', data=None, software=None, publications=None, other_links=None, science_keywords=None, type_keywords=None, other_keywords=None, image=None, related_modelcatalog_assets=None)
    """

    _version: str = "v1.0.3"

    item_type: ModelTypeEnum = "Model"
    name: str
    description: str
    organization: bool = True
    external_organization_name: Optional[List[str]]
    release_date: Optional[str]
    last_update: Optional[str]
    person: Optional[List[Person]]
    version: Optional[str]
    how_to_cite: Optional[str]
    usgs_missionarea: Optional[List[MissionAreaKeywordEnum]]
    identifier: Optional[List[Identifier]]
    programming_language: Optional[List[str]]
    license: Optional[str] = "CC0"
    data: Optional[Data]
    software: Optional[Software]
    publications: Optional[Publications]
    other_links: Optional[OtherLinks]
    science_keywords: Optional[List[str]]
    type_keywords: Optional[List[TypeKeywordEnum]]
    other_keywords: Optional[List[str]]
    image: Optional[HttpUrl]
    related_modelcatalog_assets: Optional[List[str]]
