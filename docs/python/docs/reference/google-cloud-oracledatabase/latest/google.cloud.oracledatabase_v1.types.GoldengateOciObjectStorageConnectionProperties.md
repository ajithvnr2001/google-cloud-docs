---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOciObjectStorageConnectionProperties
title: Class GoldengateOciObjectStorageConnectionProperties (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:07.980453+00:00
---

# Class GoldengateOciObjectStorageConnectionProperties (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOciObjectStorageConnectionProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GoldengateOciObjectStorageConnectionProperties (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    GoldengateOciObjectStorageConnectionProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The properties of GoldengateOciObjectStorageConnection.

## Attributes  
  
---  
**Name** | **Description**  
`technology_type` |  `str`   
Optional. The technology type of OciObjectStorageConnection.   
`tenancy_id` |  `str`   
Optional. The OCID of the related OCI tenancy.   
`region` |  `str`   
Optional. The name of the region of OCI Object Storage. e.g.: us-ashburn-1 If the region is not provided, backend will default to the default region.   
`user_id` |  `str`   
Optional. The OCID of the OCI user who will access the Object Storage. The user must have write access to the bucket they want to connect to.   
`private_key_file` |  `str`   
Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint.   
`private_key_passphrase_secret` |  `str`   
Optional. The passphrase of the private key.   
`public_key_fingerprint` |  `str`   
Optional. The fingerprint of the API Key of the user specified by the userId.   
`use_resource_principal` |  `bool`   
Optional. Specifies that the user intends to authenticate to the instance using a resource principal.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
