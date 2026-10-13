---
url: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide/
title: IBM Db2 for SAP planning guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:20.515647+00:00
---

# IBM Db2 for SAP planning guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  IBM Db2 for SAP planning guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides information that you can use to plan for the installation of an IBM Db2 Advanced Enterprise Server Edition (AESE) (IBM Db2) system that supports SAP applications on Google Cloud.

For information about how to deploy IBM Db2 database with SAP systems that run on Google Cloud, read this guide and then see the What's next section.

For information from SAP about using IBM Db2 with SAP deployments, see [SAP on IBM Db2 for Linux, UNIX, and Windows](https://help.sap.com/viewer/p/DB6).

For more information about the products that SAP has certified to run on Google Cloud, including IBM Db2, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

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

An IBM Db2 installation with a single-partition database on Google Cloud comprises the following components:

  * One Compute Engine VM running your IBM Db2 database.
  * One or more persistent disk drives for the following:

    * The root disk.
    * The database id volume (`/db2/<DBSID>/`),
    * The instance volume (`/db2/db2<dbsid>`), which contains the home directory of user `db2<dbsid>` and the IBM Db2 instance data for `<DBSID>` as well as the IBM Db2 software.
    * The log volume (`/db2/<DBSID>/log_dir`), which contains at least the online database log files.
    * The dump/diagnostic volume (`/db2/<DBSID>/db2dump`), which contains Db2 diagnostic log files, Db2 dump files, and further service engineer information.
    * The data volume (`/db2/<DBSID>/sapdata<n>` or `/db2/<DBSID>/sapdata/sapdata<n>`). This is the storage location for tablespaces with container-type database managed space (DMS) FILE or tablespaces with Db2's automatic storage
    * The temporary tablespace volume (`/db2/<DBSID>/saptmp<n>` or `/db2/ <DBSID>/saptmp/saptmp<n>`). This is the storage location for temporary tablespaces.



Depending on the requirements of your installation, you might also need to include the following as well:

  * A NAT gateway. A NAT gateway lets you provide Internet connectivity for your VMs while denying direct Internet connectivity to those VMs. You could also configure this VM as a bastion host that lets you establish SSH connections to the other VMs on your private subnet. See NAT gateways and bastion hosts for more information.
  * A backup volume for storing warm backups.
  * A storage volume for storing log archives.



Different use cases might require additional devices or databases. For more information, see:

  * [SAP Note 1707361 - Inst. Systems Based on NW 7.1 and Higher: UNIX Db2 for LUW](https://launchpad.support.sap.com/#/notes/1707361).
  * The appropriate [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) for your SAP system with IBM Db2.

**Note:** You might be able to achieve a [sustained use discount](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) of up to 30% for your Compute Engine instances. Use the [pricing calculator](https://cloud.google.com/pricing/calculator) to help you estimate your actual costs.

## Resource requirements

In many ways, running IBM Db2 with SAP on Google Cloud is similar to running it in your own data center. You still need to think about computing resources, storage, and networking considerations.

For more information, see the appropriate [installation guide](https://help.sap.com/viewer/30839dda13b2485889466316ce5b39e9/CURRENT_VERSION/en-US/c8ed609927fa4e45988200b153ac63d1.html) for your SAP system with IBM Db2.

### VM configuration

IBM Db2 is certified to run on all Compute Engine machine types, including custom types. In most cases, use a machine type with two or more virtual CPUs.

For information about different Compute Engine machine types and their use cases, see [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) in the Compute Engine documentation.

#### CPU configuration

The number of vCPUs required varies depending on the application load on IBM Db2 LUW. You should allocate a minimum of two vCPUs to your IBM Db2 installation. To achieve best use of existing resources by your IBM Db2 system, follow the guidance in the [SAP on IBM Db2 for Linux, UNIX, and Windows documentation](https://help.sap.com/viewer/p/DB6) and adjust your computing resources as needed.

#### Memory configuration

Your IBM Db2 VM should have at least 4 GB of RAM per vCPU. Of this amount, approximately 80% of your RAM should be allocated to IBM Db2, with the rest allocated to the OS on which IBM Db2 is running.

The optimal amount of memory for your use case depends on the complexity of the queries you're running, the size of your data, the amount of parallelism you're using, and the level of performance you're expecting. For further guidance about optimizing your memory configuration, see the [SAP on IBM Db2 for Linux, UNIX, and Windows documentation](https://help.sap.com/viewer/p/DB6).

### Storage configuration

By default, each Compute Engine VM has a small [root persistent disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) that contains the operating system. In addition, you should create, attach, format, and mount additional disks for your database, your logs, and your stored procedures.

Your disk size and performance requirements will depend on your application. Size each device according to your needs.

For more information about the persistent disk options for IBM Db2, see Persistent disks.

For guidance from SAP on disk sizing, see:

  * [Required File Systems for IBM Db2 for Linux, UNIX, and Windows](https://help.sap.com/viewer/ce9e270ad34949969c16d09d1b099a26/CURRENT_VERSION/en-US/713eb64f45c6448c8dbe8a51b85680ee.html)
  * [1707361 - Inst. Systems Based on NW 7.1 and Higher: UNIX Db2 for LUW](https://launchpad.support.sap.com/#/notes/1707361)



### Supported IBM Db2 versions

You must use the SAP-certified IBM Db2 software fix pack (FP) levels. The use of other IBM Db2 software levels is not allowed.

For more information, see [SAP Note 101809 - DB6: Supported Db2 Versions and Fix Pack Levels](https://launchpad.support.sap.com/#/notes/101809).

### Supported IBM Db2 features

SAP supports most IBM Db2 features on Google Cloud. However, the following features are not supported:

  * Multi-partition Db2 databases
  * IBM Db2 pureScale feature



### Supported operating systems

SAP has certified Google Cloud to run IBM Db2 on the following SUSE Linux Enterprise Server (SLES), Red Hat Enterprise Linux (RHEL), and Windows Server operating system images:

  * SLES 12 SP2 or later
  * RHEL 7.4 or later
  * Windows Server 2016 or later



For more information about Compute Engine images, see [Images](https://docs.cloud.google.com/compute/docs/images).

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

Google Cloud also offers [local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) disk drives. Although local SSDs can offer some advantages over persistent disks, don't use them as part of an IBM Db2 system. VM instances with local SSDs attached cannot be stopped and then restarted.

### NAT gateways and bastion hosts

If your security policy requires truly internal VMs, you need to set up a NAT proxy manually on your network and a corresponding route so that VMs can reach the Internet. It is important to note that you cannot connect to a fully internal VM instance directly by using SSH. To connect to such internal machines, you must set up a bastion instance that has an external IP address and then tunnel through it. When VMs do not have external IP addresses, they can be reached only by other VMs on the network, or through a managed VPN gateway. You can provision VMs in your network to act as trusted relays for inbound connections, called bastion hosts, or network egress, called NAT gateways. For more transparent connectivity without setting up such connections, you can use a managed VPN gateway resource.

#### Using bastion hosts for inbound connections

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private-network VMs. This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH communication from the Internet.

![Bastion host shown in SSH scenario](https://docs.cloud.google.com/static/solutions/images/bastion.png)

You can achieve SSH access to VMs that do not have an external IP address by first connecting to a bastion host. A complete hardening of a bastion host is outside the scope of this article, but you can take some initial steps, including:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private VMs from only the bastion host.



By default, SSH on VMs is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private VM. Due to this two-step login, you should use SSH-agent forwarding to reach the target VM instead of storing the target VM's private key on the bastion host. You must do this even if you are using the same key-pair for both bastion and target VMs, as the bastion has direct access only to the public half of the key-pair.

#### Using NAT gateways for traffic egress

When a VM does not have an assigned, external IP address, it cannot make direct connections to external services, including other Google Cloud services. To allow these VMs to reach services on the Internet, you can set up and configure a [NAT gateway](https://docs.cloud.google.com/compute/docs/vpc/special-configurations#natgateway). The NAT gateway is a VM that can route traffic on behalf of any other VM on the network. You should have one NAT gateway per network. Be aware that a single-VM NAT gateway should not be considered highly available, and cannot support high traffic throughput for multiple VMs. See the [IBM Db2 Deployment Guide for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide) for instructions on how to set up a VM to act as a NAT gateway.

### Custom images

After your system is up and running, you can [create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images). You should create these images when you modify the state of your root persistent disk and want to be able to easily restore the new state. You should have a plan for how to manage the custom images you create. For more information, see [Image Management Best Practices](https://docs.cloud.google.com/solutions/image-management-best-practices).

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

By creating firewall rules, you can restrict all traffic on a given set of ports to specific source IP addresses. You should follow the minimum privilege model to restrict access to the specific IP addresses, protocols, and ports that need access. For example, you should always set up a [bastion host](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide#bastion_hosts_nat) and allow SSH into your SAP NetWeaver system only from that host.

#### Custom networks and firewall rules

You can use a network to define a gateway IP and the network range for the VMs attached to that network. All Compute Engine networks use the [IPv4](https://tools.ietf.org/html/rfc791) protocol. Every Google Cloud project is provided with a default network with preset configurations and firewall rules, but you should add a custom subnetwork and firewall rules based on a minimum privilege model. By default, a newly created network has no firewall rules and hence no network access.

Depending on your requirements, you might want to add additional subnetworks to isolate parts of your network. For more information, see [Subnetworks](https://docs.cloud.google.com/compute/docs/vpc#vpc_networks_and_subnets).

The firewall rules apply to the entire network and all the VMs in the network. You can add a firewall rule that allows traffic between VMs in the same network and across subnetworks. You can also configure firewalls to apply to specific target VMs by using the [tagging mechanism](https://docs.cloud.google.com/compute/docs/vpc/add-remove-network-tags).

Some SAP products, such as SAP NetWeaver, require access to certain ports. Be sure to add firewall rules to allow access to [the ports outlined by SAP](https://help.sap.com/viewer/575a9f0e56f34c6e8138439eefc32b16/2.0/en-US/616a3c0b1cc748238de9c0341b15c63c.html).

#### Routes

[Routes](https://docs.cloud.google.com/compute/docs/vpc/routes) are global resources attached to a single network. User-created routes apply to all VMs in a network. This means you can add a route that forwards traffic from VM to VM within the same network and across subnetworks without requiring external IP addresses.

For external access to Internet resources, launch a VM with no external IP address and configure another virtual machine as a NAT gateway. This configuration requires you to add your NAT gateway as a route for your SAP instance. For more information, see NAT gateways and bastion hosts.

#### Cloud VPN

You can securely connect your existing network to Google Cloud through a [VPN](https://wikipedia.org/wiki/Virtual_private_network) connection by using [IPsec](https://wikipedia.org/wiki/IPsec) by using Cloud VPN. Traffic traveling between the two networks is encrypted by one VPN gateway, then decrypted by the other VPN gateway. This protects your data as it travels over the Internet. You can dynamically control which VMs can send traffic down the VPN using [instance tags on routes](https://docs.cloud.google.com/compute/docs/vpc/using-routes#addingroute). Cloud VPN tunnels are billed at a static monthly rate plus standard egress charges. Note that connecting two networks in the same project still incurs standard egress charges. For more information, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

#### Securing a Cloud Storage bucket

If you use Cloud Storage to host your backups for your data and log, make sure you use TLS (HTTPS) while sending data to Cloud Storage from your VMs to protect data in transit. Cloud Storage automatically encrypts data at rest. You can specify your own encryption keys if you have your own key-management system.

#### Related security documents

Refer to the following additional security resources for your SAP environment on Google Cloud:

  * [Securely connecting to VM instances](https://docs.cloud.google.com/solutions/connecting-securely)
  * [Google Cloud Security](https://cloud.google.com/security)
  * [Compliance resource center](https://cloud.google.com/compliance)
  * [Google security overview](https://docs.cloud.google.com/docs/security/overview/whitepaper)
  * [Google infrastructure security design overview](https://docs.cloud.google.com/static/docs/security/infrastructure/design/resources/google_infrastructure_whitepaper_fa.pdf)



### Backup and recovery

You must have a plan for how to restore your system to operating condition if the worst happens.

For information about the backup and recovery of IBM Db2 systems that support SAP, see:

  * [Backup and Recovery](https://help.sap.com/viewer/db6_admin/ab9e4c2d68364a80b654ab70d398464c.html)
  * [Enabling Recoverability of the IBM Db2 for Linux, UNIX, and Windows Database](https://help.sap.com/viewer/ce9e270ad34949969c16d09d1b099a26/CURRENT_VERSION/en-US/182a0c2a00ef4a85b656c8359a1cfa31.html)



For general guidance about how to plan for disaster recovery using Google Cloud, see:

  * [How to Design a Disaster Recovery Plan](https://docs.cloud.google.com/solutions/designing-a-disaster-recovery-plan)
  * [Disaster Recovery Cookbook](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook)



## Automation for IBM Db2 deployments

Google Cloud provides a [Terraform](https://docs.cloud.google.com/docs/terraform) configuration file that you can use to automate the deployment of resources for IBM Db2 with Linux.

The `sap_db2.tf` configuration provided by Google Cloud for IBM Db2 provisions the following resources:

  * A Compute Engine instance based on the machine type of your choice.
  * Your choice of Red Hat Enterprise Linux (RHEL) or SUSE Linux Enterprise Server (SLES) operating system.
  * Compute Engine persistent disks.
  * Google Cloud's Agent for SAP



For the deployment automation instructions, see [Automated VM deployment for IBM Db2 on Linux using Terraform](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf).

## High-availability IBM Db2 clusters

You can set up a highly-available and disaster-tolerant IBM Db2 cluster on Google Cloud that is supported by SAP. The solution that you use depends on the version of IBM Db2 that you want to use:

  * (**Recommended solution**) To deploy IBM Db2 version later than 11.5, see HA for IBM Db2 versions later than 11.5.
  * (**Legacy solution**) To deploy IBM Db2 version 11.5 or earlier, see HA for IBM Db2 version 11.5 or earlier.



### HA for IBM Db2 versions later than 11.5

To run IBM Db2 version **11.5.8 or later** , you can configure a two-host HADR Pacemaker cluster by using the clustering solution provided by IBM for Db2. This solution includes the following components:

  * SAP NetWeaver installed as a distributed system.

For information about setting this up, see the SAP document [SAP Products Based on SAP NetWeaver 7.3 EHP1 to 7.52 Supported for Installation Using Software Provisioning Manager 1.0](https://help.sap.com/docs/SLTOOLSET/ce9e270ad34949969c16d09d1b099a26/caf54343cfaa420ebec647a7ec6e5c32.html?version=CURRENT_VERSION). For information about how to enable your SAP system with a virtual hostname and IP address, see the SAP document [Virtual host name and IP address](https://help.sap.com/docs/db6/administration/virtual-host-name-and-ip-address).

  * An IBM Db2 integrated Pacemaker software stack.

For more information, see the IBM document [Installing the Pacemaker cluster software stack](https://www.ibm.com/docs/en/db2/11.5?topic=manager-installing-pacemaker-cluster).

  * An IBM Db2 HADR pair.

For more information, see the SAP document [Configuring the HADR pair](https://help.sap.com/docs/DB6/e3eefec5d20740f4872652a475457348/967b625fc71c429191a89b03e250ccdb.html).

  * A Pacemaker-managed HA cluster.

For more information, see the IBM document [Creating an HADR Db2 instance on a Pacemaker-managed Linux cluster](https://www.ibm.com/docs/en/db2/11.5?topic=option-creating-pacemaker-managed-hadr-db2-instance).

  * A virtual IP (VIP) implementation by using Network Load Balancer.

For more information, see [Configure VIP for two-node Db2 HADR Pacemaker cluster with on Google Cloud](https://www.ibm.com/docs/en/db2/latest?topic=cloud-configure-vip-hadr-pacemaker-network-load-balancer).




#### Solution support

Because this solution includes components managed by different vendors, use the following information to get support for deploying or troubleshooting this solution:

  * If you need support with internal Application Load Balancer or the fencing agent provided by Google Cloud, then contact Cloud Customer Care.
  * For any other issue, such as those related to Pacemaker, you must contact IBM support.



#### Relevant SAP notes

For information from SAP about Db2 support for Pacemaker cluster software, see the following SAP notes:

  * [3100287 - DB6: Db2 Support for Pacemaker Cluster Software](https://me.sap.com/notes/3100287)
  * [3100330 - DB6: Using Db2 HADR with Pacemaker Cluster Software](https://me.sap.com/notes/3100330)



### HA for IBM Db2 version 11.5 or earlier

In this **legacy solution** , the HA cluster is configured and managed by IBM Tivoli System Automation for Multiplatforms (TSAMP) and uses the IBM Db2 HADR function for replication purposes.

Applications connect to the primary IBM Db2 server through a floating IP address, which, in the event of a failover, TSAMP reassigns to the standby server.

The IBM Db2 HADR function supports up to three standby servers. On Google Cloud, the host VMs in the cluster must be in the same region but can be in different zones within the region.

SAP support for DB2 HA clusters on Google Cloud is listed in [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432).

For information about the IBM Db2 features that SAP supports, see [SAP Note 1555903](https://launchpad.support.sap.com/#/notes/1555903).

#### Deployment architectures

You can deploy the host VMs in a IBM Db2 HA cluster across multiple Compute Engine zones in the same region or, if necessary, you can deploy them in a single zone.

For the highest availability, deploy each host VM in different zone.

The following diagram shows a multi-zone deployment that uses a static route implementation for the floating IP address.

![Each host of a Db2 HA cluster is deployed in a different zone.](https://docs.cloud.google.com/static/sap/docs/images/db2-ha-multizone-routes.svg)

The following diagram shows a single-zone deployment that uses an alias IP implementation for the floating IP address.

![Both hosts of a Db2 HA cluster are deployed in the same zone.](https://docs.cloud.google.com/static/sap/docs/images/db2-ha-alias-ip.svg)

#### Required documentation

To deploy an IBM Db2 HA cluster for SAP, you need to follow both SAP and Google Cloud documentation.

  * The SAP-provided [IBM Db2 high availability solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf) covers the general cluster requirements and the installation and configuration of the IBM Db2 instances, TSAMP, and the HA cluster.
  * The Google Cloud-provided [IBM Db2 for SAP High-Availability Cluster Deployment Guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide) covers how to set up the Google Cloud resources and certain cluster configuration tasks that are specific to Google Cloud.



You might need to refer to additional SAP or IBM documentation during the installation of the SAP and IBM components.

#### Requirements specific to an IBM Db2 HA cluster on Google Cloud

On Google Cloud, SAP supports IBM Db2 HA clusters only on RHEL or SLES operating systems.

For the Google Cloud software requirements for the IBM Db2 instances, see Resource requirements.

For IBM TSAMP, use the latest available version that is supported by your IBM Db2 version and your operating system.

For all other hardware and software requirements, see [IBM Db2 high availability solution: IBM Tivoli System Automation for Multiplatforms](https://help.sap.com/doc/a7ba6b8cc8dc46309c2f93bcfc417133/CURRENT_VERSION/en-US/DB6_SAMP_Guide.pdf).

#### Floating IP addresses for IBM Db2 HA clusters on Google Cloud

An IBM Db2 HA cluster for SAP uses a floating IP address, which is also known as a "virtual IP address" or "shared IP address".

For an IBM Db2 HA cluster, Google Cloud can implement a floating IP address by using either a Google Cloud static [route](https://cloud.google.com/vpc/docs/routes) or a Google Cloud [alias IP](https://cloud.google.com/vpc/docs/alias-ip) address.

The static route implementation is recommended for multi-zone IBM Db2 HA clusters. Multi-zone deployments help ensure that a single-zone failure does not take down your IBM Db2 system.

However, if your network architecture does not support static routes or you need to avoid solutions like IP overlay or complex routing, you can use the alias IP address implementation with a single-zone IBM Db2 HA cluster. Alias IP addresses are not recommended for multi-zone deployments because the reallocation of the alias might not be guaranteed in the event of a zonal failure.

Depending on whether you choose the static route implementation or the alias IP implementation, the requirements for the IP address that you use for your floating IP address are different.

The use of a static route requires that you select an IP address for your floating IP address that is:

  * Outside of the IP ranges of your existing Virtual Private Cloud subnets where the VMs reside.
  * Does not conflict with any external IP addresses in your extended network.



Consult with your network administrator to determine a suitable IP address for a static route implementation.

The use of an alias IP address requires you to reserve an IP address from your subnetwork IP range for use as the floating IP address.

For more information about floating IP addresses on Google Cloud, see [Best Practices for Floating IP Addresses](https://cloud.google.com/solutions/best-practices-floating-ip-addresses).

SAP recommends the use of floating IP addresses in IBM Db2 HA clusters. SAP does support Automatic Client Reroute (ACR), provided that you account for all requirements and limitations of this method is recognized. For more information, see [SAP Note 1568539](https://launchpad.support.sap.com/#/notes/1568539).

#### The network tiebreaker

IBM Db2 HA clusters commonly send an ICMP request (ping) to a network gateway, which serves as the default _network tiebreaker_ to determine which node should take over when communication between the nodes in a cluster is lost.

Because network gateways on Google Cloud do not respond to ICMP requests, use any other IP address that can be pinged and that is highly available itself. For example, you could use the virtual IP address of your SAP application Central Services instance or the Google DNS, 8.8.8.8.

If the network tiebreaker cannot respond to ICMP requests during setup, the setup fails.

Other network tiebreakers exist and are defined by IBM. For more information, see [Configuring the tiebreaker](https://www.ibm.com/support/knowledgecenter/en/SSRM2X_4.1.0/com.ibm.samp.doc_4.1/sampugsettingup_tiebreaker.html).

#### Setup tools for a Db2 HA cluster

You can use either one of the following tools that SAP and IBM provide to configure an IBM Db2 HADR cluster:

  * The SAP cluster setup tool (`sapdb2cluster.sh`).
  * The IBM DB2 high availability instance configuration utility (`db2haicu`).



##### SAP Db2 cluster setup tool (`sapdb2cluster.sh`)

SAP recommends the SAP-provided cluster setup tool, `sapdb2cluster.sh`, to configure and create a Db2 HA cluster. The [Google Cloud deployment instructions](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide) use the SAP cluster set up tool. The cluster setup tool simplifies much of the cluster setup and ensures that it meets SAP support requirements.

Before you create the HA cluster with the SAP cluster setup tool, one of the steps in the Google Cloud deployment instructions makes a minor modification to the SAP cluster setup tool, sapdb2cluster.sh, so that the tool skips the creation of the default `IBM.ServiceIP` resource class.

Resources created from the IBM TSAMP [`IBM.ServiceIP` resource class](https://www.ibm.com/support/knowledgecenter/en/SSRM2X_4.1.0/com.ibm.samp.doc_4.1/sampugserviceipstarted.html) issue gratuitous ARP requests, which are not supported in VPC networks on Google Cloud, as explained in [Challenges with migrating floating IPs to Compute Engine](https://docs.cloud.google.com/solutions/best-practices-floating-ip-addresses#challenges_with_migrating_floating_ip_addresses_to_compute_engine).

To download the latest version of the cluster setup tool, see [SAP Note 960843](https://launchpad.support.sap.com/#/notes/960843).

##### The IBM DB2 high availability instance configuration utility (`db2haicu`)

As an alternative to using the SAP cluster setup tool, you can use the IBM `db2haicu` utility instead, which also provides an interactive interface. The SAP cluster setup tool uses `db2haicu` for the cluster setup.

When using the `db2haicu` utility, you must configure the HADR relationship first, before you can use the `db2haicu` utility to setup the cluster. While the overall setup procedure might be more complex with the `db2haicu` utility, the utility allows for more customization for complex network configurations or other requirements that are specific to your environment.

Always follow SAP and IBM guidelines when you use the `db2haicu` utility.

For more information about `db2haicu`, see [the IBM Db2 documentation](https://www.ibm.com/support/knowledgecenter/en/SSEPGG).

#### Google Cloud helper script for IBM TSAMP cluster integration

To enable the IBM Db2 HA cluster to call the appropriate Google Cloud API commands to start, stop, and monitor the TSAMP resource for the floating IP address, you need to download a helper script from Google Cloud to the host VMs. When you create the floating IP address resource in IBM TSAMP, you reference the Google Cloud helper script.

## Licenses

This section provides information about licenses that you need to run IBM Db2 with SAP systems on Google Cloud.

### IBM Db2 licenses

When running IBM Db2 on Google Cloud, you must bring your own license (BYOL). You can obtain Db2 licenses from SAP or from IBM. For more information about licensing and support, see the following SAP notes:

  * [1168456 - DB6: Support Process and End of Support Dates for IBM DB2 LUW](https://launchpad.support.sap.com/#/notes/1168456)
  * [1260217 - DB6: Software Components Contained in DB2 License from SAP](https://launchpad.support.sap.com/#/notes/1260217)
  * [816773 - DB6: Installing the Application-Specific Db2 License from SAP](https://me.sap.com/notes/816773)



For more information about SAP licensing, contact SAP.

### Operating system licenses

In Compute Engine, there are two ways to license SLES, RHEL, and Windows Server:

  * With pay-as-you-go licensing, your Compute Engine VM hourly cost includes licensing. Google manages the licensing logistics. Your hourly costs are higher, but you have complete flexibility to increase and decrease your costs, as needed. This is the licensing model used for Google Cloud public images that include SLES, RHEL, and Windows Server.

**Important:** RHEL, SLES, and Windows Server are premium images. Premium images charge for OS licenses in addition to standard VM charges. For details about pricing, refer to the [pricing for RHEL images](https://cloud.google.com/compute/pricing#red_hat_enterprise_linux_rhel_images), [pricing for SUSE images](https://docs.cloud.google.com/compute/disks-image-pricing#suse_images), and [pricing for Windows Server images](https://docs.cloud.google.com/compute/disks-image-pricing#windows_server_pricing).
  * With BYOL, your Compute Engine VM costs are lower because the licensing isn't included. You must migrate an existing license or purchase your own license, which means paying up front, and you have less flexibility.




## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Google Cloud infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



For information about SAP support for Db2, see [SAP Note 1168456 - DB6: Support Process and End of Support Dates for IBM DB2 LUW](https://launchpad.support.sap.com/#/notes/1168456)

## What's next

To deploy IBM Db2 on Google Cloud, see the following resources:

  * To manually configure a compute instance on Windows or Linux to run IBM DB2 with an SAP system on Google Cloud, see [Manual VM deployment for IBM Db2 on Linux and Windows for SAP](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide).
  * To use Terraform to automate the deployment of resources needed to run IBM Db2 with an SAP system on Google Cloud, see [Automated VM deployment for IBM Db2 on Linux for SAP](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-deployment-guide-tf).
  * To deploy the IBM Db2 database for use with a highly available SAP system on Google Cloud, see: 
    * (**Recommended solution**) To deploy IBM Db2 version later than 11.5, see the following resources. This solution includes information about a fully-supported IBM configuration and integrated Pacemaker configuration that utilizes internal Application Load Balancer. 
      * [Installing the Pacemaker cluster software stack](https://www.ibm.com/docs/en/db2/latest?topic=manager-installing-pacemaker-cluster)
      * [Configuring the HADR pair](https://help.sap.com/docs/db6/administration/configuring-hadr-pair)
      * [Creating an HADR Db2 instance on a Pacemaker-managed Linux cluster](https://www.ibm.com/docs/en/db2/latest?topic=option-creating-pacemaker-managed-hadr-db2-instance)
      * [Configure VIP for two-node Db2 HADR Pacemaker cluster with Network Load Balancer on Google Cloud](https://www.ibm.com/docs/en/db2/latest?topic=cloud-configure-vip-hadr-pacemaker-network-load-balancer)
    * (**Legacy solution**) To deploy IBM Db2 version 11.5 or earlier, see [IBM Db2 high-availability cluster for SAP deployment guide](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-ha-deployment-guide). This solution includes information about how to configure IBM Db2 on an HA cluster that uses the IBM TSAMP solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
