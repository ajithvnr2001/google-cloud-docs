---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsRequest
title: Class ListExascaleDbStorageVaultsRequest (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:21.685905+00:00
---

# Class ListExascaleDbStorageVaultsRequest (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListExascaleDbStorageVaultsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListExascaleDbStorageVaultsRequest (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    ListExascaleDbStorageVaultsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The request for `ExascaleDbStorageVault.List`.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent value for ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.   
`page_size` |  `int`   
Optional. The maximum number of items to return. If unspecified, at most 50 ExascaleDbStorageVaults will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A token identifying a page of results the server should return.   
`filter` |  `str`   
Optional. An expression for filtering the results of the request. Filter the list as specified in https://google.aip.dev/160.   
`order_by` |  `str`   
Optional. An expression for ordering the results of the request. Order results as specified in https://google.aip.dev/132.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
