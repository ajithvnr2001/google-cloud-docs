---
url: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/patch/
title: Method: projects.profiles.patch \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:43.557201+00:00
---

# Method: projects.profiles.patch  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/reference/v2/rest/v2/projects.profiles/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Reference ](https://docs.cloud.google.com/profiler/docs/reference/v2)



Send feedback 

#  Method: projects.profiles.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



profiles.patch updates the profile bytes and labels on the profile resource created in the online mode. Updating the bytes for profiles created in the offline mode is currently not supported: the profile content must be provided at the time of the profile creation.

_Direct use of this API is discouraged, please use a[supported profiler agent](https://cloud.google.com/profiler/docs/about-profiler#profiling_agent) instead for profile collection._

### HTTP request

`PATCH https://cloudprofiler.googleapis.com/v2/{profile.name=projects/*/profiles/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`profile.name` |  `string` Output only. Opaque, server-assigned, unique ID for this profile. It takes the form `projects/{project}/profiles/{profile}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Field mask used to specify the fields to be overwritten. Currently only profileBytes and labels fields are supported by profiles.patch, so only those fields can be specified in the mask. When no mask is provided, all fields are overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
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
