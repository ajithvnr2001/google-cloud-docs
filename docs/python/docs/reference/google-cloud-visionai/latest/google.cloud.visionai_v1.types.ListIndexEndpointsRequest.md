---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListIndexEndpointsRequest
title: Class ListIndexEndpointsRequest (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:07.688061+00:00
---

# Class ListIndexEndpointsRequest (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListIndexEndpointsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListIndexEndpointsRequest (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    ListIndexEndpointsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for ListIndexEndpoints.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Format: `projects/{project}/locations/{location}`  
`page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. The service may return fewer than this value. If unspecified, a page size of 50 will be used. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A token identifying a page of results the server should return.   
`filter` |  `str`   
Optional. The filter applied to the returned list. We only support filtering for the `deployed_image_index.image_index` field. However, to filter by a corpus instead of an image index, simply use `deployed_image_index.corpus`, which will return all endpoints with `deployed_image_index.image_index` inside of the given corpus. A basic filter on image index would look like: deployed_image_index.image_index = "projects/123/locations/us-central1/corpora/my_corpus/imageIndexes/my_image_index" A basic filter on corpus would look like: deployed_image_index.corpus = "projects/123/locations/us-central1/corpora/my_corpus".   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
