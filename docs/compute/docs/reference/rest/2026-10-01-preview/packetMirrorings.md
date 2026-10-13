---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/
title: REST Resource: packetMirrorings \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:50.341358+00:00
---

# REST Resource: packetMirrorings  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: packetMirrorings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PacketMirroring
    * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: PacketMirroring

Represents a Packet Mirroring resource.

Packet Mirroring clones the traffic of specified instances in your Virtual Private Cloud (VPC) network and forwards it to a collector destination, such as an instance group of an internal TCP/UDP load balancer, for analysis or examination. For more information about setting up Packet Mirroring, see [Using Packet Mirroring](https://docs.cloud.google.com/vpc/docs/using-packet-mirroring).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "selfLink": string,
      "name": string,
      "description": string,
      "region": string,
      "network": {
        "url": string,
        "canonicalUrl": string
      },
      "priority": integer,
      "collectorIlb": {
        "url": string,
        "canonicalUrl": string
      },
      "mirroredResources": {
        "subnetworks": [
          {
            "url": string,
            "canonicalUrl": string
          }
        ],
        "instances": [
          {
            "url": string,
            "canonicalUrl": string
          }
        ],
        "tags": [
          string
        ]
      },
      "filter": {
        "cidrRanges": [
          string
        ],
        "IPProtocols": [
          string
        ],
        "direction": enum
      },
      "enable": enum
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#packetMirroring` for packet mirrorings.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URI of the region where the packetMirroring resides.  
`network` |  `object` Specifies the mirrored VPC network. Only packets in this network will be mirrored. All mirrored VMs should have a NIC in the given network. All mirrored subnetworks should belong to the given network.  
`network.url` |  `string` URL of the network resource.  
`network.canonicalUrl` |  `string` Output only. Unique identifier for the network; defined by the server.  
`priority` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The priority of applying this configuration. Priority is used to break ties in cases where there is more than one matching rule. In the case of two rules that apply for a given Instance, the one with the lowest-numbered priority value wins.Default value is 1000. Valid range is 0 through 65535.  
`collectorIlb` |  `object` The Forwarding Rule resource of type `loadBalancingScheme=INTERNAL` that will be used as collector for mirrored traffic. The specified forwarding rule must have `isMirroringCollector` set to true.  
`collectorIlb.url` |  `string` Resource URL to the forwarding rule representing the ILB configured as destination of the mirrored traffic.  
`collectorIlb.canonicalUrl` |  `string` Output only. Unique identifier for the forwarding rule; defined by the server.  
`mirroredResources` |  `object` PacketMirroring mirroredResourceInfos. MirroredResourceInfo specifies a set of mirrored VM instances, subnetworks and/or tags for which traffic from/to all VM instances will be mirrored.  
`mirroredResources.subnetworks[]` |  `object` A set of subnetworks for which traffic from/to all VM instances will be mirrored. They must live in the same region as this packetMirroring.You may specify a maximum of 5 subnetworks.  
`mirroredResources.subnetworks[].url` |  `string` Resource URL to the subnetwork for which traffic from/to all VM instances will be mirrored.  
`mirroredResources.subnetworks[].canonicalUrl` |  `string` Output only. Unique identifier for the subnetwork; defined by the server.  
`mirroredResources.instances[]` |  `object` A set of virtual machine instances that are being mirrored. They must live in zones contained in the same region as this packetMirroring.Note that this config will apply only to those network interfaces of the Instances that belong to the network specified in this packetMirroring.You may specify a maximum of 50 Instances.  
`mirroredResources.instances[].url` |  `string` Resource URL to the virtual machine instance which is being mirrored.  
`mirroredResources.instances[].canonicalUrl` |  `string` Output only. Unique identifier for the instance; defined by the server.  
`mirroredResources.tags[]` |  `string` A set of mirrored tags. Traffic from/to all VM instances that have one or more of these tags will be mirrored.  
`filter` |  `object` Filter for mirrored traffic. If unspecified, all IPv4 traffic is mirrored.  
`filter.cidrRanges[]` |  `string` One or more IPv4 or IPv6 CIDR ranges that apply as filters on the source (ingress) or destination (egress) IP in the IP header. If no ranges are specified, all IPv4 traffic that matches the specified IPProtocols is mirrored. If neither cidrRanges nor IPProtocols is specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use "0.0.0.0/0,::/0".  
`filter.IPProtocols[]` |  `string` Protocols that apply as filter on mirrored traffic. If no protocols are specified, all traffic that matches the specified CIDR ranges is mirrored. If neither cidrRanges nor IPProtocols is specified, all IPv4 traffic is mirrored.  
`filter.direction` |  `enum` Direction of traffic to mirror, either INGRESS, EGRESS, or BOTH. The default is BOTH.  
`enable` |  `enum` Indicates whether or not this packet mirroring takes effect. If set to FALSE, this packet mirroring policy will not be enforced on the network.The default is TRUE.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/aggregatedList)`

|  Retrieves an aggregated list of packetMirrorings.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/delete)`

|  Deletes the specified PacketMirroring resource.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/get)`

|  Returns the specified PacketMirroring resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/insert)`

|  Creates a PacketMirroring resource in the specified project and region using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/list)`

|  Retrieves a list of PacketMirroring resources available to the specified project and region.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/patch)`

|  Patches the specified PacketMirroring resource with the data included in the request.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/packetMirrorings/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
