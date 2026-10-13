---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/create/
title: Method: customers.v2.Users.create \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:05.133046+00:00
---

# Method: customers.v2.Users.create  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.v2.Users.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a User.

  * When creating a user that conflicts with an existing unmanaged consumer account, the API response depends on your conflicting [account management settings](https://knowledge.workspace.google.com/admin/users/find-and-add-unmanaged-users#set_option): 
    * `201 Created`: Returned if no settings are configured, or the option is set to **Replace their conflicting account with managed one**.
    * `202 Accepted`: Returned if the option is set to **Automatically invite users**.
    * `409 Conflict`: Returned if the option is set to **Preserve their conflicting account**.



### HTTP request

`POST https://cloudidentityscim.googleapis.com/v1beta1/customers/{customerId}/v2/Users`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`customerId` |  `string` Required. The customer ID.  
  
### Request body

The request body contains an instance of `[User](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#User)`.

### Response body

If successful, the response body contains a newly created instance of `[User](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#User)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/admin.directory.user`



For more information, see the [Authorization guide](https://docs.cloud.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
