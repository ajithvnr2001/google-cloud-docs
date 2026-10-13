---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-capacityplanner/latest/google.cloud.capacityplanner_v1beta.types.GcsDestination
title: Class GcsDestination (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:50.689268+00:00
---

# Class GcsDestination (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-capacityplanner/latest/google.cloud.capacityplanner_v1beta.types.GcsDestination

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GcsDestination (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    GcsDestination(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Cloud Storage location.

## Attributes  
  
---  
**Name** | **Description**  
`uri` |  `str`   
Optional. The path to the file in Cloud Storage where the export will be stored. The URI is in the form `gs://bucketName/fileName`. If the file already exists, the request succeeds, but the operation fails.   
`bucket` |  `str`   
Required. The bucket name to which the export will be stored.   
`object_` |  `str`   
Required. The object name to which the export will be stored.   
`force` |  `bool`   
Optional. Flag to indicate overwrite in case file already exists.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
