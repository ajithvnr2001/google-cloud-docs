---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters
title: REST Resource: projects.locations.privateClouds.clusters \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:14.248598+00:00
---

# REST Resource: projects.locations.privateClouds.clusters  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.clusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Cluster
    * JSON representation
  * State
  * AutoscalingSettings
    * JSON representation
  * AutoscalingPolicy
    * JSON representation
  * Thresholds
    * JSON representation
  * DatastoreMountConfig
    * JSON representation
  * DatastoreNetwork
    * JSON representation
  * AccessMode
  * NfsVersion
  * Methods



## Resource: Cluster

A cluster in a private cloud.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#State)),
      "management": boolean,
      "autoscalingSettings": {
        object ([AutoscalingSettings](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AutoscalingSettings))
      },
      "uid": string,
      "nodeTypeConfigs": {
        string: {
          object ([NodeTypeConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/NodeTypeConfig))
        },
        ...
      },
      "stretchedClusterConfig": {
        object ([StretchedClusterConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/StretchedClusterConfig))
      },
      "datastoreMountConfig": [
        {
          object ([DatastoreMountConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#DatastoreMountConfig))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#State)`)` Output only. State of the resource.  
`management` |  `boolean` Output only. True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one.  
`autoscalingSettings` |  `object (`[AutoscalingSettings](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AutoscalingSettings)`)` Optional. Configuration of the autoscaling applied to this cluster.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`nodeTypeConfigs` |  `map (key: string, value: object (`[NodeTypeConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/NodeTypeConfig)`))` Required. The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the `NodeType`).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stretchedClusterConfig` |  `object (`[StretchedClusterConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/StretchedClusterConfig)`)` Optional. Configuration of a stretched cluster. Required for clusters that belong to a STRETCHED private cloud.  
`datastoreMountConfig[]` |  `object (`[DatastoreMountConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#DatastoreMountConfig)`)` Output only. Configuration of a mounted datastore.  
  
## State

Enum State defines possible states of private cloud clusters.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | The Cluster is operational and can be used by the user.  
`CREATING` | The Cluster is being deployed.  
`UPDATING` | Adding or removing of a node to the cluster, any other cluster specific updates.  
`DELETING` | The Cluster is being deleted.  
`REPAIRING` | The Cluster is undergoing maintenance, for example: a failed node is getting replaced.  
  
## AutoscalingSettings

Autoscaling settings define the rules used by VMware Engine to automatically scale-out and scale-in the clusters in a private cloud.

JSON representation  
---  
      
    
    {
      "autoscalingPolicies": {
        string: {
          object ([AutoscalingPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AutoscalingPolicy))
        },
        ...
      },
      "minClusterNodeCount": integer,
      "maxClusterNodeCount": integer,
      "coolDownPeriod": string
    }  
  
Fields  
---  
`autoscalingPolicies` |  `map (key: string, value: object (`[AutoscalingPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AutoscalingPolicy)`))` Required. The map with autoscaling policies applied to the cluster. The key is the identifier of the policy. It must meet the following requirements:

  * Only contains 1-63 alphanumeric characters and hyphens
  * Begins with an alphabetical character
  * Ends with a non-hyphen character
  * Not formatted as a UUID
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)

Currently there map must contain only one element that describes the autoscaling policy for compute nodes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`minClusterNodeCount` |  `integer` Optional. Minimum number of nodes of any type in a cluster. If not specified the default limits apply.  
`maxClusterNodeCount` |  `integer` Optional. Maximum number of nodes of any type in a cluster. If not specified the default limits apply.  
`coolDownPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The minimum duration between consecutive autoscale operations. It starts once addition or removal of nodes is fully completed. Defaults to 30 minutes if not specified. Cool down period must be in whole minutes (for example, 30, 31, 50, 180 minutes).A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## AutoscalingPolicy

Autoscaling policy describes the behavior of the autoscaling with respect to the resource utilization. The scale-out operation is initiated if the utilization exceeds ANY of the respective thresholds. The scale-in operation is initiated if the utilization is below ALL of the respective thresholds.

JSON representation  
---  
      
    
    {
      "nodeTypeId": string,
      "scaleOutSize": integer,
      "cpuThresholds": {
        object ([Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds))
      },
      "grantedMemoryThresholds": {
        object ([Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds))
      },
      "consumedMemoryThresholds": {
        object ([Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds))
      },
      "storageThresholds": {
        object ([Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds))
      }
    }  
  
Fields  
---  
`nodeTypeId` |  `string` Required. The canonical identifier of the node type to add or remove. Corresponds to the `NodeType`.  
`scaleOutSize` |  `integer` Required. Number of nodes to add to a cluster during a scale-out operation. Must be divisible by 2 for stretched clusters. During a scale-in operation only one node (or 2 for stretched clusters) are removed in a single iteration.  
`cpuThresholds` |  `object (`[Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds)`)` Optional. Utilization thresholds pertaining to CPU utilization.  
`grantedMemoryThresholds` |  `object (`[Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds)`)` Optional. Utilization thresholds pertaining to amount of granted memory.  
`consumedMemoryThresholds` |  `object (`[Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds)`)` Optional. Utilization thresholds pertaining to amount of consumed memory.  
`storageThresholds` |  `object (`[Thresholds](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#Thresholds)`)` Optional. Utilization thresholds pertaining to amount of consumed storage.  
  
## Thresholds

Thresholds define the utilization of resources triggering scale-out and scale-in operations.

JSON representation  
---  
      
    
    {
      "scaleOut": integer,
      "scaleIn": integer
    }  
  
Fields  
---  
`scaleOut` |  `integer` Required. The utilization triggering the scale-out operation in percent.  
`scaleIn` |  `integer` Required. The utilization triggering the scale-in operation in percent.  
  
## DatastoreMountConfig

The Datastore Mount configuration

JSON representation  
---  
      
    
    {
      "fileShare": string,
      "datastore": string,
      "datastoreNetwork": {
        object ([DatastoreNetwork](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#DatastoreNetwork))
      },
      "accessMode": enum ([AccessMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AccessMode)),
      "nfsVersion": enum ([NfsVersion](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#NfsVersion)),
      "servers": [
        string
      ]
    }  
  
Fields  
---  
`fileShare` |  `string` Output only. File share name.  
`datastore` |  `string` Required. The resource name of the datastore to mount. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/datastores/my-datastore`  
`datastoreNetwork` |  `object (`[DatastoreNetwork](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#DatastoreNetwork)`)` Required. The network configuration for the datastore.  
`accessMode` |  `enum (`[AccessMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#AccessMode)`)` Optional. The access mode of the NFS volume. Optional. Default value used will be READ_WRITE  
`nfsVersion` |  `enum (`[NfsVersion](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters#NfsVersion)`)` Optional. The NFS protocol supported by the NFS volume. Default value used will be NFS_V3  
`servers[]` |  `string` Output only. Server IP addresses of the NFS volume. For NFS 3, you can only provide a single server IP address or DNS names.  
  
## DatastoreNetwork

The network configuration for the datastore.

JSON representation  
---  
      
    
    {
      "subnet": string,
      "mtu": integer,
      "networkPeering": string,
      "connectionCount": integer
    }  
  
Fields  
---  
`subnet` |  `string` Required. The resource name of the subnet Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. e.g. projects/my-project/locations/us-central1/subnets/my-subnet  
`mtu` |  `integer` Optional. MTU value is set on the VMKernel adapter for the NFS traffic. If not provided, MTU of 1500 is used. To use jumbo frames, set this value to 8896. We recommend to tune this value based on the NFS traffic performance. Performance can be determined using benchmarking I/O tools like fio (Flexible I/O Tester) utility.  
`networkPeering` |  `string` Output only. The resource name of the network peering, used to access the file share by clients on private cloud. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. e.g. projects/my-project/locations/us-central1/networkPeerings/my-network-peering  
`connectionCount` |  `integer` Optional. connectionCount is used to set multiple connections from NFS client on ESXi host to NFS server. A higher number of connections results in better performance on datastores. In clusters.mountDatastore API by default max 4 connections are configured. User can set value of connectionCount between 1 to 4. Connection_count is supported from vsphere 8.0u1 for earlier version 1 connection count is set on the ESXi hosts.  
  
## AccessMode

The access mode of the NFS volume.

Enums  
---  
`ACCESS_MODE_UNSPECIFIED` | The default value. This value should never be used.  
`READ_ONLY` | NFS is accessed by hosts in read mode  
`READ_WRITE` | NFS is accessed by hosts in read and write mode  
  
## NfsVersion

The NFS protocol supported by the NFS volume.

Enums  
---  
`NFS_VERSION_UNSPECIFIED` | The default value. This value should never be used.  
`NFS_V3` | NFS 3  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/create)`

|  Creates a new cluster in a given private cloud.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/delete)`

|  Deletes a `Cluster` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/get)`

|  Retrieves a `Cluster` resource by its resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/list)`

|  Lists `Cluster` resources in a given private cloud.  
  
### `[mountDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/mountDatastore)`

|  Mounts a `Datastore` on a cluster resource  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/patch)`

|  Modifies a `Cluster` resource.  
  
### `[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[unmountDatastore](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.clusters/unmountDatastore)`

|  Unmounts a `Datastore` on a cluster resource  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
