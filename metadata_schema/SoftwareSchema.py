from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Software(BaseModel):
    """Software

    Links to software or code related to the model. For example, where to download an executable, related USGS software release pages, or other
    source code. These links are usually organizational websites or code repositories.

    Fields
    ------
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
        Optional field for official USGS software releases on code.usgs.gov (Gitlab)
        Use the URL of the main repository landing page, not the DOI. This allows more information to be pulled from the code.usgs.gov system.
    download_url: Optional[List[HttpUrl]]
        Optional field for locations where users would download the model executable.
    external_software_repository_urls: Optional[List[HttpUrl]]
        Optional field for related code repositories that are not on code.usgs.gov (Gitlab), for example, repositories that are on github.com or gitlab.com
    runtime_image: Optional[List[HttpUrl]]
        Optional field for links to runtime images such as Docker images.

    """

    _version: str = "v1.0.3"

    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
    download_url: Optional[List[HttpUrl]]
    external_software_repository_urls: Optional[List[HttpUrl]]
    runtime_image: Optional[List[HttpUrl]]
