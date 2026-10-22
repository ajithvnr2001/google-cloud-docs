---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/list/
title: Method: projects.locations.workerPools.list \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:14.945220+00:00
---

# Method: projects.locations.workerPools.list  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: projects.locations.workerPools.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists `WorkerPool`s.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west15me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://cloudbuild.googleapis.com/v1/{parent=projects/*/locations/*}/workerPools`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the collection of `WorkerPools`. Format: `projects/{project}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudbuild.workerpools.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of `WorkerPool`s to return. The service may return fewer than this value. If omitted, the server will use a sensible default.  
`pageToken` |  `string` A page token, received from a previous `workerPools.list` call. Provide this to retrieve the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

Response containing existing `WorkerPools`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workerPools": [
        {
          object ([WorkerPool](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#WorkerPool))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workerPools[]` |  `object (`[WorkerPool](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools#WorkerPool)`)` `WorkerPools` for the specified project.  
`nextPageToken` |  `string` Continuation token used to page through large result sets. Provide this value in a subsequent ListWorkerPoolsRequest to return the next page of results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
