---
url: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-nfs-volumes-to-gcve/
title: Attach NFS volumes to Google Cloud VMware Engine as NFS datastores \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:01.861108+00:00
---

# Attach NFS volumes to Google Cloud VMware Engine as NFS datastores  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-nfs-volumes-to-gcve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Attach NFS volumes to Google Cloud VMware Engine as NFS datastores Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to attach NetApp Volumes NFS volumes as external NFS datastores to a VMware Engine private cloud environment. This approach is suitable for setting up external NFS datastores for Tier-2 and Tier-3 workloads, backups, and archival storage that don't require virtual storage area network (vSAN) performance.

## Before you begin

Before you attach a NetApp Volumes NFS volume as a VMware Engine NFS datastore, you must meet the following requirements:

  * **Protocol** : Use NFSv3 only. VMware Engine doesn't support NFSv4.1 for external datastores.

  * **Supported service levels** : Flex Unified, Standard, Premium, and Extreme.

  * **Service subnet** : Configure a dedicated `/26` or larger CIDR block for NFS traffic between ESXi hosts and NetApp Volumes. Use this subnet exclusively for NFS datastores. A single service subnet can be used by multiple NFS datastores.

  * **Export policy** : Configure the export policy to allow the service subnet CIDR with **Read & write** access and **Root access**.




## Configure a service subnet for NFS

Use the following instructions to configure a service subnet for NFS:

  1. Go to the **VMware Engine** page in the Google Cloud console.

[Go to VMware Engine](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Subnets**.

  3. Locate the free service subnet, and then click the **Edit** icon (edit) in the **Actions** column.

  4. In the **Edit subnet** panel, enter an IPv4 CIDR in the **IP address range** field.

  5. Click **Save**.

  6. Copy the following information from the service subnet:

     * **IP address range**

     * **Gateway IP**

     * **VLAN ID**




## Create an NFS volume

Create an NFS volume to use as an NFS datastore. For instructions, see [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#create_a_volume).

To create the NFS volume:

  1. Click the **Protocol(s)** drop-down list, and select **NFSv3** as the protocol.

  2. Select the **Block volume from deletion when clients are connected** checkbox for volumes used as Google Cloud VMware Engine datastores.

**Caution:** This selection is permanent.
  3. Configure the export policy to allow the service subnet CIDR with **Read & write** access and **Root access**.

  4. Create the volume.

  5. Copy the IP address for the NFS volume.




## Create the NFS datastore

You can create and manage NFS datastores backed by NetApp Volumes volumes using the VMware Engine API, Google Cloud CLI, or Terraform.

For more information about creating an NFS datastore, see [Create an NFS datastore](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores#create-datastore) for VMware Engine API, Google Cloud CLI, or Terraform.

## Mount the NFS datastore

After creating a datastore, you must mount it to a vSphere cluster to make the datastore available to ESXi hosts. To mount an NFS datastore, use the Google Cloud CLI, API, or Terraform. For instructions to mount the NFS datastore, see [Mount a datastore](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores#mount-datastore).

After VMware Engine mounts the datastore, use vCenter to provision VMs on the external datastore.

## Limitations

The following limitations apply to NetApp Volumes datastores:

  * vStorage APIs for Array Integration (VAAI) copy offload isn't supported.



## What's next

  * [Attach iSCSI volumes to Google Cloud VMware Engine as VMFS datastores](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-iscsi-volumes-to-gcve).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
