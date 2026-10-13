---
url: https://docs.cloud.google.com/python/docs/reference/datamigration/latest/google.cloud.clouddms_v1.types.CreateConversionWorkspaceRequest
title: Class CreateConversionWorkspaceRequest (1.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:26.749437+00:00
---

# Class CreateConversionWorkspaceRequest (1.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datamigration/latest/google.cloud.clouddms_v1.types.CreateConversionWorkspaceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateConversionWorkspaceRequest (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.4  1.11.0  1.10.1  1.9.5  1.8.0  1.7.1  1.6.2  1.5.0  1.4.3  1.3.2  1.2.1  1.1.0  1.0.2  0.2.4  0.1.0 
    
    
    CreateConversionWorkspaceRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message to create a new Conversion Workspace in the specified project and region.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent which owns this collection of conversion workspaces.   
`conversion_workspace_id` |  `str`   
Required. The ID of the conversion workspace to create.   
`conversion_workspace` |  `[google.cloud.clouddms_v1.types.ConversionWorkspace](https://docs.cloud.google.com/python/docs/reference/datamigration/latest/google.cloud.clouddms_v1.types.ConversionWorkspace)`   
Required. Represents a conversion workspace object.   
`request_id` |  `str`   
A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored. It is recommended to always set this value to a UUID. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (\\_), and hyphens (-). The maximum length is 40 characters.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
