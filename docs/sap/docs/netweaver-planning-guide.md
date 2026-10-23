---
url: https://docs.cloud.google.com/sap/docs/netweaver-planning-guide/
title: SAP NetWeaver planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:44.974056+00:00
---

# SAP NetWeaver planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-planning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP NetWeaver planning guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of how SAP NetWeaver works on Google Cloud, and provides details that you can use when planning the migration of your existing SAP NetWeaver system, or when implementing a new system. Google Cloud is certified for running SAP NetWeaver application servers ABAP and Java, and SAP products based on these application server stacks.

This guide does not cover the specifics of deploying the SAP NetWeaver system. To learn how to plan for your deployment of SAP NetWeaver, see the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).

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

### Pricing and quotas

You can use the [pricing calculator](https://cloud.google.com/products/calculator/) to estimate your usage costs. For more pricing information, see [Compute Engine pricing](https://cloud.google.com/compute/pricing), [Cloud Storage pricing](https://cloud.google.com/storage/pricing), and [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

Google Cloud resources are subject to quotas. If you plan to use high-CPU or high-memory machines, then you might need to request additional quota. For more information, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

## Compliance and sovereign controls

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must plan for using Assured Workloads \- a service that helps you run secure and compliant workloads on Google Cloud without compromising the quality of your cloud experience. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

## Overview of SAP NetWeaver on Google Cloud

In many ways, running SAP NetWeaver on Google Cloud is similar to running it in your own data center. You still need to think about computing resources, storage, and networking considerations. You also still need to think through how to handle backups and disaster recovery for your database.

Here are some of the differences that you should understand:

  * You interact with the various infrastructure components through _services_ , which are abstractions or virtualizations of the hardware that you would use on premises. For example, some of the virtualized infrastructure services that you use instead of hardware on Google Cloud include Compute Engine instances and persistent disks, Virtual Private Cloud networks and firewalls, and Cloud Storage buckets for mass storage.
  * Google Cloud services offer particular features and introduce certain limitations.
  * Google Cloud services work together in particular ways.
  * SAP NetWeaver and the Google Cloud services work together in particular ways.



The following diagram provides a high-level overview of SAP NetWeaver running on Google Cloud:

![Overview of SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/static/sap/docs/images/netweaver-overview.svg)

Here are some important things to notice in the diagram:

  * The system uses some number of Compute Engine instances and persistent disks. These components host the software, including the main database system.
  * The SAP NetWeaver system consists of its usual application components plus a Host Agent component.
  * The SAP Host Agent/SAPOSCOL component collects monitoring metadata from Google Cloud's Agent for SAP. Google Cloud's Agent for SAP aggregates metrics from Cloud Monitoring, the Google Cloud monitoring solution.
  * All communication between Google Cloud components and external components pass through a networking layer. This layer provides security features, including firewalls, routes and internet gateways, VPN, and so on.



### Two-tier architecture

The following diagram shows some details of a 2-tier architecture running on a Compute Engine instance.

![2-tier architecture](https://docs.cloud.google.com/static/sap/docs/images/netweaver-2-tier.svg)

In this architecture, all the components run on a single Compute Engine instance. The compute instance has 5 attached Persistent Disk volumes, each serving a specific role. These roles include:

  * **Root disk** : Contains the operating system for the compute instance.
  * **Swap disk** : Contains the operating system's paging file.
  * **SAP NetWeaver** : Contains the NetWeaver installation and the profile files.
  * **Data volume** : Contains the database files.
  * **Logs volume** : Contains the database-system logs used for maintaining data consistency, backup, and recovery operations.



Depending on which database server you are using, the data volumes that you need might be different than those shown in the preceding figure.

Up to a limit, the performance of an SSD or balanced persistent disk improves as the size of the disk and the number of vCPUs increases. If you use one of these persistent disk types, create a larger PD volume and logically partition the disk in the guest operating system for multiple file systems. For example, if you use SAP HANA, you can map the `/hana/data`, `/hana/log`, and `/hana/shared` volumes to a single persistent disk. Using a larger single persistent disk also allows for easier resizing in the VM and simplifies management.

Depending on your application, attaching multiple persistent disk volumes to your VM can have operational benefits. For example, it can simplify the use of persistent disk snapshots for specific volumes.

Striping over multiple persistent disk volumes does not provide a significant performance benefit for SAP on Google Cloud.

For more information, see:

  * [Persistent disk performance](https://docs.cloud.google.com/compute/docs/disks/performance#multiple_disks_on_a_single_vm_instance) in the Compute Engine documentation.
  * [Persistent disk storage](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#persistent_disk_storage) on this page



The database server is also likely to require higher performance persistent disks than SAP NetWeaver requires.

For example, for a SAP HANA deployment:

  * The disk marked "Data volume" contains the data files.
  * The disk marked "Logs" contains the HANA log files.
  * The HANA binaries and shared files can be hosted on the disk labeled "NetWeaver".
  * You need an additional volume for storing database backups.



For information about SAP HANA on Google Cloud, see:

  * [SAP HANA deployment architecture](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#deployment_architecture)
  * [Persistent disk storage for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage_for_sap_hana).



For a list of the disk drives required for SAP ASE, see the [SAP ASE Planning Guide](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide#deployment_architecture).

For a list of the disk drives required for SAP MaxDB, see the [SAP MaxDB Planning Guide](https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide#deployment_architecture).

For a deployment of IBM Db2 for Linux, UNIX and Windows (IBM Db2), more disk drives are required than those shown in the preceding figure. For a list of the required disk drives, see the [IBM Db2 for SAP Planning Guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#deployment_architecture).

For information about Microsoft SQL Server on Google Cloud, see [Windows on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows#sql_server).

In upcoming sections, you learn about details and recommendations for these components.

### Three-tier architecture

The following diagram shows some details of a 3-tier architecture running on Compute Engine.

![3-tier architecture](https://docs.cloud.google.com/static/sap/docs/images/netweaver-3-tier.svg)

In this architecture, the SAP NetWeaver system distributes work across multiple NetWeaver Application Servers (AS) hosted on multiple VMs. All the NetWeaver AS nodes share the same database, which is hosted on a separate VM. All the NetWeaver AS nodes mount and access a shared file system that hosts the SAP NetWeaver profiles. This shared file system is contained on a persistent disk that is attached to VM 1, along with the SAP central services.

## Certified machines

Google Cloud provides most computing resources as VMs, also called _VM instances_ , through Compute Engine. Google Cloud provides bare-metal machines through Bare Metal Solution.

All machine types can:

  * Run operating systems.
  * Host SAP central services.
  * Host SAP AS.
  * Host database servers.



As you plan your SAP implementation, consider the following:

  * The number of machines that your implementation architecture requires. This number can range from one VM for a development, training, or small production system, to many VMs for a scale-out production system.
  * Particular _machine types_ , which determine processing power—CPU types, number of cores, and so on—and available volatile memory.
  * Increasing the number of vCPUs in a VM instance increases the network bandwidth for outgoing communications (the egress rate) from the VM up to a limit that can differ depending on the machine type. See [VPC resource quotas per instance](https://docs.cloud.google.com/vpc/docs/quota#per_instance).
  * _Image types_ , which determine the operating system, and the database type if you choose to use SQL Server.
  * The location of the VMs. Compute Engine resources run in Google Cloud data centers worldwide, and these data centers are organized by _region_ and _zone_. You learn more in Plan regions and zones.
  * The amount of persistent disk storage and the number of persistent disks. For most machine types, you can attach up to 257 TB of persistent disk storage. Although you can attach up to 128 persistent disks to most machine types, using fewer persistent disks reduces management overhead.



If you expect high network traffic, as is often the case in three-tier architectures that put the database on a separate VM, select a VM instance with enough vCPUs to provide the throughput you need.

For information on Google Cloud machine types and SAPS, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

The following sections provide further details.

### Machine types

For information about the Compute Engine machine types that SAP has certified for use with SAP NetWeaver, go to [Certified solutions and machine types](https://docs.cloud.google.com/sap/docs/sap-certifications#certified-machine-types-and-solutions) and in the **Certified SAP solution** menu, select **SAP NetWeaver**.

Before selecting a machine type for use, confirm that it is available in the region and zones that you need.

**Note:** Because the capacity (SAPS) of an instance of a custom machine type (a _custom VM instance_) is not predetermined, SAP cannot guarantee that a configured custom VM instance would be suitable to run Business Suite workloads without first reviewing the configuration. For more information, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432). 

#### Regional availability of SAP-certified Bare Metal Solution machines

The Bare Metal Solution servers that are certified for SAP applications are available only in Bare Metal Solution region extensions, which are not available for every Google Cloud region. For the full list of regions that have a Bare Metal Solution region extension, see [Bare Metal Solution regional availability](https://docs.cloud.google.com/bare-metal/docs/bms-planning#regional_availability).

### Images

When you create a Compute Engine VM, you use an image that contains the base components you require. For example, an image can contain a Microsoft Windows Server operating system with a SQL Server installation.

When you order a Bare Metal Solution machine, you also specify the operating system that you need. The machine becomes available with the operating system already installed.

For VMs, there are several ways that you can specify an image. You can:

  * Use the Terraform configuration file provided by Google Cloud, that is designed to make setting up SAP NetWeaver easier. For more information, see the SAP NetWeaver on Google Cloud deployment guide for your operating system.
  * Use a [public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage). Google provides a variety of public images. You must choose an image that contains components that are supported for SAP NetWeaver.
  * Create your own [custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images). You might want to set up your own base system from scratch and create a custom image that you can reuse. You can also create an image by [importing an existing boot disk](https://docs.cloud.google.com/compute/docs/images/import-existing-image) to Compute Engine.



#### Supported public images

Compute Engine provides public images for supported operating system versions in [image families](https://docs.cloud.google.com/compute/docs/images#image_families).

To see the available versions in each image family, see the operating system details:

  * [Red Hat Enterprise Linux (RHEL)](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel)
  * [SUSE Linux Enterprise Server (SLES)](https://docs.cloud.google.com/compute/docs/images/os-details#suse_linux_enterprise_server_sles)
  * [Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server)
  * [SQL Server Enterprise](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server)



For more information about the support status of the operating system versions that are certified for SAP, see [OS support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support).

#### Planning for image management

After your system is up and running, you can [create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images). Create custom images when you modify the state of your root persistent disk so you can easily restore the new state if needed. Plan for the management of the custom images you create. For more information, see [Image Management Best Practices](https://docs.cloud.google.com/solutions/image-management-best-practices).

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



### Deploying VMs

You can use the standard Google Cloud methods to deploy your VMs on Compute Engine: the Google Cloud console, the Google Cloud CLI, Terraform, and the [REST API](https://docs.cloud.google.com/compute/docs/reference/latest). The following guides provide generally useful information about how to deploy VMs:

  * [Creating and Starting an Instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * [Creating Windows Server Instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances)
  * [Creating SQL Server Instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)



For detailed information and instructions about deploying your SAP NetWeaver system on Compute Engine VMs, see the following:

  * [Overview of Linux deployment for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
  * [Overview of Windows deployment for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)



### Automation for SAP NetWeaver deployments

Google Cloud provides Terraform configuration files that you can use to automate the deployment of Google Cloud infrastructure for SAP NetWeaver with Linux.

The provided configuration file instantiate the following resources for SAP NetWeaver:

  * An instance of the machine type of your choice.
  * Your choice of the following operating systems: 
    * Red Hat Enterprise Linux (RHEL)
    * SUSE Linux Enterprise Server (SLES)
  * Persistent Disk or Hyperdisk volumes.
  * The XFS file system.



For automated deployment instructions, see:

  * [Terraform: Automated VM deployment for SAP NetWeaver on Linux](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-tf)
  * [Terraform: HA cluster configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf)
  * [Terraform: HA cluster configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel-tf)



#### Custom VMs and automated deployments

The Terraform configuration files provided by Google Cloud don't support the deployment of Compute Engine custom machine types.

If you need to use a custom machine type, then deploy an instance based on a small predefined machine type first and, after the deployment is complete, customize the instance as needed.

For more information about modifying compute instances, see [Modify compute instance configurations for SAP systems](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations).

### Accessing VMs

The creator of a VM has full root-privileges.

  * On a Linux-based VM, the creator has SSH capability and can use the Google Cloud console to grant SSH capability to other users.
  * On a Windows-based VM, the creator can use the Google Cloud console to generate a username and password; after that, anyone who knows the username and password can connect to the VM using RDP.



After a user with administrative privileges has connected to an instance through SSH or RDP, they can add other system users with standard Linux commands or Windows user-account management. The following pages provide generally useful information about connecting to Compute Engine VMs:

  * [Connecting to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools)
  * [Connecting to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)



If you use Linux instances, then you need to plan for how you use _SSH keys_. In general, Compute Engine manages SSH keys for you. You can decide to manage your own SSH keys, but you need to understand the associated risks. For details, see [SSH Keys](https://docs.cloud.google.com/compute/docs/instances/ssh-keys).

For details and instructions about how to connect to Compute Engine VMs in your SAP NetWeaver deployment, see the deployment guide for your operating system:

  * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-manual#connecting_to_your_vm)
  * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-manual#connecting_to_your_vm)



## Databases

You can use the following database management systems with SAP NetWeaver on Google Cloud:

  * SAP HANA on Linux.
  * SAP ASE on Linux or Windows.
  * SAP MaxDB on Linux or Windows.
  * IBM Db2 on Linux or Windows.
  * Microsoft SQL Server Enterprise on Windows.
  * Oracle Database 19c or later on Oracle Linux. For more information, see [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).
  * Oracle Database on Bare Metal Solution servers with operating systems that Bare Metal Solution supports for Oracle. For more information, see [Operating systems](https://docs.cloud.google.com/bare-metal/docs/bms-planning#operating_systems).



### SAP HANA

SAP HANA is certified to run in Google Cloud on the following Linux operating systems:

  * [Red Hat Enterprise Linux (RHEL) for SAP Solutions](https://access.redhat.com/solutions/3082481)
  * SUSE Linux Enterprise Server (SLES)
  * [SUSE Linux Enterprise Server (SLES) for SAP](https://www.suse.com/products/sles-for-sap/)



For more information on supported machine types and operating systems, see the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide).

For more information about SAP HANA, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide) and the [SAP documentation](https://help.sap.com/viewer/product/SAP_HANA_PLATFORM/2.0.00/en-US).

To determine the sizing guidelines and recommendations for SAP HANA, see the [SAP benchmark sizing](https://www.sap.com/about/benchmark/sizing.what-is-sizing.html#what-is-sizing) page.

### SAP ASE

SAP ASE on Google Cloud is supported on the following operating systems:

  * [SLES](https://www.suse.com/products/server/)
  * [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)
  * Windows Server



For more information on supported machine types and operating systems, see the [SAP ASE planning guide](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide).

To deploy SAP ASE with Linux on Google Cloud, see [Terraform: Automated VM deployment for SAP ASE on Linux](https://docs.cloud.google.com/sap/docs/sap-ase-deployment-linux-tf).

To deploy SAP ASE with Windows on Google Cloud, contact [Cloud Customer Care](https://cloud.google.com/support).

For information about SAP ASE from SAP, see the [SAP documentation](https://help.sap.com/viewer/product/SAP_ASE/latest).

### SAP MaxDB

SAP MaxDB on Google Cloud is supported on the following operating systems:

  * [SLES](https://www.suse.com/products/server/)
  * [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)
  * Windows Server



For more information on supported machine types and operating systems, see the [SAP MaxDB planning guide](https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide).

To deploy SAP MaxDB with Linux on Google Cloud, contact [Cloud Customer Care](https://cloud.google.com/support). {# TODO(lakshmang): once we have the TF config for MaxDB on Linux, update this sentence }

For information about SAP MaxDB from SAP, see the [SAP MaxDB Library](https://help.sap.com/viewer/9d62a6d2a95149718db6b65b7ffa2052/113/en-US).

### IBM Db2 for Linux, UNIX and Windows

IBM Db2 is supported on [SLES](https://www.suse.com/products/server/), [RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux), and Windows Server.

For information about supported machine types and operating systems, see the [IBM Db2 for SAP Planning Guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide).

To deploy IBM Db2 on Google Cloud, see:

  * [Automated VM deployment for IBM Db2 on Linux](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf)
  * [Manual VM deployment for IBM Db2 on Linux and Windows](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide)



For information about IBM Db2 from SAP, see [SAP on IBM Db2 for Linux, UNIX and Windows](https://help.sap.com/viewer/p/DB6).

### Microsoft SQL Server

You can install SQL Server in several ways:

  * You can use a public image provided by Google with SQL Server Enterprise. The SQL Server in Windows Server image is a [premium image](https://docs.cloud.google.com/compute/all-pricing#premium_images), which means that the image cost is bundled with the machine type cost.
  * You can download the SQL Server DVD from SAP, and use the SAP-specific script `SQL4SAP.bat` that installs SQL Server with the correct settings.
  * You can download the SQL Server DVD either from SAP or Microsoft and use the standard Microsoft `setup.exe` to install SQL Server so that you can customize your setup.



If you use SQL Server as your database, you must ensure that SQL Server is configured to use the SAP [collation](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support), `SQL_Latin1_General_CP850_BIN2`, for compatibility with SAP systems.

**Note:** If you are installing SQL Server through Microsoft, during the **Server Configuration** step, make sure you select the SAP collation. The **Collation** tab can be easy to miss.

You can confirm the collation of your SQL Server in your server properties:

![SQL Server dialog showing collation setting](https://docs.cloud.google.com/static/sap/docs/images/gcp-netweaver-sql-collation.png)

If you have already configured your SQL Server, then you can update the collation, but you need to recreate the databases afterwards. For more details on how to specify or change the collation, see the [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-windows-manual#configure-sql-server).

### Oracle Database

For use with SAP NetWeaver based applications, SAP has certified the use of Oracle Database 19c or later running on Oracle Linux. For more information, see [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).

For information about running Oracle Database with a highly-available SAP Central Services instance, see [Linux HA clustering software](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide#linux_ha_clustering_software).

### Oracle on Bare Metal Solution

SAP on Oracle is supported on Bare Metal Solution servers, which run in a regional extension that is co-located and connected to select Google Cloud regions.

For more information, see:

  * [Bare Metal Solution for Oracle](https://docs.cloud.google.com/bare-metal)
  * [SAP NetWeaver on Bare Metal Solution planning guide](https://docs.cloud.google.com/sap/docs/netweaver-on-bms-planning)



### Database backup and recovery

You must have a plan for how to restore your system to operating condition if the worst happens. For general guidance about how to plan for disaster recovery using Google Cloud, see:

  * [How to Design a Disaster Recovery Plan](https://docs.cloud.google.com/solutions/designing-a-disaster-recovery-plan)
  * [Disaster Recovery Cookbook](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook)



For information about SAP HANA backup and recovery, see the [SAP HANA on Google Cloud Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#backup_and_recovery).

For information about SAP ASE backup and recovery, see [SAP ASE Performance and Tuning Series: Physical Database Tuning](https://help.sap.com/viewer/2693691eb79c472481cabe88ec2d9867/latest/en-US/a9cc04c7bc2b1014be7ee05ff749e3d1.html).

For information about SAP MaxDB backup and recovery, see [SAP MaxDB Database Administration](https://help.sap.com/viewer/2c2effc99b6746019aeb1af52ad59f5d/114/en-US/1a32c42a0fcf40b5b95ff7040a60aa41.html).

For information about IBM Db2 backup and recovery, see [Backup and Recovery](https://help.sap.com/viewer/db6_admin/ab9e4c2d68364a80b654ab70d398464c.html).

As an alternative to native disaster recovery options, for cross-region active-passive disaster recovery (DR), you can use [PD Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about). PD Async Replication provides asynchronous replication of data between two Google Cloud regions.

## Storage

By default, each Compute Engine VM has a small [root persistent disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) that contains the operating system. You can add additional disks to your VMs to act as storage for the different components of your system.

### Persistent disk storage

For persistent block storage, you can attach Persistent Disk and Hyperdisk volumes to your Compute Engine VMs.

Compute Engine offers different types of Persistent Disk and Hyperdisk. Each type has different performance characteristics. Google Cloud manages the underlying hardware of these disks to ensure data redundancy, and to optimize performance.

With SAP NetWeaver, you can use any of the following Persistent Disk or Hyperdisk types:

  * **Persistent Disk types** : Standard (`pd-standard`), Balanced (`pd-balanced`), Performance or SSD (`pd-ssd`), and Extreme (`pd-extreme`) 
    * Standard Persistent Disk is backed by standard hard-disk drives (HDD). Disks of this type are efficient and economical for handling sequential read-write operations, but are not optimized to handle high rates of random input-output operations per second (IOPS).
    * Balanced, Performance or SSD (`pd-ssd`), and Extreme Persistent Disk types are backed by solid-state drives (SSD). These disk types provide cost-effective and reliable block storage.
    * Performance (SSD) Persistent Disk provides higher performance than Balanced Persistent Disk.
    * Balanced and Performance (SSD) Persistent Disk support PD Async Replication. You can use this feature for cross-region active-passive disaster recovery. For more information, see [PD Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).
    * While you can use Extreme Persistent Disk (`pd-extreme`) with your SAP applications, we recommend that you instead use Hyperdisk volumes, which provide greater performance. For information about the machine types that support using Extreme Persistent Disk, see [Machine shape support](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#machine_shape_support).
  * **Hyperdisk types** : Hyperdisk Balanced (`hyperdisk-balanced`) and Hyperdisk Extreme (`hyperdisk-extreme`) 
    * Hyperdisk Extreme provides higher maximum IOPS and throughput options than Persistent Disk types.
    * For Hyperdisk Extreme, you select the performance you need by provisioning IOPS, which also determines your throughput. For more information, see [Size and performance limits for Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
    * For Hyperdisk Balanced, you select the performance you need by provisioning IOPS and throughput. For more information, see [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
    * For information about the machine types that support using Hyperdisk, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).

The performance of SSD and Balanced Persistent Disk volumes scale automatically with size. Therefore, you can adjust performance by resizing your existing Persistent Disk volumes or adding more Persistent Disk volumes to a VM. The performance of Extreme Persistent Disk volumes is not affected by size. 

The type of VM you are using and the number of vCPUs it contains can also affect or limit persistent disk performance.

The following figure shows approximate performance numbers for Balanced Persistent Disk volumes in an example SAP NetWeaver configuration on Google Cloud. The actual numbers you might see in a similar configuration are likely to differ for a variety of reasons, including improvements made by Compute Engine over time.

![Two balanced persistent disks, one 80 GB and the other 250 GB, are attached
to an n2-standard-32 host VM that is running SAP NetWeaver](https://docs.cloud.google.com/static/sap/docs/images/netweaver-pd-architecture.png)

As indicated in the preceding figure, when the Persistent Disk volumes are of the same type, such as SSD or Balanced, then the performance that they provide to the VM is cumulative. Therefore, you can estimate the overall performance by adding the performance numbers of each Persistent Disk volume.

For example, if you attach two Balanced Persistent Disk volumes as shown in the figure, one that provides 180 IOPS for read and write, and throughput of 8.4 MB per second, and the other that provides 1,500 IOPS for reads and writes and 70 MB per second of throughput, then together the two Balanced Persistent Disk volumes provide 1,680 IOPS for reads and writes and 78.4 MB per second of throughput. For more information, see the "Multiple disks attached to a single VM instance" and "Simultaneous reads and writes" sections in [Factors that affect Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors).

**Note:** Disk size, machine type memory, and network usage are calculated in gigabytes (GB), where 1 GB is 230 bytes. This unit of measurement is also known as a [gibibyte (GiB)](https://wikipedia.org/wiki/Gibibyte).

Persistent Disk and Hyperdisk volumes are located independently from your VMs, so you can detach or move the disks to keep your data, even after you delete your VMs.

In the [VM instances](https://console.cloud.google.com/compute/instances) page of the Google Cloud console, you can see the disks that are attached to your VM instances under **Additional disks** on the **VM instance details** page for each VM instance.

For more information about the different types of block storage offered by Compute Engine, their performance characteristics, and how to work with them, see the Compute Engine documentation:

  * [Storage options](https://docs.cloud.google.com/compute/docs/disks)
  * [About Google Cloud Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance)
  * [Other factors that affect performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors)
  * [Adding or resizing zonal persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Creating persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)



#### Persistent disks deployed by the deployment templates

If you deploy the host VM by using the Terraform configuration files that Google Cloud provides for SAP NetWeaver, then the deployment automation scripts attach two or three Persistent Disk or Hyperdisk volumes for the required SAP NetWeaver volumes or drives, depending on whether you are using Windows Server or Linux.

### File sharing solutions

Several file sharing solutions are available on Google Cloud, including the following:

  * Filestore
  * NetApp Cloud Volumes ONTAP
  * Google Cloud NetApp Volumes



To determine which solution is best for your deployment scenario, see [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap).

### Local SSD (non-persistent)

Google Cloud offers [local SSD](https://docs.cloud.google.com/compute/docs/disks#localssds) disk drives. Although local SSDs can offer some advantages over persistent disks, don't use them as part of an SAP NetWeaver system. VM instances with local SSDs attached cannot be stopped and then restarted.

### Using Cloud Storage for object storage

Cloud Storage is an object store for files of any type or format; it has virtually unlimited storage, and you do not have to worry about provisioning it or adding more capacity. An [object](https://docs.cloud.google.com/storage/docs/objects) in Cloud Storage contains file data and its associated metadata, and can be up to 5 terabytes in size. A Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/buckets) can store any number of objects.

It's common practice to use Cloud Storage to store backup files for nearly any purpose. For example, for SAP HANA backups, Cloud Storage is a good place to store the files. For database backup planning, refer to the resources in Database backup and recovery. You can also use Cloud Storage as part of a migration process.

Choose your Cloud Storage option based on how frequently you need to access the data. For frequent access multiple times a month, select the Standard storage class. For infrequent access, select Nearline or Coldline storage. For archival data you don't expect to access, select Archive storage.

When you plan your storage options, start with the frequently accessed tier and age your backup data to the infrequent access tiers, because backups are rarely used as they become older. The probability of needing a backup that is 3 years old is extremely low, and you can age this backup into the Archive tier to optimize costs.

For a more detailed comparison, see [Storage Classes](https://docs.cloud.google.com/storage/docs/storage-classes).

## User identification and resource access

When planning security for an SAP deployment on Google Cloud, you must identify:

  * The user accounts and applications that need access to the Google Cloud resources in your Google Cloud project
  * The specific Google Cloud resources in your project that each user needs to access



You must add each user to your project by adding their Google account ID to the project as a principal. For an application program that uses Google Cloud resources, you create a _service account_ , which provides a user identity for the program within your project.

Compute Engine VMs have their own service account. Any programs that run on a VM can use the VM service account, as long as the VM service account has the resource permissions that the program needs.

After you identify the Google Cloud resources that each user needs to use, you grant each user permission to use each resource by assigning resource-specific roles to the user. Review the predefined roles that IAM provides for each resource, and assign roles to each user that provide just enough permissions to complete the user's tasks or functions and no more.

If you need more granular or restrictive control over permissions than the predefined IAM roles provide, you can create custom roles.

For more information about the IAM roles that SAP programs need on Google Cloud, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).

For an overview of identity and access management for SAP on Google Cloud, see [Identity and access management overview for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap).

## Networking and network security

Consider the information in the following sections when planning networking and network security.

### Minimum privilege model

One of your first lines of defense is to restrict who can reach your network and your VMs by using [firewalls](https://docs.cloud.google.com/compute/docs/vpc/firewalls). By default, all traffic to VMs, even from other VMs, is blocked by the firewall unless you create rules to allow access. The exception is the `default` network that is created automatically with each project and has default [firewall rules](https://docs.cloud.google.com/compute/docs/networking#firewall_rules).

By creating firewall rules, you can restrict all traffic on a given set of ports to specific source IP addresses. Follow the minimum privilege model in order to restrict access to the specific IP addresses, protocols, and ports that need access. For example, always set up a bastion host and allow SSH into your SAP NetWeaver system only from that host.

### Custom networks and firewall rules

You can use a network to define a gateway IP and the network range for the VMs attached to that network. All Compute Engine networks use the [IPv4](https://tools.ietf.org/html/rfc791) protocol. Every Google Cloud project is provided with a default network with preset configurations and firewall rules, but you should add a custom subnetwork and add firewall rules based on a minimum privilege model. By default, a newly created network has no firewall rules and hence no network access.

You might want to add more than one subnetwork, if you want to isolate parts of your network, and depending on your requirements. For more information, see [Subnetworks](https://docs.cloud.google.com/compute/docs/vpc#vpc_networks_and_subnets).

The firewall rules apply to the entire network and all the VMs in the network. You can add a firewall rule that allows traffic between VMs in the same network and across subnetworks. You can also configure firewalls to apply to specific target VMs by using the [tagging mechanism](https://docs.cloud.google.com/compute/docs/vpc/add-remove-network-tags).

SAP requires access to certain ports, so add firewall rules to allow access to [the ports outlined by SAP](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).

### Routes

[Routes](https://docs.cloud.google.com/compute/docs/vpc/routes) are global resources attached to a single network. User-created routes apply to all VMs in a network. This means you can add a route that forwards traffic from VM to VM within the same network and across subnetworks without requiring external IP addresses.

For external access to internet resources, launch a VM with no external IP address and configure another virtual machine as a NAT gateway. This configuration requires you to add your NAT gateway as a route for your SAP instance.

### Using bastion hosts and NAT gateways

If your security policy requires truly internal VMs, you need to set up a NAT proxy manually on your network and a corresponding route so that VMs can reach the internet. It is important to note that you cannot connect to a fully internal VM instance directly by using SSH. To connect to such internal machines, you must set up a _bastion_ instance that has an external IP address and then tunnel through it. When VMs do not have external IP addresses, they can only be reached by other VMs on the network, or through a managed VPN gateway. You can provision VMs in your network to act as trusted relays for inbound connections, called _bastion hosts_ , or network egress, called _NAT gateways_. For more transparent connectivity without setting up such connections, you can use a managed VPN gateway resource.

#### Using bastion hosts for inbound connections

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private-network VMs. This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH communication from the internet.

![Bastion host show in SSH scenario](https://docs.cloud.google.com/static/solutions/images/bastion.png)

SSH access to VMs that do not have an external IP address can be achieved by first connecting to a bastion host. A complete hardening of a bastion host is outside the scope of this article, but some initial steps taken can include:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private VMs from only the bastion host.



By default, SSH on VMs is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private VM. Due to this two-step login, you should use SSH-agent forwarding to reach the target VM instead of storing the target VM's private key on the bastion host. You must do this even if you are using the same key-pair for both bastion and target VMs, as the bastion has direct access only to the public half of the key-pair.

#### Using NAT gateways for traffic egress

When a VM does not have an assigned, external IP address, it cannot make direct connections to external services, including other Google Cloud services. To allow these VMs to reach services on the internet, you can set up and configure a [NAT gateway](https://docs.cloud.google.com/compute/docs/vpc/special-configurations#natgateway). The NAT gateway is a VM that can route traffic on behalf of any other VM on the network. Use one NAT gateway per network. A single-VM NAT gateway is not highly available and cannot support high traffic throughput for multiple VMs. For instructions on how to set up a VM to act as a NAT gateway, see the NetWeaver Deployment Guide for your operating system:

  * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
  * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)



### Cloud VPN

You can securely connect your existing network to Google Cloud through a [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection that uses [IPsec](https://wikipedia.org/wiki/IPsec) by using Cloud VPN. Traffic traveling between the two networks is encrypted by one VPN gateway, then decrypted by the other VPN gateway. This protects your data as it travels over the internet. You can dynamically control which VMs can send traffic down the VPN using [instance tags on routes](https://docs.cloud.google.com/compute/docs/vpc/using-routes#addingroute). Cloud VPN tunnels are billed at a static monthly rate plus standard egress charges. Note that connecting two networks in the same project still incurs standard egress charges. For more information, see:

  * [The VPN Overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Choosing a VPN Routing Option](https://docs.cloud.google.com/network-connectivity/docs/how-to/how-to-choose#cloud-vpn)



### Securing a Cloud Storage bucket

If you use Cloud Storage to host your backups for your data and log, make sure you use TLS (HTTPS) while sending data to Cloud Storage from your VMs to protect data in transit. Cloud Storage automatically encrypts data at rest. You can specify your own encryption keys if you have your own key-management system.

### Sending email

To help protect your systems and Google's from abuse, Google Cloud enforces limitations for sending email from Compute Engine. For more information, see [Sending email from an instance](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail).

### Related security documents

Refer to the following additional security resources for your SAP environment on Google Cloud:

  * [Securely Connecting to VM Instances](https://cloud.google.com/solutions/connecting-securely)
  * [Security Center](https://cloud.google.com/security/)
  * [Compliance in the Google Cloud](https://cloud.google.com/security/compliance)
  * [Google Cloud security whitepaper](https://cloud.google.com/security/whitepaper)
  * [Google Infrastructure security design](https://cloud.google.com/security/security-design/resources/google_infrastructure_whitepaper_fa.pdf)



## Monitoring

For support and monitoring, Google Cloud provides the _Agent for SAP_ , for SAP workloads running on Compute Engine instances and Bare Metal Solution servers.

As mandated by SAP, to get support from SAP and to enable SAP to meet its service-level agreements (SLAs), you must install Google Cloud's Agent for SAP on all Compute Engine instances and Bare Metal Solution servers that run any SAP system. For more information on the support prerequisites, see [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

**Version 3.15 (latest)** of Google Cloud's Agent for SAP is the successor of Google Cloud's monitoring agent for SAP NetWeaver version 2, monitoring agent for SAP HANA version 2, and the Cloud Storage Backint agent for SAP HANA. Therefore, in addition to the collection of metrics, version 3.15 (latest) of Google Cloud's Agent for SAP includes the optional feature: _Backint based backup and recovery for SAP HANA_.

You can opt in to these features that enable products and services such as [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) for your SAP workloads.

**Note:** SAP Host Agent, with the `saposcol program`, is required on any host that is running an SAP system. SAP Host Agent is installed automatically during the installation of new SAP system instances with SAP kernel 7.20 or higher. For more information, see [SAP Host Agent](https://help.sap.com/docs/SAP%20Host%20Agent/8661d17ee5c047a887f686b33e990ede/e817cfb89dbc4d799825c94da59c7867.html).

You install Google Cloud's Agent for SAP on the host alongside the SAP system. For instructions about how to install and configure the agent, validate your installation, and verify that the agent is running as expected, see [Install the agent on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). 

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



## Scale-out of SAP NetWeaver application servers

SAP supports a scale-out architecture that uses multiple application servers, which supports a higher workload.

If you are using Windows Server as your operating system, you can use Active Directory running on a VM as a domain controller. For more information, see [Setting up Active Directory on Google Compute Engine](https://docs.cloud.google.com/compute/docs/tutorials/setup-active-directory). Alternatively, you can connect Compute Engine VMs to your on-premises Active Directory domain controller using VPN.

In scale-out configuration, nodes must access a shared file system. For Windows Server, specify where the shared file system is mounted during installation through the SAP installer. For Linux, use the Network File System (NFS) as your fileshare on the NetWeaver binaries/profiles disk of the central system (`/sapmnt/[SID]`, where `[SID]` is the system ID). See [the SAP documentation](https://help.sap.com/saphelp_nwpi711/helpdata/en/27/44f17a26a74a8abfd202c4f5dc9a0f/frameset.htm) for details.

For information about the file sharing solutions available on Google Cloud for SAP NetWeaver, see File sharing solutions.

## Migrating an existing SAP NetWeaver system

By migrating an existing SAP NetWeaver landscape, you can leverage your investment in your existing setup in the cloud. Migrating a system of any significant scale requires careful planning and step-by-step migration, to avoid losing consistency between the system components.

For migrations, follow SAP standard migration practices. SAP recommends [following their best practices](https://wiki.scn.sap.com/wiki/display/SL/System+Copy+and+Migration) for copying components from your source system to a newly created target system. When the source and target systems use the same OS and database system, use _homogeneous system copy_ , and when the source and target systems use a different OS or database system, use _heterogeneous system copy_.

## Licensing

This section provides information about licensing requirements.

### SAP Licensing

Running SAP on Google Cloud requires you to bring your own license (BYOL).

**Note:** After you deploy SAP NetWeaver on Google Cloud, you must install your permanent SAP NetWeaver license before the temporary license for SAP NetWeaver expires.

See the following SAP notes:

  * [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441)
  * [2456953 - Windows on Google Cloud Platform (IaaS): Adaptation of your SAP License](https://me.sap.com/notes/2456953)



For more information from SAP about managing your SAP NetWeaver licenses, see [SAP Licensing Procedure](https://help.sap.com/viewer/0643d547dfad4ce497bd7da1264fce77/7.5.6/en-US/fbde4502adef496988fe13d459d66b8b.html).

### Microsoft Windows Server and SQL Server

In Compute Engine, there are two ways to license Microsoft software:

  * With pay-as-you-go licensing, your Compute Engine VM hourly cost includes licensing. Google manages the licensing logistics with Microsoft. Your hourly costs are higher, but you have complete flexibility to increase and decrease your costs, as needed. This is the licensing model used for Google Cloud public images that include Windows Server, with or without SQL Server.

**Important** : Windows Server and SQL Server are premium images. and all prices for premium images are in addition to charges for using a machine type. Refer to [Premium images](https://docs.cloud.google.com/compute/pricing#premiumimages) for details on pricing.
  * With BYOL, your Compute Engine VM costs are lower because the licensing isn't included. You must migrate an existing license or purchase your own license, which means paying up front, and you have less flexibility. However, with very stable usage needs, or with no-charge or discounted licensing through Microsoft licensing agreements, this approach might be less expensive.




Microsoft's terms for migrating licenses are different for Windows Server and SQL Server. For full details about BYOL on Google Cloud, see [Using Existing Microsoft Application Licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing).

For information about SAP license restrictions for SQL Server, see the SAP note [2139358 - Effect of changes in licensing terms of SQL Server](https://launchpad.support.sap.com/#/notes/2139358).

### Linux

In Compute Engine, there are two ways to license SLES or RHEL:

  * With pay-as-you-go licensing, your Compute Engine VM hourly cost includes licensing. Google manages the licensing logistics. Your hourly costs are higher, but you have complete flexibility to increase and decrease your costs, as needed. This is the licensing model used for Google Cloud public images that include SLES or RHEL.

**Important** : SLES and RHEL are premium images, and all prices for premium images are in addition to charges for using a machine type. Refer to [Premium images](https://docs.cloud.google.com/compute/pricing#premiumimages) for details on pricing.

  * With BYOL, your Compute Engine VM costs are lower because the licensing isn't included. You must migrate an existing license or purchase your own license, which means paying up front, and you have less flexibility.




## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



## What's next

  * To complete the tasks necessary for deployment, see the NetWeaver Deployment Guide for your operating system:

    * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
    * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)
  * For an overview of high-availability SAP NetWeaver systems on Google Cloud, see [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide).

  * For an overview of disaster recovery options for SAP NetWeaver systems on Google Cloud, see [Disaster recovery planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-dr-on-gcp).

  * For more details on administration of VMs and monitoring, see the [SAP NetWeaver on Google Cloud Operations Guide](https://docs.cloud.google.com/sap/docs/netweaver-operations-guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
