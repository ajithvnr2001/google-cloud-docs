---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userStores.userLicenses/list/
title: Method: projects.locations.userStores.userLicenses.list \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:44.306872+00:00
---

# Method: projects.locations.userStores.userLicenses.list  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userStores.userLicenses/list/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.userStores.userLicenses.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists the User Licenses.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1/{parent=projects/*/locations/*/userStores/*}/userLicenses`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent `[UserStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userStores#UserStore)` resource name, format: `projects/{project}/locations/{location}/userStores/{userStoreId}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, defaults to 100. The maximum value is 1000; values above 1000 will be coerced to 1000.If this field is negative, an INVALID_ARGUMENT error is returned.  
`pageToken` |  `string` Optional. A page token, received from a previous `userLicenses.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `userLicenses.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter for the list request.Supported fields:

  * `licenseAssignmentState`
  * `userPrincipal` * Examples:
  * `licenseAssignmentState = ASSIGNED` to list assigned user licenses.
  * `licenseAssignmentState = NO_LICENSE` to list not licensed users.
  * `licenseAssignmentState = NO_LICENSE_ATTEMPTED_LOGIN` to list users who attempted login but no license assigned.
  * `licenseAssignmentState != NO_LICENSE_ATTEMPTED_LOGIN` to filter out users who attempted login but no license assigned.
  * `userPrincipal = user1@example.com` to list user license for `user1@example.com`.

  
`orderBy` |  `string` Optional. The order in which the `[UserLicense](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense)`s are listed. The value must be a comma-separated list of fields. Default sorting order is ascending. To specify descending order for a field, append a " desc" suffix. Redundant space characters in the syntax are insignificant.Supported fields (only `userPrincipal` is supported for now):

  * `userPrincipal`

If not set, the default ordering is by `userPrincipal`.Examples:

  * `userPrincipal` to order by `userPrincipal` in ascending order.
  * `userPrincipal desc` to order by `userPrincipal` in descending order.

  
  
### Request body

The request body must be empty.

### Response body

Response message for `[UserLicenseService.ListUserLicenses](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userStores.userLicenses/list#google.cloud.discoveryengine.v1.UserLicenseService.ListUserLicenses)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userLicenses": [
        {
          object ([UserLicense](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`userLicenses[]` |  `object (`[UserLicense](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense)`)` All the customer's `[UserLicense](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/UserLicense)`s.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.userStores.listUserLicenses`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
