---
url: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles/patch/
title: Method: organizations.locations.securityProfiles.patch \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:58.809133+00:00
---

# Method: organizations.locations.securityProfiles.patch  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Reference ](https://docs.cloud.google.com/firewall/docs/apis)



Send feedback 

#  Method: organizations.locations.securityProfiles.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates the parameters of a single SecurityProfile.

### HTTP request

`PATCH https://networksecurity.googleapis.com/v1/{securityProfile.name=organizations/*/locations/*/securityProfiles/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`securityProfile.name` |  `string` Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfiles/{securityProfile}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Field mask is used to specify the fields to be overwritten in the SecurityProfile resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[SecurityProfile](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles#SecurityProfile)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-24 UTC."],[],[]] 
