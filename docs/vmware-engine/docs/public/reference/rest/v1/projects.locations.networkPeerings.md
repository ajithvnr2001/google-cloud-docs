---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings
title: REST Resource: projects.locations.networkPeerings \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:06.939157+00:00
---

# REST Resource: projects.locations.networkPeerings  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.networkPeerings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NetworkPeering
    * JSON representation
  * State
  * PeerNetworkType
  * Methods



## Resource: NetworkPeering

Details of a network peering.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "peerNetwork": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings#State)),
      "stateDetails": string,
      "peerMtu": integer,
      "peerNetworkType": enum ([PeerNetworkType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings#PeerNetworkType)),
      "uid": string,
      "vmwareEngineNetwork": string,
      "description": string,
      "exportCustomRoutes": boolean,
      "importCustomRoutes": boolean,
      "exchangeSubnetRoutes": boolean,
      "exportCustomRoutesWithPublicIp": boolean,
      "importCustomRoutesWithPublicIp": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the network peering. NetworkPeering is a global resource and location can only be global. Resource names are scheme-less URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/networkPeerings/my-peering`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`peerNetwork` |  `string` Required. The relative resource name of the network to peer with a standard VMware Engine network. The provided network can be a consumer VPC network or another standard VMware Engine network. If the `peerNetworkType` is VMWARE_ENGINE_NETWORK, specify the name in the form: `projects/{project}/locations/global/vmwareEngineNetworks/{vmwareEngineNetworkId}`. Otherwise specify the name in the form: `projects/{project}/global/networks/{network_id}`, where `{project}` can either be a project number or a project ID.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings#State)`)` Output only. State of the network peering. This field has a value of 'ACTIVE' when there's a matching configuration in the peer network. New values may be added to this enum when appropriate.  
`stateDetails` |  `string` Output only. Output Only. Details about the current state of the network peering.  
`peerMtu` |  `integer` Optional. Maximum transmission unit (MTU) in bytes. The default value is `1500`. If a value of `0` is provided for this field, VMware Engine uses the default value instead.  
`peerNetworkType` |  `enum (`[PeerNetworkType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings#PeerNetworkType)`)` Required. The type of the network to peer with the VMware Engine network.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`vmwareEngineNetwork` |  `string` Required. The relative resource name of the VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}` where `{project}` can either be a project number or a project ID.  
`description` |  `string` Optional. User-provided description for this network peering.  
`exportCustomRoutes` |  `boolean` Optional. True if custom routes are exported to the peered network; false otherwise. The default value is true.  
`importCustomRoutes` |  `boolean` Optional. True if custom routes are imported from the peered network; false otherwise. The default value is true.  
`exchangeSubnetRoutes` |  `boolean` Optional. True if full mesh connectivity is created and managed automatically between peered networks; false otherwise. Currently this field is always true because Google Compute Engine automatically creates and manages subnetwork routes between two VPC networks when peering state is 'ACTIVE'.  
`exportCustomRoutesWithPublicIp` |  `boolean` Optional. True if all subnet routes with a public IP address range are exported; false otherwise. The default value is true. IPv4 special-use ranges (<https://en.wikipedia.org/wiki/IPv4#Special_addresses>) are always exported to peers and are not controlled by this field.  
`importCustomRoutesWithPublicIp` |  `boolean` Optional. True if all subnet routes with public IP address range are imported; false otherwise. The default value is true. IPv4 special-use ranges (<https://en.wikipedia.org/wiki/IPv4#Special_addresses>) are always imported to peers and are not controlled by this field.  
  
## State

Possible states of a network peering.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified network peering state. This is the default value.  
`INACTIVE` | The peering is not active.  
`ACTIVE` | The peering is active.  
`CREATING` | The peering is being created.  
`DELETING` | The peering is being deleted.  
  
## PeerNetworkType

Type or purpose of the network peering connection.

Enums  
---  
`PEER_NETWORK_TYPE_UNSPECIFIED` | Unspecified  
`STANDARD` | Peering connection used for connecting to another VPC network established by the same user. For example, a peering connection to another VPC network in the same project or to an on-premises network.  
`VMWARE_ENGINE_NETWORK` | Peering connection used for connecting to another VMware Engine network.  
`PRIVATE_SERVICES_ACCESS` | Peering connection used for establishing [private services access](https://cloud.google.com/vpc/docs/private-services-access).  
`NETAPP_CLOUD_VOLUMES` | Peering connection used for connecting to NetApp Cloud Volumes.  
`THIRD_PARTY_SERVICE` | Peering connection used for connecting to third-party services. Most third-party services require manual setup of reverse peering on the VPC network associated with the third-party service.  
`DELL_POWERSCALE` | Peering connection used for connecting to Dell PowerScale Filers  
`GOOGLE_CLOUD_NETAPP_VOLUMES` | Peering connection used for connecting to Google Cloud NetApp Volumes.  
`GOOGLE_CLOUD_FILESTORE_INSTANCES` | Peering connection used for connecting to Google Cloud Filestore Instances.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/create)`

|  Creates a new network peering between the peer network and VMware Engine network provided in a `NetworkPeering` resource.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/delete)`

|  Deletes a `NetworkPeering` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/get)`

|  Retrieves a `NetworkPeering` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/list)`

|  Lists `NetworkPeering` resources in a given project.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.networkPeerings/patch)`

|  Modifies a `NetworkPeering` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
