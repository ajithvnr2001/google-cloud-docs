---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AlloyDbSource
title: Class AlloyDbSource (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:36.460212+00:00
---

# Class AlloyDbSource (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AlloyDbSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AlloyDbSource (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    AlloyDbSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AlloyDB source import data from.

## Attributes  
  
---  
**Name** | **Description**  
`project_id` |  `str`   
The project ID that contains the AlloyDB source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request.   
`location_id` |  `str`   
Required. The AlloyDB location to copy the data from with a length limit of 256 characters.   
`cluster_id` |  `str`   
Required. The AlloyDB cluster to copy the data from with a length limit of 256 characters.   
`database_id` |  `str`   
Required. The AlloyDB database to copy the data from with a length limit of 256 characters.   
`table_id` |  `str`   
Required. The AlloyDB table to copy the data from with a length limit of 256 characters.   
`gcs_staging_dir` |  `str`   
Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the AlloyDB export to a specific Cloud Storage directory. Ensure that the AlloyDB service account has the necessary Cloud Storage Admin permissions to access the specified Cloud Storage directory.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
