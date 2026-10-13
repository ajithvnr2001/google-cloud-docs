---
url: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions/patch/
title: Method: projects.locations.lbRouteExtensions.patch \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:50.867962+00:00
---

# Method: projects.locations.lbRouteExtensions.patch  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Method: projects.locations.lbRouteExtensions.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * IAM Permissions



Updates the parameters of the specified `LbRouteExtension` resource.

### HTTP request

`PATCH https://networkservices.googleapis.com/v1/{lbRouteExtension.name=projects/*/locations/*/lbRouteExtensions/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`lbRouteExtension.name` |  `string` Required. Identifier. Name of the `LbRouteExtension` resource in the following format: `projects/{project}/locations/{location}/lbRouteExtensions/{lbRouteExtension}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Used to specify the fields to be overwritten in the `LbRouteExtension` resource by the update. The fields specified in the `updateMask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server guarantees that for 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server ignores the second request This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[LbRouteExtension](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions#LbRouteExtension)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-extensions/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `service` resource:

  * `compute.backendServices.use`
  * `compute.regionBackendServices.use`



Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `forwardingRules` resource:

  * `compute.forwardingRules.update`
  * `compute.globalForwardingRules.update`



Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `networkservices.lbRouteExtensions.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
