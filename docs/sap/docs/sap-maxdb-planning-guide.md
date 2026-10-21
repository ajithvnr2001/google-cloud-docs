---
url: https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide/
title: SAP MaxDB planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:38.376557+00:00
---

# SAP MaxDB planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP MaxDB planning guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of how SAP MaxDB works on Google Cloud, and provides details that you can use when planning the implementation of a new SAP MaxDB system.

For information about how to deploy SAP MaxDB on Google Cloud, see the following:

  * To deploy a single-node system, contact [Cloud Customer Care](https://cloud.google.com/support).
  * To deploy a high-availability (HA) cluster on RHEL, see [Manual HA cluster configuration guide for SAP MaxDB on RHEL](https://docs.cloud.google.com/sap/docs/sap-maxdb-ha-config-rhel).



For information from SAP about SAP MaxDB, see the SAP MaxDB Library, which is available in the [SAP Help Portal](https://help.sap.com/viewer/9d62a6d2a95149718db6b65b7ffa2052/113/en-US).

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

A basic single-node SAP MaxDB installation on Google Cloud comprises the following components:

  * One Compute Engine VM running your SAP MaxDB database.
  * Three or four attached persistent disk drives:

Drive contents | Linux | Windows  
---|---|---  
Root directory of the database instance | `/sapdb/[DBSID]` | `MaxDB (D:)`  
Database data files | `/sapdb/[DBSID]/sapdata` | `MaxDB Data (E:)`  
Database transaction logs | `/sapdb/[DBSID]/saplog` | `MaxDB Log (L:)`  
Database backups (optional) | `/maxdbbackup` | `Backup (X:)`  



Optionally, you can expand your installation to include the following as well:

  * NetWeaver directories, including:

    * `/usr/sap` on Linux or `SAP (S:)` on Windows
    * `/sapmnt` on Linux or `Pagefile (P:)` on Windows
  * A NAT gateway. A NAT gateway allows you to provide internet connectivity for your VMs while denying direct internet connectivity to those VMs. You could also configure this VM as a bastion host that allows you to establish SSH connections to the other VMs on your private subnet. See NAT gateways and bastion hosts for more information.




Different use cases might require additional devices or databases. For more information, see the MaxDB documentation in the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_MAXDB).

**Note:** You might be able to achieve a [sustained use discount](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) of up to 30% for your Compute Engine instances. Use the [pricing calculator](https://cloud.google.com/pricing/calculator) to help you estimate your actual costs.

## Resource requirements

In many ways, running SAP MaxDB on Google Cloud is similar to running it in your own data center. You still need to think about computing resources, storage, and networking considerations. For more information, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

### VM configuration

SAP MaxDB is certified to run on all Compute Engine machine types, including custom types. However, if you run MaxDB on the same VM as SAP NetWeaver or Application Server Central Services (ASCS), you must use a VM that is supported by SAP NetWeaver. For a list of the VMs that SAP NetWeaver supports, see the [SAP NetWeaver Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#machine_types).

For information about all of the machine types available on Google Cloud and their use cases, see [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) in the Compute Engine documentation.

#### CPU configuration

The number of vCPUs you select for MaxDB depends on your application load and your performance objectives. You must allocate a minimum of two vCPUs to your SAP MaxDB installation. For the best performance, scale the number of vCPUs and the size of your persistent disks until your performance objectives are met. For more information from SAP about MaxDB, see the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_MAXDB).

#### Memory configuration

The memory you allocate to your SAP MaxDB system is dependent on your use case. The optimal amount of memory for your use case depends on the complexity of the queries you're running, the size of your data, the amount of parallelism you're using, and the level of performance you're expecting.

For more information from SAP about MaxDB, see the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_MAXDB).

### Storage configuration

By default, each Compute Engine VM has a small [root persistent disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) that contains the operating system. You provision additional disks for your database data, logs, and, optionally, database backups.

Use a high-performance persistent disk for the log volume and, depending on your performance objectives, the data volume, as well.

For more information about the persistent disk options for SAP MaxDB, see Persistent disks.

For more information from SAP about storage configuration for SAP MaxDB, see the following SAP notes:

  * [869267 - FAQ: SAP MaxDB Log area](https://me.sap.com/notes/869267).
  * [1173395 - FAQ: SAP MaxDB and liveCache configuration](https://me.sap.com/notes/1173395).



### Supported SAP MaxDB versions and features

SAP MaxDB version 7.9.09 and newer is certified by SAP for use on Google Cloud.

SAP also certifies the following versions of SAP liveCache and SAP Content Server on Google Cloud:

  * SAP liveCache technology with a minimal installation version of SAP LC/LCAPPS 10.0 SP 39. For all other information about supported versions, see SAP Note [2074842 - Matrix of liveCache Versions for SCM 7.02 and Later](https://me.sap.com/notes/2074842).
  * SAP Content Server 6.50 on Windows using Internet Information Services 10 (IIS)
  * SAP Content Server 6.50 on Linux using Apache Web Server 2.4.xx



For more information about the SAP products that are supported on Google Cloud, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

### Supported operating systems

You can run SAP MaxDB on the following operating systems on Google Cloud:

  * Red Hat Entrprise Linux (RHEL)
  * SUSE Linux Enterprise Server (SLES)
  * Windows Server



SAP lists the operating system versions that you can use with MaxDB in the [SAP Product Availability Matrix](https://apps.support.sap.com/sap/support/pam).

Compute Engine provides Linux and Windows operating systems as _public images_ that include enhancements for Google Cloud. For more information about Compute Engine images, see [OS images](https://docs.cloud.google.com/compute/docs/images).

## Deployment considerations

### Regions and zones

When you deploy a VM, you must choose a region and zone. A region is a specific geographical location where you can run your resources, and corresponds to a data center location. Each region has one or more zones.

Global resources, such as preconfigured disk images and disk snapshots, can be accessed across regions and zones. Regional resources, such as static external IP addresses, can be accessed only by resources that are in the same region. Zonal resources, such as VMs and disks, can be accessed only by resources that are located in the same zone.

![Google Cloud regions and zones](https://docs.cloud.google.com/static/docs/images/overview/regions-zones.svg)

When choosing regions and zones for your VMs, keep the following in mind:

  * **The location of your users and your internal resources** , such as your data center or corporate network. To decrease latency, select a location that is in close proximity to your users and resources.
  * **The location of your other SAP resources**. Your SAP application and your database must be in the same zone.



### Persistent disks

Persistent disks are durable block storage devices that function similarly to the physical disks in a desktop or a server.

Compute Engine offers different types of persistent disks. Each type has different performance characteristics. Google Cloud manages the underlying hardware of persistent disks to ensure data redundancy and to optimize performance.

You can use any of the following Compute Engine persistent disk types:

  * **Standard persistent disks (`pd-standard`)**: efficient and economical block storage backed by [standard hard disk drives (HDD)](https://en.wikipedia.org/wiki/Hard_disk_drive) for handling sequential read-write operations, but not optimized to handle high rates of random input-output operations per second (IOPS).
  * **SSD (`pd-ssd`)**: provides reliable, high-performance block storage backed by [solid-state drives (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive).
  * **Balanced (`pd-balanced`)**: provides cost-effective and reliable SSD-based block storage.
  * **Extreme (`pd-extreme`)**: provides higher maximum IOPS and throughput options than `pd-ssd` for larger Compute Engine machine types. For more information, see [Extreme persistent disks](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk).



The performance of SSD and balanced persistent disks scales automatically with size, so you can adjust performance by resizing your existing persistent disks or adding more persistent disks to a VM.

The type of VM you are using and the number of vCPUs it contains also affects persistent disk performance.

Persistent disks are located independently from your VMs, so you can detach or move persistent disks to keep your data, even after you delete your VMs.

For more information about the different types of Compute Engine persistent disks, their performance characteristics, and how to work with them, see the Compute Engine documentation:

  * [Storage options](https://docs.cloud.google.com/compute/docs/disks)
  * [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance)
  * [Other factors that affect Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors)
  * [Add a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Creating persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)



#### Local SSD (non-persistent)

Google Cloud also offers [local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) disk drives. Although local SSDs can offer some advantages over persistent disks, don't use them as part of an SAP MaxDB system. VM instances with local SSDs attached cannot be stopped and then restarted.

### NAT gateways and bastion hosts

If your security policy requires truly internal VMs, you need to set up a NAT proxy manually on your network and a corresponding route so that VMs can reach the internet. It is important to note that you cannot connect to a fully internal VM instance directly by using SSH. To connect to such internal machines, you must set up a bastion instance that has an external IP address and then tunnel through it. When VMs don't have external IP addresses, they can be reached only by other VMs on the network, or through a managed VPN gateway. You can provision VMs in your network to act as trusted relays for inbound connections, called bastion hosts, or network egress, called NAT gateways. For more transparent connectivity without setting up such connections, you can use a managed VPN gateway resource.

#### Using bastion hosts for inbound connections

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private-network VMs. This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH communication from the internet.

![Bastion host shown in SSH scenario](https://docs.cloud.google.com/static/solutions/images/bastion.png)

You can achieve SSH access to VMs that don't have an external IP address by first connecting to a bastion host. A complete hardening of a bastion host is outside the scope of this guide, but you can take some initial steps, including:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private VMs from only the bastion host.



By default, SSH on VMs is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private VM. Due to this two-step login, you use SSH-agent forwarding to reach the target VM instead of storing the target VM's private key on the bastion host. You must do this even if you are using the same key-pair for both bastion and target VMs, as the bastion has direct access only to the public half of the key-pair.

#### Using NAT gateways for traffic egress

When a VM does not have an assigned, external IP address, it cannot make direct connections to external services, including other Google Cloud services. To allow these VMs to reach services on the internet, you can set up and configure a [NAT gateway](https://docs.cloud.google.com/compute/docs/vpc/special-configurations#natgateway). The NAT gateway is a VM that can route traffic on behalf of any other VM on the network. You must have one NAT gateway for each network. Be aware that a single-VM NAT gateway must not be considered highly available, and cannot support high traffic throughput for multiple VMs. For instructions on how to set up a VM to act as a NAT gateway, see either the [SAP MaxDB Deployment Guide for Linux](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-linux#setting-up-a-nat-gateway) or the [SAP MaxDB Deployment Guide for Windows](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-windows#setting-up-a-nat-gateway).

### Custom images

After your system is up and running, you can [create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images). You must create these images when you modify the state of your root persistent disk and want to be able to restore the new state. You must design a plan for how to manage the custom images you create. For more information, see [Image Management Best Practices](https://docs.cloud.google.com/solutions/image-management-best-practices).

### User identification and resource access

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

Consider the information in the following sections when planning networking and security.

#### Minimum privilege model

One of your first lines of defense is to restrict who can reach your network and your VMs by using [firewalls](https://docs.cloud.google.com/compute/docs/vpc/firewalls). By default, all traffic to VMs, even from other VMs, is blocked by the firewall unless you create rules to allow access. The exception is the default network that is created automatically with each project and has default [firewall rules](https://docs.cloud.google.com/compute/docs/networking#firewall_rules).

By creating firewall rules, you can restrict all traffic on a given set of ports to specific source IP addresses. Follow the minimum privilege model to restrict access to the specific IP addresses, protocols, and ports that need access. For example, always set up a [bastion host](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#bastion_hosts_nat) and allow SSH connections to your SAP NetWeaver system only from that host.

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

You can use a network to define a gateway IP and the network range for the VMs attached to that network. All Compute Engine networks use the [IPv4](https://tools.ietf.org/html/rfc791) protocol. Every Google Cloud project is provided with a default network with preset configurations and firewall rules, but you must add a custom subnetwork and firewall rules based on a minimum privilege model. By default, a newly created network has no firewall rules and hence no network access.

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

Refer to the following additional security resources for your SAP environment on Google Cloud:

  * [Securely connecting to VM instances](https://docs.cloud.google.com/solutions/connecting-securely)
  * [Security Center](https://cloud.google.com/security/)
  * [Compliance resource center](https://cloud.google.com/compliance)
  * [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)
  * [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design/resources/google_infrastructure_whitepaper_fa.pdf?e=48754805)



### Backup and recovery

You must have a plan for how to restore your system to operating condition if the worst happens. For general guidance about how to plan for disaster recovery using Google Cloud, see:

  * [How to Design a Disaster Recovery Plan](https://docs.cloud.google.com/solutions/designing-a-disaster-recovery-plan)
  * [Disaster Recovery Cookbook](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook)



## Licenses

This section provides information about licensing requirements.

### SAP licenses

Running SAP MaxDB on Google Cloud requires you to bring your own license (BYOL). For more information, see the following SAP notes:

  * [2446441 - Linux on Google Cloud Platform (IaaS): Adaption of your SAP License](https://me.sap.com/notes/2446441)
  * [2456953 - Windows on Google Cloud Platform (IaaS): Adaptation of your SAP License](https://me.sap.com/notes/2456953)



For more information about SAP licensing, contact SAP.

### Operating system licenses

In Compute Engine, there are two ways to license SLES, RHEL, and Windows Server:

  * With pay-as-you-go licensing, your Compute Engine VM hourly cost includes licensing. Google manages the licensing logistics. Your hourly costs are higher, but you have complete flexibility to increase and decrease your costs, as needed. This is the licensing model used for Google Cloud public images that include SLES, RHEL, and Windows Server.

**Important:** RHEL, SLES, and Windows Server are premium images. Premium images charge for OS licenses in addition to standard VM charges. For details about pricing, refer to the [pricing for RHEL images](https://docs.cloud.google.com/compute/disks-image-pricing#rhel_images), [pricing for SUSE images](https://docs.cloud.google.com/compute/disks-image-pricing#suse_images), and [pricing for Windows Server images](https://docs.cloud.google.com/compute/disks-image-pricing#windows_server_pricing).
  * With BYOL, your Compute Engine VM costs are lower because the licensing isn't included. You must migrate an existing license or purchase your own license, which means paying up front, and you have less flexibility.




## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



You can also browse the information about SAP MaxDB in the [SAP Help Portal](https://help.sap.com/viewer/p/SAP_MAXDB).

## What's next

  * To deploy SAP MaxDB on Linux, see the [SAP MaxDB Deployment Guide for Linux](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-linux).

  * To deploy SAP MaxDB on Windows, see the [SAP MaxDB Deployment Guide for Windows](https://docs.cloud.google.com/sap/docs/sap-maxdb-deployment-windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
