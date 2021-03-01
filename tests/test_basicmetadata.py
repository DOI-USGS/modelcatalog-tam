from PersonSchema import Person
from BasicProfileSchema import BasicProfile
from ResourceSchema import Resources
from ReferenceSchema import References
from IdentifierSchema import Identifier
from pydantic import ValidationError


def test_min_metadata():
    mdata = BasicProfile(
        item_type="model",
        name="Modflow",
        description="Sample description",
        organization=0,
    )
    assert mdata


def test_full_metadata():
    """https://www.sciencebase.gov/catalog/item/5eb4485382ce25b5135abf00"""
    per1 = Person(
            name="John C Warner",
            orcid="https://orcid.org/0000-0003-4993-021X",
            email="jcwarner@usgs.gov",
            authortype="author",
        )
    ppl = [per1]

    rsc = Resources(
        release_download_url="https://www.usgs.gov/software/coupled-ocean-atmosphere-wave-sediment-transport-coawst-modeling-system",
        weblinks=["https://code.usgs.gov/coawstmodel/COAWST/-/tree/master"],
        usgs_website="https://coawstmodel-trac.sourcerepo.com/coawstmodel_COAWST/",
        official_usgs_software_gitlab_releases=[
            "https://code.usgs.gov/coawstmodel/COAWST/"
        ],
    )

    mdata = BasicProfile(
        item_type="model",
        name="COAWST - Coupled-Ocean-Atmosphere-Waves-Sediment Transport",
        description='"The COAWST modeling system joins an ocean model, an atmosphere model, a wave model, and a sediment transport model for studies of coastal change. COAWST is an open-source tool that combines many sophisticated systems that each provide relative earth-system components necessary to investigate the dynamics of coastal storm impacts. Specifically, the COAWST Modeling System includes an ocean component—Regional Ocean Modeling System (ROMS); atmosphere component—Weather Research and Forecast Model (WRF), hydrology component- WRF_Hydro; wave components—Simulating Waves Nearshore (SWAN), WAVEWATCHIII, and InWave; a sediment component—the USGS Community Sediment Models; and a sea ice model. We began with a coupled modeling system as described [...]',
        organization=0,
        release_date="200810",
        last_update="202009",
        author=ppl,
        contact=ppl,
        version="3.4",
        how_to_cite='Warner, J.C., Ganju, N.K., Sherwood, C.R., Tarandeep, K., Aretxabaleta, A., He, R., Zambon, J., and Kumar, N., 2019, Coupled-Ocean-Atmosphere-Wave-Sediment Transport (COAWST) Modeling System: U.S. Geological Survey Software Release, 23 April 2019,&nbsp;<a href="https://doi.org/10.5066/P9NQUAOW" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183);">https://doi.org/10.5066/P9NQUAOW',
        usgs_missionarea="Water Resources",
        identifier=[
            Identifier(name="DOI:10.5066/P9NQUAOW",
            id="DOI:10.5066/P9NQUAOW",
            type="Digital Object Identifier")
            ],
        programming_language="Fortran, Roff, C++, C, MATLAB, PostScript",
        resources=rsc,
        image="https://www.sciencebase.gov/catalog/file/get/5eb4485382ce25b5135abf00?f=__disk__d0%2F5d%2F21%2Fd05d214d168dd342556cb4b7a73f7e488e04fa5b",
    )
    assert mdata
