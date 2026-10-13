---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/create/
title: Method: projects.locations.bareMetalClusters.bareMetalNodePools.create \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:14.671861+00:00
---

# Method: projects.locations.bareMetalClusters.bareMetalNodePools.create  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Method: projects.locations.bareMetalClusters.bareMetalNodePools.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new bare metal node pool in a given project, location and Bare Metal cluster.

### HTTP request

`POST https://gkeonprem.googleapis.com/v1/{parent=projects/*/locations/*/bareMetalClusters/*}/bareMetalNodePools`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this node pool will be created. projects/{project}/locations/{location}/bareMetalClusters/{cluster}  
  
### Query parameters

Parameters  
---  
`bareMetalNodePoolId` |  `string` The ID to use for the node pool, which will become the final component of the node pool's resource name.This value must be up to 63 characters, and valid characters are /[a-z][0-9]-/.The value must not be permitted to be a UUID (or UUID-like: anything matching /^[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$/i).  
`validateOnly` |  `boolean` If set, only validate the request, but do not actually create the node pool.  
  
### Request body

The request body contains an instance of `[BareMetalNodePool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools#BareMetalNodePool)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
