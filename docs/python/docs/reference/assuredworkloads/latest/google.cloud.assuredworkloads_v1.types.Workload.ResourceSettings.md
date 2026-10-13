---
url: https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload.ResourceSettings
title: Class ResourceSettings (2.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:44.408619+00:00
---

# Class ResourceSettings (2.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload.ResourceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceSettings (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.0 (latest)  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.15.2  1.14.0  1.13.1  1.12.5  1.11.0  1.10.3  1.9.1  1.8.1  1.7.0  1.6.1  1.5.0  1.4.2  1.3.0  1.2.3  1.1.0  1.0.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.2  0.3.1  0.2.1  0.1.0 
    
    
    ResourceSettings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represent the custom settings for the resources to be created.

## Attributes  
  
---  
**Name** | **Description**  
`resource_id` |  `str`   
Resource identifier. For a project this represents project_id. If the project is already taken, the workload creation will fail. For KeyRing, this represents the keyring_id. For a folder, don't set this value as folder_id is assigned by Google.   
`resource_type` |  `[google.cloud.assuredworkloads_v1.types.Workload.ResourceInfo.ResourceType](https://docs.cloud.google.com/python/docs/reference/assuredworkloads/latest/google.cloud.assuredworkloads_v1.types.Workload.ResourceInfo.ResourceType)`   
Indicates the type of resource. This field should be specified to correspond the id to the right resource type (CONSUMER_FOLDER or ENCRYPTION_KEYS_PROJECT)   
`display_name` |  `str`   
User-assigned resource display name. If not empty it will be used to create a resource with the specified name.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
