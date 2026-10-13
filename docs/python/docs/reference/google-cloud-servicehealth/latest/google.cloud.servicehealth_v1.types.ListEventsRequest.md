---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-servicehealth/latest/google.cloud.servicehealth_v1.types.ListEventsRequest
title: Class ListEventsRequest (0.5.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:56.290833+00:00
---

# Class ListEventsRequest (0.5.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-servicehealth/latest/google.cloud.servicehealth_v1.types.ListEventsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListEventsRequest (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0  0.4.0  0.3.0  0.2.0  0.1.11 
    
    
    ListEventsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Requests list of events.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent value using the form `projects/{project_id}/locations/{location}/events`. `project_id` \- ID of the project for which to list service health events. `location` \- The location to get the service health events from. To retrieve service health events of category = INCIDENT, use `location` = `global`.   
`page_size` |  `int`   
Optional. The maximum number of events that should be returned. Acceptable values are 1 to 100, inclusive. (The default value is 10.) If more results are available, the service returns a next_page_token that you can use to get the next page of results in subsequent list requests. The service may return fewer events than the requested page_size.   
`page_token` |  `str`   
Optional. A token identifying a page of results the server should return. Provide Page token returned by a previous `ListEvents` call to retrieve the next page of results. When paginating, all other parameters provided to `ListEvents` must match the call that provided the page token.   
`filter` |  `str`   
Optional. A filter expression that filters resources listed in the response. The expression takes the following forms: \- field=value for `category` and `state`\ \- field <,>, <=, or="">= value for `update_time` Examples: `category=INCIDENT`, `update_time>="2000-01-01T11:30:00-04:00"`, `event_impacts.product.product_name:"Eventarc"` .. raw:: html   
Multiple filter queries are separated by spaces. Example: `category=INCIDENT state=ACTIVE`. By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly. Filter is supported for the following fields: `category`, `state`, `update_time`, `event_impacts.product.product_name`  
`view` |  `[google.cloud.servicehealth_v1.types.EventView](https://docs.cloud.google.com/python/docs/reference/google-cloud-servicehealth/latest/google.cloud.servicehealth_v1.types.EventView)`   
Optional. Event fields to include in response.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
