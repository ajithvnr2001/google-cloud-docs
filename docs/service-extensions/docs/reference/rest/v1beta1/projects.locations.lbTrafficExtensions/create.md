---
url: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.lbTrafficExtensions/create/
title: Method: projects.locations.lbTrafficExtensions.create \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:15.396901+00:00
---

# Method: projects.locations.lbTrafficExtensions.create  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.lbTrafficExtensions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Method: projects.locations.lbTrafficExtensions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * IAM Permissions



Creates a new `LbTrafficExtension` resource in a given project and location.

### HTTP request

`POST https://networkservices.googleapis.com/v1beta1/{parent=projects/*/locations/*}/lbTrafficExtensions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the `LbTrafficExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`lbTrafficExtensionId` |  `string` Required. User-provided ID of the `LbTrafficExtension` resource to be created.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server ignores the second request This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[LbTrafficExtension](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.lbTrafficExtensions#LbTrafficExtension)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/service-extensions/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `service` resource:

  * `compute.backendServices.use`
  * `compute.regionBackendServices.use`



Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `forwardingRules` resource:

  * `compute.forwardingRules.update`
  * `compute.globalForwardingRules.update`



Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkservices.lbTrafficExtensions.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
