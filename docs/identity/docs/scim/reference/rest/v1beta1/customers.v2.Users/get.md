---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/get/
title: Method: customers.v2.Users.get \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:05.191398+00:00
---

# Method: customers.v2.Users.get  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.v2.Users.get Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a User.

### HTTP request

`GET https://cloudidentityscim.googleapis.com/v1beta1/customers/{customerId}/v2/Users/{userId}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`customerId` |  `string` Required. The customer ID.  
`userId` |  `string` Required. The user ID.  
  
### Query parameters

Parameters  
---  
`attributes` |  `string` Optional. The attributes parameter as described in RFC 7644 Section 3.4.2.5. Must be a comma-separated list (without spaces) of top-level attributes.Must contain only top-level attributes. Sub-attributes (for example, `name.familyName`) are not supported within the `attributes` parameter.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[User](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#User)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/admin.directory.user.readonly`
  * `https://www.googleapis.com/auth/admin.directory.user`



For more information, see the [Authorization guide](https://docs.cloud.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
