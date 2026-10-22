---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/plan-ip-architecture/
title: IP address planning and architecture \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:44.154892+00:00
---

# IP address planning and architecture  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/plan-ip-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  IP address planning and architecture Stay organized with collections  Save and categorize content based on your preferences. 

Effective IP address planning helps mitigate future networking disruptions for your workloads and services as they scale.

This document is for network administrators within the platform administrator group who are responsible for planning their IP address ranges for an organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

**Note:** This document assumes close coordination with the infrastructure operator group during the planning of your organization. The infrastructure operator group is referred to as the _IO_ throughout this document.

## Benefits for careful IP address planning

Careful IP address planning provides the following benefits:

  * **Isolation** : proper network segmentation between different organizations and between management and data planes.
  * **Scalability** : sufficient IP address space for current and future workloads and services, including administrative services that cannot be allocated additional IP address space after an organization is provisioned.
  * **Connectivity** : correct routing and reachability for all components within the GDC air-gapped universe, and to external networks as required.
  * **Compliance** : adherence to specific network addressing schemes or restrictions mandated by your environment.



The GDC architecture uses [Virtual Routing and Forwarding (VRF)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/security#sw-defined-net) instances to achieve network isolation and segmentation. Understanding which IP address spaces you manage and the ones exclusively owned by your IO is key to successful planning.

## Planning process

Before the IO provisions your organization, you must determine the IP address architecture for your organization. The IO walks you through these steps.

The high-level process for planning and provisioning an organization's network IP addresses is the following:

  1. **Define CIDR ranges** : work with your network team to determine appropriate non-overlapping CIDR blocks for your Default VPC, Infra VPC, Admin Network Segment, and Data Network Segment.

  2. **Provide CIDR ranges to the IO** : supply these CIDR blocks to the IO as part of the organization intake questionnaire (OIQ) when requesting a new organization. The IO uses the CIDR blocks to configure the necessary global subnets in the appropriate API servers.




After the IO provisions your organization, you are responsible for managing certain IP address spaces within the organization, primarily for workload deployment and external service exposure.

For more information about IP address architecture planning, see the IP address architecture considerations section of this document.

For more information about each network and how to select the CIDR ranges for each network, see the IP address considerations for an organization section of this document.

## IP address architecture considerations

To provision a durable IP address architecture that can adapt when your organization's networking requirements change, consider the following IP address traits in GDC:

  * **Overlapping and non-overlapping IP addresses** : 
    * Virtual Private Cloud (VPC) networks can overlap between _different_ organizations but must be unique within an organization across all its zones and unique from any networks they peer with.
    * External network segments can overlap between _different_ organizations if those organizations use separate [interconnects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview). If they share an interconnect, IP addresses must be unique within the _same_ organization across all its zones and unique from any networks they peer with.
  * **Minimum CIDR block sizes** : adhere to the minimum CIDR prefix lengths specified for each network segment to allocate sufficient address space for system components and future growth.
  * **RFC 1918 preference** : while public IP addresses can be used in most managed networks, if the zone doesn't connect to the internet, [RFC 1918](https://tools.ietf.org/html/rfc1918) private addresses are generally recommended for internal GDC air-gapped networks.
  * **OIQ accuracy** : the information you provide to your IO in the OIQ is critical. Inaccurate or poorly planned IP address ranges can lead to significant deployment challenges.
  * **Multi-zone** : organization VPCs and external network segments span across a global organization, but require unique IP address allocations for each zone that don't overlap _within that global organization_. Use global subnets to allocate unique IP address ranges for each zone for a given organization.



As an example IP address architecture, see the following diagram:

![Your interconnects in your universe determine how you set up your IP address architecture.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/platform/images/network-interconnects.png)

In this diagram, there are two different [interconnects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview) that span a multi-zone universe: dedicated interconnect and shared interconnect. Multiple organizations are defined in this universe. Organization 1 is within a dedicated interconnect, so its externally-scoped subnets can overlap with other organizations in the universe. However, the organizations in the shared interconnect cannot have overlapping externally-scoped subnets with each other since they all reside within the same interconnect.

Each organization defines the VPC networks and external network segments. In this example, anycast IP addresses are used to route traffic between the zonal external network segments so the closest or best-performing zone services the networking request. For more information about anycast IP addresses, see [IP addresses in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#ips-in-gdc).

## IP address considerations for an organization

Review each network and understand its purpose within your organization before completing the OIQ for defining CIDR ranges:

  * **Default VPC**: hosts internal IP addresses for internal workloads. You can allocate additional IP addresses to this network after your organization is provisioned.
  * **Infra VPC**: hosts internal IP addresses for first-party GDC air-gapped services. You cannot allocate additional IP addresses to this network after your organization is provisioned.
  * **Admin Network Segment**: hosts external IP addresses for administrative services. You cannot allocate additional IP addresses to this network after your organization is provisioned.
  * **Data Network Segment**: hosts external IP addresses for external services. You can allocate additional IP addresses to this network after your organization is provisioned.



For more information about network descriptions and the IP addresses they use, see [Networks in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#networks-in-gdc).

**Important:** Verify with your IO that you don't define IP addresses that are reserved and unusable. For more information, see [IPv4 address selection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#ipv4-usage-limitations).

### VPC networks

Prepare the following information for each VPC network type to deliver to your IO for the provisioning of your IP address spaces within your organization's VPC networks.

#### Default VPC

You deploy and manage your internal workloads, such as virtual machines (VM) and containers, from the Default VPC.

IP addresses in the Default VPC must be unique from other VPCs in all zones of your universe and any peered network IP addresses. IP addresses in this VPC can overlap between different organizations, and can be [RFC 1918](https://tools.ietf.org/html/rfc1918) private IP addresses or public IP addresses. You can create additional Default VPC subnets after the organization is provisioned.

Consider the following information when collaborating with your IO on the Default VPC root IP address range. Note that the corresponding OIQ field and global root subnet name are fixed values and cannot change.

  * **OIQ field** : `defaultVPCCIDR`
  * **Global root subnet name** : `default-vpc-root-cidr`
  * **Global API server** : Global organization
  * **Subnet minimum size** : `/16` for each zone
  * **Subnet recommended size** : `/16` for each zone



#### Infra VPC

You don't directly deploy workloads to the Infra VPC, but you must provide the IP address range for consumption by the system-managed GDC air-gapped services.

IP addresses in the Infra VPC must be unique from other VPCs in all zones of your universe and any peered network IP addresses. IP addresses in this VPC can overlap between different organizations, and can be [RFC 1918](https://tools.ietf.org/html/rfc1918) private IP addresses or public IP addresses. You cannot create additional Infra VPC subnets after the organization is provisioned.

Consider the following information when collaborating with your IO on the Infra VPC root IP address range. Note that the corresponding OIQ field and global root subnet name are fixed values and cannot change.

  * **OIQ field** : `infraVPCCIDR`
  * **Global root subnet name** : `infra-vpc-root-cidr`
  * **Global API server** : Global root
  * **Subnet minimum size** : `/16` for each zone
  * **Subnet recommended size** : `/16` for each zone



### External network segments

Prepare the following information for each external network segment type to deliver to your IO for the provisioning of your IP address spaces within your organization's external networks.

#### Admin Network Segment

You don't directly deploy external services to the Admin Network Segment, but you must provide the IP address range for consumption by the administrative services that will run in your organization, such as the GDC console and management APIs. You cannot allocate additional IP addresses to this network after your organization is provisioned.

IP addresses in the Admin Network Segment can overlap between _different_ organizations if those organizations use separate interconnect attachment groups. If they share an attachment group, the IP addresses must be unique within the _same_ organization across all its zones and unique from any networks they peer with. You cannot create additional Admin Network Segment subnets after the organization is provisioned.

Consider the following information when collaborating with your IO on the Admin Network Segment root IP address range. Note that the corresponding OIQ field and global root subnet name are fixed values and cannot change.

  * **OIQ field** : `orgAdminExternalCIDR`
  * **Global root subnet name** : `admin-external-root-cidr`
  * **Global API server** : Global root
  * **Subnet minimum size** : `/26` for each zone
  * **Subnet recommended size** : `/26` for each zone



#### Data Network Segment

You deploy and manage your external services that operate outside of your organization, such as [egress Network Address Translation (NAT)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-settings) and [external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service), within the Data Network Segment. You can allocate additional IP addresses to this network after your organization is provisioned.

IP addresses in the Data Network Segment can overlap between _different_ organizations if those organizations use separate interconnect attachment groups. If they share an attachment group, the IP addresses must be unique within the _same_ organization across all its zones and unique from any networks they peer with. You can create additional Data Network Segment subnets after the organization is provisioned.

Consider the following information when collaborating with your IO on the Data Network Segment root IP address range. Note that the corresponding OIQ field and global root subnet name are fixed values and cannot change.

  * **OIQ field** : `orgDataExternalCIDR`
  * **Global root subnet name** : `data-external-root-cidr`
  * **Global API server** : Global root
  * **Subnet minimum size** : `/26` for each zone
  * **Subnet recommended size** : `/23` for each zone



## What's next

  * [Interconnect overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview)
  * [Create an attachment group](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-attachment-group)
  * [Provision IP addresses for workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets)
  * [Bring your own external IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-external-subnets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
