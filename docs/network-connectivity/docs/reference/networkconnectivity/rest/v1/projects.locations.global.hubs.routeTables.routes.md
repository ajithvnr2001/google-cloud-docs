---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes
title: REST Resource: projects.locations.global.hubs.routeTables.routes \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:36.935762+00:00
---

# REST Resource: projects.locations.global.hubs.routeTables.routes  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  REST Resource: projects.locations.global.hubs.routeTables.routes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Route
    * JSON representation
  * RouteType
  * NextHopVpcNetwork
    * JSON representation
  * NextHopVPNTunnel
    * JSON representation
  * NextHopRouterApplianceInstance
    * JSON representation
  * NextHopInterconnectAttachment
    * JSON representation
  * NextHopSpoke
    * JSON representation
  * Methods



## Resource: Route

A route defines a path from VM instances within a spoke to a specific destination resource. Only VPC spokes have routes.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "ipCidrRange": string,
      "type": enum ([RouteType](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#RouteType)),
      "nextHopVpcNetwork": {
        object ([NextHopVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopVpcNetwork))
      },
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/State)),
      "spoke": string,
      "location": string,
      "priority": string,
      "nextHopVpnTunnel": {
        object ([NextHopVPNTunnel](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopVPNTunnel))
      },
      "nextHopRouterApplianceInstance": {
        object ([NextHopRouterApplianceInstance](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopRouterApplianceInstance))
      },
      "nextHopInterconnectAttachment": {
        object ([NextHopInterconnectAttachment](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopInterconnectAttachment))
      },
      "nextHopSpoke": {
        object ([NextHopSpoke](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopSpoke))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The name of the route. Route names must be unique. Route names use the following form: `projects/{projectNumber}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the route was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the route was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ipCidrRange` |  `string` The destination IP address range.  
`type` |  `enum (`[RouteType](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#RouteType)`)` Output only. The route's type. Its type is determined by the properties of its IP address range.  
`nextHopVpcNetwork` |  `object (`[NextHopVpcNetwork](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopVpcNetwork)`)` Immutable. The destination VPC network for packets on this route.  
`labels` |  `map (key: string, value: string)` Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` An optional description of the route.  
`uid` |  `string` Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different `uid`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/State)`)` Output only. The current lifecycle state of the route.  
`spoke` |  `string` Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE  
`location` |  `string` Output only. The origin location of the route. Uses the following form: "projects/{project}/locations/{location}" Example: projects/1234/locations/us-central1  
`priority` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The priority of this route. Priority is used to break ties in cases where a destination matches more than one route. In these cases the route with the lowest-numbered priority value wins.  
`nextHopVpnTunnel` |  `object (`[NextHopVPNTunnel](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopVPNTunnel)`)` Immutable. The next-hop VPN tunnel for packets on this route.  
`nextHopRouterApplianceInstance` |  `object (`[NextHopRouterApplianceInstance](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopRouterApplianceInstance)`)` Immutable. The next-hop Router appliance instance for packets on this route.  
`nextHopInterconnectAttachment` |  `object (`[NextHopInterconnectAttachment](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopInterconnectAttachment)`)` Immutable. The next-hop VLAN attachment for packets on this route.  
`nextHopSpoke` |  `object (`[NextHopSpoke](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes#NextHopSpoke)`)` Immutable. The next-hop spoke for packets on this route.  
  
## RouteType

The route's type

Enums  
---  
`ROUTE_TYPE_UNSPECIFIED` | No route type information specified  
`VPC_PRIMARY_SUBNET` | The route leads to a destination within the primary address range of the VPC network's subnet.  
`VPC_SECONDARY_SUBNET` | The route leads to a destination within the secondary address range of the VPC network's subnet.  
`DYNAMIC_ROUTE` | The route leads to a destination in a dynamic route. Dynamic routes are derived from Border Gateway Protocol (BGP) advertisements received from an NCC hybrid spoke.  
  
## NextHopVpcNetwork

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` The URI of the VPC network resource  
  
## NextHopVPNTunnel

A route next hop that leads to a VPN tunnel resource.

JSON representation  
---  
      
    
    {
      "uri": string,
      "vpcNetwork": string,
      "siteToSiteDataTransfer": boolean
    }  
  
Fields  
---  
`uri` |  `string` The URI of the VPN tunnel resource.  
`vpcNetwork` |  `string` The VPC network where this VPN tunnel is located.  
`siteToSiteDataTransfer` |  `boolean` Indicates whether site-to-site data transfer is allowed for this VPN tunnel resource. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).  
  
## NextHopRouterApplianceInstance

A route next hop that leads to a Router appliance instance.

JSON representation  
---  
      
    
    {
      "uri": string,
      "vpcNetwork": string,
      "siteToSiteDataTransfer": boolean
    }  
  
Fields  
---  
`uri` |  `string` The URI of the Router appliance instance.  
`vpcNetwork` |  `string` The VPC network where this VM is located.  
`siteToSiteDataTransfer` |  `boolean` Indicates whether site-to-site data transfer is allowed for this Router appliance instance resource. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).  
  
## NextHopInterconnectAttachment

A route next hop that leads to an interconnect attachment resource.

JSON representation  
---  
      
    
    {
      "uri": string,
      "vpcNetwork": string,
      "siteToSiteDataTransfer": boolean
    }  
  
Fields  
---  
`uri` |  `string` The URI of the interconnect attachment resource.  
`vpcNetwork` |  `string` The VPC network where this interconnect attachment is located.  
`siteToSiteDataTransfer` |  `boolean` Indicates whether site-to-site data transfer is allowed for this interconnect attachment resource. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).  
  
## NextHopSpoke

A route next hop that leads to a spoke resource.

JSON representation  
---  
      
    
    {
      "uri": string,
      "siteToSiteDataTransfer": boolean
    }  
  
Fields  
---  
`uri` |  `string` The URI of the spoke resource.  
`siteToSiteDataTransfer` |  `boolean` Indicates whether site-to-site data transfer is allowed for this spoke resource. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). Whether this route is accessible to other hybrid spokes with site-to-site data transfer enabled. If this is false, the route is only accessible to VPC spokes of the connected Hub.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes/get)`

|  Gets details about the specified route.  
  
### `[list](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes/list)`

|  Lists routes in a given route table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
