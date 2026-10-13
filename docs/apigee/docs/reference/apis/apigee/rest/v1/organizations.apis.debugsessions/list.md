---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list/
title: Method: organizations.apis.debugsessions.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:22.306704+00:00
---

# Method: organizations.apis.debugsessions.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apis.debugsessions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ApiDebugSession
    * JSON representation
  * Try it!



Lists debug sessions that are currently active in the given API Proxy.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/apis/*}/debugsessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the API Proxy for which to list debug sessions. Must be of the form: `organizations/{organization}/apis/{api}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.tracesessions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of debug sessions to return. The page size defaults to 25.  
`pageToken` |  `string` Optional. Page token, returned from a previous debugsessions.list call, that you can use to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response for `[debugsessions.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list#google.cloud.apigee.v1.DebugSessionService.ListApiDebugSessions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessions": [
        {
          object ([ApiDebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list#ApiDebugSession))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`sessions[]` |  `object (`[ApiDebugSession](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list#ApiDebugSession)`)` Session info that includes debug session ID, environment ID, api proxy revision ID and the first transaction creation timestamp.  
`nextPageToken` |  `string` Page token that you can include in a ListApiDebugSessionsRequest to retrieve the next page. If omitted, no subsequent pages exist.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## ApiDebugSession

Session carries the debug session id and its creation time.

JSON representation  
---  
      
    
    {
      "id": string,
      "apiProxyRevisionId": string,
      "environmentId": string,
      "createTime": string
    }  
  
Fields  
---  
`id` |  `string` The debug session ID.  
`apiProxyRevisionId` |  `string` The revision ID of the deployed API proxy.  
`environmentId` |  `string` The environment ID of the deployed API proxy.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The first transaction creation timestamp in millisecond, recorded by UAP.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
