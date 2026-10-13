---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/get/
title: Method: projects.locations.azureClusters.get \u00a0|\u00a0 GKE Multi-Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:10.297645+00:00
---

# Method: projects.locations.azureClusters.get  |  GKE Multi-Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE Multi-Cloud Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations)



Send feedback 

#  Method: projects.locations.azureClusters.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



GKE-on-Azure is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement> for more details.

Describes a specific `[AzureCluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters#AzureCluster)` resource.

### HTTP request

`GET https://{endpoint}/v1/{name=projects/*/locations/*/azureClusters/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[AzureCluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters#AzureCluster)` resource to describe.`AzureCluster` names are formatted as `projects/<project-id>/locations/<region>/azureClusters/<cluster-id>`.See [Resource Names](https://cloud.google.com/apis/design/resource_names) for more details on Google Cloud Platform resource names.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[AzureCluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters#AzureCluster)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gkemulticloud.azureClusters.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
