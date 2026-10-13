---
url: https://docs.cloud.google.com/python/docs/reference/essentialcontacts/latest/google.cloud.essential_contacts_v1.types.ComputeContactsRequest
title: Class ComputeContactsRequest (1.15.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:10.592173+00:00
---

# Class ComputeContactsRequest (1.15.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/essentialcontacts/latest/google.cloud.essential_contacts_v1.types.ComputeContactsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ComputeContactsRequest (1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.6  1.6.0  1.5.3  1.4.1  1.3.0  1.2.3  1.1.2  1.0.1  0.4.2  0.3.0  0.2.4  0.1.1 
    
    
    ComputeContactsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the ComputeContacts method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The name of the resource to compute contacts for. Format: organizations/{organization_id}, folders/{folder_id} or projects/{project_id}   
`notification_categories` |  `MutableSequence[[google.cloud.essential_contacts_v1.types.NotificationCategory](https://docs.cloud.google.com/python/docs/reference/essentialcontacts/latest/google.cloud.essential_contacts_v1.types.NotificationCategory)]`   
The categories of notifications to compute contacts for. If ALL is included in this list, contacts subscribed to any notification category will be returned.   
`page_size` |  `int`   
Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of `next_page_token` in the response indicates that more results might be available. If not specified, the default page_size is 100.   
`page_token` |  `str`   
Optional. If present, retrieves the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of other method parameters should be identical to those in the previous call.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
