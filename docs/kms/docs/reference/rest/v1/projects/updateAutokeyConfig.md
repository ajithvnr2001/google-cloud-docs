---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/updateAutokeyConfig/
title: Method: projects.updateAutokeyConfig \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:49.768099+00:00
---

# Method: projects.updateAutokeyConfig  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/updateAutokeyConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  Method: projects.updateAutokeyConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



**Full name** : projects.updateAutokeyConfig

Updates the `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)` for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A `[KeyHandle](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyHandles#KeyHandle)` creation in the folder's descendant projects will use this configuration to determine where to create the resulting `[CryptoKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey)`.

### HTTP request

Choose an endpoint:

globaleurope-west6us-east7europe-west3us-west8europe-west9me-central2us-east1us-west1us-west3us-central2us-east4us-west2europe-west8us-central1us-west4us-east5us-south1northamerica-northeast1northamerica-northeast2usinca

  
`PATCH https://cloudkms.googleapis.com/v1/{autokeyConfig.name=projects/*/autokeyConfig}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`autokeyConfig.name` |  `string` Identifier. Name of the `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)` resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig`, `projects/{PROJECT_NUMBER}/autokeyConfig`, or `projects/{PROJECT_ID}/autokeyConfig`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Masks which fields of the `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)` to update, e.g. `keyProject`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)`.

### Response body

If successful, the response body contains an instance of `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudkms`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudkms.autokeyConfigs.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]] 
