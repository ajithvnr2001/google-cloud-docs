---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems
title: REST Resource: projects.locations.dbSystems \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:43.495893+00:00
---

# REST Resource: projects.locations.dbSystems  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dbSystems Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DbSystem
    * JSON representation
  * DbSystemProperties
    * JSON representation
  * DbSystemDatabaseEdition
  * LicenseModel
  * DataCollectionOptionsDbSystem
    * JSON representation
  * DbSystemLifecycleState
  * DbHome
    * JSON representation
  * ComputeModel
  * DbSystemOptions
    * JSON representation
  * StorageManagement
  * Methods



## Resource: DbSystem

Details of the DbSystem (BaseDB) resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystem/>

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([DbSystemProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemProperties))
      },
      "gcpOracleZone": string,
      "labels": {
        string: string,
        ...
      },
      "odbNetwork": string,
      "odbSubnet": string,
      "entitlementId": string,
      "displayName": string,
      "createTime": string,
      "ociUrl": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the DbSystem resource in the following format: projects/{project}/locations/{region}/dbSystems/{dbSystem}  
`properties` |  `object (`[DbSystemProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemProperties)`)` Optional. The properties of the DbSystem.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle DbSystem is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the DbSystem.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the DbSystem. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Required. The name of the OdbSubnet associated with the DbSystem for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the DbSystem  
`displayName` |  `string` Required. The display name for the System db. The name does not have to be unique within your project.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the DbSystem was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
  
## DbSystemProperties

The properties of a DbSystem.

JSON representation  
---  
      
    
    {
      "shape": string,
      "computeCount": integer,
      "initialDataStorageSizeGb": integer,
      "databaseEdition": enum ([DbSystemDatabaseEdition](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemDatabaseEdition)),
      "licenseModel": enum ([LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#LicenseModel)),
      "sshPublicKeys": [
        string
      ],
      "hostnamePrefix": string,
      "hostname": string,
      "privateIp": string,
      "dataCollectionOptions": {
        object ([DataCollectionOptionsDbSystem](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DataCollectionOptionsDbSystem))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone))
      },
      "lifecycleState": enum ([DbSystemLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemLifecycleState)),
      "dbHome": {
        object ([DbHome](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbHome))
      },
      "ocid": string,
      "memorySizeGb": integer,
      "computeModel": enum ([ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#ComputeModel)),
      "dataStorageSizeGb": integer,
      "recoStorageSizeGb": integer,
      "domain": string,
      "nodeCount": integer,
      "dbSystemOptions": {
        object ([DbSystemOptions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemOptions))
      }
    }  
  
Fields  
---  
`shape` |  `string` Required. Shape of DB System.  
`computeCount` |  `integer` Required. The number of CPU cores to enable for the DbSystem.  
`initialDataStorageSizeGb` |  `integer` Required. The initial data storage size in GB.  
`databaseEdition` |  `enum (`[DbSystemDatabaseEdition](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemDatabaseEdition)`)` Required. The database edition of the DbSystem.  
`licenseModel` |  `enum (`[LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#LicenseModel)`)` Required. The license model of the DbSystem.  
`sshPublicKeys[]` |  `string` Required. SSH public keys to be stored with the DbSystem.  
`hostnamePrefix` |  `string` Optional. Prefix for DB System host names.  
`hostname` |  `string` Output only. The hostname of the DbSystem.  
`privateIp` |  `string` Optional. The private IP address of the DbSystem.  
`dataCollectionOptions` |  `object (`[DataCollectionOptionsDbSystem](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DataCollectionOptionsDbSystem)`)` Optional. Data collection options for diagnostics.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone)`)` Optional. Time zone of the DbSystem.  
`lifecycleState` |  `enum (`[DbSystemLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemLifecycleState)`)` Output only. State of the DbSystem.  
`dbHome` |  `object (`[DbHome](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbHome)`)` Optional. Details for creating a Database Home.  
`ocid` |  `string` Output only. OCID of the DbSystem.  
`memorySizeGb` |  `integer` Optional. The memory size in GB. This value can not be set and is automatically calculated based on the number of ECPUs allocated to the DbSystem.  
`computeModel` |  `enum (`[ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#ComputeModel)`)` Optional. The compute model of the DbSystem.  
`dataStorageSizeGb` |  `integer` Optional. The data storage size in GB that is currently available to DbSystems. The value is same as initialDataStorageSizeGb. This can be modified from OCI console.  
`recoStorageSizeGb` |  `integer` Optional. The reco/redo storage size in GB. The value for recovery storage size is based on the available data storage size.  
`domain` |  `string` Optional. The host domain name of the DbSystem.  
`nodeCount` |  `integer` Optional. The number of nodes to launch for a virtual machine DbSystem. By default this will be set to 1.  
`dbSystemOptions` |  `object (`[DbSystemOptions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#DbSystemOptions)`)` Optional. The options for the DbSystem.  
  
## DbSystemDatabaseEdition

The editions available for DbSystem.

Enums  
---  
`DB_SYSTEM_DATABASE_EDITION_UNSPECIFIED` | The database edition is unspecified.  
`STANDARD_EDITION` | The database edition is Standard.  
`ENTERPRISE_EDITION` | The database edition is Enterprise.  
`ENTERPRISE_EDITION_HIGH_PERFORMANCE` | The database edition is Enterprise Edition.  
  
## LicenseModel

The license model of the DbSystem.

Enums  
---  
`LICENSE_MODEL_UNSPECIFIED` | The license model is unspecified.  
`LICENSE_INCLUDED` | The license model is included.  
`BRING_YOUR_OWN_LICENSE` | The license model is bring your own license.  
  
## DataCollectionOptionsDbSystem

Data collection options for DbSystem.

JSON representation  
---  
      
    
    {
      "isDiagnosticsEventsEnabled": boolean,
      "isIncidentLogsEnabled": boolean
    }  
  
Fields  
---  
`isDiagnosticsEventsEnabled` |  `boolean` Optional. Indicates whether to enable data collection for diagnostics.  
`isIncidentLogsEnabled` |  `boolean` Optional. Indicates whether to enable incident logs and trace collection.  
  
## DbSystemLifecycleState

The various lifecycle states of the DbSystem.

Enums  
---  
`DB_SYSTEM_LIFECYCLE_STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UPDATING` | Indicates that the resource is in updating state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`TERMINATED` | Indicates that the resource is in terminated state.  
`FAILED` | Indicates that the resource is in failed state.  
`MIGRATED` | Indicates that the resource has been migrated.  
`MAINTENANCE_IN_PROGRESS` | Indicates that the resource is in maintenance in progress state.  
`NEEDS_ATTENTION` | Indicates that the resource needs attention.  
`UPGRADING` | Indicates that the resource is upgrading.  
  
## DbHome

Details of the Database Home resource.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "dbVersion": string,
      "database": {
        object ([Database](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database))
      },
      "isUnifiedAuditingEnabled": boolean
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The display name for the Database Home. The name does not have to be unique within your project.  
`dbVersion` |  `string` Required. A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.  
`database` |  `object (`[Database](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database)`)` Required. The Database resource.  
`isUnifiedAuditingEnabled` |  `boolean` Optional. Whether unified auditing is enabled for the Database Home.  
  
## ComputeModel

The compute model of the DbSystem.

Enums  
---  
`COMPUTE_MODEL_UNSPECIFIED` | The compute model is unspecified.  
`ECPU` | The compute model is virtual.  
`OCPU` | Deprecated: This option is not supported. Please use ECPU instead. The compute model is physical.This item is deprecated!  
  
## DbSystemOptions

Details of the DbSystem Options.

JSON representation  
---  
      
    
    {
      "storageManagement": enum ([StorageManagement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#StorageManagement))
    }  
  
Fields  
---  
`storageManagement` |  `enum (`[StorageManagement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems#StorageManagement)`)` Optional. The storage option used in DB system.  
  
## StorageManagement

The storage option used in DB system.

Enums  
---  
`STORAGE_MANAGEMENT_UNSPECIFIED` | The storage management is unspecified.  
`ASM` | Automatic storage management. This option is not supported. Only LVM is supported.  
`LVM` | Logical Volume management.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/create)`

|  Creates a new DbSystem in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/delete)`

|  Deletes a single DbSystem.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/get)`

|  Gets details of a single DbSystem.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/list)`

|  Lists all the DbSystems for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
