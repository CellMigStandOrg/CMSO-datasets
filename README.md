[![Build Status](https://travis-ci.org/CellMigStandOrg/CMSO-datasets.svg?branch=master)](https://travis-ci.org/CellMigStandOrg/CMSO-datasets)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

CMSO datasets
=============

This repository contains metadata files for cell migration datasets curated, or in the process of being curated, by
the Cell Migration Standardisation Organisation (CMSO).

Each folder represents a given dataset and has a unique accession number. Within each folder, the top-level README describes
the dataset linking to the reference publication if available, it indicates the level of curation performed and what metadata
files are included.

After the curation is performed, the expected metadata files represent the three units of information defined by CMSO:

- the experimental setup, expressed using the [ISA](http://isa-tools.org) format
- the imaging metadata, expressed via [OME companion files](https://www.openmicroscopy.org/site/support/ome-model/ome-tiff/file-structure.html)
- the tracking data, expressed using the CMSO [Biotracks](https://github.com/CellMigStandOrg/biotracks) format

How to add a new dataset?
-------------------------

In order to submit a new dataset, a minimal set of information needs to be provided based on the [MIACME](https://github.com/CellMigStandOrg/MIACME) guidelines.

How to propose changes to an existing dataset?
----------------------------------------------

We welcome issues in the [tracker](https://github.com/CellMigStandOrg/CMSO-datasets/issues) as well as Pull Requests
suggesting changes to the datasets available in this repository.

How to run the dataset validation code from this repository?
------------------------------------------------------------

If you would like to run locally the dataset validation code from this repository, you can follow the following steps:

1. Clone the repository
   ```git clone https://github.com/CellMigStandOrg/CMSO-datasets```
1. We suggest you use a python virtual environment. So, if not already installed in your system, first install the virtual environment via `pip`:
   `pip install virtualenv`
1. Create a virtual environment:
   `virtualenv venv`
1. Then, activate the virtual environment:
  `source venv/bin/activate`
1. Install the requirements:
  `pip install -r requirements.txt`
1. Validate the ISA metadata:
   `python check_isa.py`
1. Validate the biotracks datapackage:
   `python check_dpkg.py`


