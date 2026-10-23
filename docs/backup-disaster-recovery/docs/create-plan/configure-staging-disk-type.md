---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/configure-staging-disk-type/
title: Configure the staging disk type on a host in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:07.409439+00:00
---

# Configure the staging disk type on a host in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/configure-staging-disk-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Configure the staging disk type on a host in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

Configure your staging disk type by choosing between a file-based backup and recovery in NFS or Block or a logical volume manager (LVM) snapshot with change-block tracking (CBT).

## Common use cases

You can configure the staging disk type for the following database types:

  * [IBM Db2](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/db2-intro)

  * [PostgreSQL](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/postgresql-intro)

  * [SAP ASE](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-ase-intro)

  * [SAP IQ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/sap-iq-intro)

  * [SAP MaxDB](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/maxdb-intro)




## Types of staging disk formats

The backup method is limited by the staging disk format set in the appliance management console. There are two types of staging disk formats:

  * **Block** : Block-based staging disks are useful for backup and recovery, as well as test data management usage.

    * Backup and DR change-block tracking (CBT) is only available on block-based staging disks.

    * Virtual databases can only be mounted to block-based staging disks.

    * Block-based staging disks can be used for both volume level and Full+Incremental file-based backups.

  * **NFS** : NFS-based staging disks permit only file-based backup with Full+Incremental file system backup.

    * Select **NFS** only if **Block** isn't an option in your network.



## Configure staging disk format

  1. From the appliance management console, go to the **Manage** drop-down menu and click **Hosts**.

  2. In the Hosts page, right-click the host you want to configure and click **Edit**.

  3. In the Edit host page, go to the **Staging disk format** setting and from the drop-down list, select **Block** or **NFS**.

  4. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
