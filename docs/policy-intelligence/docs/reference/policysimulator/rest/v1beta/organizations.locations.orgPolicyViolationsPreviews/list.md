---
url: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews/list/
title: Method: organizations.locations.orgPolicyViolationsPreviews.list \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:01.366559+00:00
---

# Method: organizations.locations.orgPolicyViolationsPreviews.list  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  Method: organizations.locations.orgPolicyViolationsPreviews.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



orgPolicyViolationsPreviews.list lists each `[OrgPolicyViolationsPreview](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews#OrgPolicyViolationsPreview)` in an organization. Each `[OrgPolicyViolationsPreview](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews#OrgPolicyViolationsPreview)` is available for at least 7 days.

### HTTP request

`GET https://policysimulator.googleapis.com/v1beta/{parent=organizations/*/locations/*}/orgPolicyViolationsPreviews`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent the violations are scoped to. Format: `organizations/{organization}/locations/{location}`Example: `organizations/my-example-org/locations/global`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. The service may return fewer than this value. If unspecified, at most 5 items will be returned. The maximum value is 10; values above 10 will be coerced to 10.  
`pageToken` |  `string` Optional. A page token, received from a previous call. Provide this to retrieve the subsequent page.When paginating, all other parameters must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

ListOrgPolicyViolationsPreviewsResponse is the response message for `[OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews/list#google.cloud.policysimulator.v1beta.OrgPolicyViolationsPreviewService.ListOrgPolicyViolationsPreviews)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "orgPolicyViolationsPreviews": [
        {
          object ([OrgPolicyViolationsPreview](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews#OrgPolicyViolationsPreview))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`orgPolicyViolationsPreviews[]` |  `object (`[OrgPolicyViolationsPreview](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/organizations.locations.orgPolicyViolationsPreviews#OrgPolicyViolationsPreview)`)` The list of OrgPolicyViolationsPreview  
`nextPageToken` |  `string` A token that you can use to retrieve the next page of results. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `policysimulator.orgPolicyViolationsPreviews.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-16 UTC."],[],[]] 
