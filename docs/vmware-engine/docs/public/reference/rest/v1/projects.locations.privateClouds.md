---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds
title: REST Resource: projects.locations.privateClouds \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:11.099321+00:00
---

# REST Resource: projects.locations.privateClouds  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrivateCloud
    * JSON representation
  * State
  * NetworkConfig
    * JSON representation
  * ManagementCluster
    * JSON representation
  * Hcx
    * JSON representation
  * State
  * Nsx
    * JSON representation
  * State
  * Vcenter
    * JSON representation
  * State
  * Type
  * Methods



## Resource: PrivateCloud

Represents a private cloud resource. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "expireTime": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State)),
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#NetworkConfig))
      },
      "managementCluster": {
        object ([ManagementCluster](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#ManagementCluster))
      },
      "description": string,
      "hcx": {
        object ([Hcx](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Hcx))
      },
      "nsx": {
        object ([Nsx](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Nsx))
      },
      "vcenter": {
        object ([Vcenter](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Vcenter))
      },
      "uid": string,
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Type))
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this private cloud. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the resource was scheduled for deletion.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the resource will be irreversibly deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State)`)` Output only. State of the resource. New values may be added to this enum when appropriate.  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#NetworkConfig)`)` Required. Network configuration of the private cloud.  
`managementCluster` |  `object (`[ManagementCluster](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#ManagementCluster)`)` Required. Input only. The management cluster for this private cloud. This field is required during creation of the private cloud to provide details for the default cluster.The following fields can't be changed after private cloud creation: `ManagementCluster.clusterId`, `ManagementCluster.nodeTypeId`.  
`description` |  `string` User-provided description for this private cloud.  
`hcx` |  `object (`[Hcx](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Hcx)`)` Output only. HCX appliance.  
`nsx` |  `object (`[Nsx](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Nsx)`)` Output only. NSX appliance.  
`vcenter` |  `object (`[Vcenter](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Vcenter)`)` Output only. Vcenter appliance.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#Type)`)` Optional. Type of the private cloud. Defaults to STANDARD.  
  
## State

Enum State defines possible states of private clouds.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | The private cloud is ready.  
`CREATING` | The private cloud is being created.  
`UPDATING` | The private cloud is being updated.  
`FAILED` | The private cloud is in failed state.  
`DELETED` | The private cloud is scheduled for deletion. The deletion process can be cancelled by using the corresponding undelete method.  
`PURGING` | The private cloud is irreversibly deleted and is being removed from the system.  
  
## NetworkConfig

Network configuration in the consumer project with which the peering has to be done.

JSON representation  
---  
      
    
    {
      "managementCidr": string,
      "vmwareEngineNetwork": string,
      "vmwareEngineNetworkCanonical": string,
      "managementIpAddressLayoutVersion": integer,
      "dnsServerIp": string
    }  
  
Fields  
---  
`managementCidr` |  `string` Required. Management CIDR used by VMware management appliances.  
`vmwareEngineNetwork` |  `string` Optional. The relative resource name of the VMware Engine network attached to the private cloud. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}` where `{project}` can either be a project number or a project ID.  
`vmwareEngineNetworkCanonical` |  `string` Output only. The canonical name of the VMware Engine network in the form: `projects/{projectNumber}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}`  
`managementIpAddressLayoutVersion` |  `integer` Output only. The IP address layout version of the management IP address range. Possible versions include: * `managementIpAddressLayoutVersion=1`: Indicates the legacy IP address layout used by some existing private clouds. This is no longer supported for new private clouds as it does not support all features. * `managementIpAddressLayoutVersion=2`: Indicates the latest IP address layout used by all newly created private clouds. This version supports all current features.  
`dnsServerIp` |  `string` Output only. DNS Server IP of the Private Cloud. All DNS queries can be forwarded to this address for name resolution of Private Cloud's management entities like vCenter, NSX-T Manager and ESXi hosts.  
  
## ManagementCluster

Management cluster configuration.

JSON representation  
---  
      
    
    {
      "clusterId": string,
      "nodeTypeConfigs": {
        string: {
          object ([NodeTypeConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/NodeTypeConfig))
        },
        ...
      },
      "stretchedClusterConfig": {
        object ([StretchedClusterConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/StretchedClusterConfig))
      }
    }  
  
Fields  
---  
`clusterId` |  `string` Required. The user-provided identifier of the new `Cluster`. The identifier must meet the following requirements:

  * Only contains 1-63 alphanumeric characters and hyphens
  * Begins with an alphabetical character
  * Ends with a non-hyphen character
  * Not formatted as a UUID
  * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)

  
`nodeTypeConfigs` |  `map (key: string, value: object (`[NodeTypeConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/NodeTypeConfig)`))` Required. The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the `NodeType`).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stretchedClusterConfig` |  `object (`[StretchedClusterConfig](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/StretchedClusterConfig)`)` Optional. Configuration of a stretched cluster. Required for STRETCHED private clouds.  
  
## Hcx

Details about a HCX Cloud Manager appliance.

JSON representation  
---  
      
    
    {
      "internalIp": string,
      "version": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_1)),
      "fqdn": string
    }  
  
Fields  
---  
`internalIp` |  `string` Internal IP address of the appliance.  
`version` |  `string` Version of the appliance.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_1)`)` Output only. The state of the appliance.  
`fqdn` |  `string` Fully qualified domain name of the appliance.  
  
## State

State of the appliance

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified appliance state. This is the default value.  
`ACTIVE` | The appliance is operational and can be used.  
`CREATING` | The appliance is being deployed.  
`ACTIVATING` | The appliance is being activated.  
  
## Nsx

Details about a NSX Manager appliance.

JSON representation  
---  
      
    
    {
      "internalIp": string,
      "version": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_2)),
      "fqdn": string
    }  
  
Fields  
---  
`internalIp` |  `string` Internal IP address of the appliance.  
`version` |  `string` Version of the appliance.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_2)`)` Output only. The state of the appliance.  
`fqdn` |  `string` Fully qualified domain name of the appliance.  
  
## State

State of the appliance

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified appliance state. This is the default value.  
`ACTIVE` | The appliance is operational and can be used.  
`CREATING` | The appliance is being deployed.  
  
## Vcenter

Details about a vCenter Server management appliance.

JSON representation  
---  
      
    
    {
      "internalIp": string,
      "version": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_3)),
      "fqdn": string
    }  
  
Fields  
---  
`internalIp` |  `string` Internal IP address of the appliance.  
`version` |  `string` Version of the appliance.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds#State_3)`)` Output only. The state of the appliance.  
`fqdn` |  `string` Fully qualified domain name of the appliance.  
  
## State

State of the appliance

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified appliance state. This is the default value.  
`ACTIVE` | The appliance is operational and can be used.  
`CREATING` | The appliance is being deployed.  
  
## Type

Enum Type defines private cloud type.

Enums  
---  
`STANDARD` | Standard private is a zonal resource, with 3+ nodes. Default type.  
`TIME_LIMITED` | Time limited private cloud is a zonal resource, can have only 1 node and has limited life span. Will be deleted after defined period of time, can be converted into standard private cloud by expanding it up to 3 or more nodes.  
`STRETCHED` | Stretched private cloud is a regional resource with redundancy, with a minimum of 6 nodes, nodes count has to be even.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/create)`

|  Creates a new `PrivateCloud` resource in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/delete)`

|  Schedules a `PrivateCloud` resource for deletion.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/get)`

|  Retrieves a `PrivateCloud` resource by its resource name.  
  
### `[getDnsForwarding](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/getDnsForwarding)`

|  Gets details of the `DnsForwarding` config.  
  
### `[getIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/list)`

|  Lists `PrivateCloud` resources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/patch)`

|  Modifies a `PrivateCloud` resource.  
  
### `[privateCloudDeletionNow](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/privateCloudDeletionNow)`

|  Accelerates the deletion of a private cloud that is currently in soft deletion A `PrivateCloud` resource in soft deletion has `PrivateCloud.state` set to `SOFT_DELETED` and `PrivateCloud.expireTime` set to the time when deletion can no longer be reversed.  
  
### `[resetNsxCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/resetNsxCredentials)`

|  Resets credentials of the NSX appliance.  
  
### `[resetVcenterCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/resetVcenterCredentials)`

|  Resets credentials of the Vcenter appliance.  
  
### `[setIamPolicy](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[showNsxCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/showNsxCredentials)`

|  Gets details of credentials for NSX appliance.  
  
### `[showVcenterCredentials](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/showVcenterCredentials)`

|  Gets details of credentials for Vcenter appliance.  
  
### `[testIamPermissions](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[undelete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/undelete)`

|  Restores a private cloud that was previously scheduled for deletion by `DeletePrivateCloud`.  
  
### `[updateDnsForwarding](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds/updateDnsForwarding)`

|  Updates the parameters of the `DnsForwarding` config, like associated domains.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
