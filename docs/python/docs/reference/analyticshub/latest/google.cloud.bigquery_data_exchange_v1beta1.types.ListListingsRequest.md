---
url: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsRequest
title: Class ListListingsRequest (0.9.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:56.537751+00:00
---

# Class ListListingsRequest (0.9.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListListingsRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.20  0.4.20  0.3.2  0.2.1  0.1.1 
    
    
    ListListingsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for requesting the list of listings.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource path of the listing. e.g. `projects/myproject/locations/US/dataExchanges/123`.   
`page_size` |  `int`   
The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection.   
`page_token` |  `str`   
Page token, returned by a previous call, to request the next page of results.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
