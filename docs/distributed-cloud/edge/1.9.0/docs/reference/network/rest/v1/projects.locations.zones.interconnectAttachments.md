---
url: https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments
title: REST Resource: projects.locations.zones.interconnectAttachments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:56.382816+00:00
---

# REST Resource: projects.locations.zones.interconnectAttachments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments




#  REST Resource: projects.locations.zones.interconnectAttachments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InterconnectAttachment
    * JSON representation
  * Methods



## Resource: InterconnectAttachment

Message describing InterconnectAttachment object

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
      "interconnect": string,
      "network": string,
      "vlanId": integer,
      "mtu": integer,
      "state": enum ([ResourceState](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/ResourceState))
    }  
  
Fields  
---  
`name` |  `string` Required. The canonical resource name of the interconnect attachment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the interconnect attachment was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the interconnect attachment was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`interconnect` |  `string` Required. The canonical name of underlying Interconnect object that this attachment's traffic will traverse through. The name is in the form of `projects/{project}/locations/{location}/zones/{zone}/interconnects/{interconnect}`.  
`network` |  `string` Optional. The canonical Network name in the form of `projects/{project}/locations/{location}/zones/{zone}/networks/{network}`.  
`vlanId` |  `integer` Required. VLAN id provided by user. Must be site-wise unique.  
`mtu` |  `integer` IP (L3) MTU value of the virtual edge cloud. Valid values are: 1500 and 9000. Default to 1500 if not set.  
`state` |  `enum (`[ResourceState](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/ResourceState)`)` Output only. Current stage of the resource to the device by config push.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/create)`

|  Creates a new InterconnectAttachment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/delete)`

|  Deletes a single InterconnectAttachment.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/get)`

|  Gets details of a single InterconnectAttachment.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/edge/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/list)`

|  Lists InterconnectAttachments in a given project and location.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
