---
url: https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer/
title: Proxy Network Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:37.190992+00:00
---

# Proxy Network Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Proxy Network Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

Proxy Network Load Balancers are layer 4 reverse proxy load balancers that distribute TCP traffic to backends in your Google Cloud Virtual Private Cloud (VPC) network or in other cloud environments. Traffic is terminated at the load balancing layer and then forwarded to the closest available backend by using TCP.

Proxy Network Load Balancers are intended for TCP traffic only, with or without SSL. For HTTP(S) traffic, we recommend that you use an Application Load Balancer instead.

The proxy Network Load Balancers support the following features:

  * **TLS/SSL offload for external load balancers**. You can use a global external proxy Network Load Balancer or a classic proxy Network Load Balancer to offload TLS at the load balancing layer by using an SSL proxy.
  * **Support for all ports**. These load balancers allow any valid port from 1-65535. For more information, see [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications).
  * **Port remapping**. The port used by the load balancer's forwarding rule does not have to match the port used when making connections to its backends. For example, the forwarding rule could use TCP port 80, while the connection to the backends could use TCP port 8080.
  * **Relays original source IP address**. You can use the PROXY protocol to relay the client's source IP address and port information to the load balancer backends.



The following diagram shows a sample proxy Network Load Balancer architecture. [ ![Proxy Network Load Balancer architecture.](https://docs.cloud.google.com/static/load-balancing/images/proxy-network-load-balancer.svg)](https://docs.cloud.google.com/static/load-balancing/images/proxy-network-load-balancer.svg) Proxy Network Load Balancer architecture (click to enlarge).

Proxy Network Load Balancers are available in the following modes of deployment:

  * **External proxy Network Load Balancer** : Load balances traffic that comes from clients on the internet. For architecture details, see [External proxy Network Load Balancer architecture](https://docs.cloud.google.com/load-balancing/docs/tcp#components).

Deployment mode | Network service tier | Load-balancing scheme † | IP address | Frontend ports  
---|---|---|---|---  
Global external | Premium Tier | EXTERNAL_MANAGED | IPv4   
IPv6  | Can reference exactly one port from 1-65535  
Classic | Global in Premium Tier Regional in Standard Tier | EXTERNAL | IPv4   
IPv6 (requires Premium Tier)  
Regional external | Premium or Standard Tier | EXTERNAL_MANAGED | IPv4   
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))   
  * **Internal proxy Network Load Balancer** : Load balances traffic within your VPC network or networks connected to your VPC network. For architecture details, see [Internal proxy Network Load Balancer architecture](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#components).

Deployment mode | Network service tier | Load-balancing scheme † | IP address | Frontend ports  
---|---|---|---|---  
Regional internal | Premium Tier | INTERNAL_MANAGED | IPv4  
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))  | Can reference exactly one port from 1-65535  
Cross-region internal  | Premium Tier | INTERNAL_MANAGED | IPv4   
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))   



† The load-balancing scheme is an attribute on the [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) and the [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) of a load balancer and indicates whether the load balancer can be used for internal or external traffic. The term `*_MANAGED` in the load-balancing scheme indicates that the load balancer is implemented as a managed service on [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) or as a managed service on the open source [Envoy proxy](https://www.envoyproxy.io/). In a load-balancing scheme that is `*_MANAGED`, requests are routed either to the GFE or to the Envoy proxy.

## External proxy Network Load Balancer

**Preview — Cross-region, regional external, and regional internal proxy Network Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The external proxy Network Load Balancer distributes traffic that comes from the internet to backends in your Google Cloud VPC network, on-premises, or in other cloud environments. These load balancers can be deployed in one of the following modes: global, regional, or classic.

External proxy Network Load Balancers support the following features:

  * **IPv6 termination**. The external load balancers support both IPv4 and [IPv6 addresses](https://docs.cloud.google.com/load-balancing/docs/ipv6) for client traffic. Client IPv6 requests are terminated at the load balancing layer and then proxied over IPv4 or IPv6 (provided the backends are configured as dual-stack) connection to your backends. Note that classic load balancers only support proxying over IPv4 to your backends.
  * **TLS/SSL offload**. You can use a global external proxy Network Load Balancer or a classic proxy Network Load Balancer to offload TLS at the load balancing layer by using an SSL proxy. New connections are forwarded to the closest available backends by using either SSL (recommended) or TCP. You can configure the following aspects of your deployment:

    * **Better utilization of backends**. SSL processing can be very CPU-intensive if the ciphers used are not CPU efficient. To maximize CPU performance, use ECDSA SSL certificates and TLS 1.2, and prefer the `ECDHE-ECDSA-AES128-GCM-SHA256` cipher suite for SSL between the load balancer and your backend instances.
    * **SSL policies**. [SSL policies](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) give you the ability to control the features of SSL that your load balancer negotiates with clients.
  * **Integration with Cloud Armor**. You can use [Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types) to protect your infrastructure from distributed denial-of-service (DDoS) attacks and other targeted attacks.

  * **Geographic control over where TLS is terminated**. The load balancer terminates TLS in locations that are distributed globally, so as to minimize latency between clients and the load balancer. If you require geographic control over where TLS is terminated, you can use the Standard Network Tier to force the load balancer to terminate TLS on backends that are located in a specific region only. For details, see [Configuring Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard-for-https-and-tcp-ssl).

  * **Support for App Hub**. Resources used by global external proxy Network Load Balancers and regional external proxy Network Load Balancers can be designated as services in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview).




In the following diagram, traffic from users in City A and City B is terminated at the load balancing layer, and a separate connection is established to the selected backend.

[ ![Proxy Network Load Balancer with SSL termination.](https://docs.cloud.google.com/static/load-balancing/images/ssl-lb-overview.svg)](https://docs.cloud.google.com/static/load-balancing/images/ssl-lb-overview.svg) Proxy Network Load Balancer with SSL termination.

For more details, see [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).

## Internal proxy Network Load Balancer

**Preview — Cross-region, regional external, and regional internal proxy Network Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) is an Envoy proxy-based regional Layer 4 load balancer that lets you run and scale your TCP service traffic behind an internal IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network.

The load balancer distributes TCP traffic to backends hosted on Google Cloud, on-premises, or in other cloud environments. These load balancers can be deployed in one of the following modes: cross-region or regional.

Internal proxy Network Load Balancers support the following features:

  * **IPv6 termination**. The internal load balancers support both IPv4 and [IPv6 addresses](https://docs.cloud.google.com/load-balancing/docs/ipv6) for client traffic. Client IPv6 requests are terminated at the load balancing layer and then proxied over IPv4 or IPv6 (provided the backends are configured as dual-stack) connection to your backends.
  * **Locality policies**. Within a backend instance group or network endpoint group, you can configure how requests are distributed to member instances or endpoints.
  * **Global access**. When global access is enabled, clients from any region can access the load balancer.
  * **Access from connected networks**. You can make your internal load balancer accessible to clients from networks beyond its own Google Cloud VPC network. The other networks must be connected to the load balancer's VPC network by using either VPC Network Peering, Cloud VPN, or Cloud Interconnect.
  * **Support for App Hub**. Resources used by cross-region internal proxy Network Load Balancers and regional internal proxy Network Load Balancers can be designated as services in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview).



For more details, see [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).

### High availability and cross-region failover

You can set up a cross-region internal proxy Network Load Balancer in multiple regions to get the following benefits:

  1. If backends in a particular region are down, the traffic fails over to the backends in another region gracefully.

The cross-region failover deployment example shows the following:

     * A cross-region internal proxy Network Load Balancer with a frontend VIP address in the Region A of your VPC network. Your clients are also located in the Region A.
     * A global backend service that references the backends in the Google Cloud Region A and Region B.
     * When the backends in the Region A are down, traffic fails over to the Region B.
[ ![Cross-region internal proxy Network Load Balancer with a cross-region failover deployment.](https://docs.cloud.google.com/static/load-balancing/images/cross-region-proxy-backend-failover.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-region-proxy-backend-failover.svg) Cross-region internal proxy Network Load Balancer with a cross-region failover deployment (click to enlarge).
  2. Cross-region internal proxy Network Load Balancers can also shield your application from complete regional outages by serving traffic to your client from proxies and backends in another region.

The high availability deployment example shows the following:

     * A cross-region internal proxy Network Load Balancer with frontend VIPs in the Region A and Region B of your VPC network. Your clients are located in the Region A.
     * You can make the load balancer accessible by using frontend VIPs from two regions.

[ ![Cross-region internal proxy Network Load Balancer with high availability deployment.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-failover.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-proxy-failover.svg) Cross-region internal proxy Network Load Balancer with high availability deployment (click to enlarge).



For information about how to set up a high availability deployment, see:

  * [Set up a cross-region internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)
  * [Set up a cross-region internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-hybrid)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
