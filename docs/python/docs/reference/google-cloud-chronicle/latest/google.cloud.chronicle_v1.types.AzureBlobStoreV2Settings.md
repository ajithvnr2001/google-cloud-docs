---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.AzureBlobStoreV2Settings
title: Class AzureBlobStoreV2Settings (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:12.862950+00:00
---

# Class AzureBlobStoreV2Settings (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.AzureBlobStoreV2Settings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AzureBlobStoreV2Settings (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    AzureBlobStoreV2Settings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AzureBlobStoreV2Settings is the settings proto for Azure Blob Storage feeds.

## Attributes  
  
---  
**Name** | **Description**  
`azure_uri` |  `str`   
Required. Azure URI.   
`authentication` |  `[google.cloud.chronicle_v1.types.AzureAuthV2](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.AzureAuthV2)`   
Required. Authentication.   
`source_deletion_option` |  `[google.cloud.chronicle_v1.types.SourceDeletionOptionV2](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.SourceDeletionOptionV2)`   
Optional. Source deletion option.   
`max_lookback_days` |  `int`   
Optional. Maximum File Age to ingest in days.   
`chronicle_service_account` |  `str`   
Output only. SA that will read data, this is Storage Transfer Service SA of Customer's Tenancy Project.   
`include_prefixes` |  `MutableSequence[str]`   
Optional. Optional list of object prefixes to include.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
