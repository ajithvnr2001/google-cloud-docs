---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/dr-for-microsoft-sql-server-with-hdb-mw-async-pd/
title: Enable Disaster Recovery for Microsoft SQL server on Hyperdisk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:38.627996+00:00
---

# Enable Disaster Recovery for Microsoft SQL server on Hyperdisk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/dr-for-microsoft-sql-server-with-hdb-mw-async-pd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable Disaster Recovery for Microsoft SQL server on Hyperdisk Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to enable Hyperdisk Balanced Asynchronous Replication across two Google Cloud regions as a disaster recovery (DR) solution, and how to bring up the DR instances in case of a disaster.

**Note:** This tutorial uses Google Cloud Hyperdisk, the recommended durable block storage for Google Cloud. To deploy a SQL Server with a [machine series that doesn't support Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support), see [Enable disaster recovery for Microsoft SQL Server with Persistent Disk](https://docs.cloud.google.com/compute/docs/instances/sql-server/dr-for-microsoft-sql-server-with-async-pd) for instructions.

Microsoft SQL Server [Failover Cluster Instances](https://docs.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver15) (FCI) is a single highly available SQL Server instance that's deployed across multiple Windows Server Failover Cluster (WSFC) nodes. At any point in time, one of the cluster nodes actively hosts the SQL instance. In the event of a zonal outage or VM issue , WSFC automatically transfers ownership of the instance's resources to another node within the cluster allowing clients to reconnect SQL Server FCI requires data to be located on [shared disks](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms) so that it can be accessed across all WSFC nodes.

To ensure SQL Server deployment can withstand a regional outage, replicate the primary region's disk data to a secondary region by enabling Asynchronous Replication. This tutorial uses Hyperdisk Balanced High Availability multi-writer disks to enable [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) across two Google Cloud regions as a disaster recovery (DR) solution for SQL Server FCI, and how to bring up the DR instances in case of a disaster. In this document, a disaster is an event in which a primary database cluster fails or becomes unavailable because the cluster's region becomes unavailable, perhaps because of a natural disaster.

This tutorial is intended for database architects, administrators, and engineers.

## Objectives

  * Enable Hyperdisk Asynchronous Replication for all SQL Server FCI cluster nodes running on Google Cloud.
  * Simulate a disaster event and perform a complete DR process to validate the DR configuration.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/all-pricing)
  * [Asynchronous Replication Protection](https://docs.cloud.google.com/compute/disks-image-pricing#pdasynchronousreplication/)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. For this tutorial, you need a Google Cloud project. You can create a new one, or select a project you already created:

     1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set up the SQL Server cluster in primary region by following the steps in this [Configuring a SQL Server FCI cluster with Hyperdisk Balanced High Availability multiwriter mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer) guide. After you set up the cluster, return this tutorial to enable DR in the secondary region.

  3. Appropriate permissions in both your Google Cloud project and SQL Server to perform backups and restores.




## Disaster recovery in Google Cloud

DR in Google Cloud involves maintaining continuous access to data when a region fails or becomes inaccessible. There are multiple deployment options for DR site and they will be dictated by the recovery point objective (RPO) and recovery time objective (RTO) requirements. This tutorial covers one of the options where the disks attached to the virtual machine are replicated from the primary to the DR region.

## Disaster recovery using Hyperdisk Asynchronous Replication

Hyperdisk Asynchronous Replication is a storage option that provides asynchronous storage copy for replication of disks between two regions. In the unlikely event of a regional outage, Hyperdisk Asynchronous Replication lets you failover your data to a secondary region and restart your workloads in that region.

Hyperdisk Asynchronous Replication replicates data from a disk that is attached to a running workload, referred to as the primary disk, to a separate disk located in another region. The disk that receives the replicated is referred to as the secondary disk. The region where the primary disk is running is referred to as the primary region, and the region where the secondary disk is running is the secondary region. To ensure that the replicas of all the disks that are attached to each SQL Server node contain data from the same point in time, the disks are added to a [consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#consistency_groups). Consistency groups let you perform DR and DR testing across multiple disks.

### Disaster recovery architecture

For Hyperdisk Asynchronous Replication, the following diagram shows a minimal architecture that supports database HA in a primary region, R1, and disk replication from the primary region to the secondary region, R2.

![Primary and standby instances are located across two zones in region R1, underlying disks
are replicated using asynchronous replication to region R2.](https://docs.cloud.google.com/static/compute/images/dr-for-microsoft-sql-server-with-mw-async-pd-config.png)

**Figure 1.** Disaster recovery architecture with Microsoft SQL Server and Hyperdisk Asynchronous Replication

This architecture works as follows:

  * Two instances of Microsoft SQL Server, a primary instance and a standby instance, are part of a FCI cluster, and are located in the primary region, (R1) but in different zones (zones A and B). Both instances share a Hyperdisk Balanced High Availability disk, enabling access to the data from both VMs. For instructions, see [Configuring a SQL Server FCI cluster with Hyperdisk Balanced High Availability multiwriter mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer)
  * Disks from both the SQL nodes are added to consistency groups and replicated to the DR region, R2. Compute Engine asynchronously replicates the data from R1 to R2.
  * Asynchronous replication only replicates the data on the disks to R2 and doesn't replicate the VM metadata. During DR, new VMs are created and the existing replicated disks are attached to the VMs in order to bring the nodes online.



### Disaster recovery process

The DR process prescribes the operational steps that you must take after a region becomes unavailable to resume the workload in another region. A basic database DR process consists of the following steps:

  1. The first region (R1), which is running the primary database instance, becomes unavailable.
  2. The operations team recognizes and formally acknowledges the disaster and decides whether a failover is required.
  3. If a failover is required, you must terminate replication between the primary and secondary disks. A new VM is created from the disk replicas and brought online.
  4. The database in the DR region, R2, is validated and brought online. The database in R2 becomes the new primary database enabling connectivity.
  5. Users resume processing on the new primary database and access the primary instance in R2.



Although this basic process establishes a working primary database again, it doesn't establish a complete HA architecture, because the new primary database is not being replicated.

![Primary and standby instances are located across two zones in region R1, underlying disks are replicated using asynchronous replication to region R2.](https://docs.cloud.google.com/static/compute/images/dr-for-microsoft-sql-server-with-mw-async-pd-failover.png)

**Figure 2.** SQL Server deployment after Disaster recovery with Persistent Disk Asynchronous Replication

### Fallback to a recovered region

When the primary region (R1) is brought back online, you can plan and execute the failback process. The failback process consists of all the steps outlined in this tutorial but, in this case, R2 is the source and R1 is the recovery region.

## Choose a SQL Server edition

This tutorial supports the following versions of Microsoft SQL Server:

  * SQL Server 2016 Enterprise and Standard Edition
  * SQL Server 2017 Enterprise and Standard Edition
  * SQL Server 2019 Enterprise and Standard Edition
  * SQL Server 2022 Enterprise and Standard Edition



The tutorial uses the SQL Server failover cluster instance with Hyperdisk Balanced High Availability disk.

If you don't require SQL Server Enterprise [features](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver16#scale-limits) you can use Standard edition of SQL Server:

The 2016, 2017, 2019, and 2022 versions of SQL Server have [Microsoft SQL Server Management Studio](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) installed in the image; you don't need to install it separately. However, in a production environment, we recommend that you install one instance of Microsoft SQL Server Management Studio on a separate VM in each region. If you set up an HA environment, you should install Microsoft SQL Server Management Studio once for each zone to ensure that it remains available if another zone becomes unavailable.

## Set up disaster recovery for Microsoft SQL Server

This tutorial uses the `sql-ent-2022-win-2022` image for Microsoft SQL Server Enterprise.

For a complete list of images, see [OS Images](https://docs.cloud.google.com/compute/docs/images).

### Set up a two-instance high availability cluster

To set up disk replication for SQL Server between two regions, first create a two-instance HA cluster in a region. One instance serves as the primary, and the other instance serves as the standby. To accomplish this step, follow the instructions in [Configuring a SQL Server FCI cluster with Hyperdisk Balanced High Availability multiwriter mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer). This tutorial uses `us-central1` for the primary region _R1_. If you followed the steps in [Configuring a SQL Server FCI cluster with Hyperdisk Balanced High Availability multiwriter mode](https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-failover-cluster-instance-pd-multi-writer), you will have created two SQL Server instances in the same region (`us-central1`). You will have deployed a primary SQL Server instance (`node-1`) in `us-central1-a`, and a standby instance (`node-2`) in `us-central1-b`.

### Enable disk Asynchronous Replication

After you have created and configured all the VMs, enable disk replication between the two regions by completing the following steps:

  1. Create a consistency group for both SQL Server nodes and the node hosting witness and domain controller roles. One of the [limitations](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#limitations) for consistency groups is that they can't span across zones, so you must add each node to a separate consistency group.
         
         gcloud compute resource-policies create disk-consistency-group node-1-disk-const-grp \
         --region=$REGION
         
         gcloud compute resource-policies create disk-consistency-group node-2-disk-const-grp \
         --region=$REGION
         
         gcloud compute resource-policies create disk-consistency-group witness-disk-const-grp \
         --region=$REGION
         
         gcloud compute resource-policies create disk-consistency-group multiwriter-disk-const-grp \
         --region=$REGION
         

  2. Add the disks from primary and standby VMs to the corresponding consistency groups.
         
         gcloud compute disks add-resource-policies node-1 \
         --zone=$REGION-a \
         --resource-policies=node-1-disk-const-grp
         
         gcloud compute disks add-resource-policies node-2 \
         --zone=$REGION-b \
         --resource-policies=node-2-disk-const-grp
         
         gcloud compute disks add-resource-policies mw-datadisk-1 \
         --region=$REGION \
         --resource-policies=multiwriter-disk-const-grp
         
         gcloud compute disks add-resource-policies witness \
         --zone=$REGION-c \
         --resource-policies=witness-disk-const-grp
         

  3. Create blank secondary disks in the [secondary region](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#supported_region_pairs).
         
         DR_REGION="us-west1"
         gcloud compute disks create node-1-replica \
           --zone=$DR_REGION-a \
           --size=50 \
           --primary-disk=node-1 \
           --primary-disk-zone=$REGION-a
         
         gcloud compute disks create node-2-replica \
           --zone=$DR_REGION-b \
           --size=50 \
           --primary-disk=node-2 \
           --primary-disk-zone=$REGION-b
         
         gcloud compute disks create multiwriter-datadisk-1-replica \
           --replica-zones=$DR_REGION-a,$DR_REGION-b \
           --size=$PD_SIZE \
           --type=hyperdisk-balanced-high-availability \
           --access-mode READ_WRITE_MANY \
           --primary-disk=multiwriter-datadisk-1 \
           --primary-disk-region=$REGION
         
         gcloud compute disks create witness-replica \
           --zone=$DR_REGION-c \
           --size=50 \
           --primary-disk=witness \
           --primary-disk-zone=$REGION-c
         

  4. Start disk replication. Data is replicated from the primary disk to the newly created blank disk in the DR region.
         
         gcloud compute disks start-async-replication node-1 \
           --zone=$REGION-a \
           --secondary-disk=node-1-replica \
           --secondary-disk-zone=$DR_REGION-a
         
         gcloud compute disks start-async-replication node-2 \
           --zone=$REGION-b \
           --secondary-disk=node-2-replica \
           --secondary-disk-zone=$DR_REGION-b
         
         gcloud compute disks start-async-replication multiwriter-datadisk-1 \
           --region=$REGION \
           --secondary-disk=multiwriter-datadisk-1-replica \
           --secondary-disk-region=$DR_REGION
         
         gcloud compute disks start-async-replication witness \
           --zone=$REGION-c \
           --secondary-disk=witness-replica \
           --secondary-disk-zone=$DR_REGION-c
         




Data should be replicating between regions at this point. The replication status for each disk should say `Active`.

## Simulate a disaster recovery

In this section, you test the disaster recovery architecture set up in this tutorial.

### Simulate an outage and execute a disaster recovery failover

During a failover, you create new VMs in the DR region and attach the replicated disks to them. To simplify the failover, you can use a different Virtual Private Cloud (VPC) in the DR region for recovery, so that you can use the same IP address.

Before starting failover, ensure that `node-1` is the primary node for the AlwaysOn availability group that you created. Bring up the domain controller and the primary SQL Server node in order to avoid any data synchronization issues, as the two nodes are protected by two separate consistency groups. To simulate an outage, use the following steps:

  1. Create a recovery VPC.
         
         DRVPC_NAME="default-dr"
         DRSUBNET_NAME="default-recovery"
         
         gcloud compute networks create $DRVPC_NAME \
         --subnet-mode=custom
         
         CIDR=$(gcloud compute networks subnets describe default \
         --region=$REGION --format=value\(ipCidrRange\))
         
         gcloud compute networks subnets create $DRSUBNET_NAME \
         --network=$DRVPC_NAME --range=$CIDR --region=$DR_REGION
         

  2. Terminate, or stop, data replication.
         
         PROJECT=$(gcloud config get-value project)
         
         gcloud compute disks stop-group-async-replication projects/$PROJECT/regions/$REGION/resourcePolicies/node-1-disk-const-grp \
         --zone=$REGION-a
         
         gcloud compute disks stop-group-async-replication projects/$PROJECT/regions/$REGION/resourcePolicies/node-2-disk-const-grp \
         --zone=$REGION-b
         
         gcloud compute disks stop-group-async-replication projects/$PROJECT/regions/$REGION/resourcePolicies/multiwriter-disk-const-grp \
         --zone=$REGION-c
         
         gcloud compute disks stop-group-async-replication projects/$PROJECT/regions/$REGION/resourcePolicies/witness-disk-const-grp \
         --zone=$REGION-c
         

  3. Stop the source VMs in the primary region.
         
         gcloud compute instances stop node-1 \
           --zone=$REGION-a
         
         gcloud compute instances stop node-2 \
           --zone=$REGION-b
         
         gcloud compute instances stop witness \
           --zone=$REGION-c
         

  4. Rename the existing VMs to avoid duplicate names in the project.
         
         gcloud compute instances set-name witness \
         --new-name=witness-old \
         --zone=$REGION-c
         
         gcloud compute instances set-name node-1 \
         --new-name=node-1-old \
         --zone=$REGION-a
         
         gcloud compute instances set-name node-2 \
         --new-name=node-2-old \
         --zone=$REGION-b
         

  5. Create VMs in the DR region using the secondary disks. These VMs will have the IP address of the source VM.
         
         NODE1IP=$(gcloud compute instances describe node-1-old --zone $REGION-a --format=value\(networkInterfaces[0].networkIP\))
         NODE2IP=$(gcloud compute instances describe node-2-old --zone $REGION-b --format=value\(networkInterfaces[0].networkIP\))
         WITNESSIP=$(gcloud compute instances describe witness-old --zone $REGION-c --format=value\(networkInterfaces[0].networkIP\))
         
         gcloud compute instances create node-1 \
           --zone=$DR_REGION-a \
           --machine-type $MACHINE_TYPE \
           --network=$DRVPC_NAME \
           --subnet=$DRSUBNET_NAME \
           --private-network-ip $NODE1IP\
           --disk=boot=yes,device-name=node-1-replica,mode=rw,name=node-1-replica \
           --disk=boot=no,device-name=mw-datadisk-1-replica,mode=rw,name=mw-datadisk-1-replica,scope=regional
         
         gcloud compute instances create witness \
           --zone=$DR_REGION-c \
           --machine-type=n2-standard-2 \
           --network=$DRVPC_NAME \
           --subnet=$DRSUBNET_NAME \
           --private-network-ip $WITNESSIP \
           --disk=boot=yes,device-name=witness-replica,mode=rw,name=witness-replica
         
         gcloud compute instances create node-2 \
           --zone=$DR_REGION-b \
           --machine-type $MACHINE_TYPE \
           --network=$DRVPC_NAME \
           --subnet=$DRSUBNET_NAME \
           --private-network-ip $NODE2IP\
           --disk=boot=yes,device-name=node-2-replica,mode=rw,name=node-2-replica \
           --disk=boot=no,device-name=mw-datadisk-1-replica,mode=rw,name=mw-datadisk-1-replica,scope=regional
         
         




You've simulated an outage and failed over to the DR region. Now you can test whether the secondary instance is working correctly.

### Verify SQL Server connectivity

After you create the VMs, verify that the databases have been recovered successfully and the server is functioning as expected. To test the database, run a query from recovered database.

  1. Connect to the SQL Server VM by using Remote Desktop.
  2. Open the SQL Server Management Studio.
  3. In the Connect to server dialog, verify the server name is set to `node-1`, and select **Connect**.
  4. In the file menu, select **File > New > Query** with the current connection.
         
         USE [bookshelf];
         SELECT * FROM Books;
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, follow the steps in this section to delete the resources that you created.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
