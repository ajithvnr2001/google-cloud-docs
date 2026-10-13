---
url: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submitAsOperation/
title: Method: projects.regions.jobs.submitAsOperation \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:34.586409+00:00
---

# Method: projects.regions.jobs.submitAsOperation  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submitAsOperation/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  Method: projects.regions.jobs.submitAsOperation Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Submits job to a cluster.

### HTTP request

`POST https://dataproc.googleapis.com/v1/projects/{projectId}/regions/{region}/jobs:submitAsOperation`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` Required. The ID of the Google Cloud Platform project that the job belongs to. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `projectId`:

  * `dataproc.jobs.create`
  * `dataproc.clusters.use`

  
`region` |  `string` Required. The Dataproc region in which to handle the request.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "job": {
        object ([Job](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#Job))
      },
      "requestId": string
    }  
  
Fields  
---  
`job` |  `object (`[Job](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#Job)`)` Required. The job resource.  
`requestId` |  `string` Optional. A unique id used to identify the request. If the server receives two [SubmitJobRequest](https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.SubmitJobRequest)s with the same id, then the second request will be ignored and the first `[Job](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#Job)` created and stored in the backend is returned.It is recommended to always set this value to a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier).The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataproc`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
