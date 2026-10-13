---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest
title: Class ListRolesRequest (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:33.745461+00:00
---

# Class ListRolesRequest (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListRolesRequest (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    ListRolesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request to get all roles defined under a resource.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
The `parent` parameter's value depends on the target resource for the request, namely 
    
    
    roles` __,
       

projects`` `__, or 
    
    
    organizations` __.
       Each resource type's parent value format is described
       below:
       
       - 

roles.list()`` `__: An empty string. This method doesn't require a resource; it simply returns all `predefined roles   
`page_size` |  `int`   
Optional limit on the number of roles to include in the response. The default is 300, and the maximum is 1,000.   
`page_token` |  `str`   
Optional pagination token returned in an earlier ListRolesResponse.   
`view` |  `[google.cloud.iam_admin_v1.types.RoleView](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.RoleView)`   
Optional view for the returned Role objects. When `FULL` is specified, the `includedPermissions` field is returned, which includes a list of all permissions in the role. The default value is `BASIC`, which does not return the `includedPermissions` field.   
`show_deleted` |  `bool`   
Include Roles that have been deleted.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
