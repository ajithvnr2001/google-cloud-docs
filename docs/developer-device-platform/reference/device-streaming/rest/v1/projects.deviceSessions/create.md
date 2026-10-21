---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/create/
title: Method: projects.deviceSessions.create \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:58.133281+00:00
---

# Method: projects.deviceSessions.create  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.deviceSessions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a DeviceSession.

### HTTP request

`POST https://devicestreaming.googleapis.com/v1/{parent=projects/*}/deviceSessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The Compute Engine project under which this device will be allocated. "projects/{projectId}" It takes the form `projects/{project}`.  
  
### Query parameters

Parameters  
---  
`deviceSessionId` |  `string` Optional. The ID to use for the DeviceSession, which will become the final component of the DeviceSession's resource name.This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.  
  
### Request body

The request body contains an instance of `[DeviceSession](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#DeviceSession)`.

### Response body

If successful, the response body contains a newly created instance of `[DeviceSession](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#DeviceSession)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `devicestreaming.deviceSessions.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
