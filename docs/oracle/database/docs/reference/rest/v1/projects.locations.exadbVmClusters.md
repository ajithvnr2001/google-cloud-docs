---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters
title: REST Resource: projects.locations.exadbVmClusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:46.503885+00:00
---

# REST Resource: projects.locations.exadbVmClusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.exadbVmClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExadbVmCluster
    * JSON representation
  * ExadbVmClusterProperties
    * JSON representation
  * ExadbVmClusterStorageDetails
    * JSON representation
  * LicenseModel
  * DataCollectionOptionsCommon
    * JSON representation
  * ExadbVmClusterLifecycleState
  * ShapeAttribute
  * Methods



## Resource: ExadbVmCluster

ExadbVmCluster represents a cluster of VMs that are used to run Exadata workloads. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/>

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([ExadbVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterProperties))
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
`name` |  `string` Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadbVmCluster}  
`properties` |  `object (`[ExadbVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterProperties)`)` Required. The properties of the ExadbVmCluster.  
`gcpOracleZone` |  `string` Output only. Immutable. The GCP Oracle zone where Oracle ExadbVmCluster is hosted. Example: us-east4-b-r2. During creation, the system will pick the zone assigned to the ExascaleDbStorageVault.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the ExadbVmCluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. Immutable. The name of the OdbNetwork associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Required. Immutable. The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`backupOdbSubnet` |  `string` Required. Immutable. The name of the backup OdbSubnet associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`displayName` |  `string` Required. Immutable. The display name for the ExadbVmCluster. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the ExadbVmCluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the ExadbVmCluster.  
  
## ExadbVmClusterProperties

The properties of an ExadbVmCluster.

JSON representation  
---  
      
    
    {
      "clusterName": string,
      "gridImageId": string,
      "nodeCount": integer,
      "enabledEcpuCountPerNode": integer,
      "additionalEcpuCountPerNode": integer,
      "vmFileSystemStorage": {
        object ([ExadbVmClusterStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterStorageDetails))
      },
      "licenseModel": enum ([LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#LicenseModel)),
      "exascaleDbStorageVault": string,
      "hostnamePrefix": string,
      "hostname": string,
      "sshPublicKeys": [
        string
      ],
      "dataCollectionOptions": {
        object ([DataCollectionOptionsCommon](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#DataCollectionOptionsCommon))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone))
      },
      "lifecycleState": enum ([ExadbVmClusterLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterLifecycleState)),
      "shapeAttribute": enum ([ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ShapeAttribute)),
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
`vmFileSystemStorage` |  `object (`[ExadbVmClusterStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterStorageDetails)`)` Required. Immutable. Total storage details for the ExadbVmCluster.  
`licenseModel` |  `enum (`[LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#LicenseModel)`)` Optional. Immutable. The license type of the ExadbVmCluster.  
`exascaleDbStorageVault` |  `string` Required. Immutable. The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascaleDbStorageVault}  
`hostnamePrefix` |  `string` Required. Immutable. Prefix for VM cluster host names.  
`hostname` |  `string` Output only. The hostname of the ExadbVmCluster.  
`sshPublicKeys[]` |  `string` Required. Immutable. The SSH public keys for the ExadbVmCluster.  
`dataCollectionOptions` |  `object (`[DataCollectionOptionsCommon](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#DataCollectionOptionsCommon)`)` Optional. Immutable. Indicates user preference for data collection options.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone)`)` Optional. Immutable. The time zone of the ExadbVmCluster.  
`lifecycleState` |  `enum (`[ExadbVmClusterLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ExadbVmClusterLifecycleState)`)` Output only. State of the cluster.  
`shapeAttribute` |  `enum (`[ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters#ShapeAttribute)`)` Required. Immutable. The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later  
`memorySizeGb` |  `integer` Output only. Memory per VM (GB) (Read-only): Shows the amount of memory allocated to each VM. Memory is calculated based on 2.75 GB per Total ECPUs.  
`scanListenerPortTcp` |  `integer` Optional. Immutable. SCAN listener port - TCP  
`ociUri` |  `string` Output only. Deep link to the OCI console to view this resource.  
`giVersion` |  `string` Output only. The Oracle Grid Infrastructure (GI) software version.  
  
## ExadbVmClusterStorageDetails

The storage allocation for the exadbvmcluster, in gigabytes (GB).

JSON representation  
---  
      
    
    {
      "sizeInGbsPerNode": integer
    }  
  
Fields  
---  
`sizeInGbsPerNode` |  `integer` Required. The storage allocation for the exadbvmcluster per node, in gigabytes (GB). This field is used to calculate the total storage allocation for the exadbvmcluster.  
  
## LicenseModel

The Oracle license model that applies to the ExaScale VM cluster

Enums  
---  
`LICENSE_MODEL_UNSPECIFIED` | Unspecified.  
`LICENSE_INCLUDED` | Default is license included.  
`BRING_YOUR_OWN_LICENSE` | Bring your own license.  
  
## DataCollectionOptionsCommon

Data collection options for diagnostics. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/DataCollectionOptions>

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
  
## ExadbVmClusterLifecycleState

The various lifecycle states of the VM cluster.

Enums  
---  
`EXADB_VM_CLUSTER_LIFECYCLE_STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UPDATING` | Indicates that the resource is in updating state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`TERMINATED` | Indicates that the resource is in terminated state.  
`FAILED` | Indicates that the resource is in failed state.  
`MAINTENANCE_IN_PROGRESS` | Indicates that the resource is in maintenance in progress state.  
  
## ShapeAttribute

The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later

Enums  
---  
`SHAPE_ATTRIBUTE_UNSPECIFIED` | Default unspecified value.  
`SMART_STORAGE` | Indicates that the resource is in smart storage.  
`BLOCK_STORAGE` | Indicates that the resource is in block storage.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/create)`

|  Creates a new Exadb (Exascale) VM Cluster resource.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/delete)`

|  Deletes a single Exadb (Exascale) VM Cluster.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/get)`

|  Gets details of a single Exadb (Exascale) VM Cluster.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/list)`

|  Lists all the Exadb (Exascale) VM Clusters for the given project and location.  
  
### `[patch](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/patch)`

|  Updates a single Exadb (Exascale) VM Cluster.  
  
### `[removeVirtualMachine](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/removeVirtualMachine)`

|  Removes virtual machines from an existing exadb vm cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
