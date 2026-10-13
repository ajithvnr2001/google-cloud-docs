---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers
title: REST Resource: projects.locations.cloudExadataInfrastructures.dbServers \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:41.807152+00:00
---

# REST Resource: projects.locations.cloudExadataInfrastructures.dbServers  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.cloudExadataInfrastructures.dbServers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbServer
    * JSON representation
  * DbServerProperties
    * JSON representation
  * State
  * Methods



## Resource: DbServer

Details of the database server resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbServer/>

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "properties": {
        object ([DbServerProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers#DbServerProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the database server resource with the format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}/dbServers/{db_server}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`properties` |  `object (`[DbServerProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers#DbServerProperties)`)` Optional. Various properties of the database server.  
  
## DbServerProperties

Various properties and settings associated with Exadata database server.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "ocpuCount": integer,
      "maxOcpuCount": integer,
      "memorySizeGb": integer,
      "maxMemorySizeGb": integer,
      "dbNodeStorageSizeGb": integer,
      "maxDbNodeStorageSizeGb": integer,
      "vmCount": integer,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers#State)),
      "dbNodeIds": [
        string
      ]
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of database server.  
`ocpuCount` |  `integer` Optional. OCPU count per database.  
`maxOcpuCount` |  `integer` Optional. Maximum OCPU count per database.  
`memorySizeGb` |  `integer` Optional. Memory allocated in GBs.  
`maxMemorySizeGb` |  `integer` Optional. Maximum memory allocated in GBs.  
`dbNodeStorageSizeGb` |  `integer` Optional. Local storage per VM.  
`maxDbNodeStorageSizeGb` |  `integer` Optional. Maximum local storage per VM.  
`vmCount` |  `integer` Optional. Vm count per database.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers#State)`)` Output only. State of the database server.  
`dbNodeIds[]` |  `string` Output only. OCID of database nodes associated with the database server.  
  
## State

The various lifecycle states of the database server.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`CREATING` | Indicates that the resource is in creating state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UNAVAILABLE` | Indicates that the resource is in unavailable state.  
`DELETING` | Indicates that the resource is in deleting state.  
`DELETED` | Indicates that the resource is in deleted state.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers/list)`

|  Lists the database servers of an Exadata Infrastructure instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
