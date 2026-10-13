---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListMirroringEndpointGroupsRequest
title: Class ListMirroringEndpointGroupsRequest (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:32.497376+00:00
---

# Class ListMirroringEndpointGroupsRequest (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListMirroringEndpointGroupsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListMirroringEndpointGroupsRequest (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    ListMirroringEndpointGroupsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for ListMirroringEndpointGroups.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent, which owns this collection of endpoint groups. Example: `projects/123456789/locations/global`. See https://google.aip.dev/132 for more details.   
`page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. See https://google.aip.dev/158 for more details.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListMirroringEndpointGroups` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListMirroringEndpointGroups` must match the call that provided the page token. See https://google.aip.dev/158 for more details.   
`filter` |  `str`   
Optional. Filter expression. See https://google.aip.dev/160#filtering for more details.   
`order_by` |  `str`   
Optional. Sort expression. See https://google.aip.dev/132#ordering for more details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
