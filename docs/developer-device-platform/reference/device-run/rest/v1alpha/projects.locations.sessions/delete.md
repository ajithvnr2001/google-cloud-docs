---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/delete/
title: Method: projects.locations.sessions.delete \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:56.349156+00:00
---

# Method: projects.locations.sessions.delete  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.locations.sessions.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Deletes a session.

This RPC returns immediately and deletion proceeds asynchronously. It will cancel the session at first if it is still running.

### HTTP request

`DELETE https://devicerun.googleapis.com/v1alpha/{name=projects/*/locations/*/sessions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the session. Format: `projects/{project}/locations/{location}/sessions/{session}`. It takes the form `projects/{project}/locations/{location}/sessions/{session}`.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` Optional. A unique identifier for this request.This request is only idempotent if a `requestId` is provided, i.e. if a request with the same `requestId` is received, then the previous result will be returned. The server will guarantee that for at least 60 minutes after the first request.The value must be a UUID (ex. 123e4567-e89b-12d3-a456-426655440000). See github.com/google/uuid for more details.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://docs.cloud.google.com/iam/docs) permission on the `name` resource:

  * `devicerun.sessions.delete`



For more information, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
