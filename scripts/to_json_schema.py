import os 
os.chdir('./metadata_schema')

from BasicProfileSchema import BasicProfile

with open('json-schema/BasicProfile.json', 'w') as f:
    f.write(BasicProfile.schema_json(indent=2))
