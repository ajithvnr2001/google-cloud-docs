---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/patch/
title: Method: projects.locations.zones.patch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:52.445829+00:00
---

# Method: projects.locations.zones.patch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/patch/




#  Method: projects.locations.zones.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates the parameters of a zone.

### HTTP request

`PATCH https://gdchardwaremanagement.googleapis.com/v1alpha/{zone.name=projects/*/locations/*/zones/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`zone.name` |  `string` Identifier. Name of this zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. A mask to specify the fields in the Zone to overwrite with this update. The fields specified in the updateMask are relative to the zone, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155).  
  
### Request body

The request body contains an instance of `[Zone](https://docs.cloud.google.com/distributed-cloud/edge/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones#Zone)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.8.0/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gdchardwaremanagement.zones.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
