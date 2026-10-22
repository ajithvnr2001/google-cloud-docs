---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy-lb-and-other-networks/
title: Internal proxy Network Load Balancers and connected networks \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:01.754206+00:00
---

# Internal proxy Network Load Balancers and connected networks  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy-lb-and-other-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal proxy Network Load Balancers and connected networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes scenarios for accessing an internal load balancer in your Virtual Private Cloud (VPC) network from a connected network. Before reviewing the information on this page, you should already be familiar with the concepts in the following guide:

  * [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)



## Use VPC Network Peering

When you use [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#internal_load_balancing) to connect your VPC network to another network, Google Cloud shares subnet routes between the networks. The subnet routes allow traffic from the peer network to reach internal load balancers in your network. Access is allowed if the following is true:

  * You create ingress firewall rules to allow traffic from client VMs in the peer network. Google Cloud [firewall rules](https://docs.cloud.google.com/vpc/docs/vpc-peering#firewall) aren't shared among networks when using VPC Network Peering.
  * For regional internal Application Load Balancers, client virtual machine (VM) instances in the peer network must be located in the same region as your internal load balancer. This restriction is waived if you configure global access.



You cannot selectively share only some internal passthrough Network Load Balancers, regional internal proxy Network Load Balancers, or internal Application Load Balancers by using VPC Network Peering. All internal load balancers are shared automatically. You can limit access to the load balancer's backends by using ingress [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) applicable to the backend VM instances. 

## Use Cloud VPN and Cloud Interconnect

You can access an internal load balancer from a peer network that is connected through a [Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or VLAN attachment for a [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) connection or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview). The peer network can be an on-premises network, another Google Cloud VPC network, or a virtual network hosted by a different cloud provider.

### Access through Cloud VPN tunnels

You can access an internal load balancer through a Cloud VPN tunnel when all of the following conditions are met.

#### In the internal load balancer's network

  * Both the Cloud VPN gateway and tunnel(s) must be located in the same region as the load balancer when global access is disabled. If global access is enabled on the load balancer's forwarding rule, this restriction is waived.


  * Routes must provide response paths from proxy systems back to the on-premises or peer network where the client is located. If you're using Cloud VPN tunnels with [dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing), consider the [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) of the load balancer's Cloud VPN network. The dynamic routing mode determines which custom dynamic routes are available to proxies in the [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/l7-internal#proxy-only_subnet).



#### In the peer network

The peer network must have at least one Cloud VPN tunnel with routes to the subnet where the internal load balancer is defined.

If the peer network is another Google Cloud VPC network:

  * The peer network's Cloud VPN gateway and tunnel(s) can be located in any region.

  * For Cloud VPN tunnels that use dynamic routing, the dynamic routing mode of the VPC network determines which routes are available to clients in each region. To provide a consistent set of custom dynamic routes to clients in all regions, use global dynamic routing mode.

  * Ensure on-premises or peer network firewalls permit packets sent to the IP address of the load balancer's forwarding rule. Ensure on-premises or peer network firewalls permit response packets received from the IP address of the load balancer's forwarding rule.




The following diagram highlights key concepts when accessing an internal load balancer by way of a Cloud VPN gateway and its associated tunnel. Cloud VPN securely connects your on-premises network to your Google Cloud VPC network using Cloud VPN tunnels.

[ ![Internal load balancing and Cloud VPN.](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-vpn-single-tunnel.svg)](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-vpn-single-tunnel.svg) Internal load balancing and Cloud VPN (click to enlarge).

Note the following configuration elements associated with this example:

  * In the `lb-network`, a Cloud VPN tunnel that uses dynamic routing has been configured. The VPN tunnel, gateway, and Cloud Router are all located in REGION_A, the same region where the internal load balancer's components are located.
  * Ingress allow firewall rules have been configured to apply to the backend VMs in the instance groups A and B so that they can receive traffic from IP addresses in the VPC network and from the on-premises network, `10.1.2.0/24` and `192.168.1.0/24`. No egress deny firewall rules have been created, so the [implied allow egress rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) applies.
  * Packets sent from clients in the on-premises networks, including from `192.168.1.0/24`, to the IP address of the internal load balancer, `10.1.2.99`, are delivered directly to a healthy backend VM, such as `vm-a2`, according to the configured [session affinity](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create#--session-affinity).
  * Replies sent from the backend VMs (such as `vm-a2`) are delivered through the VPN tunnel to the on-premises clients.



To troubleshoot Cloud VPN, see [Cloud VPN troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

### Access through Cloud Interconnect

You can access an internal load balancer from an on-premises peer network that is connected to the load balancer's VPC network when all the following conditions are met in the internal load balancer's network:

  * Both the VLAN attachment and Cloud Router must be located in the same region as the load balancer when global access is disabled. If global access is enabled on the load balancer's forwarding rule, this restriction is waived.

  * On-premises routers must provide response paths from the load balancer's backends to the on-premises network. VLAN attachments for both Dedicated Interconnect and Partner Interconnect must use Cloud Routers; thus, custom dynamic routes provide response paths. The set of custom dynamic routes they learn depends on the dynamic routing mode of the load balancer's network.

  * Ensure on-premises firewalls permit packets sent to the IP address of the load balancer's forwarding rule. Ensure on-premises firewalls permit response packets received from the IP address of the load balancer's forwarding rule.




### Use global access with Cloud VPN and Cloud Interconnect

By default, clients must be in the same network or in a VPC network connected by using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). You can enable global access to allow clients from any region to access your load balancer.

For cross-region internal proxy Network Load Balancers, global access is enabled by default. Clients from any region can access your load balancer. For regional internal proxy Network Load Balancers, when you [enable global access](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#ilb-global-access), the following resources can be located in any region: 

  * Cloud Routers
  * Cloud VPN gateways and tunnels
  * VLAN attachments



In the diagram:

  * The load balancer's frontend and backends are in the `REGION_A` region.
  * The Cloud Router is in the `REGION_B` region.
  * The Cloud Router peers with the on-premises VPN router.
  * The Border Gateway Protocol (BGP) peering session can be through Cloud VPN or Cloud Interconnect with Direct Peering or Partner Interconnect.

[ ![Internal load balancing with global access.](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-on-premises-clients.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-on-premises-clients.svg) Internal load balancing with global access (click to enlarge).

The VPC network's [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-routing-mode) is set to `global` to enable the Cloud Router in `REGION_B` to advertise the subnet routes for subnets in any region of the load balancer's VPC network.

### Multiple egress paths

In production environments, you should use multiple Cloud VPN tunnels or VLAN attachments for redundancy. This section discusses requirements when using multiple tunnels or VLAN attachments.

In the following diagram, two Cloud VPN tunnels connect `lb-network` to an on-premises network. Although Cloud VPN tunnels are used here, the same principles apply to Cloud Interconnect.

[ ![Internal load balancing and multiple Cloud VPN tunnels.](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-vpn-multiple-tunnel.svg)](https://docs.cloud.google.com/static/load-balancing/images/proxy-ilb-vpn-multiple-tunnel.svg) Internal load balancing and multiple Cloud VPN tunnels (click to enlarge).

You must configure each tunnel or each VLAN attachment in the same region as the internal load balancer. This requirement is waived if you enabled global access.

Multiple tunnels or VLAN attachments can provide additional bandwidth or can serve as standby paths for redundancy.

Keep in mind the following points:

  * If the on-premises network has two routes with the same priorities, each with a destination of `10.1.2.0/24` and a next hop corresponding to a different VPN tunnel in the same region as the internal load balancer, traffic can be sent from the on-premises network (`192.168.1.0/24`) to the load balancer by using [equal-cost multipath (ECMP)](https://www.wikipedia.org/wiki/Equal-cost_multi-path_routing).
  * After packets are delivered to the VPC network, the internal load balancer distributes them to backend VMs according to the configured [session affinity](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create#--session-affinity).
  * If the `lb-network` has two routes, each with the destination `192.168.1.0/24` and a next hop corresponding to different VPN tunnels, responses from backend VMs can be delivered over each tunnel according to the [priority of the routes in the network](https://docs.cloud.google.com/vpc/docs/routes#instancerouting). If different route priorities are used, one tunnel can serve as a backup for the other. If the same priorities are used, responses are delivered by using ECMP.
  * Replies sent from the backend VMs (such as `vm-a2`) are delivered directly to the on-premises clients through the appropriate tunnel. From the perspective of `lb-network`, if routes or VPN tunnels change, traffic might egress by using a different tunnel. This might result in TCP session resets if an in-progress connection is interrupted.



## What's next

  * To configure and test a regional internal proxy Network Load Balancer, see [Set up a regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
