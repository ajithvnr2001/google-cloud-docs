---
url: https://docs.cloud.google.com/sap/docs/oracle-planning/
title: Plan Oracle Database implementation for SAP NetWeaver \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:44.261321+00:00
---

# Plan Oracle Database implementation for SAP NetWeaver  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/oracle-planning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Plan Oracle Database implementation for SAP NetWeaver Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides details that you can use to plan the implementation of Oracle Database 19c or later, on Oracle Linux, that supports SAP NetWeaver based applications running on Google Cloud. 

For information about how to deploy an Oracle Database 19c or later on Oracle Linux for SAP systems running on Google Cloud, see [Deploy Oracle Database for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node).

## Licenses

To run an Oracle Database with SAP systems on Google Cloud, you need to bring your own license (BYOL) for Oracle Database 19c or later.

You also need to purchase Oracle Linux Premier Support. For more information, see the SAP note [3408032 - Oracle Linux: operating system support process](https://me.sap.com/notes/3408032).

For information about running an Oracle Database 19c with SAP NetWeaver based products and solutions, see the SAP note [2799900 - Central Technical Note for Oracle Database 19c](https://me.sap.com/notes/2799900).

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

## Compliance and sovereign controls

If you require your SAP workload to run in compliance with data residency, access control, support personnel, or regulatory requirements, then you must plan for using Assured Workloads \- a service that helps you run secure and compliant workloads on Google Cloud without compromising the quality of your cloud experience. For more information, see [Compliance and sovereign controls for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls). 

## Deployment architecture

For SAP NetWeaver based applications running on Google Cloud, a conventional single-node Oracle Database instance comprises of the following components:

  * A Compute Engine instance that runs your Oracle Database.
  * If you're using XFS file system, then you need Persistent Disk or Hyperdisk volumes for the following drives. We strongly recommend that you use Hyperdisk volumes.

Drive contents | Linux directory  
---|---  
Oracle installation |  `/oracle/DB_SID`  
`/oracle/DB_SID/origlogA`  
`/oracle/DB_SID/origlogB`  
`/oracle/DB_SID/sapdata1`  
`/oracle/DB_SID/sapdata2`  
Oracle mirror |  `/oracle/DB_SID/mirrlogA`  
`/oracle/DB_SID/mirrlogB`  
`/oracle/DB_SID/sapreorg`  
`/oracle/DB_SID/saptrace`  
`/oracle/DB_SID/saparch`  
`/oracle/DB_SID/sapbackup`  
`/oracle/DB_SID/sapcheck`  
`/oracle/DB_SID/sapdata3`  
`/oracle/DB_SID/sapdata4`  
`/oracle/DB_SID/sapprof`  
Backup of offline redolog file | `/oracle/DB_SID/oraarch`  
SAP NetWeaver installation | `/usr/sap`  
SAP NetWeaver directory containing mount points for shared file systems | `/sapmnt`  
  * If you intend to use Oracle Automatic Storage Management (ASM) to manage storage for your Oracle Database, then you need Persistent Disk or Hyperdisk volumes for the following drives. We strongly recommend that you use Hyperdisk volumes.

Drive contents | Linux directory  
---|---  
Oracle installation | `/oracle`  
Oracle ASM disks |  For information about identifying storage requirements for Oracle ASM, including redundancy level, disk group layout, and disk sizes, see the following:
    * [ Identifying storage requirements for Oracle Automatic Storage Management](https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/identifying-storage-requirements-for-oracle-automatic-storage-management.html)
    * [ASM - Scalability and Limits](https://support.oracle.com/epmos/faces/DocContentDisplay?_afrLoop=159873613454038&id=370921.1&_afrWindowMode=0&_adf.ctrl-state=1c8l0bbjg5_53) (Oracle account required)  
SAP NetWeaver installation | `/usr/sap`  
SAP NetWeaver directory containing mount points for shared file systems | `/sapmnt`  
  * Optionally, you can expand your deployment to include a NAT gateway, which lets you provide internet connectivity for your compute instance while denying direct internet connectivity to them. You can also configure your compute instance as a bastion host that lets you establish SSH connections to the other compute instances on your private subnet. For more information, see NAT gateways and bastion hosts.




Different use cases might require additional devices. For more information, see the SAP documentation [SAP on Oracle](https://help.sap.com/docs/SUPPORT_CONTENT/ora/3354617160.html).

**Note:** You might be able to achieve a sustained use discount of up to 30% for your Compute Engine instances. Use the pricing calculator to help you estimate your actual costs.

## Resource requirements

In many ways, running an Oracle Database in an SAP NetWeaver based system is similar to running it in your own data center. You still need to think about computing resources, storage, and networking considerations.

For information from SAP about resource requirements for running an Oracle database, see the SAP note [2799900 - Central Technical Note for Oracle Database 19c](https://me.sap.com/notes/2799900).

### Compute instance configuration

To run an Oracle Database for SAP NetWeaver based applications on Google Cloud, SAP has certified the use of all Compute Engine machine types, including custom machine types. However, if you run the Oracle database on the same compute instance as the SAP NetWeaver or Application Server Central Services (ASCS), then you must use a compute instance that is certified by SAP for use with SAP NetWeaver.

For information about the Compute Engine machine types that SAP has certified for use with SAP NetWeaver, go to [Certified solutions and machine types](https://docs.cloud.google.com/sap/docs/sap-certifications#certified-machine-types-and-solutions) and in the **Certified SAP solution** list, select **SAP NetWeaver**.

#### CPU configuration

The number of vCPUs that you need to run an Oracle Database depends on your SAP application load and your performance objectives. You must allocate a minimum of 2 vCPUs to your Oracle Database installation. For the best performance, scale the number of vCPUs and the size of your block storage until your performance objectives are met.

#### Memory configuration

The memory that you allocate for your Oracle Database depends on your use case. The optimal amount of memory for your use case depends on the complexity of the queries you're running, the size of your data, the amount of parallelism you're using, and the level of performance you're expecting.

### Storage configuration

By default, Compute Engine automatically creates a boot disk when you create an instance. You provision additional disks for your database data, logs, and, optionally, database backups.

For the volumes of your Oracle Database instance, use disks that satisfy your performance requirements. For information about factors that determine Hyperdisk or Persistent Disk performance, see [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance) and [About Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance), respectively.

For mission-critical workloads, we strongly recommend that you use Hyperdisk volumes. For more information about block storage for your Oracle Database, see Block storage.

## Supported Oracle Database versions and features

To use Oracle Databases with SAP NetWeaver based applications running on Google Cloud, SAP has certified the following:

  * Oracle Database 19c or later
  * The database must use the Unicode character set.
  * The database must use a file system that has been validated by Oracle. While you can use [Oracle Automatic Storage Management (ASM)](https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/configuring-storage-for-oracle-automatic-storage-management.html), Oracle recommends using a file system for the Oracle database.
  * You must have a Premier Support subscription for your Oracle Database.



Real Application Clusters (RAC) and Pacemaker based high-availability (HA) solutions are not supported.

For more information, see the SAP note [3559536](https://me.sap.com/notes/3559536).

## Supported operating systems

To use Oracle Databases with SAP NetWeaver based applications running on Google Cloud, SAP has certified the following operating systems:

  * Oracle Linux 9 or Oracle Linux 8, with the following kernel:

    * UEK 7: 5.15.0-1.43.4.2.el9uek.x86_64 or later
    * UEK 7: 5.15.0-202.135.2.el8uek.x86_64 or later

You can get these images from Compute Engine. For more information, see [Oracle Linux](https://docs.cloud.google.com/compute/docs/images/os-details#oracle_linux).




To use Oracle Linux for running Oracle Database with SAP NetWeaver, you must also ensure the following:

  * You've purchased Oracle Linux Premier Support.
  * All components of your SAP system run the same Oracle Linux version. This includes the database, app servers, and any other closely-coupled auxiliary system.
  * Your compute instances must be able to retrieve additional software and updates from the Unbreakable Linux Network (ULN) either directly using HTTPS or a ULN proxy.
  * If you're using Oracle Linux 9.5, then the minimum version of Oracle Database that you must use is 19.26.



While using Oracle Database based installations, to make the SAP Central Services instance highly available, you need to ensure the following:

  * A Compute Engine instance that runs Oracle Database or any other closely-coupled auxiliary system must use a supported operating system, as mentioned earlier in this section.
  * As an exception to the preceding requirement, a compute instance that runs the SAP Central Services instance like the ASCS or the ERS, can use any SAP-certified OS as long as that compute instance doesn't host the Oracle Database or has any Oracle software installed.



For more information, see the SAP note [3074643 - OLNX: FAQ: if Pacemaker for Oracle Linux is supported in SAP Environment](https://me.sap.com/notes/3074643).

## Deployment considerations

This section provides information for planning the aspects such as deployment location, block storage, user identification and access control, network, and backup and recovery for your Oracle Database.

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



### Block storage

For persistent block storage, you can attach Hyperdisk and Persistent Disk volumes to your Compute Engine instances.

Compute Engine offers different types of Hyperdisk and Persistent Disk. Each type has different performance characteristics. Google Cloud manages the underlying hardware of these disks to ensure data redundancy, and to optimize performance.

With SAP NetWeaver, you can use any of the following Hyperdisk or Persistent Disk types:

  * **Hyperdisk types** : Hyperdisk Balanced (`hyperdisk-balanced`) and Hyperdisk Extreme (`hyperdisk-extreme`) 
    * Hyperdisk Extreme provides higher maximum IOPS and throughput options than Persistent Disk types.
    * For Hyperdisk Extreme, you select the performance you need by provisioning IOPS, which also determines your throughput. For more information, see [Size and performance limits for Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
    * For Hyperdisk Balanced, you select the performance you need by provisioning IOPS and throughput. For more information, see [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
    * For information about the machine types that support using Hyperdisk, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).
  * **Persistent Disk types** : Performance or SSD (`pd-ssd`) 
    * SSD Persistent Disk is backed by solid-state drives (SSD). It provides cost-effective and reliable block storage.
    * SSD Persistent Disk supports PD Async Replication. You can use this feature for cross-region active-passive disaster recovery. For more information, see [About Persistent Disk Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).
    * The performance of SSD Persistent Disk volumes scale automatically with size. Therefore, you can adjust performance by resizing your existing Persistent Disk volumes or adding more Persistent Disk volumes to a Compute Engine instance.



The type of compute instance that you are using and the number of vCPUs it contains can also affect or limit persistent disk performance.

**Note:** Disk size, machine type memory, and network usage are calculated in gigabytes (GB), where 1 GB is 230 bytes. This unit of measurement is also known as a [gibibyte (GiB)](https://wikipedia.org/wiki/Gibibyte).

Persistent Disk and Hyperdisk volumes are located independently from your compute instances, so you can detach or move the disks to keep your data, even after you delete your compute instances.

In the [VM instances](https://console.cloud.google.com/compute/instances) page of the Google Cloud console, you can see the disks that are attached to your VM instances under **Additional disks** on the **VM instance details** page for each VM instance.

For more information about the different types of block storage offered by Compute Engine, their performance characteristics, and how to work with them, see the Compute Engine documentation:

  * [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks)
  * [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [About Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance)
  * [Other factors that affect Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors)
  * [Create a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk)
  * [Create a Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)



### NAT gateways and bastion hosts

If your security policy requires truly internal compute instances, then you need to set up a NAT proxy manually on your network and a corresponding route so that compute instances can reach the internet. It is important to note that you cannot connect to a fully internal compute instance directly by using SSH. To connect to such internal instances, you must set up a bastion instance that has an external IP address and then tunnel through it. When compute instances don't have external IP addresses, they can be reached only by other instances on the network, or through a managed VPN gateway. You can provision compute instances in your network to act as trusted relays for inbound connections, called bastion hosts, or network egress, called NAT gateways. For more transparent connectivity without setting up such connections, you can use a managed VPN gateway resource.

#### Using bastion hosts for inbound connections

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private-network compute instances. This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH communication from the internet.

The following image shows how a bastion hosts connecting external and internal compute instances connect using SSH:

![Bastion host in SSH scenario](https://docs.cloud.google.com/static/solutions/images/bastion.png)

To use SSH to connect to compute instances that don't have an external IP address, you first need to connect to a bastion host. A complete hardening of a bastion host is outside the scope of this guide, but you can take some initial steps, including:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private compute instances from only the bastion host.



By default, SSH on Compute Engine instances is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private compute instance. Due to this two-step login, you must use SSH-agent forwarding to reach the target instance instead of storing the private key of the target instance on the bastion host. You must do this even if you are using the same key-pair for both the bastion and target instances, as the bastion has direct access only to the public half of the key-pair.

#### Using NAT gateways for traffic egress

When a Compute Engine instance does not have an assigned, external IP address, it cannot make direct connections to external services, including other Google Cloud services. To let these instances reach services on the internet, you can set up and configure a NAT gateway. The NAT gateway is an instance that can route traffic on behalf of any other instance on the network. You must have only one NAT gateway for each network. Be aware that a single-instance NAT gateway must not be considered highly available, and cannot support high traffic throughput for multiple instances. For information about how to set up a compute instance to act as a NAT gateway, see [Set up a NAT gateway](https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node#set_up_a_nat_gateway).

### Custom images

After your system is up and running, you can [create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images). We recommend that you create these images when you modify the state of your boot disk and want to be able to restore the new state. You also need to have a plan for how to manage the custom images you create. For more information, see [Image management best practices](https://docs.cloud.google.com/compute/docs/images/image-management-best-practices).

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

### Networking and network security

When you are planning networking and security, consider the information in the following sections.

#### Minimum privilege model

One of your first lines of defense is to restrict who can reach your network and your VMs by using [firewalls](https://docs.cloud.google.com/compute/docs/vpc/firewalls). By default, all traffic to VMs, even from other VMs, is blocked by the firewall unless you create rules to allow access. The exception is the default network that is created automatically with each project and has default [firewall rules](https://docs.cloud.google.com/compute/docs/networking#firewall_rules).

By creating firewall rules, you can restrict all traffic on a given set of ports to specific source IP addresses. We recommend that you follow the minimum privilege model to restrict access to the specific IP addresses, protocols, and ports that need access. For example, we recommend that you always set up a [bastion host](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#bastion_hosts_nat) and allow SSH connections to your SAP NetWeaver system only from that host.

#### Access management

Understanding how access management works in Google Cloud is key to planning your implementation. You need to make decisions about:

  * How to organize your resources in Google Cloud.
  * Which team members can access and work with resources.
  * Exactly which permissions each team member can have.
  * Which services and applications need to use which service accounts, and what level of permissions to grant in each case.

**Important:** We strongly recommend that you follow the best practices for enterprise-grade access control provided in [Verify every access attempt explicitly](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly) in the Google Cloud Well-Architected Framework.

Start by understanding the [Cloud Platform Resource Hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). It's important that you understand what the various resource containers are, how they relate to each other, and where the access boundaries are created.

Identity and Access Management (IAM) provides unified control over permissions for Google Cloud resources. You can manage access control by defining who has what access to resources. For example, you can control who can perform control-plane operations on your SAP instances, such as creating and modifying VMs, persistent disks, and networking.

For more details about IAM, see the [Overview of IAM](https://docs.cloud.google.com/iam/docs/overview).

For an overview of IAM in Compute Engine, see [Access Control Options](https://docs.cloud.google.com/compute/docs/access).

IAM roles are key to granting permissions to users. For a reference about roles and which permissions they provide, see [Identity and Access Management Roles](https://docs.cloud.google.com/iam/docs/overview#roles).

Google Cloud's service accounts provide a way for you to give permissions to applications and services. It's important to understand how service accounts work in Compute Engine. For details, see [Service Accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).

#### Custom networks and firewall rules

You can use a network to define a gateway IP and the network range for the VMs attached to that network. All Compute Engine networks use the [IPv4](https://tools.ietf.org/html/rfc791) protocol. Every Google Cloud project is provided with a default network with preset configurations and firewall rules, but we recommend that you add a custom subnetwork and firewall rules based on a minimum privilege model. By default, a newly created network has no firewall rules and hence no network access.

Depending on your requirements, you might want to add additional subnetworks to isolate parts of your network. For more information, see [Subnetworks](https://docs.cloud.google.com/compute/docs/vpc#vpc_networks_and_subnets).

The firewall rules apply to the entire network and all the VMs in the network. You can add a firewall rule that allows traffic between VMs in the same network and across subnetworks. You can also configure firewalls to apply to specific target VMs by using the [tagging mechanism](https://docs.cloud.google.com/compute/docs/vpc/add-remove-network-tags).

Some SAP products, such as SAP NetWeaver, require access to certain ports. Be sure to add firewall rules to allow access to [the ports outlined by SAP](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).

#### Routes

[Routes](https://docs.cloud.google.com/compute/docs/vpc/routes) are global resources attached to a single network. User-created routes apply to all VMs in a network. This means you can add a route that forwards traffic from VM to VM within the same network and across subnetworks without requiring external IP addresses.

For external access to internet resources, launch a VM with no external IP address and configure another virtual machine as a NAT gateway. This configuration requires you to add your NAT gateway as a route for your SAP instance. For more information, see NAT gateways and bastion hosts.

#### Cloud VPN

You can securely connect your existing network to Google Cloud through a [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection using [IPsec](https://wikipedia.org/wiki/IPsec) by using Cloud VPN. Traffic traveling between the two networks is encrypted by one VPN gateway, then decrypted by the other VPN gateway. This protects your data as it travels over the internet. You can dynamically control which VMs can send traffic down the VPN using [instance tags on routes](https://docs.cloud.google.com/compute/docs/vpc/using-routes#addingroute). Cloud VPN tunnels are billed at a static monthly rate plus standard egress charges. Note that connecting two networks in the same project still incurs standard egress charges. For more information, see [Cloud VPN Overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Creating a VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-vpns).

#### Securing a Cloud Storage bucket

If you use Cloud Storage to host your backups for your data and log, make sure you use TLS (HTTPS) while sending data to Cloud Storage from your VMs to protect data in transit. Cloud Storage automatically encrypts data at rest. You can specify your own encryption keys if you have your own key-management system.

#### Related security documents

For additional security resources for your SAP environment on Google Cloud, see the following:

  * [Securely connecting to VM Instances](https://cloud.google.com/solutions/connecting-securely)
  * [Google Cloud security](https://cloud.google.com/security)
  * [Compliance resource center](https://cloud.google.com/compliance)
  * [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)
  * [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design)



### Backup and recovery

You must have a plan for how to restore your system to operating condition if the worst happens. For general guidance about how to plan for disaster recovery using Google Cloud, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

To receive support from Oracle and SAP for your Oracle Linux based Oracle Database, make sure that you have purchased Oracle Linux Premier Support. 

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



## What's next

  * To deploy an Oracle Database with Oracle Linux for SAP NetWeaver based applications running on Google Cloud, see [Deploy Oracle Database for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-deployment-single-node).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
