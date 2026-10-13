---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks
title: REST Resource: projects.locations.zones.networks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:46.358147+00:00
---

# REST Resource: projects.locations.zones.networks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks




#  REST Resource: projects.locations.zones.networks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Network
    * JSON representation
  * Methods



## Resource: Network

Message describing Network object

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
      "mtu": integer
    }  
  
Fields  
---  
`name` |  `string` Required. The canonical resource name of the network.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the network was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the network was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`mtu` |  `integer` IP (L3) MTU value of the network. Valid values are: 1500 and 9000. Default to 1500 if not set.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks/create)`

|  Creates a new Network in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks/delete)`

|  Deletes a single Network.  
  
### `[diagnose](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks/diagnose)`

|  Get the diagnostics of a single network resource.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks/get)`

|  Gets details of a single Network.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/edge/1.6.0/docs/reference/network/rest/v1/projects.locations.zones.networks/list)`

|  Lists Networks in a given project and location.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
