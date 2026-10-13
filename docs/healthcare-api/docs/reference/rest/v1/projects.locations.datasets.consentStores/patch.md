---
url: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch/
title: Method: consentStores.patch \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:31.658996+00:00
---

# Method: consentStores.patch  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  Method: consentStores.patch Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.consentStores.patch

Updates the specified `[consent store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)`.

### HTTP request

`PATCH https://healthcare.googleapis.com/v1/{consentStore.name=projects/*/locations/*/datasets/*/consentStores/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`consentStore.name` |  `string` Identifier. Resource name of the consent store, of the form `projects/{projectId}/locations/{locationId}/datasets/{datasetId}/consentStores/{consentStoreId}`. Cannot be changed after creation.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string(`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The update mask that applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>. Only the `labels`, `defaultConsentTtl`, and `enableConsentCreateOnUpdate` fields are allowed to be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[ConsentStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)`.

### Response body

If successful, the response body contains an instance of `[ConsentStore](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-healthcare`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
