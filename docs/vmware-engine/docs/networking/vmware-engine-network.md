---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network/
title: About VMware Engine networks \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:03.253101+00:00
---

# About VMware Engine networks  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About VMware Engine networks

Google Cloud VMware Engine uses a _VMware Engine network_ to provide network connectivity between one or more private clouds, Google Cloud Virtual Private Cloud networks, and on-premises networks.

## Types of VMware Engine networks

By default, VMware Engine offers a global VMware network which provides network connectivity between one or more private clouds, Virtual Private Cloud networks, or on-premises networks. These global VMware networks are referred to as _Standard VMware Engine Networks_.

In addition, projects created before November 2023 have _Legacy VMware Engine Networks_ , which are regional networks that must exist in each region that contains a private cloud.

**Note:** Only projects created before November 2023 can use Legacy VMware Engine Networks. It is not possible to create these networks in projects created after November 2023.

## Standard VMware Engine networks

Create one or more standard networks in a project to create network isolation between your private clouds.

![Network connectivity of a standard VMware Engine network uses VPC network peering.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-network-overview-standard.png)

### Network connectivity for Standard VMware Engine networks

To establish communication to VMware Engine from your VPC network, you must create a [VPC Network peering](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network) relationship between your VPC network and a VMware Engine network. This enables exclusive communication using internal IP addresses between virtual machine (VM) instances in your VPC network and VMware VMs.

### DNS resolution behavior

The following section outlines the DNS resolution behavior for VMware Engine networks.

#### Private cloud management zone

Each private cloud creates a corresponding authoritative Cloud DNS zone used to resolve all management appliances like vCenter Server, NSX Manager, and HCX.

#### Google Cloud resolution

By default, you can resolve the management zone from any of your VPC networks that has Cloud DNS enabled. When a VMware Engine network is [VPC peered](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network), VMware Engine automatically creates a [management DNS zone binding](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns), ensuring resolution from any of your Google Cloud VMs.

#### On-premises resolution

See [Configuring DNS for management appliance access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises).

#### DNS Resolution from private cloud VMs and management appliances

Each private cloud deploys a Cloud DNS Server used for all management appliances resolution and that you can configure as the DNS server for all VMware workloads.

#### Private cloud workload DNS server IP

To get the IP address of your private cloud's DNS server and configure DNS for your VMware workloads or NSX segment DHCP DNS setting:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click the name of the private cloud you want to configure DNS for.

  3. On the **Summary page** for the private cloud, under **Private cloud DNS servers** , click **Copy** to copy the private Cloud DNS server IP address.




#### Binding Cloud DNS zones

You can bind Cloud DNS zones configured in your project to a VMware Engine network; this ensures proper resolution of authoritative or conditional forward zones from any of your private cloud VMs or management appliances. See [Configuring DNS bindings](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings) for more information.

#### Private Google Access

To enable Private Google Access for VMware Engine, configure the DNS server in your VMware Engine environment to use the private virtual IP address. For more information, see [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid) and [Configuring Private Google Access for on-premises hosts][configure Private Google Access on premises hosts]. The domain `private.googleapis.com` uses `199.36.153.8/30`.

## Legacy VMware Engine networks

A Legacy VMware Engine network is a regional network that provides network connectivity between one or more private clouds, Virtual Private Cloud networks, and on-premises networks. You must name legacy networks using the convention `<region>-default` and you must create a network for each region where you create a private cloud.

![Network connectivity of a legacy VMware Engine network private connections.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-network-overview-legacy.png)

### Network connectivity for Legacy VMware Engine networks

To establish communication to VMware Engine from your VPC network, you must [enable private services access and create a private connection](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access) between your VPC network and the VMware Engine network. This enables exclusive communication using internal IP addresses between VM instances in your VPC network and VMware VMs.

Legacy networks function at a regional level, and can only connect to service producer networks in the corresponding region. You must establish separate private connections to service producer networks in each region.

### DNS Resolution behavior for Legacy VMware Engine networks

The following sections outline the DNS Resolution behavior for Legacy VMware Engine networks.

#### Private cloud management zone

Each private cloud creates a corresponding authoritative Cloud DNS zone used to resolve all management appliances like vCenter Server, NSX Manager, and HCX.

##### Google Cloud resolution

By default, you can resolve the management zone from any of your VPC networks where you have enabled Cloud DNS. When a [private connection](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access) is created between your VPC network and a Legacy VMware Engine network, Google automatically creates DNS peering, ensuring resolution from any of your Google Cloud VMs.

##### On-premises resolution

See [Configuring DNS for management appliance access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises).

### DNS Resolution from private cloud management appliances

Private cloud management appliances use conditional DNS forwarding rules which you can configure within each private cloud. For more information, see [Create legacy DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding).

### Private cloud VMware VM resolution

Private clouds connected to Legacy VMware Engine networks don't have Cloud DNS automatically configured. You can choose to use Cloud DNS within your project or use a third party DNS solution.

To use Cloud DNS, do the following:

  1. [Enable inbound DNS forwarding on the VPC network](https://docs.cloud.google.com/dns/docs/best-practices#use_dns_server_policies_to_allow_queries_from_on-premises).
  2. [Identify the DNS server addresses to use for VMware VMs](https://docs.cloud.google.com/dns/docs/policies#list-in-entrypoints).



## What's next

  * Learn how to [create a VMware Engine network](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vmware-engine-network).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
