---
url: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors
title: REST Resource: projects.attestors \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:04.788276+00:00
---

# REST Resource: projects.attestors  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  REST Resource: projects.attestors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Attestor
    * JSON representation
  * Methods



## Resource: Attestor

An `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)` that attests to container image artifacts. An existing attestor cannot be modified except where indicated.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "updateTime": string,
      "etag": string,
    
      // Union field attestor_type can be only one of the following:
      "userOwnedDrydockNote": {
        object ([UserOwnedDrydockNote](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor#UserOwnedDrydockNote))
      }
      // End of list of possible types for union field attestor_type.
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated.  
`description` |  `string` Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time when the attestor was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`etag` |  `string` Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See <https://google.aip.dev/154>.  
Union field `attestor_type`. Required. Identifies an `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)` that attests to a container image artifact. This determines how an attestation will be stored, and how it will be used during policy enforcement. Updates may not change the attestor type, but individual attestor fields may be updated. `attestor_type` can be only one of the following:  
`userOwnedDrydockNote` |  `object (`[UserOwnedDrydockNote](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor#UserOwnedDrydockNote)`)` A Drydock ATTESTATION_AUTHORITY Note, created by the user.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/create)`

|  Creates an `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`, and returns a copy of the new `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`.  
  
### `[delete](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/delete)`

|  Deletes an `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`.  
  
### `[get](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/get)`

|  Gets an `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`.  
  
### `[getIamPolicy](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/list)`

|  Lists `[attestors](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`.  
  
### `[setIamPolicy](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/update)`

|  Updates an `[attestor](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/Shared.Types/Attestor)`.  
  
### `[validateAttestationOccurrence](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1beta1/projects.attestors/validateAttestationOccurrence)`

|  Returns whether the given `Attestation` for the given image URI was signed by the given `Attestor`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
