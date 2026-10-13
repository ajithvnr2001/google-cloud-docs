---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:55.577261+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_exadata_infrastructure`

Get details for an Exadata Infrastructure in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `get_exadata_infrastructure` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_exadata_infrastructure",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `CloudExadataInfrastructure.Get`.

### GetCloudExadataInfrastructureRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.  
  
## Output Schema

Represents CloudExadataInfrastructure resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudExadataInfrastructure/>

### CloudExadataInfrastructure

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "gcpOracleZone": string,
      "entitlementId": string,
      "properties": {
        object ([CloudExadataInfrastructureProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure#Output.Schema.CloudExadataInfrastructureProperties))
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Exadata Infrastructure resource with the format: projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle Exadata Infrastructure is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`entitlementId` |  `string` Output only. Entitlement ID of the private offer against which this infrastructure resource is provisioned.  
`properties` |  `object (`[CloudExadataInfrastructureProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure#Output.Schema.CloudExadataInfrastructureProperties)`)` Optional. Various properties of the infra.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Exadata Infrastructure was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### CloudExadataInfrastructureProperties

JSON representation  
---  
      
    
    {
      "ocid": string,
      "computeCount": integer,
      "storageCount": integer,
      "totalStorageSizeGb": integer,
      "availableStorageSizeGb": integer,
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure#Output.Schema.MaintenanceWindow))
      },
      "state": enum (State),
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
          object ([CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.CustomerContact))
        }
      ],
      "monthlyStorageServerVersion": string,
      "monthlyDbServerVersion": string,
      "computeModel": enum (ComputeModel),
      "databaseServerType": string,
      "storageServerType": string
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of created infra. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>  
`computeCount` |  `integer` Optional. The number of compute servers for the Exadata Infrastructure.  
`storageCount` |  `integer` Optional. The number of Cloud Exadata storage servers for the Exadata Infrastructure.  
`totalStorageSizeGb` |  `integer` Optional. The total storage allocated to the Exadata Infrastructure resource, in gigabytes (GB).  
`availableStorageSizeGb` |  `integer` Output only. The available storage can be allocated to the Exadata Infrastructure resource, in gigabytes (GB).  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure#Output.Schema.MaintenanceWindow)`)` Optional. Maintenance window for repair.  
`state` |  `enum (`State`)` Output only. The current lifecycle state of the Exadata Infrastructure.  
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
`customerContacts[]` |  `object (`[CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.CustomerContact)`)` Optional. The list of customer contacts.  
`monthlyStorageServerVersion` |  `string` Output only. The monthly software version of the storage servers (cells) in the Exadata Infrastructure. Example: 20.1.15  
`monthlyDbServerVersion` |  `string` Output only. The monthly software version of the database servers (dom0) in the Exadata Infrastructure. Example: 20.1.15  
`computeModel` |  `enum (`ComputeModel`)` Output only. The compute model of the Exadata Infrastructure.  
`databaseServerType` |  `string` Output only. The database server type of the Exadata Infrastructure.  
`storageServerType` |  `string` Output only. The storage server type of the Exadata Infrastructure.  
  
### MaintenanceWindow

JSON representation  
---  
      
    
    {
      "preference": enum (MaintenanceWindowPreference),
      "months": [
        enum (google.type.Month)
      ],
      "weeksOfMonth": [
        integer
      ],
      "daysOfWeek": [
        enum (google.type.DayOfWeek)
      ],
      "hoursOfDay": [
        integer
      ],
      "leadTimeWeek": integer,
      "patchingMode": enum (PatchingMode),
      "customActionTimeoutMins": integer,
      "isCustomActionTimeoutEnabled": boolean
    }  
  
Fields  
---  
`preference` |  `enum (`MaintenanceWindowPreference`)` Optional. The maintenance window scheduling preference.  
`months[]` |  `enum (`google.type.Month`)` Optional. Months during the year when maintenance should be performed.  
`weeksOfMonth[]` |  `integer` Optional. Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week.  
`daysOfWeek[]` |  `enum (`google.type.DayOfWeek`)` Optional. Days during the week when maintenance should be performed.  
`hoursOfDay[]` |  `integer` Optional. The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are: 0 - represents time slot 0:00 - 3:59 UTC 4 - represents time slot 4:00 - 7:59 UTC 8 - represents time slot 8:00 - 11:59 UTC 12 - represents time slot 12:00 - 15:59 UTC 16 - represents time slot 16:00 - 19:59 UTC 20 - represents time slot 20:00 - 23:59 UTC  
`leadTimeWeek` |  `integer` Optional. Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.  
`patchingMode` |  `enum (`PatchingMode`)` Optional. Cloud CloudExadataInfrastructure node patching method, either "ROLLING" or "NONROLLING". Default value is ROLLING.  
`customActionTimeoutMins` |  `integer` Optional. Determines the amount of time the system will wait before the start of each database server patching operation. Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive).  
`isCustomActionTimeoutEnabled` |  `boolean` Optional. If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### CustomerContact

JSON representation  
---  
      
    
    {
      "email": string
    }  
  
Fields  
---  
`email` |  `string` Required. The email address used by Oracle to send notifications regarding databases and infrastructure.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
