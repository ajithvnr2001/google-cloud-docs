---
url: https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide/
title: High-availability planning guide for SAP NetWeaver on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:45.750153+00:00
---

# High-availability planning guide for SAP NetWeaver on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  High-availability planning guide for SAP NetWeaver on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of the options, recommendations, and general concepts that you need to know before you deploy a high-availability (HA) SAP NetWeaver system on Google Cloud.

This guide assumes that you already have an understanding of the concepts and practices that are generally required to implement an SAP NetWeaver high-availability system. Therefore, the guide focuses primarily on what you need to know to implement such a system on Google Cloud.

If you need to know more about the general concepts and practices that are required to implement an SAP NetWeaver HA system, see:

  * The SAP best practices document [Building High Availability for SAP NetWeaver and SAP HANA on Linux](https://support.sap.com/content/dam/SAAP/SAP_Activate/AGS_70.pdf)
  * [The SAP NetWeaver documentation](https://help.sap.com/viewer/product/SAP_NETWEAVER/ALL/en-US)



This planning guide focuses solely on HA for SAP NetWeaver and does not cover HA for database systems. For information about HA for SAP HANA, see the [SAP HANA high availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide).

## Deployment architecture

The following diagram shows a basic Linux HA cluster that uses Pacemaker cluster software.

The cluster includes two hosts: a primary host and a secondary host. Each host is located in a different zone within the same region.

The cluster uses the SAP Standalone Enqueue Server 2 (ENSA2). For a description of a cluster that uses the earlier version of the Standalone Enqueue Server (ENSA1), see Standalone Enqueue Server (ENSA1) architecture.

The active Central Services instance is on the primary host. The active Enqueue Replication Server 2 (ERS) instance is on the secondary host. Central Services and ERS each have their own virtual IP address (VIP). In the diagram, "Central Services" represents either ABAP SAP Central Services or, for a Java stack, SAP Central Services.

For more information about the Standalone Enqueue Server 2 in HA configurations, see [SAP Note 2711036 - Usage of the Standalone Enqueue Server 2 in an HA Environment](https://launchpad.support.sap.com/#/notes/2711036).

![A basic HA setup for SAP NetWeaver on Google Cloud with two hosts,
each in a different zone](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ha-linux.svg)

### Standalone Enqueue Server (ENSA1) architecture

In the following diagram, the active Central Services instance, which contains the lock management, or Enqueue service, and the inactive Enqueue Replication Server (ERS) instance are on the primary host. The active ERS instance and the inactive Central Services instance are on the secondary host. Each Central Services and ERS pair has its own virtual IP address (VIP). In the diagram, "Central Services" represents either ABAP SAP Central Services or, for a Java stack, SAP Central Services.

In the event of a failure, the HA clustering software has to relocate the Standalone Enqueue Server to the node where the Enqueue Replication Server is running in order to retain the lock information. Consider updating your system to use Standalone Enqueue Server 2, if your software version supports it. For more information refer to [SAP Note 2630416 - Support for Standalone Enqueue Server 2](https://launchpad.support.sap.com/#/notes/2630416).

![A basic HA setup for SAP NetWeaver on Google Cloud with two hosts,
each in a different zone](https://docs.cloud.google.com/static/sap/docs/images/netweaver-ha-linux-ensa-1.svg)

## The high availability of Google Cloud infrastructure

Google Cloud is highly available by design, with a redundant infrastructure of data centers around the world that contain zones designed to be independent from each other. Zones usually have power, cooling, networking, and control planes that are isolated from other zones. If a single failure event were to occur, in most cases, it would affect only a single zone.

In some cases, you might meet your availability requirements without implementing all of the traditional, on-premises safeguards against hardware, storage, and networking failures, which could save you both time and money.

Before you design and implement your high-availability strategy on Google Cloud, review the [Google Cloud Service Level Agreements](https://cloud.google.com/terms/sla/).

For general information about the reliability, privacy, and security of Google Cloud, see [Reliability](https://support.google.com/googlecloud/answer/6056635).

### HA clustering options for SAP systems on Google Cloud

You define a high-availability (HA) cluster for SAP NetWeaver on Google Cloud by using the same types of third-party HA cluster software that you might use in an on-premises installation. The HA cluster software monitors the health of the systems and manages the failover when problems occur.

You can use a number of different HA cluster software solutions, such as the following:

  * Red Hat Enterprise Linux (RHEL) for SAP Solutions
  * SUSE Linux Enterprise Server (SLES) for SAP Applications
  * Windows Server Failover Clustering



### Linux HA clustering software

Recent versions of both RHEL and SLES include integrated HA support that is enabled specifically for Google Cloud. To check if your Linux version includes Google Cloud-enabled HA support, look for "GC-HA" in the table in [Operating system support for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table).

While using Oracle Database based installations, to make the SAP Central Services instance highly available, you need to ensure the following:

  * A Compute Engine instance that runs Oracle Database or any other closely-coupled auxiliary system must use a [supported operating system](https://docs.cloud.google.com/sap/docs/oracle-planning#supported_operating_systems).
  * As an exception to the preceding requirement, a compute instance that runs the SAP Central Services instance like the ASCS or the ERS, can use any SAP-certified OS as long as that compute instance doesn't host the Oracle Database or has any Oracle software installed.



For more information about running Oracle Database with SAP NetWeaver based applications, see [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning).

### Windows HA clustering software

On Windows Server you use Windows Server Failover Clustering (WSFC) to create the HA cluster, as described in [Running Windows Server Failover Clustering](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering).

On Google Cloud, the routing of incoming traffic to the active node in a WSFC cluster is managed by Cloud Load Balancing, which does not require an alias IP or static route VIP implementation.

Cloud Load Balancing uses health checks to determine the active node.

## Google Cloud zones, regions, and SAP NetWeaver HA deployments

Deploy the nodes of your HA cluster across two or more Compute Engine zones within the same region. Deploying the nodes in different zones ensures that they are on different physical machines and also protects against the very unlikely possibility of a zonal failure.

Keeping the zones within the same region ensures that the nodes are close enough geographically to meet SAP latency requirements for high-availability systems.

## Compute Engine virtual machines and SAP NetWeaver HA deployments

To support high availability, Compute Engine VMs are backed by live migration and automatic restart.

### Compute Engine live migration

Compute Engine monitors the state of the underlying infrastructure. When an infrastructure maintenance event occurs, Compute Engine automatically migrates your instance away from the event and, if possible, keeps your instance running during the migration. No user intervention is required.

In the case of major outages, there might be a slight delay between when the instance goes down and when it is available.

In most cases, live migration events occur without impacting the HA cluster. However, test your HA cluster by simulating a live migration of the active host after your HA cluster is set up and the systems are running, especially if your HA cluster monitor is configured with a low failover threshold. For more information about simulating a live migration event, see [Testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies).

A migrated instance is identical to the original instance, including the instance ID, private IP address, and all instance metadata and storage.

By default, standard instances are set to live migrate. We recommend not changing this setting.

For more information, see [Live migrate](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#live_migrate).

### Compute Engine automatic restart

If your instance is set to terminate when there is a maintenance event, or if your instance crashes because of an underlying hardware issue, you can set up Compute Engine to automatically restart the instance. By default, instances are set to automatically restart. We recommend not changing this setting.

For more information about automatic restart, see [Automatic restart](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#autorestart).

## Shared storage options for HA SAP systems on Google Cloud

The SAP NetWeaver global file system is a single point of failure that needs to be available to all of the SAP NetWeaver instances in your HA system. To ensure the availability of the global file system on Google Cloud, you can use either highly available shared storage or replicated zonal persistent disks.

For a high-availability shared storage solution you can use Google Cloud [Filestore](https://docs.cloud.google.com/filestore/docs) or solutions such as [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) or [NetApp Cloud Volumes ONTAP](https://docs.netapp.com/us-en/storage-management-cloud-volumes-ontap/index.html).

When using [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) as the shared storage solution, you must account for potential I/O pauses during [NetApp Volumes maintenance events](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#maintenance_event-related_application_disruptions). If Pacemaker timeouts are not adjusted, then I/O pauses can trigger cluster failovers during the NetApp Volumes maintenance events. When you're deploying a cluster, make sure that you increase the interval and timeout monitor settings for the `Filesystem` and `SAPInstance` resources. For more information, see the Pacemaker configuration details in the following resources:

  * [RHEL deployment guide](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#create_the_file_system_resources)
  * [SLES deployment guide](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#create_the_file_system_resources)
  * [Google Cloud NetApp Volumes application resilience](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/application-resilience#use_cluster_software_applications_to_automate_failovers).



The Regional (formerly Enterprise) tier of Filestore can be used for multi-zone high-availability deployments and the Basic tier of Filestore can be used for single-zone deployments.

For replication of zonal persistent disks for Linux systems, you can use a Distributed Replicated Block Device (DRBD) to replicate the persistent disks that contain the SAP global file system between the nodes in your HA cluster.

Although Compute Engine regional persistent disks offer synchronously replicated block storage across zones, they are not supported for SAP NetWeaver HA systems.

For more information about storage options on Google Cloud, see:

  * [File sharing solutions for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/filers-for-sap)
  * [File storage on Compute Engine](https://docs.cloud.google.com/architecture/filers-on-compute-engine)
  * [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks)



## Networking options for HA SAP systems

When you set up your network for your HA cluster, in addition to completing the steps in [Creating a network](https://docs.cloud.google.com/sap/docs/netweaver-deployment-linux-dm#creating_a_network), you need to complete the following HA-specific tasks:

  * Choose your VIP implementation for Linux systems, as described in the following section. Windows systems use an internal load balancer, which doesn't require the same VIP solutions as Linux systems.
  * Define the communication path between the SAP Central Services instance and the Enqueue Replication Server instance.
  * Define firewall rules to support your defined communication paths.



## Virtual IP implementation on Google Cloud

A high-availability cluster uses a _floating_ or _virtual_ IP address (VIP) to move its workload from one cluster node to another in the event of an unexpected failure or for scheduled maintenance. The IP address of the VIP doesn't change, so client applications are unaware that the work is being served by a different node.

A VIP is also referred to as a _floating IP address_.

On Google Cloud, VIPs are implemented slightly differently than they are in on-premises installations, in that when a failover occurs, gratuitous ARP requests cannot be used to announce the change. Instead, you can implement a VIP address for an SAP HA cluster by using one of the following methods:

  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) failover support (recommended).
  * Google Cloud static [routes](https://docs.cloud.google.com/vpc/docs/routes).
  * Deprecated: Google Cloud [alias IP](https://docs.cloud.google.com/vpc/docs/alias-ip) addresses. Use [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) or static [routes](https://docs.cloud.google.com/vpc/docs/routes) instead.



### Internal passthrough Network Load Balancer VIP implementations

A load balancer typically distributes user traffic across multiple instances of your applications, both to distribute the workload across multiple active systems and to protect against a processing slowdown or failure on any one instance.

The [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) also provides failover support that you can use with Compute Engine health checks to detect failures, trigger failover, and reroute traffic to a new primary SAP system in an OS-native HA cluster.

Failover support is the recommended VIP implementation for a variety of reasons, including:

  * Load balancing on Compute Engine offers a [99.99% availability](https://cloud.google.com/compute/sla) SLA.
  * Load balancing supports multi-zone high-availability clusters, which protects against zone failures with predictable cross-zone failover times.
  * Using load balancing reduces the time required to detect and trigger a failover, usually within seconds of the failure. Overall failover times are dependent on the failover times of each of the components in the HA system, which can include the hosts, database systems, application systems, and more.
  * Using load balancing simplifies cluster configuration and reduces dependencies.
  * Unlike a VIP implementation that uses routes, with load balancing, you can use IP ranges from your own VPC network, allowing you to reserve and configure them as needed.
  * Load balancing can easily be used to reroute traffic to a secondary system for planned maintenance outages.



When you create a [health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts?hl=en) for a load balancer implementation of a VIP, you specify the host port that the health check probes to determine the health of the host. For an SAP HA cluster, specify a target host port that is in the private range, 49152-65535, to avoid clashing with other services. On the host VM, configure the target port with a secondary helper service, such as the socat utility or HAProxy.

For database clusters in which the secondary, standby system remains online, the health check and helper service enables load balancing to direct traffic to the online system that is currently serving as the primary system in the cluster.

Using the helper service and port redirection, you can trigger a failover for planned software maintenance on your SAP systems.

**Note:** When you use a load balancer, by default, you can't send TCP network traffic directly from a secondary node to the primary node through the VIP address. Any traffic that is sent to the VIP from a back-end cluster node is returned by the load balancer's back-end service to the sending node. The health check is ignored. For more information see [Sending requests from load balanced VMs](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#test-from-backend-vms).

For more information about failover support, see [Configuring failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover).

To deploy an HA cluster with a load-balancer VIP implementation, see:

  * [Terraform: SAP HANA high-availability cluster configuration guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-tf-deployment)
  * [HA cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel)
  * [HA cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles)



### Static route VIP implementations

The static route implementation also provides protection against zone failures, but requires you to use a VIP outside of the IP ranges of your existing VPC subnets where the VMs reside. Consequently, you also need to make sure that the VIP does not conflict with any external IP addresses in your extended network.

Static route implementations can also introduce complexity when used with shared VPC configurations, which are intended to segregate network configuration to a host project.

If you use a static route implementation for your VIP, consult with your network administrator to determine a suitable IP address for a static route implementation.

### Alias IP VIP implementations

Alias IP VIP implementations are deprecated for multi-zone HA deployments because, if a zone fails, the reallocation of the alias IP to a node in a different zone can be delayed or time out. Implement your VIP with an internal passthrough Network Load Balancer with failover support instead.

If you have existing multi-zone SAP HA clusters that use an alias IP implementation for the VIP, you can migrate to an internal passthrough Network Load Balancer implementation without changing your VIP address. Both alias IP addresses and internal passthrough Network Load Balancers use IP ranges from your VPC network.

While alias IP addresses must not be used for VIP implementations in multi-zone HA clusters, they have other use cases in SAP deployments. For example, they can be used to provide a logical host name and IP assignments for flexible SAP deployments, such as those managed by SAP Landscape Management.

### General best practices for VIPs on Google Cloud

For more information about VIPs on Google Cloud, see [Best Practices for Floating IP Addresses](https://docs.cloud.google.com/solutions/best-practices-floating-ip-addresses).

## Configuring high-availability clusters for SAP NetWeaver on Google Cloud

Google Cloud provides a Terraform configuration file that you can use to automate the deployment of SAP NetWeaver HA systems or you can deploy and configure your SAP NetWeaver HA systems manually.

To automate the deployment of SAP NetWeaver HA systems, you complete the Terraform configuration file and use standard Terraform commands to apply the configurations. For deployment instructions, see:

  * [Terraform: HA cluster configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles-tf)
  * [Terraform: HA cluster configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel-tf)



The automated deployment method deploys Google Cloud infrastructure for an SAP NetWeaver system that is fully supported by SAP and that adheres to the best practices of both SAP and Google Cloud.

For SAP NetWeaver, the automated deployment method deploys a performance-optimized, high-availability Linux cluster that includes:

  * Automatic failover.
  * Automatic restart.
  * A reservation of the virtual IP address (VIP) that you specify.
  * Failover support provided by [internal TCP/UDP load balancing](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview), which manages routing from the virtual IP address (VIP) to the nodes of the HA cluster.
  * A firewall rule that allows [Compute Engine health checks](https://cloud.google.com/load-balancing/docs/health-check-concepts) to monitor the VM instances in the cluster.
  * The Pacemaker high-availability cluster resource manager.
  * A Google Cloud fencing mechanism, the `fence_gce` fencing agent.
  * A VM with the required Persistent Disk or Hyperdisk volumes for each SAP NetWeaver instance.



For instructions to deploy and manually configure an HA cluster on Google Cloud for SAP NetWeaver, see:

  * [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles)
  * [HA cluster manual configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
