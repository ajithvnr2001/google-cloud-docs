---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-smb-host/
title: Add SMB file systems to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:18.384869+00:00
---

# Add SMB file systems to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-smb-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add SMB file systems to the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR discovers Server Message Block (SMB), formerly known as CIFS, shares on a Windows host using Windows credentials. Before you can run application discovery to add the SMB shares to Backup and DR, you must have the following:

  * Windows server credentials

  * [Backup and DR agent installed on Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)

  * Add host that has SMB shares




## Windows server credentials

To discover SMB shares, you must have valid Windows server credentials.

Use the following instructions to validate them:

  1. Log into the target Windows server as the user you intend to share with Backup and DR and ensure that all SMB shares that you want to back up are visible. This validates that you have the correct username and password.

  2. If the SMB shares that you want are already mapped and present, then move to the next step. For all new SMB shares, use Windows Explorer to map the target SMB share to a local drive letter. Don't specify additional credentials when mapping the drive. Specify **Reconnect at logon**.




## Install the Backup and DR agent and generate secret key

You need to have the secret key to provide access to the SMB host. If you haven't already done so, [install the Backup and DR Agent using the agent install](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent).

## Add the SMB host

**Note:** If you have added the Windows server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead find and edit that host and proceed from step 7.

Use these instructions to add a new Windows Server host to the appliance management console:

  1. In the appliance management console, go to **Manage** > **Hosts**.

  2. Select **\+ Add Host**.

  3. In the **Add Host** form, enter the name and an optional friendly name. The name of a host must start with a letter, and can contain letters and digits (0-9). Underscore ('_') characters are not allowed.

  4. Enter the IP address of the host in **IP Address**. Click the **plus sign +** to add it.

  5. In the **Appliances** section, select the appliance management console managed appliances that serve this host. If the list is long, you can use the search box to find a specific appliance or group of appliances.

  6. Leave **Host Type** as **Generic**.

  7. In the Backup and DR agent settings, complete the following steps:

     * Backup and DR agent port is normally port 5106. If it is anything else, enter the port number.

     * Add credentials for the host. For SMB shares that need to be discovered, you must supply a username and password that can access those SMB shares and validated in Windows server credentials section.

     * You need to supply a secret key generated on the Windows host servers by the Backup and DR agent, to initialize trusted communications between the host and Backup and DR agent. This only needs to be done once. If you don't have the secret key, generate one by [Install the Backup and DR agent on a Windows host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent).

  8. Click **Add**.




## Discover SMB shares

To add SMB shares, you must do the following:

  1. Discover the SMB application discovery using either of the following methods:

     * In the appliance management console, click the **Back up & Recover** drop-down menu and select **Back up** , and then select **All Apps**.

     * Go to **App Manager** > **Applications** , select **Add Applications** and then select **All Apps**.

  2. Select the host that you added in Add SMB host section and click **Discover**.

After the SMB shares are discovered, you can find them using the **SMB** filter in the **Applications** page.

**Note:** In order to find the share, the username and password for the host server must be set to the user that mapped the shares on the server. You can only find mapped shares for a user if a backup/recovery appliance can impersonate that user.



## What's next

  * To view SMB-specific backup settings, see [Configure application settings to protect mapped SMB file system data](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-app-settings-for-filesystems).

  * To restore an SMB share, see [Restore a mapped SMB file system](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/filesystem-restore#restore_a_mapped_smb_file_system).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
