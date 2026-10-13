---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/create/
title: Method: projects.locations.clusters.create \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:28.649440+00:00
---

# Method: projects.locations.clusters.create  |  Google Distributed Cloud connected, version 1.6.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters/create/

Select versionkeyboard_arrow_down

  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/apis)



Send feedback 

#  Method: projects.locations.clusters.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Creates a new Cluster in a given project and location.

### HTTP request

`POST https://edgecontainer.googleapis.com/v1/{parent=projects/*/locations/*}/clusters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent location where this cluster will be created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.clusters.create`

  
  
### Query parameters

Parameters  
---  
`clusterId` |  `string` Required. A client-specified unique identifier for the cluster.  
`requestId` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `requestId` is provided.  
  
### Request body

The request body contains an instance of `[Cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.clusters#Cluster)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/container/rest/v1/projects.locations.operations#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
