---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1beta/projects.locations.resourceBundles.releases/patch/
title: Method: projects.locations.resourceBundles.releases.patch \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:12.753148+00:00
---

# Method: projects.locations.resourceBundles.releases.patch  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1beta/projects.locations.resourceBundles.releases/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)



Send feedback 

#  Method: projects.locations.resourceBundles.releases.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Updates the parameters of a single Release.

### HTTP request

`PATCH https://configdelivery.googleapis.com/v1beta/{release.name=projects/*/locations/*/resourceBundles/*/releases/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`release.name` |  `string` Identifier. Name of the Release. Format is `projects/{project}/locations/location}/resourceBundles/{resourceBundle}/release/[a-z][a-z0-9\-]{0,62}`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Field mask is used to specify the fields to be overwritten in the Release resource by the update. The fields specified in the updateMask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[Release](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1beta/projects.locations.resourceBundles.releases#Release)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-28 UTC."],[],[]] 
