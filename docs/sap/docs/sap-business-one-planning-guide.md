---
url: https://docs.cloud.google.com/sap/docs/sap-business-one-planning-guide/
title: SAP Business One planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:13.511241+00:00
---

# SAP Business One planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-business-one-planning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP Business One planning guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of how SAP Business One works with Google Cloud, and provides details that you can use when planning the implementation of a new SAP Business One system.

For more information about how to deploy SAP Business One on Google Cloud, see the [SAP Business One deployment guide](https://docs.cloud.google.com/sap/docs/sap-business-one-deployment-guide).

## About SAP Business One on Google Cloud

SAP supports Business One on Google Cloud with either SAP HANA or Microsoft SQL Server.

This guide, as well as the [SAP Business One Deployment Guide](https://docs.cloud.google.com/sap/docs/sap-business-one-deployment-guide), covers Business One with SAP HANA only.

SAP HANA is an in-memory, column-oriented, relational database that provides high-performance analytics and real-time data processing. SAP Business One is business management software designed for small and medium-sized enterprises.

You can leverage the ease of provisioning, high scalability, and redundant infrastructure capabilities of Google Cloud to run your business-critical SAP Business One workloads cost-effectively on SAP HANA. Google Cloud provides a set of physical assets, such as computers and hard disk drives, and virtual resources, such as Compute Engine virtual machines (VMs), located in Google data centers around the world.

When you deploy SAP Business One and SAP HANA on Google Cloud, you deploy them to a VM running on Compute Engine. Compute Engine VMs provide persistent disks, which function similarly to physical disks in a desktop or a server, but are automatically managed for you by Compute Engine to ensure data redundancy and optimized performance.

For information from SAP about SAP Business One for SAP HANA, see the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_BUSINESS_ONE_VERSION_FOR_SAP_HANA).

For information about the costs that are associated with running Business One on SAP HANA on Google Cloud, see the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#costs).

## Google Cloud basics

Google Cloud consists of many cloud-based services and products. When running SAP products on Google Cloud, you mainly use the IaaS-based services offered through [Compute Engine](https://docs.cloud.google.com/compute/docs) and [Cloud Storage](https://docs.cloud.google.com/storage/docs), as well as some platform-wide features, such as [tools](https://docs.cloud.google.com/docs/overview/developer-and-admin-tools).

See the [Google Cloud platform overview](https://docs.cloud.google.com/docs/overview) for important concepts and terminology. This guide duplicates some information from the overview for convenience and context.

For an overview of considerations that enterprise-scale organizations should take into account when running on Google Cloud, see the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).

### Interacting with Google Cloud

Google Cloud offers three main ways to interact with the platform, and your resources, in the cloud:

  * The Google Cloud console, which is a web-based user interface.
  * The `gcloud` command-line tool, which provides a superset of the functionality that Google Cloud console offers.
  * [Client libraries](https://docs.cloud.google.com/sdk/cloud-client-libraries), which provide APIs for accessing services and management of resources. Client libraries are useful when building your own tools.

**Important** : If you are using the gcloud CLI, then make sure that you are using the latest version. To install the latest version of the gcloud CLI, see the [gcloud install instructions.](https://cloud.google.com/sdk/downloads)

### Google Cloud services

SAP deployments typically utilize some or all of the following Google Cloud services:

Service | Description  
---|---  
[VPC networking](https://docs.cloud.google.com/compute/docs/networking) |  Connects your Compute Engine instances to each other and to the internet. Each compute instance is a member of either a legacy network with a single global IP range, or a recommended subnet network, where the instance is a member of a single subnetwork that is a member of a larger network. Note that a Virtual Private Cloud (VPC) network cannot span Google Cloud projects, but a Google Cloud project can have multiple VPC networks. To connect resources from multiple projects to a common VPC network, you can use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), so that the resources can communicate with each other securely and efficiently by using internal IP addresses from that network. For information about how to provision a Shared VPC including requirements, configuration steps, and usage, see [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).   
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) | Creates and manages compute instances with your choice of operating system and software stack.  
[Persistent Disk and Hyperdisk](https://docs.cloud.google.com/compute/docs/disks) |  You can use Persistent Disk and Google Cloud Hyperdisk:

  * Persistent Disk volumes are available as either standard hard disk drives (HDD) or solid-state drives (SSD). For Balanced Persistent Disk and SSD Persistent Disk volumes, [PD Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) provides asynchronous replication of SAP data between two Google Cloud regions.
  * Hyperdisk Extreme volumes provide higher maximum IOPS and throughput options than SSD Persistent Disk volumes.
  * Compute Engine enables [default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption), including content inside Persistent Disk and Hyperdisk volumes. For more information about disk encryption and possible encryption options, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

  
[Google Cloud console](https://console.cloud.google.com/) |  A browser-based tool for managing Compute Engine resources. Use a template to describe all of the Compute Engine resources and instances you need. You don't have to individually create and configure the resources or figure out dependencies because the Google Cloud console does that for you.  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) | You can store your SAP database backups in Cloud Storage for added durability and reliability, with replication.  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) |  Provides visibility into the deployment, performance, uptime, and health of Compute Engine, network, and persistent storage disks. Monitoring collects metrics, events, and metadata from Google Cloud and uses these to generate insights through dashboards, charts, and alerts. You can monitor the compute metrics at no cost through Monitoring.  
[IAM](https://docs.cloud.google.com/iam/docs) |  Provides unified control over permissions for Google Cloud resources. IAM lets you control who can perform control-plane operations on your compute instances, including creating, modifying, and deleting instances and persistent storage disks, and creating and modifying networks.  
  
### Pricing and quotas

You can use the [pricing calculator](https://cloud.google.com/products/calculator/) to estimate your usage costs. For more pricing information, see [Compute Engine pricing](https://cloud.google.com/compute/pricing), [Cloud Storage pricing](https://cloud.google.com/storage/pricing), and [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

Google Cloud resources are subject to quotas. If you plan to use high-CPU or high-memory machines, then you might need to request additional quota. For more information, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

## Software versions supported by SAP on Google Cloud

SAP Business One 10.0 for SAP HANA is supported by SAP on Google Cloud with the following software versions:

  * SAP HANA 2.0
  * SUSE Linux Enterprise Server (SLES) 15 and later service packs (x86_64)



SAP Business One 9.3 for SAP HANA is supported by SAP on Google Cloud with the following software versions:

  * SAP HANA 1.0
  * SLES 12 SP3



## Resource requirements

### VM types

The following Compute Engine VM types are officially supported by SAP for production use of SAP Business One on Google Cloud.

Google Cloud Instance Type | vCPU | Memory (GiB) | CPU Platform  
---|---|---|---  
n2-highmem-8 | 8 | 64 | Intel Cascade Lake  
n2-highmem-16 | 16 | 128 | Intel Cascade Lake  
n2-highmem-32 | 32 | 256 | Intel Cascade Lake  
n2-highmem-64 | 64 | 512 | Intel Cascade Lake  
n1-highmem-32 | 32 | 208 | Intel Broadwell  
n1-highmem-64 | 64 | 416 | Intel Broadwell  
  
For a list of the Compute Engine VM instance types that SAP certifies, see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#certified_vms_for_sap_hana).

The operating system you choose must be compatible with the version of SAP Business One you plan to install. For more information see the [SAP product availability matrix](https://apps.support.sap.com/sap/support/pam). For more information about different instance types and their use cases, see the [machine types](https://docs.cloud.google.com/compute/docs/machine-types) documentation.

### Storage configuration

SAP HANA is an in-memory database, so data is mostly stored and processed in memory. Protection against data loss is provided by saving the data to a persistent storage location.

Compute Engine SSD-based persistent disks serve as the block storage on the [Compute Engine VM types](https://docs.cloud.google.com/sap/docs/sap-business-one-planning-guide#vm_types) that are certified for Business One on SAP HANA. On a VM with 32 or more vCPUs, an 834 GB SSD persistent disk can achieve up to 400 MB/sec for writes, and 400 MB/sec for reads, which meets the minimum performance requirements for the `/hana/data` and `/hana/log` volumes.

The default storage configuration for SAP HANA backup uses standard HDD persistent disks. Standard HDD persistent disks are efficient and economical for handling sequential read-write operations, but are not optimized to handle high rates of random input-output operations per second (IOPS). SAP HANA uses sequential I/O with large blocks to back up the database. Standard HDD persistent disks provide a low-cost, high-performance option for this scenario.

The SAP HANA backup volume size is designed to provide optimal baseline and burst throughput as well as the ability to hold several backup sets. Holding multiple backup sets in the backup volume makes it easier to recover your database if necessary.

You can also use other backup solutions for SAP HANA, including the Backint feature of Google Cloud's Agent for SAP, which lets you store SAP HANA backups directly in Cloud Storage.

For more information about backing up SAP HANA, see [Backup and recovery](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).

### Memory configuration

The memory configuration of your Compute Engine VM differs depending on the instance type that you choose. To see the memory configurations that you can choose from see [Certified Compute Engine VMs for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#certified_vms_for_sap_hana).

### Operating systems

Business One 10.0 is supported by SAP on the following operating systems:

  * SLES 15 SP1
  * SLES 15 SP1 for SAP



Business One 9.3 is supported by SAP on SLES 12 SP3.

  * SLES 12 SP3
  * SLES 12 SP3 for SAP



## Licensing

Running SAP Business One and SAP HANA on Google Cloud requires you to bring your own license (BYOL). For more information about SAP licensing, contact SAP.

You can install Business One and apply your existing license to the instance before the grace period ends.

## Deployment architecture

![SAP Business One on Google Cloud deployment architecture](https://docs.cloud.google.com/static/solutions/images/sap-business-one-architecture.svg)

You deploy SAP Business One using a single-node architecture that has the following components:

  * One Compute Engine VM instance, with an SSD-based persistent disk that meets SAP HANA performance requirements, and a network bandwidth of up to 16 Gbps. The SSD-based persistent disk is partitioned and mounted to `/hana/data` to host the data. You install both the SAP HANA database and the SAP Business One Server on this single VM. For more information about the persistent disk options for SAP HANA, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage).

  * VPC firewall rules restricting access to instances.

  * Optionally, a Persistent Disk volume for backups of the SAP HANA database. If you use the Backint feature of Google Cloud's Agent for SAP, then you don't require a Persistent Disk volume for backups.

  * Automated SAP HANA database installation with a configuration file that you create.

  * An optional Compute Engine VM as a bastion host.

  * An optional, but recommended, subnetwork with a custom topology and IP ranges in the Google Cloud region of your choice. The SAP HANA database and the other Compute Engine instances are launched within this subnetwork. You can use an existing subnetwork for SAP HANA.

  * An optional, but recommended, Internet gateway configured for outbound Internet access for your SAP HANA and other instances. This guide assumes you are using this gateway.

  * An optional Compute Engine VM for SAP HANA Studio. This is an optional step that isn't discussed in these SAP Business One guides. To learn more, see the [SAP Hana deployment guide](https://docs.cloud.google.com/sap/docs/sap-hana-deployment-guide).

  * An optional Compute Engine VM for SAP Business One Client, for administration.




The deployment uses an optional NAT bastion host for accessing SAP HANA, so that an external IP is not exposed. The bastion host is deployed in the same subnetwork as the SAP Business One Server instance.

You can use Cloud Storage to back up your local backups available in `/hanabackup`. This mount should be sized equal to or greater than the data mount.

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



## What's next

For information specific to deployment, see the [SAP Business One deployment guide](https://docs.cloud.google.com/sap/docs/sap-business-one-deployment-guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
