---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.CreateUrlListRequest
title: Class CreateUrlListRequest (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:26.027191+00:00
---

# Class CreateUrlListRequest (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.CreateUrlListRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateUrlListRequest (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    CreateUrlListRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request used by the CreateUrlList method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource of the UrlList. Must be in the format `projects/*/locations/{location}`.   
`url_list_id` |  `str`   
Required. Short name of the UrlList resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "url_list".   
`url_list` |  `[google.cloud.network_security_v1.types.UrlList](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.UrlList)`   
Required. UrlList resource to be created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
