from ResourceSchema import Resources
from ReferenceSchema import References
from PersonSchema import Person
from IdentifierSchema import Identifier
from RelatedCatalogItemSchema import RelatedCatalogItem

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class ModelTypeEnum(str, Enum):
    model = "model"
    framework = "framework"
    tool = "tool"
    testbed = "testbed"


class TypeKeywordEnum(str, Enum):
    theoretical = "Theoretical"
    empirical = "Empirical"
    physics_based = "Physics-based"
    process_based = "Process-based"
    statistical = "Statistical"
    geospatial = "Geospatial"


class BasicProfile(BaseModel):
    """Basic metadata profile

    Fields
    ------
    item_type : ModelTypeEnum
        model, tool, framework, testbed
        model
    name : str
        title
        COAWST - Coupled-Ocean-Atmosphere-Waves-Sediment Transport
    description : str
        abstract or general description
        The COAWST modeling system joins an ocean model, an atmosphere model, a wave model, and a sediment transport model for studies of coastal change...
    organization: bool = 1
        1 = usgs ; 0 = external
        1
    external_organization_name: Optional[str]
    release_date : str
        Date
        200810
    last_update : str
        Date
        202009
    author : Optional[List[Person]]
        The author(s) or developer(s) of this content.
        Person(
                name="John C Warner",
                orcid="https://orcid.org/0000-0003-4993-021X",
                email="jcwarner@usgs.gov",
                authortype="maintainer",
            )
    contact : Optional[List[Person]]
        Person(s) responsible for maintenance of the model or item.
        Person(
                name="John C Warner",
                orcid="https://orcid.org/0000-0003-4993-021X",
                email="jcwarner@usgs.gov",
                authortype="author",
            )
    version : str
        Latest release version v1.0.0
        3.4
    how_to_cite: Optional[str]
        Preferred citation format
        Warner, J.C., Ganju, N.K., Sherwood, C.R., Tarandeep, K., Aretxabaleta, A., He, R., Zambon, J., and Kumar, N., 2019, Coupled-Ocean-Atmosphere-Wave-Sediment Transport (COAWST) Modeling System...
    usgs_missionarea: Optional[str]
        USGS mission area
        Water Resources
    identifier: Optional[List[Identifier]]
        Identifiers related to the model
    programming_language: Optional[str]
        Primary programming language used for the modeling
        Fortran, Roff, C++, C, MATLAB, PostScript
    license: Optional[str]
       CC0 see: https://creativecommons.org/publicdomain/zero/1.0/legalcode
    resources: Optional[Resources]
        Custom object containing advanced resource section
    references: Optional[References]
        Custom object containing advanced reference section
    science_keywords: Optional[str]
        Topical science keywords that will help for discovering the item. Preferred to use terms from the USGS Thesaurus please see: https://apps.usgs.gov/thesaurus/
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
        For example, platform and mode (Jupyter, Graphical User Interface, etc).
        Jupyter Notebook
    image: Optional[HttpUrl]
        Header image for the model profile page
        https://www.sciencebase.gov/catalog/file/get/5eb4485382ce25b5135abf00?f=__disk__d0%2F5d%2F21%2Fd05d214d168dd342556cb4b7a73f7e488e04fa5b
    related_catalog_items: Optional[List[str]]
        coawst - wrf item
    related_catalog_item_types: Optional[str]
    """

    _version: str = "v1.0.0"

    item_type: ModelTypeEnum = "model"
    name: str
    description: str
    organization: bool = 1
    external_organization_name: Optional[str]
    release_date: Optional[str]
    last_update: Optional[str]
    subtitle: Optional[str]
    author: Optional[List[Person]]
    contact: Optional[List[Person]]
    version: Optional[str]
    how_to_cite: Optional[str]
    usgs_missionarea: Optional[str]
    identifier: Optional[List[Identifier]]
    programming_language: Optional[str]
    license: Optional[str] = "CC0"
    resources: Optional[Resources]
    references: Optional[References]
    science_keywords: Optional[List[str]]
    type_keywords: Optional[TypeKeywordEnum]
    other_keywords: Optional[str]
    image: Optional[HttpUrl]
    related_catalog_item: Optional[RelatedCatalogItem]
