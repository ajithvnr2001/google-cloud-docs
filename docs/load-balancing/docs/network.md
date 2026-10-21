---
url: https://docs.cloud.google.com/load-balancing/docs/network/
title: Backend service-based regional external passthrough Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:55.368080+00:00
---

# Backend service-based regional external passthrough Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Backend service-based regional external passthrough Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

Regional external passthrough Network Load Balancers are regional, Layer 4 load balancers that distribute external traffic among backends (instance groups or network endpoint groups (NEGs)) in the same region as the load balancer. These backends must be in the same region and project but can be in different VPC networks. These load balancers are built on [Maglev](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) and the [Andromeda network virtualization stack](https://cloudplatform.googleblog.com/2014/04/enter-andromeda-zone-google-cloud-platforms-latest-networking-stack.html).

Regional external passthrough Network Load Balancers can receive traffic from:

  * Any client on the internet
  * Google Cloud VMs with external IPs
  * Google Cloud VMs that have internet access through Cloud NAT or instance-based NAT



Regional external passthrough Network Load Balancers are _not proxies_. The load balancer itself doesn't terminate user connections. Load-balanced packets are sent to the backend VMs with their source and destination IP addresses, protocol, and, if applicable, ports, unchanged. The backend VMs then terminate user connections. Responses from the backend VMs go directly to the clients, not back through the load balancer. This process is known as direct server return (DSR).

Backend service-based regional external passthrough Network Load Balancers support the following features:

  * **Managed and unmanaged instance group backends**. Backend service-based regional external passthrough Network Load Balancers support both managed and unmanaged instance groups as backends. Managed instance groups automate certain aspects of backend management and provide better scalability and reliability as compared to unmanaged instance groups.
  * **Zonal NEG backends**. Backend service-based regional external passthrough Network Load Balancers support using zonal NEGs with `GCE_VM_IP` endpoints. Zonal NEG `GCE_VM_IP` endpoints let you do the following: 
    * Forward packets to any network interface, not just `nic0`.
    * Place the same `GCE_VM_IP` endpoint in two or more zonal NEGs connected to different backend services.
  * **Support for multiple protocols**. Backend service-based regional external passthrough Network Load Balancers can load-balance TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic.
  * **Support for IPv6 connectivity**. Backend service-based regional external passthrough Network Load Balancers can handle both IPv4 and IPv6 traffic.
  * **Fine-grained traffic distribution control**. A backend service allows traffic to be distributed according to the configured session affinity, connection tracking policy, and weighted load balancing settings. The backend service can also be configured to enable connection draining and designate failover backends for the load balancer. Most of these settings have default values that let you get started quickly. For more information, see [Traffic distribution for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution).
  * **Support for non-legacy, regional health checks**. Backend service-based regional external passthrough Network Load Balancers support regional health checks, which can use any supported health check protocol.
  * **Google Cloud Armor integration**. Cloud Armor supports advanced network DDoS protection for regional external passthrough Network Load Balancers. For more information, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).
  * **GKE integration**. If you are building applications in GKE, we recommend that you use the built-in [GKE Service controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service), which deploys Google Cloud load balancers on behalf of GKE users. This is the same as the standalone load balancing architecture described on this page, except that its lifecycle is fully automated and controlled by GKE.

Related GKE documentation:

    * [LoadBalancer Service concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer)
    * [Exposing applications using Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps)



## Architecture

The following diagram illustrates the components of a regional external passthrough Network Load Balancer:

[ ![Regional external passthrough Network Load Balancer with a regional backend service](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-backend-service.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-backend-service.svg) Regional external passthrough Network Load Balancer with a regional backend service

The load balancer is made up of several configuration components. A single load balancer can have the following:

  * One or more regional external IP addresses
  * One or more regional external forwarding rules
  * One regional external backend service
  * One or more backends: either all instance groups or all zonal NEG backends (`GCE_VM_IP` endpoints)
  * Health check associated with the backend service



Additionally, you must create firewall rules that allow your load balancing traffic and health check probes to reach the backend VMs.

### IP address

A regional external passthrough Network Load Balancer requires at least one forwarding rule. The forwarding rule references a regional external IP address that is accessible anywhere on the internet.

  * For **IPv4 traffic** , the forwarding rule references a single [regional external IPv4 address](https://docs.cloud.google.com/vpc/docs/ip-addresses). Regional external IPv4 addresses come from a pool unique to each Google Cloud region. The IPv4 address can be assigned either by specifying [a reserved external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) or by letting Google Cloud automatically assign an ephemeral IPv4 address.

  * For **IPv6 traffic** , the forwarding rule references a `/96` range of IPv6 addresses from a dual-stack or IPv6-only subnet. The subnet must have an [assigned external IPv6 subnet range](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) in the VPC network. External IPv6 addresses are available in Premium Tier and Standard Tier ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).

The `/96` IPv6 address range can be assigned by either specifying [a reserved external IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address), specifying a custom ephemeral IPv6 address, or letting Google Cloud automatically assign an ephemeral IPv6 address.

To specify a custom ephemeral IPv6 address, you must use the gcloud CLI or the API. The Google Cloud console doesn't support specifying custom ephemeral IPv6 addresses for forwarding rules.

For more details about IPv6 support, see the VPC documentation on [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) and [IPv6 addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).




Use a reserved IP address for the forwarding rule if you need to keep the address associated with your project for reuse after you delete a forwarding rule or if you need multiple forwarding rules to reference the same IP address.

Regional external passthrough Network Load Balancers support both Standard Tier and Premium Tier for regional external IPv4 addresses. Both the IP address and the forwarding rule must use the same network tier. Regional external IPv6 addresses are available in both Premium Tier and Standard Tier.

### Forwarding rule

A regional external forwarding rule specifies the protocol and ports on which the load balancer accepts traffic. Because regional external passthrough Network Load Balancers are not proxies, they pass traffic to backends on the same protocol and ports, if the packet carries port information. The forwarding rule in combination with the IP address forms the frontend of the load balancer.

The load balancer preserves the source IP addresses of incoming packets. The destination IP address for incoming packets is an IP address associated with the load balancer's forwarding rule.

Incoming traffic is matched to a forwarding rule, which is a combination of a particular IP address (either an IPv4 address or an IPv6 address range), protocol, and if the protocol is port-based, one of port(s), a range of ports, or all ports. The forwarding rule then directs traffic to the load balancer's backend service.

  * If the forwarding rule references an IPv4 address, the forwarding rule is not associated with any subnet. That is, its IP address comes from outside of any Google Cloud subnet range.

  * If the forwarding rule references a `/96` IPv6 address range, this `/96` IPv6 address range must come from a dual-stack or single-stack IPv6 subnet with an external IPv6 subnet range (with `--ipv6-access-type` set to `EXTERNAL`).

The subnet that the forwarding rule references can be the same subnet used by the backend instances; or, backend instances can be located in any dual-stack or single-stack IPv6 subnet in the same region as the forwarding rule. For example, the subnet used by the backends can have an internal IPv6 subnet range (with `--ipv6-access-type` set to `INTERNAL`).




A regional external passthrough Network Load Balancer requires at least one forwarding rule. Forwarding rules can be configured to direct traffic coming from a specific range of source IP addresses to a specific backend service (or target instance). For details, see traffic steering. You can define multiple forwarding rules for the same load balancer as described in Multiple forwarding rules.

If you want the load balancer to handle both IPv4 and IPv6 traffic, create two forwarding rules: one rule for IPv4 traffic that points to IPv4 (or dual-stack) backends, and one rule for IPv6 traffic that points only to dual-stack backends. It's possible to have an IPv4 and an IPv6 forwarding rule reference the same backend service, but the backend service must reference dual-stack backends.

#### Forwarding rule protocols

Regional external passthrough Network Load Balancers support the following protocol options for each forwarding rule: `TCP`, `UDP`, and `L3_DEFAULT`.

Use the `TCP` and `UDP` options to configure TCP or UDP load balancing. The `L3_DEFAULT` protocol option enables a regional external passthrough Network Load Balancer to load balance TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic.

In addition to supporting protocols other than TCP and UDP, `L3_DEFAULT` makes it possible for a single forwarding rule to serve multiple protocols. For example, IPsec services typically handle some combination of ESP and UDP-based IKE and NAT-T traffic. The `L3_DEFAULT` option allows a single forwarding rule to be configured to process all of those protocols.

Forwarding rules using the `TCP` or `UDP` protocols can reference a backend service using either the same protocol as the forwarding rule or a backend service whose protocol is `UNSPECIFIED`. `L3_DEFAULT` forwarding rules can only reference a backend service with protocol `UNSPECIFIED`.

If you're using the `L3_DEFAULT` protocol, you must configure the forwarding rule to accept traffic on all ports. To configure all ports, either set [`--ports=ALL`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules) by using the Google Cloud CLI, or set [`allPorts` to `True`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) by using the API.

The following table summarizes how to use these settings for different protocols.

Traffic to be load balanced | Forwarding rule protocol | Backend service protocol  
---|---|---  
**TCP** | `TCP` | `TCP` or `UNSPECIFIED`  
`L3_DEFAULT` | `UNSPECIFIED`  
**UDP** | `UDP` | `UDP` or `UNSPECIFIED`  
`L3_DEFAULT` | `UNSPECIFIED`  
**ESP, GRE, ICMP/ICMPv6 (echo request only)** | `L3_DEFAULT` | `UNSPECIFIED`  
  
#### Multiple forwarding rules

You can configure multiple forwarding rules, of which there can be two types:

  * **Multiple forwarding rules for the same IP address**. You can configure multiple forwarding rules for the same IP address as long as no two forwarding rules consume the same protocol and port combinations. Each forwarding rule can have a different backend service, or multiple forwarding rules can have the same backend service.

  * **Multiple forwarding rules that reference the same backend service**. You can configure multiple forwarding rules for the same backend service. Subject to the conditions noted in the first point, two or more forwarding rules can use the same IP address, or each forwarding rule can use a unique IP address.




When using multiple forwarding rules, make sure that you configure the application running on your backend VMs so that it binds to all the external IP address(es) of the load balancer's forwarding rule(s).

Configuring multiple forwarding rules can be useful for the following use cases:

  * You need to configure more than one external IP address for the same backend service. For example, one forwarding rule for an IPv4 address and another for an IPv6 address.
  * You need to configure multiple forwarding rules for the same external IP address but with different protocols or non-overlapping ports or port ranges. The forwarding rules can use the same or different backend services.



#### Multiple forwarding rules protocol and port constraints

Google Cloud selects at most one forwarding rule to process an incoming packet. Except for steering forwarding rules, which are discussed in the next section, two or more forwarding rules that use the same regional external IP address must have unique protocol and port combinations according to these constraints: 

  * **A forwarding rule configured for all ports of a protocol prevents the creation of other forwarding rules using the same protocol and IP address**.

Forwarding rules using `TCP` or `UDP` protocols can be configured to use all ports, or they can be configured for specific ports. For example, if you create a forwarding rule using IP address `198.51.100.1`, the `TCP` protocol, and all ports, you cannot create any other forwarding rule using IP address `198.51.100.1` and the `TCP` protocol. You can create two forwarding rules, both using the IP address `198.51.100.1` and the `TCP` protocol, if each one has unique ports or non-overlapping port ranges. For example, you can create two forwarding rules using IP address `198.51.100.1` and the `TCP` protocol, where one forwarding rule's ports are `80,443` and the other uses the port range `81-442`.

  * **Only one`L3_DEFAULT` forwarding rule can be created per IP address**.

This is because the `L3_DEFAULT` protocol uses all ports by definition. In this context, the all ports term includes protocols without port information.

  * **A single`L3_DEFAULT` forwarding rule can coexist with other forwarding rules that use specific protocols (`TCP` or `UDP`) and the same IP address**.

If you have specific TCP or UDP forwarding rules attached to an IP address, you can also attach an `L3_DEFAULT` forwarding rule to that same IP address to act as a fallback for any traffic that doesn't match the specific forwarding rules. An `L3_DEFAULT` forwarding rule processes packets sent to its destination IP address if and only if the packet's destination IP address, protocol, and destination port don't match a protocol-specific forwarding rule.  


To illustrate this, consider these two scenarios. Forwarding rules in both scenarios use the same IP address `198.51.100.1`.

    * **Scenario 1**. The first forwarding rule uses the `L3_DEFAULT` protocol. The second forwarding rule uses the `TCP` protocol and all ports. TCP packets sent to any destination port of `198.51.100.1` are processed by the second forwarding rule. Packets using different protocols are processed by the first forwarding rule.

    * **Scenario 2**. The first forwarding rule uses the `L3_DEFAULT` protocol. The second forwarding rule uses the `TCP` protocol and port `8080`. TCP packets sent to `198.51.100.1:8080` are processed by the second forwarding rule. All other packets, including TCP packets sent to _different_ destination ports, are processed by the first forwarding rule.




#### Forwarding rule selection

Google Cloud selects one or zero forwarding rules to process an incoming packet by using this elimination process, starting with the set of forwarding rule candidates which match the destination IP address of the packet:

  * Eliminate forwarding rules whose protocol doesn't match the packet's protocol, except for `L3_DEFAULT` forwarding rules. Forwarding rules using the `L3_DEFAULT` protocol are never eliminated by this step because `L3_DEFAULT` matches all protocols. For example, if the packet's protocol is TCP, only forwarding rules using the `UDP` protocol are eliminated.

  * Eliminate forwarding rules whose port doesn't match the packet's port. Forwarding rules configured for all ports are never eliminated by this step because an all ports forwarding rule matches any port.



  * If the remaining forwarding rule candidates include both `L3_DEFAULT` and protocol specific forwarding rules, eliminate the `L3_DEFAULT` forwarding rules. If the remaining forwarding rule candidates are all `L3_DEFAULT` forwarding rules, none are eliminated at this step.


  * At this point, the remaining forwarding rule candidates fall into one of the following categories:

    * A single forwarding rule remains which matches the packet's destination IP address, protocol, and port, and is used to route the packet.

    * Two or more forwarding rule candidates remain which match the packet's destination IP address, protocol, and port. This means the remaining forwarding rule candidates include steering forwarding rules (discussed in the next section). Select the steering forwarding rule whose _source_ range includes the most specific (longest prefix match) CIDR containing the packet's source IP address. If no steering forwarding rules have a source range including the packet's source IP address, select the parent forwarding rule.

    * Zero forwarding rule candidates remain and the packet is dropped.




#### Traffic steering

Forwarding rules for regional external passthrough Network Load Balancers can be configured to direct traffic coming from a specific source IP address or a range of IP addresses to a specific backend service (or target instance).

Traffic steering is useful for troubleshooting and for advanced configurations. With traffic steering, you can direct certain clients to a different set of backends, a different backend service configuration, or both. For example:

  * Traffic steering lets you create two forwarding rules which direct traffic to the same backend (instance group or NEG) by way of two backend services. The two backend services can be configured with different health checks, different session affinities, or different traffic distribution control policies (connection tracking, connection draining, and failover).
  * Traffic steering lets you create a forwarding rule to redirect traffic from a low-bandwidth backend service to a high-bandwidth backend service. Both backend services contain the same set of backend VMs or endpoints, but load-balanced with different weights using [weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#weighted-lb).
  * Traffic steering lets you create two forwarding rules which direct traffic to different backend services, with different backends (instance groups or NEGs). For example, one backend could be configured using different machine types in order to better process traffic from a certain source IP addresses.



Traffic steering is configured with a forwarding rule API parameter called `sourceIPRanges`. Forwarding rules that have at least one source IP range configured are called _steering forwarding rules_.

A steering forwarding rule can use the `sourceIPRanges` parameter to specify a comma-separated list of up to 64 source IP addresses or IP address ranges. You can update this list of source IP address ranges at any time.

Each steering forwarding rule requires that you first create a _parent forwarding rule_. The parent and steering forwarding rules share the same regional external IP address, IP protocol, and port information; however, the parent forwarding rule does not have any source IP address information. For example:

  * **Parent forwarding rule** : IP address: `198.51.100.1`, IP protocol: `TCP`, ports: 80
  * **Steering forwarding rule** : IP address: `198.51.100.1`, IP protocol: `TCP`, ports: 80, sourceIPRanges: `203.0.113.0/24`



A parent forwarding rule that points to a backend service can be associated with a steering forwarding rule that points to a backend service or a target instance.

For a given parent forwarding rule, two or more steering forwarding rules can have _overlapping, but not identical,_ source IP address ranges and IP addresses. As an example, one steering forwarding rule can have the source IP range `203.0.113.0/24` and another steering forwarding rule for the same parent can have the source IP address `203.0.113.0`.

You must delete all steering forwarding rules before you can delete the parent forwarding rule upon which they depend.

To learn how incoming packets are processed when steering forwarding rules are used, see Forwarding rule selection.

**Session affinity behavior across steering changes**

This section describes the conditions under which session affinity might break when the source IP address ranges configured for a steering forwarding rule are updated:

  * If an existing connection continues to match the same forwarding rule after you change the source IP ranges for a steering forwarding rule, session affinity doesn't break. If your change results in an existing connection matching a different forwarding rule, then:
  * Session affinity _always breaks_ under these circumstances: 
    * The newly matched forwarding rule directs an established connection to a backend service (or target instance) which doesn't reference the previously selected backend VM.
    * The newly matched forwarding rule directs an established connection to a backend service which does reference the previously selected backend VM, but the backend service is not configured to [persist connections when backends are unhealthy](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-persistence), and the backend VM fails the backend service's health check.
  * Session affinity _might break_ when the newly matched forwarding rule directs an established connection to a backend service, and the backend service does reference the previously selected VM, but the backend service's combination of session affinity and connection tracking mode results in a different connection tracking hash.



**Preserving session affinity across steering changes**

This section describes how to avoid breaking session affinity when the source IP ranges for steering forwarding rules are updated:

  * **Steering forwarding rules pointing to backend services**. If both the parent and the steering forwarding rule point to backend services, you'll need to manually make sure that the [session affinity](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#session-affinity) and [connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#tracking-policy) settings are _identical_. Google Cloud does not automatically reject configurations if they are not identical.
  * **Steering forwarding rules pointing to target instances**. A parent forwarding rule that points to a backend service can be associated with a steering forwarding rule that points to a target instance. In this case, the steering forwarding rule inherits [session affinity](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#session-affinity) and [connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#tracking-policy) settings from the parent forwarding rule.



For instructions on how to configure traffic steering, see [Configure traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-traffic-steering).

### Regional backend service

Each regional external passthrough Network Load Balancer has one regional backend service that defines the behavior of the load balancer and how traffic is distributed to its backends. The name of the backend service is the name of the regional external passthrough Network Load Balancer shown in the Google Cloud console.

Each backend service defines the following backend parameters:

  * **Protocol**. A backend service accepts traffic on the IP address and ports (if configured) specified by one or more regional external forwarding rules. The backend service passes packets to backend VMs while preserving the packet's source and destination IP addresses, protocol, and, if the protocol is port-based, the source and destination ports.

Backend services used with regional external passthrough Network Load Balancers support the following protocol options: `TCP`, `UDP`, or `UNSPECIFIED`.

Backend services with the `UNSPECIFIED` protocol can be used with any forwarding rule regardless of the forwarding rule protocol. Backend services with a specific protocol (`TCP` or `UDP`) can only be referenced by forwarding rules with the same protocol (`TCP` or `UDP`). Forwarding rules with the `L3_DEFAULT` protocol can only refer to backend services with the `UNSPECIFIED` protocol.

See Forwarding rule protocol specification for a table with possible forwarding rule and backend service protocol combinations.

  * **Traffic distribution**. A backend service allows traffic to be distributed according to the configured session affinity, connection tracking policy, and weighted load balancing settings. The backend service can also be configured to enable connection draining and designate failover backends for the load balancer. Most of these settings have default values that let you get started quickly. For more information, see [Traffic distribution for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution).

  * **Health check**. A backend service must have an associated regional health check.

  * **Backends**. Each backend service operates in a single region and distributes traffic to either instance groups or zonal NEGs in the same region. You can use either instance groups or zonal NEGs, but not a combination of both, as backends for a regional external passthrough Network Load Balancer:

    * If you choose instance groups, you can use unmanaged instance groups, zonal managed instance groups, regional managed instance groups, or a combination of instance group types.
    * If you choose zonal NEGs, you must use `GCE_VM_IP` zonal NEGs.

Each instance group or NEG backend has an associated VPC network, even if that instance group or NEG hasn't been connected to a backend service yet. For more information about how a network is associated with each type of backend, see [Instance group backends and network interfaces](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#ig-nic-net) and Zonal NEG backends and network interfaces.




#### Instance groups

A regional external passthrough Network Load Balancer distributes connections among backend VMs contained within managed or unmanaged instance groups. Instance groups can be regional or zonal in scope.

Each instance group has an associated VPC network, even if that instance group hasn't been connected to a backend service yet. For more information about how a network is associated with instance groups, see Instance group backends and network interfaces.

The regional external passthrough Network Load Balancer is highly available by design. There are no special steps needed to make the load balancer highly available because the mechanism doesn't rely on a single device or VM instance. You only need to make sure that your backend VM instances are deployed to multiple zones so that the load balancer can work around potential issues in any given zone.

  * **Regional managed instance groups**. Use regional managed instance groups if you can deploy your software by using instance templates. Regional managed instance groups automatically distribute traffic among multiple zones, providing the best option to avoid potential issues in any given zone.

An example deployment using a regional managed instance group is shown here. The instance group has an instance template that defines how instances should be provisioned, and each group deploys instances within three zones of the `us-central1` region.

[ ![Regional external passthrough Network Load Balancer with a regional managed instance group](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-regional.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-regional.svg) Regional external passthrough Network Load Balancer with a regional managed instance group
  * **Zonal managed or unmanaged instance groups**. Use zonal instance groups in different zones (in the same region) to protect against potential issues in any given zone.

An example deployment using zonal instance groups is shown here. This load balancer provides availability across two zones.

[ ![Regional external passthrough Network Load Balancer with zonal instance groups](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal.svg)](https://docs.cloud.google.com/static/load-balancing/images/network-load-balancer-zonal.svg) Regional external passthrough Network Load Balancer with zonal instance groups



#### Zonal NEGs

A regional external passthrough Network Load Balancer distributes connections among `GCE_VM_IP` endpoints contained within [zonal network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts). These endpoints must be located in the same region as the load balancer. For some recommended zonal NEG use cases, see [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#l4lb-zonal-neg).

Zonal NEGs support both IPv4 and dual-stack (IPv4 and IPv6) VMs. For both IPv4 and dual-stack VMs, it is sufficient to specify only the VM instance when attaching an endpoint to a NEG. You don't need to specify the endpoint's IP address. The VM instance must always be in the same zone as the NEG.

Each zonal NEG has an associated VPC network and a subnet, even if that zonal NEG hasn't been connected to a backend service yet. For more information about how a network is associated with zonal NEGs, see Zonal NEG backends and network interfaces.

#### Instance group backends and network interfaces

The VPC network and subnet that are associated with an instance group are set implicitly as described in [Instance group backends and network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-net-ig).

To distribute load-balanced traffic to a non-`nic0` load balancer target interface, you can't use instance group backends. Use zonal NEGs with `GCE_VM_IP` endpoints instead. For more information, see Backend services and VPC networks. 

#### Zonal NEG backends and network interfaces

The VPC network and subnet that are associated with a zonal NEG with `GCE_VM_IP` endpoints are set when the NEG is created. For more information and rules for endpoints, see [`GCE_VM_IP` zonal NEG backends and network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-net-neg-vm-ip).

#### Backend services and VPC networks

The backend service isn't associated with any VPC network; however, each backend instance group or zonal NEG is associated with a VPC network, as noted previously. As long as all backends are located in the same region and project, and as long as all backends are of the same type (instance groups or zonal NEGs), the load balancer and its backends can be either in the same or different VPC networks.

To distribute packets to non-`nic0` interfaces, you must meet both of the following requirements:

  * You must use zonal NEGs (with `GCE_VM_IP` endpoints), not instance groups.

  * The non-`nic0` interface must be a [load balancer target interface](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#load-balancers). For more information, see [`GCE_VM_IP` zonal NEG backends and network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-net-neg-vm-ip).




#### Dual-stack backends (IPv4 and IPv6)

If you want the load balancer to use dual-stack backends that handle both IPv4 and IPv6 traffic, note the following requirements:

  * Backends must be configured in [dual-stack subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6) that are in the same region as the load balancer's IPv6 forwarding rule. For the backends, you can use a subnet with the `ipv6-access-type` set to either `EXTERNAL` or `INTERNAL`. If the backend subnet's `ipv6-access-type` is set to `INTERNAL`, you must use a different IPv6-only subnet or dual-stack subnet with `ipv6-access-type` set to `EXTERNAL` for the load balancer's external forwarding rule.
  * Backends must be configured to be dual-stack with `stack-type` set to `IPV4_IPV6`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, you must also set the `--ipv6-network-tier` to `PREMIUM` or `STANDARD` ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). For instructions, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).



#### IPv6-only backends

If you want the load balancer to use IPv6-only backends, note the following requirements:

  * IPv6-only instances are supported in managed and unmanaged instance groups. No other backend type is supported.
  * Backends must be configured in either [dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6) or [IPv6-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only) that are in the same region as the load balancer's IPv6 forwarding rule. For the backends, you can use a subnet with the `ipv6-access-type` set to either `INTERNAL` or `EXTERNAL`. If the backend subnet's `ipv6-access-type` is set to `INTERNAL`, you must use a different IPv6-only subnet with `ipv6-access-type` set to `EXTERNAL` for the load balancer's external forwarding rule.
  * Backends must be configured to be IPv6-only with the VM `stack-type` set to `IPV6_ONLY`. If the backend subnet's `ipv6-access-type` is set to `EXTERNAL`, then the `--ipv6-network-tier` must match the IPv6 network tier of the subnet that the VM belongs to. For instructions, see [Create an instance template with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#template-ipv6).



Note that IPv6-only VMs can be created under both dual-stack and IPv6-only subnets, but dual-stack VMs can't be created under IPv6-only subnets.

### Health checks

Health check information is used to [determine eligible backends for new connections](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#id-eligible-backends), and to [control whether existing connections persist on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-persistence). 

#### Health check type, protocol, and port

The load balancer's backend service must reference a regional health check, using any supported health check protocol and port. The health check protocol and port details don't have to match the forwarding rule protocol and port information. 

Because all supported health check protocols rely on TCP (UDP health checks are not supported), when you use a regional external passthrough Network Load Balancer to balance connections and traffic for other protocols, backend VMs must run a TCP-based server to answer health check probers. For example, you can use an HTTP health check combined with running an HTTP server on each backend VM. In this example, your scripts or software are responsible for configuring the HTTP server so that it returns status `200` only when the software listening to load-balanced connections is operational.

For more information about supported health check protocols and ports, see [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports) and [How health checks work](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#method).

#### Health check packets

For instance group backends, health check probers send packets to the `nic0` network interface of each backend VM. For `GCE_VM_IP` zonal NEG backends, health check probers send packets to the network interface in the VPC subnetwork of the NEG. Health check packets have the following characteristics:

  * Source IP address from the relevant health check [probe IP range](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges-passthrough).


  * Destination IP address that matches each IP address of a forwarding rule that references the regional external passthrough Network Load Balancer backend service.


  * Destination port that matches the port number you specify in the health check.



Applications running on the backend VMs must bind to and listen on relevant IP address and port combinations. To accomplish this, configure the application to bind to and listen on the relevant ports of any of the VM's IP addresses (`0.0.0.0` or `::/0`). For more information, see [Destination for probe packets](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#hc-packet-dest).

### Firewall rules

Because a regional external passthrough Network Load Balancer is not a proxy, it passes traffic to backend VMs without modifying their source and destination IP addresses, protocol, and ports, if the protocol carries port information. Therefore, you must create ingress allow [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or an ingress allow [hierarchical firewall policy](https://docs.cloud.google.com/vpc/docs/firewall-policies) to control access to the load balancer's backend VMs, specifically, to permit health checks and the traffic that you're load balancing. Otherwise, the [implied deny ingress firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) blocks incoming packets from all external source IP addresses.

Forwarding rules and ingress allow firewall rules or Hierarchical firewall policies work together in the following way: a forwarding rule specifies the destination IP address, protocol and, if defined, port requirements that a packet must meet to be forwarded to a backend VM. Ingress allow firewall rules control whether the firewall delivers the forwarded packets to the VM or drops it. The Google Cloud default VPC network includes a limited set of [pre-populated ingress allow firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc).

  * To accept traffic from any IP address on the internet, you must create an ingress allow firewall rule with the `0.0.0.0/0` or `::/0` source range. To only allow traffic from certain IP address ranges, use more restrictive source ranges.

  * As a security best practice, your ingress allow firewall rules should only permit the [IP protocols and ports](https://docs.cloud.google.com/vpc/docs/firewalls#protocols_and_ports) that you need. Restricting the protocol (and, if possible, port) configuration is especially important when using forwarding rules whose protocol is set to `L3_DEFAULT`. `L3_DEFAULT` forwarding rules forward packets for all supported IP protocols (on all ports if the protocol and packet have port information).

  * Regional external passthrough Network Load Balancers use Google Cloud health checks. Therefore, you must always allow traffic from the [health check IP address ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges-passthrough). You can configure these ingress allow firewall rules specific to the protocol and ports of the load balancer's health check.




### IP addresses for request and return packets

When a backend VM receives a load-balanced packet from a client, the packet's source and destination are as follows:

  * **Source** : an external IP address associated with the client, a Google Cloud VM or a system on the internet.
  * **Destination** : the IP address of the load balancer's forwarding rule.

Because the load balancer is a passthrough load balancer (not a proxy), packets arrive bearing the IP address of the load balancer's forwarding rule. 

Although the guest environment automatically configures local routes so that the VM's operating system accepts traffic destined for the load balancer's IP address, the operating system cannot deliver these packets to your application if the application is configured to listen only on the VM's assigned internal IP address.

To ensure that the operating system delivers packets to your application, configure the application running on backend VMs to do the following:

  * Listen on (bind to) the load balancer's forwarding rule IP address or any IP address (`0.0.0.0` or `::`)


  * If the load balancer forwarding rule's protocol supports ports, listen on (bind to) a port that's included in the load balancer's forwarding rule



Return packets are sent directly from the load balancer's backend VMs to the client. The return packet's source IP address depends on the protocol:

  * TCP is connection-oriented so backend VMs must reply with packets whose source IP addresses match the destination IP address of the requesting packet so that the client can associate the response packets with the appropriate TCP connection.
  * UDP, ESP, GRE, ICMP, and ICMPv6 are connectionless. Backend VMs can send response packets whose source IP addresses either match the forwarding rule's IP address or match any assigned external IP address for the VM. Practically speaking, most clients expect the response to come from the same IP address to which they sent packets.



The following table summarizes the source and destination IP addresses for response packets:

Traffic type | Source | Destination  
---|---|---  
TCP | The requesting packet's destination | The requesting packet's source  
UDP, ESP, GRE, ICMP, and ICMPv6 | For most use cases, the requesting packet's destination1 | The requesting packet's source  
  
1 When a VM has an external IP address or when you are using Cloud NAT, it is also possible to set the response packet's source IP address to the VM NIC's primary internal IPv4 address. Google Cloud or Cloud NAT changes the response packet's source IP address to either the NIC's external IPv4 address or a Cloud NAT external IPv4 address in order to send the response packet to the client's external IP address. Not using the forwarding rule's IP address as a source is an advanced scenario because the client receives a response packet from an external IP address that doesn't match the IP address to which it sent a request packet.

### Return path

Regional external passthrough Network Load Balancers use [special routes](https://docs.cloud.google.com/vpc/docs/routes#health_checks_for_all_load_balancer_types) outside of your VPC network to direct incoming requests and health check probes to each backend VM.

The load balancer preserves the source IP addresses of packets. Responses from the backend VMs go directly to the clients, not back through the load balancer. The industry term for this is _direct server return_.

### Outbound internet connectivity from backends

VM instances configured as a regional external passthrough Network Load Balancer's backend endpoints can initiate connections to the internet using the load balancer's forwarding rule IP address as the source IP address of the outbound connection.

Generally, a VM instance always uses its own external IP address or Cloud NAT to initiate connections. You use the forwarding rule IP address to initiate connections from backend endpoints only in special scenarios such as when you need VM instances to originate and receive connections at the same external IP address, and you also need the backend redundancy provided by the regional external passthrough Network Load Balancer for inbound connections.

Outbound packets sent from backend VMs directly to the internet have no restrictions on traffic protocols and ports. Even if an outbound packet is using the forwarding rule's IP address as the source, the packet's protocol and source port don't have to match the forwarding rule's protocol and port specification. However, inbound response packets must match the forwarding rule IP address, protocol, and destination port of the forwarding rule. For more information, see [Paths for regional external passthrough Network Load Balancers and external protocol forwarding](https://docs.cloud.google.com/vpc/docs/routes#paths_to_backends).

Additionally, any responses to the VM's outbound connections are subject to load balancing, just like all the other incoming packets meant for the load balancer. This means that responses might not arrive on the same backend VM that initiated the connection to the internet. If the outbound connections and load balanced inbound connections share common protocols and ports, then you can try one of the following suggestions:

  * Synchronize outbound connection state across backend VMs, so that connections can be served even if responses arrive at a backend VM other than the one that has initiated the connection.

  * Use a [failover configuration](https://docs.cloud.google.com/load-balancing/docs/network/networklb-failover-overview), with a single primary VM and a single backup VM. Then, the active backend VM that initiates the outbound connections always receives the response packets.




This path to internet connectivity from a regional external passthrough Network Load Balancer's backends is the default intended behavior according to Google Cloud's [implied firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules). However, if you have security concerns about leaving this path open, you can use targeted egress firewall rules to block unsolicited outbound traffic to the internet.

## Shared VPC architecture

Note the following points in relation to a [Shared VPC architecture](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) for a regional external passthrough Network Load Balancer:

  * Except for the IP address resource, all other resources associated with a regional external passthrough Network Load Balancer—forwarding rule, backend service, health check, and backend groups (instance groups or NEGs)—must exist in the same project, and this project can be a host project or a service project.

  * If the load balancing resources exist in the host project, then the IP address resource must also exist in the host project.

  * If the load balancing resources exist in a service project, then the IP address resource can be either in the same service project, or in the host project.




The following table outlines where the different components of a regional external passthrough Network Load Balancer exist in a Shared VPC architecture.

Location of load balancing resources1 | Required location of IP address resource  
---|---  
Host project | Host project  
Service project | Service project _or_ host project  
  
1 Includes the forwarding rule, backend service, health check, and backends (instance groups or NEGs)

## Traffic distribution

Regional external passthrough Network Load Balancers support a variety of traffic distribution customization options, including session affinity, connection tracking, weighted load balancing, and failover. For details about how regional external passthrough Network Load Balancers distribute traffic, and how these options interact with each other, see [Traffic distribution for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution).

## Limitations

  * You cannot use the Google Cloud console to do the following tasks:

    * Create or modify a regional external passthrough Network Load Balancer whose forwarding rule uses the `L3_DEFAULT` protocol.
    * Create or modify a regional external passthrough Network Load Balancer whose backend service protocol is set to `UNSPECIFIED`.
    * Create or modify a regional external passthrough Network Load Balancer that configures a connection tracking policy.
    * Create or modify source IP-based traffic steering for a forwarding rule.

Use either the Google Cloud CLI or the REST API instead.

  * Regional external passthrough Network Load Balancers don't support VPC Network Peering.

  * For Dynamic NICs, you must manually add local routes for forwarding rule IP addresses as described in the following known issue: [Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dropped-packets-dynamic-nics).




## Pricing

For pricing information, see [Network pricing: Cloud Load Balancing](https://cloud.google.com/vpc/network-pricing#cloud-load-balancing).

## What's next

  * To configure a regional external passthrough Network Load Balancer with a backend service for TCP or UDP traffic only (supporting IPv4 and IPv6 traffic), see [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service).
  * To configure a regional external passthrough Network Load Balancer for multiple IP protocols (supporting IPv4 and IPv6 traffic), see [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols).
  * To configure a regional external passthrough Network Load Balancer with a zonal NEG backend, see [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg)
  * To configure a regional external passthrough Network Load Balancer with a _target pool_ , see [Set up a regional external passthrough Network Load Balancer with a target pool](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network).
  * To learn how to transition a regional external passthrough Network Load Balancer from a target pool backend to a regional backend service, see [Transitioning a regional external passthrough Network Load Balancer from a target pool to a backend service](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services).
  * To use prebuilt Terraform templates to streamline the setup and management of Google Cloud's networking infrastructure, explore the [Simplified Cloud Networking Configuration Solutions GitHub repository](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
