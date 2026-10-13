---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes
title: REST Resource: projects.locations.cloudVmClusters.dbNodes \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:42.623109+00:00
---

# REST Resource: projects.locations.cloudVmClusters.dbNodes  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.cloudVmClusters.dbNodes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbNode
    * JSON representation
    * DbNodeProperties
      * JSON representation
    * State
  * Methods



## Resource: DbNode

Details of the database node resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbNode/>

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([DbNodeProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes#DbNode.DbNodeProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the database node resource in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloudVmCluster}/dbNodes/{db_node}  
`properties` |  `object (`[DbNodeProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes#DbNode.DbNodeProperties)`)` Optional. Various properties of the database node.  
  
### DbNodeProperties

Various properties and settings associated with Db node.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "ocpuCount": integer,
      "memorySizeGb": integer,
      "dbNodeStorageSizeGb": integer,
      "dbServerOcid": string,
      "hostname": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes#DbNode.State)),
      "totalCpuCoreCount": integer,
      "createTime": string
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of database node.  
`ocpuCount` |  `integer` Optional. OCPU count per database node.  
`memorySizeGb` |  `integer` Memory allocated in GBs.  
`dbNodeStorageSizeGb` |  `integer` Optional. Local storage per database node.  
`dbServerOcid` |  `string` Optional. Database server OCID.  
`hostname` |  `string` Optional. DNS  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes#DbNode.State)`)` Output only. State of the database node.  
`totalCpuCoreCount` |  `integer` Total CPU core count of the database node.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the database node was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### State

The various lifecycle states of the database node.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UPDATING` | Indicates that the resource is in updating state.  
`STOPPING` | Indicates that the resource is in stopping state.  
`STOPPED` | Indicates that the resource is in stopped state.  
`STARTING` | Indicates that the resource is in starting state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`TERMINATED` | Indicates that the resource is in terminated state.  
`FAILED` | Indicates that the resource is in failed state.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes/list)`

|  Lists the database nodes of a VM Cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
