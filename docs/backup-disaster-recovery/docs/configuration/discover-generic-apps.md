---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-generic-apps/
title: Add generic applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:29.494952+00:00
---

# Add generic applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-generic-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add generic applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can discover and manage applications and databases on a Linux host that weren't automatically discovered by the Backup and DR agent. Once you've discovered one or more applications, you can protect them all at once by applying a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) or add them to the applications list as unmanaged or ignored VMs.

## Use Linux Change Block Tracking to protect your generic applications

This option leverages the Linux Change Block Tracking (CBT) driver and tracks block level changes to logical volumes for incremental backups. Databases and applications that run on Linux can be discovered and managed using this option.

During the appliance management console configuration, you may have already added the hosts that have the applications to your appliances. See [Add a Host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications) for more information.

## Linux Change Block Tracking requirements

Linux CBT requires the following:

  * Linux application volumes managed by Linux logical volume manager (LVM)

  * At least 20% free space for the Linux application's LVM volume group, not including the boot volume when protecting the application

  * A Linux host with a Backup and DR agent installed

  * A Linux host running a supported version of the Linux operating system, refer to the [Backup and DR support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

  * Successful operation normally requires some scripting work, which is often minimal, but may be extensive. If you need assistance, contact [Support](https://docs.cloud.google.com/backup-disaster-recovery/docs/support) for help.




## Protect your generic applications

Use the following instructions to discover and protect generic applications:

  1. In the appliance management console, click the **App Manager** drop-down menu and click **Applications**.

  2. Click **Add Application**.

  3. Select **Generic App (volume based)** and then follow the steps in the wizard.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
