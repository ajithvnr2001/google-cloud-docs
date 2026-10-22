---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-cloud-instances/
title: Back up Compute Engine instances from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:30.337880+00:00
---

# Back up Compute Engine instances from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-cloud-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up Compute Engine instances from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can back up Compute Engine instances working completely within the Google Cloud environment using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or Terraform. This method is familiar but it has some limitations.

If you have any of the following backup requirements, you can use the Backup and DR appliance management console to back up Compute Engine instances to a backup/recovery appliance:

  * Backups of specific disks attached to a virtual machine (VM)
  * Automated protection of Google Compute Engine VMs based on tags
  * If the Google Cloud console-based backup plans and backup vaults are not in a [location that is compatible](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility) with the region where your source VMs are running.



To back up Compute Engine instances in the Google Cloud environment, see [Back up Compute Engine instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).

To back up Compute Engine instances using the appliance management console, use these instructions:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Filter applications by **Compute Engine Instance**.

  3. Select an unmanaged instance, and then select **Manage Backup Plan** from the drop-down list at the bottom right corner of the page.

The **Manage Backup Plan** page opens.

  4. Select the following from the **Template** and **Profile** drop-down lists:

     * **Template** : An existing backup template that includes policies to define the snapshot or replication of the application data.
     * **Profile** : An existing resource profile that defines the resources used to store the data of the application as snapshot or replicated backups.

The **Manage Backup Plan** page shows a view of the policies assigned to the selected applications in the backup plan policy map. Data capture management comes from the template policies and profiles that you designed in the backup plans.

  5. Click **Apply**.

The **Apply Backup Plan** page opens.

  6. Configure the instance's details as needed.

  7. Click **Apply Backup Plan** to apply the backup template and resource profile.

  8. Click **Edit** in the **Volume Inclusion Rule** section to include or exclude volumes for data capture.

The **Manage Volumes** dialog opens.

     1. Under **Eligible Volumes** , configure the inclusion rule. You can select from **Capture All Volumes** , **Capture Only Boot Volume** , **Include Selected Volumes** , and **Exclude Selected Volumes**. The selected volumes are captured when the next scheduled job runs. For more information, see Specify individual Compute Engine instance volumes to protect.
     2. If there is a large number of volumes, use the search field to look up specific databases.
     3. Click **Save** to save the manage membership configuration.

The application is not captured until the scheduled job runs according to the hours of operations defined in the backup template. For example, if you assign a template at 10:00 AM with 2:00 am to 5:00 AM for the hours of operation, then the first job does not start until the appliance has an available job slot at 2:00 AM of the following day. To run a job immediately, see [perform an on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

  9. To change backup plan settings for the application, see [Modify backup plan management of a managed application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application).

  10. To disable the backup plan, see [Remove backup plan management of an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/states-of-an-application#remove).

  11. Click **Save Changes**.




## Specify individual Compute Engine instance volumes to protect

You can choose which volumes of a Compute Engine instance to protect using the following options:

  * **Capture all volumes** : Captures the boot volume and all volumes in the Compute Engine instance. Any newly added volumes are captured when they are detected. This is the default selection.
  * **Capture boot volume** : Captures only the boot volume and excludes all other volumes.
  * **Include Selected Volumes** : Captures the selected volumes in the Compute Engine instance. Volumes added after this rule is saved are not included for capture process, they are excluded until a new rule includes them.
  * **Exclude Selected Volumes** : Excludes the selected volumes from being included in the capture process. Volumes added after this rules is saved are included in the capture process until a new rule excludes them.

**Note:** If a selected volume is no longer available, the capture job succeeds and then warns you the first time that the volume is detected as missing. If a previously selected volume re-appears after it has been identified as missing, future capture jobs will capture the volume.



## The Backup and DR Compute Engine guide

  * [Check for the cloud credentials](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/create-cloud-credentials)
  * [Discover and protect Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-ce-inst)
  * [Mount backups of Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances)
  * [Restore a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-instance)
  * [Import Persistent Disk snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/import-pdsnapshot-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
