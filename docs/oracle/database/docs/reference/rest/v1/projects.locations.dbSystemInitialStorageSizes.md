---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes
title: REST Resource: projects.locations.dbSystemInitialStorageSizes \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:45.037834+00:00
---

# REST Resource: projects.locations.dbSystemInitialStorageSizes  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dbSystemInitialStorageSizes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbSystemInitialStorageSize
    * JSON representation
  * DbSystemInitialStorageSizeProperties
    * JSON representation
  * StorageManagement
  * ShapeType
  * StorageSizeDetails
    * JSON representation
  * Methods



## Resource: DbSystemInitialStorageSize

Summary of the DbSystem initial storage size.

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([DbSystemInitialStorageSizeProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#DbSystemInitialStorageSizeProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the resource.  
`properties` |  `object (`[DbSystemInitialStorageSizeProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#DbSystemInitialStorageSizeProperties)`)` Output only. The properties of the DbSystem initial storage size summary.  
  
## DbSystemInitialStorageSizeProperties

The properties of a DbSystem initial storage size summary.

JSON representation  
---  
      
    
    {
      "storageManagement": enum ([StorageManagement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageManagement)),
      "shapeType": enum ([ShapeType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#ShapeType)),
      "storageSizeDetails": [
        {
          object ([StorageSizeDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageSizeDetails))
        }
      ],
      "launchFromBackupStorageSizeDetails": [
        {
          object ([StorageSizeDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageSizeDetails))
        }
      ]
    }  
  
Fields  
---  
`storageManagement` |  `enum (`[StorageManagement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageManagement)`)` Output only. The storage option used in DB system.  
`shapeType` |  `enum (`[ShapeType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#ShapeType)`)` Output only. VM shape platform type  
`storageSizeDetails[]` |  `object (`[StorageSizeDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageSizeDetails)`)` Output only. List of storage disk details.  
`launchFromBackupStorageSizeDetails[]` |  `object (`[StorageSizeDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes#StorageSizeDetails)`)` Output only. List of storage disk details available for launches from backup.  
  
## StorageManagement

The storage option used in the DB system.

Enums  
---  
`STORAGE_MANAGEMENT_UNSPECIFIED` | Unspecified storage management.  
`ASM` | Automatic Storage Management.  
`LVM` | Logical Volume Management.  
  
## ShapeType

The shape type of the DB system.

Enums  
---  
`SHAPE_TYPE_UNSPECIFIED` | Unspecified shape type.  
`STANDARD_X86` | Standard X86.  
  
## StorageSizeDetails

The initial storage size, in gigabytes, that is applicable for virtual machine DBSystem.

JSON representation  
---  
      
    
    {
      "dataStorageSizeInGbs": integer,
      "recoStorageSizeInGbs": integer
    }  
  
Fields  
---  
`dataStorageSizeInGbs` |  `integer` Output only. The data storage size, in gigabytes, that is applicable for virtual machine DBSystem.  
`recoStorageSizeInGbs` |  `integer` Output only. The RECO/REDO storage size, in gigabytes, that is applicable for virtual machine DBSystem.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes/list)`

|  Lists all the DbSystemInitialStorageSizes for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
