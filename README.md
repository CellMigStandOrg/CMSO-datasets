[![Build Status](https://travis-ci.org/CellMigStandOrg/CMSO-datasets.svg?branch=master)](https://travis-ci.org/CellMigStandOrg/CMSO-datasets)

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

In order to submit a new dataset, a minimal set of information needs to be provided.

How to propose changes to an existing dataset?
----------------------------------------------

We welcome issues in the [tracker](https://github.com/CellMigStandOrg/CMSO-datasets/issues) as well as Pull Requests
suggesting changes to the datasets available in this repository.
