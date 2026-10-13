---
url: https://docs.cloud.google.com/python/docs/reference/beyondcorpappconnections/latest/google.cloud.beyondcorp_appconnections_v1.types.ListAppConnectionsRequest
title: Class ListAppConnectionsRequest (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:34.161055+00:00
---

# Class ListAppConnectionsRequest (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/beyondcorpappconnections/latest/google.cloud.beyondcorp_appconnections_v1.types.ListAppConnectionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListAppConnectionsRequest (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.0  0.4.18  0.3.0  0.2.2  0.1.1 
    
    
    ListAppConnectionsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for BeyondCorp.ListAppConnections.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`  
`page_size` |  `int`   
Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.   
`page_token` |  `str`   
Optional. The next_page_token value returned from a previous ListAppConnectionsRequest, if any.   
`filter` |  `str`   
Optional. A filter specifying constraints of a list operation.   
`order_by` |  `str`   
Optional. Specifies the ordering of results. See `Sorting order   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
