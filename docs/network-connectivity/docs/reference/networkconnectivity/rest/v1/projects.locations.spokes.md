---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes
title: REST Resource: projects.locations.spokes \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:24.371800+00:00
---

# REST Resource: projects.locations.spokes  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spokes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Spoke
    * JSON representation
  * Methods



## Resource: Spoke

A Network Connectivity Center spoke represents one or more network connectivity resources.

When you create a spoke, you associate it with a hub. You must also identify a value for exactly one of the following fields:

  * linkedVpnTunnels
  * linkedInterconnectAttachments
  * linkedRouterApplianceInstances
  * linkedVpcNetwork

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "hub": string,
      "group": string,
      "linkedVpnTunnels": {
        object ([LinkedVpnTunnels](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedVpnTunnels))
      },
      "linkedInterconnectAttachments": {
        object ([LinkedInterconnectAttachments](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedInterconnectAttachments))
      },
      "linkedRouterApplianceInstances": {
        object ([LinkedRouterApplianceInstances](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedRouterApplianceInstances))
      },
      "linkedVpcNetwork": {
        object ([LinkedVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedVpcNetwork))
      },
      "linkedProducerVpcNetwork": {
        object ([LinkedProducerVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedProducerVpcNetwork))
      },
      "uniqueId": string,
      "state": enum ([State](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/State)),
      "reasons": [
        {
          object ([StateReason](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#StateReason))
        }
      ],
      "spokeType": enum ([SpokeType](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/SpokeType)),
      "etag": string,
      "fieldPathsPendingUpdate": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. The name of the spoke. Spoke names must be unique. They use the following form: `projects/{projectNumber}/locations/{region}/spokes/{spokeId}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the spoke was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the spoke was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. An optional description of the spoke.  
`hub` |  `string` Immutable. The name of the hub that this spoke is attached to.  
`group` |  `string` Optional. The name of the group that this spoke is associated with.  
`linkedVpnTunnels` |  `object (`[LinkedVpnTunnels](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedVpnTunnels)`)` Optional. VPN tunnels that are associated with the spoke.  
`linkedInterconnectAttachments` |  `object (`[LinkedInterconnectAttachments](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedInterconnectAttachments)`)` Optional. VLAN attachments that are associated with the spoke.  
`linkedRouterApplianceInstances` |  `object (`[LinkedRouterApplianceInstances](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedRouterApplianceInstances)`)` Optional. Router appliance instances that are associated with the spoke.  
`linkedVpcNetwork` |  `object (`[LinkedVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedVpcNetwork)`)` Optional. VPC network that is associated with the spoke.  
`linkedProducerVpcNetwork` |  `object (`[LinkedProducerVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#LinkedProducerVpcNetwork)`)` Optional. The linked producer VPC that is associated with the spoke.  
`uniqueId` |  `string` Output only. The Google-generated UUID for the spoke. This value is unique across all spoke resources. If a spoke is deleted and another with the same name is created, the new spoke is assigned a different `uniqueId`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/State)`)` Output only. The current lifecycle state of this spoke.  
`reasons[]` |  `object (`[StateReason](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke#StateReason)`)` Output only. The reasons for current state of the spoke.  
`spokeType` |  `enum (`[SpokeType](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/SpokeType)`)` Output only. The type of resource associated with the spoke.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`fieldPathsPendingUpdate[]` |  `string` Optional. The list of fields waiting for hub administration's approval.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create)`

|  Creates a Network Connectivity Center spoke.  
  
### `[delete](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/delete)`

|  Deletes a Network Connectivity Center spoke.  
  
### `[get](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/get)`

|  Gets details about a Network Connectivity Center spoke.  
  
### `[getIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/list)`

|  Lists the Network Connectivity Center spokes in a specified project and location.  
  
### `[patch](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/patch)`

|  Updates the parameters of a Network Connectivity Center spoke.  
  
### `[setIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
