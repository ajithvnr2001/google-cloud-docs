---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListAccessibleDataAgentsRequest
title: Class ListAccessibleDataAgentsRequest (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:36.396313+00:00
---

# Class ListAccessibleDataAgentsRequest (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListAccessibleDataAgentsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListAccessibleDataAgentsRequest (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListAccessibleDataAgentsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Message for requesting list of accessible DataAgents.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent value for ListAccessibleDataAgentsRequest.   
`page_size` |  `int`   
Optional. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListAccessibleDataAgents` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccessibleDataAgents` must match the call that provided the page token. The service may return fewer than this value.   
`filter` |  `str`   
Optional. Filtering results. See `AIP-160 `__ for syntax.   
`order_by` |  `str`   
Optional. User specification for how to order the results.   
`show_deleted` |  `bool`   
Optional. If true, the list results will include soft-deleted DataAgents. Defaults to false.   
`creator_filter` |  `[google.cloud.geminidataanalytics_v1.types.ListAccessibleDataAgentsRequest.CreatorFilter](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListAccessibleDataAgentsRequest.CreatorFilter)`   
Optional. Filter for the creator of the agent.   
  
## Classes 

### CreatorFilter
    
    
    CreatorFilter(value)

Filter for the creator of the agent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
