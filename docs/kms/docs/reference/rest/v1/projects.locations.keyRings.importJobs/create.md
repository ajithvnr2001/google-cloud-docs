---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create/
title: Method: importJobs.create \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:37.525107+00:00
---

# Method: importJobs.create  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  Method: importJobs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



**Full name** : projects.locations.keyRings.importJobs.create

Create a new `[ImportJob](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)` within a `[KeyRing](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)`.

`[ImportJob.import_method](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob.FIELDS.import_method)` is required.

### HTTP request

Choose an endpoint:

globaleurope-west6us-east7europe-west3us-west8europe-west9me-central2us-east1us-west1us-west3us-central2us-east4us-west2europe-west8us-central1us-west4us-east5us-south1northamerica-northeast1northamerica-northeast2usinca

  
`POST https://cloudkms.googleapis.com/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The `[name](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing.FIELDS.name)` of the `[KeyRing](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings#KeyRing)` associated with the `[ImportJobs](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudkms.importJobs.create`

  
  
### Query parameters

Parameters  
---  
`importJobId` |  `string` Required. It must be unique within a KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`  
  
### Request body

The request body contains an instance of `[ImportJob](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)`.

### Response body

If successful, the response body contains a newly created instance of `[ImportJob](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudkms`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-10 UTC."],[],[]] 
