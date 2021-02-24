from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class References(BaseModel):
    """Reference extension

    Fields
    ------
    model_output : Optional[str]
        Optional container for model output information.
    usgs_datarelease_links : Optional[List[HttpUrl]]
        Data release landing page
    model_citations : Optional[List[str]]
    """

    _version: str = "v1.0.0"

    model_output: Optional[str]
    usgs_datarelease_links: Optional[List[HttpUrl]]
    model_citations: Optional[List[str]]
