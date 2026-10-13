---
url: https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update/
title: Method: projects.locations.jobs.update \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:01.285661+00:00
---

# Method: projects.locations.jobs.update  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Method: projects.locations.jobs.update Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the state of an existing Cloud Dataflow job.

To update the state of an existing job, we recommend using `projects.locations.jobs.update` with a [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.update` is not recommended, as you can only update the state of jobs that are running in `us-central1`.

### IAM Permissions

  1. Requires the `dataflow.jobs.cancel` permission to cancel a job.
  2. Requires the `dataflow.jobs.updateContents` permission to update runtime parameters.



### HTTP request

Choose a location:

global

  
`PUT https://dataflow.googleapis.com/v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` The ID of the Cloud Platform project that the job belongs to.  
`location` |  `string` The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job.  
`jobId` |  `string` The job ID.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The list of fields to update relative to Job. If empty, only RequestedJobState will be considered for update. If the FieldMask is not empty and RequestedJobState is none/empty, The fields specified in the update mask will be the only ones considered for update. If both RequestedJobState and updateMask are specified, an error will be returned as we cannot update both state and mask.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Job](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job)`.

### Response body

If successful, the response body contains an instance of `[Job](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
