---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes
title: REST Resource: projects.locations.privateClouds.clusters.nodes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:06:56.198163+00:00
---

# REST Resource: projects.locations.privateClouds.clusters.nodes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.clusters.nodes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Node
    * JSON representation
  * State
  * Methods



## Resource: Node

Node in a cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "fqdn": string,
      "internalIp": string,
      "nodeTypeId": string,
      "version": string,
      "customCoreCount": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes#State))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this node. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster/nodes/my-node  
`fqdn` |  `string` Output only. Fully qualified domain name of the node.  
`internalIp` |  `string` Output only. Internal IP address of the node.  
`nodeTypeId` |  `string` Output only. The canonical identifier of the node type (corresponds to the `NodeType`). For example: standard-72.  
`version` |  `string` Output only. The version number of the VMware ESXi management component in this cluster.  
`customCoreCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Customized number of cores  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes#State)`)` Output only. The state of the appliance.  
  
## State

Enum State defines possible states of a node in a cluster.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | Node is operational and can be used by the user.  
`CREATING` | Node is being provisioned.  
`FAILED` | Node is in a failed state.  
`UPGRADING` | Node is undergoing maintenance, e.g.: during private cloud upgrade.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes/get)`

|  Gets details of a single node.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters.nodes/list)`

|  Lists nodes in a given cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
