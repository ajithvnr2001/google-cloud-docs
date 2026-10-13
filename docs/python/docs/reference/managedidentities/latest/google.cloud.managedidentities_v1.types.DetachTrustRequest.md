---
url: https://docs.cloud.google.com/python/docs/reference/managedidentities/latest/google.cloud.managedidentities_v1.types.DetachTrustRequest
title: Class DetachTrustRequest (1.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:05.838324+00:00
---

# Class DetachTrustRequest (1.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/managedidentities/latest/google.cloud.managedidentities_v1.types.DetachTrustRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DetachTrustRequest (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.2  1.11.0  1.10.1  1.9.5  1.8.0  1.7.2  1.6.0  1.5.4  1.4.2  1.3.1  1.2.0  1.1.3  1.0.0  0.2.2  0.1.0 
    
    
    DetachTrustRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for DetachTrust

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource domain name, project name, and location using the form: `projects/{project_id}/locations/global/domains/{domain_name}`  
`trust` |  `[google.cloud.managedidentities_v1.types.Trust](https://docs.cloud.google.com/python/docs/reference/managedidentities/latest/google.cloud.managedidentities_v1.types.Trust)`   
Required. The domain trust resource to removed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
