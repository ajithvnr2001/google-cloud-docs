---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list/
title: Method: organizations.environments.apis.revisions.debugsessions.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:49.137505+00:00
---

# Method: organizations.environments.apis.revisions.debugsessions.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.apis.revisions.debugsessions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Session
    * JSON representation
  * Try it!



Lists debug sessions that are currently active in the given API Proxy revision.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*/apis/*/revisions/*}/debugsessions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the API Proxy revision deployment for which to list debug sessions. Must be of the form: `organizations/{organization}/environments/{environment}/apis/{api}/revisions/{revision}`.If the API proxy resource has the `space` attribute set, IAM permissions are checked differently . To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.tracesessions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of debug sessions to return. The page size defaults to 25.  
`pageToken` |  `string` Optional. Page token, returned from a previous debugsessions.list call, that you can use to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessions": [
        {
          object ([Session](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list#Session))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`sessions[]` |  `object (`[Session](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions/list#Session)`)` Session info that includes debug session ID and the first transaction creation timestamp.  
`nextPageToken` |  `string` Page token that you can include in a ListDebugSessionsRequest to retrieve the next page. If omitted, no subsequent pages exist.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## Session

Session carries the debug session id and its creation time.

JSON representation  
---  
      
    
    {
      "id": string,
      "timestampMs": string
    }  
  
Fields  
---  
`id` |  `string` The debug session ID.  
`timestampMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The first transaction creation timestamp in millisecond, recorded by UAP.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
