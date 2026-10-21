---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/patch/
title: Method: peerings.patch \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:24.493927+00:00
---

# Method: peerings.patch  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  Method: peerings.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



**Full name** : projects.locations.global.peerings.patch

Updates the labels for specified Peering.

### HTTP request

`PATCH https://managedidentities.googleapis.com/v1beta1/{peering.name=projects/*/locations/global/peerings/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`peering.name` |  `string` Output only. Unique name of the peering in this scope including projects and location using the form: `projects/{projectId}/locations/global/peerings/{peeringId}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from `[Peering](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings#Peering)`: * `labels`This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `updateMask`:

  * `managedidentities.peerings.update`

  
  
### Request body

The request body contains an instance of `[Peering](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings#Peering)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
