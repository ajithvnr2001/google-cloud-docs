---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes
title: REST Resource: projects.locations.nodeTypes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:10.151906+00:00
---

# REST Resource: projects.locations.nodeTypes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.nodeTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NodeType
    * JSON representation
  * Kind
  * Capability
  * Methods



## Resource: NodeType

Describes node type.

JSON representation  
---  
      
    
    {
      "name": string,
      "nodeTypeId": string,
      "displayName": string,
      "virtualCpuCount": integer,
      "totalCoreCount": integer,
      "memoryGb": integer,
      "diskSizeGb": integer,
      "availableCustomCoreCounts": [
        integer
      ],
      "kind": enum ([Kind](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#Kind)),
      "families": [
        string
      ],
      "capabilities": [
        enum ([Capability](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#Capability))
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this node type. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-proj/locations/us-central1-a/nodeTypes/standard-72`  
`nodeTypeId` |  `string` Output only. The canonical identifier of the node type (corresponds to the `NodeType`). For example: standard-72.  
`displayName` |  `string` Output only. The friendly name for this node type. For example: ve1-standard-72  
`virtualCpuCount` |  `integer` Output only. The total number of virtual CPUs in a single node.  
`totalCoreCount` |  `integer` Output only. The total number of CPU cores in a single node.  
`memoryGb` |  `integer` Output only. The amount of physical memory available, defined in GB.  
`diskSizeGb` |  `integer` Output only. The amount of storage available, defined in GB.  
`availableCustomCoreCounts[]` |  `integer` Output only. List of possible values of custom core count.  
`kind` |  `enum (`[Kind](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#Kind)`)` Output only. The type of the resource.  
`families[]` |  `string` Output only. Families of the node type. For node types to be in the same cluster they must share at least one element in the `families`.  
`capabilities[]` |  `enum (`[Capability](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#Capability)`)` Output only. Capabilities of this node type.  
  
## Kind

Enum Kind defines possible types of a NodeType.

Enums  
---  
`KIND_UNSPECIFIED` | The default value. This value should never be used.  
`STANDARD` | Standard HCI node.  
`STORAGE_ONLY` | Storage only Node.  
  
## Capability

Capability of a node type.

Enums  
---  
`CAPABILITY_UNSPECIFIED` | The default value. This value is used if the capability is omitted or unknown.  
`STRETCHED_CLUSTERS` | This node type supports stretch clusters.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/get)`

|  Gets details of a single `NodeType`.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/list)`

|  Lists node types  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
