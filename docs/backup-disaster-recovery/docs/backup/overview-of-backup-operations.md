---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/overview-of-backup-operations/
title: Overview of backup operations \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:23.019979+00:00
---

# Overview of backup operations  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/overview-of-backup-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Overview of backup operations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of backup operations for Google Cloud resources using Backup and DR in the Google Cloud console.

With Google-managed backups, you can protect workloads by sending backups directly to an immutable backup vault. Storing backups in a backup vault provides enforced retention and protection against accidental or malicious deletion.

## Core components of backup operations

Before you can perform backup operations, you must configure the following core components:

  * **Backup vault** : a [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) is a centralized storage container where backup sets are stored. backup vaults provide immutability and enforced retention periods. You can configure a vault to store backups in a single region or across multiple regions. For more information, see [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).

  * **Backup plan** : a [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan) defines automated backup strategies for your resources. Each backup plan contains one or more backup rules that specify:

    * The backup frequency (hourly, daily, weekly, monthly, or yearly).

    * The retention period for captured backups.

    * The target backup vault where backups are stored.

    * A backup window defining the specific timeframe when backup jobs can start (minimum of six hours in 24-hour clock format).

    * You can create a backup plan with the following settings:

      * [With a backup rule](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create-with-rule)
      * [Without a backup rule](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create-without-rule)
      * [With selective disk backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#selective-disk-backup)
  * **Customer-managed encryption keys (CMEK)** : you can optionally use [CMEK](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek) to encrypt backups stored in a backup vault with keys managed in Cloud Key Management Service. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/cmek-create-key).




## Backup operations

You can back up supported workloads to a backup vault using two primary methods:

  * **Scheduled backups** : when you assign a backup plan to a protected resource, Backup and DR automatically captures and retains backups according to the backup rules defined in the plan.

  * **On-demand backups** : you can trigger an immediate, on-demand backup at any time. On-demand backups are ideal for capturing a known good recovery point before making major infrastructure or database changes, or for _ad hoc_ data protection.




### Types of backup operations

Depending on your resource protection requirements, you can perform different types of backup operations:

  * **Full virtual machine (VM) backup** : protects a Compute Engine instance and includes all attached boot and non-boot disks in the backup.

  * **Selective disk backup** : lets you configure criteria in a backup plan (using `boot-disk-only` or label exclusion properties `disk-exclusion-labels`) to exclude specific attached non-boot disks from Compute Engine instance backups. When you restore an instance from a selective disk backup, only the protected disks are restored. See [Selective disk backup for Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#selective-disk-backup).

  * **Independent disk backup** : backs up individual Persistent Disk volumes directly without backing up an entire Compute Engine instance. See [Back up disks to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-backup).

  * **Database and file share backup** : captures automated enhanced backups for Cloud SQL instances, AlloyDB for PostgreSQL clusters, and Filestore file shares.




### Supported workloads for backup

You can configure scheduled and on-demand backups in the Google Cloud console for the following Google Cloud resources:

  * **Compute Engine instances** : protect Compute Engine instances, including boot disks and attached non-boot disks. You can also [protect instances using the default backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/backup-plan-default) or [migrate existing backup configurations to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/migrate-compute-instance-backup-to-vault). See [Back up Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).

  * **Persistent Disk** : back up individual persistent disks independently of Compute Engine instances. See [Back up disks to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-backup).

  * **Cloud SQL instances** : configure automated enhanced backups for Cloud SQL databases. See [Back up Cloud SQL instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup).

  * **AlloyDB clusters** : protect AlloyDB for PostgreSQL clusters and databases. See [Back up AlloyDB clusters to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup).

  * **Filestore instances** : back up Filestore file shares and instances. See [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup).




## Ongoing management of backups and protected data sources

For ongoing management of backups and protected data sources, see [Manage backups in a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage) and [Manage data sources](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage).

## What's next

  * [Explore the 30-day introductory trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial)
  * [Review Backup and DR IAM roles and permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control)
  * [Monitor backup jobs in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
