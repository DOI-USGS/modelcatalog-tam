from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class Software(BaseModel):
    """Software

    Where to download it, related software release pages,
    source code (organizational website or repository, if available).

    Fields
    ------
    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
        Optional field for official USGS software releases on code.usgs.gov (Gitlab)
        Use the DOI of the software release, unless the DOI does not point to the
        main landing page of the repository. If the DOI points to a location other
        than the main repository landing page, point to the main repository landing page.
    download_url: Optional[List[HttpUrl]]
        Optional field for locations where users would download the model executable
    external_software_repository_urls: Optional[List[HttpUrl]]
        Optional field for related code repositories that are not on code.usgs.gov (Gitlab),
        for example, repositories that are on github.com or gitlab.com
    runtime_image: Optional[List[HttpUrl]]
        Optional field for links to runtime images such as Docker images.

    """

    _version: str = "v1.0.3"

    usgs_software_gitlab_release_urls: Optional[List[HttpUrl]]
    download_url: Optional[List[HttpUrl]]
    external_software_repository_urls: Optional[List[HttpUrl]]
    runtime_image: Optional[List[HttpUrl]]
