from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Publications(BaseModel):
    """Publications:

    Publications where the model is described, cited, or used.

    Fields
    ------
    primary_publications: Optional[List[HttpUrl]]
        Optional container for primary publications links. For example, the first publication about the model, describing the model.
    model_citations: Optional[List[HttpUrl]]
        Optional field References to reports or publications where the model is used or cited.
    model_application: Optional[List[HttpUrl]]
        A publication describing the use of a particular model software to analyze a specific situation (region, time period, etc.). Terminology used in the USGS Water Resources Mission Area.
    user_manual_url: Optional[List[HttpUrl]]
        Optional field for locations of model user manuals or similar documentation.

    """

    _version: str = "v1.0.3"

    primary_publications: Optional[List[HttpUrl]]
    model_citations: Optional[List[HttpUrl]]
    model_application: Optional[List[HttpUrl]]
    user_manual_url: Optional[List[HttpUrl]]
