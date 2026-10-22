---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-oci/
title: Configure your OCI resources \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:11.657165+00:00
---

# Configure your OCI resources  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-oci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure your OCI resources Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm) . 

After you configure your Google Cloud resources, configure your Oracle Cloud Infrastructure (OCI) resources.

## Create a VCN

Create a virtual cloud network (VCN) that's in the same region and tenancy as your FastConnect ports.

###  Console 

**Note:** For the most up-to-date information about how to create a VCN, see [Working with VCNs and subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#working) in the OCI documentation.

  1. Sign in to the OCI console.

  2. Make sure that the **Regions** list shows the region where your FastConnect port is located.

  3. In the menu menu, select **Networking > Virtual cloud networks**.

  4. Click **Create VCN**.

  5. Fill in the required fields, and then define at least one IPv4 CIDR block.

  6. Click **Create VCN**.




## Create a subnet

In your VCN, create a subnet.

###  Console 

**Note:** For the most up-to-date information about how to create a subnet, see [Working with VCNs and subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#working) in the OCI documentation.

  1. If you don't already have it displayed, navigate to the VCN that you just created.

  2. Click **Add subnet**.

  3. Fill in the required fields, and then define at least one IPv4 CIDR block.

  4. Click **Create Subnet**.




## Create a DRG and attach it to your VCN

A Dynamic Routing Gateway (DRG) is a virtual router. Create a DRG and attach it to your VCN.

###  Console 

**Note:** For the most up-to-date information about how to create a DRG, see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#console) in the OCI documentation.

  1. In the menu menu, select **Networking**. In the **Customer connectivity** section, select **Dynamic routing gateway**.

  2. Click **Create Dynamic Routing Gateway**.

  3. Enter a name.

  4. Click **Create Dynamic Routing Gateway**.

  5. OCI displays a page that represents the DRG; you might have to wait a few minutes for the system to provision the resource. While it does so, the controls on the page are disabled. When the controls become active, click **Create Virtual Cloud Network Attachment**.

  6. Enter an attachment name.

  7. Select the **VCN network** that you created previously.

**Note:** Don't change any of the values listed under **Advanced options**.
  8. Click **Create Virtual Cloud Network Attachment**.




## Create a private virtual circuit

For each of your FastConnect resources, create a private virtual circuit. As part of this process, you configure a Border Gateway Protocol (BGP) session.

Complete the following steps twice. The first time, use the values that you set for your primary VLAN attachment. The second time, use the values from your redundant attachment.

###  Console 

**Note:** For the most up-to-date information about how to create a virtual circuit, see the Set up your virtual circuits section on the [Getting started with FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#getstarted) page in the OCI documentation.

  1. In the menu menu, select **Networking**. In the **Customer connectivity** section, select **FastConnect**.

  2. Click the name of your FastConnect resource.

  3. Click **Virtual circuits**. The page updates to include additional options.

  4. Click **Add virtual circuit**.

  5. Fill out the **Create virtual circuit form** :

     * Enter a name for the circuit.

     * Select the **Private virtual circuit** box.

     * Select the **DRG** that you created previously.

     * In the **Provisioned bandwidth** field, enter the capacity that you chose for your Google Cloud VLAN attachment.

     * In the **VLAN** field, enter the same VLAN ID that you chose for your Google Cloud VLAN attachment.

     * In the **Customer BGP IPv4 address** field, enter the value from the **Cloud Router BGP IP** field on your Google Cloud VLAN attachment.

     * In the **Oracle BGP IPv4 address** field, enter the value from the **BGP Peer IP** field on your Google Cloud VLAN attachment.

     * In the **Customer BGP ASN** field, enter the value of your Google Cloud Router ASN.

     * If you configured MD5 authentication on the Cloud Router, select **Use a BGP MD5 authentication key** , and enter your key.

     * Optional: Adjust the MTU from the default setting of `1500`.

  6. Click **Create**.




After you create each circuit, you see the corresponding BGP session.

[ Previous arrow_back  Configure your Google Cloud resources  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources)

[ Next Verify your connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/test-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
