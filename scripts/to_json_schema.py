'''
Run script within the scripts directory
'''

import os 
from pathlib import Path

cpath = Path.cwd().parents[0]
npath = Path.joinpath(cpath, 'metadata_schema')

os.chdir(npath)

from BasicProfileSchema import BasicProfile

with open('json-schema/BasicProfile.json', 'w') as f:
    f.write(BasicProfile.schema_json(indent=2))
