---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentregistry/latest/google.cloud.agentregistry_v1.types.ListServicesRequest
title: Class ListServicesRequest (0.1.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:29.969358+00:00
---

# Class ListServicesRequest (0.1.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentregistry/latest/google.cloud.agentregistry_v1.types.ListServicesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListServicesRequest (0.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.2 (latest)  0.1.1 
    
    
    ListServicesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for requesting list of Services

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The project and location to list services in. Expected format: `projects/{project}/locations/{location}`.   
`page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.   
`page_token` |  `str`   
Optional. A token identifying a page of results the server should return.   
`filter` |  `str`   
Optional. A query string used to filter the list of services returned. The filter expression must follow AIP-160 syntax. Filtering is supported on the `name`, `display_name`, `description`, and `labels` fields. Some examples: \- `name = "projects/p1/locations/l1/services/s1"` \- `display_name = "my-service"` \- `description : "myservice description"` \- `labels.env = "prod"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
