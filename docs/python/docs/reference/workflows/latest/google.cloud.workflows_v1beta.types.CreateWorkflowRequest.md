---
url: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1beta.types.CreateWorkflowRequest
title: Class CreateWorkflowRequest (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:00.690772+00:00
---

# Class CreateWorkflowRequest (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1beta.types.CreateWorkflowRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateWorkflowRequest (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.0  1.11.0  1.10.2  1.9.1  1.8.0  1.7.4  1.6.3  1.5.0  1.4.1  1.3.0  1.2.3  1.1.0  1.0.0  0.3.2  0.2.0  0.1.0 
    
    
    CreateWorkflowRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for the CreateWorkflow method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Project and location in which the workflow should be created. Format: projects/{project}/locations/{location}   
`workflow` |  `[google.cloud.workflows_v1beta.types.Workflow](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1beta.types.Workflow)`   
Required. Workflow to be created.   
`workflow_id` |  `str`   
Required. The ID of the workflow to be created. It has to fulfill the following requirements: \- Must contain only letters, numbers, underscores and hyphens. \- Must start with a letter. \- Must be between 1-64 characters. \- Must end with a number or a letter. \- Must be unique within the customer project and location.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
