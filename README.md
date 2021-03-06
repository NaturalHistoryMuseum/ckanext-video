<img src=".github/nhm-logo.svg" align="left" width="150px" height="100px" hspace="40"/>

# ckanext-video

[![Travis](https://img.shields.io/travis/NaturalHistoryMuseum/ckanext-video/master.svg?style=flat-square)](https://travis-ci.org/NaturalHistoryMuseum/ckanext-video)
[![Coveralls](https://img.shields.io/coveralls/github/NaturalHistoryMuseum/ckanext-video/master.svg?style=flat-square)](https://coveralls.io/github/NaturalHistoryMuseum/ckanext-video)
[![CKAN](https://img.shields.io/badge/ckan-2.9.0a-orange.svg?style=flat-square)](https://github.com/ckan/ckan)

_A CKAN extension for embedding Youtube or Vimeo videos as views._


# Overview

Adds an 'Embedded Video' view type, which displays a video from YouTube or Vimeo (either using the resource URL or a different URL).


# Installation

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

# Configuration

There are currently no options that can be specified in your .ini config file.


# Usage

After enabling this extension in the list of plugins, the Embedded Video view should become available for resources. The resource does not have to link to the video; the URL can be overridden when creating the view.


# Testing

_Test coverage is currently extremely limited._

To run the tests, use nosetests inside your virtualenv. The `--nocapture` flag will allow you to see the debug statements.
```bash
nosetests --ckan --with-pylons=$TEST_CONFIG_FILE --where=$INSTALL_FOLDER/src/ckanext-video --nologcapture --nocapture
```
