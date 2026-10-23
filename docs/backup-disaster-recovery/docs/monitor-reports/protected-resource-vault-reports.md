---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-vault-reports/
title: Protected resource reports for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:14.341995+00:00
---

# Protected resource reports for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-vault-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protected resource reports for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of prebuilt protected resource reports, which are available in BigQuery and Data Studio. These reports are displayed for resources that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink) in the same project where the logs are being routed through the log sink.

**Note:** If you want to learn about the protected resource report that are protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Protected Resource reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-reports).

The protected resource report includes the following fields:

  * **date** : The date when the protected resource information was last updated.
  * **resource_type** : The type of resource, for example, a Compute Engine.
  * **resource_name** : The name of the protected resource.
  * **resource_project_name** : The name of the project where the resource exists.
  * **resource_data_size_in_gib** : The data size of the protected resource.
  * **backup_vault_name** : The name of the backup vault in which the backups of the protected resource are stored.
  * **backup_plan_name** : The name of the backup plan that is associated with the protected resource. 
  * **backup_rules.rule_name** : The name of the backup rule used to backup jobs.
  * **backup_rules.recurrence** : The backup recurrence type, which can be hourly, daily, weekly, monthly, or yearly.
  * **backup_rules.recurrence_schedule** : The recurrence schedule of a backup based on the backup rule.
  * **backup_rules.backup_window** : The backup window where you have defined the timeframe of when backup jobs can start. The backup window uses the 24-hour clock format, with start and end times between 00 and 24 hours, a minimum of six hours for the window.
  * **backup_rules.backup_window_time_zone** : The timezone in which the backups are scheduled.
  * **backup_rules.retention_days** : The duration in days for which the backups should be retained in the backup vault before they are deleted.
  * **last_backup_plan_assoc_date** : The timestamp that shows when the backup plan was last associated, which is in the YYYY-MM-DDTHH:MM:SS.SSSZ format.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault.
  * **resource_location** : The location of the protected resource.
  * **resource_id** : The ID of the protected resource.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
