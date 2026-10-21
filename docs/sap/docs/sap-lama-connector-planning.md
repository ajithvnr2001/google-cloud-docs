---
url: https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning/
title: Connector for SAP Landscape Management planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:39.381321+00:00
---

# Connector for SAP Landscape Management planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Connector for SAP Landscape Management planning guide Stay organized with collections  Save and categorize content based on your preferences. 

You can manage your SAP system landscape on Google Cloud with [SAP Landscape Management, Enterprise Edition (SAP Landscape Management)](https://www.sap.com/products/landscape-management.html) by installing the Google Cloud Connector for SAP Landscape Management (Connector for LaMa).

Google Cloud provides the Connector for LaMa free of charge. You must obtain all licenses that are required for SAP Landscape Management from SAP.

Installing the Connector for LaMa enables a Cloud Manager function for Google Cloud in SAP Landscape Management.

This guide does not include instructions for installing, configuring, or operating SAP Landscape Management. For information about installing and configuring SAP Landscape Management, see the latest SAP documentation in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_MANAGEMENT_ENTERPRISE).

For information from SAP about configuration and support of the Connector for LaMa, see [SAP Note 3078321](https://launchpad.support.sap.com/#/notes/3078321).

## Operations that Connector for LaMa enables

Installing the Connector for LaMa enables the following SAP SAP Landscape Management operations on Google Cloud.

### SAP System and Instance Operations

The Cloud Manager function for Google Cloud supports the following SAP Landscape Management operations at the SAP system or SAP instance level:

  * SAP System/Instance prepare, unprepare
  * SAP System/Instance relocation
  * SAP System start, stop including virtual hosts



### SAP System Provisioning Scenarios

The cloud manager supports the following SAP Landscape Management scenarios for system Provisioning:

  * SAP System Clone and System Copy 
    * Storage-based copy procedure, which are based on snapshots of Compute Engine persistent disks
  * SAP System Refresh and Database Refresh 
    * Storage-based copy procedure, which are based on snapshots of Compute Engine persistent disks



### Creating SAP HANA System Replication Tiers

The cloud manager supports the following SAP Landscape Management scenarios for SAP HANA system replication tiers:

  * Storage-based copy procedure, which are based on snapshots of Compute Engine persistent disks



## Architecture

The following diagram shows the high-level architecture of SAP Landscape Management on Google Cloud.

![SAP Landscape Management is installed on a server and connects to the managed
landscape over the network. Systems and hosts on Google Cloud
are managed directly and through Google Cloud APIs. Storage is
managed through APIs only.](https://docs.cloud.google.com/static/sap/docs/images/lama-on-gc-architecture.svg)

The following diagram illustrates the SAP and Google Cloud software that is required on a managed virtual host, as well as the types of SAP applications that can be managed.

![Required software on a managed virtual host includes SAP Host Agent
components sapacosprep, database library, custom exit, and platform library;
SAP Adaptive Extenstions component HANA operations; Connector for LaMa
components storage library and platform library. Types of managed applications
include SAP NetWeaver ABAP or Java applications, SAP HANA, and custom
applications](https://docs.cloud.google.com/static/sap/docs/images/lama-managed-host-detail.svg)

## Software requirements

The following sections list the SAP Landscape Management, SAP NetWeaver, and Google Cloud software that is required for managing SAP landscapes on Google Cloud.

When you evaluate the software requirements for the Connector for LaMa, you need to consider the requirements of SAP Landscape Management, the Connector for LaMa, and the managed systems.

### SAP software requirements

Software | Requirements  
---|---  
SAP Landscape Management | Enterprise Edition, 3.0 Support Package (SP) 15 or later.  
SAP NetWeaver Application Server for Java | 7.50 SP 15 or later.  
SAP Host Agent | 7.21 PL51 or later.  
[Support for duplicate IP addresses](https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment#c4lm_duplicate_ip_address) requires version 7.21 PL54 or later.  
  
For more information, see the SAP documentation (You need an SAP user account to access SAP Notes.):  


  * [SAP Note 2219592 - Upgrade Strategy of SAP Host Agent](https://launchpad.support.sap.com/#/notes/2219592)
  * [SAP Note 2659101 - SAP HostAgent versions with SAP Landscape Management](https://launchpad.support.sap.com/#/notes/2659101)

  
SAP Adaptive Extension | S1.0 EXT PL61 or later.  
[Support for duplicate IP addresses](https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment#c4lm_duplicate_ip_address) requires version S1.0 EXT PL65 or later.  
  
For more information, see the SAP documentation:  


  * [SAP Adaptive Extensions documentation](https://help.sap.com/viewer/p/SAP_ADAPTIVE_EXTENSIONS)
  * [SAP note 1759181 - Installation of SAPACEXT.SAR](https://launchpad.support.sap.com/#/notes/1759181)
  * [SAP note 1808793 - SAP Adaptive Extension Improvements and Fixes](https://launchpad.support.sap.com/#/notes/1808793)

  
  
### Connector for LaMa software requirements

Software | Requirements  
---|---  
Connector for LaMa | Version 2.3.0 or later.  
Operation definitions and scripts |  For Linux, Connector for LaMa version 2.3.0 or later. For Windows, Connector for LaMa version 2.3.0 or later.  The Connector for LaMa download package includes two operation definitions, `AcActivateIP` and `AcDeactivateIP`, with corresponding scripts.  The operation definitions and scripts are SAP Host Agent components that enable SAP Landscape Management to activate and deactivate Virtual IP addresses in alias IP ranges in the local OS. The alias IPs and logical host names are core elements of SAP Adaptive Design.  The operation definitions and scripts must be installed on each VM that is managed by SAP Landscape Management.   
OS storage libraries for sapacosprep |  For Linux, Connector for LaMa version 2.3.0 or later. For Windows, Connector for LaMa version 2.3.0 or later.  The Connector for LaMa download package includes a storage library, which is an extension of the SAP Host Agent that enables SAP Landscape Management to trigger OS-level storage operations in VM instances on Google Cloud.  The storage library needs to be deployed on each Compute Engine virtual machine (VM) that is managed by SAP Landscape Management.   
  
### Managed SAP landscape requirements

In the SAP landscape that you manage, the software and infrastructure must meet certain requirements.

#### Managed Google Cloud resources

The Connector for LaMa currently supports the following combinations of managed resources on Google Cloud.

To see current restrictions for the management of Google Cloud resources by SAP Landscape Management, see the section for supported scenarios or known limitations.

Resource | Description  
---|---  
VM instances |  Compute Engine VM instances that are supported by SAP.  For the list of supported VM types, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).  For VM types that are certified by SAP for SAP HANA, see [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).   
Operating systems | 

  * Linux 
    * Red Hat Enterprise Linux (RHEL) for SAP 7.7, 7.9, 8.1, 8.2, 8.4, 8.6
    * SUSE Linux Enterprise Server (SLES) for SAP 12 SP5, SLES for SAP 15 SP1 and SP2
  * Windows Server 
    * 2019, Datacenter edition
    * 2016, Datacenter edition

  
Storage |  Compute Engine Zonal Persistent disks (Standard and SSD): 

  * Direct mounted PD (without OS level LVM and no partitioning)
  * Direct mounted PD (without OS level LVM and with partitioning)
  * Managed by OS level LVM (Only one Logical Volume per Volume Group is supported)
  * The storage layout should follow the SAP Adaptive Design principle to support the SAP Landscape Management scenarios involving operations on storage level.

For more information about Compute Engine persistent disks, see [Persistent disks](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).  NFS based Storage: 

  * SAP Landscape Management can manage only: 
    * Local NFS servers that are hosted on the same VM as a Central Services instance. For more information, see [SAP Note 2628497 - Mount SAN volumes via NFS in SAP Landscape Management](https://launchpad.support.sap.com/#/notes/2628497)
    * Client mount operations for NFS storage that is provided services like those listed in [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap)

For information about restrictions that are related to SAP Landscape Management storage operations on Google Cloud, see Known Issues and Limitations.   
  
#### Managed SAP resources

Resource | Requirements  
---|---  
SAP NetWeaver based Systems | SAP NetWeaver ABAP or JAVA:  


  * RHEL for SAP 7.7, 7.9, 8.1, 8.2, 8.4
  * SLES for SAP 12 SP5, SLES for SAP 15 SP1 and SP2
  * Windows Server Datacenter Edition 2019, 2016

  
Database Servers | SAP ASE: 

  * RHEL for SAP 7.7, 7.9, 8.1, 8.2, 8.4
  * SLES for SAP 12 SP5, SLES for SAP 15 SP1 and SP2
  * Windows Server Datacenter Edition 2019, 2016

SAP HANA: 

  * RHEL for SAP 7.7, 7.9, 8.1, 8.2, 8.4
  * SLES for SAP 12 SP5, SLES for SAP 15 SP1 and SP2
  * Running on dedicated database VMs

  
  
#### Recommendations for managed resources

Deployment recommendations:

  * Deploy SAP systems to be managed by SAP Landscape Management in accordance with SAP adaptive design or enablement principles. For more information, see: 
    * [SAP Adaptive Design](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/3.0.15.0/en-US/737a99e86f8743bdb8d1f6cf4b862c79.html)
    * [SAP Landscape Management, Enterprise Edition, Provisioning and Adaptive Design Principles](https://www.sap.com/documents/2021/07/c840f2a9-eb7d-0010-bca6-c68f7e60039b.html)
  * Run SAP systems that are managed by SAP Landscape Management on Compute Engine VM instances that are certified by SAP. See: 
    * [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps)
    * [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana)
  * Run SAP HANA databases on dedicated VMs.



Network Recommendations:

  * Install each SAP and database instance by using a logical hostname with a dedicated virtual IP address (VIP).
  * Virtual hostnames can be resolved to VIPs for Forward and Reverse lookup.
  * DNS requires A (address) records. CNAME records are not supported.
  * VIPs are based on Google Cloud alias IP ranges and can be bonded to a network interface on any VM instance within a given region.
  * VIPs must be activated in the OS on the primary network interface.
  * Google Cloud provides the operation definitions, `AcActivateIP` and `AcDeactivateIP`, to handle IPs in the OS.



Storage and mount point configuration:

  * Configure mount points that contain the data of an SAP system or database instance only for that system or instance. Do not share the mount points with any other system on the same VM.
  * Configure mount points to support the SAP Landscape Management scenarios for Prepare, Unprepare, and Relocation.



For more information, see the SAP Landscape Management documentation:

  * [Instance Operations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/4c981257691646b6934bf391b0c81300.html)
  * [System Operations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/0ea7b909d53b42608fc246cf60912f09.html)



## Authentication and access control for the Connector for LaMa

Google Cloud uses [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to identify programs like the Connector for LaMa and to control which Google Cloud resources the programs can access.

The Connector for LaMa and, by extension, SAP Landscape Management use a service account to operate within the Google Cloud environment. The Google Cloud resources that SAP Landscape Management can operate on are determined by the permissions that are granted to one or more roles that are assigned to the service account.

### Required permissions for the Connector for LaMa

The service account that the Connector for LaMa uses must be granted permissions to the Google Cloud resources that the Connector for LaMa accesses.

Depending on the actions that you perform with Connector for LaMa, the minimum permissions that you grant to the service account might be different.

The `Compute Admin` predefined IAM role and the Compute Engine default service account for VMs each contain all of the permissions that the Connector for LaMa requires, but each also contains additional permissions that Connector for LaMa doesn't need.

For the strictest access control, [create a separate, dedicated service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for the Connector for LaMa and grant the service account only the minimum permissions that are required to perform the actions that you need SAP Landscape Management to perform.

For a list of permissions that Connector for LaMa requires, see Required IAM resource permissions for the Connector for LaMa.

### Service account options for the Connector for LaMa

If the Connector for LaMa is installed on a Compute Engine VM, by default, the Connector for LaMa uses the service account of the VM.

If you use the VM service account, the Connector for LaMa has the same project-level permissions as all of the other programs and processes that use the VM service account.

If SAP Landscape Management is not running on a Compute Engine VM, you must [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for the Connector for LaMa.

Create service accounts for Connector for LaMa in the Google Cloud project that contains the SAP systems that SAP Landscape Management manages.

When you create a dedicated service account for the Connector for LaMa, you also need to [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). You copy and paste the key file contents into SAP Landscape Management when you configure the Cloud Manager for Google Cloud functionality.

When using a dedicated service account for the Connector for LaMa, rotate your keys regularly as a best practice to protect against unauthorized access.

### More information about IAM

For more information about IAM service accounts, roles, and permissions, and how they are used with Compute Engine VMs, see:

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Understanding IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [Service accounts on Compute Engine VMs](https://docs.cloud.google.com/compute/docs/access/service-accounts)
  * [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)



## Meaning of SAP Landscape Management terms for Google Cloud

The following table maps terms that are used in the SAP Landscape Management interface to their meaning on Google Cloud.

SAP Landscape Management term | Google Cloud meaning  
---|---  
Cloud Manager | Google Cloud  
Project Pool | Google Cloud Project  
Zone Pool | Google Cloud Zone  
Virtual Host | Compute Engine VM instance  
Virtual Disk | Compute Engine Persistent Disk  
  
## Supported SAP Landscape Management Scenarios and Operations

The following sections describe the SAP Landscape Management scenarios and operations that are supported in the Google Cloud environment.

### Instance, system, and host operations

On Google Cloud, you can perform the following SAP instance, SAP system, and Compute Engine VM operations with SAP Landscape Management:

Action | SAP Landscape Management operation  
---|---  
SAP System / SAP Instance Start including Prepare | 

  * Preparing Systems and Instances.
  * Starting Including Preparing Systems and Instances.

  
SAP System / SAP Instance Stop including Unprepare | 

  * Stopping and Unpreparing Systems and Instances.
  * Unpreparing Systems and Instances.

  
Starting Systems and VM Hosts | 

  * Starting systems and VM hosts using the Cloud Operations Optimizer Workflow for Start System and Virtual Host.
  * For more information, see Virtual Host Management Operations.

  
Stopping Systems and VM Hosts  | 

  * Stopping systems and VM hosts using the Cloud Operations Optimizer Workflow for Stop System and Virtual Host.
  * For more information, see Virtual Host Management Operations.

  
SAP Application Instance Relocation | 

  * Relocating Not Running Systems and Instances.
  * Relocating Running Systems and Instances.

  
SAP Central Instance and Database Relocation | 

  * Relocating Not Running Systems and Instances.
  * Relocating Running Systems and Instances.

  
Virtual Host Operations | For more information, see Virtual Host Management Operations.  
  
For details about how to configure and execute the operations and for further prerequisites, see the SAP Landscape Management documentation:

  * [Instance Operations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/4c981257691646b6934bf391b0c81300.html)
  * [System Operations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/0ea7b909d53b42608fc246cf60912f09.html)



### System provisioning

The following tables describes the supported system provisioning scenarios that you can use SAP Landscape Management for on Google Cloud.

To deploy new VMs with SAP Landscape Management, you first need to create Compute Engine VM instance templates.

The image that you use for the instance template must include an installed and configured SAP Host Agent with all additional components, like the storage library and operation definitions and scripts.

For more information about creating instance templates, see [Creating instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

System provisioning type | Supported scenario  
---|---  
SAP System Clone by using Compute Engine snapshots | 

  * You can clone a SAP system to create a duplicate without renaming it or performing any post processing.
  * The procedure is a storage-based copy procedure that is based on persistent disk snapshots
  * You can using existing VMs as the target or you can deploy new VMs during the process by using Compute Engine instance templates.

  
SAP System Copy | 

  * You can copy an SAP system to create a renamed, duplicate system and perform post processing.
  * The procedure is a storage-based copy procedure that is based on persistent disk snapshots.
  * You can using existing VMs as the target or you can deploy new VMs during the process by using Compute Engine instance templates.

  
SAP System Refresh | 

  * You can refresh an existing SAP system with data from a source system while maintaining the configuration.
  * The procedure is a storage-based copy procedure that is based on persistent disk snapshots.
  * The target VMs must already exist.
  * The mount points and storage volumes that contain the database logs, data, and software can only be used for the database instance and cannot be shared with any other instance or database.

  
SAP Database Refresh | 

  * You can refresh an existing SAP database while keeping the application instance configuration.
  * Storage based copy procedure.
  * The target VMs and application instances already exist.
  * The mount points and storage volumes that contain the database logs, data, and software can only be used for the database instance and cannot be shared with any other instance or database.

  
  
For an overview of the SAP Landscape Management system provisioning concepts, see the SAP Landscape Management documentation:

  * [System Provisioning Concepts](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/a2add4362c6c4ea3b06687a91ca7ebeb.html)
  * [General Prerequisites for Provisioning Systems](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/04f0d35e9c854881abc1af8084603c45.html)



For scenario specific prerequisites and requirements and for details how to configure and execute the provisioning scenarios, see the following SAP Landscape Management documentation:

  * [Cloning a System](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/e838481cc426498f8f799ef6591c423e.html)
  * [Copying a System](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/13b478e67f194810800edb3cce67ad6c.html)
  * [Refreshing a System](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/5eb30aa708c943299c109c289f6a3dc0.html)
  * [Refreshing a Database](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/ad3afa80090a4e7a83203a565b4c9e2e.html)



### Creating SAP HANA System Replication tiers

You can use SAP Landscape Management to create SAP HANA System Replication tiers subject to the following supported scenario:

  * Copy of an original SAP HANA system to create a system replication tier for HANA system replication.
  * Storage based copy procedure.
  * Target VMs already existing.
  * Mount points and storage volumes containing the database logs, data, and software are only used for the database instance and not be shared with any other instance or database.



### Virtual Host Management Operations

On Google Cloud you can perform the following SAP Landscape Management virtual host management operations:

SAP Landscape Management operation | Google Cloud action  
---|---  
Activate | Start a VM instance. Equivalent to issuing the `gcloud` command `gcloud compute instances start`. For more information, see [Stopping and starting an instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).  
Deactivate (Power off) | Stop a VM instance. Equivalent to issuing the `gcloud` command `gcloud compute instances stop`. For more information, see [Stopping and starting an instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).  
Resize | Change the Compute Engine machin type. Equivalent to issuing the `gcloud` command `gcloud compute instances set-machine-type`. For more information, see [Changing the machine type of an instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).  
  
For details how to configure and execute the operations and for further prerequisites, see [Virtual Element Operations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-us/804dd796d4aa4ca7919c378f0880abfb.html) in the SAP Landscape Management documentation.

## Known Issues and Limitations

The following sections explain the various restrictions that apply when using SAP Landscape Management with Google Cloud.

### SAP Landscape Management System

With a dedicated service account configuration, you can run SAP Landscape Management outside Google Cloud; however, you need to use an appropriate hybrid connectivity solution to support your requirements for both performance and resiliency. For more information, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

### Internet Protocol version 4 (IPv4) requirement

The SAP Landscape Management software stack requires Internet Protocol version 4 (IPv4). The [Connector for LaMa installation instructions](https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment), include a step for configuring the Java Virtual Machine (JVM) to use IPv4.

To configure the JVM, you can use the [Java System Properties tool](https://help.sap.com/viewer/product/SAP_NETWEAVER_750/LATEST/en-US?q=java%20system%20properties) of SAP Netweaver Administrator.

For more information about this requirement and configuring the JVM, see:

  * [SAP Note 2250890 - IPv6 addresses are used unexpectedly](https://launchpad.support.sap.com/#/notes/2250890)
  * [SAP Note 1888685 - Change the JVM parameter setting for NW7.1 and above releases](https://launchpad.support.sap.com/#/notes/1888685)



### Compute Engine Persistent Disk

The following restrictions apply when using SAP Landscape Management to manage Compute Engine persistent disks:

  * Only zonal persistent disks are supported. Regional Disks are not supported.
  * Partitioning of disks to span multiple instances is not supported.
  * For mount points that are managed by SAP Landscape Management: 
    * The `/etc/fstab` file cannot contain any entries.
    * Only one logical volume per volume group and one volume group per device is supported in the current version.
    * All mount points that are associated with a logical volume in a volume group must be configured in SAP Landscape Management mount configuration. Any logical volume in a volume group that is not configured in the SAP Landscape Management mount configuration leads to errors during SAP Landscape Management operations like Unprepare. For more information, see [Adding Mount Point Configurations](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/cd571541a0254b1b98790742c8340e7f.html).



### Operational restrictions

The following sections describe restrictions that apply to certain SAP Landscape Management operations and provisioning actions on Google Cloud.

#### Instance and system operational restrictions

The following restrictions apply to the SAP Landscape Management Prepare/Unprepare and Relocation operations on Google Cloud:

  * If a mount point is busy, the unmount operation during unprepare or relocate can fail. For example, if a user that is logged on to a VM changes the working directory to a directory under a mount point that is managed by SAP Landscape Management.
  * If a VM instance has an external IP address, you cannot use SAP Landscape Management to update an alias IP range. However, you can avoid this limitation if you use a second NIC for the external IP.



#### System provisioning restrictions

The following table shows the restrictions that apply to provisioning systems on Google Cloud with SAP Landscape Management:

System provisioning scenario | Restrictions  
---|---  
SAP System Copy | 

  * Mount points and storage volumes that contain the database logs, data, and software can be used only by the database instance and cannot be shared with any other instance or database..

  
SAP System Refresh | 

  * Mount points and storage volumes that contain the database logs, data, and software can be used only by the database instance and cannot be shared with any other instance or database.
  * Install the database client software on a separate volume if the SAP application servers need the software.

  
SAP Database Refresh | 

  * Target VMs and application instances must exist already.
  * Mount points and storage volumes that contain the database logs, data, and software can be used only by the database instance and cannot be shared with any other instance or database.
  * Install the database client software on a separate volume if the SAP application servers need the software.

  
  
## Required IAM resource permissions for the Connector for LaMa

Grant all of the same permissions to a service account for the Connector for LaMa that a user would need to execute the same functions.

To allow stop and start actions on your managed VMs, you can assign the Compute Admin (`roles/compute.admin`) role to the service account.

In production environments, follow the principle of least privilege.

If the Compute Admin role is too permissive, you can create a custom role and use the following permissions to start with:
    
    
    compute.addresses.useInternal
      compute.disks.create
      compute.disks.createSnapshot
      compute.disks.delete
      compute.disks.get
      compute.disks.list
      compute.disks.setLabels
      compute.disks.update
      compute.disks.use
      compute.globalOperations.list
      compute.images.useReadOnly
      compute.instanceTemplates.list
      compute.instanceTemplates.useReadOnly
      compute.instances.attachDisk
      compute.instances.create
      compute.instances.delete
      compute.instances.detachDisk
      compute.instances.get
      compute.instances.list
      compute.instances.setMachineType
      compute.instances.setMetadata
      compute.instances.setServiceAccount
      compute.instances.setTags
      compute.instances.start
      compute.instances.stop
      compute.instances.suspend
      compute.instances.updateNetworkInterface
      compute.machineTypes.get
      compute.machineTypes.list
      compute.networks.use
      compute.projects.get
      compute.snapshots.create
      compute.snapshots.delete
      compute.snapshots.get
      compute.snapshots.list
      compute.snapshots.setLabels
      compute.snapshots.useReadOnly
      compute.subnetworks.use
      compute.zoneOperations.list
      compute.zones.list
      resourcemanager.projects.get
      resourcemanager.projects.list
      storage.objects.delete
      storage.objects.get
      storage.objects.list

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
