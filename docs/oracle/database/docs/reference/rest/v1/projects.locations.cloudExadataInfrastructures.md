---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures
title: REST Resource: projects.locations.cloudExadataInfrastructures \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:41.741371+00:00
---

# REST Resource: projects.locations.cloudExadataInfrastructures  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.cloudExadataInfrastructures Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CloudExadataInfrastructure
    * JSON representation
  * CloudExadataInfrastructureProperties
    * JSON representation
  * MaintenanceWindow
    * JSON representation
  * MaintenanceWindowPreference
  * Month
  * PatchingMode
  * State
  * ExascaleConfig
    * JSON representation
  * Methods



## Resource: CloudExadataInfrastructure

Represents CloudExadataInfrastructure resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/>

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "gcpOracleZone": string,
      "entitlementId": string,
      "properties": {
        object ([CloudExadataInfrastructureProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#CloudExadataInfrastructureProperties))
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Exadata Infrastructure resource with the format: projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloudExadataInfrastructure}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle Exadata Infrastructure is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`entitlementId` |  `string` Output only. Entitlement ID of the private offer against which this infrastructure resource is provisioned.  
`properties` |  `object (`[CloudExadataInfrastructureProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#CloudExadataInfrastructureProperties)`)` Optional. Various properties of the infra.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Exadata Infrastructure was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## CloudExadataInfrastructureProperties

Various properties of Exadata Infrastructure.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "computeCount": integer,
      "storageCount": integer,
      "totalStorageSizeGb": integer,
      "availableStorageSizeGb": integer,
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#MaintenanceWindow))
      },
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#State)),
      "shape": string,
      "ociUrl": string,
      "cpuCount": integer,
      "maxCpuCount": integer,
      "memorySizeGb": integer,
      "maxMemoryGb": integer,
      "dbNodeStorageSizeGb": integer,
      "maxDbNodeStorageSizeGb": integer,
      "dataStorageSizeTb": number,
      "maxDataStorageTb": number,
      "activatedStorageCount": integer,
      "additionalStorageCount": integer,
      "dbServerVersion": string,
      "storageServerVersion": string,
      "nextMaintenanceRunId": string,
      "nextMaintenanceRunTime": string,
      "nextSecurityMaintenanceRunTime": string,
      "customerContacts": [
        {
          object ([CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/CustomerContact))
        }
      ],
      "monthlyStorageServerVersion": string,
      "monthlyDbServerVersion": string,
      "computeModel": enum ([ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/ComputeModel)),
      "databaseServerType": string,
      "storageServerType": string,
      "exascaleConfig": {
        object ([ExascaleConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#ExascaleConfig))
      }
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of created infra. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>  
`computeCount` |  `integer` Optional. The number of compute servers for the Exadata Infrastructure.  
`storageCount` |  `integer` Optional. The number of Cloud Exadata storage servers for the Exadata Infrastructure.  
`totalStorageSizeGb` |  `integer` Optional. The total storage allocated to the Exadata Infrastructure resource, in gigabytes (GB).  
`availableStorageSizeGb` |  `integer` Output only. The available storage can be allocated to the Exadata Infrastructure resource, in gigabytes (GB).  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#MaintenanceWindow)`)` Optional. Maintenance window for repair.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#State)`)` Output only. The current lifecycle state of the Exadata Infrastructure.  
`shape` |  `string` Required. The shape of the Exadata Infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance.  
`ociUrl` |  `string` Output only. Deep link to the OCI console to view this resource.  
`cpuCount` |  `integer` Output only. The number of enabled CPU cores.  
`maxCpuCount` |  `integer` Output only. The total number of CPU cores available.  
`memorySizeGb` |  `integer` Output only. The memory allocated in GBs.  
`maxMemoryGb` |  `integer` Output only. The total memory available in GBs.  
`dbNodeStorageSizeGb` |  `integer` Output only. The local node storage allocated in GBs.  
`maxDbNodeStorageSizeGb` |  `integer` Output only. The total local node storage available in GBs.  
`dataStorageSizeTb` |  `number` Output only. Size, in terabytes, of the DATA disk group.  
`maxDataStorageTb` |  `number` Output only. The total available DATA disk group size.  
`activatedStorageCount` |  `integer` Output only. The requested number of additional storage servers activated for the Exadata Infrastructure.  
`additionalStorageCount` |  `integer` Output only. The requested number of additional storage servers for the Exadata Infrastructure.  
`dbServerVersion` |  `string` Output only. The software version of the database servers (dom0) in the Exadata Infrastructure.  
`storageServerVersion` |  `string` Output only. The software version of the storage servers (cells) in the Exadata Infrastructure.  
`nextMaintenanceRunId` |  `string` Output only. The OCID of the next maintenance run.  
`nextMaintenanceRunTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the next maintenance run will occur.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextSecurityMaintenanceRunTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the next security maintenance run will occur.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`customerContacts[]` |  `object (`[CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/CustomerContact)`)` Optional. The list of customer contacts.  
`monthlyStorageServerVersion` |  `string` Output only. The monthly software version of the storage servers (cells) in the Exadata Infrastructure. Example: 20.1.15  
`monthlyDbServerVersion` |  `string` Output only. The monthly software version of the database servers (dom0) in the Exadata Infrastructure. Example: 20.1.15  
`computeModel` |  `enum (`[ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/ComputeModel)`)` Output only. The compute model of the Exadata Infrastructure.  
`databaseServerType` |  `string` Output only. The database server type of the Exadata Infrastructure.  
`storageServerType` |  `string` Output only. The storage server type of the Exadata Infrastructure.  
`exascaleConfig` |  `object (`[ExascaleConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#ExascaleConfig)`)` Output only. The Exascale configuration for the Exadata Infrastructure.  
  
## MaintenanceWindow

Maintenance window as defined by Oracle. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/MaintenanceWindow>

JSON representation  
---  
      
    
    {
      "preference": enum ([MaintenanceWindowPreference](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#MaintenanceWindowPreference)),
      "months": [
        enum ([Month](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#Month))
      ],
      "weeksOfMonth": [
        integer
      ],
      "daysOfWeek": [
        enum ([DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek))
      ],
      "hoursOfDay": [
        integer
      ],
      "leadTimeWeek": integer,
      "patchingMode": enum ([PatchingMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#PatchingMode)),
      "customActionTimeoutMins": integer,
      "isCustomActionTimeoutEnabled": boolean
    }  
  
Fields  
---  
`preference` |  `enum (`[MaintenanceWindowPreference](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#MaintenanceWindowPreference)`)` Optional. The maintenance window scheduling preference.  
`months[]` |  `enum (`[Month](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#Month)`)` Optional. Months during the year when maintenance should be performed.  
`weeksOfMonth[]` |  `integer` Optional. Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.  
`daysOfWeek[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)`)` Optional. Days during the week when maintenance should be performed.  
`hoursOfDay[]` |  `integer` Optional. The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are: 0 - represents time slot 0:00 - 3:59 UTC 4 - represents time slot 4:00 - 7:59 UTC 8 - represents time slot 8:00 - 11:59 UTC 12 - represents time slot 12:00 - 15:59 UTC 16 - represents time slot 16:00 - 19:59 UTC 20 - represents time slot 20:00 - 23:59 UTC  
`leadTimeWeek` |  `integer` Optional. Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.  
`patchingMode` |  `enum (`[PatchingMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures#PatchingMode)`)` Optional. Cloud CloudExadataInfrastructure node patching method, either "ROLLING" or "NONROLLING". Default value is ROLLING.  
`customActionTimeoutMins` |  `integer` Optional. Determines the amount of time the system will wait before the start of each database server patching operation. Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).  
`isCustomActionTimeoutEnabled` |  `boolean` Optional. If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.  
  
## MaintenanceWindowPreference

Maintenance window preference.

Enums  
---  
`MAINTENANCE_WINDOW_PREFERENCE_UNSPECIFIED` | Default unspecified value.  
`CUSTOM_PREFERENCE` | Custom preference.  
`NO_PREFERENCE` | No preference.  
  
## Month

Represents a month in the Gregorian calendar.

Enums  
---  
`MONTH_UNSPECIFIED` | The unspecified month.  
`JANUARY` | The month of January.  
`FEBRUARY` | The month of February.  
`MARCH` | The month of March.  
`APRIL` | The month of April.  
`MAY` | The month of May.  
`JUNE` | The month of June.  
`JULY` | The month of July.  
`AUGUST` | The month of August.  
`SEPTEMBER` | The month of September.  
`OCTOBER` | The month of October.  
`NOVEMBER` | The month of November.  
`DECEMBER` | The month of December.  
  
## PatchingMode

Patching mode.

Enums  
---  
`PATCHING_MODE_UNSPECIFIED` | Default unspecified value.  
`ROLLING` | Updates the Cloud Exadata database server hosts in a rolling fashion.  
`NON_ROLLING` | The non-rolling maintenance method first updates your storage servers at the same time, then your database servers at the same time.  
  
## State

The various lifecycle states of the Exadata Infrastructure.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | The Exadata Infrastructure is being provisioned.  
`AVAILABLE` | The Exadata Infrastructure is available for use.  
`UPDATING` | The Exadata Infrastructure is being updated.  
`TERMINATING` | The Exadata Infrastructure is being terminated.  
`TERMINATED` | The Exadata Infrastructure is terminated.  
`FAILED` | The Exadata Infrastructure is in failed state.  
`MAINTENANCE_IN_PROGRESS` | The Exadata Infrastructure is in maintenance.  
  
## ExascaleConfig

Details of the Exascale configuration for the Exadata Infrastructure.

JSON representation  
---  
      
    
    {
      "totalStorageSizeGb": integer,
      "availableStorageSizeGb": integer
    }  
  
Fields  
---  
`totalStorageSizeGb` |  `integer` Output only. Total storage size needed for Exascale in GBs.  
`availableStorageSizeGb` |  `integer` Output only. Available storage size for Exascale in GBs.  
  
## Methods  
  
---  
  
### `[configureExascale](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/configureExascale)`

|  Configures Exascale for a single Exadata Infrastructure.  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/create)`

|  Creates a new Exadata Infrastructure in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/delete)`

|  Deletes a single Exadata Infrastructure.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/get)`

|  Gets details of a single Exadata Infrastructure.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/list)`

|  Lists Exadata Infrastructures in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
