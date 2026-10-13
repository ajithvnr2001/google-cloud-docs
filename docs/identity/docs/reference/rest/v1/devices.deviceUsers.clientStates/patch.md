---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/patch/
title: Method: devices.deviceUsers.clientStates.patch \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:36.625882+00:00
---

# Method: devices.deviceUsers.clientStates.patch  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: devices.deviceUsers.clientStates.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates the client state for the device user

**Note** : This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium

### HTTP request

`PATCH https://cloudidentity.googleapis.com/v1/{clientState.name=devices/*/deviceUsers/*/clientStates/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`clientState.name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: `devices/{device}/deviceUsers/{deviceUser}/clientState/{partner}`, where partner corresponds to the partner storing the data. For partners belonging to the "BeyondCorp Alliance", this is the partner ID specified to you by Google.For all other callers, this is a string of the form: `{customer}-suffix`, where `customer` is your customer ID. The _suffix_ is any string the caller specifies. This string will be displayed verbatim in the administration console. This suffix is used in setting up Custom Access Levels in Context-Aware Access.Your organization's customer ID can be obtained from the URL: `GET https://www.googleapis.com/admin/directory/v1/customers/my_customer` The `id` field in the response contains the customer ID starting with the letter 'C'. The customer ID to be used in this API is the string after the letter 'C' (not including 'C')  
  
### Query parameters

Parameters  
---  
`customer` |  `string` Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Comma-separated list of fully qualified names of fields to be updated. If not specified, all updatable fields in ClientState are updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ClientState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates#ClientState)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.devices`
  * `https://www.googleapis.com/auth/cloud-identity`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
