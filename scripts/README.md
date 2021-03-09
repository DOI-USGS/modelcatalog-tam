## Downloading ScienceBase Models

### Run
---
```shell
$ cd scripts
$ python get_models_from_sb.py
108 models found
108 new models downloaded
```
Downloaded files will be in the path specified by `config.SB_MODELS_IN`. This can take a few seconds.
  
### Troubleshooting
---
Problem: `Exception: Login failed`  
Solutions:
   1. Check that you are on the VPN  
   2. Check that `SB_SERVICE_ACCOUNT` and `SB_PWD` are set in your environment

## Converting ScienceBase Models to Model Catalog Models

### Run
---
```shell
$ cd scripts
$ python to_json_schema.py
```
Converted files will be in the path specified by `config.SB_MODELS_OUT`. Don't blink or you'll miss it.
