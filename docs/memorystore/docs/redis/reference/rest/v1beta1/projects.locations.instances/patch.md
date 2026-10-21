---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/patch/
title: Method: projects.locations.instances.patch \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:50.662088+00:00
---

# Method: projects.locations.instances.patch  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Method: projects.locations.instances.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Updates the metadata and configuration of a specific Redis instance.

Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call operations.delete.

### HTTP request

`PATCH https://redis.googleapis.com/v1beta1/{instance.name=projects/*/locations/*/instances/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`instance.name` |  `string` Required. Unique name of the resource in this scope including project and location using the form: `projects/{projectId}/locations/{locationId}/instances/{instanceId}`Note: Redis instances are managed and addressed at regional level so locationId here refers to a GCP region; however, users may choose which specific zone (or collection of zones for cross-zone instances) an instance should be provisioned in. Refer to `[locationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance.FIELDS.location_id)` and `[alternativeLocationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance.FIELDS.alternative_location_id)` fields for more details.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from `[Instance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance)`:

  * `displayName`
  * `labels`
  * `memorySizeGb`
  * `redisConfig`
  * `replicaCount`

This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Instance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances#Instance)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
