---
url: https://docs.cloud.google.com/bigquery/docs/aws-vpn-network-attachment/
title: Set up AWS VPN and network attachments \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:12.285721+00:00
---

# Set up AWS VPN and network attachments  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/aws-vpn-network-attachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up AWS VPN and network attachments

A VPN and network attachment let you establish a reliable, security-enhanced connection between Amazon Web Services (AWS) and Google Cloud. By configuring gateways, tunnels, and routes across both cloud environments, you can direct traffic between your deployed databases and instances.

## Before you begin

Ensure that you have the following:

  * Access to AWS and Google Cloud accounts with appropriate permissions.
  * Existing [Virtual Private Clouds](https://docs.cloud.google.com/vpc/docs/overview) in both AWS and Google Cloud.



## Set up networking on AWS

  1. Create a virtual private gateway that is attached to the VPC where your database is deployed. For detailed instructions, see [Create an AWS Direct Connect virtual private gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-virtual-private-gateway.html) in the AWS documentation.
  2. Create a customer gateway using the public IP address of your Google Cloud VPN gateway. For detailed instructions, see [Create a customer gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-cgw) in the AWS documentation.
  3. Create the VPN connection using the virtual private gateway and customer gateway that you created earlier. For detailed instructions, see [Get started with AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html) and [How do I establish an encrypted connection over an AWS Direct Connect connection?](https://repost.aws/knowledge-center/create-vpn-direct-connect) in the AWS documentation.
  4. Add routes to direct traffic to the Google Cloud IP ranges using the VPN connection. For detailed instructions, see [Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) and [Configure routing](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-configure-route-tables) in the AWS documentation.



## Set up networking on Google Cloud

The setup on Google Cloud requires creating the VPN gateway and VPN tunnels, configuring the routes, and creating the Google Cloud network attachment.

### Create the VPN gateway

**Note:** The following steps describe how to create a [Classic VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#classic-vpn). You can create a high-availability (HA) VPN instead if it fits your use case. For more information, see [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

  1. In the Google Cloud console, go to the **Cloud VPN gateways** page.

[Go to Cloud VPN gateways](https://console.cloud.google.com/hybrid/vpn?tab=gateways)

  2. Click **Create VPN gateway**.

  3. Select the **Classic VPN** option button.

  4. Provide a VPN gateway name.

  5. Select an existing VPC network in which to create the VPN gateway and tunnel.

  6. Select the region.

  7. For **IP address** , create or choose an existing regional [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).

  8. Provide a tunnel name.

  9. For **Remote peer IP address** , enter the AWS VPN gateway public IP address.

  10. Specify options for **IKE version** and **IKE pre-shared key**.

  11. Specify the routing options as required to direct traffic to the AWS IP ranges.

  12. Click **Create**.




For more information, see [Create a gateway and tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns#create_a_gateway_and_tunnel).

### Create the network attachment

  1. In the Google Cloud console, go to the **Network attachments** page.

[Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

  2. Click add **Create network attachment**.

  3. Provide a name for the network attachment.

  4. For **Network** , select the appropriate VPC network.

  5. For **Region** , choose where your VPN gateway is located.

  6. For **Subnetwork** , select the VPN tunnel that you created earlier.

  7. Click **Create network attachment**.




For more information, see [Create network attachments](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-network-attachments).

## Test the VPN connection

  1. Deploy the instances in both the AWS and Google Cloud VPC environments.
  2. To verify connectivity, attempt to ping or connect to instances across the VPN.
  3. Ensure the security groups and firewall rules allow for traffic through the VPN.



## Troubleshoot

If you're having issues setting up your network attachment, do the following:

  * Ensure that the VPN connections are up and running in both the AWS console and the Google Cloud console.
  * Check the VPN logs for errors or dropped packets.
  * Verify that the routing tables in both AWS and Google Cloud are correctly configured.
  * Ensure that the necessary ports are open in both the AWS security groups and the Google Cloud firewall rules.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
