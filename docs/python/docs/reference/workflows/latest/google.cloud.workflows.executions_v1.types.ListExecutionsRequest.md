---
url: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsRequest
title: Class ListExecutionsRequest (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:01.386562+00:00
---

# Class ListExecutionsRequest (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListExecutionsRequest (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.0  1.11.0  1.10.2  1.9.1  1.8.0  1.7.4  1.6.3  1.5.0  1.4.1  1.3.0  1.2.3  1.1.0  1.0.0  0.3.2  0.2.0  0.1.0 
    
    
    ListExecutionsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for the [ListExecutions][] method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Name of the workflow for which the executions should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow}   
`page_size` |  `int`   
Maximum number of executions to return per call. Max supported value depends on the selected Execution view: it's 1000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.   
`page_token` |  `str`   
A page token, received from a previous `ListExecutions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExecutions` must match the call that provided the page token. Note that pagination is applied to dynamic data. The list of executions returned can change between page requests.   
`view` |  `[google.cloud.workflows.executions_v1.types.ExecutionView](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ExecutionView)`   
Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.   
`filter` |  `str`   
Optional. Filters applied to the [Executions.ListExecutions] results. The following fields are supported for filtering: executionID, state, startTime, endTime, duration, workflowRevisionID, stepName, and label.   
`order_by` |  `str`   
Optional. The ordering applied to the [Executions.ListExecutions] results. By default the ordering is based on descending start time. The following fields are supported for order by: executionID, startTime, endTime, duration, state, and workflowRevisionID.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
