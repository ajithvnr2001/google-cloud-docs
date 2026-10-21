---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy/
title: Internal proxy Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:23.555907+00:00
---

# Internal proxy Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal proxy Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud internal proxy Network Load Balancer is a proxy-based load balancer powered by [open source Envoy proxy software](https://www.envoyproxy.io/) and [the Andromeda network virtualization stack](https://www.usenix.org/system/files/conference/nsdi18/nsdi18-dalton.pdf).

The internal proxy Network Load Balancer is a Layer 4 load balancer that lets you run and scale your TCP service traffic behind a regional internal IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network. The load balancer first terminates the TCP connection between the client and the load balancer at an Envoy proxy. The proxy opens a second TCP connection to backends hosted in Google Cloud, on-premises, or other cloud environments. For more use cases, see [Proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer).

## Modes of operation

You can configure an internal proxy Network Load Balancer in the following modes:

  * **Regional internal proxy Network Load Balancer**. This is a regional load balancer that is implemented as a managed service based on the open source [Envoy proxy](https://www.envoyproxy.io/). With regional mode, all clients and backends are from a specified region, which helps when you need regional compliance.

  * **Cross-region internal proxy Network Load Balancer**. This is a multi-region load balancer that is implemented as a managed service based on the open source [Envoy proxy](https://www.envoyproxy.io/). The cross-region mode lets you load balance traffic to backend services that are globally distributed with backends in multiple regions, including traffic management that ensures traffic is directed to the closest backend. This load balancer also enables high availability. Placing backends in multiple regions helps avoid failures in a single region. If one region's backends are down, traffic can fail over to another region. The load balancer's forwarding rule IP addresses are always accessible in all regions.

The following table describes the important differences between regional and cross-region modes:

Feature | Regional internal proxy Network Load Balancer | Cross-region internal proxy Network Load Balancer  
---|---|---  
Virtual IP address (VIP) of the load balancer. | Allocated from a subnet in a specific Google Cloud region. | Allocated from a subnet in a specific Google Cloud region. VIP addresses from multiple regions can share the same global backend service.  
Client access | Not globally accessible by default.  
You can optionally [ enable global access.](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#client-access) | Always globally accessible. Clients from any Google Cloud region can send traffic to the load balancer.   
Load balanced backends | Regional backends.  
Load balancer can only send traffic to backends that are in the same region as the proxy of the load balancer. | Global backends.  
Load balancer can send traffic to backends in any region.  
High availability and failover | Automatic failover to healthy backends in the same region. | Automatic failover to healthy backends in the same or different regions.  



### Identify the mode

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

  2. In the **Load Balancers** tab, you can see the load balancer type, protocol, and region. If the region is blank, then the load balancer is in the cross-region mode. The following table summarizes how to identify the mode of the load balancer. 

Load balancer mode | Load balancer type | Access type | Region  
---|---|---|---  
Regional internal proxy Network Load Balancer | Network (Proxy) | Internal | Specifies a region   
Cross-region internal proxy Network Load Balancer | Network (Proxy) | Internal |   



###  gcloud 

To determine the mode of a load balancer, run the following command:
    
    
    gcloud compute forwarding-rules describe FORWARDING_RULE_NAME
    

In the command output, check the load balancing scheme, region, and network tier. The following table summarizes how to identify the mode of the load balancer.

Load balancer mode | Load balancing scheme | Forwarding rule  
---|---|---  
Regional internal proxy Network Load Balancer | INTERNAL_MANAGED | Regional  
Cross-region internal proxy Network Load Balancer | INTERNAL_MANAGED | Global  
  
**Important:** After you create a load balancer, you can't edit its mode. Instead, you must delete the load balancer and create a new one.

## Architecture

The following diagram shows the Google Cloud resources required for internal proxy Network Load Balancers.

###  Regional 

This diagram shows the components of a regional internal proxy Network Load Balancer deployment in Premium Tier.

[ ![Components of a Regional internal proxy Network Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-simple.svg)](https://docs.cloud.google.com/static/load-balancing/images/int-tcp-proxy-simple.svg) Regional internal proxy Network Load Balancer components (click to enlarge).

###  Cross-region 

This diagram shows the components of a cross-region internal proxy Network Load Balancer deployment in Premium Tier within the same VPC network. Each global forwarding rule uses a regional IP address that the clients use to connect.

[ ![Components of a Cross-region internal proxy Network Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-lb.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-lb.svg) Cross-region internal proxy Network Load Balancer components (click to enlarge).

### Proxy-only subnet

**Preview — Cross-region, regional external, and regional internal proxy Network Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In the previous diagram, the [_proxy-only subnet_](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) provides a set of IP addresses that Google uses to run Envoy proxies on your behalf. You must create a proxy-only subnet in each region of a VPC network where you use an Envoy-based internal proxy Network Load Balancer.

The following table describes proxy-only subnet requirements for internal proxy Network Load Balancers:

Load balancer mode | Value of the `--purpose` flag | Value of the `--stack-type` flag  
---|---|---  
Regional internal proxy Network Load Balancer |  `REGIONAL_MANAGED_PROXY` Regional and cross-region load balancers can't share the same subnets All the regional Envoy-based load balancers in a region and VPC network share the same proxy-only subnet. | 

  * `IPV4_IPV6` to terminate incoming IPv6 or IPv4 traffic
  * `IPV4_ONLY` to terminate incoming IPv4 traffic

  
Cross-region internal proxy Network Load Balancer |  `GLOBAL_MANAGED_PROXY` Regional and cross-region load balancers can't share the same subnets The cross-region Envoy-based load balancer must have a proxy-only subnet in each region in which the load balancer is configured. Cross-region load balancer proxies in the same region and network share the same proxy-only subnet. | 

  * `IPV4_IPV6` to terminate incoming IPv6 or IPv4 traffic
  * `IPV4_ONLY` to terminate incoming IPv4 traffic

  
  
Further:

  * Proxy-only subnets are _only_ used for Envoy proxies, not your backends.
  * Backend virtual machine (VM) instances or endpoints of all internal proxy Network Load Balancers in a region and VPC network receive connections from the proxy-only subnet.
  * The IP address of an internal proxy Network Load Balancer is _not_ located in the proxy-only subnet. The load balancer's IP address is defined by its internal managed forwarding rule.



### Forwarding rules and IP addresses

**Preview — Cross-region, regional external, and regional internal proxy Network Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) route traffic by IP address, port, and protocol to a load balancing configuration consisting of a target proxy and a backend service.

**IP address specification**. Each forwarding rule references a single regional IP address that you can use in DNS records for your application. You can either reserve a static IP address that you can use or let Cloud Load Balancing assign one for you. We recommend that you reserve a static IP address; otherwise, you must update your DNS record with the newly assigned ephemeral IP address whenever you delete a forwarding rule and create a new one.

Clients use the IP address and port to connect to the load balancer's Envoy proxies—the forwarding rule's IP address is the IP address of the load balancer (sometimes called a virtual IP address or VIP). Clients connecting to a load balancer must use TCP. For the complete list of supported protocols, see [Load balancer feature comparison](https://docs.cloud.google.com/load-balancing/docs/features#protocols_from_the_clients_to_the_load_balancer).

The internal IP address associated with the forwarding rule can come from a subnet in the same network and region as your backends.

**Port specification**. Each forwarding rule that you use in an internal proxy Network Load Balancer can reference a [single port from 1-65535](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). To support multiple ports, you must configure multiple forwarding rules.

The following table shows the forwarding rule requirements for internal proxy Network Load Balancers:

Load balancer mode | Forwarding rule, IP address, and proxy-only subnet `--purpose` | Routing from the client to the load balancer's frontend  
---|---|---  
Regional internal proxy Network Load Balancer | [Regional `forwardingRules`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert) [Regional IP address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert) Load balancing scheme:`INTERNAL_MANAGED` Proxy-only subnet `--purpose`:`REGIONAL_MANAGED_PROXY` IP address `--purpose`:`SHARED_LOADBALANCER_VIP` |  You can enable global access to allow clients from any region to access your load balancer. Backends must also be in the same region as the load balancer.  
Cross-region internal proxy Network Load Balancer | [Global `globalForwardingRules`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules/insert) [Regional IP addresses](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert) Load balancing scheme:`INTERNAL_MANAGED` Proxy-only subnet `--purpose`:`GLOBAL_MANAGED_PROXY` IP address `--purpose`:`SHARED_LOADBALANCER_VIP` | Global access is enabled by default to allow clients from any region to access your load balancer. Backends can be in multiple regions.  
  
  
#### Forwarding rules and VPC networks

This section describes how forwarding rules used by external Application Load Balancers are associated with VPC networks.

Load balancer mode | VPC network association  
---|---  
  
  * Regional internal proxy Network Load Balancer
  * Cross-region internal proxy Network Load Balancer

| Depending on whether you use an IPv4 address or an IPv6 address range, there is always an explicit or implicit VPC network associated with the forwarding rule.

  * Regional internal IPv4 addresses always exist inside VPC networks. When you create the forwarding rule, you're required to specify the subnet from which the internal IP address is taken. This subnet must be in the same region and VPC network where a proxy-only subnet has been created. Thus, there is an implied network association.
  * Regional internal IPv6 address ranges always exist inside a VPC network. When you create the forwarding rule, you're required to specify the subnet from which the IP address range is taken. This subnet must be in the same region and VPC network where a proxy-only subnet has been created. Thus, there is an implied network association. **Network and subnet requirements.** For IPv6 traffic, your network and subnets must meet the following configuration requirements:
    * VPC network: you must use a custom mode VPC network configured with the `--enable-ula-internal-ipv6` flag.
    * Forwarding rule subnet: this subnet must be a dual-stack (`IPv4_IPv6`) or `IPV6_ONLY` subnet with the `ipv6-access-type` set to `INTERNAL`.
**IPv6 address allocation options.** The forwarding rule must also reference a `/96` range of IPv6 addresses from the subnet's `/64` internal IPv6 address range. You can assign this `/96` range using one of the following methods:
    * Specifying a reserved internal IPv6 address.
    * Specifying a custom ephemeral IPv6 address.
    * Letting Google Cloud automatically assign an ephemeral IPv6 address.
**Limitations.** To specify a custom ephemeral IPv6 address, you must use the Google Cloud CLI or the API. The Google Cloud console doesn't support specifying custom ephemeral IPv6 addresses for forwarding rules.

  
  
### Target proxies

The internal proxy Network Load Balancer terminates TCP connections from the client and creates new connections to the backends. By default, the original client IP address and port information isn't preserved. You can preserve this information by using the [PROXY protocol](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol). The [target proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies) routes incoming requests directly to the load balancer's backend service.

The following table shows the target proxy APIs required by internal proxy Network Load Balancers:

Load balancer mode | Target proxy | Reference  
---|---|---  
Regional internal proxy Network Load Balancer | [Regional `regionTargetTcpProxies`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies) | Target proxy references either a single backend service or one or more TLS routes.  
Cross-region internal proxy Network Load Balancer | [Global `targetTcpProxies`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies) | Target proxy references either a single backend service or one or more TLS routes.  
  
### TLS routes

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A [TLS route](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes) resource lets you define how traffic is routed to backend services based on SNI hostnames.

If the load balancer's target TCP proxy is not referenced by a TLS route, then only the single default backend service is used, and the value of SNI hostname sent by the client or its absence isn't relevant.

You can attach a TLS route configuration to a load balancer's target proxy by using the [gcloud network-services tls-routes](https://cloud.google.com/sdk/gcloud/reference/network-services/tls-routes) commands.

The following table shows the TLS routes APIs required by internal proxy Network Load Balancers:

Load balancer mode | TLS route | Reference  
---|---|---  
Regional internal proxy Network Load Balancer | [Regional `tlsRoutes`](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes) | Each TLS route can reference one or more backend services.  
Cross-region internal proxy Network Load Balancer | [Global `tlsRoutes`](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes) | Each TLS route can reference one or more backend services.  
  
### Backend service

A [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) directs incoming traffic to one or more attached backends. A backend is either an instance group or a network endpoint group. The backend contains balancing mode information to define fullness based on connections (or, for instance group backends only, utilization).

Each load balancer has at least one backend service resource. If you use TLS routes to configure routing, you can configure multiple backend services for your load balancer. Without TLS routes, you're limited to only a single backend service per load balancer.

The following table specifies the backend service APIs for internal proxy Network Load Balancers:

Load balancer mode | Backend service type  
---|---  
Regional internal proxy Network Load Balancer | [Regional `regionBackendServices`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices)  
Cross-region internal proxy Network Load Balancer | [Global `backendServices`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)  
  
#### Supported backends

The internal proxy Network Load Balancer supports the following types of backends:

Load balancer mode | Supported backends on a backend service  
---|---  
Instance groups | Zonal NEGs | Internet NEGs | Serverless NEGs | Hybrid NEGs | Private Service Connect NEGs | GKE  
Regional internal proxy Network Load Balancer |  |    
`GCE_VM_IP_PORT` type endpoints | Regional NEGs only |  |  | [ Add a Private Service Connect NEG](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-tcp-proxy-lb) |   
Cross-region internal proxy Network Load Balancer |  |    
`GCE_VM_IP_PORT` type endpoints |  |  |  | [ Add a Private Service Connect NEG](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#add-neg-tcp-proxy-lb) |   
  
All of the backends must be of the same type (instance groups or NEGs). You can simultaneously use different types of instance group backends, or you can simultaneously use different types of NEG backends, but you can't use instance group and NEG backends together on the same backend service.

You can mix zonal NEGs and hybrid NEGs within the same backend service.

To minimize service interruptions to your users, enable connection draining on backend services. Such interruptions can happen when a backend is terminated, removed manually, or removed by an autoscaler. To learn more about using connection draining to minimize service interruptions, see [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining).

#### Backends and VPC networks

  * For instance groups, zonal NEGs, and hybrid connectivity NEGs, all backends must be located in the same project and region as the backend service. However, a load balancer can reference a backend that uses a different VPC network in the same project as the backend service. Connectivity between the load balancer's VPC network and the backend VPC network can be configured using either VPC Network Peering, Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or a Network Connectivity Center framework. 

**Backend network definition**

    * For zonal NEGs and hybrid NEGs, you explicitly specify the VPC network when you create the NEG.
    * For managed instance groups, the VPC network is defined in the instance template.
    * For unmanaged instance groups, the instance group's VPC network is set to match the VPC network of the `nic0` interface for the first VM added to the instance group.

**Backend network requirements**

Your backend's network must satisfy _one of the following_ network requirements:

    * The backend's VPC network must exactly match the forwarding rule's VPC network.

    * The backend's VPC network must be connected to the forwarding rule's VPC network using VPC Network Peering. You must configure subnet route exchanges to allow communication between the proxy-only subnet in the forwarding rule's VPC network and the subnets used by the backend instances or endpoints.

**Backend IPv6 subnet requirements**

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The IP version used for the frontend connection is independent of the backend connection. Since the proxy-only subnet is [dual-stack (IPV4_IPV6)](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#dual_stack_proxy_only), the proxy-only subnet can communicate with backends using either IPv4 or IPv6.

If your backend instances are handling IPv6 traffic, the backend subnet can be configured with a stack type of `IPV4_ONLY` or `IPV4_IPV6` (dual-stack). If the backend subnet's stack type includes IPv6, you must explicitly set the subnet's ipv6-access-type to `INTERNAL`.



  * Both the backend's VPC network and the forwarding rule's VPC network must be [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview) attached to the same [NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). Import and export filters must allow communication between the proxy-only subnet in the forwarding rule's VPC network and the subnets used by backend instances or endpoints.


  * For all other backend types, all backends must be located in the same VPC network and region.




#### Backends and network interfaces

If you use instance group backends, packets are always delivered to `nic0`. If you want to send packets to non-`nic0` interfaces (either [vNICs or Dynamic Network Interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types)), use NEG backends instead.

If you use zonal NEG backends, packets are sent to whatever network interface is represented by the endpoint in the NEG. The NEG endpoints must be in the same VPC network as the NEG's explicitly defined VPC network.

#### Protocol for communicating with the backends

When you configure a backend service for an internal proxy Network Load Balancer, you set the protocol that the backend service uses to communicate with the backends. The load balancer uses only the protocol that you specify, and doesn't attempt to negotiate a connection with the other protocol. The internal proxy Network Load Balancers only support TCP for communicating with the backends.

### Health check

Each backend service specifies a health check that periodically monitors the backends' readiness to receive a connection from the load balancer. This reduces the risk that requests might be sent to backends that can't service the request. Health checks don't check if the application itself is working.

#### Health check protocol

Although it is not required and not always possible, it is a best practice to use a health check whose protocol matches the [protocol of the backend service](https://docs.cloud.google.com/load-balancing/docs/features#protocol-to-backends). For example, a TCP health check most accurately tests TCP connectivity to backends. For the list of supported health check protocols, see the [Health checks](https://docs.cloud.google.com/load-balancing/docs/features#health-checks) section of the Load balancer feature comparison page.

The following table specifies the scope of health checks supported by internal proxy Network Load Balancers in each mode:

Load balancer mode | Health check type  
---|---  
Regional internal proxy Network Load Balancer  | [Regional `regionHealthChecks`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)  
Cross-region internal proxy Network Load Balancer | [Global `healthChecks`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks)  
  
For more information about health checks, see the following:

  * [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts)
  * [Use health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks)



### Firewall rules

Internal proxy Network Load Balancers require the following firewall rules:

  * An ingress allow rule that permits traffic from the Google health check probes. For more information about the specific health check probe IP address ranges and why it's necessary to allow traffic from them, see [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).
  * An ingress allow rule that permits traffic from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).



The ports for these firewall rules must be configured as follows:

  * Allow traffic to the destination port for each backend service's health check.

  * For instance group backends: Determine the ports to be configured by the mapping between the backend service's [named port](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports) and the port numbers associated with that named port on each instance group. The port numbers can vary among instance groups assigned to the same backend service.

  * For `GCE_VM_IP_PORT` NEG backends, allow traffic to the port numbers of the endpoints.




There are certain exceptions to the firewall rule requirements for these load balancers:

  * Allowing traffic from Google's health check probe ranges isn't required for hybrid NEGs. However, if you're using a combination of hybrid and zonal NEGs in a single backend service, you need to allow traffic from the [Google health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) for the zonal NEGs. 
  * For regional internet NEGs, health checks are optional. Traffic from load balancers using _regional_ internet NEGs originates from the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) and is then NAT-translated (by using Cloud NAT) to either manually or automatically allocated NAT IP addresses. This traffic includes both health check probes and user requests from the load balancer to the backends. For details, see [Regional NEGs: Use a Cloud NAT gateway](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts#nat-support). 



Use Cloud NGFW firewall policy rules to control client access to the forwarding rules of Envoy proxy-based load balancers, such as regional internal proxy Network Load Balancers and cross-region internal proxy Network Load Balancers. Both Cloud NGFW Essentials and Cloud NGFW Standard support these features.

For more information, see [Use regional network firewall policies to protect internal Application Load Balancers and internal proxy Network Load Balancers](https://docs.cloud.google.com/firewall/docs/regional-network-app-lb).

### Client access

Clients can be in the same network or in a VPC network connected by using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

For regional internal proxy Network Load Balancers, clients must be in the same region as the load balancer by default. You can [enable global access](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#global-access) to allow clients from any region to access your load balancer.

For cross-region internal proxy Network Load Balancers, global access is enabled by default. Clients from any region can access your load balancer.

The following table summarizes client access for regional internal proxy Network Load Balancers:

Global access disabled | Global access enabled  
---|---  
Clients must be in the same region as the load balancer. They also must be in the same VPC network as the load balancer or in a VPC network that is connected to the load balancer's VPC network by using VPC Network Peering. | Clients can be in any region. They still must be in the same VPC network as the load balancer or in a VPC network that's connected to the load balancer's VPC network by using VPC Network Peering.  
On-premises clients can access the load balancer through [Cloud VPN tunnels or VLAN attachments](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks#using-vpn-interconnect). These tunnels or attachments must be in the same region as the load balancer. | On-premises clients can access the load balancer through Cloud VPN tunnels or VLAN attachments. These tunnels or attachments can be in any region.  
  
## Shared VPC architecture

The internal proxy Network Load Balancer supports networks that use Shared VPC. Shared VPC lets you maintain a clear separation of responsibilities between network administrators and service developers. Your development teams can focus on building services in service projects, and the network infrastructure teams can provision and administer load balancing. If you're not already familiar with Shared VPC, read the [Shared VPC overview documentation](https://docs.cloud.google.com/vpc/docs/shared-vpc).

IP address | Forwarding rule | Target proxy | Backend components  
---|---|---|---  
An internal IP address must be defined in the same project as the backends. For the load balancer to be available in a Shared VPC network, the internal IP address _must_ be defined in the same service project where the backend VMs are located, _and_ it must reference a subnet in the desired Shared VPC network in the host project. The address itself comes from the primary IP range of the referenced subnet. | An internal forwarding rule must be defined in the same project as the backends. For the load balancer to be available in a Shared VPC network, the internal forwarding rule _must_ be defined in the same service project where the backend VMs are located, _and_ it must reference the same subnet (in the Shared VPC network) that the associated internal IP address references. | The target proxy must be defined in the same project as the backends. | In a Shared VPC scenario, the backend VMs are typically located in a service project. A regional internal backend service and health check must be defined in that service project.  
  
## Traffic distribution

An internal proxy Network Load Balancer distributes traffic to its backends as follows:

  1. Connections originating from a single client are sent to the same zone as long as healthy backends (instance groups or NEGs) within that zone are available and have capacity, as determined by the [balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution). For regional internal proxy Network Load Balancers, the balancing mode can be `CONNECTION` (instance group or NEG backends) or `UTILIZATION` (instance group backends only).
  2. Connections from a client are sent to the same backend if you have configured session affinity.
  3. After a backend is selected, traffic is then distributed among instances (in an instance group) or endpoints (in a NEG) according to a load balancing policy. For the load balancing policy algorithms supported, see the `localityLbPolicy` setting in the [regional backend service API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices).



### SNI-based routing with TLS routes

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

SNI-based routing lets your TCP proxy Network Load Balancers route traffic to specific backend services based on the Server Name Indication (SNI) hostname provided during the TLS handshake. SNI is a TLS extension that allows a client to specify the domain name it wants to reach before the encrypted tunnel is established. The SNI hostname is transmitted in an unencrypted format within the `ClientHello` message so that the load balancer can inspect this value and route traffic to the appropriate backend service.

You can use a TLS route configuration resource to map specific SNI hostnames to backend services. When SNI-based routing is configured, the load balancer enables _TLS passthrough_ , where the encrypted byte stream is passed directly to the backend without being decrypted by the load balancer.

This feature unlocks some key use-cases such as:

  * Use a single global anycast IP address and port to serve multiple applications, reducing IPv4 address consumption.
  * Supports end-to-end encrypted deployments where certificates can remain on the backends, ensuring that traffic is never unencrypted in transit.
  * Allows platform administrators to manage the core infrastructure while service owners independently manage their specific routes and backends.
  * Enables routing to specific shards for stateful non-HTTP applications (such as MongoDB) based on the SNI provided by the client.



#### How traffic is distributed when TLS routes are used

When SNI-based routing is configured, traffic is routed to backend services as follows:

  1. The load balancer listens on the IP and port defined in the forwarding rule.
  2. When a client initiates a TLS connection, the load balancer intercepts the `ClientHello` message and extracts the SNI hostname.
  3. The extracted SNI is compared against the hostnames defined in the configured TLS routes. The load balancer uses the following logic to determine which backend service should receive the traffic:

     1. If the client does not use the TLS protocol, the load balancer closes the connection.
     2. If the client does not send any SNI hostname name in its `ClientHello` message, the load balancer closes the connection.
     3. If the client sends an SNI hostname that is not a valid DNS name, the load balancer closes the connection.
     4. If the client sends an SNI hostname that doesn't match any SNI hostnames associated with a TLS route, the load balancer closes the connection.
     5. In all other situations: The load balancer selects a backend service using the following matching process:

Matching is done by the longest suffix (longest in terms of the number of subdomains). To illustrate the matching method, consider a TLS route whose SNI is `*.foo.com`, another TLS route whose SNI is `*.bar.foo.com`, and the third TLS route whose SNI is `baz.bar.foo.com`.

        * If the client's SNI hostname is `baz.bar.foo.com`, the load balancer selects a backend service which is referenced by the TLS route whose SNI is `baz.bar.foo.com`.
        * If the client's SNI hostname is `qux.bar.foo.com`, the load balancer selects a backend service which is referenced by the TLS route whose SNI is `*.bar.foo.com`.
        * If the client's SNI hostname is `qux.qux.foo.com`, the load balancer selects a backend service which is referenced by the TLS route whose SNI is `*.foo.com`.

Once a match is found, the encrypted byte stream is proxied directly to the assigned backend service without terminating the TLS connection (for TLS passthrough).




#### Limitations

The following limitations apply when you use TLS routes to configure SNI-based routing:

  * A target TCP proxy can either reference a single backend service or one or more TLS routes. You can't configure both.
  * Proxy Network Load Balancers can't detect HTTP connection coalescing, which might lead to misrouted HTTP requests.

By default, browsers already coalesce HTTP connections. For example, when a browser opens a connection to `www.example.com` and the server presents a certificate for `*.example.com` during TLS handshake, the browser reuses this connection for all requests to `*.example.com`, as long as the hostname resolves to the same IP address. This is in accordance with [RFC 7540](https://www.rfc-editor.org/rfc/rfc7540).

With SNI-based routing, once a connection is established, it is then permanently bound to its destination backend. Consider a deployment where `*.example.com` is served by one HTTPS backend with a `*.example.com` TLS certificate, and `my.example.com` is served by another HTTPS backend. If a connection to `*.example.com` is established first, then subsequent HTTP requests to `my.example.com` are coalesced onto the same connection, using the `*.example.com` HTTPS backend.




### Session affinity

Session affinity lets you configure the load balancer's backend service to send all requests from the same client to the same backend, as long as the backend is healthy and has capacity.

Internal proxy Network Load Balancers offer the following types of session affinity: 

  * **None**

A session affinity setting of `NONE` does _not_ mean that there is no session affinity. It means that no session affinity option is explicitly configured.

Hashing is always performed to select a backend. And a session affinity setting of `NONE` means that the load balancer uses a 5-tuple hash to select a backend. The 5-tuple hash consists of the source IP address, the source port, the protocol, the destination IP address, and the destination port.

A session affinity of `NONE` is the default value.

  * **Client IP affinity**

_Client IP_ session affinity (`CLIENT_IP`) is a 2-tuple hash created from the source and destination IP addresses of the packet. Client IP affinity forwards all requests from the same client IP address to the same backend, as long as that backend has capacity and remains healthy.

When you use client IP affinity, keep the following in mind:

    * The packet destination IP address is only the same as the load balancer forwarding rule's IP address if the packet is sent directly to the load balancer.
    * The packet source IP address might not match an IP address associated with the original client if the packet is processed by an intermediate NAT or proxy system before being delivered to a Google Cloud load balancer. In situations where many clients share the same effective source IP address, some backend VMs might receive more connections or requests than others.



Keep the following in mind when configuring session affinity:

  * Don't rely on session affinity for authentication or security purposes. Session affinity can break whenever the number of serving and healthy backends changes. For more details, see Losing session affinity.

  * The default values of the `--session-affinity` and `--subsetting-policy` flags are both `NONE`, and only one of them at a time can be set to a different value.




**Losing session affinity**

All session affinity options require the following:

  * The selected backend instance or endpoint must remain configured as a backend. Session affinity can break when one of the following events occurs: 
    * You remove the selected instance from its instance group.
    * Managed instance group autoscaling or autohealing removes the selected instance from its managed instance group.
    * You remove the selected endpoint from its NEG.
    * You remove the instance group or NEG that contains the selected instance or endpoint from the backend service.
  * The selected backend instance or endpoint must remain healthy. Session affinity can break when the selected instance or endpoint fails health checks.

All session affinity options have the following additional requirements: 
  * The instance group or NEG that contains the selected instance or endpoint must not be full as defined by its [target capacity](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity). (For regional managed instance groups, the zonal component of the instance group that contains the selected instance must not be full.) Session affinity can break when the instance group or NEG is full and other instance groups or NEGs are not. Because fullness can change in unpredictable ways when using the `UTILIZATION` balancing mode, you should use the `RATE` or `CONNECTION` balancing mode to minimize situations when session affinity can break.

  * The _total number_ of configured backend instances or endpoints must remain constant. When at least one of the following events occurs, the number of configured backend instances or endpoints changes, and session affinity can break:

    * Adding new instances or endpoints:

      * You add instances to an existing instance group on the backend service.
      * Managed instance group autoscaling adds instances to a managed instance group on the backend service.
      * You add endpoints to an existing NEG on the backend service.
      * You add non-empty instance groups or NEGs to the backend service.
    * Removing any instance or endpoint, _not just the selected instance or endpoint_ :

      * You remove any instance from an instance group backend.
      * Managed instance group autoscaling or autohealing removes any instance from a managed instance group backend.
      * You remove any endpoint from a NEG backend.
      * You remove any existing, non-empty backend instance group or NEG from the backend service.
  * The _total number_ of healthy backend instances or endpoints must remain constant. When at least one of the following events occurs, the number of healthy backend instances or endpoints changes, and session affinity can break:

    * Any instance or endpoint passes its health check, transitioning from unhealthy to healthy.
    * Any instance or endpoint fails its health check, transitioning from healthy to unhealthy or timeout.



## Failover

If a backend becomes unhealthy, traffic is automatically redirected to healthy backends.

The following table describes the failover behavior for internal proxy Network Load Balancers:

Load balancer mode | Failover behavior | Behavior when all backends are unhealthy  
---|---|---  
Regional internal proxy Network Load Balancer  | The load balancer implements a gentle failover algorithm per zone. Rather than waiting for all the backends in a zone to become unhealthy, the load balancer starts redirecting traffic to a different zone when the ratio of healthy to unhealthy backends in any zone is less than a certain percentage threshold (70%; this threshold can't be configured). If all backends in all zones are unhealthy, the load balancer immediately terminates the client connection. Envoy proxy sends traffic to healthy backends in a region based on the configured [ traffic distribution](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution). | Terminates the connection  
Cross-region internal proxy Network Load Balancer | Automatic failover to healthy backends in the same region or other regions. Traffic is distributed among healthy backends spanning multiple regions based on the configured [ traffic distribution](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution). | Terminates the connection  
  
## Load balancing for GKE applications

If you are building applications in Google Kubernetes Engine (GKE), you can use standalone zonal NEGs to load balance traffic directly to containers. With standalone NEGs you are responsible for creating the [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) object that creates the zonal NEG, and then associating the NEG with the backend service so that the load balancer can connect to the Pods.

Related GKE documentation:

  * [Container-native load balancing through standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg)



## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas).

## Limitations

  * The internal proxy Network Load Balancer doesn't support Shared VPC deployments where the load balancer's frontend is in one host or service project and the backend service and backends are in another service project (also known as cross-project service referencing).
  * Google Cloud does not make any guarantees on the lifetime of TCP connections when you use internal proxy Network Load Balancers. Clients should be resilient to dropped connections, both due to broader internet issues and due to regularly scheduled restarts of the Envoy proxies managing the connections.



## What's next

  * [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)

  * [Set up a cross-region internal Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-hybrid)



  * [Set up a regional internal proxy Network Load Balancer with an instance group backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)

  * [Set up a regional internal proxy Network Load Balancer with a zonal NEG backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal)

  * [Set up a regional internal proxy Network Load Balancer with a hybrid NEG backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid)

  * [Set up a regional internal proxy Network Load Balancer with an internet NEG backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-internet)

  * [View metrics with Cloud Monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
