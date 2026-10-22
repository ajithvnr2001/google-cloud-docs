---
url: https://docs.cloud.google.com/architecture/landing-zones/decide-network-design/
title: Decide the network design for your Google Cloud landing zone \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:57.905167+00:00
---

# Decide the network design for your Google Cloud landing zone  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/decide-network-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Decide the network design for your Google Cloud landing zone Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

When you design your landing zone, you must choose a network design that works for your organization. This document describes four common network designs, and helps you choose the option that best meets your organization's requirements, and your organization's preference for centralized control or decentralized control. It's intended for network engineers, architects, and technical practitioners who are involved in creating the network design for your organization's landing zone.

This article is part of a series about [landing zones](https://docs.cloud.google.com/architecture/landing-zones).

## Choose your network design

The network design that you choose depends primarily on the following factors:

  * **Centralized or decentralized control:** Depending on your organization's preferences, you must choose one of the following: 
    * Centralize control over the network including IP addressing, routing, and firewalling between different workloads.
    * Give your teams greater autonomy in running their own environments and building network elements within their environments themselves.
  * **On-premises or hybrid cloud connectivity options:** All the network designs discussed in this document provide access from on-premises to cloud environments through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview). However, some designs require you to set up multiple connections in parallel, while others use the same connection for all workloads.
  * **Security requirements:** Your organization might require traffic between different workloads in Google Cloud to pass through centralized network appliances such as [next generation firewalls (NGFW)](https://en.wikipedia.org/wiki/Next-generation_firewall). This constraint influences your Virtual Private Cloud (VPC) network design.
  * **Scalability:** Some designs might be better for your organization than others, based on the number of workloads that you want to deploy, and the number of virtual machines (VMs), internal load balancers, and other resources that they will consume.



## Decision points for network design

The following flowchart shows the decisions that you must make to choose the best network design for your organization.

![Decisions for network designs.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-network-design-flow.svg)

The preceding diagram guides you through the following questions:

  1. Do you require [Layer 7](https://en.wikipedia.org/wiki/OSI_model#Layer_7:_Application_layer) inspection using network appliances between different workloads in Google Cloud? 
     * If yes, see Hub-and-spoke topology with centralized appliances.
     * If no, proceed to the next question.
  2. Do many of your workloads require on-premises connectivity? 
     * If yes, go to decision point 4.
     * If no, proceed to the next question.
  3. Can your workloads communicate using private endpoints in a service producer and consumer model? 
     * If yes, see Expose services in a consumer-producer model with Private Service Connect.
     * If no, proceed to the next question.
  4. Do you want to administer firewalling and routing centrally? 
     * If yes, see Shared VPC network for each environment.
     * If no, see Hub-and-spoke topology without appliances.



This chart is intended to help you make a decision, however, it can often be the case that multiple designs might be suitable for your organization. In these instances, we recommend that you choose the design that fits best with your use case.

## Network design options

The following sections describe four common design options. We recommend option 1 for most use cases. The other designs discussed in this section are alternatives that apply to specific organizational edge-case requirements.

The best fit for your use case might also be a network that combines elements from multiple design options discussed in this section. For example, you can use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks in hub-and-spoke topologies for better collaboration, centralized control, and to limit the number of VPC spokes. Or, you might design most workloads in a Shared VPC topology but isolate a small number of workloads in separate VPC networks that only expose services through a few defined endpoints using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

**Note:** When the design options refer to connections to on-premises networks, you can use the same concepts for connections to other cloud service providers (CSPs) using [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

### Option 1: Shared VPC network for each environment

We recommend this network design for most use cases. This design uses separate Shared VPC networks for each deployment environment that you have in Google Cloud (development, testing, and production). This design lets you centrally manage network resources in a common network and provides network isolation between the different environments.

Use this design when the following is true:

  * You want central control over firewalling and routing rules.
  * You need a simple, scalable infrastructure.
  * You need centralized IP address space management.



Avoid this design when the following is true:

  * You want developer teams to have full autonomy, including the ability to manage their own firewall rules, routing, and peering to other team networks.
  * You need Layer 7 inspection using NGFW appliances.



The following diagram shows an example implementation of this design.

![Option 1 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-network-design-option1.svg)

The preceding diagram shows the following:

  * The on-premises network is spread across two geographical locations.
  * The on-premises network connects through redundant Cloud Interconnect instances to two separate Shared VPC networks, one for production and one for development.
  * The production and development environments are connected to both Cloud Interconnect instances with different [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).
  * Each Shared VPC has service projects that host the workloads.
  * Firewall rules are centrally administered in the host project.
  * The development environment has the same VPC structure as the production environment.



By design, traffic from one environment cannot reach another environment. However, if specific workloads must communicate with each other, you can allow data transfer through controlled channels on-premises, or you can share data between applications with Google Cloud services like [Cloud Storage](https://docs.cloud.google.com/storage) or [Pub/Sub](https://docs.cloud.google.com/pubsub). We recommend that you avoid directly connecting separated environments through VPC Network Peering, because it increases the risk of accidentally mixing data between the environments. Using VPC Network Peering between large environments also increases the risk of hitting [VPC quotas](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering) around peering and peering groups.

For more information, see the following:

  * [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Shared VPC architecture in the enterprise foundations guide](https://docs.cloud.google.com/architecture/security-foundations/networking#dual-shared-vpc-network-topology)
  * [Reference architecture in VPC design best practices](https://docs.cloud.google.com/architecture/best-practices-vpc-design#multiple-host-project-multiple-service-projects-multiple-shared-vpc)
  * [Network stage for Terraform example foundation](https://github.com/terraform-google-modules/terraform-example-foundation/tree/main/3-networks-svpc) using [Cloud Foundation toolkit](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit)



To implement this design option, see [Create option 1: Shared VPC network for each environment](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design#option-1-shared-vpc-network-for-each-environment).

### Option 2: Hub-and-spoke topology with centralized appliances

This network design uses hub-and-spoke topology. A hub VPC network contains a set of appliance VMs such as NGFWs that are connected to the spoke VPC networks that contain the workloads. Traffic between the workloads, on-premises networks, or the internet is routed through appliance VMs for inspection and filtering.

Use this design when the following is true:

  * You require Layer 7 inspection between different workloads or applications.
  * You have a corporate mandate that specifies the security appliance vendor for all traffic.



Avoid this design when the following is true:

  * You don't require Layer 7 inspection for most of your workloads.
  * You want workloads on Google Cloud to not communicate at all with each other.
  * You only need Layer 7 inspection for traffic going to on-premises networks.



The following diagram shows an example implementation of this pattern.

![Option 2 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-network-design-option2.svg)

The preceding diagram shows the following:

  * A production environment which includes a hub VPC network and multiple spoke VPC networks that contain the workloads.
  * The spoke VPC networks are connected with the hub VPC network by using VPC Network Peering.
  * The hub VPC network has multiple instances of a virtual appliance in a managed instance group. Traffic to the managed instance group goes through an internal passthrough Network Load Balancer.
  * The spoke VPC networks communicate with each other through the virtual appliances by using static routes with the internal load balancer as the next hop.
  * Cloud Interconnect connects the transit VPC networks to on-premises locations.
  * On-premises networks are connected through the same Cloud Interconnects using separate VLAN attachments.
  * The transit VPC networks are connected to a separate network interface on the virtual appliances, which lets you inspect and filter all traffic to and from these networks by using your appliance.
  * The development environment has the same VPC structure as the production environment.
  * This setup doesn't use source network address translation (SNAT). SNAT isn't required because Google Cloud uses _symmetric hashing_. For more information see [Symmetric hashing](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#symmetric-hashing).



By design, traffic from one spoke network cannot reach another spoke network. However, if specific workloads must communicate with each other, you can set up direct peering between the spoke networks using VPC Network Peering, or you can share data between applications with Google Cloud services like Cloud Storage or Pub/Sub.

To maintain low latency when the appliance communicates between workloads, the appliance must be in the same [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) as the workloads. If you use multiple regions in your cloud deployment, you can have one set of appliances and one hub VPC for each environment in each region. Alternatively, you can use [network tags with routes](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#interaction_with_routes) to have all instances communicate with the closest appliance.

[Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) can restrict the connectivity within the spoke VPC networks that contain workloads. Often, teams who administer the workloads also administer these firewall rules. For central policies, you can use [hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies). If you require a central network team to have full control over firewall rules, consider centrally deploying those rules in all VPC networks by using a [GitOps approach](https://docs.cloud.google.com/architecture/managing-infrastructure-as-code). In this case, restrict the IAM permissions to only those administrators who can change the firewall rules. Spoke VPC networks can also be Shared VPC networks if multiple teams deploy in the spokes.

In this design, we recommend that you use VPC Network Peering to connect the hub VPC network and spoke VPC networks because it adds minimum complexity. However, the maximum number of spokes is limited by the following:

  * The limit on [VPC Network Peering connections ](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering)from a single VPC network.
  * Peering group limits such as the maximum number of forwarding rules for the internal TCP/UDP Load Balancing for each peering group.



If you expect to reach these limits, you can connect the spoke networks through Cloud VPN. Using Cloud VPN adds extra cost and complexity and each Cloud VPN tunnel has a bandwidth limit.

For more information, see the following:

  * [Hub and spoke transitivity architecture in the enterprise foundations guide](https://docs.cloud.google.com/architecture/security-foundations/networking#hub-spoke-network-topology)
  * [Hub and spoke with Network Virtual Appliance (NVA)](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast/stages/2-networking/datasets/hub-and-spokes-nva) as part of the Fabric FAST framework
  * [Terraform hub-and-spoke transitivity module](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/3-networks-hub-and-spoke/modules/transitivity) as part of the [example foundation](https://github.com/terraform-google-modules/terraform-example-foundation)



To implement this design option, see [Create option 2: Hub-and-spoke topology with centralized appliances](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design#create_option_2_hub-and-spoke_topology_with_centralized_appliances).

### Option 3: Hub-and-spoke topology without appliances

This network design also uses a hub-and-spoke topology, with a hub VPC network that connects to on-premises networks and spoke VPC networks that contain the workloads. Because VPC Network Peering is non-transitive, spoke networks cannot communicate with each other directly.

Use this design when the following is true:

  * You want workloads or environments in Google Cloud to not communicate with each other at all using internal IP addresses, but you do want them to share on-premises connectivity.
  * You want to give teams autonomy in managing their own firewall and routing rules.



Avoid this design when the following is true:

  * You require Layer 7 inspection between workloads.
  * You want to centrally manage routing and firewall rules.
  * You require communications from on-premises services to managed services that are connected to the spokes through another VPC Network Peering, because VPC Network Peering is non-transitive.



The following diagram shows an example implementation of this design.

![Option 3 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-network-design-option3.svg)

The preceding diagram shows the following:

  * A production environment which includes a hub VPC network and multiple spoke VPC networks that contain the workloads.
  * The spoke VPC networks are connected with the hub VPC network by using VPC Network Peering.
  * Connectivity to on-premises locations passes through Cloud Interconnect connections in the hub VPC network.
  * On-premises networks are connected through the Cloud Interconnect instances using separate VLAN attachments.
  * The development environment has the same VPC structure as the production environment.



By design, traffic from one spoke network cannot reach another spoke network. However, if specific workloads must communicate with each other, you can set up direct peering between the spoke networks using VPC Network Peering, or you can share data between applications with Google Cloud services like Cloud Storage or Pub/Sub.

This network design is often used in environments where teams act autonomously and there is no centralized control over firewall and routing rules. However, the scale of this design is limited by the following:

  * The limit on [VPC Network Peering connections from a single VPC network](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering)

  * Peering group limits such as the maximum number of forwarding rules for the internal passthrough Network Load Balancer for each peering group




Therefore, this design is not typically used in large organizations that have many separate workloads on Google Cloud.

As a variation to the design, you can use Cloud VPN instead of VPC Network Peering. Cloud VPN lets you increase the number of spokes, but adds a [bandwidth limit for each tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits) and increases complexity and costs. When you use [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip), Cloud VPN also allows for transitivity between the spokes without requiring you to directly connect all the spoke networks.

For more information, see the following:

  * [Hub-and-spoke network architecture](https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology)
  * [Hub-and-spoke architecture in the enterprise foundations guide](https://docs.cloud.google.com/architecture/security-foundations/networking#hub-spoke-network-topology)
  * [Hub and spoke with VPC Peerings](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast/stages/2-networking/datasets/hub-and-spokes-peerings) as part of the Fabric FAST framework
  * [NCC Hub and spoke](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast/stages/2-networking/datasets/hub-and-spokes-ncc) as part of Fabric FAST framework



To implement this design option, see [Create option 3: Hub-and-spoke topology without appliances](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design#create_option_3_hub-and-spoke_topology_without_appliances).

### Option 4: Expose services in a consumer-producer model with Private Service Connect

In this network design, each team or workload gets their own VPC network, which can also be a Shared VPC network. Each VPC network is independently managed and uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to expose all the services that need to be accessed from outside the VPC network.

Use this design when the following is true:

  * Workloads only communicate with each other and the on-premises environment through defined endpoints.
  * You want teams to be independent of each other, and manage their own IP address space, firewalls, and routing rules.



Avoid this design when the following is true:

  * Communication between services and applications uses many different ports or channels, or ports and channels change frequently.
  * Communication between workloads uses protocols other than TCP or UDP.
  * You require Layer 7 inspection between workloads.



The following diagram shows an example implementation of this pattern.

![Option 4 diagram.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-network-design-option4.svg)

The preceding diagram shows the following:

  * Separate workloads are located in separate projects and VPC networks.
  * A client VM in one VPC network can connect to a workload in another VPC network through a Private Service Connect endpoint.
  * The endpoint is attached to a service attachment in the VPC network where the service is located. The service attachment can be in a different region from the endpoint if the endpoint is configured for [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access).
  * The service attachment connects to the workload through Cloud Load Balancing.
  * Clients in the workload VPC can reach workloads that are located on-premises as follows: 
    * The endpoint is connected to a service attachment in a transit VPC network.
    * The service attachment is connected to the on-premises network using Cloud Interconnect.
  * An internal Application Load Balancer is attached to the service attachment and uses a hybrid network endpoint group to balance traffic load between the endpoints that are located on-premises.
  * On-premises clients can also reach endpoints in the transit VPC network that connect to service attachments in the workload VPC networks.



For more information, see the following:

  * [Publish managed services using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)
  * [Access published services through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services)



To implement this design option, see [Create option 4: Expose services in a consumer-producer model with Private Service Connect](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design#option-4-psc).

## Best practices for network deployment

After you choose the best network design for your use case, we recommend implementing the following best practices:

  * [Use custom mode VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#custom-mode) and delete the default network to have better control over your network's IP addresses.
  * [Limit external access](https://docs.cloud.google.com/architecture/best-practices-vpc-design#limit-access) by using Cloud NAT for resources that need internet access and reducing the use of public IP addresses to resources accessible through Cloud Load Balancing. For more information, see [Alternatives to using an external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#ext-ip-alternatives).

  * If you use Cloud Interconnect, make sure that you follow the recommended topologies for [non-critical](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/non-critical-overview) or [production-level applications](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview). Use redundant connections to meet the SLA for the service. Alternatively, you can connect Google Cloud to on-premises networks through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * Enforce the policies introduced in [limit external access by using an organization policy](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design#limit_external_access_by_using_an_organization_policy) to restrict direct access to the internet from your VPC.

  * Use [hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies) to inherit firewall policies consistently across your organization or folders.

  * Follow [DNS best practices](https://docs.cloud.google.com/dns/docs/best-practices) for hybrid DNS between your on-premises network and Google Cloud.




For more information, see [Best practices and reference architectures for VPC design](https://docs.cloud.google.com/architecture/best-practices-vpc-design).

## What's next

  * [Implement your Google Cloud landing zone network design](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design)
  * [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security) (next document in this series).
  * Read [Best practices for VPC network design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).
  * Read more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
