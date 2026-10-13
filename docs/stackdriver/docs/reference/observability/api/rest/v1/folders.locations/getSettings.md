---
url: https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/getSettings/
title: Method: folders.locations.getSettings \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:50.005300+00:00
---

# Method: folders.locations.getSettings  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations/getSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Method: folders.locations.getSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Get Settings

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast2asia-southeast3australia-southeast2europe-north2europe-west1europe-west3europe-west4europe-west6europe-west8me-central1northamerica-northeast2northamerica-south1southamerica-west1us-central1us-east1us-east5us-south1us-west1us-west2us-west3asia-northeast1asia-southeast1australia-southeast1europe-central2europe-north1europe-southwest1europe-west10europe-west12europe-west2europe-west9me-central2me-west1northamerica-northeast1southamerica-east1us-east4us-west4useu

  
`GET https://observability.googleapis.com/v1/{name=folders/*/locations/*/settings}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the settings to retrieve.Name format:
    
    
    "projects/[PROJECT_ID]/locations/[LOCATION]/settings"
    "folders/[FOLDER_ID]/locations/[LOCATION]/settings"
    "organizations/[ORGANIZATION_ID]/locations/[LOCATION]/settings"
      
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Settings](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/Settings)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `observability.settings.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
