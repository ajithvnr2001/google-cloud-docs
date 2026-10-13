---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/isInvitableUser/
title: Method: customers.userinvitations.isInvitableUser \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:46.417912+00:00
---

# Method: customers.userinvitations.isInvitableUser  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/isInvitableUser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.userinvitations.isInvitableUser Stay organized with collections  Save and categorize content based on your preferences. 

Verifies whether a user account is eligible to receive a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` (is an unmanaged account).

Eligibility is based on the following criteria:

  * the email address is a consumer account and it's the primary email address of the account, and
  * the domain of the email address matches an existing verified Google Workspace or Cloud Identity domain



If both conditions are met, the user is eligible.

**Note:** This method is not supported for Workspace Essentials customers.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/{name=customers/*/userinvitations/*}:isInvitableUser`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. `UserInvitation` name in the format `customers/{customer}/userinvitations/{user_email_address}`  
  
### Request body

The request body must be empty.

### Response body

Response for userinvitations.isInvitableUser RPC.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "isInvitableUser": boolean
    }  
  
Fields  
---  
`isInvitableUser` |  `boolean` Returns true if the email address is invitable.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.userinvitations.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.userinvitations`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
