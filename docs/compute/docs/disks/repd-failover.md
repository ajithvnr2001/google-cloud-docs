---
url: https://docs.cloud.google.com/compute/docs/disks/repd-failover/
title: Manage failures for regional disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:17.038793+00:00
---

# Manage failures for regional disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/repd-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage failures for regional disks Stay organized with collections  Save and categorize content based on your preferences. 

Regional Persistent Disk and Hyperdisk Balanced High Availability are storage options that provide synchronous replication of data between two zones in a region. You can use Regional Persistent Disk or Hyperdisk Balanced High Availability as a building block when you [implement high availability (HA) services](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk) in Compute Engine. 

This document explains the various scenarios that can disrupt the working of your regional disks and how you can manage these scenarios.

## Before you begin

  * Review the basics about regional disks and failover. For more information, see [ About synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to migrate regional disk data using a replica recovery checkpoint, ask your administrator to grant you the following IAM roles: 

  * To migrate regional disk data using a replica recovery checkpoint: [](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1)[Compute Instance Admin (v1)](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 
  * To view regional disk metrics (one of the following): 
    * [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer)[Monitoring viewer](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) (`roles/monitoring.viewer`) on the project
    * [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor)[Monitoring editor](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) (`roles/monitoring.editor`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to migrate regional disk data using a replica recovery checkpoint. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to migrate regional disk data using a replica recovery checkpoint:

  * To create a standard snapshot from the replica recovery checkpoint: 
    * `compute.snapshots.create` on the project
    * `compute.disks.createSnapshot` on the disk
  * To create a new regional disk from the standard snapshot: `compute.disks.create` on the project where you want to create the new disk 
  * To migrate VMs to the new disk: 
    * `compute.instances.attachDisk` on the VM instance
    * `compute.disks.use permission` on the newly created disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

You can't use `force-attach` operations on disks that are in multi-writer mode.

## Failure scenarios

With regional disks, when the device is _fully replicated_ , data is automatically replicated to two zones in a region. A write is acknowledged back to a compute instance when it is durably persisted in both replicas.

If replication to one zone fails or is very slow for a while, the disk replication status switches to _degraded_. In this mode, write is acknowledged after it is durably persisted in one replica.

If and when Compute Engine detects that replication can be resumed, data that was written to one replica after the other replica entered the degraded state is synced to both zones and the disk returns to a fully replicated state. This transition is fully automated.

[RPO and RTO](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) are undefined while a device is in a degraded state. To minimize data and availability loss in the event of a failure of a disk operating in a degraded state, we recommend that you back up your regional disks regularly using [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots). You can recover a disk by restoring the snapshot.

### Zonal failures

A replicated disk, or _regional_ disk, is synchronously replicated to disk replicas in the primary and secondary zones. Zonal failures happen when a zonal replica becomes unavailable. Zonal failures can happen in either the primary or secondary zone due to one of the following reasons:

  * There is a zonal outage.
  * The replica experiences excessive slowness in write operations.



The following table provides the various zonal failure scenarios that you might encounter for regional disks and the recommended action for each scenario. In each of these scenarios, it is assumed that your primary zonal replica is healthy and synced during the initial state.

Fully replicatedDegradedCatching up

Secondary replica: syncedSecondary replica: catching upSecondary replica: out of sync

Primary zoneSecondary zone

Clear all

**Initial state of the disk** | **Failure in** | **New state of the disk** | **Consequences of failure** | **Action to take**  
---|---|---|---|---  
**Primary replica:** Synced **Secondary replica:** Synced **Disk status:** Fully replicated **Disk attached in:** primary zone | Primary zone |  **Primary replica:** Out of sync or unavailable **Secondary replica:** Synced **Disk status:** Degraded **Disk attached in:** primary zone | 

  * The replica in the secondary zone remains healthy and has the latest disk data. 
  * The replica in the primary zone is unhealthy and is not guaranteed to have all the disk data. 

|  Failover the disk by force-attaching to a VM in the healthy secondary zone.   
**Primary replica:** Synced **Secondary replica:** Synced **Disk status:** Fully replicated **Disk attached in:** primary zone | Secondary zone |  **Primary replica:** Synced **Secondary replica:** Out of sync or unavailable **Disk status:** Degraded **Disk attached in:** primary zone | 

  * The replica in the primary zone remains healthy and has the latest disk data. 
  * The replica in the secondary zone is unhealthy and is not guaranteed to have all the disk data. 

|  No action needed. Compute Engine brings the unhealthy replica in the secondary zone back into sync after it is available again.   
**Primary replica:** Synced **Secondary replica:** Out of sync and unavailable **Disk status:** Degraded **Disk attached in:** primary zone | Primary zone |  **Primary replica:** Synced but unavailable **Secondary replica:** Out of sync **Disk status:** Unavailable **Disk attached in:** primary zone | 

  * Both zonal replicas are unavailable and cannot serve traffic. The disk becomes unavailable. 
  * If the zonal outage or replica failure is temporary, then no data is lost. 
  * If the zonal outage or replica failure is permanent, then any data written to the healthy replica while the disk was degraded is permanently lost. 

|  Google recommends that you [ use an existing standard snapshot and create a new disk ](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#use_repd_boot_disks) to recover your data. As a best practice, back up the regional disks regularly using standard snapshots.   
**Primary replica:** Synced **Secondary replica:** Catching up but available **Disk status:** Catching up **Disk attached in:** primary zone | Primary zone |  **Primary replica:** Unavailable **Secondary replica:** Catching up but available **Disk status:** Unavailable **Disk attached in:** primary zone | 

  * Both zonal replicas cannot serve traffic. The disk becomes unavailable. 
  * If the zonal outage or replica failure is temporary, then your disk resumes operations after the primary replica is available again. 
  * If the zonal outage or replica failure is permanent, your disk becomes unusable. 

| 

  * Google recommends that you [ use an existing standard snapshot and create a new disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#use_repd_boot_disks) to recover your data. As a best practice, back up the regional disk regularly using standard snapshots. 
  * If you don't have any existing standard snapshots of the disk, you can still  recover your data from the out of sync replica by using the replica recovery checkpoint. 

  
**Primary replica:** Synced **Secondary replica:** Out of sync but available **Disk status:** Degraded **Disk attached in:** primary zone | Primary zone |  **Primary replica:** Unavailable **Secondary replica:** Out of sync but available **Disk status:** Unavailable **Disk attached in:** primary zone | 

  * Both zonal replicas cannot serve traffic. The disk becomes unavailable.
  * If the zonal outage or replica failure is temporary, then your disk resumes operations after the primary replica is available again. 
  * If the zonal outage or replica failure is permanent, your disk becomes unusable. 

| 

  * Google recommends that you [ use an existing standard snapshot and create a new disk ](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#use_repd_boot_disks) to recover your data. As a best practice, back up the regional disk regularly using standard snapshots. 
  * If you don't have any existing standard snapshots of the disk, you can still  recover your data from the out of sync replica by using the replica recovery checkpoint. 

  
  
### Application and VM failures

In the event of outages caused by VM misconfiguration, an unsuccessful OS upgrade, or other application failures, you can `force-attach` your regional disk to a compute instance in the same zone as the healthy replica.

Failure category and (probability) | Failure types | Action  
---|---|---  
Application failure (High) | 

  * Unresponsive applications
  * Failure due to application administrative actions (for example, upgrade) 
  * Human error (for example, misconfiguration of parameters such as SSL certificate or ACLs)

|  Application control plane can trigger [ failover](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-failover) based on [ health check](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#health-checks) thresholds.   
VM failure (Medium) | 

  * Infrastructure or hardware failure
  * VM unresponsive due to CPU contention, intermediate network interruption

|  VMs are usually [ autohealed](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing). The application control plane can trigger [ failover](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd-failover) based on [ health check](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#health-checks) thresholds.   
Application corruption (Low-Medium) |  Application data corruption  
(for example, due to application bugs or an unsuccessful OS upgrade)  | Application recovery:  


  * Try application-specific recovery tools if available. For example, [MySQL database page corruption](https://dev.mysql.com/doc/refman/5.7/en/forcing-innodb-recovery.html). 
  * Restore from logical replication archive. For example, a read replica or logical log archive such as [ PostgreSQL continuous archiving](https://www.postgresql.org/docs/9.6/static/continuous-archiving.html). 

  
  
## Failover a regional disk using `force-attach`

In the event that the primary zone fails, you can fail over your Regional Persistent Disk or Hyperdisk Balanced High Availability volume to a compute instance in another zone by using a force-attach operation.

When there's a failure in the primary zone, you might not be able to detach the disk from the instance because the instance can't be reached to perform the detach operation. _Force-attach_ lets you attach a Regional Persistent Disk or Hyperdisk Balanced High Availability volume to a compute instance even if that volume is attached to another instance.

After you complete the force-attach operation, Compute Engine prevents the original instance from writing to the regional disk. Using the force-attach operation lets you safely regain access to your data and recover your service. You also have the option to [manually shut down the VM instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance_through_the_os) after you perform the force-attach operation.

To force attach an existing disk to a compute instance, select one of the following tasks:

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project.

  3. Click the name of the instance that you want to change.

  4. On the details page, click **Edit**.

  5. In the **Additional disks** section, click **Attach additional disk**.

  6. Select the regional, or synchronously replicated disk from the drop-down list.

  7. To force attach the disk, select the **Force-attach disk** checkbox.

  8. Click **Done** , and then click **Save**.




You can perform the same steps to `force-attach` a disk to the original compute instance after the failure is resolved.

###  gcloud 

In the gcloud CLI, use the [`instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) to attach the replica disk to a compute instance. Include the `--disk-scope` flag and set it to `regional`.
    
    
    gcloud compute instances attach-disk VM_NAME \
        --disk DISK_NAME --disk-scope regional \
        --force-attach
    

Replace the following:

  * `VM_NAME`: the name of the new compute instance in the region
  * `DISK_NAME`: the name of the regional disk



After you `force-attach` the disk, mount the file systems on the disk, if necessary. The compute instance can use the force-attached disk to continue read and write operations to the disk.

###  REST 

Construct a `POST` request to the [`compute.instances.attachDisk` method](https://docs.cloud.google.com/compute/docs/reference/v1/instances/attachDisk), and include the URL to the regional disk that you just created. To attach the disk to the new compute instance, the `forceAttach=true` query parameter is required if the primary compute instance still has the disk attached.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/attachDisk?forceAttach=true
    
    {
     "source": "projects/PROJECT_ID/regions/REGION/disks/DISK_NAME"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the location of your compute instance
  * `VM_NAME`: the name of the compute instance where you are adding the regional disk
  * `REGION`: the region where your regional disk is located
  * `DISK_NAME`: the name of the regional disk



After you attach the regional disk, mount the file systems on the disks if necessary. The compute instance can use the replica disk to continue read and write operations to the disk.

**Note:** You can't attach the disk if doing so exceeds the [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance). for the compute instance.

## Failover a boot disk to a secondary instance

You can have only one boot disk attached to a compute instance. When failing over a regional boot disk, use one of the following methods, depending on whether the secondary compute instance already exists:

  * If you don't have an active standby VM, then create a new instance in the secondary zone. When you create the second instance, use the regional disk for the boot disk, as described in [Create a new VM with a regional boot disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#create-vm-repd-boot-disk).

  * If you have a standby VM in the secondary zone, then replace the boot disk of the standby VM with the regional boot disk, as described in [Attach a regional boot disk to a VM](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#attach-repd-boot-disk).




## Use replica recovery checkpoint to recover regional disks

A replica recovery checkpoint represents the most recent crash-consistent point in time of a fully replicated Regional Persistent Disk or Hyperdisk Balanced High Availability volume. Compute Engine lets you create standard snapshots from the replica recovery checkpoint for degraded regional disks.

In rare scenarios, when your disk is degraded, the zonal replica that is synced with the latest disk data can also fail before the out-of-sync replica catches up. You won't be able to force-attach your disk to compute instances in either zone. Your replicated disk becomes unavailable and you must migrate the data to a new disk. In such scenarios, if you don't have any existing standard snapshots available for your disk, you might still be able to recover your disk data from the incomplete replica by using a standard snapshot created from the replica recovery checkpoint. See Procedure to migrate and recover disk data for detailed steps.

**Important:** In case of an unavailable disk, Google recommends that you always use any existing standard snapshots to create a new Regional Persistent Disk or Hyperdisk Balanced High Availability volume and recover disk data. Create standard snapshots from a checkpoint only if you don't have any existing standard snapshots available. 

### Procedure to migrate and recover disk data

To recover and migrate the data of a regional disk by using the replica recovery checkpoint, perform the following steps:

  1. Create a standard snapshot of the impacted Regional Persistent Disk or Hyperdisk Balanced High Availability volume from its replica recovery checkpoint.

You can create the standard snapshot for a disk from its replica recovery checkpoint by using only gcloud CLI or REST.

###  gcloud 

To create a snapshot using the replica recovery checkpoint, use the [ `gcloud compute snapshots create` command ](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create). Include the `--source-disk-for-recovery-checkpoint` flag to specify that you want to create the snapshot using a replica recovery checkpoint. Exclude the `--source-disk` and `--source-disk-region` parameters. 
         
         gcloud compute snapshots create SNAPSHOT_NAME \
             --source-disk-for-recovery-checkpoint=SOURCE_DISK \
             --source-disk-for-recovery-checkpoint-region=SOURCE_REGION \
             --storage-location=STORAGE_LOCATION \
             --snapshot-type=SNAPSHOT_TYPE
         

Replace the following: 

     * `DESTINATION_PROJECT_ID`: The ID of project in which you want to create the snapshot.
     * `SNAPSHOT_NAME`: A name for the snapshot.
     * `SOURCE_DISK`: The name or full path of the source disk that you want to use to create the snapshot. To specify the full path of a source disk, use the following syntax: 
           
           projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME
             

If you specify the full path to the source disk, you can exclude the `--source-disk-for-recovery-checkpoint-region` flag. If you specify only the disk's name, then you must include this flag.

To create a snapshot from the recovery checkpoint of a source disk in a different project, you must specify the full path to the source disk.

     * `SOURCE_PROJECT_ID`: The project ID of the source disk whose checkpoint you want to use to create the snapshot.
     * `SOURCE_REGION`: The region of the source disk whose checkpoint you want to use to create the snapshot. 
     * `SOURCE_DISK_NAME`: The name of the source disk whose checkpoint you want to use to create the snapshot. 
     * `STORAGE_LOCATION`: Optional: The [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.  
Use the `--storage-location` flag only if you want to override the predefined or customized default storage location configured in your snapshot settings.
     * `SNAPSHOT_TYPE`: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created.

You can use replica recovery checkpoint to create a snapshot only on [degraded disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd_replication_state). If you try to create a snapshot from a replica recovery checkpoint when the device is fully replicated, you see the following error message:
    
    The device is fully replicated and should not create snapshots out of a recovery checkpoint. Please
    create regular snapshots instead.
    

###  REST 

To create a snapshot using the replica recovery checkpoint, make a `POST` request to the [ `snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert). Exclude the `sourceDisk` parameter and instead include the `sourceDiskForRecoveryCheckpoint` parameter to specify that you want to create the snapshot using the checkpoint. 
    
    POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT_ID/global/snapshots
    
    {
      "name": "SNAPSHOT_NAME",
      "sourceDiskForRecoveryCheckpoint": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
      "storageLocations": "STORAGE_LOCATION",
      "snapshotType": "SNAPSHOT_TYPE"
    }
    

Replace the following: 

     * `DESTINATION_PROJECT_ID`: The ID of project in which you want to create the snapshot.
     * `SNAPSHOT_NAME`: A name for the snapshot.
     * `SOURCE_DISK`: The name or full path of the source disk that you want to use to create the snapshot. To specify the full path of a source disk, use the following syntax: 
           
           projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME
             

If you specify the full path to the source disk, you can exclude the `--source-disk-for-recovery-checkpoint-region` flag. If you specify only the disk's name, then you must include this flag.

To create a snapshot from the recovery checkpoint of a source disk in a different project, you must specify the full path to the source disk.

     * `SOURCE_PROJECT_ID`: The project ID of the source disk whose checkpoint you want to use to create the snapshot.
     * `SOURCE_REGION`: The region of the source disk whose checkpoint you want to use to create the snapshot. 
     * `SOURCE_DISK_NAME`: The name of the source disk whose checkpoint you want to use to create the snapshot. 
     * `STORAGE_LOCATION`: Optional: The [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.  
Use the `storageLocations` parameter only if you want to override the predefined or customized default storage location configured in your snapshot settings.
     * `SNAPSHOT_TYPE`: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created.

You can use replica recovery checkpoint to create a snapshot only on [degraded disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#repd_replication_state). If you try to create a snapshot from a replica recovery checkpoint when the device is fully replicated, you see the following error message:
    
    The device is fully replicated and should not create snapshots out of a recovery checkpoint. Please
    create regular snapshots instead.
    

  2. Create a new Regional Persistent Disk or Hyperdisk Balanced High Availability disk using this snapshot. When you create the new disk, you recover all the data from the most recent replica recovery checkpoint by restoring the data to the new disk from the snapshot. For detailed steps, see [Create a new instance with a regional boot disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#create-vm-repd-boot-disk).

  3. Migrate all the VM workloads to the newly created disk and validate that these VM workloads are running correctly. For more information, see [Move a VM across zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones#moving-an-instance-manually).




After you recover and migrate your disk data and VMs to the newly created Regional Persistent Disk or Hyperdisk Balanced High Availability disk, you can resume your operations.

### Determine the RPO provided by replica recovery checkpoint

This section explains how to determine the RPO provided by the latest replica recovery checkpoint of a Regional Persistent Disk or Hyperdisk Balanced High Availability volume.

#### Zonal replicas are fully synced

Compute Engine refreshes the replica recovery checkpoint of your Regional Persistent Disk or Hyperdisk Balanced High Availability volume approximately every 15 minutes. As a result, when your zonal replicas are fully synced, the RPO is approximately 15 minutes.

#### Zonal replicas are out of sync

You can't view the exact creation and refresh timestamps of a replica recovery checkpoint. However, you can estimate the approximate RPO that your latest checkpoint provides by using the following data:

  * **Most recent timestamp of the fully replicated disk state** : You can get this information by using the Cloud Monitoring data for the `replica_state` metric of the regional disk. Check the `replica_state` metric data for the out of sync replica to determine when the replica went out of sync. Because Compute Engine refreshes the disk's checkpoint every 15 minutes, the most recent checkpoint refresh could have been approximately 15 minutes before this timestamp.
  * **Most recent write operation timestamp** : You can get this information by using the Cloud Monitoring data for the `write_ops_count` metric of the regional disk. Check the `write_ops_count` metric data to determine the most recent write operation for the disk.



After you determine these timestamps, use the following formula to calculate the approximate RPO provided by the replica recovery checkpoint of your disk. If the calculated value is less than zero, then the RPO is effectively zero.
    
    
    Approximate RPO provided by the latest checkpoint =
    (Most recent write operation timestamp - (Most recent timestamp of the fully
    replicated disk state - 15 minutes))
    

## What's next

  * Learn how to [monitor replica states and replication status for regional disks](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state).
  * Learn how to [determine the exact disk replication status](https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state#determine-repd-replication-status-monitoring).
  * Learn how to [create a snapshot of a disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Learn how to [build high availability services using regional disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk).
  * Learn how to [build scalable and resilient web applications on Google Cloud](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * Review the [disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
