---
url: https://docs.cloud.google.com/architecture/partners/palo-alto-networks-ngfw/
title: Secure virtual private cloud networks with the Palo Alto VM-Series NGFW \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:47.519809+00:00
---

# Secure virtual private cloud networks with the Palo Alto VM-Series NGFW  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/palo-alto-networks-ngfw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Secure virtual private cloud networks with the Palo Alto VM-Series NGFW Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-01-05 UTC

By: Matt McLimans, Technical Engagement Manager, [Palo Alto Networks](https://www.paloaltonetworks.com/)

This document describes the networking concepts that you need to understand to deploy Palo Alto Networks VM-Series next generation firewall (NGFW) in Google Cloud. This document is intended for network administrators, solution architects, and security professionals who are familiar with [Compute Engine](https://docs.cloud.google.com/compute) and [Virtual Private Cloud (VPC) networking](https://docs.cloud.google.com/vpc).

The VM-Series NGFW helps enterprises secure their applications, users, and other data deployed across Google Cloud and other virtualization environments.

Palo Alto Networks delivers zero-trust security capabilities for all enterprise networks by using the following approaches to threat prevention:

  * Securing all applications with Layer-7 inspection, granting access based on user identification, and preventing known and unknown threats.
  * Segmenting mission-critical applications and data using zero-trust principles to improve security posture and achieve compliance with various security standards—for example, PCI DSS.
  * Using [Panorama](https://www.paloaltonetworks.com/network-security/panorama) to centrally manage both physical and virtual firewalls. Panorama helps provide a consistent security posture across all hybrid and multicloud environments.
  * Using tooling to automate the deployment and configuration of VM-Series NGFWs.
  * Using predefined and custom network tags within security policies to dynamically update objects as Cloud workloads are created, moved, and destroyed.



The VM-Series NGFW helps secure workloads deployed across both your VPC networks and your remote networks. The actions in the following list correspond to the numbers in the following diagram.

  1. Prevent inbound threats from the internet to resources deployed in VPC networks, on-premises, and in other cloud environments.
  2. Stop outbound connections from VPC networks to suspicious destinations, such as command-and-control servers, or malicious code repositories.
  3. Prevent threats from moving laterally between workload VPC networks and stealing data.
  4. Secure traffic between remote networks connected through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect), [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview), or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  5. Help extend security to remote users and mobile devices to provide granular application access to Google Cloud resources.




![Network workloads that the VM-Series NGFW helps secure.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-01.svg)

For more information, see [VM-Series Virtual Next-Generation Firewalls](https://www.paloaltonetworks.com/resources/datasheets/vm-series-spec-sheet).

## Architecture

As shown in the following diagram, the VM-Series is deployed through Compute Engine. Securing the users, applications, and data residing in your VPC networks requires a minimum of three network interfaces. The network interfaces are as follows:

  * Management
  * Untrust
  * Trust



For more information, see [Multiple network interfaces overview and examples](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

The following diagram shows the components required to help secure network traffic with the VM-Series firewall. The management network provides access to on-premises networks to provide private access. The untrust network serves as the VM-Series user interface. It's common to connect the management network to an internet gateway for resources deployed to the trust network. The trust network contains the cloud workloads that you want to protect. Panorama Management provides centralized management of the VM-Series firewalls. You can deploy Panorama Management either as a compute instance in Google Cloud, or as a virtual or physical appliance in an on-premises data center.

![Network components and traffic patterns.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-02.svg)

### Components

The following sections explain the network components in more detail.

#### Untrust network

The untrust VPC interface serves as the internet gateway for resources deployed in a private network. To enable outbound internet connectivity from a private VPC network, either attach an [External IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) to the untrust interface, or deploy a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to a public VPC network. For inbound internet connectivity to private-network resources, you can achieve traffic distribution and high availability by configuring the interfaces to serve as the backend of the external load balancer. To serve as the backend of your [regional external passthrough Network Load Balancers and external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs), we recommend that you set the untrust interface as the primary VPC network interface through an [interface swap](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/deploy-vm-series-on-gcp/management-interface-mapping-for-google-internal-load-balancing.html).

#### Management network

The management interface is the primary network interface of the compute instance. The IP address of the management interface provides access to the VM-Series user interface and terminal console.

#### Instance group

We recommend that you deploy the VM-Series to an [instance group](https://docs.cloud.google.com/compute/docs/instance-groups). This approach lets you horizontally scale firewalls for resiliency and performance while managing the VM-Series NGFW as a single entity through a Palo Alto Networks Panorama appliance.

#### Trust network

The VM-Series trust interface is attached to a private VPC network. It's recommended that you set the trust interface as the backend of an Internal TCP/UDP Load Balancer to provide high availability. A private VPC network has a default route that points to either the trust network interface or the Internal TCP/UDP Load Balancer as the next hop. It's common for the private VPC network to be used as the following:

  * A shared VPC network that delegates its subnets to organization service projects
  * A hub VPC network that provides transitive routing and inspection for multiple VPC networks



#### Panorama

Panorama provides centralized management for all Palo Alto Networks firewalls. You can bootstrap deployed VM-Series firewalls to Panorama to receive all policy and network configurations. You can deploy Panorama in your on-premises data center or on Compute Engine. For more information, see [Panorama and Network Security Management](https://www.paloaltonetworks.com/network-security/panorama).

#### Management interface swap

For the VM-Series firewalls to receive traffic from any Google Cloud external load balancer, you must perform a [management interface swap](https://docs.paloaltonetworks.com/vm-series/10-1/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/deploy-vm-series-on-gcp/management-interface-mapping-for-google-internal-load-balancing.html). This swap also makes the untrust interface the primary interface of the compute instance. If you don't use load balancing, you should still perform an interface swap at deployment. If you don't perform an interface swap at deployment, you must redeploy the VM-Series.

## Value

Palo Alto Networks technologies span across major security controls. They help organizations accomplish the following goals:

  * Centralize management
  * Maintain optimum connectivity
  * Extend security policies and controls to the following control types: 
    * Users
    * Applications
    * Devices



Next-Generation Firewall platforms are available in the following form factors:

  * Physical
  * Virtual
  * Containerized
  * Cloud-delivered



## Costs

The VM-Series firewall supports the following license types:

  * BYOL
  * PayGo



It also supports the following two licensing models:

  * Software Next Generation firewall credits: Flexible configurations that you specify with a deployment profile
  * Fixed VM-Series Model configurations



Both models license security services and other features.

The VM-Series uses the following billable components of Google Cloud:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing)



For more information about licensing, see [VM-Series Firewall Licensing](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/license-the-vm-series-firewall/vm-series-firewall-licensing). To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator). New Google Cloud users might be eligible for a [free trial](https://cloud.google.com/free).

## Performance

We recommend using Cloud Load Balancing to distribute traffic to VM-Series firewalls deployed across regional zones. The VM-Series integrates with instance groups and [Google Cloud Observability](https://cloud.google.com/products/operations#section-4) to scale the number of firewalls based on custom metrics. For more information, see [Autoscaling the VM-Series Firewall on Google Cloud](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/autoscaling-on-google-cloud-platform.html).

Palo Alto Networks [Single-Pass Architecture](https://www.paloguard.com/SP3-Architecture.asp) processes the following items only once:

  * Network policy enforcement
  * Application identification
  * User controls
  * Content inspection



This check significantly reduces the processing overhead required to perform multiple functions on a single device. For more information, see [VM-Series on Google Cloud Performance and Capacity](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-performance-capacity/vm-series-performance-capacity/vm-series-on-google-performance-and-capacity).

## Use cases

The following sections explain the VPC network use cases in more detail.

### Secure multiple VPC networks

Because routing between subnetworks can't be overridden, consider segmenting your networks by allocating workloads to separate VPC networks. That way, the VM-Series firewalls can route and inspect all traffic that flows across the VPC network boundary. For more information about intra-VPC network traffic, see [Google Cloud IDS](https://cloud.google.com/blog/products/identity-security/how-google-cloud-ids-helps-detect-advanced-network-threats).

### Multiple network interface models

To help secure multiple networks, add additional VM-Series dataplane interfaces directly to your VPC networks. To steer traffic to the VM-Series NGFW interface, or to an Internal TCP/UDP Load Balancer (if multiple firewall VMs are used), use a [custom route](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes) for each connected network. There's a limit of eight network interfaces per virtual machine instance. After you create the instance, you can't add or remove network interfaces.

The following diagram shows a standard configuration of a VM Series deployment using multiple VM instances in an instance group (for high availability and performance):

![Instance groups and available network traffic patterns.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-03.svg)

The following examples show the different traffic patterns that run through the VM-Series firewalls in this configuration:

  1. An inbound request is made to an application hosted in VPC C. The external load balancer distributes the request to the VM-Series untrust interfaces. The VM-Series firewall inspects and forwards the request through the NIC4 in VPC C and to the destination application.
  2. The route table of VPC B routes traffic that is destined to the internet to the IP address of VPC B's Internal TCP/UDP Load Balancer. The load balancer distributes the traffic to NIC3 on the VM-Series firewalls. The VM-Series inspects and forwards the traffic through its untrust interface (NIC0) to the internet.
  3. A resource in VPC A makes a request to a resource in VPC B. The route table of VPC A routes the request to the Internal Load Balancer in VPC A. The load balancer distributes the request to NIC2 on the VM-Series firewalls. The VM-Series inspects and forwards the request through NIC3 to the resource in VPC B. VPC B routes its return traffic to its Internal TCP/UDP Load Balancer using the VPC B route table.



### VPC network peering model

[VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) helps you to build a hub and spoke topology to secure many VPC networks. Because you can add and remove spoke VPC networks as needed, network peering provides flexibility.

In the following diagram, VM-Series firewalls are deployed to an instance group to help secure traffic for various spoke VPC networks. The hub network contains the VM-Series trust interfaces. The trust interfaces are the backend of an Internal TCP/UDP Load Balancer. The spoke networks are VPC peers of the hub network. Each spoke has a custom default route that directs traffic to the IP address of the Internal TCP/UDP Load Balancer.

![Inspection patterns for network traffic.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-04.svg)

In the configuration displayed in the previous diagram, the VM-Series firewalls inspect the traffic as follows:

  1. Traffic from the internet to applications in the spoke networks are distributed by the regional external passthrough Network Load Balancer to the VM-Series untrust interfaces (NIC0). The VM-Series firewall inspects the traffic and forwards permissible traffic through its trust interface (NIC2) to the application in the spoke network.
  2. Traffic from the spoke networks destined to the internet are routed to the Internal TCP/UDP Load Balancer in the hub VPC. The VM-Series firewall inspects the traffic and forwards permissible traffic through its untrust interface (NIC0) to the internet.
  3. Traffic between spoke networks is routed to the Internal TCP/UDP Load Balancer in the hub VPC. The VM-Series firewall inspects and forwards the traffic through the trust interface (NIC2) into the hub network which routes permissible traffic to the destination spoke network.



You can combine the multiple network interface models and VPC network peering models to help scale security for many VPC networks by attaching additional VM-Series firewall interfaces to additional hub VPC networks. To do so, connect each interface and network to multiple spoke networks through VPC Network Peering.

### Distribute VM-Series firewalls

To help secure specific traffic flows, you can deploy VM-Series firewalls across independent dedicated instance groups. The distributed-firewall design provides traffic autonomy and the ability to scale instance groups independently. The following use cases are examples of how to distribute instance groups:

  * Securing traffic for networks that span multiple regions
  * Isolating traffic based on data classification and sensitivity



The following diagram is identical to the hub-and-spoke architecture with VPC Network Peering that was shown and discussed in the previous section. The difference is that the VM-Series firewalls are deployed in two managed instance groups.

The first managed instance group is inbound. It helps secure inbound traffic from the internet to applications hosted in the spoke networks.

The second managed instance group is outbound. It helps secure all egress traffic from the spoke networks and traffic from on-premises. This instance group provides traffic isolation with the ability to independently scale the VM-Series instance groups.

![Network traffic inspection configurations.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-05.svg)

The VM-Series firewalls in the configuration displayed in the previous diagram inspect traffic as follows:

  1. Traffic from the internet to applications in the spoke networks is distributed by the regional external passthrough Network Load Balancer to the untrust interfaces on the inbound instance group. The inbound instance group inspects all traffic and forwards permissible traffic through NIC2 to the application in the spoke network.
  2. Traffic from the spoke networks destined to the internet is routed to the Internal TCP/UDP Load Balancer in the hub VPC. The load balancer distributes the traffic to NIC2 on the outbound instance group. The VM-Series inspects and forwards permissible traffic through its untrust interface (NIC0) and to the internet.
  3. Traffic between spoke networks and the remote network is routed to the Internal TCP/UDP Load Balancer in the hub VPC. The load balancer distributes permissible traffic to NIC2 on the outbound instance group. The VM-Series firewall inspects and forwards permissible traffic through NIC2 where the hub network routes that traffic to the adjacent spoke network.



### Active/passive model

You can configure the VM-Series firewalls as an [active/passive high availability (HA) pair](https://docs.paloaltonetworks.com/vm-series/11-0/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/setup-active-passive-ha-on-gcp/architecture-of-gcp-ha). In this model, each VM-Series firewall belongs to an unmanaged instance group. Only the primary VM-Series firewall receives network traffic from [Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). The health check configured on the load balancers determines the HA state of the primary VM-Series firewall. If the health check fails on the primary VM-Series firewall, the load balancers carry the active sessions to the secondary VM-Series firewall. At that point, the secondary VM-Series firewall becomes the primary firewall.

This model is suited for environments with any or all of the following requirements:

  * Maintenance of session continuity through stateful failover between VM-Series firewalls.
  * Establishment of static IPsec tunnels directly to the VM-Series firewall.
  * Preservation of the original client IP address for internet inbound traffic to internal applications protected by the VM-Series firewalls.

**Note:** There's no need to horizontally scale the VM-Series firewalls.

![Instance groups and available network traffic patterns with an active/passive HA pair.](https://docs.cloud.google.com/static/architecture/images/partners/palo-alto-networks-ngfw-06.svg)

The topology and traffic patterns are almost identical to the previous models, with the following exceptions:

  1. nic1 serves as the management and HA1 interface. The HA1 interface synchronizes configuration changes between the VM-Series firewalls.
  2. An additional interface, HA2 (nic3), is attached to the VM-Series firewalls. The HA2 interface exchanges session tables between the active/passive pair.
  3. The external and internal TCP/UDP load balancers are configured with [Connection Tracking](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-tracking) to track sessions through the VM-Series firewalls.



For more information, see [VM-Series on Google Cloud](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/about-the-vm-series-firewall-on-google-cloud-platform.html).

## What's next

  * Learn about the [VM-Series on Google Cloud](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/set-up-the-vm-series-firewall-on-google-cloud-platform/about-the-vm-series-firewall-on-google-cloud-platform.html).
  * Learn about [VM-Series licensing on all platforms](https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/license-the-vm-series-firewall/vm-series-firewall-licensing.html#id8fea514c-0d85-457f-b53c-d6d6193df07c).
  * Watch the [VM-Series capabilities in Google Cloud](https://www.youtube.com/watch?v=V_28r5fjShU).
  * Try the [Secure Google Cloud Hub-and-Spoke with VM-Series](https://github.com/PaloAltoNetworks/google-cloud-hub-spoke-tutorial) tutorial.
  * Try the [VM-Series Active/Passive HA on Google Cloud](https://github.com/PaloAltoNetworks/google-cloud-vmseries-ha-tutorial/tree/main) tutorial.
  * Deploy a hub-and-spoke network using [VPC Network Peering](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/blueprints/networking/hub-and-spoke-peering).
  * Learn about more design options for [connecting multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-01-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-01-05 UTC."],[],[]] 
