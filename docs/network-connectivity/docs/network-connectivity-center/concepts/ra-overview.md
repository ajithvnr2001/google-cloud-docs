---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview/
title: Router appliance overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:51.830139+00:00
---

# Router appliance overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Router appliance overview Stay organized with collections  Save and categorize content based on your preferences. 

Router appliance is a Network Connectivity Center (NCC) feature that lets you use a third-party network virtual appliance in Google Cloud. When you use this approach, the appliance can exchange routes with Cloud Router by using Border Gateway Protocol (BGP).

Using Router appliance and NCC, you can do the following:

  * Connect multiple VPC networks to one another. The VPC networks can be located across different projects in the same Google Cloud organization or different organizations.
  * Connect multiple VPC networks to on-premise or other cloud provider networks. These external networks can be reachable through any type of hybrid spoke. This approach is known as _site-to-cloud connectivity._
  * Use Router appliance VMs to manage connectivity between your VPC networks.
  * Use a Google Cloud VPC network as an enterprise wide area network (WAN) to connect networks that are outside of Google Cloud. You can establish connectivity between your external sites by using any type of hybrid spoke. This approach is known as _site-to-site connectivity_.



## How it works

You can configure a router appliance instance by installing an image on a Compute Engine VM. You can use an image provided by a [supported NCC partner](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners). You can also use a custom image, such as an image that you created.

After the router appliance instance is installed, you configure interfaces on the Cloud Router to establish Border Gateway Protocol (BGP) peering with the router appliance instance. BGP enables the dynamic exchange of routes between the Cloud Router and the router appliance instance. Route exchange, in turn, permits connectivity from the site through the router appliance instance to the VPC network. That is, the routes propagated by the router appliance instance can be used by VMs and other resources that have IP addresses in the same VPC network.

Cloud Router uses interfaces configured with RFC 1918 internal IP addresses to establish BGP peering with router appliance instances.

There are no separate APIs or Google Cloud resources or permissions for Router appliance. To work with Router appliance, you use Compute Engine and Cloud Router resources and permissions.

## Use case: Data transfer between on-premises sites

The following topology shows a VPC network and two on-premises sites. Each on-premises site connects to Google Cloud by using a Router appliance spoke. The two on-premises sites can use Google's network to exchange data with each other.

[ ![Router appliance topology](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/router-appliance-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/router-appliance-topology.svg) Router appliance topology (click to enlarge)

  1. On-premises `Customer network A` and `Customer network B` are each connected through _customer premises equipment (CPE)_ to a router appliance instance. CPEs typically use a connectivity mechanism, such as an SD-WAN overlay tunnel or an IPsec VPN tunnel, to establish connectivity with the router appliance instance.

Each router appliance instance is located in the Google Cloud region closest to its associated customer network. Both router appliance instances are in a single VPC network. However, the router appliance instances are in different regions. For this reason, the VPC network has its [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#switch-dynamic-routing) set to `global`.

  2. Both router appliance instances are attached as spokes to the Network Connectivity Center (NCC) hub. Because `Customer network A` and `Customer network B` need to send data to each other, both spokes have the site-to-site data transfer field enabled.

_You can use site-to-site data transfer only in supported locations._ For more information, see [Locations supported for data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

  3. In each region, a router appliance instance establishes Border Gateway Protocol (BGP) peering with the appropriate Cloud Router. Each Cloud Router receives and advertises route prefixes from the corresponding on-premises location.

  4. The Cloud Routers dynamically exchange all received routes with each other. This configuration provides end-to-end dynamic route exchange and data plane connectivity between `Customer network A` and `Customer network B`.

**Important:** For Cloud Routers in different regions to exchange routes with each other, you must enable global dynamic routing mode in your VPC network. For more information, see [Dynamic routing](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



For detailed configuration steps for a load-balanced single-site topology, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).

## Requirements

Follow these requirements when deploying router appliance instances.

### BGP configuration

  * The router appliance image that you install must support the BGP routing protocol.
  * To enable BGP peering between a router appliance instance and a Cloud Router, attach each router appliance instance as a spoke to an NCC hub.
  * Create a Cloud Router in the same region as the [subnet](https://docs.cloud.google.com/vpc/docs/vpc#subnets_vs_subnetworks) that contains the peering interface of the router appliance instance.
  * Manually create BGP interfaces on the router appliance instance. These interfaces must be in the same subnet as the router appliance instance.
  * Manually create BGP sessions with Cloud Router from the router appliance instance.
  * For VMs that have multiple network interfaces configured as part of the router appliance instance, you can establish BGP sessions with Cloud Routers that are in the same subnet as the VM interface. For more information about VM interfaces, see [Multiple network interfaces overview and examples](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).



### Availability recommendations

* The standard service-level agreement (SLA) for Compute Engine VMs also applies to the availability of router appliance instances. This availability SLA is 99.5% for a single VM and 99.99% for VMs in multiple zones. For more information, see the [Compute Engine SLA](https://cloud.google.com/compute/sla). * For a pair of router appliance instances, each for a different on-premises location, run at least two VMs in different zones. Each VM must peer with a pair of redundant Cloud Router interfaces. For more information about zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). 

## Considerations

Before using Router appliance, review the following sections.

### General considerations

  * _Router appliance requires NCC to operate._ That is, you can't configure standalone router appliance instances that peer with a Cloud Router or with other peer routers. You must configure router appliance instances as part of a NCC spoke.
  * Router appliance is only supported in the Shared VPC model when deployed in the host project. The router appliance instance must be deployed in the host project and all the other associated resources, such as hub, spoke, and Cloud Router.

Router appliance does not support Shared VPC when the Router appliance VM is deployed in the service project.




### Routing considerations

  * If multiple router appliance instances announce the same routing prefixes with the same MED, Google Cloud uses equal-cost multipath (ECMP) routing across all the router appliance instances.
  * _We recommend not advertising the same prefixes through a mix of different spoke types (router appliance instances, Cloud VPN gateways, and VLAN attachments)._ If the same prefixes are reachable through a mix of spoke types, using ECMP across the mixed spoke types can lead to imbalanced traffic across each link.
  * If a single Cloud Router learns a prefix with multiple next hops, Cloud Router selects the next hops with the shortest AS path length first, and then uses the MED to break ties. For more information, see [AS path length](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#as-path-length-legacy-bps) in the Cloud Router documentation.



## What's next

  * To set up Google Cloud resources for your router appliance instance, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To view Router appliance monitoring and logging information, see [Viewing logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/viewing-logs-metrics).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
