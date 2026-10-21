---
url: https://docs.cloud.google.com/load-balancing/docs/internal/
title: Internal passthrough Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:08.892332+00:00
---

# Internal passthrough Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal passthrough Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

An internal passthrough Network Load Balancer is a regional load balancer that is built on the [Andromeda network virtualization stack](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf).

Internal passthrough Network Load Balancers distribute traffic among internal virtual machine (VM) instances in the same region in a Virtual Private Cloud (VPC) network. It enables you to run and scale your services behind an internal IP address that is accessible only to systems in the same VPC network or systems connected to your VPC network.

Use an internal passthrough Network Load Balancer in the following circumstances:

  * You need a high-performance, pass-through Layer 4 load balancer for TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE protocols.
  * If serving traffic through TLS (SSL), it is acceptable to have SSL traffic terminated by your backends instead of by the load balancer. The internal passthrough Network Load Balancer cannot terminate SSL traffic.
  * You need to forward the original packets unproxied. For example, if you need the client source IP address to be preserved.
  * You have an existing setup that uses a pass-through load balancer, and you want to migrate it without changes.



The internal passthrough Network Load Balancers address many use cases. For a few high-level examples, see [Passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer#int-pass-netlb).

## How internal passthrough Network Load Balancers work

An internal passthrough Network Load Balancer has a frontend (the forwarding rule) and a backend (the backend service). You can use either instance groups or `GCE_VM_IP` zonal NEGs as backends on the backend service. This example shows instance group backends.

[ ![High-level internal passthrough Network Load Balancer example.](https://docs.cloud.google.com/static/load-balancing/images/ilb-high-level.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-high-level.svg) High-level internal passthrough Network Load Balancer example (click to enlarge).

Unlike a proxy load balancer, an internal passthrough Network Load Balancer doesn't terminate connections from clients and then open new connections to backends. Instead, an internal passthrough Network Load Balancer routes connections directly from clients to eligible backends, without a proxy between the clients and backends. Responses from each selected backend are delivered using direct server return. For more information, see [Traffic distribution for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution) and IP addresses for request and return packets.

The load balancer monitors backend health by using health check probes. For more information, see the Health check section.

The Google Cloud [Linux guest environment](https://docs.cloud.google.com/compute/docs/instances/linux-guest-environment), [Windows guest environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or an equivalent process configures each backend VM with the IP address of the load balancer. For VMs created from Google Cloud images, the [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment) (formerly, the Windows Guest Environment or Linux Guest Environment) installs the local route for the load balancer's IP address. Google Kubernetes Engine instances based on [Container- Optimized OS](https://docs.cloud.google.com/compute/docs/containers) implement this by using `iptables` instead.

Google Cloud virtual networking manages traffic delivery and scaling as appropriate.

### Protocols, scheme, and scope

Each internal passthrough Network Load Balancer supports the following:

  * One backend service with load balancing scheme `INTERNAL` and a supported protocol. For more information, see [backend service](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service).
  * Backend VMs specified as either one of the following: 
    * Managed and unmanaged instance groups that are located in one [region](https://docs.cloud.google.com/compute/docs/regions-zones) and VPC network.
    * Backend [zonal network endpoint groups (NEGs) with `GCE_VM_IP` type endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts) that are located in the same [region](https://docs.cloud.google.com/compute/docs/regions-zones) and VPC network. Endpoints in the NEG must be primary internal IP addresses in the same subnet and zone used by the NEG.
  * Support for IPv4 and IPv6 traffic when using instance group backends. Zonal network endpoint groups (NEGs) with `GCE_VM_IP` endpoints only support IPv4 traffic.
  * One or more forwarding rules, each using either the `TCP`, `UDP`, or `L3_DEFAULT` protocol matching the backend service's protocol.
  * Each forwarding rule with its own unique IP address or [multiple forwarding rules that share a common IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip).
  * Each forwarding rule with up to five ports or all ports.
  * If global access is enabled, clients in any region.
  * If global access is disabled, clients in the same region as the load balancer.



An internal passthrough Network Load Balancer doesn't support the following:

  * Backend VMs in multiple regions.
  * Balancing traffic that originates from the internet, unless you're using it with an external load balancer.
  * IPv6 packets with fragmented headers.



### Client access

By default, the load balancer only supports clients that are in the same region as the load balancer. Clients can be in the same network as the load balancer or in a VPC network connected by using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). You can [enable global access](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access) to allow clients from any region to access your internal passthrough Network Load Balancer.

[ ![Internal passthrough Network Load Balancer with global access.](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-global-access-arch.svg)](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-global-access-arch.svg) Internal passthrough Network Load Balancer with global access (click to enlarge).

The following table summarizes client access.

Global access disabled | Global access enabled  
---|---  
Clients must be in the same region as the load balancer. They also must be in the same VPC network as the load balancer or in a VPC network that is connected to the load balancer's VPC network by using VPC Network Peering. | Clients can be in any region. They still must be in the same VPC network as the load balancer or in a VPC network that's connected to the load balancer's VPC network by using VPC Network Peering.  
On-premises clients can access the load balancer through [Cloud VPN tunnels or VLAN attachments](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks#using-vpn-interconnect). These tunnels or attachments must be in the same region as the load balancer. | On-premises clients can access the load balancer through Cloud VPN tunnels or VLAN attachments. These tunnels or attachments can be in any region.  
  
### IP addresses for request and return packets

When a backend VM receives a load-balanced packet from a client, the packet's source and destination are as follows:

  * **Source:** the client's internal IPv4, IPv6, or the IPv4 address from one of the client's alias IPv4 ranges.
  * **Destination:** the IP address of the load balancer's forwarding rule. The forwarding rule uses either a single [ internal IPv4 address](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) or an [internal IPv6 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

Because the load balancer is a passthrough load balancer (not a proxy), packets arrive bearing the IP address of the load balancer's forwarding rule. 

Although the guest environment automatically configures local routes so that the VM's operating system accepts traffic destined for the load balancer's IP address, the operating system cannot deliver these packets to your application if the application is configured to listen only on the VM's assigned internal IP address.

To ensure that the operating system delivers packets to your application, configure the application running on backend VMs to do the following:

  * Listen on (bind to) the load balancer's forwarding rule IP address or any IP address (`0.0.0.0` or `::`)


  * If the load balancer forwarding rule's protocol supports ports, listen on (bind to) a port that's included in the load balancer's forwarding rule



Return packets are sent directly from the load balancer's backend VMs to the client. The return packet's source IP address depends on the protocol:

  * TCP and SCTP are connection-oriented so backend VMs must reply with packets whose source IP addresses match the destination IP address of the requesting packet so that the client can associate the response packets with the appropriate TCP connection.
  * UDP, ICMP, ICMPv6, ESP, AH, and GRE are connectionless. Backend VMs can send response packets whose source IP addresses either match the forwarding rule's IP address or match any assigned IP address for the VM. Practically speaking, most clients expect the response to come from the same IP address to which they sent packets.



The following table summarizes the source and destination IP addresses for response packets:

Traffic type | Source | Destination  
---|---|---  
TCP, SCTP | The requesting packet's destination | The requesting packet's source  
UDP, ICMP, ICMPv6, ESP, AH, and GRE | For most use cases, the requesting packet's destination1 | The requesting packet's source  
  
1 It is possible to set the response packet's source to the VM NIC's primary internal IPv4 address or an alias IP address range. If the VM has IP forwarding enabled, arbitrary IP address sources can also be used. Not using the forwarding rule's IP address as a source is an advanced scenario because the client receives a response packet from an internal IP address that doesn't match the IP address to which it sent a request packet.

## Architecture

An internal passthrough Network Load Balancer with multiple backends distributes connections among all of those backends. For information about the distribution method and its configuration options, see traffic distribution.

You can use either instance groups or zonal NEGs, but not a combination of both, as backends for an internal passthrough Network Load Balancer:

  * If you choose instance groups, you can use unmanaged instance groups, zonal managed instance groups, regional managed instance groups, or a combination of instance group types.
  * If you choose zonal NEGs, you must use `GCE_VM_IP` zonal NEGs.



High availability describes how to design an internal load balancer that isn't dependent on a single zone.

Instances that participate as backend VMs for internal passthrough Network Load Balancers must be running the appropriate Linux or Windows guest environment or other processes that provide equivalent functionality. This guest environment must be able to contact the metadata server (`metadata.google.internal`, 169.254.169.254) to read instance metadata so that it can generate local routes to accept traffic sent to the load balancer's internal IP address.

[This diagram](https://docs.cloud.google.com/static/load-balancing/images/ilb-high-level.svg) shows traffic distribution among VMs located in two separate instance groups. Traffic sent from the client instance to the IP address of the load balancer (10.10.10.9) is distributed among backend VMs in either instance group. Responses sent from any of the serving backend VMs are delivered directly to the client VM.

You can use an internal passthrough Network Load Balancer with either a [custom mode or auto mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) VPC network. You can also create internal passthrough Network Load Balancers with an existing [legacy network](https://docs.cloud.google.com/vpc/docs/legacy).

An internal passthrough Network Load Balancer doesn't support the following:

  * Backend VMs in multiple regions
  * Balancing traffic that originates from the internet, unless you're [using it with an external load balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer#multi-tier)
  * IPv6 packets with fragmented headers



### Internal IP address

Internal passthrough Network Load Balancers support IPv4-only, dual-stack, and IPv6-only subnets. For more information about each one, see [Types of subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

An internal passthrough Network Load Balancer requires at least one forwarding rule. The forwarding rule references the internal IP address:

  * For **IPv4 traffic** , the forwarding rule references an IPv4 address from the primary IPv4 subnet range.
  * For **IPv6 traffic** , the forwarding rule references a `/96` range of internal IPv6 addresses from the subnet's `/64` internal IPv6 address range. The subnet must be either a dual-stack or single-stack IPv6-only subnet with an [internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) (`ipv6-access-type` set to `INTERNAL`). The IPv6 address range can be a [reserved static address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) or an ephemeral address.

For more information about IPv6 support, see the VPC documentation about [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) and [IPv6 addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).




### Firewall configuration

Internal passthrough Network Load Balancers require the following configuration for hierarchical firewall policies and VPC firewall rules:

  * Allow ingress from [IPv4 or IPv6 health check source ranges](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).
  * Allow ingress from client IPv4 or IPv6 address source ranges.



For more information, see [Configuring firewall rules](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure_firewall_rules_dual_stack).

### Forwarding rules

A [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) specifies the protocol and ports on which the load balancer accepts traffic. Because internal passthrough Network Load Balancers aren't proxies, they pass traffic to backends on the same protocol and port.

An internal passthrough Network Load Balancer requires at least one internal forwarding rule. You can define multiple forwarding rules for the same load balancer.

If you want the load balancer to handle both IPv4 and IPv6 traffic, create two forwarding rules: one rule for IPv4 traffic that points to IPv4 (or dual-stack) backends, and one rule for IPv6 traffic that points only to dual-stack backends. It's possible to have an IPv4 and an IPv6 forwarding rule reference the same backend service, but the backend service must reference dual-stack backends.

The forwarding rule must reference a specific [subnet](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) in the same VPC network and region as the load balancer's backend components. This requirement has the following implications:

  * The subnet that you specify for the forwarding rule doesn't need to be the same as any of the subnets used by backend VMs; however, the subnet must be in the same region as the forwarding rule.
  * For **IPv4 traffic** , the internal forwarding rule references a regional internal IPv4 address from the primary IPv4 address range of the subnet that you select. The IPv4 address can be assigned either by specifying [a reserved internal IPv4 address](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#reserve-ip-address), specifying a custom ephemeral IPv4 address, or letting Google Cloud automatically assign an ephemeral IPv4 address.
  * For **IPv6 traffic** , the forwarding rule references a `/96` range of IPv6 addresses from the subnet's `/64` internal IPv6 address range. The subnet must be a dual-stack subnet with the `ipv6-access-type` set to `INTERNAL`. The `/96` IPv6 address range can be assigned by either specifying [a reserved internal IPv6 address](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#reserve-ip-address), specifying a custom ephemeral IPv6 address, or letting Google Cloud automatically assign an ephemeral IPv6 address.

To specify a custom ephemeral IPv6 address, you must use the gcloud CLI or the API. The Google Cloud console doesn't support specifying custom ephemeral IPv6 addresses for forwarding rules.




#### Forwarding rule protocols

Internal passthrough Network Load Balancers support the following IPv4 protocol options for each forwarding rule: `TCP`, `UDP`, or `L3_DEFAULT`.

Internal passthrough Network Load Balancers support the following IPv6 protocol options for each forwarding rule: `TCP` or `UDP`.

The `L3_DEFAULT` option enables you to load balance TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE protocols.

In addition to supporting protocols other than TCP and UDP, the `L3_DEFAULT` option makes it possible for a single forwarding rule to simultaneously forward traffic for multiple protocols. For example, in addition to making HTTP requests, you can also ping the load balancer IP address.

Forwarding rules that use the `TCP` or `UDP` protocols can reference a backend service by using either the same protocol as the forwarding rule or a backend service using the `UNSPECIFIED` protocol.

If you're using the `L3_DEFAULT` protocol, you must configure the forwarding rule to accept traffic on all ports. To configure all ports, either set [`--ports=ALL`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules) by using the Google Cloud CLI, or set [`allPorts` to `True`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) by using the API.

The following table summarizes how to use these settings for different protocols:

Traffic to be load-balanced | Forwarding rule protocol | Backend service protocol  
---|---|---  
**TCP (IPv4 or IPv6)** | `TCP` | `TCP or UNSPECIFIED`  
**UDP (IPv4 or IPv6)** | `UDP` | `UDP or UNSPECIFIED`  
**TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE** | `L3_DEFAULT` | `UNSPECIFIED`  
  
#### Forwarding rules and global access

An internal passthrough Network Load Balancer's forwarding rules are regional, even when global access is enabled. After you enable global access, the regional internal forwarding rule's `allowGlobalAccess` flag is set to `true`.

#### Forwarding rules and port specifications

When you create an internal forwarding rule, you must choose one of the following port specifications:

  * Specify at least one and up to five ports, by number.
  * Specify `ALL` to forward traffic on all ports.



An internal forwarding rule that supports either all TCP ports or all UDP ports allows backend VMs to run multiple applications, each on its own port. Traffic sent to a given port is delivered to the corresponding application, and all applications use the same IP address.

When you need to forward traffic on more than five specific ports, combine [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) with forwarding rules. When you create the forwarding rule, specify all ports, and then create ingress `allow` firewall rules that only permit traffic to the desired ports. Apply the firewall rules to the backend VMs.

You cannot modify a forwarding rule after you create it. If you need to change the specified ports or the internal IP address for an internal forwarding rule, you must delete and recreate it.

#### Multiple forwarding rules for a single backend service

You can configure multiple internal forwarding rules that all reference the same internal backend service. An internal passthrough Network Load Balancer requires at least one internal forwarding rule.

Configuring multiple forwarding rules for the same backend service lets you do the following:

  * **Assign multiple IP addresses to the load balancer**. You can create multiple forwarding rules, each using a unique IP address. Each forwarding rule can specify all ports or a set of up to five ports.

  * **Assign a specific set of ports, using the same IP address, to the load balancer**. You can create multiple forwarding rules sharing the same IP address, where each forwarding rule uses a specific set of up to five ports. This is an alternative to configuring a single forwarding rule that specifies all ports.




For more information about scenarios involving two or more internal forwarding rules that share a common internal IP address, see [Multiple forwarding rules with the same IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip).

When using multiple internal forwarding rules, make sure that you configure the software running on your backend VMs to bind to all of the forwarding rule IP addresses or to any address (`0.0.0.0/0` for IPv4 or `::/0` for IPv6). The destination IP address for a packet delivered through the load balancer is the internal IP address associated with the corresponding internal forwarding rule. For more information, see TCP and UDP request and return packets.

### Backend service

Each internal passthrough Network Load Balancer has one regional internal backend service that defines backend parameters and behavior. The name of the backend service is the name of the internal passthrough Network Load Balancer shown in the Google Cloud console.

Each backend service defines the following backend parameters:

  * **Protocol**. A backend service supports IPv4 and IPv6 traffic. If the protocol has a concept of a port (like `TCP` or `UDP`), the backend service delivers packets to backend VMs on the same destination port to which traffic was sent.

Backend services support the following IPv4 protocol options: `TCP`, `UDP`, or `UNSPECIFIED`.

Backend services support the following IPv6 protocol options: `TCP` or `UDP`. The backend service protocol must coordinate with the forwarding rule protocol.

For a table with possible forwarding rule and backend service protocol combinations, see Forwarding rule protocol specification.

  * **Traffic distribution**. A backend service allows traffic to be distributed according to a configurable [session affinity](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#session_affinity_options).

  * **Health check**. A backend service must have an associated health check.




Each backend service operates in a single region and distributes traffic for backend VMs in a single VPC network:

  * **One type of backend, one region**. Backends are either [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) or [zonal NEGs with `GCE_VM_IP` endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts) located in the same region as the backend service and forwarding rule. Instance group backends can be unmanaged instance groups, zonal managed instance groups, or regional managed instance groups. Zonal NEG backends must use `GCE_VM_IP` endpoints.

  * **One VPC network**. Each instance group or NEG backend has an associated VPC network, even if that instance group or NEG hasn't been connected to a backend service yet. For more information about how a network is associated with each type of backend, see Instance group backends and network interfaces and Zonal NEG backends and network interfaces. The backend service resource itself also has an associated VPC network, which can be defined explicitly or implicitly. For more information about the backend service's network, see Backend service network specification and Backend service network rules.




#### Instance group backends and network interfaces

The VPC network and subnet that are associated with an instance group are set implicitly as described in [Instance group backends and network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-net-ig).

To distribute load-balanced traffic to a non-`nic0` load balancer target interface, we recommend you use zonal NEGs with `GCE_VM_IP` endpoints. However, it is possible to set the VPC network of a backend service to match a VPC network that contains a non-`nic0` load balancer target interface. For more information, see Backend service network specification and Backend service network rules. 

#### Zonal NEG backends and network interfaces

The VPC network and subnet that are associated with a zonal NEG with `GCE_VM_IP` endpoints are set when the NEG is created. For more information and rules for endpoints, see [`GCE_VM_IP` zonal NEG backends and network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-net-neg-vm-ip).

#### Backend service network specification

You can explicitly associate a VPC network with a backend service by using the `--network` flag when you create the backend service. The backend service network rules go into effect immediately.

If you omit the `--network` flag when you create a backend service, Google Cloud uses one of the following qualifying events to implicitly set the backend service's associated VPC network. After it is set, the backend service's associated VPC network cannot be changed:

  * **First forwarding rule to reference a backend service** : If the backend service doesn't have any associated backend groups, the first forwarding rule that references the backend service sets the backend service's VPC network. The backend service's VPC network is the network that contains the subnet used by the forwarding rule.

  * **First instance group added to the backend service** : If the backend service doesn't have any forwarding rule that references it, the first instance group that you add as a backend sets the backend service's VPC network. The backend service's VPC network is the instance group's network—the VPC network that contains the `nic0` network interface of each member backend VM.

  * **First zonal NEG backend (with`GCE_VM_IP` endpoints) added to the backend service**: If the backend service doesn't have any forwarding rule that references it, the first zonal NEG backend (with `GCE_VM_IP` endpoints) that you add as a backend sets the backend service's VPC network. The backend service's VPC network is the NEG's network.




After the backend service's VPC network has been set by a qualifying event, any additional forwarding rules or backend groups that you add must follow the backend service network rules.

#### Backend service network rules

The following rules apply after a backend service is associated with a specific VPC network:

  * When adding a forwarding rule that references the backend service, the forwarding rule must use a subnet in the backend service's VPC network. The forwarding rule and backend service cannot use different VPC networks, even if those networks are connected.

  * When adding instance group backends, _one_ of the following must be true:

    * The instance group's VPC network (which is the network used by the `nic0` interface of each member VM) must match the backend service's VPC network.

    * Each backend VM must have a [load balancer target interface](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers) in the backend service's VPC network.

  * When adding zonal NEG backends with `GCE_VM_IP` endpoints, the NEG's VPC network must match the backend service's VPC network.




#### Dual-stack backends (IPv4 and IPv6)

If you want the load balancer to use dual-stack backends that handle both IPv4 and IPv6 traffic, note the following requirements:

  * Backends must be configured in [dual-stack subnets](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) that are in the same region as the load balancer's IPv6 forwarding rule. For the backends, you can use a subnet with the `ipv6-access-type` set to either `INTERNAL` or `EXTERNAL`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, you must use a different dual-stack or IPv6-only subnet with `ipv6-access-type` set to `INTERNAL` for the load balancer's internal forwarding rule. For more information, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).
  * Backends must be configured to be dual-stack with `stack-type` set to `IPV4_IPV6`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, you must also set the `--ipv6-network-tier` to `PREMIUM`. For more information, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).



#### IPv6-only backends

If you want the load balancer to use IPv6-only backends, note the following requirements:

  * IPv6-only instances are only supported in unmanaged instance groups. No other backend type is supported.
  * Backends must be configured in either [dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6) or [IPv6-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only) that are in the same region as the load balancer's IPv6 forwarding rule. For the backends, you can use a subnet with the `ipv6-access-type` set to either `INTERNAL` or `EXTERNAL`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, you must use a different IPv6-only subnet with `ipv6-access-type` set to `INTERNAL` for the load balancer's internal forwarding rule.
  * Backends must be configured to be IPv6-only with the VM `stack-type` set to `IPV6_ONLY`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, you must also set the `--ipv6-network-tier` to `PREMIUM`. For more information, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).



Note that IPv6-only VMs can be created under both dual-stack and IPv6-only subnets, but dual-stack VMs can't be created under IPv6-only subnets.

#### Backend subsetting

Backend subsetting is an optional feature that improves performance by limiting the number of backends to which traffic is distributed.

We recommend that you only enable subsetting if you need to support more than 250 backend VMs on a single load balancer. For more information, see [Backend subsetting for internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/backend-service#tcp-subsetting).

### Health check

Health check information is used to determine eligible backends for new connections, and you can control whether existing connections persist on unhealthy backends. For more information about eligible backends, see [Traffic distribution for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution).

#### Health check type, protocol, and port

The load balancer's backend service must reference a global or regional health check, using any supported health check protocol and port. The health check protocol and port details don't have to match the load balancer backend service protocol and forwarding rule IP port information.

Because all supported health check protocols rely on TCP, when you use an internal passthrough Network Load Balancer to balance connections and traffic for other protocols, backend VMs must run a TCP-based server to answer health check probers. For example, you can use an HTTP health check combined with running an HTTP server on each backend VM. In this example, your scripts or software are responsible for configuring the HTTP server so that it returns status `200` only when the software listening to load-balanced connections is operational.

For more information about supported health check protocols and ports, see [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports) and [How health checks work](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method).

#### Health check packets

Health check probers send packets to the backend VM network interface that's in the VPC network that matches the Backend service network specification. Health check packets have the following characteristics:

  * Source IP address from the relevant health check [probe IP range](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).
  * Destination IP address that matches each IP address of a forwarding rule that references the internal passthrough Network Load Balancer backend service.
  * Destination port that matches the port number you specify in the health check.



Software running on the backend VMs must bind to and listen on relevant IP address and port combinations. The simplest way to accomplish this is to configure software to bind to and listen on the relevant ports of any of the VM's IP addresses (`0.0.0.0`). For more information, see [Destination for probe packets](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest).

## High availability architecture

The internal passthrough Network Load Balancer is highly available by design. There are no special steps to make the load balancer highly available because the mechanism doesn't rely on a single device or VM instance.

To deploy your backend VM instances to multiple zones, follow these deployment recommendations:

  * Use [regional managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) if you can deploy your software by using instance templates. Regional managed instance groups automatically distribute traffic among multiple zones, providing the best option to avoid potential issues in any given zone.

  * If you use [zonal managed instance groups or unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups), use multiple instance groups in different zones (in the same region) for the same backend service. Using multiple zones protects against potential issues in any given zone.




## Shared VPC architecture

The following table summarizes the component requirements for internal passthrough Network Load Balancers used with Shared VPC networks. For an example, see [creating an internal passthrough Network Load Balancer on the Provisioning Shared VPC page](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#creating_an_internal_load_balancer_forwarding_rule).

IP address | Forwarding rule | Backend components  
---|---|---  
An  internal IP address must be defined in the same project as the backend VMs.   
  
For the load balancer to be available in a Shared VPC network, the Google Cloud internal IP address _must_ be defined in the same service project where the backend VMs are located, _and_ it must reference a subnet in the desired Shared VPC network in the host project. The address itself comes from the primary IP range of the referenced subnet.   
  
If you create an internal IP address in a service project and the IP address subnet is in the service project's VPC network, your internal passthrough Network Load Balancer is local to the service project. Your internal passthrough Network Load Balancer isn't local to any Shared VPC host project. | An internal forwarding rule must be defined in the same project as the backend VMs.   
  
For the load balancer to be available in a Shared VPC network, the internal forwarding rule **must** be defined in the same service project where the backend VMs are located, _and_ it must reference the same subnet (in the Shared VPC network) that the associated internal IP address references.   
  
If you create an internal forwarding rule in a service project and the forwarding rule's subnet is in the service project's VPC network, your internal passthrough Network Load Balancer is local to the service project. Your internal passthrough Network Load Balancer isn't local to any Shared VPC host project. | In a Shared VPC scenario, backend VMs are located in a service project. A  regional internal backend service and health check must be defined in that service project.  
  
## Traffic distribution

Internal passthrough Network Load Balancers support a variety of traffic distribution customization options, including session affinity, connection tracking, and failover. For details about how internal passthrough Network Load Balancers distribute traffic, and how these options interact with each other, see [Traffic distribution for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution).

## Quotas and limits

For information about quotas and limits, see [Load balancing resource quotas](https://docs.cloud.google.com/load-balancing/docs/quotas).

## Limitations

  * You cannot use the Google Cloud console to create an internal passthrough Network Load Balancer with zonal NEG backends.
  * For Dynamic NICs, you must manually add local routes for forwarding rule IP addresses as described in the following known issue: [Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dropped-packets-dynamic-nics).



## What's next

  * To configure and test an internal passthrough Network Load Balancer, see [Set up an internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal).
  * To configure Cloud Monitoring for internal passthrough Network Load Balancers, see [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring).
  * To troubleshoot issues with your internal passthrough Network Load Balancer, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb).
  * To use prebuilt Terraform templates to streamline the setup and management of Google Cloud's networking infrastructure, explore the [Simplified Cloud Networking Configuration Solutions GitHub repository](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
