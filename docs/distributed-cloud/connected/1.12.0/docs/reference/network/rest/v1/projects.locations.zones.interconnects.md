---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects
title: REST Resource: projects.locations.zones.interconnects \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:27.836476+00:00
---

# REST Resource: projects.locations.zones.interconnects  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.zones.interconnects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Interconnect
    * JSON representation
  * InterconnectType
  * Methods



## Resource: Interconnect

Message describing Interconnect object

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
      "interconnectType": enum ([InterconnectType](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects#InterconnectType)),
      "uuid": string,
      "deviceCloudResourceName": string,
      "physicalPorts": [
        string
      ],
      "remotePeeringNetworkType": enum ([RemotePeeringNetworkType](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/RemotePeeringNetworkType))
    }  
  
Fields  
---  
`name` |  `string` Required. The canonical resource name of the interconnect.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the subnet was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the subnet was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`interconnectType` |  `enum (`[InterconnectType](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects#InterconnectType)`)` Optional. Type of interconnect, which takes only the value 'DEDICATED' for now.  
`uuid` |  `string` Output only. Unique identifier for the link.  
`deviceCloudResourceName` |  `string` Output only. Cloud resource name of the switch device.  
`physicalPorts[]` |  `string` Output only. Physical ports (e.g., TenGigE0/0/0/1) that form the interconnect.  
`remotePeeringNetworkType` |  `enum (`[RemotePeeringNetworkType](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/RemotePeeringNetworkType)`)` Optional. The remote peering network type of the interconnect. It is required when peering separation is enabled.  
  
## InterconnectType

Type of interconnect.

Enums  
---  
`INTERCONNECT_TYPE_UNSPECIFIED` | Unspecified.  
`DEDICATED` | Dedicated Interconnect.  
  
## Methods  
  
---  
  
### `[diagnose](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects/diagnose)`

|  Get the diagnostics of a single interconnect resource.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects/get)`

|  Gets details of a single Interconnect.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/network/rest/v1/projects.locations.zones.interconnects/list)`

|  Lists Interconnects in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
