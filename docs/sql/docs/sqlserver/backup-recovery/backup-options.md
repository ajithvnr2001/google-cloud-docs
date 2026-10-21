---
url: https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options/
title: Choose your backup option \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:27.029024+00:00
---

# Choose your backup option  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Choose your backup option Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options "View this page for the PostgreSQL database engine") | SQL Server

This document explains the two backup options for your Cloud SQL instances, including their key features and configurations. This helps you choose the most suitable option for your instances.

Before you can use backups with your Cloud SQL instances, you must choose a backup option for each instance. Cloud SQL offers the following backup options:

  * **Enhanced backups**: This option manages and stores backups in a centralized backup management project. It uses [ Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr) and provides enforced retention, granular scheduling, and monitoring. Pricing for enhanced backups is managed by [Backup and DR Service pricing](https://cloud.google.com/backup-disaster-recovery/pricing).
  * **Standard backups**: Cloud SQL creates, manages, and stores these backups in the same project as your Cloud SQL instances.



The backup option you choose defines the features and configuration options available for your Cloud SQL instance. Although instances can't use multiple backup options simultaneously, Cloud SQL lets you switch between these backup options as needed.

**Note:** If your instance was created before the [enhanced backups launch](https://docs.cloud.google.com/sql/docs/sqlserver/release-notes#July_31_2025), then your instance is using the standard backups option. To upgrade your instance to the enhanced backups option, see [Enable enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-enhanced-backups#enable). For new instances, you'll need to select a backup option when you [create the instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

The following table provides an overview of the key features available with each backup option:

Features | Standard backups | Enhanced backups  
---|---|---  
Centralized backup management across projects | - | ✔  
Backup vault | - | ✔  
Automated backup schedule  | Daily  | Hourly, daily, weekly, monthly, yearly  
On-demand backups | ✔ | ✔  
Multi-region backups | ✔ | ✔  
Final backup in instance deletion | ✔ | ✔  
Backup retention period | 1 year | 10 years  
Retain all backups on instance deletion | ✔ | ✔  
Retain backups on project deletion | - | ✔  
Enforced retention with retention lock | - | ✔  
Point-in-time recovery using logs | ✔ | ✔  
Point-in-time recovery after instance deletion | ✔ | ✔  
Cross-region backup and restore | ✔ | -  
CMEK support | ✔ | ✔  
  
For detailed information about these backup options, see Standard backups and Enhanced backups. For more information about how backups work in Cloud SQL, see [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups).

## Enhanced backups

With enhanced backups, you can use Backup and DR to manage and store all backups for your Cloud SQL instances across various projects in one central backup project. Backup and DR provides centralized management, monitoring, and reporting of day-to-day backup operations in one place. Backups are stored in a [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup-vaults), which is a Google-managed secured and isolated storage resource, managed by Backup and DR, and [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup_plans) manage the backup and restore settings. This provides immutable and indelible backups that are independent of the source project. For more information about how backups work with Backup and DR, see [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).

With enhanced backups, you can use a centralized backup project that hosts your [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup-vaults) and [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup_plans) that you associate across all your Cloud SQL instances. These plans can also be linked across multiple projects.

**Note:** Cloud SQL recommends creating your backup vault and backup plan in a different project than your Cloud SQL instances.

When you attach a backup plan to a Cloud SQL instance, the existing backup and restore settings are overwritten by the backup plan. The plan containing your backup and restore settings is stored in the centralized backup project, and any backups created when the plan is active on your Cloud SQL instance are stored in the backup vault in the backups project.

If the Backup and DR is managed in a separate Google Cloud project, then backups are protected when a source or workload project is deleted. Roles and responsibilities are managed by the [`Backup and DR Admin`](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles), and are separate from `Cloud SQL Admin` roles and responsibilities.

You can retain backups after instance deletion, or take a final backup of your instance prior to deletion. All backups taken as part of enhanced backups can be used to restore an instance while its live, or after it is deleted.

When you use enhanced backups for an instance protected with a customer-managed encryption key (CMEK), the backup is protected using the same key as the instance, not the vault CMEK.

### Backup storage

Backups are stored in a centralized location called a backup vault. A backup vault is a secured and isolated storage, managed by Backup and DR. A backup vault stores backups in a [single region](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions) or a [multi-region](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions) as long as the selected location is [compatible with your instance's location](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility). For more information about where you can create a backup vault, see [Backup vault supported locations](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#locations).

Cloud SQL recommends that you use a backup vault that is in a different project than your Cloud SQL instance. For more information, see [Backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr#backup-vaults).

### Backup retention

Enhanced backups allow you to take [on-demand](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#on-demand-backups) and [automated backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#automated-backups). Unlike standard on-demand backups (which may be stored indefinitely), enhanced on-demand backups support user-defined custom retention periods up to 10 years. Any backups created when using the enhanced backups option are stored in the backup vault and are governed by the allowed retention range determined by the intersection of the backup vault's minimum enforced retention and the backup plan's maximum custom retention setting. If `max_custom_on_demand_retention_days` is not explicitly configured in the backup plan, a default upper limit of the backup vault's minimum enforced retention plus 30 days is applied, and regardless of configuration, the maximum allowed retention for any custom on-demand backup is 10 years (3,653 days).

If you delete your instance, then all of your instance's backups that were created when your instance was live are [retained](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#recovery-backups) automatically and follow the same retention settings set by the backup plan when the instance was live. If you elect to take a [final backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#final-backup) of your instance prior to deletion, then you can set the backup retention for the final backup for up to 10 years as well.

### Backup costs

In enhanced backups, the cost for backups are based on the total size of the backup that is stored in the backup vault. These backups are created based on the backup configuration in the instance's associated backup plan. The total cost is calculated by Backup and DR, and based on [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

### Limitations

The following limitations apply when using enhanced backups:

  * The Backup vault and your Cloud SQL instance must be in the same region or [compatible with your instance's location](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility) for multi-region Backup vault.
  * You can't create a [Disaster Recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery) for an instance using enhanced backups.
  * If your instance has a [Disaster Recovery (DR) replica](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery), then you can't enable enhanced backups for the instance.
  * You can't associate a backup plan with a replica instance.
  * If your instance is using enhanced backups, then you can't demote the instance to a replica.
  * For Cloud SQL instances, you can only select and associate with a backup vault that has a minimum enforced retention period of 10 years (3,653 days) or less.



## Standard backups

Standard backups is the backup option that is managed by Cloud SQL. Backups are created, managed, and stored in the same project as your Cloud SQL instances. Unlike enhanced backups, where backup settings are defined by a backup plan, backup configurations for standard backups are set at the instance level and defined in the instance's settings. Therefore, if you have multiple Cloud SQL instances, then you'll need to define the backup configurations for each instance separately in the instance's backup settings. Any backups created as part of standard backups are stored in the same project as the instance.

With standard backups, you can take automated and on-demand backups for your Cloud SQL instances. You can also select to [retain all backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#recovery-backups) and take a [final backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#final-backup) of your data at instance deletion. This lets you recreate any instances that you delete. However, if you don't retain backups or take a final backup prior to deleting your instance, then Cloud SQL deletes all instance backups automatically.

### Backup storage

Backups are stored in the same location for instances in both high availability (HA) or non-HA configurations. In high availability configurations, you'll still be able to access your instance's backups in the event of a failover or switchover to the secondary instance.

You can define your backup locations as follows:

  * Default locations that Cloud SQL selects, based on the location of the original instance.
  * Custom locations that you choose when you don't want to use the default location.



#### Default backup locations

If you don't specify a storage location, then your backups are stored in the multi-region that is geographically closest to the location of your Cloud SQL instance. For example, if your Cloud SQL instance is in `us-central1`, then your backups are stored in the `us` multi-region by default.

**Note:** When restoring data from a backup, restore it to an instance in a region that's available. To view a list of all backups for an instance in a region that's undergoing an outage, use the **-** wildcard with the `gcloud sql backups list --instance` command or the `backupRuns.list` API. For more information, see [Viewing a list of backups during an outage](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#backuplist). You can then restore the data from the backup to a new or existing instance in a region that's not undergoing an outage. 

#### Multi-region backups

Standard backups let you have single or multi-region backup location configurations. In a single-region configuration, backups are replicated across the different zones within the region. In a multi-region configuration, it's recommended that backups be in the same region as the instance to minimize latency and avoid potential backup failures due to organization policies, or location-based limitations.

#### Custom backup locations

Cloud SQL lets you select a custom location for your backup data. This is useful if your organization needs to comply with data residency regulations that require you to keep your backups within a specific geographic boundary. If your organization has this type of requirement, it probably uses a [Resource Location Restriction organizational policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). With this policy, when you try to use a geographic location that doesn't comply with the policy, you see an alert on the **Backups** page. If you see this alert, then you need to change the backup location to a location the policy allows.

When selecting a custom location for a backup, consider the following:

  * **Cost** : one cluster in your instance might be in a lower-cost region than the others.
  * **Proximity to your application server** : you might want to store the backup as close to your serving application as possible, to reduce potential latency.
  * **Storage utilization:** you need enough storage space to keep your backup as it grows in size. Depending on your workload, you might have clusters of different sizes or with different disk usages. This might factor into which cluster you choose.



You can select any available Cloud SQL location and multi-region location when choosing your custom backup location. For a complete list of valid regional values, see [Instance Locations](https://docs.cloud.google.com/sql/docs/sqlserver/locations#location-r). For a complete list of multi-regional values, see [Multi-regional locations](https://docs.cloud.google.com/sql/docs/sqlserver/locations#location-mr).

For more information about setting and view backup locations for an instance, see [Set a custom location for backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#locationbackups) and [View backup locations](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#view_backup_locations).

**Note:** If you change the location where backups are stored, existing backups remain in their original location.

### Backup retention

Standard backups allow you to take automatic and on-demand backups. Automated backups can be retained from 7 days to 365 days, and the default is 7 days for Cloud SQL Enterprise edition instances and 15 days for Cloud SQL Enterprise Plus edition instances. On-demand backups are retained indefinitely, until either the backup is deleted, or the instance containing the backup is deleted.

If you enable backup retention after instance deletion for your on-demand and automated backups, then those backups follow the same retention settings of 1 to 365 days for automated backups, and indefinitely for on-demand backups. For more information, see [Retain backups after instance deletion](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#recovery-backups).

### Backup costs

In standard backups, backup costs are based on the [total size of the backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#backup-size), its storage location and retention settings.

You can configure how many automated backups to retain, from 1 to 365.

For more information about pricing related to backups, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing#storage-and-networking-pricing).

### Backup rate limitations

Cloud SQL limits the rate for backup operations on the data disk. You're allowed a maximum of five backup operations every 50 minutes per instance per project. If a backup operation fails, it doesn't count towards this quota. If you reach the limit, the operation fails with an error message that tells you when you can retry.

Cloud SQL uses tokens from a bucket to determine how many backup operations are available at any one time. Each instance has a bucket. There's a maximum of five tokens in the bucket that you can use for backup operations. Every 10 minutes, a new token is added to the bucket. If the bucket is full, the token overflows.

Each time you issue a backup operation, a token is granted from the bucket. If the operation succeeds, the token is removed from the bucket. If it fails, the token is returned to the bucket. The following diagram shows how this works:

![How tokens work](https://docs.cloud.google.com/static/sql/images/backup-rate-limiting.png)

## What's next

  * [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups)
  * [Restore from a backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring#restorebackups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
