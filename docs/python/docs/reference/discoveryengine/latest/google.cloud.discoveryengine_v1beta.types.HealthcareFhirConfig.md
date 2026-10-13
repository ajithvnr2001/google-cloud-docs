---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.HealthcareFhirConfig
title: Class HealthcareFhirConfig (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:13.452876+00:00
---

# Class HealthcareFhirConfig (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.HealthcareFhirConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HealthcareFhirConfig (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    HealthcareFhirConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Config to data store for `HEALTHCARE_FHIR` vertical.

## Attributes  
  
---  
**Name** | **Description**  
`enable_configurable_schema` |  `bool`   
Whether to enable configurable schema for `HEALTHCARE_FHIR` vertical. If set to `true`, the predefined healthcare fhir schema can be extended for more customized searching and filtering.   
`enable_static_indexing_for_batch_ingestion` |  `bool`   
Whether to enable static indexing for `HEALTHCARE_FHIR` batch ingestion. If set to `true`, the batch ingestion will be processed in a static indexing mode which is slower but more capable of handling larger volume.   
`initial_filter_groups` |  `MutableSequence[str]`   
Optional. Names of the Group resources to use as a basis for the initial patient filter, in format `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}/fhir/Group/{group_id}`. The filter group must be a FHIR resource name of type Group, and the filter will be constructed from the direct members of the group which are Patient resources.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
