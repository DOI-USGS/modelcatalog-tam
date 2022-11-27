# tam

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Generic badge](https://img.shields.io/badge/Version-1.0.3-<COLOR>.svg)]()

# USGS Model Catalog Tools and Metadata

This project contains the metadata schema component of a modular catalog implementation. This example is for the USGS Model Catalog (https://data.usgs.gov/modelcatalog), which provides access to metadata that describes scientific models used in the USGS. Metadata are stored as JSON files. Other catalog components include a web presence, a repository component, and auxiliary tools like metadata entry forms.

The repository of metadata files is available in the Model Catalog intake repo (https://doi.org/10.5066/P9IVG9VZ).

## USGS Software Release Information

The official USGS software release can be found at https://doi.org/10.5066/P9WU0F71 and cited as follows:

Serna, Brandon and Hsu, Leslie, 2022. USGS Model Catalog Tools and Metadata (tam) Version 1.0.3, U.S. Geological Survey software release, https://doi.org/10.5066/P9WU0F71.

A provisional, development version is available at https://code.usgs.gov/sas/sdm/model-catalog/tam. 

The main branch will have the most up-to-date version of the code.  

IP-144090 

## Contacts
- Brandon Serna (bserna@usgs.gov), Lead developer
- Leslie Hsu (lhsu@usgs.gov), Product owner

## Metadata Schema Diagram

![](./diagrams/basicprofile-diagram.png)

## Versioning

Schema versioning can be found as a private model attribute within each schema as `model._version` and will follow semver standards (major.minor.patch)

## Requirements

The requirements.txt file lists required python packages for running tests.


## License

Unless otherwise noted, This project is in the public domain in the United
States because it contains materials that originally came from the United
States Geological Survey, an agency of the United States Department of
Interior. For more information, see the official USGS copyright policy at
https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits

Additionally, we waive copyright and related rights in the work
worldwide through the CC0 1.0 Universal public domain dedication.


### CC0 1.0 Universal Summary
-------------------------

This is a human-readable summary of the
[Legal Code (read the full text)][1].


#### No Copyright

The person who associated a work with this deed has dedicated the work to
the public domain by waiving all of his or her rights to the work worldwide
under copyright law, including all related and neighboring rights, to the
extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission.


#### Other Information

In no way are the patent or trademark rights of any person affected by CC0,
nor are the rights that other persons may have in the work or in how the
work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with
this deed makes no warranties about the work, and disclaims liability for
all uses of the work, to the fullest extent permitted by applicable law.
When using or citing the work, you should not imply endorsement by the
author or the affirmer.

## Disclaimer

This software is preliminary or provisional and is subject to revision. It is
being provided to meet the need for timely best science. The software has not
received final approval by the U.S. Geological Survey (USGS). No warranty,
expressed or implied, is made by the USGS or the U.S. Government as to the
functionality of the software and related material nor shall the fact of release
constitute any such warranty. The software is provided on the condition that
neither the USGS nor the U.S. Government shall be held liable for any damages
resulting from the authorized or unauthorized use of the software.



[1]: https://creativecommons.org/publicdomain/zero/1.0/legalcode
