---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/list/
title: Method: customers.userinvitations.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:46.240889+00:00
---

# Method: customers.userinvitations.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.userinvitations.list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resources.

**Note:** New consumer accounts with the customer's verified domain created within the previous 48 hours will not appear in the result. This delay also applies to newly-verified domains.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/{parent=customers/*}/userinvitations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The customer ID of the Google Workspace or Cloud Identity account the `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resources are associated with.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resources to return. If unspecified, at most 100 resources will be returned. The maximum value is 200; values above 200 will be set to 200.  
`pageToken` |  `string` Optional. A page token, received from a previous `userinvitations.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.  
`filter` |  `string` Optional. A query string for filtering `UserInvitation` results by their current state, in the format: `"state=='invited'"`.  
`orderBy` |  `string` Optional. The sort order of the list results.You can sort the results in descending order based on either email or last update timestamp but not both, using `order_by="email desc"`. Currently, sorting is supported for `update_time asc`, `update_time desc`, `email asc`, and `email desc`.If not specified, results will be returned based on `email asc` order.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` listing request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userInvitations": [
        {
          object ([UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`userInvitations[]` |  `object (`[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)`)` The list of `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resources.  
`nextPageToken` |  `string` The token for the next page. If not empty, indicates that there may be more `UserInvitation` resources that match the listing request; this value can be used in a subsequent `ListUserInvitationsRequest` to get continued results with the current list call.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.userinvitations.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.userinvitations`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
