---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1beta/projects.locations.workflows.executions/list/
title: Method: googleapis.workflowexecutions.v1beta.projects.locations.workflows.executions.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:54.293118+00:00
---

# Method: googleapis.workflowexecutions.v1beta.projects.locations.workflows.executions.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1beta/projects.locations.workflows.executions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.workflowexecutions.v1beta.projects.locations.workflows.executions.list Stay organized with collections  Save and categorize content based on your preferences. 

Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first).

## Arguments

Parameters  
---  
`parent` |  `string` Required. Name of the workflow for which the executions should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow}  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum number of executions to return per call. Max supported value depends on the selected Execution view: it's 10000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.  
`pageToken` |  `string` A page token, received from a previous `ListExecutions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExecutions` must match the call that provided the page token.  
`view` |  `enum` Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.  
Enum type. Can be one of the following:  
`EXECUTION_VIEW_UNSPECIFIED` | The default / unset value.  
`BASIC` | Includes only basic metadata about the execution. Following fields are returned: name, start_time, end_time, state and workflow_revision_id.  
`FULL` | Includes all data.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListExecutionsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/workflowexecutions/v1beta/Overview#ListExecutionsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/workflows/docs/reference/executions/rest/v1beta/projects.locations.workflows.executions/list).

### YAML
    
    
    - list:
        call: googleapis.workflowexecutions.v1beta.projects.locations.workflows.executions.list
        args:
            parent: ...
            pageSize: ...
            pageToken: ...
            view: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.workflowexecutions.v1beta.projects.locations.workflows.executions.list",
          "args": {
            "parent": "...",
            "pageSize": "...",
            "pageToken": "...",
            "view": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
