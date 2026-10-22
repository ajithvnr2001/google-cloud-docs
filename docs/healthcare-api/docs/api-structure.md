---
url: https://docs.cloud.google.com/healthcare-api/docs/api-structure/
title: API structure \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:46.260992+00:00
---

# API structure  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/api-structure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  API structure Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the structure of Cloud Healthcare API paths and operations and how they can be used to access and manage data.

## Overview

Healthcare data in datasets and data stores can be accessed and managed using a REST API that identifies each data store using:

  * A Google Cloud project
  * A Google Cloud location
  * The dataset ID
  * The data store type
  * The data store ID



The API also implements modality-specific standards for access that are consistent with industry standards for that modality.

## Administrative operations

Administrative operations are available for datasets and all data stores. They primarily consist of creating, reading, updating, and deleting (CRUD) datasets and data stores. Administrative operations are consistent with most Google Cloud (Google Cloud) APIs and do not require any adherence to specific modality standards.

Examples of administrative operations include:

  * Creating, deleting, getting, listing, and patching datasets and data stores
  * Setting, getting, and testing IAM permissions



## Resource names

A resource name consists of, at minimum, a project ID and a location. It can extend to include a dataset, data store, and any of a data store's child resources.

The format for a resource name for a data store that resides within a Cloud Healthcare API dataset looks like this:

`/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/DATA_STORE_TYPE/DATA_STORE_ID`

For example, the resource name for an HL7v2 store called `clinical-store1` looks like this:

`/projects/my-project/locations/us-central1/datasets/my-dataset/hl7V2Stores/clinical-store1`

This resource name shows a project called `my-project` in the `us-central1` region. The project contains a dataset called `my-dataset`, and the dataset contains an HL7v2 store called `clinical-store1`.

Operations on a location, dataset, data store, or any of a data store's child resources all require that a resource name is provided either in the REST path or the gRPC request.

## Modality paths for modality-specific operations

Operations that access data in a modality-specific data store use a request path that consists of two pieces: the resource name (for identifying the data store to access), and a modality path (for identifying the actual data to retrieve).

### FHIR resource modality paths

For example, the full request path for reading a specific FHIR Patient resource using the patient's ID might look like the following:

`RESOURCE_NAME/resources/Patient/PATIENT_ID`

with `/Patient/PATIENT_ID` being the modality path (structured according to the FHIR standard) for the Patient resource whose identifier is specified by `PATIENT_ID`.

### DICOMweb modality paths

DICOMweb requests to retrieve all studies for a given patient would look like this:

`RESOURCE_NAME/dicomWeb/studies?PatientName=PATIENT_NAME`

As another example, a request to retrieve all instances in a given study and series would look like this:

`RESOURCE_NAME/dicomWeb/studies/STUDY_UID/series/SERIES_UID/instances`

A request to retrieve an instance would look like this:

`RESOURCE_NAME/dicomWeb/studies/STUDY_UID/series/SERIES_UID/instances/INSTANCE_UID`

In all of these examples, the modality path specification is consistent with the DICOMweb standard path structure.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
