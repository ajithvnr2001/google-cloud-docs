---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/fetchClusterUpgradeInfo/
title: Method: projects.locations.clusters.fetchClusterUpgradeInfo \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:22.769267+00:00
---

# Method: projects.locations.clusters.fetchClusterUpgradeInfo  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/fetchClusterUpgradeInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  Method: projects.locations.clusters.fetchClusterUpgradeInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Fetch upgrade information of a specific cluster.

### HTTP request

`GET https://container.googleapis.com/v1/{name=projects/*/locations/*/clusters/*}:fetchClusterUpgradeInfo`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name (project, location, cluster) of the cluster to get. Specified in the format `projects/*/locations/*/clusters/*` or `projects/*/zones/*/clusters/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `container.clusters.get`

  
  
### Query parameters

Parameters  
---  
`version` |  `string` API request version that initiates this operation.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ClusterUpgradeInfo](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ClusterUpgradeInfo)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/container`
  * ` https://www.googleapis.com/auth/container.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-15 UTC."],[],[]] 
