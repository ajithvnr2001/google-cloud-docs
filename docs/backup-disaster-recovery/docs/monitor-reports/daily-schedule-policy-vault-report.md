---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/daily-schedule-policy-vault-report/
title: View daily schedule compliance reports for vaulted backups in Cloud Logging. \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:28.502715+00:00
---

# View daily schedule compliance reports for vaulted backups in Cloud Logging.  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/daily-schedule-policy-vault-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View daily schedule compliance reports for vaulted backups in Cloud Logging. Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of prebuilt daily backup schedule policy reports, which are available in BigQuery and Data Studio. These reports are displayed for resources that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink) in the same project where the logs are being routed through the log sink.

**Note:** If you want to learn about the daily backup schedule policy report that are protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Daily Schedule Compliance reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery).

The daily backup schedule compliance report includes the following fields.

  * **date** : The date that the compliance status is reported on.
  * **resource_type** : The type of resource, for example, a Compute Engine instance.
  * **resource_name** : The name of the resource that is associated with the daily schedule backup policy.
  * **resource_project_name** : The name of the project where the resource exists.
  * **backup_plan_name** : The name of the backup plan that is associated with the source resource.
  * **rule_name** : The name of the backup rule used to backup jobs.
  * **backup_window** : The backup window where you have defined the timeframe of when backup jobs can start. The backup window uses the 24-hour clock format, with start and end times between 00 and 24 hours, and a minimum of six hours for the window.
  * **backup_window_time_zone** : The timezone of the daily schedule backup policy window.
  * **backup_schedule_compliance_status** : The compliance status of the daily schedule backup policy. The status can be pending, successful, or failed.
  * **comment** : A description explaining the compliance status of the daily schedule backup policy.
  * **backup_vault_name** : The name of the backup vault that is used for daily schedule backup policy.
  * **backup_vault_project_name** : The backup vault project that is used for daily schedule backup policy.
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
