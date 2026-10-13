---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters
title: REST Resource: projects.locations.cloudVmClusters \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:42.119758+00:00
---

# REST Resource: projects.locations.cloudVmClusters  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.cloudVmClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CloudVmCluster
    * JSON representation
  * CloudVmClusterProperties
    * JSON representation
  * LicenseType
  * DiskRedundancy
  * DataCollectionOptions
    * JSON representation
  * State
  * StorageManagementType
  * IdentityConnector
    * JSON representation
  * ConnectionState
  * Methods



## Resource: CloudVmCluster

Details of the Cloud VM Cluster resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudVmCluster/>

JSON representation  
---  
      
    
    {
      "name": string,
      "exadataInfrastructure": string,
      "displayName": string,
      "properties": {
        object ([CloudVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#CloudVmClusterProperties))
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "cidr": string,
      "backupSubnetCidr": string,
      "network": string,
      "gcpOracleZone": string,
      "odbNetwork": string,
      "odbSubnet": string,
      "backupOdbSubnet": string,
      "identityConnector": {
        object ([IdentityConnector](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#IdentityConnector))
      },
      "exascaleDbStorageVault": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the VM Cluster resource with the format: projects/{project}/locations/{region}/cloudVmClusters/{cloudVmCluster}  
`exadataInfrastructure` |  `string` Required. The name of the Exadata Infrastructure resource on which VM cluster resource is created, in the following format: projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`properties` |  `object (`[CloudVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#CloudVmClusterProperties)`)` Optional. Various properties of the VM Cluster.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the VM Cluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the VM cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cidr` |  `string` Optional. Network settings. CIDR to use for cluster IP allocation.  
`backupSubnetCidr` |  `string` Optional. CIDR range of the backup subnet.  
`network` |  `string` Optional. The name of the VPC network. Format: projects/{project}/global/networks/{network}  
`gcpOracleZone` |  `string` Output only. The GCP Oracle zone where Oracle CloudVmCluster is hosted. This will be the same as the gcpOracleZone of the CloudExadataInfrastructure. Example: us-east4-b-r2.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork} It is optional but if specified, this should match the parent ODBNetwork of the odbSubnet and backupOdbSubnet.  
`odbSubnet` |  `string` Optional. The name of the OdbSubnet associated with the VM Cluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`backupOdbSubnet` |  `string` Optional. The name of the backup OdbSubnet associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`identityConnector` |  `object (`[IdentityConnector](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#IdentityConnector)`)` Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.  
`exascaleDbStorageVault` |  `string` Optional. The name of ExascaleDbStorageVault associated with the VM Cluster. Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascaleDbStorageVault}  
  
## CloudVmClusterProperties

Various properties and settings associated with Exadata VM cluster.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#LicenseType)),
      "giVersion": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone))
      },
      "sshPublicKeys": [
        string
      ],
      "nodeCount": integer,
      "shape": string,
      "ocpuCount": number,
      "memorySizeGb": integer,
      "dbNodeStorageSizeGb": integer,
      "storageSizeGb": integer,
      "dataStorageSizeTb": number,
      "diskRedundancy": enum ([DiskRedundancy](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#DiskRedundancy)),
      "sparseDiskgroupEnabled": boolean,
      "localBackupEnabled": boolean,
      "hostnamePrefix": string,
      "diagnosticsDataCollectionOptions": {
        object ([DataCollectionOptions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#DataCollectionOptions))
      },
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#State)),
      "scanListenerPortTcp": integer,
      "scanListenerPortTcpSsl": integer,
      "domain": string,
      "scanDns": string,
      "hostname": string,
      "cpuCoreCount": integer,
      "systemVersion": string,
      "scanIpIds": [
        string
      ],
      "scanDnsRecordId": string,
      "ociUrl": string,
      "dbServerOcids": [
        string
      ],
      "compartmentId": string,
      "dnsListenerIp": string,
      "clusterName": string,
      "computeModel": enum ([ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/ComputeModel)),
      "storageManagementType": enum ([StorageManagementType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#StorageManagementType))
    }  
  
Fields  
---  
`ocid` |  `string` Output only. Oracle Cloud Infrastructure ID of VM Cluster.  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#LicenseType)`)` Required. License type of VM Cluster.  
`giVersion` |  `string` Optional. Grid Infrastructure Version.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone)`)` Optional. Time zone of VM Cluster to set. Defaults to UTC if not specified.  
`sshPublicKeys[]` |  `string` Optional. SSH public keys to be stored with cluster.  
`nodeCount` |  `integer` Optional. Number of database servers.  
`shape` |  `string` Output only. Shape of VM Cluster.  
`ocpuCount` |  `number` Optional. OCPU count per VM. Minimum is 0.1.  
`memorySizeGb` |  `integer` Optional. Memory allocated in GBs.  
`dbNodeStorageSizeGb` |  `integer` Optional. Local storage per VM.  
`storageSizeGb` |  `integer` Output only. The storage allocation for the disk group, in gigabytes (GB).  
`dataStorageSizeTb` |  `number` Optional. The data disk group size to be allocated in TBs.  
`diskRedundancy` |  `enum (`[DiskRedundancy](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#DiskRedundancy)`)` Optional. The type of redundancy.  
`sparseDiskgroupEnabled` |  `boolean` Optional. Use exadata sparse snapshots.  
`localBackupEnabled` |  `boolean` Optional. Use local backup.  
`hostnamePrefix` |  `string` Optional. Prefix for VM cluster host names.  
`diagnosticsDataCollectionOptions` |  `object (`[DataCollectionOptions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#DataCollectionOptions)`)` Optional. Data collection options for diagnostics.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#State)`)` Output only. State of the cluster.  
`scanListenerPortTcp` |  `integer` Optional. SCAN listener port - TCP  
`scanListenerPortTcpSsl` |  `integer` Optional. SCAN listener port - TLS  
`domain` |  `string` Output only. Parent DNS domain where SCAN DNS and hosts names are qualified. ex: ocispdelegated.ocisp10jvnet.oraclevcn.com  
`scanDns` |  `string` Output only. SCAN DNS name. ex: sp2-yi0xq-scan.ocispdelegated.ocisp10jvnet.oraclevcn.com  
`hostname` |  `string` Output only. host name without domain. format: "-" with some suffix. ex: sp2-yi0xq where "sp2" is the hostnamePrefix.  
`cpuCoreCount` |  `integer` Required. Number of enabled CPU cores.  
`systemVersion` |  `string` Optional. Operating system version of the image.  
`scanIpIds[]` |  `string` Output only. OCIDs of scan IPs.  
`scanDnsRecordId` |  `string` Output only. OCID of scan DNS record.  
`ociUrl` |  `string` Output only. Deep link to the OCI console to view this resource.  
`dbServerOcids[]` |  `string` Optional. OCID of database servers.  
`compartmentId` |  `string` Output only. Compartment ID of cluster.  
`dnsListenerIp` |  `string` Output only. DNS listener IP.  
`clusterName` |  `string` Optional. OCI Cluster name.  
`computeModel` |  `enum (`[ComputeModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/ComputeModel)`)` Output only. The compute model of the VM Cluster.  
`storageManagementType` |  `enum (`[StorageManagementType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#StorageManagementType)`)` Output only. The storage management type of the VM Cluster.  
  
## LicenseType

Different licenses supported.

Enums  
---  
`LICENSE_TYPE_UNSPECIFIED` | Unspecified  
`LICENSE_INCLUDED` | License included part of offer  
`BRING_YOUR_OWN_LICENSE` | Bring your own license  
  
## DiskRedundancy

Types of disk redundancy provided by Oracle.

Enums  
---  
`DISK_REDUNDANCY_UNSPECIFIED` | Unspecified.  
`HIGH` | High - 3 way mirror.  
`NORMAL` | Normal - 2 way mirror.  
  
## DataCollectionOptions

Data collection options for diagnostics.

JSON representation  
---  
      
    
    {
      "diagnosticsEventsEnabled": boolean,
      "healthMonitoringEnabled": boolean,
      "incidentLogsEnabled": boolean
    }  
  
Fields  
---  
`diagnosticsEventsEnabled` |  `boolean` Optional. Indicates whether diagnostic collection is enabled for the VM cluster  
`healthMonitoringEnabled` |  `boolean` Optional. Indicates whether health monitoring is enabled for the VM cluster  
`incidentLogsEnabled` |  `boolean` Optional. Indicates whether incident logs and trace collection are enabled for the VM cluster  
  
## State

The various lifecycle states of the VM cluster.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UPDATING` | Indicates that the resource is in updating state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`TERMINATED` | Indicates that the resource is in terminated state.  
`FAILED` | Indicates that the resource is in failed state.  
`MAINTENANCE_IN_PROGRESS` | Indicates that the resource is in maintenance in progress state.  
  
## StorageManagementType

The type of storage management for the Cloud VM Cluster.

Enums  
---  
`STORAGE_MANAGEMENT_TYPE_UNSPECIFIED` | Unspecified storage management type.  
`ASM` | Automatic Storage Management.  
`EXASCALE` | Exascale storage management.  
  
## IdentityConnector

The identity connector details which will allow OCI to securely access the resources in the customer project.

JSON representation  
---  
      
    
    {
      "serviceAgentEmail": string,
      "connectionState": enum ([ConnectionState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#ConnectionState))
    }  
  
Fields  
---  
`serviceAgentEmail` |  `string` Output only. A google managed service account on which customers can grant roles to access resources in the customer project. Example: `p176944527254-55-75119d87fd8f@gcp-sa-oci.iam.gserviceaccount.com`  
`connectionState` |  `enum (`[ConnectionState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters#ConnectionState)`)` Output only. The connection state of the identity connector.  
  
## ConnectionState

The various connection states of the WorkloadIdentityPoolConnection.

Enums  
---  
`CONNECTION_STATE_UNSPECIFIED` | Default unspecified value.  
`CONNECTED` | The identity pool connection is connected.  
`PARTIALLY_CONNECTED` | The identity pool connection is partially connected.  
`DISCONNECTED` | The identity pool connection is disconnected.  
`UNKNOWN` | The identity pool connection is in an unknown state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/create)`

|  Creates a new VM Cluster in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/delete)`

|  Deletes a single VM Cluster.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/get)`

|  Gets details of a single VM Cluster.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/list)`

|  Lists the VM Clusters in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
