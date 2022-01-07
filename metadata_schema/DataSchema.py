from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Data(BaseModel):
    """Data:

    Data to report where the model is used, outputs (data release) or model archive.

    Fields
    ------
    usgs_datarelease_links: Optional[List[HttpUrl]]
        Optional field for USGS Data release Digital Object Identifiers
    model_output: Optional[List[HttpUrl]]
        Optional container for links to model output information
    model_archive: Optional[List[HttpUrl]]
        Optional field for USGS interpretive information products that consists of a 
        group of files that documents and archives numerical (ground)water
        models. Policy dictates that these are distributed online as
        USGS data releases. Terminology used in the USGS Water Resources Mission Area. 

    """

    _version: str = "v1.0.2"

    usgs_datarelease_links: Optional[List[HttpUrl]]
    model_output: Optional[List[HttpUrl]]
    model_archive: Optional[List[HttpUrl]]
