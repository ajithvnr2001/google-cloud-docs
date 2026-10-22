---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-oracle/
title: Add an Oracle database host, and discover and back up Oracle databases in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:10.919540+00:00
---

# Add an Oracle database host, and discover and back up Oracle databases in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add an Oracle database host, and discover and back up Oracle databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

There are two parts to getting your Oracle databases started with Backup and DR, adding the Oracle server host to the appliance management console, and then discovering the Oracle databases.

## Add the host

Add the host to the appliance management console. If the host is already added, then edit the host and make sure to set all the configurations correctly.

**Note:** If you have added the Windows server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead find and edit that host.

  1. Click **Manage** > **Hosts** , then click **\+ Add Host**.

  2. On the **Add Host** page complete the following:

     * **Name** : Provide the database server name.

     * **IP Address** : Provide the database server IP and click the **plus sign (+)**.

     * **Appliances** : Select the checkbox for the appliance.

     * **Host Type** : Make sure this is **Generic**.

  3. Click **Add** to add the host. The host is added.

  4. Right-click the host and select **Edit**.

  5. Leave the **Staging Disk Format** as **Block**.

  6. Enter the username and password that you set up previous in **Application Discovery Credentials**.

  7. Select **Save**.




## Discover and protect the Oracle database application

Use these instructions to discover and protect the database applications:

  1. Click **App Manager** > **Applications** , then select **Add Application**.

  2. Select **Oracle** in the **Add Application** wizard.

  3. Follow the wizard. In the **Select** section, select the database to back up, and then in the **Manage** section, apply the policy template and the resource profile that you created in [Define policy templates and resource profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices).

  4. To protect the database logs, see [Database log protection in a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices#Log-protection).

  5. Click **Application Settings** in the **Configure** section.

  6. Select the backup capture method based on your needs and the information in [Protect the Oracle environment against data loss, errors, and corruption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro) in the **Application Settings** window.

In the **Application Settings** tab, you can change [application-specific settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings).

  7. Click **Save** , then **Next** , then **Finish**.

  8. You can see the database in the **App Manager Applications** list with a green shield indicating that the backup plan has been applied.




The application may not be captured until the scheduled job runs according to the hours of operation defined in the backup template. For example, if at 10:00 (UTC) you assign a template that has hours of operation from 02:00 (UTC) to 05:00 (UTC), then the first job doesn't start until the appliance has an available job slot at 02:00 (UTC) of the following day. To run a job immediately, perform an [on-demand capture](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

You don't have to apply a backup plan right now. If you want to perform this step later, see [Back up a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect).

**Note:** For best performance, be sure to review the [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues).

## The Oracle DBA Guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
