---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/delete/
title: Method: projects.locations.clusters.nodePools.delete \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:39.180960+00:00
---

# Method: projects.locations.clusters.nodePools.delete  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/delete/




#  Method: projects.locations.clusters.nodePools.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Deletes a single NodePool.

### HTTP request

`DELETE https://edgecontainer.googleapis.com/v1/{name=projects/*/locations/*/clusters/*/nodePools/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the node pool. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `edgecontainer.nodePools.delete`

  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `requestId` is provided.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.5.1/docs/reference/container/rest/v1/projects.locations.operations#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
