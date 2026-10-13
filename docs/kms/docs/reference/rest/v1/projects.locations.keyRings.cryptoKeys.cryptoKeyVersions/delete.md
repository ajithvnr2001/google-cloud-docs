---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/delete/
title: Method: cryptoKeyVersions.delete \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:41.147778+00:00
---

# Method: cryptoKeyVersions.delete  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  Method: cryptoKeyVersions.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



**Full name** : projects.locations.keyRings.cryptoKeys.cryptoKeyVersions.delete

Permanently deletes the given `[CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)`. Only possible if the version has not been previously imported and if its `[state](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.state)` is one of `[DESTROYED](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.DESTROYED)`, `[IMPORT_FAILED](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.IMPORT_FAILED)`, or `[GENERATION_FAILED](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.GENERATION_FAILED)`. Successfully imported `[CryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` cannot be deleted at this time. The specified version will be immediately and permanently deleted upon calling this method. This action cannot be undone.

### HTTP request

Choose an endpoint:

globaleurope-west6us-east7europe-west3us-west8europe-west9me-central2us-east1us-west1us-west3us-central2us-east4us-west2europe-west8us-central1us-west4us-east5us-south1northamerica-northeast1northamerica-northeast2usinca

  
`DELETE https://cloudkms.googleapis.com/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The `[name](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.name)` of the `[CryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion)` to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `cloudkms.cryptoKeyVersions.delete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudkms`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]] 
