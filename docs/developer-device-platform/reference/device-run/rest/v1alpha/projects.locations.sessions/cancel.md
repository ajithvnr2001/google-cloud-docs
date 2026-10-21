---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel/
title: Method: projects.locations.sessions.cancel \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:56.394183+00:00
---

# Method: projects.locations.sessions.cancel  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.locations.sessions.cancel Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CancelResult
  * Try it!



Cancels an in-progress automation session.

This RPC returns immediately and cancellation proceeds asynchronously. If the session is already finished, this RPC will have no effect.

### HTTP request

`POST https://devicerun.googleapis.com/v1alpha/{name=projects/*/locations/*/sessions/*}:cancel`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the session. Format: "projects/{project}/locations/{location}/sessions/{session}" It takes the form `projects/{project}/locations/{location}/sessions/{session}`.  
  
### Request body

The request body must be empty.

### Response body

Response of the cancel session request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "cancelResult": enum ([CancelResult](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel#CancelResult))
    }  
  
Fields  
---  
`cancelResult` |  `enum (`[CancelResult](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/cancel#CancelResult)`)` The result of the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://docs.cloud.google.com/iam/docs) permission on the `name` resource:

  * `devicerun.sessions.delete`



For more information, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

## CancelResult

The result of the request.

Enums  
---  
`CANCEL_RESULT_UNSPECIFIED` | Unspecified cancel result.  
`SESSION_MARKED_AS_CANCELLED` | The session is marked as cancelled, but has not finished yet.  
`SESSION_FINISHED` | The session is finished, either by itself or by the cancel request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
