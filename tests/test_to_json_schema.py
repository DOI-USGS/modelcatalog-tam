#!/usr/bin/env python

from metadata_schema.BasicProfileSchema import BasicProfile
from metadata_schema.IdentifierSchema import Identifier
from metadata_schema.PersonSchema import Person
from metadata_schema.ReferenceSchema import References
from metadata_schema.RelatedCatalogItemSchema import RelatedCatalogItem
from metadata_schema.ResourceSchema import Resources
from scripts import model_metadata_mappers as mapper
from fixtures import model_dict


def test_get_basic_profile_model():
    """Test model_metadata_mappers.get_basic_profile_model().

    This could be made a proper unit test by changing using a test
    dictionary that lacks `contacts`, `weblinks`, and `relatedItems` as
    that would prevent calls to other functions. Otherwise, mocks could
    be used.

    :return: None
    """

    # Arrange
    test_dict = model_dict.test_dict

    # Act
    actual = mapper.get_basic_profile_model(test_dict)

    # Assert
    assert isinstance(actual, BasicProfile)


def test_get_identifier_models():

    # Arrange
    weblink_list = model_dict.test_dict['webLinks']

    # Act
    actual = mapper.get_identifier_models(weblink_list)

    # Assert
    for identifier in actual:
        assert isinstance(identifier, Identifier)


def test_get_person_models():

    # Arrange
    contact_list = model_dict.test_dict['contacts']

    # Act
    actual = mapper.get_person_models(contact_list)

    # Assert
    for contact in actual:
        assert isinstance(contact, Person)


def test_get_references_model():

    # Arrange
    weblink_list = model_dict.test_dict['webLinks']

    # Act
    actual = mapper.get_references_model(weblink_list)

    # Assert
    assert isinstance(actual, References)


def test_get_related_catalog_item_model():

    # Arrange
    related_items = model_dict.test_dict['relatedItems']

    # Act
    actual = mapper.get_related_catalog_item_model(related_items)

    # Assert
    assert isinstance(actual, RelatedCatalogItem)


def test_get_resources_model():

    # Arrange
    weblink_list = model_dict.test_dict['webLinks']

    # Act
    actual = mapper.get_resources_model(weblink_list)

    # Assert
    assert isinstance(actual, Resources)
