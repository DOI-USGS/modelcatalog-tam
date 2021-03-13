#!/usr/bin/env python

import json
from pathlib import Path

import config
from sciencebasepy import SbSession


sb = SbSession().login(config.SB_SERVICE_ACCOUNT, config.SB_PWD)
child_ids = sb.get_child_ids(config.PARENT_ID)
print(f"{len(child_ids)} models found")


def download_sb_models():
    """Download ScienceBase JSON objects.

    :return: None
    """

    if not config.SB_MODELS_IN.is_dir():
        config.SB_MODELS_IN.mkdir(parents=True, exist_ok=True)

    num_models_downloaded = 0

    for id_ in child_ids:

        fpath = Path.joinpath(config.SB_MODELS_IN, f'{id_}.json')
        if fpath.is_file():
            continue

        model_dict = sb.get_item(id_)
        model_json = json.dumps(model_dict, indent=2)

        with open(fpath, 'w') as file:
            file.write(model_json)
            num_models_downloaded += 1

    print(f"{num_models_downloaded} new models downloaded")


if __name__ == '__main__':
    download_sb_models()
