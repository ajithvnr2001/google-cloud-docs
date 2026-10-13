---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/list/
title: Method: organizations.locations.principalAccessBoundaryPolicies.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:25.921547+00:00
---

# Method: organizations.locations.principalAccessBoundaryPolicies.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: organizations.locations.principalAccessBoundaryPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Lists principal access boundary policies.

### HTTP request

`GET https://iam.googleapis.com/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource, which owns the collection of principal access boundary policies.Format: `organizations/{organizationId}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of principal access boundary policies to return. The service may return fewer than this value.If unspecified, at most 50 principal access boundary policies will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `principalAccessBoundaryPolicies.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `principalAccessBoundaryPolicies.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for principalAccessBoundaryPolicies.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "principalAccessBoundaryPolicies": [
        {
          object ([PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`principalAccessBoundaryPolicies[]` |  `object (`[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicy)`)` The principal access boundary policies from the specified parent.  
`nextPageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `iam.principalaccessboundarypolicies.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
