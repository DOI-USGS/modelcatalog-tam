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
    user_manual_url: Optional[List[HttpUrl]]
        Optional field for locations of model user manuals or similar documentation.
    download_url: Optional[List[HttpUrl]]
        Optional field for locations where users would download the model executable
    primary_publications: Optional[List[HttpUrl]]
        Optional field for the main publications describing the model itself
    weblinks: Optional[List[HttpUrl]]
        Optional field for URLs that are not a usgs.gov (Drupal CMS) website. 
        Examples include community forums for the model.
    usgs_website: Optional[List[HttpUrl]]
        Optional field for URLs that are part of the usgs.gov (Drupal CMS) website
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
        Optional field for official USGS software releases on code.usgs.gov (Gitlab)
        Use the DOI of the software release, unless the DOI does not point to the
        main landing page of the repository. If the DOI points to a location other
        than the main repository landing page, point to the main repository landing page.
    external_software_repository_urls: Optional[List[HttpUrl]]
        Optional field for related code repositories that are not on code.usgs.gov (Gitlab),
        for example, repositories that are on github.com or gitlab.com
    quickstart_notebook: Optional[List[HttpUrl]]
        Optional field for links to quickstart code notebooks on platforms such as Colab.
    runtime_image: Optional[List[HttpUrl]]
        Optional field for links to runtime images such as Docker images. 
    """

    _version: str = "v1.0.1"

    user_manual_url: Optional[List[HttpUrl]]
    download_url: Optional[List[HttpUrl]]
    primary_publications: Optional[List[HttpUrl]]
    weblink_url: Optional[List[HttpUrl]]
    usgs_website_url: Optional[List[HttpUrl]]
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
    external_software_repository_urls: Optional[List[HttpUrl]]
    quickstart_notebook: Optional[List[HttpUrl]]
    runtime_image: Optional[List[HttpUrl]]
