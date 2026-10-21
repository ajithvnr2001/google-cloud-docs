---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections
title: REST Resource: projects.locations.privateConnections \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:43:34.438100+00:00
---

# REST Resource: projects.locations.privateConnections  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateConnections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrivateConnection
    * JSON representation
  * State
  * Type
  * RoutingMode
  * PeeringState
  * Methods



## Resource: PrivateConnection

Private connection resource that provides connectivity for VMware Engine private clouds.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#State)),
      "vmwareEngineNetwork": string,
      "vmwareEngineNetworkCanonical": string,
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#Type)),
      "peeringId": string,
      "routingMode": enum ([RoutingMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#RoutingMode)),
      "uid": string,
      "serviceNetwork": string,
      "peeringState": enum ([PeeringState](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#PeeringState))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the private connection. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1/privateConnections/my-connection`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. User-provided description for this private connection.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#State)`)` Output only. State of the private connection.  
`vmwareEngineNetwork` |  `string` Required. The relative resource name of Legacy VMware Engine network. Specify the name in the following form: `projects/{project}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}` where `{project}`, `{location}` will be same as specified in private connection resource name and `{vmwareEngineNetworkId}` will be in the form of `{location}`-default e.g. projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default.  
`vmwareEngineNetworkCanonical` |  `string` Output only. The canonical name of the VMware Engine network in the form: `projects/{projectNumber}/locations/{location}/vmwareEngineNetworks/{vmwareEngineNetworkId}`  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#Type)`)` Required. Private connection type.  
`peeringId` |  `string` Output only. VPC network peering id between given network VPC and VMwareEngineNetwork.  
`routingMode` |  `enum (`[RoutingMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#RoutingMode)`)` Optional. Routing Mode. Default value is set to GLOBAL. For type = PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for other types only GLOBAL is supported.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`serviceNetwork` |  `string` Required. Service network to create private connection. Specify the name in the following form: `projects/{project}/global/networks/{network_id}` For type = PRIVATE_SERVICE_ACCESS, this field represents servicenetworking VPC, e.g. projects/project-tp/global/networks/servicenetworking. For type = NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC, e.g. projects/project-tp/global/networks/netapp-tenant-vpc. For type = DELL_POWERSCALE, this field represent Dell service VPC, e.g. projects/project-tp/global/networks/dell-tenant-vpc. For type= THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any other producer VPC to which the VMware Engine Network needs to be connected, e.g. projects/project/global/networks/vpc.  
`peeringState` |  `enum (`[PeeringState](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections#PeeringState)`)` Output only. Peering state between service network and VMware Engine network.  
  
## State

Enum State defines possible states of private connection.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`CREATING` | The private connection is being created.  
`ACTIVE` | The private connection is ready.  
`UPDATING` | The private connection is being updated.  
`DELETING` | The private connection is being deleted.  
`UNPROVISIONED` | The private connection is not provisioned, since no private cloud is present for which this private connection is needed.  
`FAILED` | The private connection is in failed state.  
  
## Type

Enum Type defines possible types of private connection.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`PRIVATE_SERVICE_ACCESS` | Connection used for establishing [private services access](https://cloud.google.com/vpc/docs/private-services-access).  
`NETAPP_CLOUD_VOLUMES` | Connection used for connecting to NetApp Cloud Volumes.  
`DELL_POWERSCALE` | Connection used for connecting to Dell PowerScale.  
`THIRD_PARTY_SERVICE` | Connection used for connecting to third-party services.  
  
## RoutingMode

Possible types for RoutingMode

Enums  
---  
`ROUTING_MODE_UNSPECIFIED` | The default value. This value should never be used.  
`GLOBAL` | Global Routing Mode  
`REGIONAL` | Regional Routing Mode  
  
## PeeringState

Enum PeeringState defines the possible states of peering between service network and the vpc network peered to service network

Enums  
---  
`PEERING_STATE_UNSPECIFIED` | The default value. This value is used if the peering state is omitted or unknown.  
`PEERING_ACTIVE` | The peering is in active state.  
`PEERING_INACTIVE` | The peering is in inactive state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/create)`

|  Creates a new private connection that can be used for accessing private Clouds.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/delete)`

|  Deletes a `PrivateConnection` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/get)`

|  Retrieves a `PrivateConnection` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/list)`

|  Lists `PrivateConnection` resources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections/patch)`

|  Modifies a `PrivateConnection` resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
