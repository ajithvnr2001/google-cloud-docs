---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers
title: REST Resource: projects.locations.zones.routers \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:52.227892+00:00
---

# REST Resource: projects.locations.zones.routers  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers

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
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.zones.routers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Router
    * JSON representation
  * Interface
    * JSON representation
  * BgpPeer
    * JSON representation
  * Bgp
    * JSON representation
  * Methods



## Resource: Router

Message describing Router object

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
      "network": string,
      "interface": [
        {
          object ([Interface](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#Interface))
        }
      ],
      "bgpPeer": [
        {
          object ([BgpPeer](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#BgpPeer))
        }
      ],
      "bgp": {
        object ([Bgp](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#Bgp))
      },
      "state": enum ([ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/ResourceState)),
      "routeAdvertisements": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The canonical resource name of the router.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the router was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the router was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`network` |  `string` Required. The canonical name of the network to which this router belongs. The name is in the form of `projects/{project}/locations/{location}/zones/{zone}/networks/{network}`.  
`interface[]` |  `object (`[Interface](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#Interface)`)` Router interfaces.  
`bgpPeer[]` |  `object (`[BgpPeer](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#BgpPeer)`)` BGP peers.  
`bgp` |  `object (`[Bgp](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers#Bgp)`)` BGP information specific to this router.  
`state` |  `enum (`[ResourceState](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/ResourceState)`)` Output only. Current stage of the resource to the device by config push.  
`routeAdvertisements[]` |  `string` Optional. A list of CIDRs in IP/Length format to advertise northbound as static routes from this router.  
  
## Interface

Router Interface defines the GDCE zone side layer-3 information for building the BGP session.

JSON representation  
---  
      
    
    {
      "name": string,
      "ipv4Cidr": string,
      "ipv6Cidr": string,
      "linkedInterconnectAttachment": string,
      "subnetwork": string,
      "loopbackIpAddresses": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Name of this interface entry. Unique within the Zones resource.  
`ipv4Cidr` |  `string` IP address and range of the interface.  
`ipv6Cidr` |  `string` IPv6 address and range of the interface.  
`linkedInterconnectAttachment` |  `string` The canonical name of the linked Interconnect attachment.  
`subnetwork` |  `string` The canonical name of the subnetwork resource that this interface belongs to.  
`loopbackIpAddresses[]` |  `string` Create loopback interface in the router when specified. The number of IP addresses must match the number of TOR devices.  
  
## BgpPeer

BGPPeer defines the peer side layer-3 information for building the BGP session.

JSON representation  
---  
      
    
    {
      "name": string,
      "interface": string,
      "interfaceIpv4Cidr": string,
      "interfaceIpv6Cidr": string,
      "peerIpv4Cidr": string,
      "peerIpv6Cidr": string,
      "peerAsn": integer,
      "localAsn": integer
    }  
  
Fields  
---  
`name` |  `string` Name of this BGP peer. Unique within the Zones resource.  
`interface` |  `string` Name of the RouterInterface the BGP peer is associated with.  
`interfaceIpv4Cidr` |  `string` IP range of the interface within Google.  
`interfaceIpv6Cidr` |  `string` IPv6 range of the interface within Google.  
`peerIpv4Cidr` |  `string` IP range of the BGP interface outside Google.  
`peerIpv6Cidr` |  `string` IPv6 range of the BGP interface outside Google.  
`peerAsn` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.  
`localAsn` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Output only. Local BGP Autonomous System Number (ASN). This field is ST_NOT_REQUIRED because it stores private ASNs, which are meaningless outside the zone in which they are being used.  
  
## Bgp

BGP information specific to this router.

JSON representation  
---  
      
    
    {
      "asn": integer,
      "keepaliveIntervalInSeconds": integer
    }  
  
Fields  
---  
`asn` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Locally assigned BGP ASN.  
`keepaliveIntervalInSeconds` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The interval in seconds between BGP keepalive messages that are sent to the peer. Default is 20 with value between 20 and 60.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/create)`

|  Creates a new Router in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/delete)`

|  Deletes a single Router.  
  
### `[diagnose](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/diagnose)`

|  Get the diagnostics of a single router resource.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/get)`

|  Gets details of a single Router.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/list)`

|  Lists Routers in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/reference/network/rest/v1/projects.locations.zones.routers/patch)`

|  Updates the parameters of a single Router.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
