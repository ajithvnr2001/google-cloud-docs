---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/dicom/
title: DICOM \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:19.189516+00:00
---

# DICOM  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/dicom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  DICOM Stay organized with collections  Save and categorize content based on your preferences. 

Digital Imaging and Communications in Medicine (DICOM) is an international standard used for medical images such as X-rays, MRIs, ultrasounds, and other medical imaging modalities.

The Cloud Healthcare API provides operations for reading DICOM instances, studies, and series that are consistent with the DICOMweb standard, and supports the DICOM DIMSE C-STORE operation using an [open source adapter](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter).

See the [DICOM](https://www.dicomstandard.org/about/) documentation for more details on DICOM.

## DICOM stores

A _DICOM store_ is a data store in the Cloud Healthcare API that holds all of your DICOM instances. DICOM stores exist inside datasets.

The [`DicomStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores) resource provides a representation of a DICOM store's attributes. For each of your DICOM stores, you can choose whether to publish changes to the DICOM store (such as the ingestion of a new instance into the store) to a [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/dicom-pubsub) topic.

## DICOMweb conformance

See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on the DICOMweb implementation in the Cloud Healthcare API.

The DICOMweb implementation in the Cloud Healthcare API only supports REST, not RPC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
