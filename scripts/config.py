#!/usr/bin/env python

import os
from pathlib import Path

# Sets the parent path to ~/path/to/repo/modelcatalog-tam
PACKAGE_DIR = Path(__file__).absolute().parent.parent
SB_MODELS_IN = Path.joinpath(PACKAGE_DIR, 'sb_models/unprocessed_sb_models')
SB_MODELS_OUT = Path.joinpath(PACKAGE_DIR, 'sb_models/processed_sb_models')

PARENT_ID = os.environ.get('PARENT_ID')
SB_PWD = os.environ.get('SB_PWD')
SB_SERVICE_ACCOUNT = os.environ.get('SB_SERVICE_ACCOUNT')
