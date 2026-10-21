---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel/
title: Add a VPN tunnel \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:51.116827+00:00
---

# Add a VPN tunnel  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Add a VPN tunnel Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add VPN tunnels to HA VPN or Classic VPN.

If you haven't set up your HA VPN gateway yet, see the following:

  * [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)
  * [Create HA VPN gateways to connect VPC networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2)
  * [Add an HA VPN gateway to HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/add-gateway-ha-vpn-interconnect)

**Note:** To create and configure an HA VPN over Cloud Interconnect deployment, see [Deploy HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-deploy-process).



## Add a tunnel from an HA VPN gateway to a peer VPN gateway

To receive a 99.99% uptime SLA, configure a tunnel on each HA VPN interface. This section includes the steps to configure additional tunnels on the interface of an HA VPN gateway.

Configure additional HA VPN tunnels in the following circumstances:

  * If you configured an HA VPN gateway to a peer VPN gateway that has a single peer VPN interface.
  * If you previously set up a single tunnel on an HA VPN gateway for a peer VPN gateway that contains any number of interfaces, but you now want a 99.99% uptime SLA for your HA VPN gateway.
  * If you deployed HA VPN over Cloud Interconnect and you need to add HA VPN tunnels to accommodate the increased capacity of a VLAN attachment.



To configure additional HA VPN tunnels, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  Console

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=tunnels)

  2. Click **Create VPN tunnel**.

  3. From the drop-down menu, select the gateway that requires the additional tunnel, and then click **Continue**.

  4. Choose a Cloud Router. If you haven't configured a Cloud Router, follow the steps for creating one in the [**Create VPN tunnels**](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#creating-ha-gw-peer-tunnel) procedure.

  5. For **Peer VPN gateway** , select **On-prem or Non Google Cloud**.

  6. For **Peer VPN gateway name** , choose the existing peer VPN gateway resource that the new tunnel will use. To check existing peer VPN gateway names for this Cloud VPN gateway, under **VPN gateway name** near the top of the page, click **View all existing tunnels**.

  7. You might receive a warning that a tunnel with the same peer VPN gateway interface is already associated with the same local Cloud VPN gateway interface. To fix this issue, under **Associated Cloud VPN gateway interface** , select the other HA VPN interface.

  8. To finish configuring the tunnel, configure the remainder of the steps as listed in the [**Create VPN tunnels**](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#creating-ha-gw-peer-tunnel) procedure.




## Add a tunnel from an HA VPN gateway to another HA VPN gateway

This section includes the steps to configure a second tunnel on the second interface of an HA VPN gateway.

If you configured one tunnel on an HA VPN gateway to another HA VPN gateway but want to receive a 99.99% uptime SLA, you must configure a second tunnel. Configure a tunnel on each HA VPN interface on each side of an HA VPN-to-HA VPN gateway configuration.

To configure a second tunnel, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=gateways)

  2. Find the HA VPN that you want to add the tunnel to.

  3. Click **Add VPN tunnel**.

  4. Under **Peer VPN gateway** , select **Google Cloud**.

  5. Under **Project** , select a Google Cloud project that will contain the new gateway.

  6. For **VPN gateway name** , choose the other HA VPN gateway that the new tunnel connects to.

  7. Select **Add the second VPN tunnel to an existing VPN tunnel for high availability**.

  8. Under **Select existing VPN tunnel** , make sure that the existing tunnel is selected. You can click a link to view all existing tunnels near the top of the same page.

  9. Specify a tunnel **Name**.

  10. Specify the same **IKE version** in use by the tunnel on the other gateway.

  11. Specify an **IKE pre-shared key** by using your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway. If you haven't configured a pre-shared key on your peer VPN gateway and want to generate one, click **Generate and copy**. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.

  12. Click **Create and continue**.

  13. Configure and save a **BGP session**. Otherwise, you can do this later by following the steps in the [**Create BGP sessions**](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#creating-ha-gw-2-gw-and-tunnel) procedure.

  14. Check the **Summary and reminder** page for configuration information, and then click **OK**.




## Add a tunnel to Classic VPN

Each Cloud VPN tunnel associated with a Classic VPN gateway _must_ connect to a _unique_ peer VPN gateway, as identified by the peer gateway's IP address. If you need to create a second tunnel to the same peer gateway, you must create that tunnel from a different Cloud VPN gateway.

**Note:** The IP address of the peer VPN gateway must be an external IP address. You can't use IP addresses that are listed in either [RFC 5737](https://tools.ietf.org/html/rfc5737) or [RFC 5735](https://datatracker.ietf.org/doc/html/rfc5735). The peer gateway must use its external IP address to identify itself, [even if it's located behind a NAT device](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#gateways_behind_nat).

To configure a second tunnel, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  Console 

**Note:** Before creating a tunnel that uses policy-based routing or a route-based VPN, review the details for [traffic selectors](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#static-routing-networks). Pay special attention to the notes about [multiple IP ranges](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-ip-ranges).

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. Click the **Google VPN gateways** tab.

  3. Click the name of an existing VPN gateway.

  4. On the **VPN gateway details** page, in the **Tunnels** section, click **Add VPN tunnel**.

  5. Supply the following information:

     1. In the **Name** field, enter a name for the tunnel.
     2. In the **Remote peer IP address** field, enter the external IP address of the peer VPN gateway.
     3. Choose an **IKE version** compatible with your peer VPN gateway.
     4. Provide the **IKE pre-shared key** (shared secret) for authentication. For suggestions, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key).
     5. Click the appropriate [**Routing option**](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#routing-options): 
        * To use dynamic routing, click **Dynamic (BGP)**. On the **Cloud Router** menu, select or create a new Cloud Router. To define the BGP session parameters, in the **BGP session** field, click edit**Edit**. Each BGP IP address range for each BGP session must be unique among all Cloud Routers in all regions of a Virtual Private Cloud (VPC) network.
        * To use route-based VPN, click **Route-based**. In the **Remote network IP ranges** field, supply the ranges of IP addresses used by the peer network.
        * To use policy-based routing, click **Policy-based**. Supply both the **Remote network IP ranges** and the **Local IP ranges**. In the **Local subnetworks** menu, select IP ranges of subnets in a VPC network.
  6. Click **Create**.

  7. Complete your configuration by following the steps in [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).




###  gcloud 

Follow the steps for creating a route-based VPN gateway and tunnel, but start in the section [Create the Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns#creating_a_gateway_and_tunnel).

If the new tunnel has the same CIDR block, you can skip to [Configure firewall rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules).

## Check tunnel status

After you configure an HA VPN or Classic VPN tunnel, [check its status](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status).

## What's next

  * To view Cloud Logging and Monitoring information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
