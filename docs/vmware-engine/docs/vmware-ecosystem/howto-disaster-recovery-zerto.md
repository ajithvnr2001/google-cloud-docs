---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto/
title: Configuring disaster recovery using Zerto \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:37.718675+00:00
---

# Configuring disaster recovery using Zerto  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuring disaster recovery using Zerto

To provide business continuity in the event of a disaster, you can set up your Google Cloud VMware Engine private cloud as a recovery site for your on-premises applications. You can follow a similar approach to set up the private cloud as a primary site that is protected by a recovery site on-premises, at a different location, or in a different VMware Engine private cloud.

VAIO with Zerto Solution version 10.0_U7 and later are supported with VMware Engine private clouds running vSphere 8.0. This recovery solution continuously replicates critical infrastructure and application virtual machines (VMs) from your on-premises vCenter to your private cloud.

If you have an existing Google Cloud VMware Engine private cloud with a previous version of Zerto Solution, you must update to the VAIO variant of Zerto Solution version 10.0_U7. For conversion instructions, see [Converting an Existing non-VAIO Deployment to the VAIO Variant](https://help.zerto.com/bundle/Linux.ZVM.HTML.10.0_U7/page/Converting_to_VAIO.htm).

**Note:** For information about sizing your disaster recovery environment, see the [Journal Overview Sizing and Best Practice](https://help.zerto.com/bundle/BP.Journal.Sizing.HTML/page/Journal_Overview_Sizing_and_Best_Practice.htm) article.

This recovery solution offers the following benefits:

  * Eliminates the need to set up a data center specifically for disaster recovery.
  * Helps with worldwide geographic resilience by leveraging the Google Cloud locations where VMware Engine is deployed.
  * Gives you an option to reduce deployment costs and total cost of ownership for disaster recovery.



This recovery solution requires you to do the following:

  * Install, configure, and manage Zerto Solution in your private cloud.
  * Provide your own licenses for Zerto Solution when the private cloud is the protected site. You can pair Zerto running on the site with your on-premises site licensing.



## Zerto disaster recovery architecture

![Zerto disaster recovery architecture.](https://docs.cloud.google.com/static/vmware-engine/images/zerto-dr-architecture.svg)

## Before you begin

To enable Zerto Virtual Replication from your on-premises environment to your private cloud, complete the following prerequisites:

  1. [Connect your on-premises network to your VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises).
  2. [Set up DNS lookup of your private cloud management components from your on-premises network to forward requests to your private Cloud DNS servers](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises). To enable forwarding of DNS lookup, create a forwarding zone entry in your on-premises DNS server for `gve.goog` to private Cloud DNS servers.
  3. Set up DNS lookup for on-premises vCenter components to be forwarded to your on-premises DNS servers. The DNS servers must be reachable from your private cloud.
  4. Install a Microsoft Windows server on your private cloud.
  5. Install Zerto Virtual Manager (ZVM) on the Windows server.
  6. Identify a [solution user account](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-solution-user-accounts) to use with ZVM, and set a strong password for the solution user account.



### Optional configuration on your private cloud

  1. Create one or more resource pools on your private cloud vCenter to use as target resource pools for VMs from your on-premises environment.
  2. Create one or more folders on your private cloud vCenter to use as target folders for VMs from your on-premises environment.
  3. [Create subnets](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vlan-subnet) on your private cloud for your failover network and set up required firewall rules.



## Deploy a disaster recovery solution using Zerto in your private cloud

Follow the [Zerto documentation](https://help.zerto.com/) for deploying the Zerto Virtual Replication solution on your private cloud. The private cloud can be a protected site or a recovery site of your Zerto Solution.

### Set up workload automation on Zerto Virtual Manager of your private cloud

The following sections describe the required and optional workload automation settings on Zerto Virtual Manager of your private cloud. These settings must be enabled to ensure Zerto Virtual Replication Appliance is gracefully managed during the node addition and host maintenance of nodes of your private cloud.

  1. In the Zerto Virtual Replication interface, under **Site Settings** , select **Workload Automation**.
  2. Select **Enable VRA auto evacuation once entering maintenance mode** option in **Host Maintenance Mode** section. This option is required to gracefully evacuate VRA during a failed node replacement, private cloud node removal and upgrades or patching of your private cloud.
  3. Optionally select : **Enable VRA auto installation once host is added to cluster** option in **VRA Deployment** section. Enabling this option allows Zerto Virtual Replication to deploy a Zerto Virtual Replication Appliance when you expand your private cloud cluster.



## What's next

  * Read the [Zerto documentation](https://help.zerto.com/).
  * [Learn about high availability for VMware virtual machines](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
