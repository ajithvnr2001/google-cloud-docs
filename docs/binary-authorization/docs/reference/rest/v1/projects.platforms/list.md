---
url: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list/
title: Method: projects.platforms.list \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:01.632557+00:00
---

# Method: projects.platforms.list  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)



Send feedback 

#  Method: projects.platforms.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Platform
    * JSON representation



Lists all platforms supported by a platform policy.

### HTTP request

`GET https://binaryauthorization.googleapis.com/v1/{parent=projects/*}/platforms`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Contains the name of the resource requested, specified using the format `projects/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. The server may return fewer results than requested. If unspecified, the server picks an appropriate default.  
`pageToken` |  `string` A token identifying a page of results the server should return. Typically, this is the value of `[ListPlatformsResponse.next_page_token](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#body.ListPlatformsResponse.FIELDS.next_page_token)` returned from the previous call to the `platforms.list` method.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[PlatformPolicyManagementService.ListPlatforms](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ListPlatforms)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "platforms": [
        {
          object ([Platform](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#Platform))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`platforms[]` |  `object (`[Platform](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#Platform)`)` The list of `[platforms](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#Platform)` supported by Binary Authorization.  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `[ListPlatformsRequest.page_token](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#body.QUERY_PARAMETERS.page_token)` field in the subsequent call to the `platforms.list` method to retrieve the next page of results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Platform

A `[platform](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms/list#Platform)` supported by Binary Authorization platform policy.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The relative resource name of the platform supported by Binary Authorization platform policies, in the form of `projects/*/platforms/*`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
