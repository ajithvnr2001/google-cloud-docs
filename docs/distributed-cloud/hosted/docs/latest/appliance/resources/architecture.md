---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/architecture/
title: Architecture \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:59.791088+00:00
---

# Architecture  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Architecture Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the deployment, cluster, and network architecture of Google Distributed Cloud (GDC) air-gapped appliance.

## Deployment architecture

The following diagram illustrates how the appliance hardware fits within a customer network that includes optional components such as HSMs, an NTP server, and additional clients within the network. The appliance is equipped with a management plane, data plane, servers, and a 1-GPU enabled server, all designed to run workloads directly at the edge. 

![Deployment architecture](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/deployment-arch.png)

## Cluster architecture

GDC air-gapped appliance operates a single cluster that encompasses all three of its bare metal nodes, known as the org infrastructure cluster. A dedicated management API server, which runs as pod workloads on the cluster, hosts management plane APIs. User workloads, which include both VMs and Kubernetes pods, can run on this cluster. There is no user cluster in this cluster model.

![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/cluster_arch.png)

## Network architecture

The EL8000 includes a backplane which creates four separate Layer 2 (L2) networks inside the device:

  1. Integrated Lights-Out (iLO) console (1GbEth)
  2. Management network (1GbEth)
  3. Data network A (10GbEth)
  4. Data network B (10GbEth)



The following diagram shows how the L2 networks are connected to the Mellanox switch (<https://www.hpe.com/psnow/doc/a00043975enw.html?jumpid=in_pdp-psnow-qs>). Each network in a blade connects to a single network switch. All of the iLO console networks in each server blade connect to network switch 1. The management networks connect to network switch 2 and the data networks connect to switches 3 and 4.

![Layer 2 networks connecting to the switch](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/backplane.png)

The customer network ports (15 and 17) have access to the cluster (VLAN 100) and only traffic to the Ingress CIDR is allowed. The Ingress CIDR is available for services and the range is advertised over Border Gateway Protocol (BGP) to the customer network.

Management network ports (16 and 18) have access to system management (VLAN 501) so that customers can have the device on a broader network and use only local connections to do system administration tasks.

### Lower network topology

#### Physical network

The GDC consists of a hybrid cluster that operates in a single tenant mode. The hybrid cluster, which we refer to as the infra cluster, consists of both the system and admin clusters merged together:

![Physical network](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/physical-network.png)

The physical design is centered on a Mellanox SN2010 that acts as a gateway between the Appliance Infra Cluster and the external customer network.

The infra cluster consists of 3 Bare Metal Nodes (BMs). The connections on the BMs can be categorized as follows:

  * Data network connectivity (subnet 198.18.2.0/24) which is over VLAN 100. The BM has a NIC with 2 ports, `NIC0P1` and `NIC0P2`, that are bonded and connected to the TOR switch. `BM1` and `BM2` directly connect to the switch whereas `BM3` connects to the TOR using an unmanaged switch.
  * Management network connectivity ( subnet 198.18..0/24) is over VLAN 501. The ILO and MGMT interfaces are connected over this VLAN using 1G interfaces. The ILO interfaces and the MGMT interfaces on the BM nodes connect to the switch using unmanaged switches.
  * Maybe: add OTS networking on VLANs 200-203(?), subnet 198.18.1.x



The connection from the Mellanox switch to the customer router provides external connectivity. 10G interfaces are used for this connectivity, and the BGP protocol is used to advertise the external network IPs to the customer. Customers use the external IPs to access the necessary services provided by the Appliance unit.

**Note:** the physical network diagram displayed earlier shows a bootstrapper device connected to port 12 of the switch. This bootstrapper is to provision the appliance unit as a part of the lowside bootstrap phase. This connection won't be present when the appliance is shipped to the customer.

#### Logical network

There are two virtual local area networks (VLANs) separating the various traffic:

  1. VLAN 100: Cluster (Ingress virtual internet protocol addresses (VIPs), cluster/node IPs) with IPv4 subnet provided by customers.
  2. VLAN 501: Management (iLO, Mgmt) with IPv4 subnet provided by the customer.



![Logical network](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/logical_network.png)

### Upper network topology

The cluster is configured using Layer 2 (L2) load balancing. The Ingress VIPs for the cluster come from the same subnet as the nodes. When an Ingress VIP is assigned to a node, the node uses Address Resolution Protocol (ARP) so that the node is reachable from the TOR.

The TOR peers with the customer network using BGP, and advertises the cluster's Ingress range (aggregated prefix provided by the customer) to the customer network. When the rack moves to a new location, we can advertise the cluster Ingress range to the new customer network. When the rack moves to a new location, you must manually update the IP addresses on the TOR interfaces connecting to the customer network, and update the BGP peering information to add the new BGP peers.

All IPs used by the cluster are either allocated from the rack's `externalCidrBlock`, or hardcoded (for cluster-internal IPs). In the following diagram, the `externalCidrBlock` example is `10.0.0.0/24`:

![The cluster uses L2 LB \(ARP\) to advertise 10.0.0.224.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/cidr-2.png)

#### Cluster IP ranges

There are several IP ranges that need to be configured in a bare metal cluster.

  * **Pod CIDR** : the IP range used to assign IPs to the pods in the cluster. This range uses island mode, so that the physical network (ToR) does not need to know about the pod CIDR. The only requirement is that the range cannot overlap with any services that the cluster pods need to access. The pod CIDR cannot be changed after the cluster is created.
  * **Service CIDR** : used for internal cluster services with the same requirement as the pod CIDR.
  * **Node CIDR** : IP addresses of the Kubernetes cluster nodes. These addresses also cannot change after the cluster is created.
  * **Ingress range** : a range of IP addresses used for any services in the cluster that are exposed externally. External clients use these IPs to access in-cluster services. This range needs to be advertised to the customer network so that clients can reach the Ingress IPs.
  * **Control plane VIP** : advertised by the cluster for access to the Kubernetes `api-server` (similar to the Ingress VIPs). This VIP must be from the same subnet as the node when the cluster is in L2 load balancing mode.



The Pod CIDR and Service CIDRs for the clusters are hardcoded. The Pod CIDR and the Service CIDR are `198.18.0.0/16`. The cluster uses the same CIDR, as this IP is not exposed outside of the cluster.

**Note:** Virtual Machine (VM) IP addresses are assigned from the `instance-default-vpc-cidr` range, which is fixed at `192.168.0.0/16`. If the appliance is connected to a customer network through the TOR switch, it is crucial to ensure that the customer network's IP range does not conflict with the `192.168.0.0/16` range. Overlapping IP ranges can lead to incorrect routing of appliance traffic.

The nodes are provisioned with IP addresses from the `externalCidrBlock` set in the GDC `cell.yaml`. These IP addresses are provided by the customer before the rack is provisioned.

The Ingress range and control plane VIP for the cluster are also allocated from the `externalCidrBlock`. The TOR must advertise the `externalCidrBlock` to the customer network so that these VIPs are accessible to clients outside of the rack.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
