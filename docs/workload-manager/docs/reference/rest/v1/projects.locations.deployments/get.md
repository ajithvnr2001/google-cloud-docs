---
url: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/get/
title: Method: projects.locations.deployments.get \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:59.230396+00:00
---

# Method: projects.locations.deployments.get  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/workload-manager/docs/authentication)



Send feedback 

#  Method: projects.locations.deployments.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets details of a single Deployment.

### HTTP request

`GET https://workloadmanager.googleapis.com/v1/{name=projects/*/locations/*/deployments/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the resource. The format is 'projects/{projectId}/locations/{locationId}/deployments/{deploymentId}'.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Deployment](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Deployment)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
