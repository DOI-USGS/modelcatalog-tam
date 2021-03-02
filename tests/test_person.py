from PersonSchema import Person
from pydantic import ValidationError
from hypothesis import given, strategies as st


def test_min_person():
    ppl = Person(
        name="Alison P Appling",
    )
    assert ppl
    assert ppl.author_type == "author"
    assert ppl.name == "Alison P Appling"


def test_full_person():
    ppl = Person(
        name="Alison P Appling",
        orcid="https://orcid.org/0000-0003-3638-8572",
        email="aappling@usgs.gov",
        author_type="author",
        thumbnail_avatar_url="https://prd-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/styles/content_grid/public/thumbnails/image/appling_headshot.png",
        organization="USGS Water Resources Mission Area",
        job_title="Data Scientist",
        sciencebase_id="68008",
        usgs_staffprofile_url="https://www.usgs.gov/staff-profiles/alison-appling",
        github_profile="aappling-usgs",
        usgs_employee=1,
    )
    assert ppl
    assert ppl.github_profile == "aappling-usgs"


def test_email():
    """ invalid email test. """
    ppl = None
    try:
        ppl = Person(
            name="Sally Johnson",
            orcid="https://orcid.org/0000-0003-4993-0000",
            email="hello-world",
            authortype="author",
        )
    except ValidationError as e:
        assert ppl is None


@given(st.builds(Person))
def test_property(instance):
    assert isinstance(instance, Person)
