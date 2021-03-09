from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Resources(BaseModel):
    """Resource extension for additional information

    How to use the model: where to download it, manuals, user community
    pages, other webpages about the model (in other catalogs), USGS
    webpage, model project page, source code (organizational website or
    repository, if available).

    Fields
    ------
    download_url : Optional[HttpUrl]
        Where users would download the model
    primary_publications : Optional[str]
    weblinks : Optional[List[HttpUrl]]
    usgs_website : Optional[HttpUrl]
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
    external_software_repository_urls: Optional[List[HttpUrl]]
    quickstart_notebook: Optional[HttpUrl]
    runtime_image: Optional[HttpUrl]
    """

    _version: str = "v1.0.0"

    user_manual_url: Optional[HttpUrl]
    download_url: Optional[HttpUrl]
    primary_publications: Optional[str]
    weblink_url: Optional[List[HttpUrl]]
    usgs_website_url: Optional[List[HttpUrl]]
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
    external_software_repository_urls: Optional[List[HttpUrl]]
    quickstart_notebook: Optional[HttpUrl]
    runtime_image: Optional[HttpUrl]
