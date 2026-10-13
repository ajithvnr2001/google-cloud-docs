---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.ListCloudControlDeploymentsRequest
title: Class ListCloudControlDeploymentsRequest (0.8.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:37.057979+00:00
---

# Class ListCloudControlDeploymentsRequest (0.8.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudsecuritycompliance/latest/google.cloud.cloudsecuritycompliance_v1.types.ListCloudControlDeploymentsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListCloudControlDeploymentsRequest (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListCloudControlDeploymentsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The request message for [ListCloudControlDeployments][].

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource for the cloud control deployment, in the format `organizations/{organization}/locations/{location}` or `projects/{project}/locations/{location}`. The only supported location is `global`.   
`page_size` |  `int`   
Optional. The requested page size. The server might return fewer items than you requested. If unspecified, the server picks an appropriate default.   
`page_token` |  `str`   
Optional. A token that identifies the page of results that the server should return.   
`filter` |  `str`   
Optional. The filter to apply on the resource, as defined by `AIP-160: Filtering `__.   
`order_by` |  `str`   
Optional. The sort order for the results. The following values are supported: \- `name` \- `name desc` If you do not specify a value, then the results are not sorted.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
