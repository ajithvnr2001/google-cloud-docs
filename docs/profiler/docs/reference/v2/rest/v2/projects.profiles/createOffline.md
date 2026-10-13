---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/createOffline/
title: Method: projects.profiles.createOffline \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:43.438518+00:00
---

# Method: projects.profiles.createOffline  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/createOffline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  Method: projects.profiles.createOffline Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



profiles.createOffline creates a new profile resource in the offline mode. The client provides the profile to create along with the profile bytes, the server records it.

_Direct use of this API is discouraged, please use a[supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._

### HTTP request

`POST https://cloudprofiler.googleapis.com/v2/{parent=projects/*}/profiles:createOffline`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Parent project to create the profile in. It takes the form `projects/{project}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `cloudprofiler.profiles.create`

  
  
### Request body

The request body contains an instance of `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Profile)`.

### Response body

If successful, the response body contains an instance of `[Profile](https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles#Profile)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
