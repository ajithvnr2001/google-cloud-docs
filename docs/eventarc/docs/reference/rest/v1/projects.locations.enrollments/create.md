---
url: https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/create/
title: Method: projects.locations.enrollments.create \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:17.539469+00:00
---

# Method: projects.locations.enrollments.create  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Reference ](https://docs.cloud.google.com/eventarc/docs/apis)



Send feedback 

#  Method: projects.locations.enrollments.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Create a new Enrollment in a particular project and location.

### HTTP request

Choose a location:

global asia-south1 asia-south2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central2 northamerica-northeast1 northamerica-northeast2 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us eu

  
`POST https://eventarc.googleapis.com/v1/{parent=projects/*/locations/*}/enrollments`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent collection in which to add this enrollment. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `eventarc.enrollments.create`

  
  
### Query parameters

Parameters  
---  
`enrollmentId` |  `string` Required. The user-provided ID to be assigned to the Enrollment. It should match the format `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`validateOnly` |  `boolean` Optional. If set, validate the request and preview the review, but do not post it.  
  
### Request body

The request body contains an instance of `[Enrollment](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments#Enrollment)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
