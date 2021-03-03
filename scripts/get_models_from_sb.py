#!/usr/bin/env python

import json
import os
from pathlib import Path

from sciencebasepy import SbSession


PACKAGE_DIR = Path(__file__).absolute().parent.parent
SB_MODELS_DIR = Path.joinpath(PACKAGE_DIR, 'sb_models/unprocessed_sb_models')

PARENT_ID = os.environ.get('PARENT_ID')
SB_PWD = os.environ.get('SB_PWD')
SB_SERVICE_ACCOUNT = os.environ.get('SB_SERVICE_ACCOUNT')

sb = SbSession().login(SB_SERVICE_ACCOUNT, SB_PWD)
child_ids = sb.get_child_ids(PARENT_ID)
print(f"{len(child_ids)} models found")


def download_sb_models():

    num_models_downloaded = 0

    for id_ in child_ids:

        fpath = Path.joinpath(SB_MODELS_DIR, f'{id_}.json')
        if fpath.is_file():
            continue

        model_dict = sb.get_item(id_)
        model_json = json.dumps(model_dict, indent=4)

        with open(fpath, 'w') as file:
            file.write(model_json)
            num_models_downloaded += 1

    print(f"{num_models_downloaded} new models downloaded")


if __name__ == '__main__':
    download_sb_models()
