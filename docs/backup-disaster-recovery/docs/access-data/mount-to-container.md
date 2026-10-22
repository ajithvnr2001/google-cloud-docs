---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-to-container/
title: Mount a backup to a container in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:50.454880+00:00
---

# Mount a backup to a container in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-to-container/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount a backup to a container in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

To mount and access application data captured from valid application types in a container environment, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** > **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Filter applications to list supported database applications—on Linux platform.

**Note:** The mount to containers capability is not available for Compute Engine instance, databases backups created using the Full+Incremental backup method, Oracle database backups, VMware VM backups, Windows application backups—SMB, file systems, and SQL server.
  3. Select the application with the chosen backup.

  4. Choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured backups in the timeline ramp view. For more information on this view, see [Access the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  5. Select a point-in-time backup, then select **Mount** from the list of access operations.

The **Mount** page opens where the **Mount to Host or VM** option is selected by default.

  6. Select the **Container** option.

  7. Enter a unique name associated with the container mount in the **Label** field.

  8. Enter a single IP address or a range of IP addresses in the **Allowed IP Addresses** field. Network addresses in the format `a.b.c.d./n` are also supported. Specifying IP addresses limits the number of hosts to only those with the IP address that are allowed to access application data for NFS.

Leaving the IP address empty allows any host to access the application data.

  9. For **Included Volumes** , all volumes are selected by default.

     * Enter the path where the backup should be mounted to inside the container in the **Mount Location** field. By default, this path is the same as the source path.
     * Enter the path where the appliance should expose the logical volume of the application over NFS in the **NFS Export Path** field. If no path is specified, the system auto generates a path and exposes the data over that path.
  10. Click **Submit**.

  11. Click **Okay** to close the dialog, or click **Monitor** to follow the progress of the job in **Monitor**. Once the mount job is complete, the backup becomes active and is available in the Active mounts view of the **App Manager**.

After a successful mount job, the data is available from the appliance over NFS. In order to access it from your container, you need to add some code to your container YAML definition. You can obtain this YAML code from either of the following:

     * The **Job Details** page, see [Monitor mount jobs to containers](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#container).
     * The **Active Mounts** page, see [Access container YAML code from the active mounts page](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-yaml).



In order to consume the selected application's data from within the container over NFS, the YAML code must be added to the container's YAML configuration file.

## Management of the active mounts

Once you have created a mount, you can track the backup from the **App Manager** > **Active Mounts**. Don't leave any backup mounted indefinitely. This is because the backup that the mount was created from, cannot expire until all its mounts have been deleted. When you have finished using the mounted backup then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the backup. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the backup later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the backup. This deletes the mounted backup, not the backup that the mount is based on.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
