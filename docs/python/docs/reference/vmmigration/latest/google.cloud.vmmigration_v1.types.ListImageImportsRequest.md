---
url: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.ListImageImportsRequest
title: Class ListImageImportsRequest (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:44.760164+00:00
---

# Class ListImageImportsRequest (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.ListImageImportsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListImageImportsRequest (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.3  1.10.0  1.9.1  1.8.5  1.7.0  1.6.2  1.5.1  1.4.0  1.3.3  1.2.0  1.1.2  1.0.0  0.1.0 
    
    
    ListImageImportsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for 'ListImageImports' call.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent, which owns this collection of targets.   
`page_size` |  `int`   
Optional. The maximum number of targets to return. The service may return fewer than this value. If unspecified, at most 500 targets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListImageImports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListImageImports` must match the call that provided the page token.   
`filter` |  `str`   
Optional. The filter request (according to AIP-160).   
`order_by` |  `str`   
Optional. The order by fields for the result (according to AIP-132). Currently ordering is only possible by "name" field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
