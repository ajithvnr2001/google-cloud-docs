---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/deidentify/
title: De-identifying sensitive data \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:20.506966+00:00
---

# De-identifying sensitive data  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/deidentify/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  De-identifying sensitive data Stay organized with collections  Save and categorize content based on your preferences. 

**Disclaimer** : This operation processes data using a mixture of rules-based and heuristic methods. Results may differ between resources and datasets due to factors like input data quality/consistency, heuristic-based algorithms, and others. This feature is not guaranteed to satisfy any specific legal, regulatory, or compliance requirements, including requirements for the de-identification of data. It is the user's responsibility to ensure that they set the appropriate configuration parameters for the operation and evaluate the end result to determine whether it is acceptable for their use cases and any legal, regulatory, or compliance requirements they may have.

De-identification is the process of removing identifying information from data. The Cloud Healthcare API detects sensitive data in [DICOM instances](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify) and [FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify), such as protected health information (PHI), and then uses a de-identification transformation to mask, delete, or otherwise obscure the data. De-identification has multiple uses cases, including:

  * When sharing health information with non-privileged parties
  * When creating datasets from multiple sources and analyzing them
  * When anonymizing data so that it can be used in machine learning models



##  De-identification overview 

De-identification works at the following levels: 

  * At the dataset level. De-identification occurs on all data in DICOM stores and FHIR stores in the dataset. If a dataset contains both DICOM instances and FHIR resources, you can de-identify all of the instances and resources at the same time.  
  
To de-identify sensitive data at the dataset level, call the Cloud Healthcare API [`datasets.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/deidentify) method.
  * At the FHIR store level. De-identification occurs on all data in a specific FHIR store in a dataset.  
  
To de-identify sensitive data at the FHIR store level, call the Cloud Healthcare API [`fhirStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify) method.
  * At the DICOM store level. De-identification occurs on all data in a specific DICOM store in a dataset.  
  
To de-identify sensitive data at the DICOM store level, call the Cloud Healthcare API [`dicomStores.deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/deidentify) method.



De-identification doesn't impact the original dataset, FHIR store, DICOM store, or the original data. Depending on how you configure the de-identification, the operation behaves as follows: 

  * If you are de-identifying data at the dataset level, de-identified copies of the original data are written to a new dataset called the _destination dataset_.
  * If you are de-identifying data at the DICOM or FHIR store level, de-identified copies of the original data are written to an existing DICOM or FHIR store in an existing dataset. The output DICOM store and FHIR store are called the _destination DICOM store_ and _destination FHIR store_ , respectively.



The source dataset, FHIR store, or DICOM store and the destination dataset, FHIR store, or DICOM store must reside in the same Google Cloud location. De-identifying data across multiple Google Cloud locations is not supported. 

##  De-identification location 

When the Cloud Healthcare API de-identifies data, the data might be processed in a location that is different from where the source and destination FHIR or DICOM store resides. After de-identification finishes, the data is stored in the same Google Cloud location as the source FHIR store or DICOM store. 

To ensure data is processed in the same location as the source FHIR or DICOM store, you can specify the `useRegionalDataProcessing` option in [`DeidentifyConfig`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#DeidentifyConfig). 

##  De-identifying data in the Google Cloud console 

You can de-identify data for a dataset, FHIR store, or DICOM store from within the Google Cloud console. For more information see [De-identifying data in the Google Cloud console (DICOM)](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify#de-identifying_data_in_the) and [De-identifying data in the Google Cloud console (FHIR)](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-deidentify#de-identifying_data_in_the). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
