---
url: https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview/
title: ONTAP-mode overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:26.981877+00:00
---

# ONTAP-mode overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  ONTAP-mode overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the ONTAP-mode for Google Cloud NetApp Volumes.

## About ONTAP-mode

The Flex Unified service level offers a storage pool deployment mode, called ONTAP-mode, that lets you use the pool as an ONTAP system.

In ONTAP-mode, you manage the storage pool as you manage an ONTAP storage system. You must be familiar with ONTAP concepts, administration, and operations to use its features effectively. For more information, see the [ONTAP 9 documentation](https://docs.netapp.com/us-en/ontap/) about configuring resources and features. Additional information and training courses are available. If you are new to ONTAP-based storage management, consider using Flex Unified Default-mode instead.

### Capacity and billing

In ONTAP-mode, you provision storage pools with a specific capacity, throughput, and IOPS. You're billed for the logical capacity that you provision for the storage pool, rather than the amount of capacity that you actually use.

For example, suppose that you provision a 10 TiB storage pool and store 5 TiB of data. In this scenario, capacity and billing work as follows:

  * You have 5 TiB of remaining capacity available for additional data.

  * You're billed for the full 10 TiB of provisioned pool capacity.




### Deployment and architecture

You can deploy an ONTAP-mode storage pool using the Google Cloud console, Google Cloud CLI, Terraform, or Google APIs. A NetApp Volumes Flex Unified ONTAP-mode storage pool corresponds to an ONTAP cluster.

The deployment includes:

  * An ONTAP [cluster](https://docs.netapp.com/us-en/ontap/concepts/cluster-storage-concept.html) with one active-passive high availability (HA) pair

  * A data [aggregate](https://docs.netapp.com/us-en/ontap/disks-aggregates/index.html)

  * A [storage virtual machine (SVM)](https://docs.netapp.com/us-en/ontap/concepts/storage-virtualization-concept.html) with a root volume

  * All necessary [logical interfaces (LIFs)](https://docs.netapp.com/us-en/ontap/networking/configure_lifs_cluster_administrators_only_overview.html) are configured for network access in an IPspace called `Gcnv` as follows:

    * One IP address for each LIF

    * One highly available NAS LIF

    * Two SAN LIFs, one on each node

    * Two intercluster LIFs, one on each node

  * A running NFS server with no volumes exported




For large capacity pools, the service deploys six active-passive HA-pairs to manage [FlexGroups](https://docs.netapp.com/us-en/ontap/flexgroup/definition-concept.html) with one SVM. Each HA-pair has one data aggregate and five LIFs.

### Managed service aspects

NetApp Volumes is a managed service. The service provider manages the virtual infrastructure for your Flex Unified ONTAP-mode system. You can't directly manage the hardware components of your storage pool, such as nodes, aggregates, or network interfaces. The service automatically performs ONTAP upgrades.

Increasing the pool's capacity might trigger an upgrade of the underlying virtual machines (VMs) to provide additional CPU and RAM for better performance. These upgrades might result in brief I/O pauses.

### Storage pool configuration and management

When deploying the pool, you define the following:

  * The Google project that owns the pool.

  * The Google zone where the pool is deployed. For regional pools, you can specify a replica zone. A regional pool corresponds to a stretched MetroCluster.

  * The network (VPC) the pool is connected to using private service access.

  * The capacity and throughput and IOPS capabilities of the pool.

  * A CMEK policy to use if you want to encrypt your data with customer-managed encryption keys instead of Google-owned and Google-managed encryption keys.

  * Auto-tiering settings.




After creating the pool, you can increase its capacity or change its performance, which updates the underlying aggregate as needed. For regional pools, you can trigger a zone switch to initiate a switchover to the replica zone and a subsequent switchback.

### ONTAP-level operations

You must perform any actions beyond storage pool management at the ONTAP level. These actions include:

  * Creating and managing volumes.

  * Creating and managing shares and export policies.

  * Creating and managing snapshots.

  * Creating and managing replications.

  * Changing SVM, volume, protocol, and share settings.

  * Managing value-added features that are available in ONTAP-mode but not in Default-mode.


**Note:** If you aren't familiar with managing ONTAP operations, the chatbot on the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/) page can help you identify what you need to do to meet your objectives. For example, you can ask, "How do I create a FlexCache volume in NetApp Volumes?" A storage pool is a managed resource that already provides nodes, aggregates, interfaces, and an SVM. Ignore any instructions that direct you to create these resources and instead use the resources provided by NetApp Volumes.

### Feature management overview

The following table provides an overview of the features that you control by using the Google Cloud NetApp Volumes API or the ONTAP API for a storage pool with ONTAP-mode enabled:

Feature | Google Cloud NetApp Volumes APIs  
  
(Google Cloud console, Google Cloud CLI, Terraform) | ONTAP REST API  
---|---|---  
Storage pool | Yes | No  
Volume | No | Yes  
Snapshot | No | Yes  
Backup (includes Backup Policy, Backup Vault) | Yes | No  
CMEK | Yes | No  
Auto-tiering (pool settings) | Yes | No  
Auto-tiering (per volume settings) | No | Yes  
Active Directory | No | Yes  
HostGroup (initiator group) | No | Yes  
Volume replication | No | Yes  
Volume migration | No | Yes  
External replication | No | Yes  
Consistency groups | No | Yes  
NVMe/TCP | No | Yes  
  
## Backup considerations

While ONTAP-mode supports manual and scheduled backups, the Google Cloud console doesn't support the following operations related to backups:

  * Configuring scheduled backups (attaching a backup policy).

  * Restoring a backup to an ONTAP-mode volume.

  * Viewing volume-to-backup vault associations.




Because ONTAP-mode volumes aren't exposed in the Google Cloud console, you must perform these operations by using the API or Google Cloud CLI.

## What's next

[Manage ONTAP in ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
