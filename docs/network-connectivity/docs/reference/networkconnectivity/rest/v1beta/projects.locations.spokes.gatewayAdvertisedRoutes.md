---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes
title: REST Resource: projects.locations.spokes.gatewayAdvertisedRoutes \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:13.666563+00:00
---

# REST Resource: projects.locations.spokes.gatewayAdvertisedRoutes  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spokes.gatewayAdvertisedRoutes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GatewayAdvertisedRoute
    * JSON representation
  * Recipient
  * Methods



## Resource: GatewayAdvertisedRoute

A gateway advertised route is a route that a gateway spoke advertises somewhere.

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
      "uniqueId": string,
      "state": enum (State),
      "ipRange": string,
      "recipient": enum ([Recipient](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes#Recipient)),
      "priority": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the gateway advertised route. Route names must be unique and use the following form: `projects/{projectNumber}/locations/{region}/spokes/{spoke}/gatewayAdvertisedRoutes/{gatewayAdvertisedRouteId}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the gateway advertised route was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the gateway advertised route was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` An optional description of the gateway advertised route.  
`uniqueId` |  `string` Output only. The Google-generated UUID for the gateway advertised route. This value is unique across all gateway advertised route resources. If a gateway advertised route is deleted and another with the same name is created, the new route is assigned a different `uniqueId`.  
`state` |  `enum (`State`)` Output only. The current lifecycle state of this gateway advertised route.  
`ipRange` |  `string` Immutable. This route's advertised IP address range. Must be a valid CIDR-formatted prefix. If an IP address is provided without a subnet mask, it is interpreted as, for IPv4, a `/32` singular IP address range, and, for IPv6, `/128`.  
`recipient` |  `enum (`[Recipient](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes#Recipient)`)` Optional. The recipient of this advertised route.  
`priority` |  `integer` Optional. The priority of this advertised route. You can choose a value from `0` to `65335`. If you don't provide a value, Google Cloud assigns a priority of `100` to the ranges.  
  
## Recipient

The recipient of an advertised route.

Enums  
---  
`RECIPIENT_UNSPECIFIED` | No recipient specified. By default routes are advertised to the hub.  
`ADVERTISE_TO_HUB` | Advertises a route toward the hub. Other spokes reachable from this spoke will receive the route.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/create)`

|  Create a GatewayAdvertisedRoute  
  
### `[delete](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/delete)`

|  Delete a GatewayAdvertisedRoute  
  
### `[get](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/get)`

|  Get a GatewayAdvertisedRoute  
  
### `[list](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/list)`

|  List GatewayAdvertisedRoutes  
  
### `[patch](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes/patch)`

|  Update a GatewayAdvertisedRoute  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
