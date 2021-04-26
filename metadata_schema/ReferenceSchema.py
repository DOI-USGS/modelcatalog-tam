from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class References(BaseModel):
    """Where the model has been used:

    References to reports or publications where the model is used,
    or cited, outputs (data release), model archive, model application.

    Fields
    ------
    model_output: Optional[List[HttpUrl]]
        Optional container for links to model output information
    usgs_datarelease_links: Optional[List[HttpUrl]]
        Optional field for USGS Data release Digital Object Identifiers
    model_citations: Optional[List[HttpUrl]]
        Optional field References to reports or publications where the model is used
        or cited
    model_archive: Optional[List[HttpUrl]]
        Optional field for USGS interpretive information products that consists of a 
        group of files that documents and archives numerical (ground)water
        models. Policy dictates that these are distributed online as
        USGS data releases. Terminology used in the USGS Water Resources Mission Area. 
    model_application: Optional[List[HttpUrl]]
        The use of a particular model software to analyze a specific
        situation (region, time period, etc.). Terminology used in the
        USGS Water Resources Mission Area. 

    """

    _version: str = "v1.0.0"

    model_output: Optional[List[HttpUrl]]
    usgs_datarelease_links: Optional[List[HttpUrl]]
    model_citations: Optional[List[HttpUrl]]
    model_archive: Optional[List[HttpUrl]]
    model_application: Optional[List[HttpUrl]]
