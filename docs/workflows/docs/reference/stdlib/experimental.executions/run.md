---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/run/
title: Function: experimental.executions.run \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:06.338062+00:00
---

# Function: experimental.executions.run  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/experimental.executions/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: experimental.executions.run Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This routine is deprecated. Use this connector [helper method](https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1/projects.locations.workflows.executions/run) instead.

Starts a workflow execution and waits for it to finish.

## Arguments

Arguments  
---  
`workflow_id` |  `string` ID of the workflow.  
`location` |  `string` If present, location of the workflow. The location of the caller is used by default.  
`project_id` |  `string` If present, project ID associated with the workflow. The project ID of the caller is used by default.  
`argument` | Optional execution parameters.  
  
## Returns

The execution's result.

## Raised exceptions

Exceptions  
---  
`ExecutionError` | If the execution finishes unsuccessfully.  
`TimeoutError` | If the execution takes more than 30 minutes to finish.  
`TypeError` | If type of `argument` is not one of: integer, float, bool, string, list, or dict.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
