---
url: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1.types.QueryHubStatusRequest
title: Class QueryHubStatusRequest (2.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:59.956168+00:00
---

# Class QueryHubStatusRequest (2.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1.types.QueryHubStatusRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QueryHubStatusRequest (2.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.18.0 (latest)  2.17.0  2.16.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1  2.6.0  2.5.1  2.4.5  2.3.0  2.2.0  2.0.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.2  1.1.0  1.0.1  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    QueryHubStatusRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request for HubService.QueryHubStatus.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the hub.   
`page_size` |  `int`   
Optional. The maximum number of results to return per page.   
`page_token` |  `str`   
Optional. The page token.   
`filter` |  `str`   
Optional. An expression that filters the list of results. The filter can be used to filter the results by the following fields: \- `psc_propagation_status.source_spoke` \- `psc_propagation_status.source_group` \- `psc_propagation_status.source_forwarding_rule` \- `psc_propagation_status.target_spoke` \- `psc_propagation_status.target_group` \- `psc_propagation_status.code` \- `psc_propagation_status.message`  
`order_by` |  `str`   
Optional. Sort the results in ascending order by the specified fields. A comma-separated list of any of these fields: \- `psc_propagation_status.source_spoke` \- `psc_propagation_status.source_group` \- `psc_propagation_status.source_forwarding_rule` \- `psc_propagation_status.target_spoke` \- `psc_propagation_status.target_group` \- `psc_propagation_status.code` If `group_by` is set, the value of the `order_by` field must be the same as or a subset of the `group_by` field.   
`group_by` |  `str`   
Optional. Aggregate the results by the specified fields. A comma-separated list of any of these fields: \- `psc_propagation_status.source_spoke` \- `psc_propagation_status.source_group` \- `psc_propagation_status.source_forwarding_rule` \- `psc_propagation_status.target_spoke` \- `psc_propagation_status.target_group` \- `psc_propagation_status.code`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
