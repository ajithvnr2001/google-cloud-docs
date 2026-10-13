---
url: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ListInstancesRequest
title: Class ListInstancesRequest (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:26.140846+00:00
---

# Class ListInstancesRequest (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ListInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListInstancesRequest (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.5  2.14.0  2.13.1  2.12.1  2.11.1  2.10.0  2.9.3  2.8.1  2.7.1  2.6.0  2.5.1  2.4.1  2.3.0  2.2.4  2.1.1  2.0.0  1.0.2  0.4.0  0.3.0 
    
    
    ListInstancesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for ListInstances.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region.   
`page_size` |  `int`   
The maximum number of items to return. If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's [`next_page_token`][google.cloud.redis.v1beta1.ListInstancesResponse.next_page_token] to determine if there are more instances left to be queried.   
`page_token` |  `str`   
The `next_page_token` value returned from a previous ListInstances request, if any.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
