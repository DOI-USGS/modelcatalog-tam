from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class References(BaseModel):
    """Where the model has been used:

    References to reports or publications where the model is used,
    or cited, outputs (data release), model archive, model application.

    Fields
    ------
    model_output : Optional[str]
        Optional container for model output information
    usgs_datarelease_links : Optional[List[HttpUrl]]
        Data release landing page
    model_citations : Optional[List[str]]
        References to reports or publications where the model is used
        or cited
    model_archive : Optional[str]
    model_application : Optional[str]
    """

    _version: str = "v1.0.0"

    model_output: Optional[str]
    usgs_datarelease_links: Optional[List[HttpUrl]]
    model_citations: Optional[List[str]]
    model_archive: Optional[str]
    model_application: Optional[str]
