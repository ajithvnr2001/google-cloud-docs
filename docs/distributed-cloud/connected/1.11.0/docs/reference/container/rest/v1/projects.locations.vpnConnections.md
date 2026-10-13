---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections
title: REST Resource: projects.locations.vpnConnections \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:17.984593+00:00
---

# REST Resource: projects.locations.vpnConnections  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections

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
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.vpnConnections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VpnConnection
    * JSON representation
  * BgpRoutingMode
  * VpcProject
    * JSON representation
  * Details
    * JSON representation
  * State
  * CloudRouter
    * JSON representation
  * CloudVpn
    * JSON representation
  * Methods



## Resource: VpnConnection

A VPN connection .

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
      "natGatewayIp": string,
      "bgpRoutingMode": enum ([BgpRoutingMode](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#BgpRoutingMode)),
      "cluster": string,
      "vpc": string,
      "vpcProject": {
        object ([VpcProject](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#VpcProject))
      },
      "enableHighAvailability": boolean,
      "router": string,
      "details": {
        object ([Details](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#Details))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of VPN connection  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the VPN connection was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the VPN connection was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`natGatewayIp` |  `string` NAT gateway IP, or WAN IP address. If a customer has multiple NAT IPs, the customer needs to configure NAT such that only one external IP maps to the GMEC Anthos cluster. This is empty if NAT is not used.  
`bgpRoutingMode  
**(deprecated)**` |  `enum (`[BgpRoutingMode](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#BgpRoutingMode)`)` This item is deprecated!Dynamic routing mode of the VPC network, `regional` or `global`.  
`cluster` |  `string` The canonical Cluster name to connect to. It is in the form of projects/{project}/locations/{location}/clusters/{cluster}.  
`vpc` |  `string` The network ID of VPC to connect to.  
`vpcProject` |  `object (`[VpcProject](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#VpcProject)`)` Optional. Project detail of the VPC network. Required if VPC is in a different project than the cluster project.  
`enableHighAvailability` |  `boolean` Whether this VPN connection has HA enabled on cluster side. If enabled, when creating VPN connection we will attempt to use 2 ANG floating IPs.  
`router` |  `string` Optional. The VPN connection Cloud Router name.  
`details` |  `object (`[Details](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#Details)`)` Output only. The created connection details.  
  
## BgpRoutingMode

Routing mode.

Enums  
---  
`BGP_ROUTING_MODE_UNSPECIFIED` | Unknown.  
`REGIONAL` | Regional mode.  
`GLOBAL` | Global mode.  
  
## VpcProject

Project detail of the VPC network.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "serviceAccount": string
    }  
  
Fields  
---  
`projectId` |  `string` The project of the VPC to connect to. If not specified, it is the same as the cluster project.  
`serviceAccount  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: do not use.  
  
## Details

The created connection details.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#State)),
      "error": string,
      "cloudRouter": {
        object ([CloudRouter](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#CloudRouter))
      },
      "cloudVpns": [
        {
          object ([CloudVpn](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#CloudVpn))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#State)`)` The state of this connection.  
`error` |  `string` The error message. This is only populated when state=ERROR.  
`cloudRouter` |  `object (`[CloudRouter](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#CloudRouter)`)` The Cloud Router info.  
`cloudVpns[]` |  `object (`[CloudVpn](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#CloudVpn)`)` Each connection has multiple Cloud VPN gateways.  
  
## State

The current connection state.

Enums  
---  
`STATE_UNSPECIFIED` | Unknown.  
`STATE_CONNECTED` | Connected.  
`STATE_CONNECTING` | Still connecting.  
`STATE_ERROR` | Error occurred.  
  
## CloudRouter

The Cloud Router info.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` The associated Cloud Router name.  
  
## CloudVpn

The Cloud VPN info.

JSON representation  
---  
      
    
    {
      "gateway": string
    }  
  
Fields  
---  
`gateway` |  `string` The created Cloud VPN gateway name.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/create)`

|  Creates a new VPN connection in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/delete)`

|  Deletes a single VPN connection.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/get)`

|  Gets details of a single VPN connection.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/list)`

|  Lists VPN connections in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
