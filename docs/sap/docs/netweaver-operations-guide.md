---
url: https://docs.cloud.google.com/sap/docs/netweaver-operations-guide/
title: SAP NetWeaver Operations Guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:47.590940+00:00
---

# SAP NetWeaver Operations Guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-operations-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP NetWeaver Operations Guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of how to manage IT ops for a running SAP NetWeaver system on Compute Engine. This guide does not cover the specifics of managing the SAP NetWeaver product. Google Cloud is certified for running SAP NetWeaver application servers ABAP and Java, and SAP products based on these application server stacks.

  * To learn how to operate your deployment of SAP NetWeaver, see the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).
  * To learn how to plan your deployment of SAP NetWeaver, see the [SAP NetWeaver on Google Cloud Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide) and the [SAP NetWeaver Master Guide](https://help.sap.com/doc/18cb1a50b9924bc3b94c2988cc8c51d9/7.5/en-US/mg_nw_75.pdf).
  * To learn how to deploy and prepare Google Cloud resources for an SAP NetWeaver system, see the deployment guide for your operating system: 
    * [SAP NetWeaver on Linux Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-linux)
    * [SAP NetWeaver on Windows Deployment Guide](https://docs.cloud.google.com/sap/docs/netweaver-deployment-guide-windows)



## Managing Compute Engine VM instances

This section shows how to perform administrative tasks typically required to operate SAP NetWeaver on Compute Engine, including information about starting and stopping systems.

### Managing VM lifetime

This section provides information about how to manage the running state of your Compute Engine VMs.

#### Maintaining VM availability

Compute Engine offers availability policies that determine how a VM behaves during certain infrastructure-related events. For VM instances in your SAP NetWeaver implementation, it is important that you do not disable the following features:

  * [Live migrate](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#live_migrate), which enables Compute Engine to keep your instance running when responding to an infrastructure maintenance event.
  * [Automatic restart](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#autorestart), which enables Compute Engine to restart your instance in the event of an instance crash. Note that the SAP system does not automatically restart.



#### Stopping a VM

You can stop one or multiple SAP NetWeaver hosts at any time; stopping a VM instance shuts down the instance. If the shutdown doesn't complete within 2 minutes, the instance is forced to halt. As a best practice, you should first stop SAP NetWeaver before you stop the instance.

**Note:** The private IP associated with the instance is not released after you stop the instance, so when you start the instance again, it will start with the same private IP address, network, and storage configuration as before.

Stopping a VM causes Compute Engine to send the [ACPI power-off signal](https://wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface) to the VM instance. After it is stopped, you are not billed for the VM instance.

If you have persistent disks attached to the VM, the disks are not deleted and you continue to be charged for them. If the data in the persistent disk is important, you can either:

  * Keep the disk.
  * Create a snapshot of the persistent disk and then delete the disk. This option can help you save on costs. You can create another disk from the snapshot when you need the data again.



To stop a VM:

  1. In the Google Cloud console, navigate to the:

[VM INSTANCES PAGE](https://console.cloud.google.com/compute/instances)

  2. Select one or more instances that you want to stop.

  3. At the top of the **VM instances** page, click _stop_**STOP**.




For alternatives and more information, see [Stopping an instance](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#stop_an_instance).

#### Restarting a VM

To restart a VM:

  1. In the Google Cloud console, navigate to the:

[VM INSTANCES PAGE](https://console.cloud.google.com/compute/instances)

  2. Select the instances that you want to restart.

  3. At the top right-hand of the page, click _play_arrow_**START**.




For alternatives and more information, see [Restarting an instance](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance#restarting_a_stopped_instance).

### Modifying a VM

You can change various attributes of a VM, including the VM type, after the VM is deployed. Some changes might require you to restore your SAP system from backups, while others only require you to restart the VM.

For more information, see [Modifying VM configurations for SAP systems](https://docs.cloud.google.com/sap/docs/modifying_vm_configurations).

## Capturing system state

This section describes scenarios that require saving the state of your system, and the Compute Engine features that you can use for these purposes.

### Using snapshots

You can create a snapshot of a persistent disk at any time to generate a point-in-time copy of the disk state. Compute Engine stores multiple copies of each snapshot, across multiple locations, with automatic checksums to ensure the integrity of your data.

Snapshots are useful for the following use cases:

Use case | Details  
---|---  
Migrate to a different type of storage. | You can use snapshots to move a persistent disk from one disk type, _standard_ or _SSD_ , to the other type. See [ Restoring a snapshot to a different disktype](https://docs.cloud.google.com/compute/docs/disks/restore-and-delete-snapshots#restoresnapshotlargersize) in the Compute Engine documentation.  
Migrate SAP NetWeaver to another zone. | You can use snapshots to move your SAP NetWeaver system from one zone to another zone in the same region, or even from one region to another region. See Moving VMs between regions and zones.  
Provide an easy, software-independent, and cost-effective backup solution. | Back up your attached persistent disks by using snapshots. You can back up your root disk and SAP NetWeaver installed binaries.  
Snapshots can be useful for taking backups of your database systems. However, depending on your implementation, you might want to use a different approach. For guidance about how to back up and restore databases, see the guides listed in Database operations.  
  
To obtain a consistent snapshot, you must either stop SAP NetWeaver or stop the database from writing to the file system.

To create a snapshot, follow the Compute Engine instructions for [creating snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots). Pay careful attention to the preparation steps, such as flushing the disk buffers to disk, to make sure that the snapshot is consistent.

### Creating images

To capture the state of a boot disk, you can create a _custom image_. An image is different from a backup because you use an image to create new VM instances that are based on a single, source VM.

**Important:** Creating an image is a destructive operation with regards to the source VM, so this is not something you would normally do in your live, production system.

When you followed the SAP NetWeaver on Google Cloud Deployment Guide, you should have created one or more images at the end of the deployment steps. However, you might want to create new images after you make important changes to the system, such as installing an update of SAP NetWeaver binaries or upgrading the SAP NetWeaver version.

For instructions, see:

  * [Creating, Deleting, and Deprecating Custom Images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), for Linux-based systems.
  * [Creating a Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image), for Windows-based systems.



### Moving VMs between regions and zones

Compute Engine enables you to move VMs between zones in the same region and zones in different regions. You might want to move a VM if, for example, a new region or zone becomes available that would give you better performance, or if a zone becomes deprecated.

The Compute Engine documentation contains [detailed instructions about how to move your VM to another zone](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).

Here are considerations for SAP NetWeaver:

  * SAP can run only in certain zones because of machine-type restrictions. See the [SAP NetWeaver on Google Cloud Planning Guide](https://docs.cloud.google.com/sap/docs/netweaver-planning-guide) for details.
  * Migrating the VM causes the VM's ID to change. This change triggers an SAP HW Key change, which requires you to import a new SAP license.
  * You can use the same hostname in the new zone, if it isn't already in use. If the hostname changes, you need to use the generic operations feature of SAP's SWPM to run a rename operation to change the SAP NetWeaver hostname.



## Database operations

This section provides resources for managing the following database servers on Google Cloud:

  * SAP HANA
  * SAP ASE
  * IBM Db2 for Linux, UNIX and Windows (IBM Db2)
  * Microsoft SQL Server



### SAP HANA operations

For more information about running SAP HANA on Google Cloud, see the [SAP HANA on Google Cloud Operations Guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide). That guide provides you with lots of details about administration, backup and recovery, security, networking, and other topics.

### SAP ASE operations

For more information about using SAP ASE, see [SAP Adaptive Server Enterprise](https://help.sap.com/viewer/product/SAP_ASE/).

### IBM Db2 operations

For more information about using IBM Db2 with SAP, see [SAP on IBM Db2 for Linux, UNIX and Windows](https://help.sap.com/viewer/p/DB6).

### Microsoft SQL Server operations

The following resources provide details about how to run Microsoft SQL Server on Google Cloud:

Resource | Description  
---|---  
[Best Practices for Microsoft SQL Server](https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices) | Learn how to configure Microsoft SQL Server for stability and performance on Compute Engine.   
  
Note the following important differences in best practices for SAP systems:  
  
  


  * Do not use local SSD drives. Use persistent disk SSDs, instead.
  * For parallel query processing, set the max degree of parallelism to 1, not 8.
  * The transaction log setting must be "FULL" for Microsoft SQL Server databases in production systems.
  * Do not use the buffer pool extension feature.

  
[Load Testing Microsoft SQL Server Using HammerDB](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb) | This tutorial shows how to use HammerDB to perform load testing on a Compute Engine Microsoft SQL Server instance.  
  
## IAM operations

Controlling access to Google Cloud resources is a critical part of securing and operating your deployment. While SAP provides its own user-management system, Google Cloud's [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) provides unified control over permissions for Google Cloud resources. You can manage access control by defining who has what access for resources. For example, you can control who can perform control-plane operations on your SAP instances such as creating and modifying VMs, persistent disks, and networking.

For an overview of IAM in Compute Engine, see [Access Control Options](https://docs.cloud.google.com/compute/docs/access).

### Managing team members

From time to time, you will want to add or remove team members from your project or change their permission levels. For details about how to manage team members, see [Add, Remove Team Members, and Change Permissions](https://docs.cloud.google.com/compute/docs/access/add-remove-change-permissions-for-team-members).

IAM _roles_ are key to granting permissions to users. For a reference about roles and which permissions they provide, see [Identity and Access Management Roles](https://docs.cloud.google.com/iam/docs/overview).

### Managing SSH keys

By default, Compute Engine automatically manages SSH keys. If you have decided to manage your own SSH keys, you need to add and remove keys from time to time during your normal operations. For detailed steps, see [Adding and Removing SSH Keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys).

### Managing service accounts

IAM's _service accounts_ provide a way for you to give permissions to applications and services. It's important to understand how service accounts work in Compute Engine.

If a service account is assigned to a Compute Engine VM, that service account is the default service account for the applications that run on that VM. Any application that uses the VM service account inherits the IAM roles and permissions that are granted to the VM service account.

For more information, see [Identity and access management for SAP programs on Google Cloud](https://docs.cloud.google.com/sap/docs/security-for-sap/iam-for-sap-programs).

### Using Cloud Logging

[Cloud Logging](https://docs.cloud.google.com/logging/docs) is the Google Cloud solution for system-wide logging. Cloud Logging allows you to store, search, analyze, monitor, and alert on log data and events. Using Cloud Logging requires that you have installed the Cloud Logging agent on each VM.

If you didn't install the agent, you can install it now. See [Installing the Logging agent](https://docs.cloud.google.com/logging/docs/agent/installation).

See [Compute Engine Logs](https://docs.cloud.google.com/logging/docs/view/service/compute-logs) for details about supported logs.

#### Access control

Cloud Logging provides granular access control to logs and logging operations. For details, see the [Access Control Guide](https://docs.cloud.google.com/logging/docs/access-control).

#### Audit logging

[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) provides key information about activities happening in Google Cloud through two log types: [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) and [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access). You can view the Activity Feed and the Logs Explorer in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
