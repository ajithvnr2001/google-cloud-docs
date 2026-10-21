---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpn-connect/
title: Connecting using VPN \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:22.179625+00:00
---

# Connecting using VPN  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpn-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting using VPN

This article describes how to connect to your private cloud after you have a point-to-site VPN gateway set up.

To establish a site-to-site connection between your on-premises network and your private cloud, use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) instead. For more details about Cloud VPN and Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

## Before you begin

This process requires you to have a point-to-site VPN gateway. For details on creating one, see [VPN gateways](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways).

## Connect to VMware Engine using point-to-site VPN

To connect to VMware Engine from your computer, you need a VPN client and a connection profile. Examples of VPN clients are [OpenVPN GUI](https://openvpn.net/community-downloads/) for Windows or [Viscosity](https://www.sparklabs.com/viscosity/download/) for macOS and OS X.

### Get a connection profile

A connection profile, sometimes known as a VPN configuration file, includes certificates and other instructions for a VPN client. Download your connection profile from the VPN gateway that you plan to use to connect to your VMware Engine network.

For example, OpenVPN Access Server [provides connection profiles](https://openvpn.net/vpn-server-resources/create-connection-profiles-and-connect-client-installers/) either as setup files or as part of pre-configured VPN client installers. You can then connect to OpenVPN Access Server using that connection profile. Connection options include the following, among others:

  * [Connect to Access Server with OpenVPN Connect or OpenVPN GUI in Windows](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-windows/)
  * [Import the configuration in Viscosity](https://www.sparklabs.com/support/kb/article/getting-started-with-viscosity-mac/#creating-your-first-connection)



### Example: Importing the VPN connection using Viscosity

  1. Extract the contents of the VPN configuration from the downloaded zip file.
  2. Open Viscosity on your computer.
  3. Click add **Add** and select **Import connection > From file**.
  4. Select the OpenVPN configuration file (`.ovpn`) for the protocol you want to use, and click **Open**. The connection now appears in the **Viscosity** menu.
  5. In the Viscosity OpenVPN client, connect to the VPN by selecting the connection from the **Viscosity** menu. The menu icon updates to indicate that the connection is established.



### Example: Connecting to multiple private clouds using Viscosity

A point-to-site VPN connection resolves the DNS names of the first private cloud that you create. When you want to access other private clouds, you must update the DNS server on your VPN client.

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to connect to.

  3. On the **Summary** page of the private cloud, under **Basic Info** , copy the private cloud DNS server IP address.

  4. Right-click the Viscosity icon in your computer's system tray, and select **Preferences**.

  5. Select the VPN connection name, and click **Edit** to change the connection properties.

  6. On the **Networking** tab, enter the following information:

     * **Servers:** private cloud DNS server IP addresses, separated by a comma or space
     * **Domains:** the domain `gve.goog`
     * Select the **Ignore DNS settings sent by VPN server** checkbox.

**Important:** To connect to your first private cloud, remove the settings and connect to the VPN server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
