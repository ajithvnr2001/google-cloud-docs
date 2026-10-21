---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-migrate-from-google-solutions/
title: Migrate from other Google Cloud solutions \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.296670+00:00
---

# Migrate from other Google Cloud solutions  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-migrate-from-google-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Migrate from other Google Cloud solutions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the migration options from VPC Network Peering and HA VPN to Virtual Private Cloud (VPC) spokes within Network Connectivity Center (NCC).

## Migrate from VPC Network Peering to NCC star topology

To migrate from VPC Network Peering to a NCC star topology configuration, which is a multipoint topology, you must configure the NCC hub for star topology. If the existing VPC Network Peering topology is in a hub and spoke or full mesh design, you can implement NCC star topology to group NCC VPC spokes into a center group or an edge group.

Choose one of the following two possible scenarios depending on the topology you choose post migration:

  * Migrate from VPC Network Peering hub and spoke topology to NCC star topology
  * Migrate from VPC Network Peering full mesh topology to NCC star topology



### Migrate from VPC Network Peering hub and spoke topology to NCC star topology

If you have a multipoint topology with a routing VPC network with hybrid attachments that is connected to workload VPC networks through VPC Network Peering, follow these migration steps.

  1. [Create a new NCC hub with a star topology configuration](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub). Leave the existing hybrid connectivity and the routing VPC intact.
  2. Create a new routing VPC network and attach it as a spoke to the NCC hub that you created. Make sure it is mapped to the center group.
  3. [Create a new VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) from existing Cloud Interconnect connections. You can also create new HA VPN tunnels on a new gateway. Connect the VLAN attachment or tunnel as a hybrid spoke to join the NCC hub that you created in step 1.
  4. After you have the new routing VPC network connected to your on-premises network using BGP and you're advertising all the dynamic routes to the new star topology hub, you can configure your workload VPC networks that are in your VPC Network Peering topology, as part of the edge group VPC spokes to the star topology hub.



If two workload VPC networks are connected together with VPC Network Peering, they can't be configured as NCC VPC spokes. Configuring the VPC networks as NCC VPC spokes that belong to an edge group, removes any conflicts with VPC Network Peering because NCC doesn't directly connect these VPC networks together. NCC preserves the existing VPC Network Peering connection. The legacy hub VPC network isn't added to NCC; only the workload VPC networks are added to NCC.

When you are ready to cutover, you can steer traffic by changing the MED value being advertised from the on-premise router to steer traffic to the new NCC star topology hub.

To connect additional VPC network to resources in the center group, you can add them as workload VPC spokes to the edge group, which enables further growth using NCC.

### Migrate from VPC Network Peering mesh topology to NCC star topology

Suppose that you have two legacy workload VPC networks `VPC1` and `VPC2` that are connected through VPC Network Peering to each other and to a routing VPC network, where all three VPC networks are fully meshed.

NCC star topology edge groups allow existing VPC networks that are connected with VPC peering to join the NCC hub as a VPC spoke.

To migrate the workload VPC networks to NCC star topology, follow these steps:

  1. [Create a new NCC hub configured with star topology configuration](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub). To prevent disruption to production traffic, leave the existing hybrid connectivity and routing VPC network intact.
  2. [Create a new VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) and connect it to the new routing VPC network that you created. Add this VPC network and VLAN attachment as spokes of the NCC hub.
  3. Add the legacy workload VPC networks `VPC1` and `VPC2` to the edge group. When configured to be part of the center group, new VPC spokes use the data path established by NCC and not VPC Network Peering.
  4. To steer traffic from the legacy routing VPC network to the new NCC connected path, lower the MED values for the legacy VPC network.
  5. Remove the legacy VPC Network Peering that is connected to your on-premises network.
  6. Add any new workload VPC networks to the center group. They are automatically connected to workload `VPC1` and `VPC2`. `VPC1` and `VPC2` remain connected to each other through VPC Network Peering. All of the VPC networks now have full mesh connectivity between each other.



In this scenario, you don't need to disconnect the legacy VPC networks from VPC Network Peering. Existing VPC Network Peering peering between workload VPC networks in production remains intact and not subject to disruption.

However, you can add new VPCs to the center group to enable further growth using NCC.

## Migrate from VPC Network Peering to full mesh topology

When your NCC hub is configured to use the default mesh topology and you migrate to VPC spokes, the topology resulting from the migration is also a full mesh topology, which means that every VPC spoke is connected to every other VPC spoke.

For existing brownfield [hub-and-spoke network topology deployments](https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology) with Virtual Private Cloud (VPC) peering, migrating directly to VPC spokes can cause disruption to existing sessions. If you attempt to configure a VPC network pair as spokes, the NCC hub detects the existing VPC peering and generates an error.

You can choose one of the following two migration options:

  * Migrate with some downtime of existing VPC peering sessions
  * Migrate with minimal downtime by using HA VPN



### Migrate with downtime of existing VPC peering sessions

If your organization can support a change management window that disrupts VPC-to-VPC communication for a brief window of time, follow these steps.

  1. Schedule a downtime for the migration process.
  2. Delete existing VPC peering.
  3. [Configure VPCs as NCC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke). This enables full mesh connectivity.



NCC ensures that between any pair of VPC networks, there is no existing peering connection.

### Migrate with minimal downtime by using HA VPN

The following migration steps result in only a minimal downtime to your organization.

  1. [Configure a new HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2) between two peered VPC networks, for example `VPC1` and `VPC2`.
  2. Delete the existing VPC Network Peering between `VPC1` and `VPC2`. During this time, packets traverse the HA VPN tunnels and inter-VPC connectivity is sustained.
  3. Configure the two VPCs, `VPC1` and `VPC2`, as NCC spokes. For detailed instructions about how to create a VPC spoke, see [Propose a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke#propose_a_spoke). This enables full mesh connectivity.
  4. [Delete the HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).



## Migrate from HA VPN

If you are an existing customer using HA VPN tunnels to enable inter-VPC communication, there are two migration patterns available that depend on your existing deployment. Start by determining if the Cloud VPN tunnels are configured as NCC hybrid spokes or standalone HA VPN tunnels.

  * If the existing Cloud VPN tunnels are configured as NCC hybrid spokes and you have an existing NCC hub, `Hub1`, that you want to migrate, follow these steps.

**Note:** There is a traffic disruption between steps 2 and 3.
    1. [Create a new NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub), `Hub2`, to support inter-VPC communication.
    2. Delete the existing NCC hub, `Hub1`, where the Cloud VPN tunnels are configured to hybrid spokes.

For information about how to delete hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).

    3. [Add the VPC network to the new hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke).

    4. [Delete the HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

  * If the existing HA VPN tunnels are not configured as Cloud VPN hybrid spokes, follow these steps.

**Note:** There is no traffic disruption when HA VPN tunnels are not configured as Cloud VPN hybrid spokes.
    1. [Create a new NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).
    2. [Configure VPCs as NCC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke).
    3. [Delete the HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
