---
url: https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots/
title: Create Linux application consistent disk snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:24.628065+00:00
---

# Create Linux application consistent disk snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create Linux application consistent disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

You can create application consistent snapshots of Persistent Disk volumes attached to Linux virtual machine (VM) instances. In general, the quality of your disk snapshot depends on how well your applications can recover from snapshots that you create during heavy write workloads. **Application consistent** snapshots capture the state of application data at the time of backup with all application transactions completed and all pending writes flushed to the disk.

To create snapshots that are application consistent, pause apps or operating system processes that write data to the disk, flush the disk buffers, and sync the file system before you create the snapshot. Depending on your application, these and other steps might be required to ensure that all application transactions are complete and captured in the backup.

To create an application consistent snapshot of your disks, use the following process:

  1. To prepare the guest environment for application consistency, create custom shell scripts to run before and after the snapshot is captured
  2. Configure snapshot settings on your VM instance.
  3. Create a snapshot with the `guest-flush` option enabled. The `guest-flush` option starts your pre- and post-snapshot scripts.



## Before you begin

  * [Create a Linux VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * [Update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

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




### Required roles and permissions

To get the permissions that you need to create an application consistent snapshot, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create an application consistent snapshot. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an application consistent snapshot:

  * `compute.snapshots.create` on the project
  * `compute.disks.createSnapshot` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported disk types

You can create application consistent snapshots for Persistent Disk volumes attached to Linux instances.

Hyperdisk volumes don't support `guest-flush` or the Volume Shadow Copy Service (VSS). To create application consistent snapshots for Hyperdisk volumes, you must manually pause the application before you create the snapshot. For more information, see [Manually create application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

## Limitations

Creating application consistent snapshots on Linux has the following limitations:

  * Application consistency depends on the behavior of your custom pre- and post-snapshot scripts, not by the snapshot operation itself.
  * When using the `guest-flush` option in your snapshot creation request, the snapshot isn't created if the script returns an error or reaches the timeout limit.
  * Hyperdisk volumes don't support `guest-flush`.



## Create pre- and post-snapshot scripts

Before you proceed, [update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest) so that you are running the latest software on your Linux VM.

To facilitate application consistency, create pre- and post-snapshot shell scripts to run before and after the snapshot is captured. Use the pre and post scripts for operations such as:

  * Pause apps or operating system processes running on the VM that writes data to the disk.
  * Flush the disk buffers. For example, MySQL has a [`FLUSH`](http://dev.mysql.com/doc/refman/5.7/en/flush.html) statement. Use whichever tool is available for your application.
  * [Sync](https://en.wikipedia.org/wiki/Sync_\(Unix\)) your file system.



The following code example shows a pre snapshot script. Note the leading `#!` characters.

**Caution:** Running `fsfreeze -f` blocks any running process that tries to access the file system, so use with caution if your application is latency-sensitive.
    
    
    #!/bin/bash
    sudo fsfreeze -f [example-disk-location]
    

The following code example shows a post snapshot script. Note the leading `#!` characters.
    
    
    #!/bin/bash
    sudo fsfreeze -u [example-disk-location]
    

You must save your scripts on your VM in the directory `/etc/google/snapshots/`. The full path of your pre script must be `/etc/google/snapshots/pre.sh` and the full path of your post script must be `/etc/google/snapshots/post.sh`.

**Note:** You must copy the scripts to every VM on which you want to enable Linux application consistent snapshots.

### Referencing specific disks in your scripts

The first argument passed to your pre- and post-snapshot scripts is a list of disks for which you are creating snapshots. You can use this argument in your scripts for various checks. For example, if your VM has multiple disks attached but you only specified one disk in your snapshot request, you can check which disk the snapshot is being created for.

The argument is formatted as follows:

  * **SCSI-attached disks** : a comma-separated list of `<target/lun>` pairs.
  * **NVME-attached disks** : a comma-separated list of `<nvme:namespace>` pairs.



For example, your SCSI-attached boot disk might appear as `1/0` while an additional disk attached to the VM might appear as `2/0`.

## Edit your guest environment configuration file

Configure your application consistent snapshot settings by updating a specific configuration file on your VM.

  1. Open or create your guest environment configuration file.
         
         edit /etc/default/instance_configs.cfg
         

  2. Add the following section to the configuration file, then save your changes and exit the editor.
         
         [Snapshots]
         enabled = ENABLED
         timeout_in_seconds = TIMEOUT_SECONDS
         

Replace the following:

     * `ENABLED`: Set to `true` to enable the application consistent snapshot feature. The default value is `false`.
     * `TIMEOUT_SECONDS`: The number of seconds the pre or post snapshot script can take to finish running before timing out. The integer value must be between 0 and 300. The default value is `60`.

**Note:** The number of seconds the entire snapshot operation can take to complete before a timeout error is 300 seconds per disk, and can't be changed.
  3. Restart the Guest Agent to use the new configuration settings.
         
         $ sudo systemctl restart google-guest-agent.service
         




## Create a snapshot with `guest-flush` enabled

Using the Google Cloud console, the Google Cloud CLI, or REST, create a snapshot with the `guest-flush` option enabled. This starts running the pre- and post-snapshot scripts before and after the snapshot is captured.

###  Console 

  1. Go to the **Create a Snapshot** page in the Google Cloud console.

[Go to the Create a Snapshot page](https://console.cloud.google.com/compute/snapshotsAdd)
  2. Enter a snapshot **Name**.
  3. Select a **Snapshot type**. The default is a `STANDARD` snapshot, which is the best option for long-term back up and disaster recovery.

Choose **Archive snapshot** for more cost-efficient data retention.

  4. Optional: Enter a **Description** of the snapshot.
  5. Under **Source disk** , select the existing disk that you want to create a snapshot of.
  6. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following:

     1. Choose the type of storage location that you want for your snapshot.

        * Choose [**Multi-regional**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) for higher availability at a higher cost.
        * Choose [**Regional snapshots**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) for more control over the physical location of your data at a lower cost.
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**. 
  7. Check the **Enable application consistent snapshot** option.
  8. Click **Create** to create the snapshot.



###  gcloud 

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --guest-flush
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot.
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --storage-location=STORAGE_LOCATION \
            --guest-flush
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, include the `--region` flag to indicate where to create your snapshot.
        
        gcloud beta compute snapshots create SNAPSHOT_NAME \
            --region=SNAPSHOT_SCOPE_REGION
            --source-disk=SOURCE_DISK_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --snapshot-type=SNAPSHOT_TYPE
        




Replace the following:

  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `--storage-location` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `gcloud compute snapshots create` command instead of the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

###  REST 

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshots/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "guestFlush": true,
        }
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, make a `POST` request to the `snapshots.insert` method and include the `storageLocations` property in your request:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "storageLocations": [
              "STORAGE_LOCATION"
          ],
          "guestFlush": true,
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, make a `POST` request to the `snapshots.insert` method and define the creation region:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/regions/SNAPSHOT_SCOPE_REGION/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotType": "SNAPSHOT_TYPE"
        }
        




Replace the following:

  * DESTINATION_PROJECT_ID: The ID of project in which you want to create the snapshot.
  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_PROJECT_ID: The ID of the source disk project.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `storageLocations` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `snapshots.insert` method instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

## Create a snapshot schedule with `guest-flush` enabled

You can enable regular and automatic application consistent backups of your zonal and regional Persistent Disk volumes with snapshot schedules. To enable application consistent snapshots for your scheduled snapshots, use the `--guest-flush` option when you create the snapshot schedule so that the pre- and post-snapshot scripts execute before and after each scheduled snapshot.

For example, after configuring your guest environment configuration file and creating custom scripts, the following command creates hourly application consistent snapshots:
    
    
    gcloud compute resource-policies create snapshot-schedule SCHEDULE_NAME \
      --description "MY HOURLY SNAPSHOT SCHEDULE" \
      --start-time 22:00 \
      --hourly-schedule 4 \
      --guest-flush \
      --max-retention-days SNAPSHOT_RETENTION_AGE
    

To learn more, see [About snapshot schedules for disks](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).

## Troubleshooting

Troubleshoot the snapshot schedule and creation process by reviewing logs and checking configurations.

### Review the logs

  1. Go to the **Logs Explorer** page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following query in the [Log query pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#query-builder):
         
         resource.type="gce_disk"
         jsonPayload.event_subtype="compute.disks.createSnapshot" OR
         protoPayload.methodName="ScheduledSnapshots"
         

  3. Run the query and investigate the logs:

![snapshot creation log query.](https://docs.cloud.google.com/static/compute/images/snapshot-query.png)




### Check configurations

  * If no pre or post snapshot scripts are found on the instance to freeze the activity/IOPS on the file system, no snapshot will be created. Make sure you've followed the steps in Create pre- and post-snapshot scripts.

  * If there is a script error or timeout, no snapshot is created. Review [Preparing for consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency). Note that the maximum timeout period that you can configure in your settings is 300 seconds. Try repeating the entire process using the sample scripts.

  * A disk must be attached to a VM to capture a snapshot of the disk with `guest-flush` enabled. To learn how to create a Linux VM and attach a disk, see [Creating a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).




## What's next

  * [Restore a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).
  * [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
