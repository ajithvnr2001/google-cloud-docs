---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list/
title: Method: projects.serviceAccounts.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:07.182931+00:00
---

# Method: projects.serviceAccounts.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.serviceAccounts.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists every `[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)` that belongs to a specific project.

### HTTP request

`GET https://iam.googleapis.com/v1/{name=projects/*}/serviceAccounts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the project associated with the service accounts, such as `projects/my-project-123`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `iam.serviceAccounts.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional limit on the number of service accounts to include in the response. Further accounts can subsequently be obtained by including the `[ListServiceAccountsResponse.next_page_token](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list#body.ListServiceAccountsResponse.FIELDS.next_page_token)` in a subsequent request.The default is 20, and the maximum is 100.  
`pageToken` |  `string` Optional pagination token returned in an earlier `[ListServiceAccountsResponse.next_page_token](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list#body.ListServiceAccountsResponse.FIELDS.next_page_token)`.  
  
### Request body

The request body must be empty.

### Response body

The service account list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "accounts": [
        {
          object ([ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`accounts[]` |  `object (`[ServiceAccount](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts#ServiceAccount)`)` The list of matching service accounts.  
`nextPageToken` |  `string` To retrieve the next page of results, set `[ListServiceAccountsRequest.page_token](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list#body.QUERY_PARAMETERS.page_token)` to this value.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/iam`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
