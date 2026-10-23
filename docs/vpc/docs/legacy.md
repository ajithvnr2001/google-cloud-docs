---
url: https://docs.cloud.google.com/vpc/docs/legacy/
title: Legacy networks \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:31.689220+00:00
---

# Legacy networks  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/legacy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Legacy networks

Legacy networks are not recommended and can no longer be created. Many newer Google Cloud features are not supported in legacy networks. Instead, use Virtual Private Cloud (VPC) networks. For more information, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc). For more information about replacing legacy networks, see Replace legacy networks.

**Note:** The [IPv4Range](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) field for creating legacy networks is deprecated and is no longer available for any Google Cloud project. You cannot create new legacy networks. However, existing legacy networks are not affected and continue to operate normally.

## About legacy networks

Legacy networks have a single [RFC 1918](https://tools.ietf.org/html/rfc1918) range, which you specify when you create the network. The network is global in scope and spans all cloud regions.

In a legacy network, instance IP addresses are not grouped by region or zone. One IP address can appear in one region, and the following IP address can be in a different region. Any given range of IPs can be spread across all regions, and the IP addresses of instances created within a region are not necessarily contiguous.

The following figure shows a legacy (non-VPC) network. Traffic from the internet passes through a global switching function in the network (shown in the diagram as a virtual switch), then down to individual instances.

Instances in a region can have IP addresses that are not grouped in any way. As shown in the example, instances from 10.240.0.0/16 are spread unpredictably across regions 1 and 2. For example, `10.240.1.4` is in region 2, `10.240.1.5` is in region 1, and `10.240.1.6` is in region 2.

[ ![A legacy network.](https://docs.cloud.google.com/static/vpc/images/no_subnetworks_1.svg)](https://docs.cloud.google.com/static/vpc/images/no_subnetworks_1.svg) A legacy network (click to enlarge).

## Differences between legacy and VPC networks

  * Legacy networks can no longer be created.

  * Legacy networks have a single global IP address range that cannot be divided into subnets. VPC networks are divided into subnets.

  * With VPC networks, each Google Cloud region can have zero or more subnets. It is not possible to create regional subnets with a legacy network.

  * Some Google Cloud networking features are [not available](https://docs.cloud.google.com/vpc/docs/using-legacy#restrictions) in legacy networks.


**Note:** You can convert a legacy network to a VPC network. For more information, see [Single-region conversion tool](https://docs.cloud.google.com/vpc/docs/legacy#single-region-conversion).

## Routes

Legacy networks start with only two routes, the default route to outside the network and the route to the overall legacy network IP range. See [Using Routes](https://docs.cloud.google.com/vpc/docs/using-routes) for instructions on creating routes.

## Firewall rules

User-created networks have a default Allow-all firewall rule for outbound traffic and a default Deny-all firewall rule for inbound traffic. See [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) for instructions on creating firewall rules.

## Replace legacy networks

If you want to move individual VM instances out of your legacy network, see [Migrating a VM between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).

If you have an existing legacy network, you can replace it with a VPC network in one of two ways:

  * **Single-region conversion tool:** Use the `gcloud` or API single-region conversion tool. This tool converts a legacy network to a custom mode VPC network. Before starting the conversion, all Google Cloud resources in the legacy network must be in a _single region_. If the legacy network contains resources in multiple regions, including stopped VMs, the conversion fails. After the conversion, the subnet in the new network has the same internal IP address range as the entire legacy network. After the conversion is complete, you can use all features that VPC networks offer, such as creating regional subnets. For more information about the conversion, see [Converting a single-region legacy network to a VPC network](https://docs.cloud.google.com/vpc/docs/using-legacy#convert).

  * **Manual migration** : Recreate resources in your legacy network in a VPC network. For more information, see [Manually migrating to a VPC network](https://docs.cloud.google.com/vpc/docs/using-legacy#manual-migration).




### Single-region conversion tool

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can convert a legacy network to a custom mode VPC network by using the [single-region conversion tool](https://docs.cloud.google.com/vpc/docs/using-legacy#convert). During the conversion, the legacy network's IP address range is used to configure a subnet in the converted VPC network. Because a given subnet can be associated with only one region, the conversion tool works only if all resources in the legacy network are in a single region.

Using the tool to convert from a legacy network to a VPC network does not disrupt network traffic; your resources continue to operate normally. The conversion is one way, so you cannot revert to a legacy network after converting to a VPC network.

If your legacy network contains Google Kubernetes Engine clusters, your GKE clusters must be upgraded _after_ the conversion to ensure that components operate correctly. For more information, see [Converting a legacy network that contains GKE clusters](https://docs.cloud.google.com/vpc/docs/using-legacy#convert-network-gke).

After the conversion is complete, the new VPC network operates as any other VPC network. You can [add new subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) and use other VPC-related features. However, the converted subnet has the same internal IP address range as the entire legacy network, so new subnets must be created from [other valid ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

The following descriptions detail what happens to resources during the conversion. Most resources remain unchanged and refer to the VPC subnet instead of the legacy network.

Legacy network
    The legacy network isn't deleted; it's converted to a VPC network. The legacy network's IPv4 range is converted to the primary range of a single subnet in a VPC network.
VPC network
    Google Cloud converts the legacy network to a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) with a single subnet in the region where your VM instances are located. The VPC network and subnet both have the same name as the original legacy network.
Subnet
    Google Cloud creates a subnet and its subnet route during the conversion. The subnet is created in the region where your VM instances are located. Google Cloud automatically converts resources such as VM instances, regional forwarding rules, and instance group managers to the subnet. The subnet has the same name as the original legacy network. If the legacy network didn't contain any resources, Google Cloud doesn't create a subnet.
VM instances
    All instances with a network interface in the converted network will reference the newly created subnet.
Forwarding rules
    All internal forwarding rules in the VPC network will reference the newly created subnet.
Routes
    All custom static routes stay the same when the network is converted to a VPC network. If Google Cloud creates a new subnet, it does add one system-generated route called a _subnet route_. For more information, see [Route types](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes).
Firewall rules
    All existing firewall rules stay the same when the network is converted to a VPC network. All VPC networks also have two implied firewall rules that cannot be removed. For more information, see [Implied rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules).
Instance group managers and instance templates
    All instance templates that have a primary network interface (nic0) referencing the legacy network will reference the newly created subnet.
VPN tunnels and gateways
    VPN tunnels and gateways stay the same and continue to function when the network is converted to a VPC network.
Cloud Router
    Cloud Routers stay the same and continue to function when the network is converted to a VPC network.
Load balancers
    Existing load balancers stay the same and continue to function when the network is converted to a VPC network.

## What's next

  * To migrate, convert, or delete a legacy network, see [Manage legacy networks](https://docs.cloud.google.com/vpc/docs/using-legacy).

  * To learn more about Google Cloud VPC networks, see the [Virtual Private Cloud (VPC) overview](https://docs.cloud.google.com/vpc/docs/overview).

  * To learn how to create and modify VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
