---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases
title: REST Resource: projects.locations.pluggableDatabases \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:54.269930+00:00
---

# REST Resource: projects.locations.pluggableDatabases  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.pluggableDatabases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PluggableDatabase
    * JSON representation
  * PluggableDatabaseProperties
    * JSON representation
  * PluggableDatabaseConnectionStrings
    * JSON representation
  * DefinedTagValue
    * JSON representation
  * PluggableDatabaseLifecycleState
  * PluggableDatabaseNodeLevelDetails
    * JSON representation
  * PluggableDatabaseOpenMode
  * OperationsInsightsState
  * Methods



## Resource: PluggableDatabase

The PluggableDatabase resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/PluggableDatabase/>

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([PluggableDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseProperties))
      },
      "ociUrl": string,
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the PluggableDatabase resource in the following format: projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}  
`properties` |  `object (`[PluggableDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseProperties)`)` Optional. The properties of the PluggableDatabase.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the PluggableDatabase was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## PluggableDatabaseProperties

The properties of a PluggableDatabase.

JSON representation  
---  
      
    
    {
      "compartmentId": string,
      "connectionStrings": {
        object ([PluggableDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseConnectionStrings))
      },
      "containerDatabaseOcid": string,
      "definedTags": {
        string: {
          object ([DefinedTagValue](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#DefinedTagValue))
        },
        ...
      },
      "freeformTags": {
        string: string,
        ...
      },
      "ocid": string,
      "isRestricted": boolean,
      "lifecycleDetails": string,
      "lifecycleState": enum ([PluggableDatabaseLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseLifecycleState)),
      "pdbName": string,
      "pdbNodeLevelDetails": [
        {
          object ([PluggableDatabaseNodeLevelDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseNodeLevelDetails))
        }
      ],
      "databaseManagementConfig": {
        object ([DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig))
      },
      "operationsInsightsState": enum ([OperationsInsightsState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#OperationsInsightsState))
    }  
  
Fields  
---  
`compartmentId` |  `string` Required. The OCID of the compartment.  
`connectionStrings` |  `object (`[PluggableDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseConnectionStrings)`)` Optional. The Connection strings used to connect to the Oracle Database.  
`containerDatabaseOcid` |  `string` Required. The OCID of the CDB.  
`definedTags` |  `map (key: string, value: object (`[DefinedTagValue](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#DefinedTagValue)`))` Optional. Defined tags for this resource. Each key is predefined and scoped to a namespace.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`freeformTags` |  `map (key: string, value: string)` Optional. Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`ocid` |  `string` Output only. The OCID of the pluggable database.  
`isRestricted` |  `boolean` Optional. The restricted mode of the pluggable database. If a pluggable database is opened in restricted mode, the user needs both create a session and have restricted session privileges to connect to it.  
`lifecycleDetails` |  `string` Output only. Additional information about the current lifecycle state.  
`lifecycleState` |  `enum (`[PluggableDatabaseLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseLifecycleState)`)` Output only. The current state of the pluggable database.  
`pdbName` |  `string` Required. The database name.  
`pdbNodeLevelDetails[]` |  `object (`[PluggableDatabaseNodeLevelDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseNodeLevelDetails)`)` Optional. Pluggable Database Node Level Details  
`databaseManagementConfig` |  `object (`[DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig)`)` Output only. The configuration of the Database Management service.  
`operationsInsightsState` |  `enum (`[OperationsInsightsState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#OperationsInsightsState)`)` Output only. The status of Operations Insights for this Database.  
  
## PluggableDatabaseConnectionStrings

The connection strings used to connect to the Oracle Database.

JSON representation  
---  
      
    
    {
      "allConnectionStrings": {
        string: string,
        ...
      },
      "pdbDefault": string,
      "pdbIpDefault": string
    }  
  
Fields  
---  
`allConnectionStrings` |  `map (key: string, value: string)` Optional. All connection strings to use to connect to the pluggable database.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pdbDefault` |  `string` Optional. The default connection string to use to connect to the pluggable database.  
`pdbIpDefault` |  `string` Optional. The default connection string to use to connect to the pluggable database using IP.  
  
## DefinedTagValue

Wrapper message for the value of a defined tag.

JSON representation  
---  
      
    
    {
      "tags": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`tags` |  `map (key: string, value: string)` The tags within the namespace.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## PluggableDatabaseLifecycleState

The various lifecycle states of the PluggableDatabase.

Enums  
---  
`PLUGGABLE_DATABASE_LIFECYCLE_STATE_UNSPECIFIED` | The lifecycle state is unspecified.  
`PROVISIONING` | The pluggable database is provisioning.  
`AVAILABLE` | The pluggable database is available.  
`TERMINATING` | The pluggable database is terminating.  
`TERMINATED` | The pluggable database is terminated.  
`UPDATING` | The pluggable database is updating.  
`FAILED` | The pluggable database is in a failed state.  
`RELOCATING` | The pluggable database is relocating.  
`RELOCATED` | The pluggable database is relocated.  
`REFRESHING` | The pluggable database is refreshing.  
`RESTORE_IN_PROGRESS` | The pluggable database is restoring.  
`RESTORE_FAILED` | The pluggable database restore failed.  
`BACKUP_IN_PROGRESS` | The pluggable database is backing up.  
`DISABLED` | The pluggable database is disabled.  
  
## PluggableDatabaseNodeLevelDetails

The Pluggable Database Node Level Details.

JSON representation  
---  
      
    
    {
      "nodeName": string,
      "openMode": enum ([PluggableDatabaseOpenMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseOpenMode)),
      "pluggableDatabaseId": string
    }  
  
Fields  
---  
`nodeName` |  `string` Required. The Node name of the Database home.  
`openMode` |  `enum (`[PluggableDatabaseOpenMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases#PluggableDatabaseOpenMode)`)` Required. The mode that the pluggable database is in to open it.  
`pluggableDatabaseId` |  `string` Required. The OCID of the Pluggable Database.  
  
## PluggableDatabaseOpenMode

The mode that the pluggable database is in to open it.

Enums  
---  
`PLUGGABLE_DATABASE_OPEN_MODE_UNSPECIFIED` | The open mode is unspecified.  
`READ_ONLY` | The pluggable database is opened in read-only mode.  
`READ_WRITE` | The pluggable database is opened in read-write mode.  
`MOUNTED` | The pluggable database is mounted.  
`MIGRATE` | The pluggable database is migrated.  
  
## OperationsInsightsState

The status of Operations Insights for this Database.

Enums  
---  
`OPERATIONS_INSIGHTS_STATE_UNSPECIFIED` | The status is not specified.  
`ENABLING` | Operations Insights is enabling.  
`ENABLED` | Operations Insights is enabled.  
`DISABLING` | Operations Insights is disabling.  
`NOT_ENABLED` | Operations Insights is not enabled.  
`FAILED_ENABLING` | Operations Insights failed to enable.  
`FAILED_DISABLING` | Operations Insights failed to disable.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases/get)`

|  Gets details of a single PluggableDatabase.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases/list)`

|  Lists all the PluggableDatabases for the given project, location and Container Database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
