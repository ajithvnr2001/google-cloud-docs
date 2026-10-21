---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig/
title: Method: projects.locations.bareMetalClusters.queryVersionConfig \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:17.068858+00:00
---

# Method: projects.locations.bareMetalClusters.queryVersionConfig  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Method: projects.locations.bareMetalClusters.queryVersionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * BareMetalClusterCreateConfig
    * JSON representation
  * BareMetalClusterUpgradeConfig
    * JSON representation



Queries the bare metal user cluster version config.

### HTTP request

`POST https://gkeonprem.googleapis.com/v1/{parent=projects/*/locations/*}/bareMetalClusters:queryVersionConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the project and location to query for version config. Format: "projects/{project}/locations/{location}"  
  
### Query parameters

Parameters  
---  
Union parameter `config_type`. The config of the version config request to specify the use case to list versions. `config_type` can be only one of the following:  
`createConfig` |  `object (`[BareMetalClusterCreateConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig#BareMetalClusterCreateConfig)`)` User cluster create use case. Require admin cluster membership or resource name.  
`upgradeConfig` |  `object (`[BareMetalClusterUpgradeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig#BareMetalClusterUpgradeConfig)`)` User cluster upgrade use case. Require user cluster resource name.  
  
### Request body

The request body must be empty.

### Response body

Response message for querying bare metal admin cluster version config.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "versions": [
        {
          object ([BareMetalVersionInfo](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalVersionInfo))
        }
      ]
    }  
  
Fields  
---  
`versions[]` |  `object (`[BareMetalVersionInfo](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalVersionInfo)`)` List of available versions to install or to upgrade to.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## BareMetalClusterCreateConfig

Message for bare metal user cluster create config.

JSON representation  
---  
      
    
    {
    
      // Union field admin_cluster can be only one of the following:
      "adminClusterMembership": string,
      "adminClusterName": string
      // End of list of possible types for union field admin_cluster.
    }  
  
Fields  
---  
Union field `admin_cluster`.`admin_cluster` can be only one of the following:  
`adminClusterMembership` |  `string` The admin cluster membership. This is the full resource name of the admin cluster's fleet membership. Format: "projects/{project}/locations/{location}/memberships/{membership}"  
`adminClusterName` |  `string` The admin cluster resource name. This is the full resource name of the admin cluster resource. Format: "projects/{project}/locations/{location}/bareMetalAdminClusters/{bareMetalAdminCluster}"  
  
## BareMetalClusterUpgradeConfig

Message for bare metal user cluster upgrade config.

JSON representation  
---  
      
    
    {
      "clusterName": string
    }  
  
Fields  
---  
`clusterName` |  `string` The user cluster resource name. This is the full resource name of the user cluster resource. Format: "projects/{project}/locations/{location}/bareMetalClusters/{bareMetalCluster}"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
