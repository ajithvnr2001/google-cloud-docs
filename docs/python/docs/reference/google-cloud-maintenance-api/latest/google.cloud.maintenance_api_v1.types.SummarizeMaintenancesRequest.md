---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesRequest
title: Class SummarizeMaintenancesRequest (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:24.001408+00:00
---

# Class SummarizeMaintenancesRequest (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SummarizeMaintenancesRequest (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    SummarizeMaintenancesRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for SummarizeMaintenances custom method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent of the resource maintenance. eg. `projects/123/locations/*`  
`page_size` |  `int`   
The maximum number of resource maintenances to send per page. The default page size is 20 and the maximum is 1000.   
`page_token` |  `str`   
The page token: If the next_page_token from a previous response is provided, this request will send the subsequent page.   
`filter` |  `str`   
Filter the list as specified in https://google.aip.dev/160. Supported fields include: \- `maintenance.maintenanceName` Examples: \- `maintenance.maintenanceName="eb3b709c-9ca1-5472-9fb6-800a3849eda1"`  
`order_by` |  `str`   
Order results as specified in https://google.aip.dev/132.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
