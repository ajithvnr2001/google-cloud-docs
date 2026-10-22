---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-generic-applications/
title: Mount generic applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:59.822269+00:00
---

# Mount generic applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-generic-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount generic applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Generic applications can be mounted like any other application in the appliance management console.

To mount a **Generic App (LVM)** , follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Right-click the **Generic App (LVM)** application that you want to mount and select **Access**.

**Note:** You can use the **Generic Apps (LVM)** filter to show the apps.
  3. Select a backup image and chose **Mount**.

  4. If you are mounting to a regular host, leave the **Host or VM** option as default. If you want to mount to a **Container** use the instructions in the [Mount an image to a container](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/consume-captured-app-data-in-a-container-environment).

  5. Select the target host from the **Host** drop-down list.

  6. Optionally, assign a **Label** to the mounted image.

  7. If required, change the default storage pool to be used for the mount from the **Storage Pool** drop-down list. This only applies to mounts where there is no existing staging disk, such as imported OnVault images, otherwise the snapshot pool where the source image disks are located are always used regardless of what is set here.

  8. Specify pre- and post-script paths for scripts that automates bringing up and shutting down the databases associated with the Linux-based generic application. Consult the administrator guide for your database to determine the script names to be used and where they reside.

  9. Select one of the following actions from the **Mount Action** drop-down menu:

     * **Keep Source Path** : Maintain the original folder structure.
     * **Specify Mount Location** : Specify a specific location to mount the application.
     * **Map Only** : Map the volumes to a host without mounting into the file system.
  10. Select **Submit**. You can go to the **Job Monitor** to view the progress and details of the job. The mounted image is available in the Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the image form the **App Manager** > **Active Mounts**. Do not leave any image mounted indefinitely. This is because the backup image that the mount was created from, cannot expire until all its mounts have been deleted. When you have finished using the mounted image then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the image. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the image later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the image. This deletes the mounted image, not the backup that the mount is based on.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
