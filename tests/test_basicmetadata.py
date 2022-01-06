from PersonSchema import Person
from BasicProfileSchema import BasicProfile
from DataSchema import Data
from SoftwareSchema import Software
from PublicationsSchema import Publications
from OtherLinksSchema import OtherLinks
from IdentifierSchema import Identifier
from pydantic import ValidationError
from hypothesis import given, strategies as st
from typing import List


def str_to_list(field: str) -> List:
    new_field_list = []
    if field:
        new_field_list.append(field)
    return new_field_list


def test_min_metadata():
    mdata = BasicProfile(
        item_type="Model",
        name="Modflow",
        description="Sample description",
        organization=True,
    )
    assert mdata


def test_full_metadata():
    """https://www.sciencebase.gov/catalog/item/5eb4485382ce25b5135abf00"""
    per1 = Person(
        name="John C Warner",
        orcid="https://orcid.org/0000-0003-4993-021X",
        email="jcwarner@usgs.gov",
        authortype=["Author"],
    )
    ppl = [per1]

    dta = Data(
        usgs_datarelease_links=["https://code.usgs.gov/coawstmodel/COAWST/"],
        model_output=["https://doi.org/10.5066/P9NQUAOW"],
        model_archive=["https://doi.org/10.5066/P9NQUAOW"],
    )

    sftwr = Software(
        usgs_software_gitlab_release_urls=[
            "https://code.usgs.gov/coawstmodel/COAWST/"
        ],
        download_url=["https://doi.org/10.5066/P9NQUAOW"],
        external_software_repository_urls=["https://code.usgs.gov/coawstmodel/COAWST/-/tree/master"],
        runtime_image=["https://doi.org/10.5066/P9NQUAOW"],
    )

    pubs = Publications(
        primary_publications=["https://doi.org/10.5066/P9NQUAOW"],
        model_citations=["https://doi.org/10.5066/P9NQUAOW"],
        model_application=["https://doi.org/10.5066/P9NQUAOW"],
        user_manual_url=["https://doi.org/10.5066/P9NQUAOW"],
    )

    othrlnks = OtherLinks(
        usgs_website=["https://coawstmodel-trac.sourcerepo.com/coawstmodel_COAWST/"],
        weblinks=["https://code.usgs.gov/coawstmodel/COAWST/-/tree/master"],
        quickstart_notebook=["https://doi.org/10.5066/P9NQUAOW"],
    )

    mdata = BasicProfile(
        item_type="Model",
        name="COAWST - Coupled-Ocean-Atmosphere-Waves-Sediment Transport",
        description='"The COAWST modeling system joins an ocean model, an atmosphere model, a wave model, and a sediment transport model for studies of coastal change. COAWST is an open-source tool that combines many sophisticated systems that each provide relative earth-system components necessary to investigate the dynamics of coastal storm impacts. Specifically, the COAWST Modeling System includes an ocean component—Regional Ocean Modeling System (ROMS); atmosphere component—Weather Research and Forecast Model (WRF), hydrology component- WRF_Hydro; wave components—Simulating Waves Nearshore (SWAN), WAVEWATCHIII, and InWave; a sediment component—the USGS Community Sediment Models; and a sea ice model. We began with a coupled modeling system as described [...]',
        organization=True,
        release_date="200810",
        last_update="202009",
        person=ppl,
        version="3.4",
        how_to_cite='Warner, J.C., Ganju, N.K., Sherwood, C.R., Tarandeep, K., Aretxabaleta, A., He, R., Zambon, J., and Kumar, N., 2019, Coupled-Ocean-Atmosphere-Wave-Sediment Transport (COAWST) Modeling System: U.S. Geological Survey Software Release, 23 April 2019,&nbsp;<a href="https://doi.org/10.5066/P9NQUAOW" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183);">https://doi.org/10.5066/P9NQUAOW',
        usgs_missionarea=["Water Resources"],
        identifier=[
            Identifier(
                name="DOI:10.5066/P9NQUAOW",
                id="DOI:10.5066/P9NQUAOW",
                type="Digital Object Identifier",
            )
        ],
        programming_language=["Fortran", "Roff", "C++", "C", "MATLAB", "PostScript"],
        data=dta,
        software=sftwr,
        publications=pubs,
        other_links=othrlnks,
        image="https://www.sciencebase.gov/catalog/file/get/5eb4485382ce25b5135abf00?f=__disk__d0%2F5d%2F21%2Fd05d214d168dd342556cb4b7a73f7e488e04fa5b",
    )
    assert mdata


def test_full_metadata_prev1():
    """https://www.sciencebase.gov/catalog/item/5eb4485382ce25b5135abf00"""
    per1 = Person(
        name="John C Warner",
        orcid="https://orcid.org/0000-0003-4993-021X",
        email="jcwarner@usgs.gov",
        authortype=["Author"],
    )

    per2 = Person(
        name="Maitane Olabarrieta",
        orcid="https://orcid.org/0000-0002-7619-7992",
        email="maitane.olabarrieta@essie.ufl.edu",
        authortype=["Author", "Point of Contact"],
    )
    ppl = [per1, per2]

    dta = Data(
        usgs_datarelease_links=["https://code.usgs.gov/coawstmodel/COAWST/"],
        model_output=["https://doi.org/10.5066/P9NQUAOW"],
        model_archive=["https://doi.org/10.5066/P9NQUAOW"],
    )

    sftwr = Software(
        usgs_software_gitlab_release_urls=[
            "https://code.usgs.gov/coawstmodel/COAWST/"
        ],
        download_url=["https://doi.org/10.5066/P9NQUAOW"],
        external_software_repository_urls=["https://code.usgs.gov/coawstmodel/COAWST/-/tree/master"],
        runtime_image=["https://doi.org/10.5066/P9NQUAOW"],
    )

    pubs = Publications(
        primary_publications=["https://doi.org/10.1029/2011JC007387"],
        model_citations=["https://doi.org/10.5066/P9NQUAOW"],
        model_application=["https://doi.org/10.5066/P9NQUAOW"],
        user_manual_url=["https://doi.org/10.5066/P9NQUAOW"],
    )

    othrlnks = OtherLinks(
        usgs_website=["https://coawstmodel-trac.sourcerepo.com/coawstmodel_COAWST/"],
        weblinks=["https://code.usgs.gov/coawstmodel/COAWST/-/tree/master"],
        quickstart_notebook=["https://doi.org/10.5066/P9NQUAOW"],
    )

    mdata = BasicProfile(
        item_type="Model",
        name="COAWST - Coupled-Ocean-Atmosphere-Waves-Sediment Transport",
        description='"The COAWST modeling system joins an ocean model, an atmosphere model, a wave model, and a sediment transport model for studies of coastal change. COAWST is an open-source tool that combines many sophisticated systems that each provide relative earth-system components necessary to investigate the dynamics of coastal storm impacts. Specifically, the COAWST Modeling System includes an ocean component—Regional Ocean Modeling System (ROMS); atmosphere component—Weather Research and Forecast Model (WRF), hydrology component- WRF_Hydro; wave components—Simulating Waves Nearshore (SWAN), WAVEWATCHIII, and InWave; a sediment component—the USGS Community Sediment Models; and a sea ice model. We began with a coupled modeling system as described [...]',
        organization=True,
        release_date="200810",
        last_update="202009",
        person=ppl,
        version="3.4",
        how_to_cite='Warner, J.C., Ganju, N.K., Sherwood, C.R., Tarandeep, K., Aretxabaleta, A., He, R., Zambon, J., and Kumar, N., 2019, Coupled-Ocean-Atmosphere-Wave-Sediment Transport (COAWST) Modeling System: U.S. Geological Survey Software Release, 23 April 2019,&nbsp;<a href="https://doi.org/10.5066/P9NQUAOW" style="box-sizing: border-box; background-color: transparent; color: rgb(51, 122, 183);">https://doi.org/10.5066/P9NQUAOW',
        usgs_missionarea=["Ecosystems", "Water Resources"],
        identifier=[
            Identifier(
                name="DOI:10.5066/P9NQUAOW",
                id="DOI:10.5066/P9NQUAOW",
                type="Digital Object Identifier",
            )
        ],
        programming_language=["Fortran", "Roff", "C++", "C", "MATLAB", "PostScript"],
        data=dta,
        software=sftwr,
        publications=pubs,
        other_links=othrlnks,
        image="https://www.sciencebase.gov/catalog/file/get/5eb4485382ce25b5135abf00?f=__disk__d0%2F5d%2F21%2Fd05d214d168dd342556cb4b7a73f7e488e04fa5b",
        related_modelcatalog_assets=["https://data.usgs.gov/modelcatalog/model/49328aa8-573c-4764-841a-93da0ee334e3"],
    )
    assert mdata


@given(st.builds(BasicProfile))
def test_property(instance):
    assert isinstance(instance, BasicProfile)
