---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-reports-bigquery/
title: Mounted backup reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:38.189274+00:00
---

# Mounted backup reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-reports-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mounted backup reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to view prebuilt mounted backup reports in BigQuery.

The Backup and DR provides prebuilt mounted backup reports that are accessible in BigQuery. You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink.

These reports provide information about the details of the mounted backups present on the backup/recovery appliance.

  * **Appliance ID** : The ID of the appliance associated with the host where the backup is mounted.
  * **Appliance name** : The name of the appliance associated with the host where the backup is mounted.
  * **Last mount date** : The timestamp when the backup was last successfully mounted.
  * **Mounted host ID** : The ID of the host where the backup is mounted.
  * **Mounted hostname** : The name of the host where the backup is mounted.
  * **Mounted backup age in days** : The number of days from when the backup was last mounted.
  * **Mounted image name** : The name of the mounted backup.
  * **Mounted resource label** : The label associated with the mounted resource.
  * **Mounted resource name** : The name of the resource on which the backup is mounted.
  * **Read mode** : The mode in which data gets read from OnVault pool.
  * **Recovery point date** : The timestamp of when the last successful backup was taken.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.
  * **Resource virtual size (GiB)** : The size of the resource in GiB.
  * **Resource size (GiB)** : The size of the protected resource in GiB.
  * **Restorable object** : The object of the application which is restored as part of mount.
  * **Storage consumed (GiB)** : The size of the storage consumed in GiB.
  * **Source image expiration date** : The mounted backup expiration date. It is in YYYY-MM-DDTHH:MM:SS.SSSZ format.
  * **Source image name** : The name of the source backup.
  * **Source image type** : The type of source backup. It can be a snapshot or OnVault backup.
  * **Source hostname** : The name of the source host.
  * **Source host ID** : The ID of the source host where the backup is mounted.
  * **Source resource name** : The name of the source resource.
  * **Source resource ID** : The ID of the source resource.
  * **Username** : The name of the user who initiated the mount operation.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
