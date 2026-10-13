---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesRequest
title: Class ListTemplatesRequest (0.4.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:06.160060+00:00
---

# Class ListTemplatesRequest (0.4.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListTemplatesRequest (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.4.2  0.3.0  0.2.0  0.1.5 
    
    
    ListTemplatesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for requesting list of Templates

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent value for ListTemplatesRequest in the format `projects/*/locations/*`.   
`page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListTemplates` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTemplates` must match the call that provided the page token.   
`filter` |  `str`   
Optional. Filtering results   
`order_by` |  `str`   
Optional. Hint for how to order the results   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
