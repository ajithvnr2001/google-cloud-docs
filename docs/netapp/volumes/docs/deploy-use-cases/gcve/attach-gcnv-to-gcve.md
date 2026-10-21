---
url: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-gcnv-to-gcve/
title: Attach Google Cloud NetApp Volumes to Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:37.965688+00:00
---

# Attach Google Cloud NetApp Volumes to Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-gcnv-to-gcve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Attach Google Cloud NetApp Volumes to Google Cloud VMware Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to attach Google Cloud NetApp Volumes to Google Cloud VMware Engine.

You can attach NetApp Volumes to VMware Engine in two ways:

  * **As a vSphere datastore** : Attach the NetApp Volumes NFS or iSCSI volume to the VMware Engine private cloud as an external datastore.

  * **Using the guest operating system** : Attach or mount the NetApp Volumes NFS or iSCSI volume directly from the guest operating system in a workload VM on the VMware Engine private cloud.




Both methods require a network connection between the VMware Engine network (VEN) and the NetApp Volumes service network. Additionally, the NetApp Volumes volume and the VMware Engine private cloud must reside in the same Google Cloud region.

## Before you begin

Before you attach NetApp Volumes to VMware Engine, you must meet the following requirements:

  * Create a NetApp Volumes storage pool in the same region as your VMware Engine private cloud.

  * Create a VMware Engine private cloud in that region.




## Required settings for VMware Engine datastores

When you create a NetApp Volumes NFS or iSCSI volume for a VMware Engine datastore, enable the **Block volume from deletion when clients are connected** restriction to prevent accidental deletion of the volume. You can enable this setting in the Google Cloud console when you create a volume in a NetApp Volumes storage pool.

## Establish network connectivity

Create a peering connection between VMware Engine and NetApp Volumes before you use NetApp Volumes volumes with VMware Engine.

You can create a peering connection using a standard or a legacy VMware Engine network:

  * For a standard VMware Engine network (VEN), follow the instructions in [Create a peering connection](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-connect-workload-vm-to-netapp-volumes#create_a_peering_connection).

  * For a legacy VMware Engine network (VEN), follow the instructions in [Create a peering connection for legacy networks](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-connect-workload-vm-to-netapp-volumes#create_a_peering_connection_for_legacy_networks).




Verify that the peering connection is active before you continue. Routes to VMware Engine nodes might take up to 20 minutes to appear after activation.

## What's next

  * [Attach NFS volumes to Google Cloud VMware Engine as NFS datastores](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-nfs-volumes-to-gcve).

  * [Attach iSCSI volumes to Google Cloud VMware Engine as VMFS datastores](https://docs.cloud.google.com/netapp/volumes/docs/deploy-use-cases/gcve/attach-iscsi-volumes-to-gcve).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
