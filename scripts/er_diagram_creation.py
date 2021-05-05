import erdantic as erd
#from erdantic.examples.pydantic import Part
import os 
from pathlib import Path

cpath = Path.cwd().parents[0]
npath = Path.joinpath(cpath, 'metadata_schema')

os.chdir(npath)

from BasicProfileSchema import BasicProfile

# Back up to the normal directory
os.chdir(Path.cwd())
# Easy one-liner
erd.draw(BasicProfile, out="../diagrams/basicprofile-diagram.png")
