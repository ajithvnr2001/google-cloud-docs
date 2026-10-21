---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking/
title: Networking \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:29.307595+00:00
---

# Networking  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Networking Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

Networking is required for resources to communicate within your Google Cloud organization and between your cloud environment and on-premises environment. This section describes the structure in the blueprint for VPC networks, IP address space, DNS, firewall policies, and connectivity to the on-premises environment.

## Network topology

The blueprint repository provides the following options for your network topology:

  * Use separate Shared VPC networks for each environment, with no network traffic directly allowed between environments.
  * Use a hub-and-spoke model that adds a hub network to connect each environment in Google Cloud, with the network traffic between environments gated by a network virtual appliance (NVA).



Choose the Shared VPC network for each environment topology when you don't want direct network connectivity between environments. Choose the hub-and-spoke network topology when you want to allow network connectivity between environments that is filtered by an NVA, such as when you rely on existing tools that require a direct network path to every server in your environment.

Both topologies use Shared VPC as a principal networking construct because Shared VPC allows a clear separation of responsibilities. Network administrators manage network resources in a centralized host project, and workload teams deploy their own application resources and consume the network resources in service projects that are attached to the host project.

### Shared VPC network for each environment topology

If you require network isolation between your development, non-production, and production networks on Google Cloud, we recommend the Shared VPC network for each environment topology. This topology allows no network traffic between environments.

The following diagram shows the Shared VPC network for each environment topology.

![The blueprint VPC network.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-vpc-network.svg)

The diagram describes the following key concepts of the Shared VPC for each environment topology:

  * Each environment (production, non-production, and development) has one Shared VPC network. This diagram shows only the production environment, but the same pattern is repeated for each environment.
  * Each Shared VPC network has two subnets, with each subnet in a different [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).
  * Connectivity with on-premises resources is enabled through four VLAN attachments to the Dedicated Interconnect instance for each Shared VPC network, using four Cloud Router services (two in each region for redundancy). For more information, see Hybrid connectivity between on-premises environment and Google Cloud.



By design, this topology doesn't allow network traffic to flow directly between environments. If you do require network traffic to flow directly between environments, you must take additional steps to allow this network path. For example, you might [configure Private Service Connect endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) to expose a service from one VPC network to another VPC network. Alternatively, you might configure your on-premises network to let traffic flow from one Google Cloud environment to the on-premises environment and then to another Google Cloud environment.

### Hub-and-spoke network topology

If you deploy resources in Google Cloud that require a direct network path to resources in multiple environments, we recommend the hub-and-spoke network topology.

The hub-and-spoke topology uses several of the concepts that are part of the Shared VPC network for each environment topology, but modifies the topology to add a hub network. The following diagram shows the hub-and-spoke topology.

![The example.com VPC network structure when using hub-and-spoke
connectivity based on VPC peering.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-hub-spoke.svg)

The diagram describes these key concepts of hub-and-spoke network topology:

  * This model adds a hub network, and each of the development, non-production, and production networks (spokes) are connected to the hub network through VPC Network Peering. Alternatively, if you anticipate exceeding [the quota limit](https://docs.cloud.google.com/vpc/docs/quota#per_network), you can use an [HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies) instead.
  * Connectivity to on-premises networks is allowed only through the hub network. All spoke networks can communicate with shared resources in the hub network and use this path to connect to on-premises networks.
  * The hub networks include an NVA for each region, deployed redundantly behind internal Network Load Balancer instances. This NVA serves as the gateway to allow or deny traffic to communicate between spoke networks.
  * The hub network also hosts tooling that requires connectivity to all other networks. For example, you might deploy tools on VM instances for configuration management to the common environment.



To enable spoke-to-spoke traffic, the blueprint deploys NVAs on the hub Shared VPC network that act as gateways between networks. Routes are exchanged from hub-to-spoke VPC networks through [custom routes exchange](https://docs.cloud.google.com/vpc/docs/vpc-peering#custom-route-exchange). In this scenario, connectivity between spokes must be routed through the NVA because VPC Network Peering is non-transitive, and therefore, spoke VPC networks can't exchange data with each other directly. You must configure the virtual appliances to selectively allow traffic between spokes.

## Project deployment patterns

When creating new projects for workloads, you must decide how resources in this project connect to your existing network. The following table describes the patterns for deploying projects that are used in the blueprint.

Pattern | Description | Example usage  
---|---|---  
Shared VPC service projects | These projects are configured as service projects to a Shared VPC host project. Use this pattern when resources in your project have the following criteria:

  * Require network connectivity to the on-premises environment or resources in the same Shared VPC topology.

| [example_shared_vpc_project.tf](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/4-projects/modules/base_env/example_shared_vpc_project.tf)  
Floating projects |  Floating projects are not connected to other VPC networks in your topology. Use this pattern when resources in your project have the following criteria:

  * Don't require full mesh connectivity to an on-premises environment or resources in the Shared VPC topology.
  * Don't require a VPC network, or you want to manage the VPC network for this project independently of your main VPC network topology (such as when you want to use an IP address range that clashes with the ranges already in use).

You might have a scenario where you want to keep the VPC network of a floating project separate from the main VPC network topology but also want to expose a limited number of endpoints between networks. In this case, [publish services by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) to share network access to an individual endpoint across VPC networks without exposing the entire network. | [example_floating_project.tf](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/4-projects/modules/base_env/example_floating_project.tf)  
Peering projects |  Peering projects create their own VPC networks and peer to other VPC networks in your topology. Use this pattern when resources in your project have the following criteria:

  * Require network connectivity in the directly peered VPC network, but don't require transitive connectivity to an on-premises environment or other VPC networks.
  * Must manage the VPC network for this project independently of your main network topology.

If you create peering projects, it's your responsibility to allocate non-conflicting IP address ranges and plan for [peering group quota](https://docs.cloud.google.com/vpc/docs/quota#per_network). | [example_peering_project.tf](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/4-projects/modules/base_env/example_peering_project.tf)  
  
## IP address allocation

This section introduces how the blueprint architecture allocates IP address ranges. You might need to change the specific IP address ranges used based on the IP address availability in your existing hybrid environment.

The following table provides a breakdown of the IP address space that's allocated for the blueprint. The hub environment only applies in the hub-and-spoke topology.

Purpose | Region | Hub environment | Development environment | Non-production environment | Production environment  
---|---|---|---|---|---  
Primary subnet ranges | Region 1 | 10.8.0.0/18 | 10.8.64.0/18 | 10.8.128.0/18 | 10.8.192.0/18  
Region 2 | 10.9.0.0/18 | 10.9.64.0/18 | 10.9.128.0/18 | 10.9.192.0/18  
Unallocated | 10.{10-15}.0.0/18 | 10.{10-15}.64.0/18 | 10.{10-15}.128.0/18 | 10.{10-15}.192.0/18  
Private services access | Global | 10.16.32.0/21 | 10.16.40.0/21 | 10.16.48.0/21 | 10.16.56.0/21  
Private Service Connect endpoints | Global | 10.17.0.5/32 | 10.17.0.6/32 | 10.17.0.7/32 | 10.17.0.8/32  
Proxy-only subnets | Region 1 | 10.26.0.0/23 | 10.26.2.0/23 | 10.26.4.0/23 | 10.26.6.0/23  
Region 2 | 10.27.0.0/23 | 10.27.2.0/23 | 10.27.4.0/23 | 10.27.6.0/23  
Unallocated | 10.{28-33}.0.0/23 | 10.{28-33}.2.0/23 | 10.{28-33}.4.0/23 | 10.{28-33}.6.0/23  
Secondary subnet ranges | Region 1 | 100.72.0.0/18 | 100.72.64.0/18 | 100.72.128.0/18 | 100.72.192.0/18  
Region 2 | 100.73.0.0/18 | 100.73.64.0/18 | 100.73.128.0/18 | 100.73.192.0/18  
Unallocated | 100.{74-79}.0.0/18 | 100.{74-79}.64.0/18 | 100.{74-79}.128.0/18 | 100.{74-79}.192.0/18  
  
The preceding table demonstrates these concepts for allocating IP address ranges:

  * IP address allocation is subdivided into ranges for each combination of purpose, region, and environment.
  * Some resources are global and don't require subdivisions for each region.
  * By default, for regional resources, the blueprint deploys in two regions. In addition, there are unused IP address ranges so that you can can expand into six additional regions.
  * The hub network is only used in the hub-and-spoke network topology, while the development, non-production, and production environments are used in both network topologies.



The following table introduces how each type of IP address range is used.

Purpose | Description  
---|---  
Primary subnet ranges | Resources that you deploy to your VPC network, such as virtual machine instances, use internal IP addresses from these ranges.  
Private services access | Some Google Cloud services such as Cloud SQL require you to preallocate a subnet range for [private services access](https://docs.cloud.google.com/service-infrastructure/docs/enabling-private-services-access). The blueprint reserves a /21 range globally for each of the Shared VPC networks to allocate IP addresses for services that require private services access. When you create a service that depends on private services access, you allocate a regional /24 subnet from the reserved /21 range.  
Private Service Connect | The blueprint provisions each VPC network with a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint to communicate with Google Cloud APIs. This endpoint lets your resources in the VPC network reach Google Cloud APIs without relying on outbound traffic to the internet or publicly advertised internet ranges.  
Proxy-based load balancers | Some types of Application Load Balancers require you to preallocate [proxy-only subnets](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets). Although the blueprint doesn't deploy Application Load Balancers that require this range, allocating ranges in advance helps reduce friction for workloads when they need to request a new subnet range to enable certain load balancer resources.  
Secondary subnet ranges | Some use cases, such as container-based workloads, require [secondary ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Although the blueprint doesn't deploy services that require secondary ranges, it allocates ranges from the RFC 6598 IP address space for secondary ranges. Alternatively, if you struggle to allocate sufficiently large CIDR blocks for these services, you might consider deploying those services in the floating project pattern introduced in the project deployment patterns section.   
  
## Centralized DNS setup

For DNS resolution between Google Cloud and on-premises environments, we recommend that you use a hybrid approach with two authoritative DNS systems. In this approach, Cloud DNS handles authoritative DNS resolution for your Google Cloud environment and your existing on-premises DNS servers handle authoritative DNS resolution for on-premises resources. Your on-premises environment and Google Cloud environment perform DNS lookups between environments through forwarding requests.

The following diagram demonstrates the DNS topology across the multiple VPC networks that are used in the blueprint.

![Cloud DNS setup for the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-dns-setup.svg)

The diagram describes the following components of the DNS design that is deployed by the blueprint:

  * The DNS hub is the central point of DNS exchange between the on-premises environment and the Google Cloud environment. DNS forwarding uses the same Dedicated Interconnect instances and Cloud Routers that are already configured in your network topology. 
    * In the Shared VPC network for each environment topology, the DNS project is the same as the production Shared VPC host project.
    * In the hub-and-spoke topology, the DNS hub project is the same as the hub Shared VPC host project.
  * Servers in each Shared VPC network can resolve DNS records from other Shared VPC networks through [DNS forwarding](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods), which is configured between Cloud DNS in each Shared VPC host project and the DNS hub.
  * On-premises servers can resolve DNS records in Google Cloud environments using [DNS server policies](https://docs.cloud.google.com/dns/docs/best-practices#use_dns_server_policies_to_allow_queries_from_on-premises) that allow queries from on-premises servers. The blueprint configures an inbound server policy in the DNS hub to allocate IP addresses, and the on-premises DNS servers forward requests to these addresses. All DNS requests to Google Cloud reach the DNS hub first, which then resolves records from DNS peers.
  * Servers in Google Cloud can resolve DNS records in the on-premises environment using [forwarding zones](https://docs.cloud.google.com/dns/docs/best-practices#use_forwarding_zones_to_query_on-premises_servers) that query on-premises servers. All DNS requests to the on-premises environment originate from the DNS hub. The DNS request source is 35.199.192.0/19.



## Firewall policies

Google Cloud has multiple [firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) types. Hierarchical firewall policies are enforced at the organization or folder level to inherit firewall policy rules consistently across all resources in the hierarchy. In addition, you can configure network firewall policies for each VPC network. The blueprint combines these firewall policies to enforce common configurations across all environments using Hierarchical firewall policies and to enforce more specific configurations at each individual VPC network using network firewall policies.

The blueprint doesn't use [legacy VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls). We recommend using only firewall policies and avoid mixing use with legacy VPC firewall rules.

### Hierarchical firewall policies

The blueprint defines a single [hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies) and attaches the policy to each of the production, non-production, development, bootstrap, and common folders. This hierarchical firewall policy contains the rules that should be enforced broadly across all environments, and delegates the evaluation of more granular rules to the network firewall policy for each individual environment.

The following table describes the hierarchical firewall policy rules deployed by the blueprint.

Rule description | Direction of traffic | Filter (IPv4 range) | Protocols and ports | Action  
---|---|---|---|---  
Delegate the evaluation of inbound traffic from RFC 1918 to lower levels in the hierarchy. | `Ingress` | 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12 | `all` | `Go to next`  
Delegate the evaluation of outbound traffic to RFC 1918 to lower levels in the hierarchy. | `Egress` | 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12 | `all` | `Go to next`  
[IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) | `Ingress` | 35.235.240.0/20 | `tcp:22,3389` | `Allow`  
[Windows server activation](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances) | `Egress` | 35.190.247.13/32 | `tcp:1688` | `Allow`  
[Health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule) for Cloud Load Balancing | `Ingress` | 130.211.0.0/22, 35.191.0.0/16, 209.85.152.0/22, 209.85.204.0/22 | `tcp:80,443` | `Allow`  
  
### Network firewall policies

The blueprint configures a [network firewall policy](https://docs.cloud.google.com/vpc/docs/network-firewall-policies) for each network. Each network firewall policy starts with a minimum set of rules that allow access to Google Cloud services and deny egress to all other IP addresses.

In the hub-and-spoke model, the network firewall policies contain additional rules to allow communication between spokes. The network firewall policy allows outbound traffic from one to the hub or another spoke, and allows inbound traffic from the NVA in the hub network.

The following table describes the rules in the global network firewall policy deployed for each VPC network in the blueprint.

Rule description | Direction of traffic | Filter | Protocols and ports  
---|---|---|---  
Allow outbound traffic to Google Cloud APIs. | `Egress` | The Private Service Connect endpoint that is configured for each individual network. See Private access to Google APIs. | `tcp:443`  
Deny outbound traffic not matched by other rules. | `Egress` | all | `all`  
Allow outbound traffic from one spoke to another spoke (for hub-and-spoke model only). | `Egress` | The aggregate of all IP addresses used in the hub-and-spoke topology. Traffic that leaves a spoke VPC is routed to the NVA in the hub network first. | `all`  
Allow inbound traffic to a spoke from the NVA in the hub network (for hub-and-spoke model only). | `Ingress` | Traffic originating from the NVAs in the hub network. | `all`  
  
When you first deploy the blueprint, a VM instance in a VPC network can communicate with Google Cloud services, but not to other infrastructure resources in the same VPC network. To allow VM instances to communicate, you must add additional rules to your network firewall policy and [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) that explicitly allow the VM instances to communicate. Tags are added to VM instances, and traffic is evaluated against those tags. Tags additionally have IAM controls so that you can define them centrally and delegate their use to other teams.

**Note:** All references to tags in this document refer to [tags with IAM controls](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). We don't recommend VPC firewall rules with [legacy network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

The following diagram shows an example of how you can add custom tags and network firewall policy rules to let workloads communicate inside a VPC network.

![Firewall rules in example.com.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-firewall-rules.svg)

The diagram demonstrates the following concepts of this example:

  * The network firewall policy contains Rule 1 that denies outbound traffic from all sources at priority 65530.
  * The network firewall policy contains Rule 2 that allows inbound traffic from instances with the `service=frontend` tag to instances with the `service=backend` tag at priority 999.
  * The instance-2 VM can receive traffic from instance-1 because the traffic matches the tags allowed by Rule 2. Rule 2 is matched before Rule 1 is evaluated, based on the priority value.
  * The instance-3 VM doesn't receive traffic. The only firewall policy rule that matches this traffic is Rule 1, so outbound traffic from instance-1 is denied.



## Private access to Google Cloud APIs

To let resources in your VPC networks or on-premises environment reach Google Cloud services, we recommend private connectivity instead of outbound internet traffic to public API endpoints. The blueprint configures [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on every subnet, creates internal endpoints with [Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to communicate with Google Cloud services, and configures firewall policies and DNS records to allow traffic to those endpoints. Used together, these controls allow a private path to Google Cloud services, without relying on internet outbound traffic or publicly advertised internet ranges.

The blueprint configures Private Service Connect endpoints with the [API bundle](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis) called `vpc-sc`, which allows access to the Google Cloud [services supported by the restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services). This control helps mitigate exfiltration risk by preventing access to other Google APIs not related to Google Cloud. This control is also a prerequisite step for enabling VPC Service Controls. For more information about the optional steps to enable VPC Service Controls, see [protect your resources with VPC Service Controls](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#protect-resources).

The following table describes the Private Service Connect endpoints created for each network.

Environment | API bundle | Private Service Connect endpoint IP address  
---|---|---  
Common | `vpc-sc` | 10.17.0.5/32  
Development | `vpc-sc` | 10.17.0.6/32  
Non-production | `vpc-sc` | 10.17.0.7/32  
Production | `vpc-sc` | 10.17.0.8/32  
  
To ensure that traffic for Google Cloud services has a DNS lookup to the correct endpoint, the blueprint configures private DNS zones for each VPC network. The following table describes these private DNS zones.

Private zone name | DNS name | Record type | Data  
---|---|---|---  
`googleapis.com.` | `*.googleapis.com.` | `CNAME` | `restricted.googleapis.com.`  
`restricted.googleapis.com` | `A` | The Private Service Connect endpoint IP address for that VPC network.  
`gcr.io.` | `*.gcr.io` | `CNAME` | `gcr.io.`  
`gcr.io` | `A` | The Private Service Connect endpoint IP address for that VPC network.  
`pkg.dev.` | `*.pkg.dev.` | `CNAME` | `pkg.dev.`  
`pkg.dev.` | `A` | The Private Service Connect endpoint IP address for that VPC network.  
  
The blueprint has additional configurations to enforce that these Private Service Connect endpoints are used consistently. Each Shared VPC network also enforces the following:

  * A network firewall policy rule that allows outbound traffic from all sources to the IP address of the Private Service Connect endpoint on TCP:443.
  * A network firewall policy rule that denies outbound traffic to 0.0.0.0/0, which includes the [default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) that are used for access to Google Cloud services.



## Internet connectivity

The blueprint doesn't allow inbound or outbound traffic between its VPC networks and the internet. For workloads that require internet connectivity, you must take additional steps to design the access paths required.

For workloads that require outbound traffic to the internet, we recommend that you manage outbound traffic through [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow outbound traffic without unsolicited inbound connections, or through [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) for more granular control to allow outbound traffic to trusted web services only.

For workloads that require inbound traffic from the internet, we recommend that you design your workload with [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https) and [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) to benefit from DDoS and WAF protections.

We don't recommend that you design workloads that allow direct connectivity between the internet and a VM using an external IP address on the VM.

## Hybrid connectivity between an on-premises environment and Google Cloud

To establish connectivity between the on-premises environment and Google Cloud, we recommend that you use [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) to maximize security and reliability. A Dedicated Interconnect connection is a direct link between your on-premises network and Google Cloud.

The following diagram introduces hybrid connectivity between the on-premises environment and a Google Virtual Private Cloud network.

![The hybrid connection structure.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-hybrid-connectivity.svg)

The diagram describes the following components of the pattern for [99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability):

  * Four Dedicated Interconnect connections, with two connections in one metropolitan area (metro) and two connections in another metro. Within each metro, there are two distinct zones within the colocation facility.
  * The connections are divided into two pairs, with each pair connected to a separate on-premises data center.
  * [VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) are used to connect each Dedicated Interconnect instance to [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) that are attached to the Shared VPC topology.
  * Each Shared VPC network has four Cloud Routers, two in each region, with the dynamic routing mode set to `global` so that every Cloud Router can announce all subnets, independent of region.



With global dynamic routing, Cloud Router advertises routes to all subnets in the VPC network. Cloud Router advertises routes to remote subnets (subnets outside of the Cloud Router's region) with a lower priority compared to local subnets (subnets that are in the Cloud Router's region). Optionally, you can change [advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority) when you configure the BGP session for a Cloud Router.

Traffic from Google Cloud to an on-premises environment uses the Cloud Router closest to the cloud resources. Within a single region, multiple routes to on-premises networks have the same multi-exit discriminator (MED) value, and Google Cloud uses [equal cost multi-path (ECMP)](https://en.wikipedia.org/wiki/Equal-cost_multi-path_routing) routing to distribute outbound traffic between all possible routes.

## On-premises configuration changes

To configure connectivity between the on-premises environment and Google Cloud, you must configure additional changes in your on-premises environment. The Terraform code in the blueprint automatically configures Google Cloud resources but doesn't modify any of your on-premises network resources.

Some of the components for hybrid connectivity from your on-premises environment to Google Cloud are automatically enabled by the blueprint, including the following:

  * Cloud DNS is configured with DNS forwarding between all Shared VPC networks to a single hub, as described in DNS setup. A Cloud DNS server policy is configured with [inbound forwarder IP addresses](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints).
  * Cloud Router is configured to export routes for all subnets and custom routes for the IP addresses used by the Private Service Connect endpoints.



To enable hybrid connectivity, you must take the following additional steps:

  1. [Order a Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect).
  2. Configure on-premises routers and firewalls to allow outbound traffic to the internal IP address space defined in IP address space allocation.
  3. Configure your on-premises DNS servers to forward DNS lookups bound for Google Cloud to the [inbound forwarder IP addresses](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints) that is already configured by the blueprint.
  4. Configure your on-premises DNS servers, firewalls, and routers to accept DNS queries from the Cloud DNS [forwarding zone](https://docs.cloud.google.com/dns/docs/zones/forwarding-zones) (35.199.192.0/19).
  5. Configure on-premise DNS servers to respond to queries from on-premises hosts to Google Cloud services with the IP addresses defined in private access to Cloud APIs.
  6. For encryption in transit over the Dedicated Interconnect connection, configure [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview) or configure [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) for IPsec encryption.



For more information, see [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

## What's next

  * Read about [detective controls](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
