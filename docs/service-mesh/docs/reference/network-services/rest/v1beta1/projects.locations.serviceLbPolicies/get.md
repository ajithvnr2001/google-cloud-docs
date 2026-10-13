---
url: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/get/
title: Method: projects.locations.serviceLbPolicies.get \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:54.173841+00:00
---

# Method: projects.locations.serviceLbPolicies.get  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/get/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/docs/apis)



Send feedback 

#  Method: projects.locations.serviceLbPolicies.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets details of a single ServiceLbPolicy.

### HTTP request

`GET https://networkservices.googleapis.com/v1beta1/{name=projects/*/locations/*/serviceLbPolicies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. A name of the ServiceLbPolicy to get. Must be in the format `projects/{project}/locations/{location}/serviceLbPolicies/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `networkservices.serviceLbPolicies.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ServiceLbPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies#ServiceLbPolicy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
