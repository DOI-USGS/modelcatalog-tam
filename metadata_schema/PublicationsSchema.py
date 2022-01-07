from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Publications(BaseModel):
    """Publications:

    References to publications where the model is used,
    or cited, model archive, model application, user manuals or documentations.

    Fields
    ------
    primary_publications: Optional[List[HttpUrl]]
        Optional container for primary publications links
    model_output: Optional[List[HttpUrl]]
        Optional container for links to model output information
    model_citations: Optional[List[HttpUrl]]
        Optional field References to reports or publications where the model is used
        or cited
    model_application: Optional[List[HttpUrl]]
        The use of a particular model software to analyze a specific
        situation (region, time period, etc.). Terminology used in the
        USGS Water Resources Mission Area.
    user_manual_url: Optional[List[HttpUrl]]
        Optional field for locations of model user manuals or similar documentation.

    """

    _version: str = "v1.0.2"

    primary_publications: Optional[List[HttpUrl]]
    model_citations: Optional[List[HttpUrl]]
    model_application: Optional[List[HttpUrl]]
    user_manual_url: Optional[List[HttpUrl]]
