---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/requesting-oci-connections/
title: Request connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:23.479399+00:00
---

# Request connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/requesting-oci-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Request connections Stay organized with collections  Save and categorize content based on your preferences. 

After you configure your Google Cloud resources, configure your Oracle Cloud Infrastructure (OCI) resources. This page provides instructions about how to configure OCI resources to connect with Google Cloud.

After you create VLAN attachments for a Cross-Cloud Interconnect for OCI connection, configure your OCI resources by creating an OCI FastConnect virtual circuit to establish connectivity into your OCI virtual cloud network (VCN).

OCI configures your VLAN attachments after the virtual circuit is created. To request a partner Cross-Cloud Interconnect for OCI connection, contact Oracle or visit their portal.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using partner Cross-Cloud Interconnect for OCI, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

When you request a connection, OCI requires the following information:

  * **Your VLAN attachment's[pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey)**: this pairing key is generated when you create the VLAN attachment.

  * **The VLAN attachment's[region](https://docs.cloud.google.com/compute/docs/regions-zones)**: the region that you select must be supported by a [partner Cross-Cloud Interconnect for OCI location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#provisioning), which is a city where OCI's network meets Google Cloud's network. Traffic between your Virtual Private Cloud (VPC) network and the OCI's network passes through this location. You must [choose an OCI location that's paired with the Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations).

  * **Your VLAN attachment's connection capacity** : this capacity can range from 1 Gbps to 50 Gbps. The capacity depends on your bandwidth requirements and what's offered by OCI. [Pricing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing#partner-pricing) for each VLAN attachment is based on its capacity.




After you request a connection and the OCI VLAN attachment configuration is complete, you receive an email notification from Google. The state of your attachment changes from `PENDING_PARTNER` to `PENDING_CUSTOMER`. If you [pre-activated](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) your attachment, it changes to `ACTIVE`.

**Note:** If your VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact OCI assistance.

If you pre-activated your VLAN attachment, the attachment can immediately start passing traffic. If not, you must activate the attachment before it can pass traffic.

## Configure OCI resources

OCI resources must be created in the OCI location paired with the Google Cloud location. For a list of paired locations, see [Paired locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations).

**Note:** For the most up-to-date information about how to configure OCI resources, see [Access to Google Cloud Platform](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/access-to-google-cloud-platform.htm#unique_1638782181) in the OCI documentation.

## Create a VCN

Create a virtual cloud network (VCN) that's in the same region and tenancy as your FastConnect ports.

###  OCI console 

**Note:** For the most up-to-date information about how to create a VCN, see [Creating a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm) in the OCI documentation.

  1. Sign in to the OCI console.
  2. Make sure that the **Regions** list shows the region where your FastConnect port is located.
  3. In the menumenu, select **Networking > Virtual cloud networks**.
  4. Click **Create VCN**.
  5. Fill in the required fields, and then define at least one IPv4 CIDR block.
  6. Click **Create VCN**.



## Create a subnet

In your VCN, create a subnet.

###  OCI console 

**Note:** For the most up-to-date information about how to create a subnet, see [Creating a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create_vcn.htm) in the OCI documentation.

  1. In the OCI console, go to the VCN that you just created.
  2. Click **Add subnet**.
  3. Fill in the required fields, and then define at least one IPv4 CIDR block.
  4. Click **Create Subnet**.



## Create a DRG and attach it to your VCN

A Dynamic Routing Gateway (DRG) is a virtual router. Create a DRG and attach it to your VCN.

###  OCI console 

**Note:** For the most up-to-date information about how to create a DRG, see [Creating a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create.htm) in the OCI documentation.

  1. In the OCI console, on the menumenu, select **Networking**.
  2. In the **Customer connectivity** section, select **Dynamic routing gateway**.

  3. Click **Create Dynamic Routing Gateway**.

  4. Enter a name.

  5. Click **Create Dynamic Routing Gateway**. OCI displays a page that represents the DRG; you might have to wait a few minutes for the system to provision the resource. While it does so, the controls on the page are disabled. When the controls become active, continue to the next step.

  6. Click **Create Virtual Cloud Network Attachment**.

  7. Enter an attachment name.

  8. Select the **VCN network** that you created previously.

**Note:** Don't change any of the values listed in the **Advanced options** section.
  9. Click **Create Virtual Cloud Network Attachment**.




## Create a private virtual circuit

Create a private virtual circuit for each FastConnect resource. If you created a pair of VLAN attachments, complete the following steps for each one.

###  OCI console 

  1. Choose a compartment. If you're not sure which one, choose the compartment that contains the DRG to connect to. This compartment, along with a corresponding IAM policy, controls who can access the virtual circuit.
  2. On the main menu, click **Networking**.
  3. In the **Customer connectivity** section, click **FastConnect**.
  4. Click **Create Connection**.
  5. In the **Connection types** section, select **FastConnect partner** , and then choose **Google Cloud: OCI Interconnect**.
  6. In the **Name** field, enter a name for the circuit. The value doesn't need to be unique across your virtual circuits, and you can change it later.
  7. Leave the **Create in compartment** list as it is (the compartment you're in).
  8. For **Virtual circuit type** , select **Private virtual circuit**.
  9. In the **Dynamic routing gateway** list, the DRG you set up earlier is shown. If not, change the compartment to the one that stores the DRG, and then select the DRG.
  10. In the **Provisioned bandwidth** list, select the capacity that you chose for your VLAN attachment (or the closest value available).
  11. In the **Partner service key** field, enter the pairing key you received from Google Cloud when you created the VLAN attachment.
  12. In the **MTU** field, enter `1500` as the MTU value.
  13. Click **Continue**. The virtual circuit is provisioned.
  14. Click **Close**.



After the virtual circuit is provisioned, the connection to Google Cloud is active. Then you can activate any VLAN attachments that you didn't pre-activate when you created them. Check the status of provisioning virtual circuits in FastConnect.

After the OCI virtual circuit is created, Google automatically configures an interface and a BGP peering session on the associated Cloud Router. Don't modify these Google-defined configurations because doing so shuts down the BGP session. However, if you delete your attachment, you can delete these configurations.

[ Previous arrow_back  Create VLAN attachments  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/creating-vlan-attachments)

[ Next Activate connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/activating-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
