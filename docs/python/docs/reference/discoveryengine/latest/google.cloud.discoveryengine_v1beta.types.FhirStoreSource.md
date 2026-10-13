---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FhirStoreSource
title: Class FhirStoreSource (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:02.158819+00:00
---

# Class FhirStoreSource (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FhirStoreSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FhirStoreSource (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    FhirStoreSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cloud FhirStore source import data from.

## Attributes  
  
---  
**Name** | **Description**  
`fhir_store` |  `str`   
Required. The full resource name of the FHIR store to import data from, in the format of `projects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}`.   
`gcs_staging_dir` |  `str`   
Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the FhirStore export to a specific Cloud Storage directory.   
`resource_types` |  `MutableSequence[str]`   
The FHIR resource types to import. The resource types should be a subset of all `supported FHIR resource types   
`update_from_latest_predefined_schema` |  `bool`   
Optional. Whether to update the DataStore schema to the latest predefined schema. If true, the DataStore schema will be updated to include any FHIR fields or resource types that have been added since the last import and corresponding FHIR resources will be imported from the FHIR store. Note this field cannot be used in conjunction with `resource_types`. It should be used after initial import.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
