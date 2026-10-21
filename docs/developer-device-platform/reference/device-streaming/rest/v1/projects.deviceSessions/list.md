---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/list/
title: Method: projects.deviceSessions.list \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:58.434572+00:00
---

# Method: projects.deviceSessions.list  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.deviceSessions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists DeviceSessions owned by the project user.

### HTTP request

`GET https://devicestreaming.googleapis.com/v1/{parent=projects/*}/deviceSessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent to request, e.g. "projects/{projectId}" It takes the form `projects/{project}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of DeviceSessions to return.  
`pageToken` |  `string` Optional. A continuation token for paging.  
`filter` |  `string` Optional. If specified, responses will be filtered by the given filter. Allowed fields are: sessionState.  
  
### Request body

The request body must be empty.

### Response body

Response message for DirectAccessService.ListDeviceSessions.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deviceSessions": [
        {
          object ([DeviceSession](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#DeviceSession))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`deviceSessions[]` |  `object (`[DeviceSession](https://docs.cloud.google.com/developer-device-platform/reference/device-streaming/rest/v1/projects.deviceSessions#DeviceSession)`)` The sessions matching the specified filter in the given cloud project.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `devicestreaming.deviceSessions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
