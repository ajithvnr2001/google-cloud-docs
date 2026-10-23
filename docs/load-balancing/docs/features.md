---
url: https://docs.cloud.google.com/load-balancing/docs/features/
title: Load balancer feature comparison \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:39.877713+00:00
---

# Load balancer feature comparison  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Load balancer feature comparison Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you a comparative overview of the load balancing features offered by Cloud Load Balancing. If you haven't already done so, begin by reading the following:

  * To get an overview of the different load balancing solutions that are available in Google Cloud, see [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).
  * To determine which Google Cloud load balancer best meets your application's needs, see [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer).



In the following tables, a checkmark indicates that a feature is supported. For more information about a feature, click the _info_ link.

## Type of load balancer

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Proxy | Load balancer modes:  
[regional](https://docs.cloud.google.com/load-balancing/docs/l7-internal)  
[cross-region](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | Load balancer modes:  
[global](https://docs.cloud.google.com/load-balancing/docs/https)  
[classic](https://docs.cloud.google.com/load-balancing/docs/https)  
[regional](https://docs.cloud.google.com/load-balancing/docs/https) | Load balancer modes:  
[regional](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)  
[cross-region](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | Load balancer modes:  
[global](https://docs.cloud.google.com/load-balancing/docs/tcp)  
[classic](https://docs.cloud.google.com/load-balancing/docs/tcp)  
[regional](https://docs.cloud.google.com/load-balancing/docs/tcp) |  |   
Passthrough |  |  |  |  | Load balancer modes:  
[regional](https://docs.cloud.google.com/load-balancing/docs/internal) | Load balancer modes:  
[global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture) ([Preview](https://cloud.google.com/products#product-launch-stages))  
[regional](https://docs.cloud.google.com/load-balancing/docs/network)  
  
## Protocols from the clients to the load balancer

This table lists the protocols supported for communication between clients and the different load balancers.

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
One of: HTTP (HTTP/1.0) HTTPS (HTTP/1.0) |  |   
(Only global and classic modes) |  |  |  |   
One of: HTTP (HTTP/1.1) HTTPS (HTTP/1.1) |   
No QUIC support |   
No QUIC support for regional mode. |  |  |  |   
HTTP/2 over TLS HTTP/2 over TCP, also known as H2C gRPC 1 |  |   
(H2C support for global and regional modes only) |  |  |  |   
HTTP/3 (based on IETF QUIC)  |  |   
(Only global and classic modes) |  |  |  |   
SSL or TCP |  |  |   
TCP only |   
Regional mode: TCP only   
  
Global and classic  
mode: SSL or TCP |  |   
TCP, UDP, or L3_DEFAULT2 |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding-rule-protocols) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#forwarding-rule-protocols) regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule-protocols)  
WebSockets |   
  
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#websocket_support) |   
  
[info](https://docs.cloud.google.com/load-balancing/docs/https#websocket_support) |  |  |  |   
TLS early data |  | 3 |  |  |  |   
  
1 To support gRPC clients, create an Application Load Balancer that [supports HTTP/2 end-to-end (with or without TLS)](https://docs.cloud.google.com/load-balancing/docs/https#grpc-support).

2 The `L3_DEFAULT` setting enables support for the following additional IP protocols:

  * For internal passthrough Network Load Balancers, `L3_DEFAULT` enables support for TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE .
  * For global external passthrough Network Load Balancers and regional external passthrough Network Load Balancers, `L3_DEFAULT` enables support for TCP, UDP, ESP, GRE, ICMP, and ICMPv6 .



3 TLS early data is supported for HTTPS over TCP (HTTP/1.1, HTTP/2) and HTTP/3 over QUIC.

## Protocols from the load balancer to the backends

This table lists the IP protocol settings supported with backend services for different load balancers. For more reference information, see [Backend services](https://docs.cloud.google.com/load-balancing/docs/apis#backend_services).

This table does not apply to Application Load Balancers with serverless NEG backends. The backend service protocol setting is ignored for these load balancers.

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
One of: HTTP (HTTP/1.1) HTTPS (HTTP/1.1) |  |  |  |  |  |   
HTTP/2 over TLS, including gRPC HTTP/2 over TCP, also known as H2C |  |   
(H2C support for global and regional modes only) |  |  |  |   
One of:  
SSL (TLS) or TCP |  |  |   
TCP only |   
Regional mode: TCP only   
  
Global and classic  
mode: SSL or TCP |  |   
One of:  
TCP, UDP, or UNSPECIFIED1 |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service) |   
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service)  
UNSPECIFIED1 |  |  |  |  |  |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#backend-services)  
WebSockets |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#websocket_support) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https#websocket_support) |  |  |  |   
  
1 The `UNSPECIFIED` setting enables support for the following IP protocols:

  * For internal passthrough Network Load Balancers, `UNSPECIFIED` enables support for TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE .
  * For global external passthrough Network Load Balancers and regional external passthrough Network Load Balancers, `UNSPECIFIED` enables support for TCP, UDP, ESP, GRE, ICMP, and ICMPv6 .



## Backends

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Backends can be in multiple regions |   
[(Only cross-region mode)](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute) and   
[classic](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple) mode) |   
(Only cross-region mode) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp) and   
[classic](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp) mode) |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#backend-service) mode)  
Backends must be in one region |   
[(Only regional mode)](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb) and   
[classic](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple) mode) |   
[(Only regional mode)](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs) and [classic](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs) mode) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service) mode)   
Cloud Storage in backend buckets |  |  |  |  |  |   
External endpoints in internet NEGs |   
[(Only regional mode)](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-int-https-external-backend) |   
([Global](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend),   
[regional](https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend), and [classic](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg) modes)  |   
[(Only regional mode)](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-internet) |   
[(Only regional mode)](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-internet) |  |   
Multiple backend services and a URL map |  |  |  |  |  |   
Virtual machine backends on Compute Engine |  |  |  |  |  |   
Self-managed Kubernetes and GKE |  |  |  |  |  |   
(Only regional mode)  
[Zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts) |   
[`GCE_VM_IP_PORT` endpoints](https://docs.cloud.google.com/load-balancing/docs/l7-internal#backend_service) |   
[`GCE_VM_IP_PORT` endpoints](https://docs.cloud.google.com/load-balancing/docs/https#backend-service) |   
[`GCE_VM_IP_PORT` endpoints](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#supported_backends) |   
[`GCE_VM_IP_PORT` endpoints](https://docs.cloud.google.com/load-balancing/docs/tcp#backend_services) |   
[`GCE_VM_IP` endpoints](https://docs.cloud.google.com/load-balancing/docs/internal#neg-nic-net) |   
[`GCE_VM_IP` endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#zonal-neg-load-balancing)  
[Private Service Connect NEGs](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) |  |   
(Only global and regional mode) |  |   
(Only global and regional mode) |  |   
Private external endpoints in hybrid NEG backends |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts) |  |   
Serverless backends |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#endpoint_types) |   
[info](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) |  |  |  |   
[Dual-stack (IPV4 and IPv6) backends](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) |   
[info](https://docs.cloud.google.com/load-balancing/docs/ipv6) |   
[(Only global and regional modes)](https://docs.cloud.google.com/load-balancing/docs/ipv6) |   
[info](https://docs.cloud.google.com/load-balancing/docs/ipv6) |   
[(Only global and regional modes)](https://docs.cloud.google.com/load-balancing/docs/ipv6) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#dual-stack-backends) |   
(Both [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#backend-service) and [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#dual-stack-backends) modes)   
[IPv6-only backends](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#ipv6-only-backends) |   
(Both [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#backend-service) and [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#ipv6-only-backends) modes)   
  
## Health checks

For links to reference information, see [Health checks](https://docs.cloud.google.com/load-balancing/docs/apis#health_checks).

Health checks are not supported for internal and external Application Load Balancers that use serverless NEG backends.

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
gRPC health checks (without TLS) | 2 | 2 | 2 | 2 |  | 1  
gRPC health checks (with TLS) | 2 | 2 | 2 | 2 |  | 1  
HTTP health checks |  | 3 |  |   
(Only classic and regional mode) |  | 1  
HTTPS health checks |  | 3 |  |   
(Only classic and regional mode) |  | 1  
HTTP/2 health checks |  |  |  |   
(Only classic and regional mode) |  | 1  
SSL health checks |  |  |  |  |  | 1  
TCP health checks |  |  |  |  |  | 1  
[Configurable health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#create-hc) |  |  |  |  |  |   
Configurable request path (HTTP, HTTPS, HTTP/2) |  |  |  |  |  |   
Configurable request string or path (TCP or SSL) |  |  |  |  |  |   
Configurable expected response string |  |  |  |  |  | 1  
[ Distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks) |  |   
(Only regional mode) |  |   
(Only regional mode) |  |   
  
1 This table documents health checks used by global external passthrough Network Load Balancers and backend service-based regional external passthrough Network Load Balancers. Target pool-based load balancers support only [legacy HTTP health checks](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools#health_checks).

2 Envoy-based regional load balancers (regional internal and external Application Load Balancers and regional internal and external proxy Network Load Balancers) that use hybrid NEG backends don't support gRPC health checks. For more information, see the [Hybrid NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks).

3 Regional external Application Load Balancer does not support legacy health checks. The global external Application Load Balancer and the classic Application Load Balancer support legacy health checks only if both of the following are true:

  * The backends are instance groups.
  * The backend virtual machine (VM) instances serve traffic that uses the HTTP or HTTPS protocol.



## IP addresses

For links to reference information, see [Addresses](https://docs.cloud.google.com/load-balancing/docs/apis#addresses).

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Regional internal IPv4 address, accessible in your VPC network |  |  |  |  |  |   
Regional internal IPv6 address, accessible in your VPC network |  ([Preview](https://cloud.google.com/products#product-launch-stages)) |  |  ([Preview](https://cloud.google.com/products#product-launch-stages)) |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal) |   
Global external IPv4 address  
(Includes BYOIP addresses) |  |   
(Only global and classic1 mode) |  |   
(Only global and classic1 mode) |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#ip-addresses)1,6 mode)  
Global external IPv6 address |  |   
[IPv6 termination](https://docs.cloud.google.com/load-balancing/docs/ipv6)  
(Only global and classic1 mode) |  |   
[IPv6 termination](https://docs.cloud.google.com/load-balancing/docs/ipv6)  
(Only global and classic1 mode) |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#ip-addresses)1,6 mode)  
Regional external IPv4 address  
(Includes BYOIP addresses) |  |   
(Only regional and classic2 mode) |  |   
(Only regional and classic2 mode) |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#ip-address) mode)  
Regional external IPv6 address  
(Includes BYOIP addresses) |  |  ([Preview](https://cloud.google.com/products#product-launch-stages)) |  |  ([Preview](https://cloud.google.com/products#product-launch-stages)) |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#ip-address)1,3 mode) 

  * [Configure BYOIP](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6)

  
Multiple forwarding rules with the same IP address, each having a unique protocol and port combination |  |  |  |  |  |   
Internet accessible4 |  |  |  |  |  |   
Privately accessible |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks)5 |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy-lb-and-other-networks)5 |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks)5 |   
Client source IP address preservation | X‑Forwarded‑For header | X‑Forwarded‑For header | [PROXY](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol) protocol | [PROXY](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol) protocol |  |   
  
1 Supported for Premium Tier only.

2 Supported for Standard Tier only.

3 Target pool-based regional external passthrough Network Load Balancers don't support IPv6 traffic.

4 Internet access is also available for clients that are in Google Cloud.

5 Private access is available in the same VPC network and from any region with global access. In cross-region mode, global access is enabled by default.

6 Global external passthrough Network Load Balancers provide two global external IP addresses for high availability.

## Network topologies

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Network Service Tiers support | Premium Tier | Global mode: Premium Tier Classic and regional mode: Premium or Standard Tier | Premium Tier | Global mode: Premium Tier Classic and regional mode: Premium or Standard Tier | Premium Tier | Global mode: Premium Tier Regional mode: Premium or Standard Tier  
**Relationships between VPC networks, load balancers, and their backends**  
Load balancer and backends in different VPC networks |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#backend-networks) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https#backend-networks) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#backend-networks) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp#backend-networks) |  |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#backend-service-networks)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#backend-service-networks)  
Backends can use a Shared VPC network |  |  |  |  |  |   
Cross-project service referencing |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#shared_vpc) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https#cross-project)  
(Only global and regional mode)  
|  |  |  |   
**Client access to load balancers**  
Google Cloud or on-premises clients must access the load balancer privately1 |  |  |  |  |  |   
Google Cloud client VMs require external IP addresses or a NAT solution like Cloud NAT to access the load balancer  |  |  |  |  |  |   
On-premises client VMs require internet access to access the load balancer |  |  |  |  |  |   
Google Cloud client VMs can be located in any region |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#client-access) |   
(Only global and classic2 modes) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#client-access) |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) |   
Google Cloud client VMs can be located in any project |  |  |  |  |  |   
**More topologies**  
Load balancer as next hop |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) |   
Specify network interface of a backend VM | 3 | 4 | 3 | 4 | [info](https://docs.cloud.google.com/load-balancing/docs/internal#ig-nic-net) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#neg-nic-net)5  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#neg-nic-net)5  
[Multi-NIC](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) load balancing | [info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#backends-interfaces) | [info](https://docs.cloud.google.com/load-balancing/docs/https#backends-interfaces) | [info](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#backends-interfaces) | [info](https://docs.cloud.google.com/load-balancing/docs/tcp#backends-interfaces) | [info](https://docs.cloud.google.com/load-balancing/docs/internal#ig-nic-net) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#neg-nic-net)5  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#neg-nic-net)5  
  
1 Google Cloud or on-premises clients must access the load balancer privately by being either in the same VPC network, in a peered VPC network, or in another network connected using Cloud VPN tunnels or Cloud Interconnect attachments (VLANs).

2 Supported for Premium Tier only.

3 For regional load balancers, the backend VM's `nic0` must be in the same network and region used by the forwarding rule. For cross-region load balancers, the backend VM's `nic0` must be in the same network used by the forwarding rule.

4 The load balancer only sends traffic to the first network interface (`nic0`), whichever VPC network that `nic0` is in.

5 The backend VMs of an instance group always receive traffic on the first network interface (`nic0`), and multi-NIC load balancing is only supported for zonal NEGs with `GCE_VM_IP` endpoints.

## Failover and availability

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Load balancer is resilient to zonal outages   
  
Automatic failover to healthy backends within same region |  |  |  |  |  |   
Load balancer is resilient to regional outages   
  
Automatic failover to healthy backends in other regions |   
(Only cross-region mode) |   
(Only global and classic1 modes) |   
(Only cross-region mode) |   
(Only global and classic1 modes) |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#high_availability_by_design) mode)   
Support for active-active high availability configuration across load balancers |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#cross-region-failover) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/https/reg-applb-ha-overview) mode) |  |  |  |   
Support for active-passive failover configuration across load balancers |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/applb-failover-overview) mode)  |  |  |  |   
Support for dual IP address based high availability |  |  |  |  |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture#high_availability_by_design) mode)   
Configurable behavior when all backends are unhealthy |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#failover-policy) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#failover-policy)2 mode)   
Configurable failover backends |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#failover) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#failover-policy)3 mode)   
Configurable connection draining on failover |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#connection-draining-failover) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-draining-failover)4 mode)   
  
1 Supported for Premium Tier.

2 When all the backends of a target pool-based regional external passthrough Network Load Balancers are unhealthy, traffic is distributed among all backends.

3 Target pool-based regional external passthrough Network Load Balancers use backup pools to support failover.

4 Target pool-based regional external passthrough Network Load Balancers don't support configuration of connection draining on failover.

## Monitoring

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Byte count metrics |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#monitoring_metrics_for_internal_https_load_balancers) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#metrics-for-tcp-ssl-proxy) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#metrics-for-tcp-ssl-proxy) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#metrics_for_internal_tcpudp_load_balancers) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#metrics-resources)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#metrics-resources)  
Packet count metrics |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#metrics_for_internal_tcpudp_load_balancers) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#metrics-resources)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#metrics-resources)  
Round trip time (RTT) metrics |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#metrics_for_internal_tcpudp_load_balancers) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#metrics-resources)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#metrics-resources)  
Request latency metrics |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#monitoring_metrics_for_internal_https_load_balancers) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#metrics_for_internal_tcpudp_load_balancers) |   
Connection count metrics |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#metrics-for-tcp-ssl-proxy) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#metrics-for-tcp-ssl-proxy) |  |   
HTTP request count metrics |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#monitoring_metrics_for_internal_https_load_balancers) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#monitoring_metrics) |  |  |  |   
  
## Logging

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
**Log type**  
HTTP request and response attribute logs |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#log_fields) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#log-fields) |  |  |  |   
Connection attribute logs |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#intproxylb-logging) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#logs-format) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#logs-format)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#logs-format)  
**Log fields**  
[](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)HTTP request |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#what_is_logged) |   
[global, classic](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#log-fields)  
[regional](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#log-fields) |  |  |  |   
String that explains the proxy response | [proxyStatus](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#proxy-status) | [statusDetails](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#failure-messages)  
[proxyStatus](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#proxy-status) |  |  |  |   
TLS metadata between client and load balancer |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#tls-details) |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#tls-details) mode) |  |  |   
Connection attributes: 5-tuple, bytes/packets sent and received |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#logs-format) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#logs-format) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#logs-format)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#logs-format)  
VM instance details and GKE details |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#intproxylb-logging) |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring) mode) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#logs-format) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#logs-format)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#logs-format)  
Client VPC or location details |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#ilb-vpcdetails) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#netlb-geographicdetails)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#netlb-geographicdetails)  
Network tier details |  |  |  |  |  |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#netlb-networkdetails)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#netlb-networkdetails)  
Labels describing the load balancer resource |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#resource-labels) |   
[global, classic](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#resource-labels)  
[regional](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#resource-labels) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#intproxylb-logging) |   
[info](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring#resource-labels) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#view_logs) |   
global: [info](https://docs.cloud.google.com/load-balancing/docs/network/global-ext-netlb-logging-monitoring#view-logs)  
regional: [info](https://docs.cloud.google.com/load-balancing/docs/network/reg-ext-netlb-logging-monitoring#view-logs)  
  
## Session affinity

For detailed information, see [Session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#session_affinity).

For links to reference information, see [Backend services](https://docs.cloud.google.com/load-balancing/docs/apis#backend_services).

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Headers |  |   
(Only global and regional mode) |  |  |  |   
HTTP cookie |  |   
(Only global and regional) |  |  |  |   
Generated cookie |  |  |  |  |  |   
Stateful cookie |   
|   
(Only global and regional) |  |  |  |   
Client IP, no destination (1-tuple)  
`CLIENT_IP_NO_DESTINATION` |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#client-ip-no-destination-affinity) |   
Client IP, Destination IP (2-tuple)  
`CLIENT_IP` |  |  |  |  | 1 | 1  
Client IP, Destination IP, Protocol (3-tuple)  
`CLIENT_IP_PROTO` |  |  |  |  | 1 | 1  
Client IP, Client Port, Destination IP, Destination Port, Protocol (5-tuple)  
`CLIENT_IP_PORT_PROTO` |  |  |  |  | 1,2 | 1,2  
None (5-tuple)  
`NONE` |  |  |  |  | 3 | 3  
  
1 Setting session affinity is only meaningful if the protocol uses sessions—for example, TCP.

2 If the protocol does not have a concept of ports or if the packet does not carry port information (subsequent UDP fragments, for example), then a 3-tuple hash of the Client IP, Destination IP, and protocol is used instead.

3 If the protocol has a concept of ports and the packet carries port information, then `None` is a 5-tuple hash. If the protocol does not have a concept of ports or if the packet does not carry port information (for example, subsequent UDP fragments), then `None` is a 3-tuple hash of the Client IP, Destination IP, and protocol.

## Load balancing methods

For detailed information, see the [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

For links to reference information, see [Backend services](https://docs.cloud.google.com/load-balancing/docs/apis#backend_services).

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Balancing mode: connection |  |  |  |  |  |   
(Only regional mode)   
Balancing mode: custom metrics | 1 | 1 |  |  |  |   
Balancing mode: in-flight | 1 | 1  
(Only global and regional modes) |  |  |  |   
Balancing mode: rate (requests per second) | 1 | 1 |  |  |  |   
Balancing mode: rate (packets per second) |  |  |  |  |  |   
(Only global mode)   
Balancing mode: backend utilization  
(instance group backends only)  | 1 | 1 |  |  |  |   
(Only global mode)   
Load balancing locality policy |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy) |  [info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)   
(Only global and regional modes) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy) |  [info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)   
(Only global and regional modes) |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)  
Configurable maximum capacity per backend instance group or NEG | 1 | 1 |  |  |  |   
(Only global mode)  
Circuit breaking | 1 |   
(Only regional mode) |  |   
(Only regional mode) |  |   
Prefers region closest to client on the internet2 |  |   
(Only global and classic3 modes) |  |   
(Only global and classic3 modes) |  |   
(Only global mode)  
Prefers region closest to the load balancer2 |  |   
(Only global and classic3 modes) |  |   
(Only classic3 modes) |  |   
(Only global mode)  
Weight-based load balancing |  |   
(Only global and regional modes) |  |  |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#weighted-lb)4 mode)   
Within zone/region load balancing policy |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-lb) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-lb) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-lb) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode-lb) |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)  
  
1 This feature is not supported with load balancers that use serverless NEG backends.

2 When the closest region is at capacity or isn't healthy, the load balancer prefers next closest region.

3 Supported for classic load balancers in Premium Tier only.

4 This feature is not supported with target pool-based regional external passthrough Network Load Balancers.

## Routing and traffic management

Filter this table:  Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
HTTP or Layer 7 request routing |   
[info](https://docs.cloud.google.com/load-balancing/docs/url-map#traffic-management-guides) |   
[info](https://docs.cloud.google.com/load-balancing/docs/url-map#traffic-management-guides) |  |  |  |   
Fault injection |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#multiple_allowed_in_a_url_map) |   
(Only global and regional modes) |  |  |  |   
Configurable timeouts |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#timeouts_and_retries) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/request-distribution#timeouts_and_retries) |   
[info](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create#--timeout) |   
[info](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create#--timeout) |  |   
Retries |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal#timeouts_and_retries) |   
[info](https://docs.cloud.google.com/load-balancing/docs/https/request-distribution#timeouts_and_retries) |  |  |  |   
Redirects |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-http-to-https-redirect) |   
[global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-http-https-redirect)  
[classic](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-http-https-redirect)  
[regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-http-https-redirect) |  |  |  |   
URL rewrites |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#rewrite_the_requested_url) |   
[global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#rewrite_the_requested_url)  
[classic](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-rewrite)  
[regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#rewrite_the_requested_url) |  |  |  |   
Request and response header transformations  
(configured on the URL map) |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#add-remove-headers) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#add-remove-headers)  
and [regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#add-remove-headers) modes) |  |  |  |   
Traffic splitting |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#set_up_traffic_splitting_detailed_steps) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#set_up_traffic_splitting_detailed_steps)  
and [regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#set_up_traffic_splitting_detailed_steps) modes) |  |  |  |   
Traffic mirroring |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#mirror_traffic)1 |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#mirror_traffic) and [regional](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#mirror_traffic) modes) |  |   
(Only regional mode) |  |   
Outlier detection |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#configure_outlier_detection) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#configure_outlier_detection) and [regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#configure_outlier_detection) modes) |  |  |  |   
Retry failed requests |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#retry_a_request) |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#retry_a_request) and [regional](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#retry_a_request) modes) |  |  |  |   
Custom request and response headers   
(configured on the backend service) |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global) and [regional](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers) modes) |  |  |  |   
Custom error responses |  |   
[(Only global mode)](https://docs.cloud.google.com/load-balancing/docs/https/custom-error-response) |  |  |  |   
Service load balancing policy |   
[info](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy) |   
[(Only global and regional modes)](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy) |   
[(Only cross-region mode)](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy) |   
[(Only global mode)](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy) |  |   
Connection tracking policy |  |  |  |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#tracking-policy) |   
(Both global3 and [regional](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#tracking-policy) modes)   
Source IP-based traffic steering |  |  |  |  |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-steering)2 mode)  
  
1 This feature is not supported with load balancers that use serverless NEG backends.

2 This feature is supported by [backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service). Global external passthrough Network Load Balancers and target pool-based regional external passthrough Network Load Balancer don't support this feature.

3 The global external passthrough Network Load Balancer doesn't support the `PER_SESSION` connection tracking mode.

For traffic management features available with Cloud Service Mesh, see [Cloud Service Mesh features: Routing and traffic management](https://docs.cloud.google.com/service-mesh/docs/features#routing_and_traffic_management).

## Autoscaling and autohealing

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Managed instance group autoscaling based on load balancer serving capacity  |  |  (Only global and classic modes) |  |  |  |   
Autohealing (native to managed instance groups and GKE)  |  |  |  |  |  |   
Connection draining |  |  |  |  |  | 1  
  
1 This table documents the autoscaling and autohealing features supported by global external passthrough Network Load Balancers and backend service-based regional external passthrough Network Load Balancers. Target pool-based regional external passthrough Network Load Balancers don't support connection draining. 

## Security

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Google-managed SSL certificates |   
[info](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary) |   
[info](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary)1 |  |   
(Only [global](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary) and [classic](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary) mode)2 |  |   
CORS |   
[info](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#multiple_allowed_in_a_url_map) |   
(Only global and regional modes) |  |  |  |   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) |  | 3 |  |  |  |   
Google Cloud Armor |   
[info](https://docs.cloud.google.com/armor/docs/security-policy-overview#expandable-2) |   
[info](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  |   
(Only [global](https://docs.cloud.google.com/armor/docs/security-policy-overview) and [classic](https://docs.cloud.google.com/armor/docs/security-policy-overview) mode) |  |   
(Only regional mode)  
SSL offload |  |  |  |   
(Only global and classic modes)2 |  |   
SSL policies   
(TLS version and cipher suites) |   
[info](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) |   
[info](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)  
(Only global and classic modes)2 |  |   
Frontend mTLS |   
[info](https://docs.cloud.google.com/load-balancing/docs/mtls) |   
[info](https://docs.cloud.google.com/load-balancing/docs/mtls) |  |  |  |   
Backend mTLS |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls) |   
[info](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)  
(Only global and regional modes) |  |  |  |   
Authorization policies |   
[info](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview) |   
[info](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview)  
(Only global and regional modes) |  |  |  |   
Service rate limiting policies |   
[info](https://docs.cloud.google.com/load-balancing/docs/srl-policy/service-rate-limiting-overview)(only regional mode) |  |  |  |  |   
  
1 Global external Application Load Balancers and classic Application Load Balancers support both Compute Engine and Certificate Manager Google-managed SSL certificates, whereas regional external Application Load Balancers support only Certificate Manager Google-managed certificates.

2 Supported only if the load balancer is configured with a target SSL proxy.

3 IAP is incompatible with Cloud CDN.

### Google Cloud Armor protection for external load balancers

Cloud Armor provides both always-on and user-configurable DDoS protections for the following external load balancers, and user-configurable security policy rules depending on the type of load balancer.

Load balancer type or mode | Cloud Armor [security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types) | Supported security policy types  
---|---|---  
Global external Application Load Balancer  |  | 

  * Backend security policy
  * Edge security policy

  
Classic Application Load Balancer |  | 

  * Backend security policy
  * Edge security policy

  
Regional external Application Load Balancer |  | 

  * Regional backend security policy

  
Global external proxy Network Load Balancer |  | 

  * Backend security policy

  
Classic proxy Network Load Balancer |  | 

  * Backend security policy

  
Regional external passthrough Network Load Balancer |  | 

  * Network edge security policy

  
  
You can also configure advanced network DDoS protection for [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network), [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding), or VMs with public IP addresses. For more information about advanced network DDoS protection, see [Configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos).

## Cross-product integrations

Feature | Application Load Balancer | Proxy Network Load Balancer | Passthrough Network Load Balancer  
---|---|---|---  
Internal | External | Internal | External | Internal | External  
Cloud CDN |  |   
(Only [global](https://docs.cloud.google.com/cdn/docs/overview) and [classic](https://docs.cloud.google.com/cdn/docs/overview)1 modes) |  |  |  |   
Service Extensions plugins and callouts |   
[info](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) |   
[info](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) |  |  |  |   
Internal Compute Engine DNS names |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/dns-names) mode) |  |   
(Only [regional](https://docs.cloud.google.com/load-balancing/docs/dns-names) mode) |  |   
[info](https://docs.cloud.google.com/load-balancing/docs/dns-names) |   
Automatic Service Directory registration (Preview) |   
[info](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd) |  |  |  |   
[info](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd) |   
[App Hub](https://docs.cloud.google.com/app-hub/docs) integration |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources) |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources) |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources) |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources) |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources) |   
[info](https://docs.cloud.google.com/app-hub/docs/supported-resources)  
  
1 Supported for Premium Tier

## What's next

For detailed information about each load balancer, see the following:

  * [External Application Load Balancer overview (global, classic, and regional)](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer overview (regional and cross-region)](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [External proxy Network Load Balancer overview (global, classic, and regional)](https://docs.cloud.google.com/load-balancing/docs/tcp)
  * [Internal proxy Network Load Balancer overview (regional and cross-region)](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * [Global external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture)
  * [Regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
