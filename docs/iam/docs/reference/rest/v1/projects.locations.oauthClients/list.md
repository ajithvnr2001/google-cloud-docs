---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/list/
title: Method: projects.locations.oauthClients.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:54.555703+00:00
---

# Method: projects.locations.oauthClients.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.oauthClients.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all non-deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s in a project. If `showDeleted` is set to `true`, then deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s are also listed.

### HTTP request

`GET https://iam.googleapis.com/v1/{parent=projects/*/locations/*}/oauthClients`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent to list `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s for.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s to return. If unspecified, at most 50 `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s will be returned. The maximum value is 100; values above 100 are truncated to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `oauthClients.list` call. Provide this to retrieve the subsequent page.  
`showDeleted` |  `boolean` Optional. Whether to return soft-deleted `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s.  
  
### Request body

The request body must be empty.

### Response body

Response message for oauthClients.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "oauthClients": [
        {
          object ([OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`oauthClients[]` |  `object (`[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`)` A list of `[OauthClient](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients#OauthClient)`s.  
`nextPageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
