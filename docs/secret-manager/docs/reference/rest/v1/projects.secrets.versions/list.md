---
url: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list/
title: Method: projects.secrets.versions.list \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:50.910594+00:00
---

# Method: projects.secrets.versions.list  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/secret-manager/docs/apis)



Send feedback 

#  Method: projects.secrets.versions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists `[SecretVersions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion)`. This call does not return secret data.

### HTTP request

`GET https://secretmanager.googleapis.com/v1/{parent=projects/*/secrets/*}/versions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the `[Secret](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#Secret)` associated with the `[SecretVersions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion)` to list, in the format `projects/*/secrets/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `secretmanager.versions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of results to be returned in a single page. If set to 0, the server decides the number of results to return. If the number is greater than 25000, it is capped at 25000.  
`pageToken` |  `string` Optional. Pagination token, returned earlier via ListSecretVersionsResponse.next_page_token][].  
`filter` |  `string` Optional. Filter string, adhering to the rules in [List-operation filtering](https://cloud.google.com/secret-manager/docs/filtering). List only secret versions matching the filter. If filter is empty, all secret versions are listed.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for `[SecretManagerService.ListSecretVersions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list#google.cloud.secretmanager.v1.SecretManagerService.ListSecretVersions)`.

JSON representation  
---  
      
    
    {
      "versions": [
        {
          object ([SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`versions[]` |  `object (`[SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion)`)` The list of `[SecretVersions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion)` sorted in reverse by createTime (newest first).  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in `[ListSecretVersionsRequest.page_token](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page.  
`totalSize` |  `integer` The total number of `[SecretVersions](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion)` but 0 when the `[ListSecretsRequest.filter](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/list#body.QUERY_PARAMETERS.filter)` field is set.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
