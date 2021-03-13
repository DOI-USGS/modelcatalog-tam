#!/usr/bin/env python

import json
from pathlib import Path

import config
from model_metadata_mappers import get_basic_profile_model


def read_files(file_list):
    for file in file_list:
        with open(file) as json_file:
            yield json.load(json_file)


def write_file(file, model):
    with open(file, 'w') as json_file:
        json_file.write(model.json(indent=2))


def main():
    if not config.SB_MODELS_OUT.is_dir():
        config.SB_MODELS_OUT.mkdir(parents=True, exist_ok=True)

    if not config.SB_MODELS_OUT.is_dir():
        config.SB_MODELS_OUT.mkdir(parents=True, exist_ok=True)

    new_sb_models = [str(file) for file in config.SB_MODELS_IN.iterdir()]
    new_sb_model_dicts = read_files(new_sb_models)
    for sb_model in new_sb_model_dicts:
        try:
            mcat_model = get_basic_profile_model(sb_model)
        except Exception as e:
            print(f'An exception was encountered with {sb_model["id"]}: {e}')
        else:
            path = Path.joinpath(config.SB_MODELS_OUT, f'{sb_model["id"]}.json')
            write_file(path, mcat_model)


if __name__ == '__main__':
    main()

# with open('../metadata_schema/json-schema/BasicProfile.json', 'w') as f:
#     # equivalent to json.dumps(BasicProfile.schema(), indent=2)
#     f.write(BasicProfile.schema_json(indent=2))
