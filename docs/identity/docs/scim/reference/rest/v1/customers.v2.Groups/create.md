---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/create/
title: Method: customers.v2.Groups.create \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:58.955474+00:00
---

# Method: customers.v2.Groups.create  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: customers.v2.Groups.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a Group.

### HTTP request

`POST https://cloudidentityscim.googleapis.com/v1/customers/{customerId}/v2/Groups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`customerId` |  `string` Required. The customer ID.  
  
### Request body

The request body contains an instance of `[Group](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups#Group)`.

### Response body

If successful, the response body contains a newly created instance of `[Group](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups#Group)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.groups`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://docs.cloud.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
