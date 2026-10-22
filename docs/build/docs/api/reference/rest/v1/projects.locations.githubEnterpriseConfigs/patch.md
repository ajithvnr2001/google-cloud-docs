---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/patch/
title: Method: projects.locations.githubEnterpriseConfigs.patch \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:16.188359+00:00
---

# Method: projects.locations.githubEnterpriseConfigs.patch  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: projects.locations.githubEnterpriseConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Update an association between a GCP project and a GitHub Enterprise server.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west15me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`PATCH https://cloudbuild.googleapis.com/v1/{githubEnterpriseConfig.name=projects/*/locations/*/githubEnterpriseConfigs/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`githubEnterpriseConfig.name` |  `string` Identifier. The full resource name for the GitHubEnterpriseConfig For example: "projects/{$projectId}/locations/{$locationId}/githubEnterpriseConfigs/{$configId}"  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Update mask for the resource. If this is set, the server will only update the fields specified in the field mask. Otherwise, a full update of the mutable resource fields will be performed.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[GitHubEnterpriseConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.githubEnterpriseConfigs#GitHubEnterpriseConfig)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
