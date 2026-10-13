---
url: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.gateways/create/
title: Method: projects.locations.gateways.create \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:37.224537+00:00
---

# Method: projects.locations.gateways.create  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.gateways/create/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/docs/apis)



Send feedback 

#  Method: projects.locations.gateways.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new Gateway in a given project and location.

### HTTP request

`POST https://networkservices.googleapis.com/v1/{parent=projects/*/locations/*}/gateways`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the Gateway. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkservices.gateways.create`

  
  
### Query parameters

Parameters  
---  
`gatewayId` |  `string` Required. Short name of the Gateway resource to be created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `gatewayId`:

  * `networkservices.gateways.create`

  
  
### Request body

The request body contains an instance of `[Gateway](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.gateways#Gateway)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
