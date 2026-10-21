---
url: https://docs.cloud.google.com/sap/docs/architectures/sap-s4hana-on-gcp/
title: Reference architecture: SAP S/4HANA on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:47.152092+00:00
---

# Reference architecture: SAP S/4HANA on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/sap-s4hana-on-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Reference architecture: SAP S/4HANA on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This reference architecture is intended for people who are evaluating Google Cloud as a platform for deploying SAP S/4HANA workloads. It includes considerations during the planning phase, deployment models and automation, and common operational procedures like backup and DR tasks. 

Google Cloud provides cost-effective, reliable, secure, and high-performance SAP-certified infrastructure for running SAP S/4HANA on SAP HANA. For a complete list of supported SAP solutions on Google Cloud, see [SAP on Google Cloud](https://docs.cloud.google.com/solutions/sap).

## Architecture

The following diagrams show a high-level view of three common deployment models for SAP S/4HANA: centralized, distributed, and distributed with high availability.

### Centralized deployment

In a centralized deployment, you can install SAP S/4HANA and the SAP HANA database on the same Compute Engine instance. We recommend this approach for non-production environments such as sandbox and development environments.

The following diagram shows a reference architecture for SAP S/4HANA on SAP HANA in a centralized deployment. Note that SAP ASCS, PAS, WD, and the SAP HANA database are all installed on the same compute instance. 

![Architecture diagram for SAP S/4HANA on Google Cloud in a centralized deployment.](https://docs.cloud.google.com/static/sap/docs/images/s4hana-centralized-deployment.svg)

### Distributed deployment

In a distributed deployment, you can install the different components on different Compute Engine instances. We recommend this approach for production environments or environments that require a lot of compute power to handle heavy transaction loads.

The following diagram shows a reference architecture for SAP S/4HANA in a distributed deployment. Note that SAP ASCS, PAS, WD, and SAP HANA are all installed on different compute instances. 

![Architecture diagram for SAP S/4HANA on Google Cloud in a distributed deployment.](https://docs.cloud.google.com/static/sap/docs/images/s4hana-distributed-deployment.svg)

### Distributed deployment with high availability

In a distributed deployment with high availability, Linux clusters are set up across zones to help guard against component failures in a given region. You can deploy a Linux cluster across zones using either an active/passive configuration or an [active/active](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.03/en-US/fe5fc53706a34048bf4a3a93a5d7c866.html) configuration. In both cases, you start by setting up two Compute Engine compute instances in separate zones for maximum redundancy, each with its own SAP HANA database. The following diagram shows an SAP S/4HANA architecture that uses a Linux cluster to achieve high availability on both the application and the SAP HANA database side: 

![Architecture diagram for SAP S/4HANA on Google Cloud in a distributed high-availability deployment.](https://docs.cloud.google.com/static/sap/docs/images/s4hana-distributed-ha-deployment.svg) The following diagrams show an SAP HANA database that is highly available during both normal operation and a takeover operation:

  * Normal operation:

![Architecture diagram for SAP HANA high-availability on Google Cloud during normal operation.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-normal-ops.svg)

  * Takeover operation:

![Architecture diagram for SAP HANA high-availability on Google Cloud during takeover operation.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-takeover-ops.svg)




To combine both high availability and disaster recovery for the database, you can use SAP HANA System Replication. The following diagram shows a combination of both to achieve maximum availability and fault tolerance:

![High-level architecture diagram for SAP S/4HANA on Google Cloud with high availability and disaster recovery.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-dr.svg)

The cluster managing the high availability includes the following functions and features:

  * Two host compute instances, each with an instance of SAP HANA.
  * Synchronous SAP HANA system replication.
  * The Pacemaker high-availability cluster resource manager.
  * A fencing mechanism that fences off the failed node.
  * Automatic restart of the failed instance as the new secondary instance . 



The architecture on the application side is similar. In this case, the cluster manages the ABAP SAP Central Services (ASCS) and the Enqueue Replication Server or Enqueue Replicator (ERS) that are used to provide the SAP S/4HANA system with high availability in case something happens to any of the ASCS and ERS instances.

Depending on the SAP S/4HANA version you use, the Enqueue Server and the Enqueue Replication Server / Enqueue Replicator run on a different version:

  * S/4HANA 1709 and earlier: ENSA1 and ERS.
  * S/4HANA 1809 or later: ENSA2 and ERS2.



The following diagram shows an SAP S/4HANA system using a Pacemaker cluster to limit the single points of failure from both the Message Server and the Enqueue Server:

![Architecture diagram for SAP NetWeaver, with a database, in a high-availability deployment on Google Cloud.](https://docs.cloud.google.com/static/sap/docs/images/sap-nw-ha.svg)

Details about the deployment of the high availability system and Linux clustering across zones are covered later in this document.

#### A note on load balancing

In a distributed SAP S/4HANA environment, load balancing is mandatory. You can configure application load balancing using a combination of the SAP application layer and Network Load Balancers. For more information, see [Internal passthrough Network Load Balancer VIP implementations](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide#vip_with_internal_tcp_udp_load_balancing_failover_support) section in the high-availability planning guide for SAP NetWeaver on Google Cloud.

## Deployment components

SAP S/4HANA consists of the following technical components:

  * SAP HANA database
  * ASCS: ABAP SAP Central Services 
    * Contains the Message Server and Enqueue Server, which are required in any SAP ABAP system.
    * Deployed either on their own VM instance in HA deployments or deployed on the VM instance hosting the PAS.
    * In HA deployments, the ASCS resources are managed by a Linux cluster resource manager such as Pacemaker.
  * ERS: Enqueue Replication Server or Enqueue Replicator 
    * Deployed in HA deployments to keep a replica of the lock table in case something happens to the ASCS instance.
    * Managed by a Linux cluster resource manager such as Pacemaker.
  * PAS: Primary Application Server 
    * The first or only application server for the SAP system.
  * AAS: Additional Application Server 
    * Usually deployed for application level load balancing. You can install multiple AAS instances to achieve higher availability from an application layer perspective as well. If one of the application servers goes down, then all user sessions connected to that application server are terminated, but users can sign in again to the other AAS in the environment.
  * SAP NetWeaver gateway 
    * Deployed either as a standalone system or as part of the SAP S/4HANA system.
    * Allows the system to connect devices, environments, and platforms to SAP systems using Open Data Protocol (OData).
  * SAP Fiori front-end server 
    * Deployed either as a standalone system or as part of the SAP S/4HANA system.
    * The SAP Netweaver ABAP system is used to host SAP Fiori applications.
  * WD: Web Dispatcher (optional) 
    * Intelligent software load balancer that distributes HTTP and HTTPS requests, based on application type, to PAS and AAS.



The following Google Cloud services are used in the SAP S/4HANA deployment:

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
[Filestore](https://docs.cloud.google.com/filestore/docs/overview) |  High-performance, fully managed NFS file storage from Google Cloud. For multi-zonal high-availability deployments, we recommend using Filestore Regional (formerly Enterprise) that has 99.99% availability SLA. For information about the Filestore service tiers, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).  
[NetApp Cloud Volumes ONTAP](https://cloud.netapp.com/ontap-cloud) |  A full-featured, smart storage solution that you deploy and manage yourself on a compute instance. For more information about NetApp Cloud Volumes ONTAP, see [Overview of Cloud Volumes ONTAP](https://docs.netapp.com/us-en/bluexp-cloud-volumes-ontap/task-getting-started-gcp.html).  
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) |  A fully managed NFS and SMB file storage solution from Google Cloud, powered by NetApp Cloud Volumes ONTAP. Depending on the region, there can be multiple service levels available to select from. For more information, see [Service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).  
  
## Design considerations

This section provides guidance to help you use this reference architecture to develop an architecture that meets your specific requirements for security, reliability, operational efficiency, cost, and performance.

### Networking

There are multiple ways to deploy an SAP S/4HANA system from the networking perspective and how you deploy your network has a significant impact on its availability, resilience, and performance. As mentioned earlier, a Virtual Private Cloud (VPC) is a secure, isolated private network hosted within Google Cloud. VPCs are global in Google Cloud, so a single VPC can span multiple regions without communicating across the internet.

A typical SAP deployment places the instances of HA systems in different zones in the same region to ensure resilience while providing low latency. Subnets can span multiple zones due to Google Cloud capabilities. These capabilities also simplify SAP clustering because the cluster's virtual IP (VIP) address can be in the same range as the instances of the HA systems. This configuration shields the floating IP by using an internal Application Load Balancer and is applicable to HA clustering of the application layer (ASCS and ERS) and the SAP HANA database layer (SAP HANA primary and secondary). 

There are multiple ways to build your network and connect your SAP S/4HANA system with your infrastructure:

  * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) connects two VPC networks so that resources in each network can communicate with each other. The VPC networks can be hosted in the same Google Cloud project, different projects of the same organization, or even different projects of different organizations. VPC Network Peering establishes a direct connection between two VPC networks, each one using their own subnets, enabling private communication between resources in the peered VPCs.

  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) is a feature in Google Cloud that lets an organization connect resources from multiple projects to a common VPC network. The systems using a Shared VPC can communicate efficiently and securely using internal IP addresses. You can centrally manage network resources such as subnets, routes, and firewalls in a host project, while delegating administrative responsibilities for creating and managing individual resources to service projects. This separation of concerns simplifies network administration and enforces consistent security policies across your organization.




For SAP systems, it is generally recommended to group resources by environment type. For example, production environments must not share computing resources with non-production environments so as to provide adequate isolation, but you can use a Shared VPC for a common layer of connectivity between your projects. You can also use independent VPCs and use VPC peering to connect projects.

While designing your network, start with a host project containing one or more Shared VPC networks. You can attach additional service projects to a host project, which allows the service projects to participate in the Shared VPC. Depending on your needs, you can deploy SAP S/4HANA on a single Shared VPC or multiple shared VPCs. The two scenarios differ in terms of network control, SAP environment isolation, and network inspection:

  * Scenario 1: Deploying SAP S/4HANA on a single Shared VPC. This simplifies the deployment and reduces administrative overhead at the expense of lower isolation between networks.
  * Scenario 2: Deploying SAP S/4HANA on multiple shared VPCs. This increases network isolation and adds security at the expense of increasing the complexity and the administrative overhead.



It is also possible to use a hybrid approach. For example, you can use one Shared VPC for the production environment and one Shared VPC for all non-production systems. For more information, see the "Networking" section in [General checklist for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/checklist-sap#checklist-section-1).

### Single points of failure

An SAP S/4HANA system has some common single points of failure that can impact the availability of the system:

  * SAP Central Services such as Message Server and Enqueue Server
  * SAP Application Server
  * SAP HANA database
  * SAP Web Dispatcher, if used as a frontend for HTTP/HTTPS access to the system
  * Shared storage such as NFS



There are multiple options for reducing the impact of such single points of failure, and these options involve deploying the system using high-availability solutions, replication services, or using other functionalities that protect the system from failures. When planning your SAP S/4HANA system we recommend that you study such single points of failure and plan accordingly. For an overview about the alternative solutions that you can use to manage single points of failure, see the following sections in this guide:

  * Availability and continuity
  * Deployment architecture for SAP HANA
  * Deployment architecture for SAP S/4HANA



### Availability and continuity

During the planning phase of implementing an SAP S/4HANA system, you need to specify the following data points for defining the system's availability and continuity:

  * **Service Level Objectives (SLO)** : A target value or range of values for a service level that is measured by a service level indicator (SLI). For example: performance, availability, and reliability.
  * **Service Level Indicators (SLI)** : Metrics, such as latency, that help in measuring the performance of a service. It is a carefully defined quantitative measure of some aspect of the level of service that is provided.
  * **Service Level Agreement (SLA)** : A service contract between two parties (provider, customer) that defines an agreement about the provided service in measurable terms called Service Level Objectives (SLOs).
  * **Recovery Time Objective (RTO)** : The maximum tolerable duration between a data-loss incident and its mitigation.
  * **Recovery Point Objective (RPO)** : The Recovery Point Objective (RPO) is the maximum amount of data that can be lost, measured in time, without causing significant harm. Practically, this translates to the point in time at which the state of the impacted data must be recovered following a data loss event.



Depending on the data points and the agreed values between all the stakeholders, the SAP S/4HANA system relies on capabilities such as high availability or disaster recovery:

  * **High Availability (HA)** : The capability of a system that supports the goal of business continuity while ensuring that data and services are available for users when needed. The usual way to achieve this capability is by enabling redundancy, including hardware redundancy, network redundancy, and data center redundancy.
  * **Disaster Recovery (DR)** : The capability of a system to be protected from unplanned outages through reliable and predictable recovery methods on a different hardware and/or physical location.



Both high availability and disaster recovery are compatible, but they cover different cases and situations. For example, an HA solution lets you continue with your operations if one of the elements of the system has an unplanned downtime or outage without causing any interruption for your users. The same can be said about a DR solution with the exception of experiencing an interruption from the moment the outage occurs until the DR solution starts the faulty elements of the system on a different location.

The ensuing sections provide an overview of the different options that you have when planning and deploying your SAP S/4HANA system on Google Cloud.

### Supported machine types for SAP S/4HANA

Google Cloud offers Compute Engine VM instance types that are certified by SAP to match sizing requirements when you're deploying SAP S/4HANA. For more information about sizing on Google Cloud and the machine types that are supported, see the following documents:

  * [ Supported machine types for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms)
  * [ Supported machine types for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types)



Custom machine types for SAP HANA on Google Cloud are also certified by SAP. You can run SAP HANA instances with less than 64 vCPUs as long as you maintain a vCPU-to-Memory ratio of at least 1:6.5.

To see the [SAPS](https://www.sap.com/about/benchmark/measuring.html) numbers for the Compute Engine virtual machines that are certified for SAP applications, see the SAP note [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

SAP provides a certified list of Google Cloud configurations for SAP HANA on its website as well. For more information, see [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).

### Plan regions and zones

When you deploy a Compute Engine instance, you must choose a region and zone. A region is a specific geographical location where you can run your resources, and corresponds to one or more data center locations in relatively close proximity to each other. Each region has one or more zones with redundant connectivity, power, and cooling.

Global resources, such as pre-configured disk images and disk snapshots, can be accessed across regions and zones. Regional resources, such as regional static external IP addresses, can only be accessed by resources that are in the same region. Zonal resources, such as compute instances and disks, can only be accessed by resources that are located in the same zone. For more information, see [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

![Google Cloud regions and zones.](https://docs.cloud.google.com/static/sap/docs/images/gc-global-regional-zonal-resources.svg)

When you choose a region and zone for your compute instances, consider the following:

  * The location of your users and your internal resources, such as your data center or corporate network. To decrease latency, select a location that is in close proximity to your users and resources.
  * The CPU platforms that are available for that region and zone. For example, Intel's Broadwell, Haswell, Skylake, and Ice Lake processors are supported for workloads of SAP NetWeaver on Google Cloud. 
    * For more information, see the SAP note [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).
    * For details about which regions the Haswell, Broadwell, Skylake, and Ice Lake processors are available for use with Compute Engine, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * Ensure that your SAP Application Server and your database are in the same region.



### Storage options for SAP S/4HANA

The following are the storage options offered by Google Cloud that are certified by SAP for use with SAP S/4HANA and SAP HANA. 

For general information about storage options in Google Cloud, see [Storage options](https://docs.cloud.google.com/compute/docs/disks).

#### Persistent Disk

  * Standard Persistent Disk (`pd-standard`): efficient and economical block storage backed by [standard hard disk drives (HDD)](https://en.wikipedia.org/wiki/Hard_disk_drive) for handling sequential read-write operations, but not optimized to handle high rates of random input-output operations per second (IOPS).
  * SSD Persistent Disk (`pd-ssd`): provides reliable, high-performance block storage backed by [solid-state drives (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive).
  * Balanced Persistent Disk (`pd-balanced`): provides cost-effective and reliable SSD-based block storage.
  * Extreme Persistent Disk (`pd-extreme`): SSD-based; provides higher maximum IOPS and throughput options than `pd-ssd` for larger Compute Engine machine types. For more information, see [Extreme persistent disks](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).



#### Hyperdisk

  * Hyperdisk Extreme (`hyperdisk-extreme`): provides higher maximum IOPS and throughput options than SSD based Persistent Disk volumes. You select the performance needed by provisioning IOPS, which determines the throughput. Its best use is to host the `/hana/data` and `/hana/log` directories. For more information, see [About Google Cloud Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme).

  * Hyperdisk Balanced (`hyperdisk-balanced`): The best fit for most workloads. We recommend this option for use with databases that don't require the performance of Hyperdisk Extreme. You select the performance you need by provisioning the IOPS and throughput. You can use Hyperdisk Balanced volumes to host the `/hana/data` and `/hana/log` directories. For more information, see [About Google Cloud Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced).




Persistent Disk and Hyperdisk are designed for high durability. They store data redundantly to ensure data integrity. Each Persistent Disk volume can store up to 64 TB, so you can create large logical volumes without managing arrays of disks. Hyperdisk volumes also allow up to 64 TB of storage, depending on the type you use. One key feature is that Persistent Disk and Hyperdisk volumes are automatically encrypted to protect data.

Upon creation, a Compute Engine VM instance allocates a single root Persistent Disk or Hyperdisk by default that contains the operating system. You can add more storage options to the VM instance as required.

For SAP implementations, review the recommended storage options in the SAP directory structure and storage options.

#### File sharing solutions

Several file sharing solutions are available on Google Cloud, including the following:

  * Filestore: Google Cloud high-performance, fully managed NFS file storage with regional availability.
  * Google Cloud NetApp Volumes: A fully managed NFS or SMB file storage solution from Google Cloud.
  * NetApp Cloud Volumes ONTAP: A full-featured, smart storage solution that you deploy and manage yourself on a Compute Engine VM.



For more information about file sharing solutions for SAP S/4HANA on Google Cloud, see [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap).

#### Cloud Storage for object storage

Cloud Storage is an object store for files of any type or format; it has virtually unlimited storage, and you don't have to worry about provisioning it or adding more capacity. An [object](https://docs.cloud.google.com/storage/docs/objects) in Cloud Storage contains file data and its associated metadata, and can be up to 5 TB in size. A Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/buckets) can store any number of objects.

It's common practice to use Cloud Storage to store backup files for nearly any purpose. For example, Cloud Storage is a good place to store the SAP HANA database backups. For information about database backup planning, see [Database backup and recovery](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#database_backup_recovery). You can also use Cloud Storage as part of a [migration process](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#migration_process).

Additionally you can use Backup and DR Service as a centralized solution for backup and disaster recovery operations. This service supports a broad spectrum of databases including SAP HANA. For more information, see [Backup and Disaster Recovery Solutions with Google Cloud](https://cloud.google.com/solutions/backup-dr).

Choose your Cloud Storage option based on how frequently you need to access the data. For frequent access, such as multiple times a month, select the Standard storage class. For infrequent access, select Nearline or Coldline storage. For archived data, which you don't expect to access, select Archive storage.

#### SAP directory structure and storage options

The following tables describe the Linux directory structures for SAP HANA databases and SAP ABAP instances on Google Cloud.

  * Recommended storage options for Linux directory structure on SAP HANA:

SAP HANA directory | Recommended storage option in Google Cloud  
---|---  
`/usr/sap` | Balanced Persistent Disk  
`/hana/data` | SSD-based Persistent Disk or Hyperdisk  
`/hana/log` | SSD-based Persistent Disk or Hyperdisk  
`/hana/shared`* | Balanced Persistent Disk  
`/hanabackup`* | Balanced Persistent Disk  
  
In distributed deployments, `/hana/shared` and `/hanabackup` can also be mounted as a network file system using an NFS solution such as Filestore. 

For information about persistent disk storage that SAP has certified for use with SAP HANA, see [Persistent disk storage for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#persistent_disk_storage_for_sap_hana).

  * Recommended storage options for Linux directory structure on SAP ABAP instance:

Directory | Recommended storage option in Google Cloud  
---|---  
`/sapmnt`† | Balanced Persistent Disk  
`/usr/sap` | Balanced Persistent Disk  
  
In distributed deployments, `/sapmnt` can also be mounted as a network file system using an NFS solution such as [Filestore](https://docs.cloud.google.com/filestore/docs). 

For information about persistent disk storage that SAP has certified for use with SAP ABAP instances, see [Persistent disk storage for SAP applications](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#persistent_disk_storage_for_sap_applications).




### OS support for SAP S/4HANA

When choosing an operating system (OS) for SAP NetWeaver on Google Cloud, in addition to confirming that the OS version is certified by SAP, you also need to confirm that all three companies, SAP, the OS vendor, and Google Cloud, still support the OS version.

Your decision must also take into account the following:

  * Whether a given OS version is available from Google Cloud. The [OS images](https://docs.cloud.google.com/compute/docs/images) provided by Compute Engine are configured to work with Google Cloud. If an OS is not available from Google Cloud, then you can bring your own OS image (BYOI) and license. BYOI OS images are referred to by Compute Engine as [custom images](https://docs.cloud.google.com/compute/docs/images#custom_images).
  * The available licensing options for a given OS version. Review if the OS version has an on-demand licensing option or if you need to bring-your-own-subscription (BYOS) from the OS vendor.
  * Whether the integrated high-availability capabilities of a given OS version are enabled for Google Cloud.
  * The [committed use discount option](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments) for SLES for SAP and RHEL for SAP images.



The following operating systems are certified by SAP for use with SAP NetWeaver on Google Cloud:

  * [Red Hat Enterprise Linux (RHEL)](https://access.redhat.com/articles/3751271)
  * [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/products/sles-for-sap/)



You can find more information about specific OS versions and their compatibility with both SAP S/4HANA and SAP HANA in the following guides:

  * [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support)
  * [OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support)



### SAP HANA Fast Restart option

For SAP HANA 2.0 SP04 and later, Google _strongly_ recommends the [SAP HANA Fast Restart option](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/ce158d28135147f099b761f8b1ee43fc.html).

This option is automatically enabled when you deploy SAP HANA using the following Terraform modules provided by Google Cloud: module `sap_hana` or `sap_hana_ha`, version `202309280828` or later. For information about how to manually enable SAP HANA Fast Restart, see [Enable the SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config#enable-hana-fast-restart).

SAP HANA Fast Restart reduces restart time in the event that SAP HANA terminates, but the operating system remains running. To reduce the restart time, SAP HANA leverages the SAP HANA persistent memory feature to preserve `MAIN` data fragments of column store tables in DRAM that is mapped to the `tmpfs` file system.

Additionally, on VMs in the M2 and M3 families of Compute Engine memory-optimized machine types, SAP HANA Fast Restart improves recovery time if uncorrectable errors occur in memory. For more information, see [SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#sap-hana-fast-restart-on-gc).

### Deployment architecture for SAP HANA

SAP HANA is a key component of any SAP S/4HANA system because it serves as a database for the system. There are two possible architectures that you can use when deploying the SAP HANA database: scale-up and scale-out.

#### Scale-up architecture

The following diagram shows a scale-up architecture for SAP HANA on Google Cloud. In the diagram, notice both the deployment on Google Cloud and the disk layout. You can use Cloud Storage to back up your local backups available in `/hanabackup`. This mount must be sized equal to or greater than the data mount.

![Architecture diagram for the deployment of an SAP HANA scale-up system on Google Cloud.](https://docs.cloud.google.com/static/sap/docs/images/hana-scale-up.svg)

#### Scale-out architecture

The scale-out architecture for SAP HANA consists of one master host, a number of worker hosts, and, optionally, one or more standby hosts. The hosts are interconnected through a network that supports sending data between hosts at rates of up to 32 Gbps, or up to 100 Gbps on selected machine types using [high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration). 

As the workload demand increases, especially when using Online Analytical Processing (OLAP), a multi-host scale-out architecture can distribute the load across all hosts.

The following diagram shows a scale-out architecture for SAP HANA on Google Cloud:

![Architecture diagram for the deployment of an SAP HANA scale-out system on Google Cloud.](https://docs.cloud.google.com/static/sap/docs/images/hana-scale-out.svg)

### Deployment architecture for SAP S/4HANA

As mentioned in the Architecture section, there are multiple deployment architectures that you can use for deploying SAP S/4HANA on Google Cloud.

#### Two-tier architecture

This architecture is presented in the centralized deployment section. The following diagram shows some details of a two-tier architecture for SAP S/4HANA running on a Compute Engine VM:

![Two-tier architecture for SAP S/4HANA on a Compute Engine
  VM on Google Cloud.](https://docs.cloud.google.com/static/sap/docs/images/sap-nw-2tier-architecture.svg)

#### Three-tier architecture

This architecture is presented in the distributed deployment section. You can use this architecture to deploy high-availability SAP S/4HANA systems. The following diagram shows some details of a three-tier architecture for SAP S/4HANA running on Compute Engine VMs:

![Three-tier architecture for SAP S/4HANA on Compute Engine
  VMs on Google Cloud.](https://docs.cloud.google.com/static/sap/docs/images/sap-nw-3tier-architecture.svg)

In this architecture, the SAP S/4HANA system distributes work across multiple NetWeaver Application Servers (AS), each hosted on a separate VM. All the NetWeaver AS nodes share the same database, which is hosted on a separate VM. All the NetWeaver AS nodes mount and access a shared file system that hosts the SAP NetWeaver profiles. This shared file system is hosted on a Persistent Disk volume shared across all nodes or on a supported [file sharing solution](https://docs.cloud.google.com/sap/docs/filers-for-sap).

### Security, privacy, and compliance

This section provides information about security, privacy, and compliance for running SAP S/4HANA on Google Cloud.

#### Compliance and sovereign controls

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must plan for using Assured Workloads \- a service that helps you run secure and compliant workloads on Google Cloud without compromising the quality of your cloud experience. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

#### Networking and network security

Consider the information in the following sections when planning networking and network security.

##### Minimum privilege model

One of your first lines of defense is to restrict who can reach your network and your VMs. You do this by using [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls). By default, all traffic to VMs, even from other VMs, is blocked by the firewall unless you create rules to allow access. The exception is the default network that is created automatically with each project and has default [firewall rules](https://docs.cloud.google.com/vpc/docs/vpc#firewall_rules).

By creating VPC firewall rules, you can restrict all traffic on a given set of ports to specific source IP addresses. To restrict access to the specific IP addresses, protocols, and ports that need access, follow the minimum privilege model. For example, always set up a bastion host and allow SSH communications to your SAP NetWeaver system only from that host.

##### Custom networks and firewall rules

You can use a network to define a gateway IP and the network range for the VMs attached to that network. All Compute Engine networks use the [IPv4](https://tools.ietf.org/html/rfc791) protocol. Every Google Cloud project is provided with a default network with preset configurations and firewall rules, but we recommend that you add a custom subnetwork and add firewall rules based on a minimum privilege model. By default, a newly created network has no firewall rules and hence no network access.

You might want to add more than one subnetwork if you want to isolate parts of your network, or satisfy other requirements. For more information, see [Networks and subnets](https://docs.cloud.google.com/compute/docs/vpc#vpc_networks_and_subnets).

The firewall rules apply to the entire network and all the VMs in the network. You can add a firewall rule that allows traffic between VMs in the same network and across subnetworks. You can also configure firewalls to apply to specific target VMs by using [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

SAP requires access to certain ports, so add firewall rules to allow access to the [ports outlined by SAP](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).

##### Routes

[Routes](https://docs.cloud.google.com/vpc/docs/routes) are global resources attached to a single network. User-created routes apply to all VMs in a network. This means you can add a route that forwards traffic from VM to VM within the same network and across subnetworks without requiring external IP addresses.

For external access to internet resources, launch a VM with no external IP address and configure another VM as a NAT gateway. This configuration requires you to add your NAT gateway as a route for your SAP instance.

#### Bastion hosts and NAT gateways

If your security policy requires truly internal VMs, then you need to manually set up a NAT proxy on your network and a corresponding route so that VMs can reach the internet. It is important to note that you cannot directly connect to a fully internal VM instance by using SSH.

To connect to such internal machines, you must set up a _bastion_ instance that has an external IP address and then tunnel through it. When VMs don't have external IP addresses, they can only be reached by other VMs on the network, or through a managed VPN gateway. You can provision VMs in your network to act as trusted relays for inbound connections, called _bastion hosts_ , or network egress, called _NAT gateways_. For more transparent connectivity without setting up such connections, you can use a managed VPN gateway resource.

##### Bastion hosts for inbound connections

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private-network VMs. This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH communication from the internet.

![Bastion host show in SSH scenario.](https://docs.cloud.google.com/static/solutions/images/bastion.png)

SSH access to VMs that don't have an external IP address can be achieved by first connecting to a bastion host. A complete hardening of a bastion host is outside the scope of this document, but some initial steps taken can include:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private VMs from only the bastion host.



By default, SSH on VMs is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private VM. Due to this two-step login, we recommend that you use SSH-agent forwarding to reach the target VM instead of storing the target VM's private key on the bastion host. You must do this even if you are using the same key-value pair for both bastion and target VMs because the bastion has direct access only to the public half of the key-pair.

##### NAT gateways for outbound data transfer

When a VM does not have an assigned, external IP address, it cannot make direct connections to external services, including other Google Cloud services. To let these VMs to reach services on the internet, you can set up and configure a [NAT gateway](https://docs.cloud.google.com/nat/docs/overview). The NAT gateway is a VM that can route traffic on behalf of any other VM on the network. Use one NAT gateway per network. A single-VM NAT gateway is not highly available and cannot support high traffic throughput for multiple VMs. For information about how to set up a VM to act as a NAT gateway, see the deployment guide for your operating system:

  * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
  * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)



#### Cloud VPN

You can securely connect your existing network to Google Cloud through a [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection that uses [IPsec](https://wikipedia.org/wiki/IPsec) by using Cloud VPN. Traffic traveling between the two networks is encrypted by one VPN gateway, then decrypted by the other VPN gateway. This protects your data as it travels over the internet. You can dynamically control which VMs can send traffic down the VPN by using instance tags on routes. Cloud VPN tunnels are billed at a static monthly rate plus standard charges for outbound data transfer. Note that connecting two networks in the same project still incurs standard charges for outbound data transfer. For more information, see:

  * [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Choosing Cloud VPN for networking connectivity](https://docs.cloud.google.com/network-connectivity/docs/how-to/how-to-choose#cloud-vpn)



#### Security for Cloud Storage buckets

If you use Cloud Storage to host your backups for your data and log volumes, then make sure you use TLS (HTTPS) while sending data to Cloud Storage from your VMs to protect data in transit.

While Cloud Storage automatically encrypts data at rest, you can instead specify your own encryption keys if you have your own key-management system.

#### Email notification limits

To help protect your systems and Google's from abuse, Google Cloud enforces limitations for sending email from Compute Engine. This has implications for the SCOT transaction on SAP NetWeaver ABAP systems because it requires a specific configuration compared to on-premises systems.

For more information, including information about configuring SCOT, see [Sending email from an instance](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail).

#### Related security documents

For more information about security resources for your SAP environment on Google Cloud, see the following:

  * [Securely connecting to VM instances](https://cloud.google.com/solutions/connecting-securely)
  * [Security Center](https://cloud.google.com/security)
  * [Compliance in Google Cloud](https://cloud.google.com/compliance)
  * [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)
  * The [Google Infrastructure Security Design Overview PDF](https://docs.cloud.google.com/static/docs/security/infrastructure/design/resources/google_infrastructure_whitepaper_fa.pdf)



### Reliability

This section provides information about aspects related to reliability for running SAP S/4HANA on Google Cloud.

#### High availability and disaster recovery

High availability (HA) and disaster recovery (DR) are sets of techniques, engineering practices, and design principles to enable business continuity in the event of failures. These approaches work by eliminating single points of failure and providing the ability to rapidly resume operations after a system or component outage with minimal business disruption. Fault recovery is the process of recovering and resuming operations after an outage due to a failed component.

For example, the following are some HA and DR tools that you can use:

  * Linux clustering across zones: For more information check the [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide) and [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide).
  * [Live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration)
  * [VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options)
  * [Service Auto-Restart](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/cf10efba8bea4e81b1dc1907ecc652d3.html?version=2.0.01)
  * Backups

Here are some further details about some of these tools: 
  * **Linux clustering across zones** : Setting up your Linux cluster across [zones](https://docs.cloud.google.com/compute/docs/regions-zones) helps guard against component failures in a given region. 

On the SAP NetWeaver application layer, you can deploy a Linux cluster across zones to reduce the impact of a failure on the ASCS and make it highly available across both nodes on different zones. The Linux cluster then moves the ASCS to the standby node in case the primary node has any issue or maintenance is being performed. Additionally you can use an Enqueue Replication Server to replicate the content of the enqueue table so that the Enqueue Server maintains the content of the enqueue table on the standby node in case the process is promoted from primary to standby.

On the SAP HANA database layer, you can deploy a Linux cluster across zones using either an active/passive configuration or an active/active configuration. In both cases, you start by setting up two Compute Engine instances in separate zones, each with its own SAP HANA database.

    * **Active/passive configuration** : Configure one instance as the cluster's primary node (active) and the other as the secondary node (passive). Use SAP HANA System Replication (SR) to configure the secondary node to take over as the primary if the primary fails. For more information about how to configure and set up HANA SR, see [HANA System Replication](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.02/en-US/099caa1959ce4b3fa1144562fa09e163.html).
    * **Active/active configuration (read-enabled)** : Configure both instances to be active, but the secondary node as read-only. This setup is based on continuous log replay. The virtual IP (VIP) is configured to point to the current read/write node. For more information, see [Active/Active (Read Enabled)](https://help.sap.com/docs/PRODUCT_ID/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html?state=PRODUCTION&version=2.0.03&locale=en-US).

Additionally it is possible to use SAP HANA System Replication as a Disaster Recovery solution. The primary database replicates its content to the standby database, which can be used in case the primary goes offline, allowing the SAP system to keep working until the service on the primary database is restored. Promoting the secondary node in this case doesn't happen automatically; it must be performed manually. You can also combine both HA and DR on the SAP HANA side to increase resilience and availability. For more information, see:

    * [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide)
    * [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide)
  * **Live migration** : Compute Engine offers live migration to keep your VM instances running even when a host system event occurs, such as a software or hardware update. In that situation, Compute Engine performs a live migration of your running instance to another host in the same zone, rather than requiring your running instance to be rebooted. The mechanism replicates the original instance's VM state, so when the new instance comes up, it already has the original instance's memory pre-loaded.

In the rare case when live migration doesn't happen, the failed virtual machine is automatically restarted on the new hardware within the same zone. For more information, see [Live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process). 




### Cost optimization

This section provides information about licensing, discounts, and estimating workload size.

#### Licensing

If you're an SAP customer, then you can use your existing license to deploy SAP SAP S/4HANA on Google Cloud under a bring-your-own-license (BYOL) model. Google Cloud supports the BYOL model for both production and non-production use cases. Operating system licenses are included in Compute Engine prices.

Alternatively, you can bring your own OS image and licenses as well. For more information, see [Custom OS images](https://docs.cloud.google.com/compute/docs/images#custom_images).

#### Discounts

With Google Cloud's pay-as-you-go pricing model, you only pay for the services you use. You don't have to be committed to a particular size or service; you can alter or stop your usage as required. For predictable workloads, Compute Engine provides committed use discounts (CUDs) that help to reduce the cost of your infrastructure by committing to a contract in return for heavily discounted VM usage prices.

Google Cloud offers these discounts in return for purchasing committed use contracts, also known as _commitments_. When you purchase a commitment, you commit either to a minimum amount of resource usage or to a minimum spend amount for a specified term of one or three years. These discounts help you lower your monthly bill for those resources used by your SAP S/4HANA system. For more information, see [Committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).

#### Size estimations

The following resources provide information about how to perform size estimations for your SAP systems before migrating them to Google Cloud:

  * [Review SAP workload sizing](https://docs.cloud.google.com/migration-center/docs/estimate/sap-sizing-guidance)
  * [Estimate infrastructure cost for your SAP workload](https://docs.cloud.google.com/migration-center/docs/estimate/specify-sap-workload-requirements)



### Operational efficiency

This section provides information about how you can optimize the operational efficiency of SAP S/4HANA on Google Cloud.

#### Backup and recovery

Create backups of your application server and database on a regular basis so that you can recover in case of a system crash, data corruption, or any other issue.

You have a number of options to back up your SAP HANA data on Google Cloud, including the following:

  * Back up using Google's [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery). For more information, see [Back up a discovered SAP HANA database and its logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/back-up-sap-hana-db).
  * Back up directly to Cloud Storage using the SAP-certified Backint feature of Google Cloud's Agent for SAP.
  * Back up to a disk and then uploading the backups to Cloud Storage.
  * Back up disks using snapshots.



###### Back up to Cloud Storage

From version 3.0, Google Cloud's Agent for SAP supports the Backint feature, which allows SAP HANA to back up and recover database backups directly from Cloud Storage. This new feature is available for SAP HANA instances running on Compute Engine instances, on premises servers, or on other cloud platforms so you can back up directly to, and recover from, Cloud Storage without needing persistent disk storage for your backups. For more information, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide?operating_system=SUSE#cloud_storage_backups).

For information about the SAP certification of this feature of the agent, see the SAP note [2031547 - Overview of SAP-certified 3rd party backup tools and associated support process](https://launchpad.support.sap.com/#/notes/2031547).

The following diagram shows the flow of backups when you use the Backint feature of Google Cloud's Agent for SAP:

![Diagram showing backing up SAP HANA data to Cloud Storage by using Google Cloud's Agent for SAP.](https://docs.cloud.google.com/static/sap/docs/images/hana-backup-using-backint.svg)

###### Back up to disks

You can use the native SAP HANA backup and recovery function with Compute Engine Persistent Disk volumes and use a Cloud Storage bucket for longer-term storage of the backups.

During normal operation, SAP HANA automatically saves data from memory to disk at regular save points. Additionally, all data changes are captured in redo log entries. A redo log entry is written to disk after each committed database transaction.

From SAP HANA 2.0 and later, use SAP HANA cockpit to create SAP HANA backups.

The following diagram shows the flow of the backup feature for SAP HANA:

![Diagram showing backing up SAP HANA data to persistent storage disk.](https://docs.cloud.google.com/static/sap/docs/images/hana-backup-using-disk.svg)

###### Back up disks using snapshots

Another option that you can add to your backup strategy is to take snapshots of entire disks by using the [disk snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots) feature of Compute Engine. For example, you can take scheduled snapshots of the disk hosting your `/hanabackup` directory for use in disaster recovery scenarios. It is also possible to use disk snapshots to back up and recover your SAP HANA data volume. To ensure application consistency, take snapshots when no changes are being made to the target volume. Snapshots occur on the block level.

After the first snapshot, each subsequent snapshot is incremental and stores only incremental block changes, as shown in the following diagram.

When you're using version 3.0 or later of Google Cloud's Agent for SAP, you can create backups and perform recovery for SAP HANA using the agent's disk snapshot feature. For more information, see [Backup and recovery for SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).

![Diagram showing backing up SAP HANA data using disk snapshots.](https://docs.cloud.google.com/static/sap/docs/images/hana-backup-using-snapshot.svg)

##### Recovery

The recovery tools in SAP HANA can recover to the latest point in time or a specific point in time, and you can use these tools to restore to a new system or create a copy of the database. Unlike backups, which you can run while the database is operational, you can use recovery tools only while the database is shut down. You can choose an appropriate option from the following:

  * Restore to the most recent state, using any of the following resources: 
    * Full backup or snapshot
    * Log backups
    * Redo log entries that are still available
  * Restore to a point in time in the past.
  * Restore to a specified full backup.



#### Monitoring

To monitor and provide support for SAP workloads running on Compute Engine instances, Google Cloud provides the Agent for SAP.

As mandated by SAP, to get support from SAP and to enable SAP to meet its service-level agreements (SLAs), you must install [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning) on all Compute Engine instances that run any SAP system. For more information about the support prerequisites, see SAP note [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

In addition to the mandatory collection of SAP Host Agent metrics, on Linux, Google Cloud's Agent for SAP includes optional features such as collection of Process monitoring metrics and Workload Manager evaluation metrics. You can opt in to these features that enable products and services such as [workload management](https://docs.cloud.google.com/workload-manager/docs/overview) for your SAP workloads.

### Performance optimization

This section provides information about optimizing the performance of SAP S/4HANA workloads through sizing and network configuration.

#### Sizing

Several sizing options are available based on the implementation type. For greenfield implementations, we recommend using the SAP Quick Sizer tool. For detailed information, see SAP's [Sizing](https://www.sap.com/about/benchmark/sizing.html) page. SAP also provides T-shirt guides for specific solutions and tools for migrating current on-premises solutions to Google Cloud. For example, see [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29) and the SAP note [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432). SAP and Google Cloud use different units to measure IOPS (input/output operations per second). Consult your SI (Systems Integrator) partner to convert SAP sizing requirements into appropriately sized Google Cloud infrastructure.

Before you migrate existing systems from SAP ECC to S/4HANA, SAP recommends that you run the `/SDF/HDB_SIZING` report, as described in SAP note [1872170 - ABAP on HANA sizing report (S/4HANA, Suite on HANA...)](https://me.sap.com/notes/1872170). This sizing report analyzes your source system's current memory and processing needs and provides information about the requirements for moving to S/4HANA. 

#### Network configuration

Your Compute Engine VM network capabilities are determined by its machine family, and not by its network interface (NIC) or IP address.

Based on its machine type, your VM instance is capable of 2 to 32 Gbps network throughput. Certain machine types also support throughputs up to 100 Gbps, which requires the use of the Google Virtual NIC (gVNIC) interface type with a Tier_1 network configuration. The ability to achieve these throughput rates is further dependent on the traffic direction and the type of the destination IP address.

Compute Engine VM network interfaces are backed by redundant and resilient network infrastructure using physical and software-defined network components. These interfaces inherit the redundancy and resiliency of the underlying platform. Multiple virtual NICs can be used for traffic separation, but that offers no additional resilience or performance benefits.

A single NIC provides the needed performance for SAP HANAdeployments on Compute Engine. Your particular use case, security requirements, or preferences might also require additional interfaces for separating traffic, such as internet traffic, internal SAP HANA System Replication traffic, or other flows that might benefit from specific network policy rules. We recommend that you employ the traffic encryption offered by the application, and secure network access by following a least-privilege firewall policy to restrict access.

Consider the need for traffic separation early on as part of your network design and allocate additional NICs when you deploy VMs. Your choice for the number of network interfaces depends on the level of isolation that you require. For more information about multi-NIC VMs, such as network and subnetwork requirements and the maximum number of network interfaces, see [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

For example, you might define a VPC network for your SAP HANA SQL application clients, such as SAP NetWeaver application servers and custom applications, and a separate VPC network for inter-server traffic, such as SAP HANA System Replication. Consider that too many segments might complicate management and troubleshooting of network issues. If you change your mind later, then you can use Compute Engine [machine images](https://docs.cloud.google.com/compute/docs/machine-images) to recreate your VM instance while retaining all associated configuration, metadata, and data. 

For more information, see:

  * [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview)
  * [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth)



## Deployment

This section provides information related to deploying SAP S/4HANA on Google Cloud.

### Important pre-deployment SAP notes

Before you begin deploying an SAP S/4HANA system on Google Cloud, read the following SAP notes. Also, before you begin any SAP implementation, check the SAP Marketplace for updated product installation guides and notes.

  * [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432)
  * [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441)
  * [2456953 - Windows on Google Cloud Platform (IaaS): Adaptation of your SAP License](https://me.sap.com/notes/2456953)
  * [1380654 - SAP support in public cloud environments](https://me.sap.com/notes/1380654)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406)



### Deployment automation

To install SAP S/4HANA on Google Cloud, you can use the following deployment options: 

  * To automate the deployment of a distributed or distributed with high availability (HA) system, you can use the Guided Deployment Automation tool in Workload Manager. This tool lets you configure and deploy supported SAP workloads directly from the Google Cloud console, or generate and download the equivalent Terraform and Ansible code. For more information, see [About Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment). 
  * To automate the deployment of a centralized or distributed SAP HANA system, you can use the Terraform configurations provided by Google Cloud. For more information, see the deployment guide for your [SAP HANA scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions). 



## What's next

  * Learn more about the Google Cloud services used in this guide: 
    * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
    * [Compute Engine](https://docs.cloud.google.com/compute/docs)
    * [Storage options](https://docs.cloud.google.com/compute/docs/disks): Persistent Disk, Hyperdisk, and Cloud Storage
    * [Google Cloud console](https://console.cloud.google.com/)
    * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
    * [Identity and Access Management](https://docs.cloud.google.com/iam/docs)
    * [Filestore](https://docs.cloud.google.com/filestore/docs)
    * [NetApp Cloud Volumes ONTAP](https://bluexp.netapp.com/ontap-cloud)
    * [Google Cloud NetApp Volumes](https://bluexp.netapp.com/google-cloud-netapp-volumes)
    * [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery#all-features)
  * For more reference architectures, design guides, and best practices, explore the [Cloud Architecture Center](https://cloud.google.com/architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
