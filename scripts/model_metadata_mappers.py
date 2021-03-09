#!/usr/bin/env python

from collections import defaultdict

from pydantic import ValidationError

from metadata_schema.BasicProfileSchema import BasicProfile
from metadata_schema.IdentifierSchema import Identifier
from metadata_schema.PersonSchema import Person
from metadata_schema.ReferenceSchema import References
from metadata_schema.RelatedCatalogItemSchema import RelatedCatalogItem
from metadata_schema.ResourceSchema import Resources


def get_basic_profile_model(input_dict):
    """Create a Model Catalog model from ScienceBase input.

    :param input_dict: DICT; a ScienceBase model
    :return: OBJ; Pydantic BasicProfile object model for use in
        the Model Catalog
    """

    bp = defaultdict(list)

    # `item_type`, `organization`, `version`, `how_to_cite`,
    # `programming_language`, `license`, and `type_keywords` are not
    # easy to get from SB models so excluded here
    bp['name'] = input_dict.get('title')
    bp['description'] = input_dict.get('body')
    bp['subtitle'] = input_dict.get('subTitle')

    # `author` and `contact`
    # `external_organization_name` and `usgs_missionarea`
    contact_list = input_dict.get('contacts')
    if contact_list:
        # `author` and `contact`
        contacts = get_person_models(contact_list)
        bp['author'] = contacts
        bp['contact'] = contacts

        # `external_organization_name` and `usgs_missionarea`
        for contact in contact_list:
            try:
                assert (
                    contact['name'] and
                    contact['type'] and
                    contact['contactType']
                )
            except KeyError:
                continue
            else:
                name = contact['name']
                if (
                    contact['contactType'].lower() == 'organization' and
                    contact['type'].lower() == 'organization'
                ):
                    bp['external_organization_name'] = name
                if (
                    contact['contactType'].lower() == 'organization' and
                    contact['type'].lower() == 'usgs mission area'
                ):
                    bp['usgs_missionarea'] = f'USGS {name} Mission Area'

    # `dates`
    dates = input_dict.get('dates')
    if dates:
        for date in dates:
            try:
                assert date['type'] and date['dateString']
            except KeyError:
                continue
            else:
                if date['type'].lower() == 'release':
                    bp['release_date'] = date.get('dateString')
                if date['type'].lower() == 'lastupdate':
                    bp['last_update'] = date.get('dateString')

    # `image`
    preview = input_dict.get('previewImage')
    if preview:
        bp['image'] = preview['original']['viewUri']

    # `science_keywords` and `other_keywords`
    tags = input_dict.get('tags')
    if tags:
        for tag in tags:
            try:
                assert tag['type']
            except KeyError:
                continue
            else:
                if tag['type'].lower() == 'science topic':
                    bp['science_keywords'].append(tag['name'])
                if tag['type'].lower() == 'subject':
                    bp['other_keywords'].append(tag['name'])

    # `identifier`, `references`, and `resources`
    weblink_list = input_dict.get('webLinks')
    if weblink_list:
        identifiers = get_identifier_models(weblink_list)
        bp['identifier'] = identifiers
        references = get_references_model(weblink_list)
        bp['references'] = references
        resources = get_resources_model(weblink_list)
        bp['resources'] = resources

    # `related_catalog_item`
    related_items = input_dict.get('relatedItems')
    if related_items:
        related_catalog_item = get_related_catalog_item_model(related_items)
        bp['related_catalog_item'] = related_catalog_item

    basic_profile_no_nones = strip_nones(bp)

    try:
        basic_profile = BasicProfile(**basic_profile_no_nones)
    except ValidationError:
        raise
    else:
        return basic_profile


def get_identifier_models(weblink_list):
    """Use ScienceBase `weblinks` field to create Identifier objects.

    :param weblink_list: LIST; ScienceBase `webLinks` dictionaries
    :return: LIST; Pydantic Identifier object models
    """

    identifiers = []

    for link in weblink_list:
        try:
            assert link['typeLabel']
        except KeyError:
            continue
        else:
            if (
                link['typeLabel'].lower()
                in ['publication', 'sourcecode', 'model output']
                and not link.get('rel')
            ):
                # `name` is required so passed as '' here, and `id` is
                # always None so not included.
                identifier = {
                    'name': '',
                    'url': link.get('uri'),
                }

                # `type`
                if identifier['url'] and 'doi.org' in identifier['url']:
                    identifier['type'] = 'Digital Object Identifier'
                else:
                    identifier['type'] = 'Custom'

                identifier_no_nones = strip_nones(identifier)

                try:
                    identifier = Identifier(**identifier_no_nones)
                except ValidationError:
                    raise
                else:
                    identifiers.append(identifier)

    if identifiers:
        return identifiers
    else:
        return None


def get_person_models(contact_list):
    """Use ScienceBase `contacts` field to create Person objects.

    :param contact_list: LIST; ScienceBase `contacts` dictionaries
    :return: LIST; Pydantic Person object models
    """

    contacts = []

    for contact in contact_list:
        try:
            assert contact['contactType']
        except KeyError:
            continue
        else:
            if contact['contactType'].lower() == 'person':
                # `thumbnail_avatar_url`, `sciencebase_id`,
                # `usgs_gitlab_id`, and `github_profile` will always be
                # None, so they can be excluded here.
                person = {
                    'name': contact.get('name'),
                    'author_type': 'Point of Contact',
                    'email': contact.get('email'),
                    'job_title': contact.get('jobTitle'),
                    'usgs_staffprofile_url': contact.get('onlineResource'),
                }

                # `usgs_employee`
                if person['email'] and person['email'][-9:] == '@usgs.gov':
                    person['usgs_employee'] = 1

                # `orcid`
                orcid = contact.get('orcId')
                if orcid:
                    person['orcid'] = f'https://orcid.org/{orcid}'

                # `organization`
                try:
                    person['organization'] = (
                        contact['organization'].get('displayText'))
                except KeyError:
                    person['organization'] = None

                # It would probably be fine to pass in None for most
                # fields, but I think it's better to let the Pydantic
                # model fill in defaults.
                person_no_nones = strip_nones(person)

                try:
                    contact = Person(**person_no_nones)
                except ValidationError:
                    raise
                else:
                    contacts.append(contact)

    if contacts:
        return contacts
    else:
        return None


def get_references_model(weblink_list):
    """Use ScienceBase `weblink_list` field to create References object.

    :param weblink_list: LIST; ScienceBase `webLinks` dictionaries
    :return: LIST; Pydantic References object model
    """

    # `usgs_datarelease_links`, `model_archive`, and `model_application`
    #  are not found in the SB data so they are excluded here
    references = defaultdict(list)

    for link in weblink_list:
        try:
            assert link['typeLabel']
        except KeyError:
            continue
        else:
            url = link.get('uri')
            # `model_citations`
            if link['typeLabel'].lower() == 'citation':
                references['model_citations'].append(url)
            # `model_output`
            if link['typeLabel'].lower() == 'model output':
                references['model_output'] = url

    references_no_nones = strip_nones(references)

    try:
        references = References(**references_no_nones)
    except ValidationError:
        raise

    if references:
        return references
    else:
        return None


def get_related_catalog_item_model(related_items):
    """Use ScienceBase model to create RelatedCatalogItem object.

    :param related_items: LIST; ScienceBase `related_items` dictionaries
    :return: LIST; Pydantic RelatedCatalogItem object model
    """

    # `related_catalog_id`, `component_of`, and `type` are not found in
    # the SB data so they are excluded here
    related = {}

    try:
        assert related_items['link']['url']
    except KeyError:
        pass
    else:
        related['related_catalog_url'] = related_items['link']['url']

    related_no_nones = strip_nones(related)

    try:
        related = RelatedCatalogItem(**related_no_nones)
    except ValidationError:
        raise

    if related:
        return related
    else:
        return None


def get_resources_model(weblink_list):
    """Use ScienceBase `weblink_list` field to create Resources object.

    :param weblink_list: LIST; ScienceBase `webLinks` dictionaries
    :return: LIST; Pydantic Resources object model
    """

    # `user_manual_url`, `quickstart_notebook`, and `runtime_image`
    # are not easily found in SB models so they are excluded here
    resources = defaultdict(list)

    for link in weblink_list:
        try:
            assert link['type'] and link['typeLabel']
        except KeyError:
            continue
        else:
            raw_url = link.get('uri')
            url = raw_url[0: raw_url.find('?#')]

            # `primary_publications`
            if link['type'].lower() == 'related_primary_publication':
                resources['primary_publications'] = url
            # `usgs_software_gitlab_release_urls` and
            # `external_software_repository_urls`
            elif link['typeLabel'].lower() == 'sourcecode':
                resources['download_url'] = url
                if 'code.usgs.gov' in url:
                    resources['usgs_software_gitlab_release_urls'].append(url)
                else:
                    resources['external_software_repository_urls'].append(url)
            # `usgs_website_url` and `weblink_url`
            elif link['typeLabel'].lower() == 'web link':
                if 'usgs.gov' in url:
                    resources['usgs_website_url'].append(url)
                elif 'doi.org' not in url:
                    resources['weblink_url'].append(url)

    resources_no_nones = strip_nones(resources)

    try:
        resources = Resources(**resources_no_nones)
    except ValidationError:
        raise

    if resources:
        return resources
    else:
        return None


def strip_nones(dict_with_nones):
    """Remove any key-value pairs from dict for which the value is None.

    :param dict_with_nones: DICT
    :return: DICT
    """

    return {
        k: v for k, v in dict_with_nones.items()
        if v is not None
    }
