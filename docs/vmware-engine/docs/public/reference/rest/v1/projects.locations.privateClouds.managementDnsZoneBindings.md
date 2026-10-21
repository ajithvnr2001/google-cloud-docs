---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings
title: REST Resource: projects.locations.privateClouds.managementDnsZoneBindings \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:17.630482+00:00
---

# REST Resource: projects.locations.privateClouds.managementDnsZoneBindings  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.managementDnsZoneBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ManagementDnsZoneBinding
    * JSON representation
  * State
  * Methods



## Resource: ManagementDnsZoneBinding

Represents a binding between a network and the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings#State)),
      "description": string,
      "uid": string,
    
      // Union field bind_network can be only one of the following:
      "vpcNetwork": string,
      "vmwareEngineNetwork": string
      // End of list of possible types for union field bind_network.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of this binding. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings#State)`)` Output only. The state of the resource.  
`description` |  `string` User-provided description for this resource.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
Union field `bind_network`. Required. The relative resource name of the network to bind to the management DNS zone. This network can be a consumer VPC network or a VMware engine network. `bind_network` can be only one of the following:  
`vpcNetwork` |  `string` Network to bind is a standard consumer VPC. Specify the name in the following form for consumer VPC network: `projects/{project}/global/networks/{network_id}`. `{project}` can either be a project number or a project ID.  
`vmwareEngineNetwork` |  `string` Network to bind is a VMware Engine network. Specify the name in the following form for VMware engine network: `projects/{project}/locations/global/vmwareEngineNetworks/{vmwareEngineNetworkId}`. `{project}` can either be a project number or a project ID.  
  
## State

Enum State defines possible states of binding between the consumer VPC network and the management DNS zone.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | The binding is ready.  
`CREATING` | The binding is being created.  
`UPDATING` | The binding is being updated.  
`DELETING` | The binding is being deleted.  
`FAILED` | The binding has failed.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/create)`

|  Creates a new `ManagementDnsZoneBinding` resource in a private cloud.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/delete)`

|  Deletes a `ManagementDnsZoneBinding` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/get)`

|  Retrieves a 'ManagementDnsZoneBinding' resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/list)`

|  Lists Consumer VPCs bound to Management DNS Zone of a given private cloud.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/patch)`

|  Updates a `ManagementDnsZoneBinding` resource.  
  
### `[repair](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.managementDnsZoneBindings/repair)`

|  Retries to create a `ManagementDnsZoneBinding` resource that is in failed state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
