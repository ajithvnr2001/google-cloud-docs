---
url: https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferOptions.OverwriteWhen
title: Class OverwriteWhen (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:37.036872+00:00
---

# Class OverwriteWhen (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/storagetransfer/latest/google.cloud.storage_transfer_v1.types.TransferOptions.OverwriteWhen

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class OverwriteWhen (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.1  1.12.0  1.11.5  1.10.0  1.9.2  1.8.1  1.7.1  1.6.0  1.5.2  1.4.1  1.3.1  1.2.1  1.1.1  1.0.2  0.1.0 
    
    
    OverwriteWhen(value)

Specifies when to overwrite an object in the sink when an object with matching name is found in the source.

## Enums  
  
---  
**Name** | **Description**  
`OVERWRITE_WHEN_UNSPECIFIED` | Overwrite behavior is unspecified.  
`DIFFERENT` | Overwrites destination objects with the source objects, only if the objects have the same name but different HTTP ETags or checksum values.  
`NEVER` | Never overwrites a destination object if a source object has the same name. In this case, the source object is not transferred.  
`ALWAYS` | Always overwrite the destination object with the source object, even if the HTTP Etags or checksum values are the same.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
