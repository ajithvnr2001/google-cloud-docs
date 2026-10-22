---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/
title: Add a Filestore or any other NFS file system or file share to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:26.488568+00:00
---

# Add a Filestore or any other NFS file system or file share to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-nfs-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add a Filestore or any other NFS file system or file share to the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR can discover and back up NFS shares on a Linux host. Before you can run application discovery to add the NFS shares to Backup and DR, you must have a Backup and DR Agent installed on the NFS host

You can also back up Filestore instances working completely within the Google Cloud environment using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or Terraform. This method is familiar but it has some limitations.

If you have any of the following backup requirements, you can use the Backup and DR appliance management console to back up Filestore instances to a backup/recovery appliance:

  * Backups of specific disks attached to a virtual machine (VM)
  * Automated protection of Google Compute Engine VMs based on tags
  * If the Google Cloud console-based backup plans and backup vaults are not in a [location that is compatible](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility) with the region where your source VMs are running.



To back up Filestore instances in the Google Cloud environment, see [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup).

To back up Filestore instances using the appliance management console, continue on this page.

## Install Backup and DR agent and generate secret key

You need to have the secret key to provide access to the NFS host. If you haven't already, [install the Backup and DR Agent using the agent install](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).

## Add NFS host

**Note:** If you've already added the Linux server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead, find and edit that host and proceed from step seven.

Use the following instructions to add a new Linux host to the appliance management console:

  1. In the appliance management console, go to **Manage** > **Hosts**.

  2. Select **\+ Add Host**.

  3. In the **Add Host** form, enter the name and an optional friendly name. The name of a host must start with a letter, and can contain letters and digits (0-9). Underscore ('_') characters are not valid in host names.

  4. Enter the IP address of the host in **IP Address**. Click the **plus sign (+)** to add it.

  5. In the **Appliances** section, select the appliance management console managed appliances that serve this host. If the list is long, you can use the search field to find a specific appliance or group of appliances.

  6. Leave **Host Type** as **Generic**.

  7. In the Backup and DR agent settings, complete the following:

     * Backup and DR agent port is normally port 5106. If it is anything else, enter the port number.

     * You need to supply a secret key generated on the Linux host servers by the Backup and DR agent to initialize trusted communications between the host and Backup and DR agent. This only needs to be done once. If you don't have the secret key, generate one by [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent).

  8. Click **Add**. If you get a partial success message, use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).




## Discover NFS shares

Use the following instructions to add NFS shares:

  1. Discover the NFS application discovery in either of the following ways:

     * In the appliance management console, click the **Back up & Recover** drop-down menu and select **Back up** , and then select **All Apps**.

     * Go to **App Manager** > **Applications** , select **Add Applications** and then select **All Apps**.

  2. Select the host that you added in **Add NFS host** section and click **Discover**. After the NFS shares are discovered, you can find them using the **NFS** filter in the **Applications** page.




## What's next

  * To apply a backup plan for NFS applications, see [Apply backup template to manage mapped NFS file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-plan-to-filesystem)

  * To define NFS specific backup settings, see [Configure application settings to protect mapped NFS file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems)

  * To mount a NFS backup, see [Mount a SMB share, file system, or NFS backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-file-system)

  * To restore NFS backups, see [File system restore](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
