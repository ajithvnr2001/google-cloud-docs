---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/get/
title: Method: projects.locations.rollouts.get \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:09.848986+00:00
---

# Method: projects.locations.rollouts.get  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/get/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.rollouts.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Retrieve a single rollout.

### HTTP request

`GET https://gkehub.googleapis.com/v1alpha/{name=projects/*/locations/*/rollouts/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the rollout to retrieve. projects/{project}/locations/{location}/rollouts/{rollout}  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Rollout](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
