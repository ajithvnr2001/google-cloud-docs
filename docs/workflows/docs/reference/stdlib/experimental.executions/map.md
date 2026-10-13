---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/map/
title: Function: experimental.executions.map \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:05.635597+00:00
---

# Function: experimental.executions.map  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/map/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: experimental.executions.map Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The behavior of this routine might change, and it might not be supported in the future.**Note:** Instead of using `experimental.executions.map` to support parallel work, we recommend you [execute workflow steps in parallel](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps). If you are already using `experimental.executions.map`, you can [migrate your workflow to use parallel steps](https://docs.cloud.google.com/workflows/docs/migrate-function-to-parallel).

Starts workflow executions and waits for all of them to finish.

## Arguments

Arguments  
---  
`workflow_id` |  `string` ID of the workflow.  
`arguments` | List of optional execution parameters. A workflow execution is created for each element of the list.  
`timeout` |  `float` The request timeout, in seconds (default: `1800.0`). If the request takes longer than the timeout, a `TimeoutError` is raised.  
`location` |  `string` If present, location of the workflow. The location of the caller is used by default.  
`project_id` |  `string` If present, project ID associated with the workflow. The project ID of the caller is used by default.  
  
## Returns

A list where each element is the result of a workflow execution starting and a corresponding argument.

## Raised exceptions

Exceptions  
---  
`ExecutionError` | If any of the executions finish unsuccessfully.  
`TimeoutError` | If waiting for the executions to finish takes longer than the specified timeout limit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
