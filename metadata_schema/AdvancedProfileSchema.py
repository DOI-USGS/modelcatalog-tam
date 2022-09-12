from BasicProfileSchema import BasicProfile


from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from enum import Enum


class StatusTypeEnum(str, Enum):
    internal = "Internal"
    public = "Public"
    experimental = "Experimental"


class ComputeEnvEnum(str, Enum):
    personal_computer = "Personal Computer"
    denali = "Framework"
    tallgrass = "Tallgrass"
    yeti = "Yeti"
    condor = "Condor"
    usgs_cloud = "USGS Cloud"
    external_cloud = "External Cloud"


class AdvancedProfile(BaseModel):
    """Advanced metadata profile
    Fields
    ------
    status_type Optional[List[StatusTypeEnum]]
        View status of information in this schema: Public or internal to USGS.
        Internal: Use this if any of the content is not for public view. If any 
        URL links are on the USGS network and require login, the status 
        should be internal. 
        Public: content may be displayed on the public view of the catalog in
        the main area.
        Experimental: content may be displayed in a public view of the catalog
        but in an area labeled "Experimental"
    compute_environment = Optional[List[ComputeEnvEnum]]
        The compute environment(s) that have been used to run the model.
        Default = personal computer. Must be in the enumerated list.
    requirements = Optional[str]
        Software and/or hardware requirements needed to run the model and 
        replicate any published results.
        Ex. A URL to a requirements.txt file in a repository; or,  Free text 
        for a human-readable list of requirements.
    dependencies = Optional[str]
        All data dependencies needed to run the model and replicate any 
        published results.
    installation_info = Optional[str]
        Information on how to install the model so that it can be run (such as 
        compilation and/or execution instructions).
    notes_file = Optional[HttpUrl]
        A URL to a text or markdown file in a code repository that has any other
        relevant notes about the model run. Examples: accuracy, time to train,
        relationships between different code repositories.



    Example
    -------
        TBD

    """

    _version: str = "v1.0.0"

    status_type = Optional[List[StatusTypeEnum]] = "Public"
    compute_environment = Optional[List[ComputeEnvEnum]]

    requirements = Optional[str]
    dependencies = Optional[str]
    installation_info = Optional[str]

    notes_file: Optional[HttpUrl]
