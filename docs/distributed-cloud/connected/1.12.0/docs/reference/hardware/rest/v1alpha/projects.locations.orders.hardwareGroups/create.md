---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/create/
title: Method: projects.locations.orders.hardwareGroups.create \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:27.889289+00:00
---

# Method: projects.locations.orders.hardwareGroups.create  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/create/




#  Method: projects.locations.orders.hardwareGroups.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a new hardware group in a given order.

### HTTP request

`POST https://gdchardwaremanagement.googleapis.com/v1alpha/{parent=projects/*/locations/*/orders/*}/hardwareGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The order to create the hardware group in. Format: `projects/{project}/locations/{location}/orders/{order}`  
  
### Query parameters

Parameters  
---  
`hardwareGroupId` |  `string` Optional. ID used to uniquely identify the HardwareGroup within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set.The hardwareGroup.name field in the request will be ignored.  
`requestId` |  `string` Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155).  
  
### Request body

The request body contains an instance of `[HardwareGroup](https://docs.cloud.google.com/distributed-cloud/edge/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups#HardwareGroup)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `gdchardwaremanagement.hardwareGroups.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
