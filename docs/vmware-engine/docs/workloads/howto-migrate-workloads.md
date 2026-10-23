---
url: https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads/
title: Migrating VMware VMs to your private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:00.774128+00:00
---

# Migrating VMware VMs to your private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrating VMware VMs to your private cloud

This document helps you design, implement, and validate a migration plan to migrate your VMware virtual machines (VMs) from a VMware environment in an on-premises data center, in another public cloud provider, or in a co-location site, to Google Cloud VMware Engine.

Read this document if you're considering the advantages of migrating and want to explore what migrating to Google Cloud might look like.

Google Cloud VMware Engine supports several options to migrate VMs from your source VMware environment:

  * Migrate VMs using VMware HCX.
  * Migrate VMs using backup and disaster recovery tools.
  * Migrate VMs using VMware PowerCLI.
  * Migrate ISOs and templates.
  * Migrate VMs using NSX Layer 2 VPN.



## Assess the source environment

To scope your migration, you must understand your current VMware environment. At the end of this migration task, you have an inventory of your VMware VMs.

To build the inventory of your VMware environment, we recommend that you use [ Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview).

### Assess your VMware on AWS environment

If your VMware environment is hosted on VMware Cloud on AWS continue reading, otherwise you can skip this section.

After assessing your VMware environment with StratoZone, we recommend that you refine your inventory. Consider the following about your VMware Cloud on AWS environment:

  * The AWS region.
  * The number and type of hosts, and their specifications.
  * VMware Cloud on AWS clusters and resource pools.
  * How you configured the VMware vSAN Storage, and if you're using any storage offload options to other AWS services, such as Amazon S3.
  * The VMware vSphere version.
  * If you're using VMware Hybrid Linked Mode, and how you configured the connection between your VMware Cloud on AWS environment and the other environments that you're monitoring using VMware Hybrid Linked mode.
  * If you're using AWS Backup to back up your VMware Cloud on AWS resources.
  * If you moved your own IP addresses to VMware Cloud on AWS.
  * If you're running enterprise workloads in your VMware Cloud on an AWS environment, such as Oracle® Real Application Clusters or Microsoft SharePoint.
  * How you manage identities and access to your VMware Cloud on AWS environment.
  * How you prepared your VMware Cloud on AWS environment for disaster recovery.
  * Any VMware Cloud on AWS subscriptions and discounts.



If you choose to migrate your VMs from your VMware Cloud on AWS environment to your private cloud, using VMware HCX, we also recommend that you:

  * Check that you are running the most recent version of VMware HCX.
  * Ensure that your VMware Cloud on AWS environment meets the requirements listed in the [VMware HCX checklist](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/com.vmware.vmc-aws-operations/GUID-DAE9B318-294A-4422-BBF4-82AE9DDFF043.html).



For more information about how to assess your source environment for a migration to Google Cloud, see [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads).

## Before you begin

Migrating VMs and data from your VMware environment requires network connectivity from the data center to your private cloud environment. Before migrating workloads, we recommend that you:

  1. Set up a site-to-site VPN connection between your VMware environment and your private cloud.
  2. Ensure that DNS records resolve across both the source environment and your private cloud.
  3. Ensure that network routes between the source environment and your private cloud are correctly configured.



The network path from your VMware environment to your private cloud must support migrating VMs with vMotion. Also, the vMotion network on your vCenter must have routing abilities. Verify that your firewall allows all vMotion traffic between your vCenter and private cloud vCenter. On the private cloud, routing on the vMotion network is configured by default.

## Migrate VMs using HCX

You can use VMware HCX to migrate VMs from your VMware environment to Google Cloud VMware Engine. VMware HCX abstracts vSphere-based resources in your VMware environment and cloud resources and presents them to applications as one continuous resource, creating a hybrid infrastructure.

To avoid unnecessary fragmentation and diminished network performance when transferring data across the site-to-site VPN, we recommend that you configure the maximum transmission unit (MTU) to account for the VPN protocol overhead when migrating VMs using VMware HCX. For example, you may need to configure the MTU to a lower value to accommodate the VPN protocol overhead in each transmission unit.

For information about how to use VMware HCX to migrate VMs from your VMware environment environment to your private cloud, see [Migrating VMware VMs using VMware HCX](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx).

## Migrate VMs using backup and disaster recovery tools

You can migrate VMs to private clouds using backup and restore tools and disaster recovery tools. When you restore from backups that are created using Google [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery) or a third- party tool, use the private cloud as a target. You can also use the private cloud as a target for disaster recovery using Google [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery), the tool of your choice, such as HCX, a tool from Broadcom by VMware that's included with VMware Engine, or by using [Live Recovery](https://www.vmware.com/products/cloud-infrastructure/live-recovery) (formerly Site Recovery Manager or SRM) by following the steps in [Configuring disaster recovery using VMware Live Site Recovery](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm).

## Migrate VMs using PowerCLI

To migrate VMs from the VMware environment vCenter to the private cloud vCenter, use VMware PowerCLI or the Cross vCenter Workload Migration Utility available from VMware Labs. The following sample script shows the PowerCLI migration commands.
    
    
    $sourceVC = Connect-VIServer -Server <source-vCenter name> -User <source-vCenter user name> -Password <source-vCenter user password>
    $targetVC = Connect-VIServer -Server <target-vCenter name> -User <target-vCenter user name> -Password <target-vCenter user password>
    $vmhost = <name of ESXi host on destination>
    $vm = Get-VM -Server $sourceVC <name of VM>
    Move-VM -VM $vm -VMotionPriority High -Destination (Get-VMhost -Server $targetVC -Name $vmhost) -Datastore (Get-Datastore -Server $targetVC -Name <name of tgt vc datastore>)
    

**Note:** To use the names of the destination vCenter server and ESXi hosts, configure DNS forwarding from your VMware environment to your private cloud. Ensure that port 902 is open on the management network in the private cloud and on any firewall protecting your VMware environment. This port is used by cold migration.

## Migrate ISOs and templates

To create new VMs on your private cloud, use ISOs and VM templates. To upload the ISOs and templates to your private cloud and make them available, complete the following steps:

  1. Upload the ISO to your private cloud vCenter by using the vCenter UI.
  2. [Publish a content library](https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-2A0F1C13-7336-45CE-B211-610D39A6E1F4.html) on your private cloud vCenter: 
     * Publish your VMware environment content library.
     * Create a new content library on the private cloud vCenter.
     * Subscribe to the published VMware environment content library.
     * Synchronize the content library for access to the subscribed published on- premises content library.



## Migrate VMs using an NSX Layer 2 VPN

This option enables the live migration of workloads from your VMware environment to the private cloud. With this stretched Layer 2 network, the subnet from the VMware environment is available on the private cloud. After migration, new IP address assignment isn't required for the VMs.

For information about how to use a Layer 2 VPN to stretch a Layer 2 network from your VMware environment to your private cloud, see [Migrate workloads using Layer 2 stretched networks](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vpn-layer2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
