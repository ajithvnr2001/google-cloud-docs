---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/networking/
title: Network traffic management for multiple zones \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.666884+00:00
---

# Network traffic management for multiple zones  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Network traffic management for multiple zones Stay organized with collections  Save and categorize content based on your preferences. 

This document explains network traffic strategies to streamline communication of your services across multiple zones in a Google Distributed Cloud (GDC) air-gapped universe. To maintain highly available applications, you must implement a networking strategy that is resilient to local outages or failures. GDC provides strategies so you can maintain internal networking configurations within an organization, and external networking configurations to other networks outside your organization across a multi-zone universe.

This document is for network administrators within the platform administrator group who are responsible for developing network configurations across zones in a GDC universe.

For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Key capabilities for multi-zone networking

GDC's networking infrastructure lets you establish resilient communication channels for your workloads and services across distinct disaster domains. Configuring failover mechanisms and global networking strategies across all zones in your air-gapped universe provides the following key capabilities:

  * Redirect network traffic to a new zone during a local outage.
  * Scale workload and service networking requests evenly across multiple zones.
  * Define ingress and egress traffic policies for global projects.
  * Allocate IP addresses across zones.



The following sections describe the key capabilities for multi-zone networking.

### Zonal network traffic redirection during outages

You can use global networking strategies to successfully redirect network traffic when there's a local outage in one of your zones.

Anycast services provide automatic multi-zone failover for IP addresses, which routes traffic to the closest or best-performing zone during a zone outage. Anycast services in GDC use Data Center Interconnection (DCI) to provide you with a full mesh to interconnect multiple GDC air-gapped zones over diverse geographic locations. With interconnected zones, you can deliver multi-zone disaster protection with site diversity while accommodating the requirement for complete disconnection from all Google Cloud infrastructure.

GDC also offers Domain Name System (DNS) redirect capabilities that are global and span across multiple zones with [Cloud DNS](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview). If a DNS service instance becomes inaccessible in a zone, clients are seamlessly served by another DNS service instance in another zone.

### Networking requests across zones

GDC offers a Layer 4 (L4) global load balancer that lets your applications expose services to one another across multiple zones with a TCP or UDP protocol. Scaling your network requests across multiple zones can prevent overloading a single zone's networking capabilities, which would slow down the response time of your application.

You can configure a load balancer to control traffic within your global organization as an internal load balancer, or configure an external load balancer to scale your service requests across networks outside your organization.

### Project ingress and egress traffic policies

You can define ingress and egress network traffic policies for all resources in a project, which can span across multiple zones. Since a project is the foundational resource boundary for your services and applications, and spans all zones in a universe by default, network traffic control from the project level gives you global control over all ingress and egress traffic configurations for the resources that reside within that project.

### IP addresses allocation across zones

GDC provides global IP address ranges for your networks that you can allocate to all your zones in a GDC universe. A subnetwork, or subnet, defines allocations of IP addresses to specific zones from the global root IP address range within a given network. You can create subnets to fine tune your IP address architecture across multiple zones and dynamically allocate IP addresses to your workloads and external services, providing streamlined control over your networking needs across a universe.

## Global networking components

GDC provides configurable networking components that can help you fully implement a highly available networking architecture for your multi-zone universe.

### Anycast services

Anycast is a network routing method that allows requests to be served by multiple locations. Anycast services are represented by unique `/32` IPv4 prefixes, which are provided using Border Gateway Protocol (BGP) to your air-gapped facilities, ensuring reachability from any connected location. While each anycast service is accessible from all zones within your GDC air-gapped network, the actual endpoint to which your network traffic is directed depends on factors such as proximity and zone preference based on your custom routing policy.

You must work with your infrastructure operator group to plan and implement your anycast networking preferences.

#### Zone proximity

GDC optimizes network traffic delivery by routing requests to the nearest available service instance, always within the same zone as the request. This delivery mechanism reduces latency and enhances the overall performance and responsiveness of your service. For example, if an anycast service is deployed across zone 1, zone 2, and zone 3, a network request originating from zone 2 would typically be routed to the service instance within zone 2, as it's the closest and, therefore, most efficient option.

#### Zone preference

GDC implements a zone preference system where zones are assigned a numerical value during creation, irrespective of its zone name, that sets customer attraction. For example, if you deploy an anycast service to zones with numerical values `1`, `2`, and `3`, GDC generally directs network traffic towards the zone with the lowest value set before the other zones. This preference system provides a degree of predictability and control over traffic patterns, but it also includes built-in failover mechanisms. In the event of a failure or outage affecting your preferred zone, the GDC system automatically shifts traffic to another zone, providing uninterrupted service availability.

#### Zonal interconnects

In a multi-zone configuration, accessing services within a specific zone requires an interconnect from your network to that zone.

For a consistent multi-zone deployment, the interconnects created in each zone in your universe must be identical in terms of capacity and configuration. Each zone you intend to access must have a corresponding interconnect.

For more information, see [Establish connectivity with interconnects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview).

### Load balancing

GDC provides an L4 passthrough load balancer for pod and VM workloads. This load balancer provides dedicated load balancing for particular zones, or global load balancing across all zones in the universe. Across your zones, you can manage internal network traffic within your organization, or external network traffic between organizations.

For more information about load balancing in GDC, see [Manage load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/expose-services).

### Project network policies

Project network policies define either ingress or egress rules for a project. Because projects are a global resource, you must define a project's network policies globally as well, to allow for cross-zone networking traffic for the services and workloads within a project.

You can define the following ingress or egress rules for your project with project network policies, which span across all your zones:

  * Across multiple organizations
  * Across multiple projects
  * Within a single project
  * Across workloads within a project
  * Across GDC-managed services within different projects



For more information, see [Configure project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview).

### Cloud DNS

Cloud DNS is a high-performance, resilient, global Domain Name System (DNS) service that publishes your domain names to the global DNS in a cost-effective way.

DNS is a hierarchical distributed database that lets you store IP addresses and other data and look them up by name. Cloud DNS lets you publish your zones and records in DNS without the burden of managing your own DNS servers and software.

Cloud DNS provides highly available services that can serve DNS requests across multiple GDC zones. If a DNS service instance becomes inaccessible in a zone, clients are seamlessly served by another DNS service instance in another zone. By seamlessly redirecting DNS requests to different zones during a zonal outage, you can confidently rely on GDC to serve your DNS needs even during a disaster.

For more information about Cloud DNS in GDC, see [About Cloud DNS](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-overview).

### Subnets for IP address management

GDC provides strategies to allocate IP addresses from your global root IP address range to workloads and services across a multi-zone universe. You control your IP address architecture across zones by creating subnets, which allocate Classless Inter-Domain Routing (CIDR) blocks. With the option to statically or dynamically allocate IP addresses to your resources, you have full control of your IP address ranges spanning multiple zones.

For more information, see [Subnets and IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview).

## What's next

  * [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview)
  * [Networking overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview)
  * [Permissions control for a multi-zone universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/permissions)
  * [High availability for your apps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
