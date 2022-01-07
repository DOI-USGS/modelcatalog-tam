'''
Run script within the scripts directory

If the python context gives errors:

`cd metadata_schema` run python repl

>
>from BasicProfileSchema import BasicProfile
>with open('json-schema/BasicProfile.json', 'w') as f:
    f.write(BasicProfile.schema_json(indent=2))
'''

import os 
from pathlib import Path

#cpath = Path.cwd().parents[0]
#path = Path.joinpath(cpath, 'metadata_schema')

#os.chdir(npath)

print(Path.cwd())
from BasicProfileSchema import BasicProfile

with open('json-schema/BasicProfile.json', 'w') as f:
    f.write(BasicProfile.schema_json(indent=2))
