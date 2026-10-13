---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies/
title: Method: policies.listPolicies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:42.525671+00:00
---

# Method: policies.listPolicies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: policies.listPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Retrieves the policies of the specified kind that are attached to a resource.

The response lists only policy metadata. In particular, policy rules are omitted.

### HTTP request

`GET https://iam.googleapis.com/v2/{parent=policies/*/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource that the policy is attached to, along with the kind of policy to list. Format: `policies/{attachmentPoint}/denypolicies`The attachment point is identified by its URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies`.For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of policies to return. IAM ignores this value and uses the value 1000.  
`pageToken` |  `string` A page token received in a `[ListPoliciesResponse](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies#body.ListPoliciesResponse)`. Provide this token to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response message for `policies.listPolicies`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#Policy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policies[]` |  `object (`[Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies#Policy)`)` Metadata for the policies that are attached to the resource.  
`nextPageToken` |  `string` A page token that you can use in a `ListPoliciesRequest` to retrieve the next page. If this field is omitted, there are no additional pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
