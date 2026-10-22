---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-vault-consumption-report/
title: Backup vault consumption report for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:30.390624+00:00
---

# Backup vault consumption report for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-vault-consumption-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup vault consumption report for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of prebuilt backup vault consumption reports, which are available in BigQuery and Data Studio. These reports are displayed for resources that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

You can access this report after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink) in the same project where the logs are being routed through the log sink.

The backup vault consumption report includes the following fields.

  * **date:** The date when the backup vault consumption report was last updated.
  * **resource_type** : The type of resource that is protected in a backup vault, for example, a Compute Engine instance.
  * **resource_name** : The name of the resource that is associated with the protected resource. 
  * **resource_project_name** : The name of the project where the resource exists.
  * **backup_vault_name** : The name of the backup vault that is associated with the protected resource.
  * **backup_vault_stored_bytes_in_gib** : The amount of storage space consumed by backups in GiB in a backup vault.
  * **backup_vault_minimum_enforced_retention_days** : The minimum timeframe in days that backups in that vault are being protected from deletion.
  * **backup_plan_name** : The name of the backup plan that is associated with the resource.
  * **first_available_restore_point** : The timestamp when the first (oldest) backup was taken, which is in the `YYYY-MM-DD HH:MM:SS UTC` format.
  * **last_available_restore_point** : The timestamp when the latest backup was successfully taken, which is in the `YYYY-MM-DD HH:MM:SS UTC` format.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault.
  * **resource_location** : The location of the protected resource.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
