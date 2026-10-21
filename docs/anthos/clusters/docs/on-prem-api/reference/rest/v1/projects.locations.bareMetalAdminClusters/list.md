---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalAdminClusters/list/
title: Method: projects.locations.bareMetalAdminClusters.list \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:15.832970+00:00
---

# Method: projects.locations.bareMetalAdminClusters.list  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalAdminClusters/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Method: projects.locations.bareMetalAdminClusters.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * ClusterView



Lists bare metal admin clusters in a given project and location.

### HTTP request

`GET https://gkeonprem.googleapis.com/v1/{parent=projects/*/locations/*}/bareMetalAdminClusters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the project and location where the clusters are listed in. Format: "projects/{project}/locations/{location}"  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. Server may return fewer items than requested. If unspecified, at most 50 clusters will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A token identifying a page of results the server should return.  
`view` |  `enum (`[ClusterView](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/list#ClusterView)`)` View for bare metal admin clusters. When `BASIC` is specified, only the admin cluster resource name and membership are returned. The default/unset value `CLUSTER_VIEW_UNSPECIFIED` is the same as `FULL', which returns the complete admin cluster configuration details.  
`allowMissing` |  `boolean` Optional. If true, return list of BareMetal Admin Clusters including the ones that only exists in RMS.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing bare metal admin clusters.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "bareMetalAdminClusters": [
        {
          object ([BareMetalAdminCluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminCluster))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`bareMetalAdminClusters[]` |  `object (`[BareMetalAdminCluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#BareMetalAdminCluster)`)` The list of bare metal admin cluster.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ClusterView

A view for admin cluster resources.

Enums  
---  
`CLUSTER_VIEW_UNSPECIFIED` | If the value is not set, the default `FULL` view is used.  
`BASIC` | Includes basic information of a admin cluster resource including admin cluster resource name and membership.  
`FULL` | Includes the complete configuration for bare metal admin cluster resource. This is the default value for ListBareMetalAdminClustersRequest method.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
