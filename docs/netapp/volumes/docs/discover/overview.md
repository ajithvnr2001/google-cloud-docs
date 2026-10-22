---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/overview/
title: Google Cloud NetApp Volumes overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:43.814791+00:00
---

# Google Cloud NetApp Volumes overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Google Cloud NetApp Volumes overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Google Cloud NetApp Volumes and how it works.

## About NetApp Volumes

NetApp Volumes is a fully managed, cloud-based data storage service that provides advanced data management capabilities and highly scalable performance.

NetApp Volumes helps to accelerate deployment times, manage your workloads and applications, and migrate workloads to the cloud while keeping the performance and features of on-premises storage.

NetApp Volumes lets you move file and block based applications to Google Cloud. It has support for Network File System (NFSv3, NFSv4.1, and NFSv4.2), Server Message Block (SMB), Internet Small Computer Systems Interface (iSCSI), and NVMe/TCP protocols built-in, so you don't need to re-architect your applications and can continue to get persistent storage for your applications.

NetApp Volumes offers multiple service levels which vary in price, performance, features, and capabilities.

## Key features

NetApp Volumes offers the following [features](https://docs.cloud.google.com/netapp/volumes/docs/discover/features). For a comparison of features across service levels, see [service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

  * **Fully-managed service** : provides a fully-managed service with no operations, integrated with the [Google Cloud console](https://console.cloud.google.com/).

  * **Volume provisioning** : provisions volumes from 1 GiB to 3 PiB in seconds.

  * **Multiprotocol support** : supports NFSv3, NFSv4.1, NFSv4.2, SMB 2.1, 3.0, and 3.1.1, iSCSI, NVMe/TCP, and S3 multiprotocol (ONTAP-mode only) protocols.

  * **Automated snapshots** : protects data with automated, efficient snapshots.

  * **Auto-tiering** : moves infrequently used data transparently to affordable cold storage.

  * **Backup** : provides manual and automated backups for long-term retention.

  * **Volume replication** : enables business continuity with asynchronous volume replication across Google Cloud.

  * **FlexCache** : allows fan-out caching of remote ONTAP volumes to accelerate access.

  * **High availability** : provides high availability with options for multi-region redundancy, backed by the [NetApp Volumes service level agreement](https://cloud.google.com/netapp/volumes/sla).

  * **Rapid cloning** : accelerates application development with rapid cloning.

  * **Multiple service level offerings** : offers multiple service levels based on location, allowing you to pick a service level that best fits your needs. For a comparison of features across service levels, see [service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

    * **Flex Unified** : highly available, general purpose storage with advanced data management capabilities.

      * **Performance** : independent provisioning of capacity and performance with zonal pools in selected regions. You can provision throughput from 64 MiBps to a maximum of 5 GiBps in increments of 1 MiBps. Each MiBps provisioned throughput includes 16 IOPS. Additional IOPS beyond the included throughput of 16 IOPS can be provisioned as required up to a maximum of 160,000 IOPS. Large capacity pools offer up to 22 GiBps of throughput and 750,000 IOPS.
**Note:** For regions with limited performance, the peak performance of a storage pool is capped. In these regions, you can provision throughput from 64 MiBps to a maximum of 1.6 GiBps in increments of 1 MiBps. Each MiBps of provisioned throughput includes 16 IOPS. You can provision additional IOPS beyond the included throughput of 16 IOPS as required up to a maximum of 90,000 IOPS. Target workloads include file shares, disaster recovery targets, and Kubernetes workloads. Large capacity pools aren't supported in regions with limited performance. For more information about limited performance regions, see [Supported regions for Flex Unified limited performance](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels#supported_regions_for_flex_unified_limited_performance).
      * **Sample use cases** : suitable for all workloads, with flexible capacity and performance scaling, and zonal and regional availability.

The Flex Unified service level offers [two operational modes](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#flex_unified_default-mode_versus_ontap-mode):

      * **Default-mode** : designed for users who want a fully managed volume experience. The Flex Unified Default-mode service level operates completely within Google data centers, using only Google Cloud compute and storage resources.

      * **ONTAP-mode** : designed for users who understand the management of ONTAP-based storage systems and want to use ONTAP's extensive capabilities. The Flex Unified ONTAP-mode service level operates completely within Google data centers, using only Google Cloud compute and storage resources.

    * **Standard** : highly available, general purpose storage with advanced data management capabilities.

      * **Performance** : up to 16 KiBps per GiB of volume capacity. Maximum of 1.6 GiBps per volume.

      * **Sample use cases** : common enterprise workloads such as Network File System (NFS) and Server Message Block (SMB) file shares, SAP shared files, and Google Cloud VMware Engine.

    * **Premium** : highly available, high-performance storage with advanced data management capabilities.

      * **Performance** : up to 64 KiBps per GiB exclusive to volume. Maximum of 4.5 GiBps per volume. 30 GiBps with large capacity volumes.

      * **Sample use cases** : performance-critical workloads requiring low latency, for example, Windows and enterprise NFS, self-managed databases and file shares, virtual desktop infrastructure (VDI), and VMware Engine.

    * **Extreme** : highly available, high-throughput storage with advanced data management capabilities.

      * **Performance** : up to 128 KiBps per GiB exclusive to volume. Maximum of 4.5 GiBps per volume. 30 GiBps with large capacity volumes.

      * **Sample use cases** : performance-critical workloads requiring high throughput and low latency, for example, Windows and enterprise NFS, self-managed databases and file shares, VDI, and VMware Engine.

    * **Flex File** : highly available, general purpose storage with advanced data management capabilities. The Flex File service level operates completely within Google data centers, using only Google Cloud compute and storage resources.

**Important:** Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. For more information, see [Migration to Flex Unified service level](https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified).
      * **Performance** :

        * **Regular pools** : up to 16 KiBps per GiB of storage pool capacity shared by all volumes in the pool in [selected regions](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels#supported_regions). Maximum of 1.6 GiBps per pool.

        * **Custom performance pools** : independent provisioning of capacity and performance with zonal pools in selected regions. You can provision throughput from 64 MiBps to a maximum of 5 GiBps in increments of 1 MiBps. Each MiBps provisioned throughput includes 16 IOPS. Additional IOPS beyond the included throughput of 16 IOPS can be provisioned as required up to a maximum of 160,000 IOPS.

      * **Sample use cases** : common enterprise workloads such as Network File System (NFS) and Server Message Block (SMB) file shares.




## How it works

NetApp Volumes provides fully managed NFS and SMB remote file systems, and iSCSI volumes as a service. Service administrators create and manage these remote file systems as volumes and share them with NFS and SMB clients over a network, or create iSCSI volumes and attach them to Linux and Windows iSCSI clients. Clients such as Compute Engine VMs mount file system volumes, their users, and the applications within the client store files in the file system volumes. You can control access using Windows or UNIX-based permission models.

The iSCSI Linux and Windows Compute Engine VMs can consume iSCSI volumes as raw block devices, or they can choose to create the supported Linux or Windows file systems and configure applications that support block storage.

## Tools to use NetApp Volumes

You can use Google Cloud NetApp Volumes using the following tools:

  * **Google Cloud SDK** : the [Google Cloud command line interface](https://docs.cloud.google.com/sdk/gcloud) lets you interact with NetApp Volumes through a terminal

  * **Google Cloud console** : the [Google Cloud console](https://console.cloud.google.com/) provides a visual interface that gives you a holistic view of your applications and projects

  * **Terraform Google Cloud Platform Provider** : NetApp Volumes resources are part of the Google [Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs). For more information about how to provision NetApp Volumes resources using Terraform, see introduction to [Terraform integration](https://community.netapp.com/t5/Tech-ONTAP-Blogs/Google-Cloud-NetApp-Volumes-Terraform-integration/ba-p/450777).




## NetApp Volumes architecture

NetApp Volumes uses the [Google Cloud Private Service Access framework](https://docs.cloud.google.com/vpc/docs/private-services-access), which creates a private connection linking your Virtual Private Cloud (VPC) to the NetApp Volumes VPC. The Google Cloud private service access framework assigns private addresses (RFC 1918) or non-private addresses (non-RFC 1918) to it using the Service Networking API and VPC peering constructs.

### Network peering

To create volumes in storage pools, you must set up private service access. You can set up private service access manually using Google Cloud console, Google Cloud CLI, or Terraform. The storage pool creation workflow also integrates private service access setup. All volumes in a pool are accessible from Network-attached storage (NAS) clients on the same VPC, but are subject to NAS access control. For Shared VPC, this enables data access across different projects. You can't attach a single volume or pool to multiple VPCs.

Independent of data access at the VPC level, all resources belong only to the project they're created in and can only be managed within that project [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) protects management access.

## Region availability

NetApp Volumes is available in several regions. For details about region availability, see [NetApp Volumes locations](https://docs.cloud.google.com/netapp/volumes/docs/locations).

## What's next

Read about [features](https://docs.cloud.google.com/netapp/volumes/docs/discover/features) of Google Cloud NetApp Volumes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
