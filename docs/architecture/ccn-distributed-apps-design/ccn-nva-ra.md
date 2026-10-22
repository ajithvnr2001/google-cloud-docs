---
url: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-nva-ra/
title: VPC Network Peering Cross-Cloud Network with NVAs and regional affinity \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:54.291168+00:00
---

# VPC Network Peering Cross-Cloud Network with NVAs and regional affinity  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-nva-ra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  VPC Network Peering Cross-Cloud Network with NVAs and regional affinity Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-08-24 UTC

This document provides a reference architecture that you can use to deploy a [Cross-Cloud Network](https://cloud.google.com/solutions/cross-cloud-network) hub-and-spoke network topology that uses network virtual appliances (NVAs) to pass traffic.

The intended audience for this document is network administrators who build network connectivity and cloud architects who plan how workloads are deployed. The document assumes that you have a basic understanding of routing, internet connectivity, and the NVA software that you want to deploy. To use this reference architecture, you should have familiarity with the [Cross-Cloud Network design guide](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design).

This design supports multiple external connections to on-premises or Cloud Service Provider (CSP) locations and multiple workload VPC networks.

This design assumes a single-region deployment. If you want to deploy in more than one region, you can use the guidance in Design alternatives, which provides for regional affinity but doesn't provide automatic regional failover. If you want automatic regional failover, you can use [NCC Cross-Cloud Network with NVAs and regional failover](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-nva).

This design places NVAs in all flows except those within and between workload VPC networks. You can cause flows to skip the NVAs by adding the appropriate skip policy-based routes. Only the flows between the external network and the services-access VPC network need NVAs as all other flows can be inspected by Cloud Next Generation Firewall.

## Architecture

The following diagram shows a high-level view of the architecture of the networks and the flows that this architecture supports.

![The four types of connections that are described in the document.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-vnp-nva-flows.svg)![A legend for the NVA architectures.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-nva-legend.svg)

The architecture contains the following high-level elements: 

Component | Purpose | Interactions  
---|---|---  
External networks (on-premises or other CSP network) | Hosts the clients of workloads that run in the workload VPCs and in the services-access VPCs. External networks can also host services.  | Exchanges data with Google Cloud's VPC networks through the NVAs that are hosted in the routing VPC network. Connects to the routing VPC network by using Cloud Interconnect or HA VPN. Terminates one end of the following flows:

  * External-to-services-access
  * External-to-workload

  
Routing VPC network (also known as the transit VPC network)  | Acts as a hub for the external network, services-access VPC network, and workload VPC networks. Hosts the NVAs that are used to process inter-network traffic.  | Connects the external network, the services-access VPC network, and the workload VPC networks together through a combination of Cloud Interconnect, HA VPN, and VPC Network Peering. When traffic from the external, services-access, and workload networks passes through the routing network, policy-based routes send the traffic to the NVAs.   
Services-access VPC network  | Provides access points to managed services that are hosted in other networks. The services-access network can also host services directly if needed.  | Exchanges data with the external and workload networks through the routing network. Connects to the routing VPC by using HA VPN. Transitive routing, which is provided by HA VPN, allows external traffic to reach managed services VPCs through the services-access VPC network. If the services-access VPC network hosts services directly, terminates one end of flows from all other networks.  
Managed services VPC network  | Hosts managed services that are needed by clients in other networks.  | Exchanges data with the external, services-access, and workload networks. Connects to the services-access VPC network by using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), which uses VPC Network Peering, or by using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Terminates one end of flows from all other networks.  
Workload VPC networks  | Hosts workloads that are needed by clients in other networks.  | Exchanges data with the external and services-access VPC networks through the routing VPC network. Connects to the routing network by using VPC Network Peering. Connects to other workload VPC networks by using NCC. Terminates one end of the following flows:

  * External-to-workload
  * Workload-to-services-access
  * Workload-to-workload

  
Internet access VPC network | Provides access to the internet for workloads that need it. | Provides outbound access to internet for workloads that need to download updates or other data from the internet. Data travels through the NVAs and out through Cloud NAT. Terminates one end of the following flows:

  * Workload-to-internet
  * Services-access-to-internet

  
  
### Connections descriptions

The following diagram shows a detailed view of the architecture that highlights the four connections among the networks:

![The four types of connections that are described in the document.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-vnp-nva-connections.svg)

This section describes the four connections that are shown in the preceding diagram.

#### Connection 1: Between external networks and the routing VPC network

This connection between external networks and routing VPC networks happens over Cloud Interconnect or HA VPN. Cloud Routers in the routing VPC network and the external routers in the external network exchange routes using BGP.

  * Routers in external networks announce the routes for external subnets to the routing VPC Cloud Routers. The preference of the routes can be expressed by using BGP metrics and attributes.
  * Cloud Routers in the routing VPC network advertise routes for prefixes in Google Cloud's VPCs to the external networks. These routes must be announced by using [Cloud Router custom route announcements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).



#### Connection 2: Between routing VPC networks and services-access VPC networks

This connection between routing VPC networks and services-access VPC networks happens over HA VPN. Routes are exchanged by using BGP between the regional Cloud Routers in the routing VPC networks and the services-access VPC networks.

  * Routing VPC HA VPN Cloud Routers announce routes for external network prefixes, workload VPCs, and other services-access VPCs to the services-access VPC Cloud Router. These routes must be announced by using Cloud Router custom route announcements.
  * The services-access VPC network announces its subnets and the subnets of any attached managed services VPC networks to the routing VPC network. Managed services VPC routes must be announced by using Cloud Router custom route announcements.



#### Connection 3: Between routing VPC networks and workload VPC networks

This connection between routing VPC networks and workload VPC networks is implemented using VPC Network Peering. This connection allows communication between the workload VPC networks and the other networks that are connected to the routing VPC network. These other networks include the external networks and the services-access VPC networks.

  * The workload VPC network automatically exports subnets to the routing VPC network.



#### Connection 4: Between workload VPC networks

Workload VPC networks are connected using NCC VPC spokes of the same hub. As such, traffic from one workload VPC network to another travels directly between the networks. The traffic doesn't transit the routing VPC network.

### Traffic flows

The following diagram shows the four flows that are enabled by this reference architecture.

![The four flows that are described in this document with a detailed background.](https://docs.cloud.google.com/static/architecture/images/ccn-distributed-apps-design/ccn-nva-flow-details.svg)

The following table describes the flows in the diagram:

Source | Destination | Description  
---|---|---  
External network  | Services-access VPC network | 

  1. Traffic follows routes over the Cloud Interconnect connections to the routing VPC network. The routes are announced by the external-facing Cloud Router.
  2. In the routing VPC network, traffic follows an untagged policy-based route to the internal passthrough Network Load Balancer in front of the NVAs.
  3. [A skip policy-based route](https://docs.cloud.google.com/vpc/docs/policy-based-routes#skip-option) is assigned to the NVA VMs. The route causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  4. Traffic follows a custom route to the services-access VPC network. The route is announced across the HA VPN connection. Traffic that's destined for an attached managed services VPC network follows VPC Network Peering custom routes to the managed services network.

  
Services-access VPC network  | External network  | 

  1. Traffic follows a custom route across the HA VPN tunnels to the routing VPC network.
  2. In the routing VPC network, traffic follows an untagged policy-based route to the internal passthrough Network Load Balancer that's in front of the NVAs.
  3. A policy-based skip route assigned to the NVA VMs causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  4. Traffic follows routes across the external connections back to the external network. The routes were learned from the external routers over BGP.

  
External network  | Workload VPC network  | 

  1. Traffic follows routes over the external connections to the routing network. The routes were announced by the external-facing Cloud Router.
  2. In the routing VPC network, traffic follows an untagged policy-based route to the internal passthrough Network Load Balancer in front of the NVAs.
  3. A policy-based skip route assigned to the NVA VMs causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  4. Traffic follows the subnet route to the relevant workload VPC network. The route was learned through VPC Network Peering.

  
Workload VPC network  | External network  | 

  1. Traffic follows a policy-based route that's programmed in the workload VPC to the internal passthrough Network Load Balancer in front of the NVAs in the routing VPC network.
  2. A policy-based skip route assigned to the NVA VMs causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  3. Traffic follows dynamic routes across the external connections back to the external network. The routes are learned from the external routers using BGP.

  
Workload VPC network  | Services-access VPC network  | 

  1. Traffic follows a policy-based route that's programmed in the workload VPC to the internal passthrough Network Load Balancer in front of the NVAs in the routing VPC network.
  2. A policy-based skip route assigned to the NVA VMs causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  3. Traffic follows a dynamic route through one of the HA VPN tunnels to the services-access VPC network. The route was learned from BGP custom route announcements.

  
Services-access VPC network  | Workload VPC network  | 

  1. Traffic follows a custom route to the routing VPC network. The route was announced across the HA VPN tunnels.
  2. In the routing VPC network, traffic follows an untagged policy-based route to the internal passthrough Network Load Balancer in front of the NVAs.
  3. A policy-based skip route assigned to the NVA VMs causes traffic leaving an NVA to skip the untagged policy-based route and instead follow VPC routing.
  4. Traffic follows the subnet route to the relevant workload VPC network. The route was learned through VPC Network Peering.

  
Workload VPC network  | Workload VPC network  | Traffic that leaves one workload VPC network follows the more specific route to the other workload VPC network through NCC. Return traffic reverses this path. This traffic doesn't pass through the NVAs.   
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Network Connectivity Center](https://cloud.google.com/network-connectivity-center): An orchestration framework that simplifies network connectivity among spoke resources that are connected to a central management resource called a _hub_. 
  * [ Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview): A service that extends your external network to the Google network through a high-availability, low-latency connection.
  * [ Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn): A service that securely extends your peer network to Google's network through an IPsec VPN tunnel.
  * [ Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview): A distributed and fully managed offering that provides Border Gateway Protocol (BGP) speaker and responder capabilities. Cloud Router works with Cloud Interconnect, Cloud VPN, and Router appliances to create dynamic routes in VPC networks based on BGP-received and custom learned routes.
  * [ Compute Engine](https://cloud.google.com/compute): A secure and customizable compute service that lets you create and run VMs on Google's infrastructure.
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Cloud Next Generation Firewall](https://docs.cloud.google.com/firewall/docs/about-firewalls): A fully distributed firewall service with advanced protection capabilities, micro-segmentation, and simplified management to help protect your Google Cloud workloads from internal and external attacks. 



## Design alternatives

For a multi-region deployment of this design, you can provide regional affinity by specifying the following in the policy-based route:

  * The source CIDR range of a relevant subnet.
  * The IP address of the relevant NVA load balancer.



You can provide for regional failover by manually adjusting routes or by using scripts.

## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, and performance.

### Security and compliance

The following list describes the security and compliance considerations for this reference architecture:

  * For compliance reasons, you might want to deploy Cloud Interconnect in a single region only. If you want to keep all traffic in a single region, you can use a 99.9% topology. For more information, see [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability) and [Establish 99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability).
  * Use Cloud Next Generation Firewall to secure traffic that travels between workload VPC networks.
  * If you require L7 traffic inspection, enable the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention) (optionally with [TLS inspection support](https://docs.cloud.google.com/firewall/docs/about-tls-inspection)) to block malicious activity and protect your workloads against threats. The service helps support [vulnerability, anti-spyware, and antivirus protection](https://docs.cloud.google.com/firewall/docs/about-threats). The service works by creating Google-managed zonal firewall endpoints that use packet intercept technology to transparently inspect the workloads without requiring any route re-architecture. Cloud Next Generation Firewall Enterprise incurs [zonal firewall endpoint and data processing charges](https://cloud.google.com/firewall/pricing).
  * Enable [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview) to allow or block connections based on Google Threat Intelligence data.
  * Use [Geolocation objects for firewall policy rules](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) to allow traffic from only allowed countries and to block embargoed countries.
  * Enable logging and monitoring as appropriate for your traffic and compliance needs. You can use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) to gain insights into your traffic patterns.
  * Use [Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/overview) to gather additional insight into your traffic.
  * If the NVAs must connect to internet locations to download updates, configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) in the internet access VPC network.
  * If you want clients in your external network to reach Google APIs directly, create a policy-based route in the routing VPC network as follows: 
    * **Source range** : An aggregate range for your external network.
    * **Destination range** : `199.36.153.4/30`
    * **Next hop** : `default-internet-gateway`
  * If you want your Google Cloud VMs to access Google APIs over private connections, do the following:

    1. In each VPC network, enable Private Google Access.
    2. In each workload network, create a policy-based route to access Google APIs: 
       * **Source range** : The address range for the workload VPC subnet.
       * **Destination range** : `199.36.153.4/30`
       * **Next hop** : `default-internet-gateway`
    3. Create a DNS response policy for Private Google Access that applies to the routing VPC network and all workload VPC networks.
    4. In the DNS response policy create a rule as follows:

       * **DNS name** : `*.googleapis.com.`
       * **Local data** :
             
             name="*.googleapis.com.",type="A",ttl=3600,rrdatas="199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7"
             




### Reliability

The following list describes the reliability considerations for this reference architecture:

  * To get 99.99% availability for Cloud Interconnect, you must connect to two different Google Cloud regions even if you have VMs in only one region.
  * To improve reliability and minimize exposure to regional failures, you can duplicate your deployment in multiple regions by using the [Google Cloud multi-regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional).
  * To handle your expected traffic between the services-access VPC and other networks, create a sufficient number of VPN tunnels. Individual VPN tunnels have [bandwidth limits](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits). The same guidance applies if you are using HA VPN between your external networks and the routing VPC network.



### Performance optimization

The following list describes the performance considerations for this reference architecture:

  * You might be able to improve network performance by increasing the maximum transmission unit (MTU) of your networks and connections. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  * Communication between the routing VPC and workload resources is over VPC Network Peering, which provides full-line-rate throughput for all VMs in the network at no additional cost. Consider [VPC Network Peering quotas and limits](https://docs.cloud.google.com/vpc/docs/quota#per_network) when you plan your deployment.
  * You can connect your external network to the routing VPC network by using HA VPN or Cloud Interconnect. For more information about balancing cost and performance considerations, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).



## Deployment

The architecture in this document creates three sets of connections to a central routing VPC network plus a different connection among workload VPC networks. After all of the connections are fully configured, all of the networks in the deployment can communicate with all other networks.

This deployment assumes that you are creating connections between the external network and routing VPC networks in one region. Workload subnets can be in any region, however. If you are placing workloads in one region only, you only need to create subnets in that region.

To deploy this reference architecture, complete the following tasks:

  1. Identify regions to place connectivity and workloads
  2. Create your VPC networks and subnets
  3. Create resource tags to govern firewall rules
  4. Create and associate network firewall policies
  5. Create connections between external networks and your routing VPC network
  6. Create connections between your routing VPC network and services-access VPC networks
  7. Create connections between your routing VPC network and workload VPC networks
  8. Connect your workload VPC networks
  9. Install NVAs
  10. Create service routing
  11. Set up internet access in the internet access network
  12. Test connectivity to workloads



### Identify regions to place connectivity and workloads

In general, you want to place connectivity, VPC subnets, and Google Cloud workloads in close proximity to your on-premises networks or other cloud clients. For more information about placing workloads, see [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/) and [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).

### Create your VPC networks and subnets

To create your VPC networks and subnets, complete the following tasks:

  1. Create or identify the projects where you will create your VPC networks. You need a routing project where you land your external-facing connectivity and another project to host your services-access and workload VPC networks. For guidance, see [Network segmentation and project structure](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#network-segmentation-and-project-structure). If you intend to use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks, [provision your projects as Shared VPC host projects](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).
  2. Plan your IP address allocations for your networks. You can preallocate and reserve your ranges by [creating internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges). Allocating address blocks that can be aggregated makes later configuration and operations more straightforward.
  3. Create a routing VPC network VPC and subnet in the routing project. If you think you'll have more than one region, enable global routing.
  4. Create an internet access VPC network and subnet in the routing project.
  5. Create a services-access VPC network and subnet in the host project. If you think that you'll have more than one region, enable global routing.
  6. Create workload VPC networks and subnets in the host projects. If you think you'll have more than one region, enable global routing.



### Create resource tags to govern Cloud Next Generation Firewall rules

Create the following [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing). You can name them how you'd like. The listed names are for example only.

  1. For the routing VPC network: 
     * **Key** : `routing-vpc-tags`
     * **Value** : `routing-vpc-multinic`
     * **Purpose** : `GCE_FIREWALL`
     * **Purpose-data** : The name of the routing VPC network.
  2. For each workload VPC network:

     * **Key** : `WORKLOAD_NAME-tags`

Replace `WORKLOAD_NAME` with the name of the workload VPC network.

     * **Values** : `WORKLOAD_NAME-clients`, `WORKLOAD_NAME-www`

Replace `WORKLOAD_NAME` with the name of the workload VPC network.

     * **Purpose** : `GCE_FIREWALL`

     * **Purpose-data** : The name of the workload VPC network.

  3. For the internet access network:

     * **Key** : `internet-tag`
     * **Value** : `internet-vpc`
     * **Purpose** : `GCE_FIREWALL`
     * **Purpose-data** : The name of the internet access network.



### Create and associate network firewall policies

This section shows you the Cloud NGFW rules to [create and associate](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies) for your deployment.

  1. Create a global network firewall policy in the routing project.
  2. Create the following firewall rules in the policy: 
     * Rule to allow ingress traffic from [health-check IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-rangesrule) for the ports in use, such as `tcp:80,443`.
     * Rule to [allow Identity-Aware Proxy traffic](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule).
     * Rule to allow ingress traffic from internal ranges such as the services-access, workload, and external networks.
  3. Associate the policy with the routing VPC network.
  4. Based on the workloads in your workload and services-access VPCs, create firewall policies and rules in the workload hosting project to govern that traffic.



### Create connections between external networks and your routing VPC network

This section assumes connectivity in a single region.

  1. Set up the connectivity between the external networks and your routing network. For an understanding of how to think about this, see [External and hybrid connectivity](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#external-and-hybrid-connectivity). For guidance on choosing a connectivity product, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).
  2. [Configure BGP](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) as follows: 
     * Configure the router in the given external location as follows: 
       * Announce all subnets for that external location by using the same BGP MED on both interfaces, such as 100. If both interfaces announce the same MED, then Google Cloud can use ECMP to load balance traffic across both connections.
     * Configure the external-facing Cloud Router in the routing VPC of the connected region as follows: 
       * Using [custom route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes), announce all subnet ranges from all regions over both external-facing Cloud Router interfaces. Aggregate them if possible. Use the same MED on both interfaces, such as 100.



### Create connections between your routing VPC network and services-access VPC networks

The services-access VPC uses HA VPN to connect to the routing VPC. The VPN allows for transitive routing between the services-access VPC and both the external and workload networks.

  1. Estimate how much traffic needs to travel between the routing and services-access VPCs. Scale your expected number of tunnels accordingly.
  2. Configure HA VPN between the routing VPC and the services-access VPC by using the instructions in [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2). Create a dedicated HA VPN Cloud Router in the routing network. Leave the external-network-facing router for external network connections. 
     * Routing VPC Cloud Router configuration: 
       * To announce external-network and workload VPC subnets to the services-access VPC, use [custom route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes) on the Cloud Router in the routing VPC.
     * Services-access VPC Cloud Router configuration: 
       * To announce services-access VPC subnets to the routing VPC, use custom route advertisements on the services-access VPC Cloud Router.
       * If you use [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to connect a managed services VPC to the services-access VPC, use custom routes to announce those subnets as well.
  3. If you connect a managed services VPC to the services-access VPC by using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), after the VPC Network Peering connection is established, update the services-access VPC side of the VPC Network Peering connection to export custom routes.



### Create connections between your routing VPC network and workload VPC networks

[Create VPC Network Peering connections](https://docs.cloud.google.com/vpc/docs/using-vpc-peering) between your routing VPC and each of your workload VPCs:

  * Enable **Export custom routes** for the routing VPC side of each connection.
  * Enable **Import custom routes** for the workload VPC side of each connection.
  * In the default scenario, only the workload VPC subnet routes are exported to the routing VPC. You don't need to export custom routes from the workload VPCs.



### Connect your workload VPC networks

Connect the workload VPC networks together by using [NCC VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). Make all spokes part of the same NCC spoke peer group. Use a core peer group to allow full mesh communication between the VPCs.

Use Cloud Next Generation Firewall to govern traffic within and between workload VPC networks.

The NCC connection announces specific routes among the workload VPC networks. Traffic between these networks follows those routes.

### Install NVAs

These instructions assume you have a VM image that you want to use for your NVAs.

Create a load-balanced group of NVAs. See [Set up internal passthrough Network Load Balancer for third-party appliances](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop) for more details.

  * Create an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) based on your NVA image with the following parameter:

    * **Network tag** : `nva-REGION`

Replace `REGION` with the name of the region.

    * **Resource Manager tag** : `routing-vpc-tags=routing-vpc-multinic`.

    * A network interface for the routing VPC network with no external IP address.

    * A network interface for the internet access VPC network with no external IP address.

    * Set `can IP forward` for the VM and operating system.

    * Create `ip route` routes and `iptables` rules to send traffic between the routing and internet access networks.

  * Create a [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs) with enough VMs to handle your expected traffic.




### Create service routing

This section describes how to send traffic through the NVAs or to bypass the NVAs as appropriate.

  1. In the routing VPC network, create a [policy-based route](https://docs.cloud.google.com/vpc/docs/use-policy-based-routes) with the following parameters: 
     * **Source range** : `0.0.0.0/0`
     * **Destination range** : `0.0.0.0/0`
     * **Next hop** : the IP address of the internal passthrough Network Load Balancer forwarding rule
     * **Network tags** : Don't specify any network tags. These parameters create a rule that applies to all traffic coming from a VLAN attachment, VPN tunnel, or another VM in the network.
  2. In the routing network, create a skip policy-based route with the following parameters:

     * **Source range** : `0.0.0.0/0`
     * **Destination range** : `0.0.0.0/0`
     * **Next hop** : Set the next hop to skip other policy-based routes and use default routing.
     * **Network tags** : `nva-REGION`

Replace `REGION` with the name of the region.

These parameters create a rule that applies only to traffic leaving the NVA VMs. It causes such traffic to skip the first policy-based route you created and instead follow the VPC routing table.

  3. In each workload network, create policy-based routes for each subnet with the following configuration:

     * **Source range** : The address range for the workload VPC subnet.
     * **Destination range** : `0.0.0.0/0`
     * **Next hop** : the IP address of the internal passthrough Network Load Balancer forwarding rule in the routing network
  4. In each workload network, create a skip policy-based route for intra-subnet traffic:

     * **Source range** : The address range for the workload VPC subnet.
     * **Destination range** : The address range for the workload VPC subnet.
     * **Next hop** : Set the next hop to skip other policy-based routes and use default routing.
  5. In each workload network, create a skip policy-based route for inter-subnet traffic. A route needs to be created for each other workload subnet unless the routes can be aggregated:

     * **Source range** : The address range for the workload VPC subnet.
     * **Destination range** : The range of the other workload subnets.
     * **Next hop** : Set the next hop to skip other policy-based routes and use default routing.



These instructions assume that all traffic other than traffic within a VPC subnet and between workload VPC subnets is routed through the NVAs. If you want traffic between workload VPCs and the services-access VPC to skip the NVAs, then install additional policy-based routing skip routes and configure additional Cloud NGFW rules for this traffic.

### Set up internet access in the internet access network

To configure outbound access to the internet, set up [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) in the internet access network.

### Test connectivity to workloads

If you have workloads already deployed in your VPC networks, test access to them now. If you connected the networks before deploying workloads, you can deploy them now and test.

## What's next

  * Learn more about the Google Cloud products used in this design guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)
    * [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Osvaldo Costa](https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer
  * Deepak Michael | Networking Specialist Customer Engineer
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking



Other contributor: [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
