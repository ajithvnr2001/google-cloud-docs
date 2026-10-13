---
url: https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/common/groups/
title: Method: common.groups \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:55.860177+00:00
---

# Method: common.groups  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/common/groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: common.groups Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Retrieves a list of groups for the authenticated user from the distributed claims endpoint.

Note: This endpoint is only supported for Looker.

### HTTP request

`GET https://cloudoauth.googleapis.com/v1/common/groups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of groups to return. If unspecified, at most 2500 groups will be returned.  
`pageToken` |  `string` Optional. A page token received from a previous `common.groups` call. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[common.groups](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest/v1/common/groups#google.cloud.identity.oauth.v1.CloudOAuthService.FetchGroups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "groups": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`groups[]` |  `string` A paginated list of enterprise group memberships for the user.  
`nextPageToken` |  `string` A token which can be sent as `pageToken` to retrieve the next page of results. If this field is empty or omitted, there are no subsequent pages. Note: Pagination is not supported in preview.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `openid`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
