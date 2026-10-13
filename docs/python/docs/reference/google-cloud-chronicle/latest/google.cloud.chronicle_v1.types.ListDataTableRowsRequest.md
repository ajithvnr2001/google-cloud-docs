---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.ListDataTableRowsRequest
title: Class ListDataTableRowsRequest (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:04.052545+00:00
---

# Class ListDataTableRowsRequest (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.ListDataTableRowsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListDataTableRowsRequest (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListDataTableRowsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request to list data table rows.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource id of the data table. Format: projects/{project}/locations/{locations}/instances/{instance}/dataTables/{data_table}   
`page_size` |  `int`   
Optional. The maximum number of data table rows to return. The service may return fewer than this value. If unspecified, at most 100 data table rows will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListDataTableRows` call.   
`order_by` |  `str`   
Optional. Configures ordering of DataTables in the response. Note: Our implementation currently supports order by "create_time asc" only   
`filter` |  `str`   
Optional. Filter facilitating search over data table rows. This filter performs a case-insensitive substring match on the row values.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
