---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdentityMappingStore
title: Class IdentityMappingStore (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:44.814670+00:00
---

# Class IdentityMappingStore (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdentityMappingStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IdentityMappingStore (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    IdentityMappingStore(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Identity Mapping Store which contains Identity Mapping Entries.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. The full resource name of the identity mapping store. Format: `projects/{project}/locations/{location}/identityMappingStores/{identity_mapping_store}`. This field must be a UTF-8 encoded string with a length limit of 1024 characters.   
`kms_key_name` |  `str`   
Input only. The KMS key to be used to protect this Identity Mapping Store at creation time. Must be set for requests that need to comply with CMEK Org Policy protections. If this field is set and processed successfully, the Identity Mapping Store will be protected by the KMS key, as indicated in the cmek_config field.   
`cmek_config` |  `[google.cloud.discoveryengine_v1beta.types.CmekConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CmekConfig)`   
Output only. CMEK-related information for the Identity Mapping Store.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
