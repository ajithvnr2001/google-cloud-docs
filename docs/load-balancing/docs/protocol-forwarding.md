---
url: https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding/
title: Protocol forwarding overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:34.227247+00:00
---

# Protocol forwarding overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Protocol forwarding overview Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses external and internal protocol forwarding only. For more information about protocol forwarding in the context of Classic VPN, see [Create a Classic VPN gateway using static routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns). 

Protocol forwarding uses a [regional forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) to deliver packets of a specific protocol to a single virtual machine (VM) instance. The forwarding rule can have an internal or an external IP address. Protocol forwarding delivers packets while preserving the destination IP address of the forwarding rule. The forwarding rule references an object called a target instance, which, in turn, references a single VM instance.

You can use protocol forwarding to do the following:

  * Provide an IP address which can be moved from one instance to another by either changing the VM referenced by the target instance object or by changing the target instance referenced by the forwarding rule.
  * Forward packets to different VMs based on protocol and port. Two forwarding rules can share the same IP address as long as their port and protocol information is unique.
  * (External protocol forwarding only) Define additional external IP addresses for a given network interface. Unlike a network interface with a 1:1 NAT configuration for its external IPv4 address, protocol forwarding preserves the destination IP address of the forwarding rule.
  * Send packets whose source IP addresses match the forwarding rule's IP address.



Protocol forwarding is different from a [pass-through load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#proxy-pass-through) in the following ways:

  * **No load balancing**. A target instance only distributes packets to a single VM.
  * **No health check**. Unlike a backend service, a target instance doesn't support a health check. You must use other means to ensure that the necessary software is running and operational on the VM referenced by the target instance.



## Architecture

Protocol forwarding uses regional external or regional internal forwarding rules and a zonal target instance object. The target instance and the VM it references must be located in a zone in the forwarding rule's region.

  * **External protocol forwarding**. You can set up multiple forwarding rules to point to a single target instance, which lets you use multiple external IP addresses with one VM instance. You can use this in scenarios where you may want to serve data from just one VM instance, but through different external IP addresses or different protocols and ports. This is especially useful for setting up SSL virtual hosting. External protocol forwarding can handle connections from IPv6 clients.

External protocol forwarding supports the following protocols: AH, ESP, GRE, ICMP, ICMPv6, SCTP, TCP, and UDP .

The following diagram shows an example of external protocol forwarding architecture. To learn how to set this up, see [Set up external protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/set-up-protocol-forwarding#set-up-ext-pf).

[ ![External protocol forwarding architecture.](https://docs.cloud.google.com/static/load-balancing/images/pf-ext.svg)](https://docs.cloud.google.com/static/load-balancing/images/pf-ext.svg) External protocol forwarding architecture (click to enlarge).
  * **Internal protocol forwarding**. Internal protocol forwarding uses either a regional internal IPv4 address (from the [primary IPv4 address range of a subnet](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges)) or a regional internal IPv6 address range (from the [IPv6 address range of a subnet](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges)).

Internal protocol forwarding supports the following protocols: TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE .

The following diagram shows an example of internal protocol forwarding architecture. To learn how to set this up, see [Set up internal protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/set-up-protocol-forwarding#set-up-int-pf).

[ ![Internal protocol forwarding architecture.](https://docs.cloud.google.com/static/load-balancing/images/pf-int.svg)](https://docs.cloud.google.com/static/load-balancing/images/pf-int.svg) Internal protocol forwarding architecture (click to enlarge).

With internal protocol forwarding, you can change the target of a forwarding rule to switch between a target instance and a backend service of a pass-through load balancer. For details, see [Switch between a target instance and a backend service](https://docs.cloud.google.com/load-balancing/docs/switch-between-target-instance-and-backend-service).




### Forwarding rules

Each forwarding rule matches an IP address, protocol, and optionally, port information (if specified and if the protocol supports ports). When a forwarding rule references a target instance, Google Cloud routes packets that match the forwarding rule's address, protocol, and port specification to the VM referenced by the target instance.

  * Internal protocol forwarding:

    * **IPv4 address support**. A regional internal IPv4 address from the primary IPv4 range of a subnet. You can specify a [reserved static IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip) or a custom ephemeral IPv4 address. If not specified, Google Cloud automatically assigns an ephemeral IPv4 address.

    * **IPv6 address support**. The forwarding rule references a `/96` range of IP addresses from the subnet's `/64` internal IPv6 address range. The subnet must be either of the following:

      * A dual-stack (IPv4 and IPv6) subnet
      * A single-stack (IPv6-only) subnet

The subnet's `ipv6-access-type` setting must be set to `INTERNAL`.

Internal IPv6 addresses are available only in Premium Tier. You can specify a [reserved static IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) or a custom ephemeral IPv6 address. If not specified, Google Cloud automatically assigns an ephemeral IPv6 address.

To specify a custom ephemeral IPv6 address, you must use the gcloud CLI or the API. The Google Cloud console doesn't support specifying custom ephemeral IPv6 addresses for forwarding rules.

    * **Protocol options**. `TCP`(default), `UDP`, and `L3_DEFAULT`.

      * The `L3_DEFAULT` forwarding rule protocol option forwards all TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE traffic. For the TCP, UDP, and SCTP protocols, `L3_DEFAULT` also forwards all ports.
    * **Port specification options**. A list of up to five contiguous or non-contiguous ports or all ports.

  * External protocol forwarding:

    * **IPv4 address support**. The forwarding rule references a single [regional external IPv4 address](https://docs.cloud.google.com/vpc/docs/ip-addresses). Regional external IPv4 addresses come from a pool unique to each Google Cloud region. You can specify a [reserved static IPv4 address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses). If not specified, Google Cloud automatically assigns an IPv4 address.

    * **IPv6 address support**. The forwarding rule references a `/96` range of IP addresses from the second half (`/65`) of the subnet's `/64` external IPv6 address range as described in [External IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6). The subnet must be either of the following:

      * A dual-stack (IPv4 and IPv6) subnet
      * A single-stack (IPv6-only) subnet

The subnet `ipv6-access-type` must be set to `EXTERNAL`.

External IPv6 addresses are available only in Premium Tier. You can specify a [reserved static IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) or a custom ephemeral IPv6 address. If not specified, Google Cloud automatically assigns an ephemeral IPv6 address.

To specify a custom ephemeral IPv6 address, you must use the gcloud CLI or the API. The Google Cloud console doesn't support specifying custom ephemeral IPv6 addresses for forwarding rules.

    * **Protocol options**. `AH`, `ESP`, `ICMP`, `SCTP`, `TCP` (default), `UDP`, and `L3_DEFAULT` :

      * The `L3_DEFAULT` forwarding rule protocol option forwards all AH, ESP, GRE, ICMP, ICMPv6, SCTP, TCP, and UDP traffic. For the TCP, UDP, and SCTP protocols, `L3_DEFAULT` also forwards all ports.
      * IPv6 forwarding rules don't support the `ICMP` protocol setting because the ICMP protocol only supports IPv4 addresses. To serve ICMPv6 and GRE traffic, set the forwarding rule protocol to `L3_DEFAULT`.
    * **Port specification options**. A contiguous port range or all ports.




Keep the following points in mind when working with forwarding rules:

  * For protocol forwarding, a forwarding rule can only reference a single target instance.

  * For internal passthrough Network Load Balancers and backend service-based regional external passthrough Network Load Balancers, a forwarding rule can only reference a single backend service.

  * You can switch between internal protocol forwarding and an internal passthrough Network Load Balancer without deleting and re-creating the forwarding rule. To switch between external protocol forwarding and a backend service-based regional external passthrough Network Load Balancer, you must delete and re-create the forwarding rule. For details, see [Switch between a target instance and a backend service](https://docs.cloud.google.com/load-balancing/docs/switch-between-target-instance-and-backend-service).

  * Port information can only be specified for protocols that have a concept of port: `TCP`, `UDP`, or `SCTP`.

  * If you expect fragmented UDP packets, do one of the following to ensure that all fragments (including those without port information) are delivered to the instance:

    * Use a single `L3_DEFAULT` forwarding rule, or
    * Use a single `UDP` forwarding rule configured to forward all ports.



### Target instances

A target instance is a zonal resource that references one VM instance in the same zone. The forwarding rule that references the target instance must be in the region containing the target instance's zone. Because a target instance doesn't have a Cloud NAT policy applied to it, it can be used for IPsec traffic that can't traverse NAT.

#### Multi-NIC support

Protocol forwarding using target instances delivers packets to a [load balancer target interface](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers), which can be the `nic0` vNIC or a different vNIC or Dynamic Network Interface.

To select a load balancer target interface, use the `--network` flag when you create the target instance:

  * If you omit the `--network` flag when you create a target instance, Google Cloud delivers packets to the `nic0` interface of the referenced VM.
  * If you include the `--network` flag when you create a target instance, the VM must have a load balancer target interface in that VPC network.
  * Internal protocol forwarding and IPv6 external protocol forwarding have the following additional requirement because their forwarding rules use subnets: When configuring a forwarding rule to reference a target instance, the forwarding rule must use a subnet of the target instance's VPC network. The forwarding rule and target instance cannot use different VPC networks, even if those networks are connected in some way.

**Note:** Cloud Armor features such as [advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos) and [network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies) aren't supported for VM instances using Dynamic NICs.

#### IPv6 support for VM instances

If you want the protocol forwarding deployment to support IPv6 traffic, the VM instance must be configured in either a [dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6) or a [single-stack IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only) that is in the same region as the IPv6 forwarding rule.

Note that while IPv6-only instances can be created in both dual-stack and IPv6-only subnets, dual-stack VMs can't be created in IPv6-only subnets.

The VM instance can be created in a subnet with the `ipv6-access-type` set to either `EXTERNAL` or `INTERNAL`. The VM inherits the `ipv6-access-type` setting (either `EXTERNAL` or `INTERNAL`) from the subnet.

For instructions, see [Create an instance that uses IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6). If you want to use an existing VM, you can update the VM to be dual-stack by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update). Updating existing VMs to IPv6-only isn't supported.

### IP addresses for request and return packets

When a target instance receives a packet from a client, the request packet's source and destination IP addresses are as shown in this table.

**Table 1.** Source and destination IP addresses for request packets Protocol forwarding type | Source IP address | Destination IP address  
---|---|---  
**External protocol forwarding** | The external IP address associated with a Google Cloud VM or an external IP address of a client on the internet. | The IP address of the forwarding rule.  
**Internal protocol forwarding** | A client's internal IP address; for Google Cloud clients, the primary internal IPv4 address or IPv6 address or an IPv4 address from an alias IP range of a VM's network interface. | The IP address of the forwarding rule.  
  
Software running on the target instance VMs should be configured to do the following:

  * Listen on (bind to) the forwarding rule IP address or any IP address (`0.0.0.0` or `::`).
  * If the forwarding rule's protocol supports ports, then listen on (bind to) a port that's included in the forwarding rule.



Return packets are sent directly from the target instance to the client. The response packet's source and destination IP addresses depend on the protocol:

  * TCP is connection-oriented. Target instances must reply with packets that have source IP addresses that match the forwarding rule's IP address. This ensures that the client can associate the response packets with the appropriate TCP connection.
  * AH, ESP, GRE, ICMP, ICMPv6, and UDP are connectionless. Target instances can send response packets which have source IP addresses that either match the forwarding rule's IP address, or match any IP address assigned to the VM's NIC in the same VPC network as the forwarding rule. Practically speaking, most clients expect the response to come from the same IP address to which they sent packets.



The following table summarizes sources and destinations for return packets:

**Table 2.** Source and destination IP addresses for return packets Traffic type | Source IP address | Destination IP address  
---|---|---  
**TCP** | The IP address of the forwarding rule. | The request packet's source IP address.  
**AH, ESP, GRE, ICMP, ICMPv6, and UDP** | For most use cases, the IP address of the forwarding rule.1 | The request packet's source IP address.  
  
1 With internal protocol forwarding, it is possible to set the response packet's source to the VM NIC's primary internal IPv4 address or IPv6 address or an alias IP address range. If a VM has IP forwarding enabled, it can use an arbitrary source IP address for packets that it sends to destinations routed within a VPC network. Not using the forwarding rule's IP address as a source is an advanced scenario because the client receives a response packet from an internal IP address that does not match the IP address to which it sent a request packet.

### Outbound internet connectivity from target instances

VM instances referenced by target instances can initiate connections to the internet by using the IP address of the associated forwarding rule as the source IP address of the outbound connection.

Generally, a VM instance always uses its own external IP address or Cloud NAT to initiate connections. You use the forwarding rule IP address to initiate connections from target instances only in special scenarios such as when you need VM instances to originate and receive connections at the same external IP address.

Outbound packets sent from target instance VMs directly to the internet have no restrictions on traffic protocols and ports. Even if an outbound packet is using the forwarding rule's IP address as the source, the packet's protocol and source port don't have to match the forwarding rule's protocol and port specification. However, inbound response packets must match the forwarding rule IP address, protocol, and destination port of the forwarding rule. For more information, see [Paths for regional external passthrough Network Load Balancers and external protocol forwarding](https://docs.cloud.google.com/vpc/docs/routes#paths_to_backends).

This path to internet connectivity from a target instance VM is the default intended behavior according to Google Cloud's [implied firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules). However, if you have security concerns about leaving this path open, you can use targeted egress firewall rules to block unsolicited outbound traffic to the internet.

## Limitations

  * A forwarding rule cannot point to more than one target instance.
  * Health checks are not supported with target instances. You must ensure that the necessary software is running and operational on the VM referenced by the target instance.
  * Internal protocol forwarding for IPv6 traffic doesn't support the `L3_DEFAULT` protocol. Use either `TCP` or `UDP`.
  * For Dynamic NICs, you must manually add local routes for forwarding rule IP addresses as described in the following known issue: [Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dropped-packets-dynamic-nics).



## API and gcloud reference

For forwarding rules, see the following:

  * [gcloud compute forwarding-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)
  * [REST Resource: forwardingRules](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)



For target instances, see the following:

  * [gcloud compute target-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-instances)
  * [REST Resource: targetInstances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances)



## Pricing

For pricing information, see [Network pricing: Cloud Load Balancing](https://cloud.google.com/vpc/network-pricing#cloud-load-balancing).

## Quotas and limits

For the quotas on forwarding rules for protocol forwarding, see [Quotas and limits: Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/quotas#forwarding_rules).

## What's next

  * [Troubleshoot protocol forwarding](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-networking#troubleshooting_protocol_forwarding_for_private_forwarding_rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
