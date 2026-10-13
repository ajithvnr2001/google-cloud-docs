---
url: https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.ListInstancesResponse
title: Class ListInstancesResponse (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:29.247540+00:00
---

# Class ListInstancesResponse (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.ListInstancesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListInstancesResponse (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.0  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.5  1.8.0  1.7.0  1.6.2  1.5.1  1.4.1  1.3.0  1.2.3  1.1.3  1.0.0  0.2.3  0.1.0 
    
    
    ListInstancesResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ListInstancesResponse is the result of ListInstancesRequest.

## Attributes  
  
---  
**Name** | **Description**  
`instances` |  `MutableSequence[[google.cloud.filestore_v1.types.Instance](https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.Instance)]`   
A list of instances in the project for the specified location. If the `{location}` value in the request is "-", the response contains a list of instances from all locations. If any location is unreachable, the response will only return instances in reachable locations and the "unreachable" field will be populated with a list of unreachable locations.   
`next_page_token` |  `str`   
The token you can use to retrieve the next page of results. Not returned if there are no more results in the list.   
`unreachable` |  `MutableSequence[str]`   
Unordered list. Locations that could not be reached.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
