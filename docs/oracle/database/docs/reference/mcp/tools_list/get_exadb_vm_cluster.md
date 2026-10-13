---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:57.142865+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_exadb_vm_cluster`

Get details for an Exadb Vm Cluster in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `get_exadb_vm_cluster` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_exadb_vm_cluster",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `ExadbVmCluster.Get`.

### GetExadbVmClusterRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the ExadbVmCluster in the following format: projects/{project}/locations/{location}/exadbVmClusters/{exadb_vm_cluster}.  
  
## Output Schema

ExadbVmCluster represents a cluster of VMs that are used to run Exadata workloads. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/>

### ExadbVmCluster

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([ExadbVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.ExadbVmClusterProperties))
      },
      "gcpOracleZone": string,
      "labels": {
        string: string,
        ...
      },
      "odbNetwork": string,
      "odbSubnet": string,
      "backupOdbSubnet": string,
      "displayName": string,
      "createTime": string,
      "entitlementId": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster}  
`properties` |  `object (`[ExadbVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.ExadbVmClusterProperties)`)` Required. The properties of the ExadbVmCluster.  
`gcpOracleZone` |  `string` Output only. Immutable. The GCP Oracle zone where Oracle ExadbVmCluster is hosted. Example: us-east4-b-r2. During creation, the system will pick the zone assigned to the ExascaleDbStorageVault.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the ExadbVmCluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. Immutable. The name of the OdbNetwork associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Required. Immutable. The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`backupOdbSubnet` |  `string` Required. Immutable. The name of the backup OdbSubnet associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`displayName` |  `string` Required. Immutable. The display name for the ExadbVmCluster. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the ExadbVmCluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the ExadbVmCluster.  
  
### ExadbVmClusterProperties

JSON representation  
---  
      
    
    {
      "clusterName": string,
      "gridImageId": string,
      "nodeCount": integer,
      "enabledEcpuCountPerNode": integer,
      "additionalEcpuCountPerNode": integer,
      "vmFileSystemStorage": {
        object ([ExadbVmClusterStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.ExadbVmClusterStorageDetails))
      },
      "licenseModel": enum (LicenseModel),
      "exascaleDbStorageVault": string,
      "hostnamePrefix": string,
      "hostname": string,
      "sshPublicKeys": [
        string
      ],
      "dataCollectionOptions": {
        object ([DataCollectionOptionsCommon](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.DataCollectionOptionsCommon))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone))
      },
      "lifecycleState": enum (ExadbVmClusterLifecycleState),
      "shapeAttribute": enum (ShapeAttribute),
      "memorySizeGb": integer,
      "scanListenerPortTcp": integer,
      "ociUri": string,
      "giVersion": string
    }  
  
Fields  
---  
`clusterName` |  `string` Optional. Immutable. The cluster name for Exascale vm cluster. The cluster name must begin with an alphabetic character and may contain hyphens(-) but can not contain underscores(_). It should be not more than 11 characters and is not case sensitive. OCI Cluster name.  
`gridImageId` |  `string` Required. Immutable. Grid Infrastructure Version.  
`nodeCount` |  `integer` Required. The number of nodes/VMs in the ExadbVmCluster.  
`enabledEcpuCountPerNode` |  `integer` Required. Immutable. The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure.  
`additionalEcpuCountPerNode` |  `integer` Optional. Immutable. The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure.  
`vmFileSystemStorage` |  `object (`[ExadbVmClusterStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.ExadbVmClusterStorageDetails)`)` Required. Immutable. Total storage details for the ExadbVmCluster.  
`licenseModel` |  `enum (`LicenseModel`)` Optional. Immutable. The license type of the ExadbVmCluster.  
`exascaleDbStorageVault` |  `string` Required. Immutable. The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}  
`hostnamePrefix` |  `string` Required. Immutable. Prefix for VM cluster host names.  
`hostname` |  `string` Output only. The hostname of the ExadbVmCluster.  
`sshPublicKeys[]` |  `string` Required. Immutable. The SSH public keys for the ExadbVmCluster.  
`dataCollectionOptions` |  `object (`[DataCollectionOptionsCommon](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster#Output.Schema.DataCollectionOptionsCommon)`)` Optional. Immutable. Indicates user preference for data collection options.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone)`)` Optional. Immutable. The time zone of the ExadbVmCluster.  
`lifecycleState` |  `enum (`ExadbVmClusterLifecycleState`)` Output only. State of the cluster.  
`shapeAttribute` |  `enum (`ShapeAttribute`)` Required. Immutable. The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later  
`memorySizeGb` |  `integer` Output only. Memory per VM (GB) (Read-only): Shows the amount of memory allocated to each VM. Memory is calculated based on 2.75 GB per Total ECPUs.  
`scanListenerPortTcp` |  `integer` Optional. Immutable. SCAN listener port - TCP  
`ociUri` |  `string` Output only. Deep link to the OCI console to view this resource.  
`giVersion` |  `string` Output only. The Oracle Grid Infrastructure (GI) software version.  
  
### ExadbVmClusterStorageDetails

JSON representation  
---  
      
    
    {
      "sizeInGbsPerNode": integer
    }  
  
Fields  
---  
`sizeInGbsPerNode` |  `integer` Required. The storage allocation for the exadbvmcluster per node, in gigabytes (GB). This field is used to calculate the total storage allocation for the exadbvmcluster.  
  
### DataCollectionOptionsCommon

JSON representation  
---  
      
    
    {
      "isDiagnosticsEventsEnabled": boolean,
      "isHealthMonitoringEnabled": boolean,
      "isIncidentLogsEnabled": boolean
    }  
  
Fields  
---  
`isDiagnosticsEventsEnabled` |  `boolean` Optional. Indicates whether to enable data collection for diagnostics.  
`isHealthMonitoringEnabled` |  `boolean` Optional. Indicates whether to enable health monitoring.  
`isIncidentLogsEnabled` |  `boolean` Optional. Indicates whether to enable incident logs and trace collection.  
  
### TimeZone

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
