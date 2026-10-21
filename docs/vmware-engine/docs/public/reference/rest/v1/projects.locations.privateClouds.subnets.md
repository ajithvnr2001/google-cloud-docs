---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets
title: REST Resource: projects.locations.privateClouds.subnets \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:19.137166+00:00
---

# REST Resource: projects.locations.privateClouds.subnets  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.privateClouds.subnets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Subnet
    * JSON representation
  * State
  * Methods



## Resource: Subnet

Subnet in a private cloud. Either `management` subnets (such as vMotion) that are read-only, or `userDefined`, which can also be updated.

JSON representation  
---  
      
    
    {
      "name": string,
      "ipCidrRange": string,
      "gatewayIp": string,
      "type": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets#State)),
      "vlanId": integer
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this subnet. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet`  
`ipCidrRange` |  `string` The IP address range of the subnet in CIDR format '10.0.0.0/24'.  
`gatewayIp` |  `string` The IP address of the gateway of this subnet. Must fall within the IP prefix defined above.  
`type` |  `string` Output only. The type of the subnet. For example "management" or "userDefined".  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets#State)`)` Output only. The state of the resource.  
`vlanId` |  `integer` Output only. VLAN ID of the VLAN on which the subnet is configured  
  
## State

Defines possible states of subnets.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | The subnet is ready.  
`CREATING` | The subnet is being created.  
`UPDATING` | The subnet is being updated.  
`DELETING` | The subnet is being deleted.  
`RECONCILING` | Changes requested in the last operation are being propagated.  
`FAILED` | Last operation on the subnet did not succeed. Subnet's payload is reverted back to its most recent working state.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/get)`

|  Gets details of a single subnet.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/list)`

|  Lists subnets in a given private cloud.  
  
### `[patch](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/patch)`

|  Updates the parameters of a single subnet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
