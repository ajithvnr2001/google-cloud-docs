---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListDataSchemasRequest
title: Class ListDataSchemasRequest (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:44.176704+00:00
---

# Class ListDataSchemasRequest (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListDataSchemasRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListDataSchemasRequest (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    ListDataSchemasRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for ListDataSchemas.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent, which owns this collection of data schemas. Format: projects/{project_number}/locations/{location_id}/corpora/{corpus_id}   
`page_size` |  `int`   
The maximum number of data schemas to return. The service may return fewer than this value. If unspecified, at most 50 data schemas will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
A page token, received from a previous `ListDataSchemas` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataSchemas` must match the call that provided the page token.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
