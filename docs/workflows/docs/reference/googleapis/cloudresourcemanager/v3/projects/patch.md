---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/projects/patch/
title: Method: googleapis.cloudresourcemanager.v3.projects.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:04.070884+00:00
---

# Method: googleapis.cloudresourcemanager.v3.projects.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/projects/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudresourcemanager.v3.projects.patch Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This method doesn't return a long-running operation (LRO) name. To avoid a LRO polling error, set the `skip_polling` connector parameter to `true` so that the connector invocation call is non-blocking if the initial request succeeds. A successful request returns `"done":true`; otherwise, to catch any exceptions use a [`try/except` structure](https://docs.cloud.google.com/workflows/docs/reference/syntax/catching-errors). For more information, see the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

Updates the `display_name` and labels of the project identified by the specified `name` (for example, `projects/415104041262`). Deleting all labels requires an update mask for labels field. The caller must have `resourcemanager.projects.update` permission for this project.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`name` |  `string` Required. Output only. The unique resource name of the project. It is an int64 generated number prefixed by "projects/". Example: `projects/415104041262`  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Optional. An update mask to selectively update fields.  
`body` |  `object ([Project](https://cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/Overview#Project))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
`OperationError` | If the long-running operation finished unsuccessfully.  
`ResponseTypeError` | If the long-running operation returned a response of the wrong type.  
  
## Response

If successful, the response contains an instance of [`Operation`](https://cloud.google.com/workflows/docs/reference/googleapis/cloudresourcemanager/v3/Overview#Operation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/resource-manager/reference/rest/v3/projects/patch).

### YAML
    
    
    - patch:
        call: googleapis.cloudresourcemanager.v3.projects.patch
        args:
            name: ...
            updateMask: ...
            body:
                displayName: ...
                labels: ...
                parent: ...
                projectId: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.cloudresourcemanager.v3.projects.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "body": {
              "displayName": "...",
              "labels": "...",
              "parent": "...",
              "projectId": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
