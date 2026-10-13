---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemShapes
title: REST Resource: projects.locations.dbSystemShapes \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:43.056690+00:00
---

# REST Resource: projects.locations.dbSystemShapes  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemShapes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dbSystemShapes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbSystemShape
    * JSON representation
  * Methods



## Resource: DbSystemShape

Details of the Database System Shapes resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystemShapeSummary/>

JSON representation  
---  
      
    
    {
      "name": string,
      "shape": string,
      "minNodeCount": integer,
      "maxNodeCount": integer,
      "minStorageCount": integer,
      "maxStorageCount": integer,
      "availableCoreCountPerNode": integer,
      "availableMemoryPerNodeGb": integer,
      "availableDataStorageTb": integer,
      "minCoreCountPerNode": integer,
      "minMemoryPerNodeGb": integer,
      "minDbNodeStoragePerNodeGb": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Database System Shape resource with the format: projects/{project}/locations/{region}/dbSystemShapes/{db_system_shape}  
`shape` |  `string` Optional. shape  
`minNodeCount` |  `integer` Optional. Minimum number of database servers.  
`maxNodeCount` |  `integer` Optional. Maximum number of database servers.  
`minStorageCount` |  `integer` Optional. Minimum number of storage servers.  
`maxStorageCount` |  `integer` Optional. Maximum number of storage servers.  
`availableCoreCountPerNode` |  `integer` Optional. Number of cores per node.  
`availableMemoryPerNodeGb` |  `integer` Optional. Memory per database server node in gigabytes.  
`availableDataStorageTb` |  `integer` Optional. Storage per storage server in terabytes.  
`minCoreCountPerNode` |  `integer` Optional. Minimum core count per node.  
`minMemoryPerNodeGb` |  `integer` Optional. Minimum memory per node in gigabytes.  
`minDbNodeStoragePerNodeGb` |  `integer` Optional. Minimum node storage per database server in gigabytes.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemShapes/list)`

|  Lists the database system shapes available for the project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
