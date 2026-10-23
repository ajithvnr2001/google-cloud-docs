---
url: https://docs.cloud.google.com/vmware-engine/docs/quickstart-network-segment/
title: Creating your first subnet \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:49.893025+00:00
---

# Creating your first subnet  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/quickstart-network-segment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating your first subnet

Google Cloud VMware Engine creates a network for each private cloud and uses VLANs for network management. For workload virtual machines (VMs), you create subnets as network segments on NSX Manager for your private cloud. VMware Engine includes NSX for workload networking and security features such as microsegmentation and firewall policies. This page explains how to create subnets for your workloads using NSX Manager.

## Before you begin

This quickstart assumes that you have done the following:

  1. Created a Google Cloud VMware Engine private cloud. You can create one by completing the following quickstart: [Creating your first private cloud](https://docs.cloud.google.com/vmware-engine/docs/create-private-cloud).
  2. Allocated address ranges in your network for the following purposes: 
     * A DHCP service
     * A subnet for the NSX workload network segment

**Note:** VMware Engine gives you administrator access to NSX Manager by default. If you prefer role-based access control (RBAC) for NSX, then you must set up VMware Identity Manager (vIDM). If you require [RBAC for NSX](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-1CAC911E-A224-4521-A9A2-0D668B4BFB61.html), [contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/support).

## Access NSX Manager from the VMware Engine portal

The process of creating a subnet happens in NSX, which you access through VMware Engine:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Click the private cloud name where you want to create the subnet.

  4. Under **Management appliances** , click the **URL** corresponding to NSX Manager.

  5. When prompted, enter your sign-in credentials. As a reminder, you can [retrieve generated credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client#sign-in) from the private cloud details page.




If you've set up vIDM and connected it to an identity source, such as Active Directory, use your identity source credentials instead.

## Set up DHCP service for the subnet

Before you can create a subnet, set up a DHCP service:

  1. In NSX, go to **Networking > DHCP**. The networking dashboard shows that the service creates one tier-0 and one tier-1 gateway.
  2. To begin provisioning a DHCP server, click **Add DHCP Profile**.

**Note:** NSX supports DHCP relay as well. For more information, see the VMware documentation for [creating a DHCP relay service](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-2505EDA1-769C-46A5-A206-38EF9B760C9A.html)
  3. In the **DHCP name** field, enter a name for the profile.

  4. For **Profile type** , select **DHCP server**.

  5. In the **Server IP address** column, provide a DHCP service IP address range.

  6. Click **Save** to create the DHCP service.




## Create a network segment in NSX

For workload VMs, you create subnets as NSX network segments for your private cloud:

  1. In NSX, go to **Networking > Segments**.
  2. Click **Add Segment**.
  3. In the **Segment Name** field, enter a name for your segment.
  4. In the **Connected Gateway** list, select **Tier1** to connect to the tier-1 gateway.
  5. In the **Transport zone** list, select **TZ-OVERLAY | Overlay**.
  6. In the **Subnets** column, enter the subnet range. Specify the subnet range with `.1` as the last octet. For example, `10.12.2.1/24`.
  7. Click **Set DHCP Config**.
  8. Set **DHCP Type** to **Segment DHCP Server**.
  9. Select the **DHCP Server Profile** that you just created.
  10. Provide values for **DHCP Ranges** and click **Apply**.
  11. Click **Save**. You can now select this network segment in vCenter when creating a VM.



In a given region, you can advertise at most **250** unique routes from VMware Engine to your VPC network using private services access. For example, those unique routes include private cloud management IP address ranges, NSX workload network segments, and HCX internal IP address ranges. This route limit includes all private clouds in the region and corresponds to the Cloud Router learned route limit.

For information about routing limits, see [Cloud Router Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

## Best practices for subnet configuration and route redistribution in NSX

To ensure optimal network operation and to prevent routing loops and service disruptions, follow these guidelines when configuring subnets and routes redistribution within NSX:

  1. **Subnet overlapping** : Avoid overlapping subnets - Ensure that IP subnets used in VMware Engine are unique and don't overlap with subnets in your private cloud or external networks. Overlaps can cause routing problems and disrupt services.
  2. **Tier-0 route redistribution** : 
     * Automatic redistribution - VMware Engine redistributes routes for connected Tier-1 segments within the Tier-0 router using BGP for proper connectivity between workloads and the external world.
     * Redistributing static routes - When redistributing static routes on Tier-0, it's crucial to first deny the default route (`0.0.0.0/0`) and then allow all traffic using a prefix list to prevent routing loops. To do this, you should create and attach a prefix-list to both of the BGP neighbors on the Tier-0 gateway, as VMware Engine already configures a default route (`0.0.0.0/0`) on Tier-0 gateways pointing toward the underlying infrastructure, which you can do by following the steps in the next two sections.



## Create a prefix-list in NSX

To create a prefix-list in NSX in VMware Engine, do the following:

  1. In NSX, go to **Networking > Tier-0 Gateways**.
  2. Click the menu icon (three dots) and click **Edit**.
  3. Click **Routing**.
  4. Click **Set** next to IP Prefix List.
  5. Click **Add IP Prefix List**.
  6. Enter a name for the IP prefix list.
  7. Click **Set** to add IP prefixes.
  8. Click **Add Prefix**. 
     1. In the **Network** field, enter a keyword "any".
     2. Leave all fields as is, and in the **Action** field, select **Permit** from the drop-down menu.
     3. Click **Add**.
  9. Click **Add Prefix** again. 
     1. In the **Network** field, enter an IP address in CIDR format, for example `0.0.0.0/0`.
     2. Leave all fields as is, and in the **Action** field, select Deny from the drop-down menu.
     3. Click **Add**.
  10. Click **Apply**.
  11. Click **Save > Close**.



## Attach the prefix-list to both BGP neighbors

After creating the prefix-list, the next task is to attach the prefix-list to both the BGP neighbors in NSX by doing the following:

  1. In NSX, go to **Networking > Tier-0 Gateways**.
  2. Click the menu icon (three dots) and click **Edit**.
  3. Click **BGP**.
  4. Click **BGP Neighbors**.
  5. Click the menu icon (three dots) and select **Edit**.
  6. Click **Route Filter**.
  7. Click the menu icon (three dots) and select **Edit**.
  8. Click **Configure** on the **Out Filter** field.
  9. Select the prefix-list name previously created.
  10. Click **Save**.
  11. Click **Add > Apply**.
  12. Click **Save**.
  13. Repeat steps 5-13 to update another BGP neighbor.
  14. Click **Close Editing**.



## What's next

  * Learn more about [IP address management (IPAM)](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-A27DF20A-5162-40F5-B7D5-2DF8B6AE5DBE.html) using NSX.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
