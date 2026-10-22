---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/locations/regionalWebhook/
title: Method: locations.regionalWebhook \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:21.012151+00:00
---

# Method: locations.regionalWebhook  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/locations/regionalWebhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: locations.regionalWebhook Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Try it!



locations.regionalWebhook is called when the API receives a regional GitHub webhook.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west15me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`POST https://cloudbuild.googleapis.com/v1/{location=locations/*}/regionalWebhook`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. The location where the webhook should be sent.  
  
### Query parameters

Parameters  
---  
`webhookKey` |  `string` For GitHub Enterprise webhooks, this key is used to associate the webhook request with the GitHubEnterpriseConfig to use for validation.  
  
### Request body

The request body contains an instance of `[HttpBody](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/HttpBody)`.

### Response body

If successful, the response body is an empty JSON object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
