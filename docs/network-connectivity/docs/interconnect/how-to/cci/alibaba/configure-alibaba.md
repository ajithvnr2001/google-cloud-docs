---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-alibaba/
title: Configure your Alibaba Cloud resources \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:52.617076+00:00
---

# Configure your Alibaba Cloud resources  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-alibaba/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure your Alibaba Cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [Alibaba Cloud documentation](https://www.alibabacloud.com/help/) . 

After you configure your Google Cloud resources, configure your Alibaba Cloud resources.

For the most up-to-date information about how to create a Virtual Border Router (VBR), see [Create and manage a VBR](https://www.alibabacloud.com/help/en/express-connect/latest/create-a-vbr) in the Alibaba Cloud documentation.

## Create a Virtual Border Router (VBR)

A VBR connects customer premises equipment to a Virtual Private Cloud (VPC) network and allows data transfer between them.

To create a VBR, follow these steps.

###  Console 

  1. Log in to the [Alibaba Cloud Express Connect console](https://www.alibabacloud.com/help/en/express-connect).
  2. On the **Virtual Border Router** page, click **Create VBR** , and then set the following parameters:

     1. For **Physical Connection Interface** , select **Express Connect circuit** , and then select the **Express Connect circuit ID** from the list.
     2. For **VLAN ID** , enter the VLAN ID that you used earlier when configuring Google resources.
     3. For **Set VBR Bandwidth Value** , enter your desired bandwidth.
     4. For **IPv4 Address (Alibaba Cloud Gateway)** , enter the BGP peer IP address of the Google Cloud Router BGP peering.
     5. For **IPv4 Address (Data Center Gateway)** , enter the Cloud Router BGP IP address of the Google Cloud Router BGP peering.
  3. Click **OK**.




## Create a VBR-to-VPC network connection

To connect the VBR to a VPC network, follow these steps.

###  Console 

  1. In the Express Connect console, go to the **VPC Peering Connections > VBR-to-VPC** page.
  2. Click **Create Peering Connection** , and then set the following parameters:

     1. For **Initiator Region** , select the region where you created the VBR.
     2. For **Initiator VBR** , select the VBR that you created.
     3. For **Acceptor Region Type** , select **Intra-Region** if the VPC network is in the same region as the VBR. Select **Inter-Region** if the VPC network is in a different region.
     4. For **Acceptor VPC** , select the VPC network that you want to connect to Google Cloud.
     5. Select the **I have read and accept the Terms of Service for Express Connect Peering Connections (Pay-As-You-Go)** checkbox.
  3. Click **OK**.




## Create a custom route in the VPC network

To create a custom route in the VPC network, follow these steps:

###  Console 

  1. In the VPC console, on the **Route Tables** page, click the route table.
  2. On the specific route table page, choose the **Custom Route** tab under the **Route Entry List** tab.
  3. Click **Add Route Entry** , and then set the following parameters:

     1. For **Destination CIDR Block** , enter the VPC IP address range in Google Cloud.
     2. For **Next Hop Type** , select **Router Interface (To VBR)** , click **General Routing** , and then select the VBR.
  4. Click **OK**.




## Create a custom route in the VBR

To create a custom route in the VBR, follow these steps.

###  Console 

  1. In the Express Connect console, on the **Virtual Border Router** page, click the VBR.
  2. On the specific **VBR** page, click the **Routes** tab.
  3. Click **Add Route** , and then set the following parameters:

     1. For **Next Hop Type** , select **VPC**.
     2. For **Destination CIDR Block** , enter the VPC network IP address range on Alibaba Cloud.
     3. For **Next Hop** , select the VPC network.
  4. Click **OK**.




## Configure BGP peering in a VBR

To set up BGP peering in the VBR, follow these steps.

###  Console 

  1. In the Express Connect console, on the **Virtual Border Router** page, click the VBR.
  2. On the corresponding **VBR** page, click the **BGP Groups** tab.
  3. Click **Create BGP Group** , and then set the following parameters:

     1. For **Peer ASN** , enter the ASN that you specified in the Cloud Router on Google Cloud.
     2. If you configured BGP MD5 authentication on your Google Cloud Router BGP peering, for **BGP Key** , enter the BGP MD5 key.
     3. Click **OK**.
  4. On the corresponding **VBR** page, click the **BGP Peers** tab.

  5. Click **Create BGP Peer** , and then set the following parameters:

     1. For **BGP Group** , select the BGP group.
     2. For **BGP Peer IP** , enter the VLAN attachment's Cloud Router BGP IP.
     3. If you enabled Bidirectional Forwarding Detection (BFD) on your Google Cloud Router BGP peering, check the **Enable BFD** option.
     4. Click **OK**.
  6. On the corresponding **VBR** page, click the **Advertised BGP Subnets** tab.

  7. Click **Advertise BGP Subnet** , and then set the following parameters:

     1. For **Advertised Subnet** , enter the VPC network IP address range on Alibaba Cloud.
     2. Click **OK**.



[ Previous arrow_back  Configure your Google Cloud resources  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources)

[ Next Verify your connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/test-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
