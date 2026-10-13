---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.CreatePrincipalAccessBoundaryPolicyRequest
title: Class CreatePrincipalAccessBoundaryPolicyRequest (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:46.271488+00:00
---

# Class CreatePrincipalAccessBoundaryPolicyRequest (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.CreatePrincipalAccessBoundaryPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreatePrincipalAccessBoundaryPolicyRequest (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    CreatePrincipalAccessBoundaryPolicyRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for CreatePrincipalAccessBoundaryPolicyRequest method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported. Format: `organizations/{organization_id}/locations/{location}`  
`principal_access_boundary_policy_id` |  `str`   
Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /`a-z][a-z0-9-.]`{2,62}/.   
`principal_access_boundary_policy` |  `[google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicy)`   
Required. The principal access boundary policy to create.   
`validate_only` |  `bool`   
Optional. If set, validate the request and preview the creation, but do not actually post it.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
