---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_cloud_vm_clusters/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:56.308909+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_cloud_vm_clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_cloud_vm_clusters`

List Cloud Vm Clusters in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `list_cloud_vm_clusters` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_cloud_vm_clusters",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `CloudVmCluster.List`.

### ListCloudVmClustersRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The name of the parent in the following format: projects/{project}/locations/{location}.  
`pageSize` |  `integer` Optional. The number of VM clusters to return. If unspecified, at most 50 VM clusters will be returned. The maximum value is 1,000.  
`pageToken` |  `string` Optional. A token identifying the page of results the server returns.  
`filter` |  `string` Optional. An expression for filtering the results of the request.  
  
## Output Schema

The response for `CloudVmCluster.List`.

### ListCloudVmClustersResponse

JSON representation  
---  
      
    
    {
      "cloudVmClusters": [
        {
          object ([CloudVmCluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.CloudVmCluster))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`cloudVmClusters[]` |  `object (`[CloudVmCluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.CloudVmCluster)`)` The list of VM Clusters.  
`nextPageToken` |  `string` A token to fetch the next page of results.  
  
### CloudVmCluster

JSON representation  
---  
      
    
    {
      "name": string,
      "exadataInfrastructure": string,
      "displayName": string,
      "properties": {
        object ([CloudVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.CloudVmClusterProperties))
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
        object ([IdentityConnector](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.IdentityConnector))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the VM Cluster resource with the format: projects/{project}/locations/{region}/cloudVmClusters/{cloud_vm_cluster}  
`exadataInfrastructure` |  `string` Required. The name of the Exadata Infrastructure resource on which VM cluster resource is created, in the following format: projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`properties` |  `object (`[CloudVmClusterProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.CloudVmClusterProperties)`)` Optional. Various properties of the VM Cluster.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the VM Cluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the VM cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cidr` |  `string` Optional. Network settings. CIDR to use for cluster IP allocation.  
`backupSubnetCidr` |  `string` Optional. CIDR range of the backup subnet.  
`network` |  `string` Optional. The name of the VPC network. Format: projects/{project}/global/networks/{network}  
`gcpOracleZone` |  `string` Output only. The GCP Oracle zone where Oracle CloudVmCluster is hosted. This will be the same as the gcp_oracle_zone of the CloudExadataInfrastructure. Example: us-east4-b-r2.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the odb_subnet and backup_odb_subnet.  
`odbSubnet` |  `string` Optional. The name of the OdbSubnet associated with the VM Cluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`backupOdbSubnet` |  `string` Optional. The name of the backup OdbSubnet associated with the VM Cluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`identityConnector` |  `object (`[IdentityConnector](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.IdentityConnector)`)` Output only. The identity connector details which will allow OCI to securely access the resources in the customer project.  
  
### CloudVmClusterProperties

JSON representation  
---  
      
    
    {
      "ocid": string,
      "licenseType": enum (LicenseType),
      "giVersion": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone))
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
      "diskRedundancy": enum (DiskRedundancy),
      "sparseDiskgroupEnabled": boolean,
      "localBackupEnabled": boolean,
      "hostnamePrefix": string,
      "diagnosticsDataCollectionOptions": {
        object ([DataCollectionOptions](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.DataCollectionOptions))
      },
      "state": enum (State),
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
      "computeModel": enum (ComputeModel)
    }  
  
Fields  
---  
`ocid` |  `string` Output only. Oracle Cloud Infrastructure ID of VM Cluster.  
`licenseType` |  `enum (`LicenseType`)` Required. License type of VM Cluster.  
`giVersion` |  `string` Optional. Grid Infrastructure Version.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone)`)` Optional. Time zone of VM Cluster to set. Defaults to UTC if not specified.  
`sshPublicKeys[]` |  `string` Optional. SSH public keys to be stored with cluster.  
`nodeCount` |  `integer` Optional. Number of database servers.  
`shape` |  `string` Output only. Shape of VM Cluster.  
`ocpuCount` |  `number` Optional. OCPU count per VM. Minimum is 0.1.  
`memorySizeGb` |  `integer` Optional. Memory allocated in GBs.  
`dbNodeStorageSizeGb` |  `integer` Optional. Local storage per VM.  
`storageSizeGb` |  `integer` Output only. The storage allocation for the disk group, in gigabytes (GB).  
`dataStorageSizeTb` |  `number` Optional. The data disk group size to be allocated in TBs.  
`diskRedundancy` |  `enum (`DiskRedundancy`)` Optional. The type of redundancy.  
`sparseDiskgroupEnabled` |  `boolean` Optional. Use exadata sparse snapshots.  
`localBackupEnabled` |  `boolean` Optional. Use local backup.  
`hostnamePrefix` |  `string` Optional. Prefix for VM cluster host names.  
`diagnosticsDataCollectionOptions` |  `object (`[DataCollectionOptions](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster#Output.Schema.DataCollectionOptions)`)` Optional. Data collection options for diagnostics.  
`state` |  `enum (`State`)` Output only. State of the cluster.  
`scanListenerPortTcp` |  `integer` Output only. SCAN listener port - TCP  
`scanListenerPortTcpSsl` |  `integer` Output only. SCAN listener port - TLS  
`domain` |  `string` Output only. Parent DNS domain where SCAN DNS and hosts names are qualified. ex: ocispdelegated.ocisp10jvnet.oraclevcn.com  
`scanDns` |  `string` Output only. SCAN DNS name. ex: sp2-yi0xq-scan.ocispdelegated.ocisp10jvnet.oraclevcn.com  
`hostname` |  `string` Output only. host name without domain. format: "-" with some suffix. ex: sp2-yi0xq where "sp2" is the hostname_prefix.  
`cpuCoreCount` |  `integer` Required. Number of enabled CPU cores.  
`systemVersion` |  `string` Optional. Operating system version of the image.  
`scanIpIds[]` |  `string` Output only. OCIDs of scan IPs.  
`scanDnsRecordId` |  `string` Output only. OCID of scan DNS record.  
`ociUrl` |  `string` Output only. Deep link to the OCI console to view this resource.  
`dbServerOcids[]` |  `string` Optional. OCID of database servers.  
`compartmentId` |  `string` Output only. Compartment ID of cluster.  
`dnsListenerIp` |  `string` Output only. DNS listener IP.  
`clusterName` |  `string` Optional. OCI Cluster name.  
`computeModel` |  `enum (`ComputeModel`)` Output only. The compute model of the VM Cluster.  
  
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
  
### DataCollectionOptions

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
  
### IdentityConnector

JSON representation  
---  
      
    
    {
      "serviceAgentEmail": string,
      "connectionState": enum (ConnectionState)
    }  
  
Fields  
---  
`serviceAgentEmail` |  `string` Output only. A google managed service account on which customers can grant roles to access resources in the customer project. Example: `p176944527254-55-75119d87fd8f@gcp-sa-oci.iam.gserviceaccount.com`  
`connectionState` |  `enum (`ConnectionState`)` Output only. The connection state of the identity connector.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
