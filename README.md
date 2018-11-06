### DOCKER
docker run -it -v ~/scw_repos/lxml:/mnt lambci/lambda:build-python3.6 bash

```bash
# on container
pip install lxml -t /mnt/
```

#### update the setup.py with new version number if changing
