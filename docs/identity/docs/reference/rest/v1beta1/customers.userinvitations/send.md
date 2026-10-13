---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/send/
title: Method: customers.userinvitations.send \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:46.032601+00:00
---

# Method: customers.userinvitations.send  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/send/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.userinvitations.send Stay organized with collections  Save and categorize content based on your preferences. 

Sends a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` to email. If the `UserInvitation` does not exist for this request and it is a valid request, the request creates a `UserInvitation`.

**Note:** The `get` and `list` methods have a 48-hour delay where newly-created consumer accounts will not appear in the results. You can still send a `UserInvitation` to those accounts if you know the unmanaged email address and `[userinvitations.isInvitableUser](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/isInvitableUser#google.apps.cloudidentity.userinvitations.v1beta1.UserInvitationsService.IsInvitableUser)`==True.

### HTTP request

`POST https://cloudidentity.googleapis.com/v1beta1/{name=customers/*/userinvitations/*}:send`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. `UserInvitation` name in the format `customers/{customer}/userinvitations/{user_email_address}`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-identity.userinvitations`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
