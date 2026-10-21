---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets/
title: VLANs and subnets on VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:54.045565+00:00
---

# VLANs and subnets on VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VLANs and subnets on VMware Engine

Google Cloud VMware Engine uses a VMware Engine network to provide network connectivity between one or more private clouds, Google Cloud Virtual Private Cloud networks, and on-premises networks. VMware Engine offers two network types: _Standard_ and _Legacy_. Standard networks are the default for projects created in or after November 2023, are global, and use VPC network peering for connectivity. Legacy networks are available only in projects created before November 2023, are regional, and use private service access for connectivity. For more information, see [About VMware Engine networks](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network).

Regardless of network type, you can create network segments (subnets) using NSX-T Data Center for your workload virtual machines (VMs).

![VLANs and subnets.](https://docs.cloud.google.com/static/vmware-engine/images/vlan-subnet.svg)

## Management VLANs

Google creates a VLAN (Layer 2 network) for each private cloud. The Layer 2 traffic stays within the boundary of a private cloud, letting you isolate the local traffic within the private cloud. These VLANs are used for the management network. For workload VMs, you must create network segments on NSX Manager for your private cloud.

## Subnets

When you use VMware Engine, Google creates management subnets for you, and you create workload subnets using NSX-T for your workload VMs.

### Workload subnets

For your workload VMs, you must [create a network segment on the NSX manager](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets) for your private cloud. You can configure any IP address range that doesn't overlap with other networks in your private cloud, your on-premises network, your private cloud management network, or subnet IP address ranges in any peered Virtual Private Cloud (VPC) network. For a detailed breakdown of how VMware Engine allocates subnet IP address ranges for management, see [Networking requirements](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements).

Within a private cloud, workload network segments can communicate with each other by default. Communication between private clouds depends on the VMware Engine network type:

  * **Standard networks:** Communication between private clouds is done through VPC network peering and depends on your VPC configuration.
  * **Legacy networks:** East-west data across private clouds in the same region stays in the same Layer 3 network and transfers over the local network infrastructure within the region.



### Management subnets

When you create a private cloud, VMware Engine creates the following management subnets:

  * **System management:** VLAN and subnet for ESXi hosts' management network, DNS server, vCenter Server
  * **VMotion:** VLAN and subnet for ESXi hosts' vMotion network
  * **VSAN:** VLAN and subnet for ESXi hosts' vSAN network
  * **NsxtEdgeUplink1:** VLAN and subnet for VLAN uplinks to an external network
  * **NsxtEdgeUplink2:** VLAN and subnet for VLAN uplinks to an external network
  * **HCXUplink:** Used by HCX IX (mobility) and NE (extension) appliances to reach their peers and enable the creation of the HCX Cloud Service Mesh.
  * **NsxtHostTransport:** VLAN and subnet for host transport zone



## Service subnets

When you create a private cloud, VMware Engine automatically creates additional service subnets. You can target service subnets for appliance or service deployment scenarios, such as storage, backup, disaster recover (DR), media streaming, and providing high scale linear throughput and packet processing for even the largest scaled private clouds. The service subnet names are as follows:

  * `service-1`
  * `service-2`
  * `service-3`
  * `service-4`
  * `service-5`



Virtual Machine communication across a service subnet exits the **VMware ESXi** host directly into the Google Cloud networking infrastructure, enabling high speed communication.

**Note:** NSX gateway and distributed firewall rules won't apply to any service subnets.

### Configuring service subnets

When VMware Engine creates a service subnet, it does not allocate a CIDR range or prefix. You must specify a non-overlapping CIDR range and prefix. The first usable address will become the gateway address. To allocate a CIDR range and prefix, edit one of the service subnets.

Service subnets can be updated if CIDR requirements change. Modification of an existing service subnet CIDR may cause network availability disruption for VMs attached to that service subnet.

### Configuring vSphere distributed port groups

To connect a VM to a service subnet, you need to create a new Distributed Port Group. This group maps the service subnet ID to a network name within a vCenter private cloud.

To do this, navigate to the network configuration section of the vCenter interface, select **Datacenter-dvs** , and then select **New Distributed Port Group**.

After the distributed port group has been created, you can attach VMs by selecting the corresponding name in the network configuration of the VM properties. 

The following are Distributed Port Group critical configuration values:

  * **Port binding** : static binding
  * **Port allocation** : elastic
  * **Number of ports** : 120
  * **VLAN type** : VLAN
  * **VLAN ID** : the corresponding subnet ID within the subnets section of the Google Cloud VMware Engine interface



## Recommended MTU settings

The [maximum transmission unit (MTU)](https://wikipedia.org/wiki/Maximum_transmission_unit) is the size, in bytes, of the largest packet supported by a network layer protocol, including both headers and data. To avoid fragmentation-related issues, we recommend the following MTU settings:

  * For VMs that communicate only with other endpoints within a standard private cloud, you can use MTU settings up to 8800 bytes.

  * For VMs that communicate only with other endpoints within a stretched private cloud, you can use MTU settings up to 8600 bytes.

  * For VMs that communicate to or from a private cloud **without** encapsulation, use the standard 1500 byte MTU setting. This common default setting is valid for VM interfaces that send traffic in the following ways:

    * From a VM in a private cloud to a VM in another private cloud
    * From an on-premises endpoint to a private cloud
    * From a VM in a private cloud to an on-premises endpoint
    * From the internet to a private cloud
    * From a VM in a private cloud to the internet
  * For VMs that communicate to or from the internet with large packet UDP traffic flows that are sensitive to fragmentation, use an MTU setting of 1370 bytes or lower. This recommendation applies to communications using public connections or IP addresses provided by VMware Engine. MSS clamping generally resolves fragmentation issues with TCP-based traffic flows.

  * For VMs that communicate to or from a private cloud **with** encapsulation, calculate the best MTU setting based on VPN endpoint configurations. This generally results in an MTU setting of 1350–1390 bytes or lower for VM interfaces that send traffic in the following ways:

    * From an on-premises endpoint to a private cloud with encapsulation
    * From a private cloud VM to an on-premises endpoint with encapsulation
    * From a VM in one private cloud to a VM in another private cloud with encapsulation

**Note:** The default MTU setting is 1440 bytes on the **HCX** uplink profile.

These recommendations are especially important in cases where an application isn't able to control the maximum payload size. For additional guidance on calculating encapsulation overhead, see the following resources:

  * [Cloud VPN MTU considerations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations)
  * [VMware NSX VPNs](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/)
  * [Traffic Engineering in HCX Enterprise](https://cloud.vmware.com/community/2020/01/16/traffic-engineering-hcx-enterprise/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
