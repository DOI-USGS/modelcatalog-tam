from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class OtherLinks(BaseModel):
    """Additional Information:

    Other webpages about the model (in other catalogs), USGS
    webpage, model project page, etc.

    Fields
    ------
    usgs_website: Optional[List[HttpUrl]]
        Optional field for URLs that are part of the usgs.gov (Drupal CMS) website
    weblinks: Optional[List[HttpUrl]]
        Optional field for URLs that are not a usgs.gov (Drupal CMS) website. 
        Examples include community forums for the model.
    quickstart_notebook: Optional[List[HttpUrl]]
        Optional field for links to quickstart code notebooks on platforms such as Colab.

    """

    _version: str = "v1.0.3"

    usgs_website: Optional[List[HttpUrl]]
    weblinks: Optional[List[HttpUrl]]
    quickstart_notebook: Optional[List[HttpUrl]]
