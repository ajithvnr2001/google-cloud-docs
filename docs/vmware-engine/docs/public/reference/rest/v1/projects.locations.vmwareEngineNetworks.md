---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks
title: REST Resource: projects.locations.vmwareEngineNetworks \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:20.513001+00:00
---

# REST Resource: projects.locations.vmwareEngineNetworks  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.vmwareEngineNetworks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VmwareEngineNetwork
    * JSON representation
  * VpcNetwork
    * JSON representation
  * Type
  * State
  * Type
  * Methods



## Resource: VmwareEngineNetwork

VMware Engine network resource that provides connectivity for VMware Engine private clouds.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "vpcNetworks": [
        {
          object ([VpcNetwork](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#VpcNetwork))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#State)),
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#Type_1)),
      "uid": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the VMware Engine network. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/global/vmwareEngineNetworks/my-network`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` User-provided description for this VMware Engine network.  
`vpcNetworks[]` |  `object (`[VpcNetwork](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#VpcNetwork)`)` Output only. VMware Engine service VPC networks that provide connectivity from a private cloud to customer projects, the internet, and other Google Cloud services.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#State)`)` Output only. State of the VMware Engine network.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#Type_1)`)` Required. VMware Engine network type.  
`uid` |  `string` Output only. System-generated unique identifier for the resource.  
`etag` |  `string` Checksum that may be sent on update and delete requests to ensure that the user-provided value is up to date before the server processes a request. The server computes checksums based on the value of other fields in the request.  
  
## VpcNetwork

Represents a VMware Engine VPC network that is managed by a VMware Engine network resource.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#Type)),
      "network": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks#Type)`)` Output only. Type of VPC network (INTRANET, INTERNET, or GOOGLE_CLOUD)  
`network` |  `string` Output only. The relative resource name of the service VPC network this VMware Engine network is attached to. For example: `projects/123123/global/networks/my-network`  
  
## Type

Enum Type defines possible types of a VMware Engine network controlled service.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`INTRANET` | VPC network that will be peered with a consumer VPC network or the intranet VPC of another VMware Engine network. Access a private cloud through Compute Engine VMs on a peered VPC network or an on-premises resource connected to a peered consumer VPC network.  
`INTERNET` | VPC network used for internet access to and from a private cloud.  
`GOOGLE_CLOUD` | VPC network used for access to Google Cloud services like Cloud Storage.  
  
## State

Enum State defines possible states of VMware Engine network.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`CREATING` | The VMware Engine network is being created.  
`ACTIVE` | The VMware Engine network is ready.  
`UPDATING` | The VMware Engine network is being updated.  
`DELETING` | The VMware Engine network is being deleted.  
  
## Type

Enum Type defines possible types of VMware Engine network.

Enums  
---  
`TYPE_UNSPECIFIED` | The default value. This value should never be used.  
`LEGACY` | Network type used by private clouds created in projects without a network of type `STANDARD`. This network type is no longer used for new VMware Engine private cloud deployments.  
`STANDARD` | Standard network type used for private cloud connectivity.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/create)`

|  Creates a new VMware Engine network that can be used by a private cloud.  
  
### `[delete](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/delete)`

|  Deletes a `VmwareEngineNetwork` resource.  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/get)`

|  Retrieves a `VmwareEngineNetwork` resource by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/list)`

|  Lists `VmwareEngineNetwork` resources in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.vmwareEngineNetworks/patch)`

|  Modifies a VMware Engine network resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
