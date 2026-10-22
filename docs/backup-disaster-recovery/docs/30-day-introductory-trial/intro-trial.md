---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial/
title: 30-day introductory trial for Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:05.009584+00:00
---

# 30-day introductory trial for Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  30-day introductory trial for Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

The 30-day introductory trial for Backup and DR lets you evaluate data protection features for your workloads without incurring backup management or vault storage charges. When the 30-day trial period ends, your project is automatically upgraded to paid usage, and standard charges apply for backup management and vault storage. This document describes trial eligibility, initiation, pricing, available features, and resource limitations.

* * *

## Trial features and capabilities

During the 30-day introductory trial, you can explore and evaluate core Backup and DR product features without incurring backup management or vault storage charges. When the 30-day trial period ends, your project is automatically upgraded to paid usage, and standard Backup and DR pricing applies for backup management and vault storage. You can test the following standard data protection capabilities across your workloads:

Capability | Description  
---|---  
[Store backups in immutable backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) |  Store backups in a Google-managed vault that provides isolated storage of immutable backups with enforced retention.   
[Manage workload backups centrally](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan) |  Manage workload backups across Google Cloud resources and enterprise applications from a single interface.   
[Monitor backup operations](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor) |  Get real-time visibility into backup operations with detailed monitoring, customizable alerts, and automated reports.   
[Delegate backup management](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control) |  Retain centralized control over policies while empowering teams to manage their own backups.   
  
## Overview

You can use the 30-day introductory trial to explore Backup and DR and evaluate data protection capabilities for your workloads for up to 30 days. You can enable the trial using the Google Cloud console or the REST APIs. After activation, you have access to standard Backup and DR features to protect, monitor, and manage your backups. For pricing details, see [Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing).

The following table provides information about the 30-day introductory trial for Backup and DR:

Eligibility  |  You are eligible to subscribe to the Backup and DR introductory trial once for every project for a 30-day period. The introductory trial is designed to give you a fresh evaluation of Google Cloud Backup and DR. Therefore, it cannot be activated on a project that meets either of these conditions:

  * The project already has an active Google Cloud Backup and DR configuration (the API is enabled and an appliance management console or backup vault is set up).
  * An introductory trial has already been enabled on this project within the past 12 months.

  
---|---  
Initiation  |  You can subscribe to the Backup and DR trial using the Google Cloud console or the REST APIs. To initiate the trial, you need the Service Usage Admin role (`serviceusage.services.enable` permission).  
Duration  |  Your introductory trial ends when one of the following occurs:

  * 30 days have elapsed since you initiated the trial.
  * You upgrade your trial to paid usage.
  * You disable the Backup and DR API on the project it was enabled on.

You can cancel your trial at any time. When you do, existing backups are not removed automatically and they continue to incur storage charges after the 30-day trial period is over until you delete them. To avoid these charges, you must manually delete that backup data and remove resources from all backup policies. **Note:** If you don't disable your trial after the 30-day introductory trial period, the project is upgraded to paid usage and charges are applied as per Backup and DR pricing in the same project where the resources are backed up and backups are stored.  
Features  |  All features are available during the trial. Backup and DR supports backing up Compute Engine instances, Persistent Disks, Cloud SQL instances, AlloyDB clusters, Google Cloud VMware Engine, file systems, and enterprise databases such as SAP HANA, Microsoft SQL Server, IBM Db2, Oracle, and PostgreSQL. For more details, see the Backup and DR [support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).  
Self-managed storage  |  In addition to workloads in Google Cloud, Backup and DR also supports self-managed storage using backup/recovery appliances managed by a appliance management console. The appliance management console and backup/recovery appliances are available in these [supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan#regions).  
Service level agreement (SLA)  |  SLAs might be limited during the trial period.  
  
When the 30-day trial period ends, your project is automatically upgraded to paid usage, and standard charges apply. For more information about Backup and DR, see the [Product overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).

## Pricing

Before you subscribe to the Backup and DR introductory trial, ensure that Cloud Billing is enabled for your project. If you are a new user, sign in to the Google Cloud console with your Google Cloud account and set up a Cloud Billing account.

During the trial, we don't charge you for backup management or for backup storage data in the backup vault. However, you are charged for inter-region data transfers, multi-regional uploads and downloads, self-managed storage, and backup/recovery appliance costs, when applicable.

When the 30-day trial period ends, your project is automatically upgraded to paid usage, and standard charges apply for backup management and backup storage data in the backup vault. For full pricing details, see the [Backup and DR pricing](https://docs.cloud.google.com/backup-disaster-recovery/pricing) page.

## Limitations

The 30-day introductory trial for Backup and DR has the following limitations:

  * You can activate this trial only once for a project.

  * Once activated for a project, the trial period lasts for 30 days.

  * You can store up to 50 TiB of backup storage data per backup vault.

  * You can create up to 10 backup vaults.

  * SLAs might be limited during the trial period.

  * Google Cloud can discontinue the trial at any time.




Most users find these resource limits sufficient for a thorough evaluation. If your business needs require a higher limit during evaluation, contact support to request an extension.

## Get support

For product-specific issues, contact Cloud Customer Care. For questions, feedback, or support related to the trial, contact [gcbdr-intro-trial@google.com](mailto:gcbdr-intro-trial@google.com).

**Note:** Trial inclusions and conditions may be changed, suspended, or discontinued at any time without prior notice.

## Considerations

  * **Introductory trials are unavailable in projects with an active Backup and DR configuration** : You cannot configure a new introductory trial if the Backup and DR API is already enabled and a appliance management console or backup vault is set up. You are also ineligible if an introductory trial was enabled on this project within the past 12 months. Instead, subscribe to a trial using a different project or create a new Google Cloud project specifically for your trial.

  * **The introductory trial cannot be paused** : The 30-day trial period runs continuously from the moment you activate it and is designed to be used in one single, continuous period.

You can unsubscribe from the trial at any time; however, be aware that this is a final action. If you unsubscribe, you won't be able to reactivate the current trial and you will lose eligibility to start a new trial on the same project for the next 12 months.

We recommend activating the trial only when you are ready to evaluate it fully over 30 consecutive days.

  * **The default resource quota for the introductory trial is 50 TiB** : Backup jobs fail after you reach the default resource quota. Quotas can be increased for your trial evaluation. To extend your quota, contact Cloud Customer Care or contact us at [gcbdr-intro-trial@google.com](mailto:gcbdr-intro-trial@google.com).

  * **Projects automatically upgrade to paid usage and incur charges after the trial completes** : After the 30-day introductory trial period ends, your project automatically upgrades to paid usage, and standard charges apply for backup management and vault storage. Your backups are not automatically removed at the end of the trial and continue to incur storage charges until you manually delete them.

To clean up your data after the trial ends, avoid setting a higher enforced retention period, higher expiration in the backup rule, or enabling a retention lock on your backups during the trial. A higher enforced retention period or locked retention policy blocks early deletion of backups, which leads to ongoing charges after your trial has finished.




## What's next

  * [Configure and manage the 30-day introductory trial for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/configure-trial)

  * Learn about [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).

  * For details about Backup and DR pricing after the trial period, see the [Pricing page](https://docs.cloud.google.com/backup-disaster-recovery/pricing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
