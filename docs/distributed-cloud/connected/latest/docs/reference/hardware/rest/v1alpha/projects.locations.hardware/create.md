---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/create/
title: Method: projects.locations.hardware.create \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:05.462819+00:00
---

# Method: projects.locations.hardware.create  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/hardware/rest/v1alpha/projects.locations.hardware/create/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/apis)



Send feedback 

#  Method: projects.locations.hardware.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates new hardware in a given project and location.

### HTTP request

`POST https://gdchardwaremanagement.googleapis.com/v1alpha/{parent=projects/*/locations/*}/hardware`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location to create hardware in. Format: `projects/{project}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`hardwareId` |  `string` Optional. ID used to uniquely identify the Hardware within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set.The hardware.name field in the request will be ignored.  
  
### Request body

The request body contains an instance of `[Hardware](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/hardware/rest/v1alpha/projects.locations.hardware#Hardware)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `gdchardwaremanagement.hardware.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
