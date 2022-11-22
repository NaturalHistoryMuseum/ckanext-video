<!--header-start-->
<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-video

[![Tests](https://img.shields.io/github/workflow/status/NaturalHistoryMuseum/ckanext-video/Tests?style=flat-square)](https://github.com/NaturalHistoryMuseum/ckanext-video/actions/workflows/main.yml)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-video/main?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-video)
[![CKAN](https://img.shields.io/badge/ckan-2.9.1-orange.svg?style=flat-square)](https://github.com/ckan/ckan)
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/)
[![Docs](https://img.shields.io/readthedocs/ckanext-video?style=flat-square)](https://ckanext-video.readthedocs.io)

_A CKAN extension for embedding Youtube or Vimeo videos as views._

<!--header-end-->

# Overview

<!--overview-start-->
Adds an 'Embedded Video' view type, which displays a video from YouTube or Vimeo (either using the resource URL or a different URL).

<!--overview-end-->

# Installation

<!--installation-start-->
Path variables used below:
- `$INSTALL_FOLDER` (i.e. where CKAN is installed), e.g. `/usr/lib/ckan/default`
- `$CONFIG_FILE`, e.g. `/etc/ckan/default/development.ini`

1. Clone the repository into the `src` folder:

  ```bash
  cd $INSTALL_FOLDER/src
  git clone https://github.com/NaturalHistoryMuseum/ckanext-video.git
  ```

2. Activate the virtual env:

  ```bash
  . $INSTALL_FOLDER/bin/activate
  ```

3. Install the requirements from requirements.txt:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-video
  pip install -r requirements.txt
  ```

4. Run setup.py:

  ```bash
  cd $INSTALL_FOLDER/src/ckanext-video
  python setup.py develop
  ```

5. Add 'video' to the list of plugins in your `$CONFIG_FILE`:

  ```ini
  ckan.plugins = ... video
  ```

<!--installation-end-->

# Configuration

<!--configuration-start-->
There are currently no options that can be specified in your .ini config file.

<!--configuration-end-->

# Usage

<!--usage-start-->
After enabling this extension in the list of plugins, the Embedded Video view should become available for resources. The resource does not have to link to the video; the URL can be overridden when creating the view.

<!--usage-end-->

# Testing

<!--testing-start-->
There is a Docker compose configuration available in this repository to make it easier to run tests.

To run the tests against ckan 2.9.x on Python3:

1. Build the required images
```bash
docker-compose build
```

2. Then run the tests.
   The root of the repository is mounted into the ckan container as a volume by the Docker compose
   configuration, so you should only need to rebuild the ckan image if you change the extension's
   dependencies.
```bash
docker-compose run ckan
```

The ckan image uses the Dockerfile in the `docker/` folder.

<!--testing-end-->
