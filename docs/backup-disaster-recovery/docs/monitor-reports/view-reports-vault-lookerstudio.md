---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-vault-lookerstudio/
title: View backup plan based reports in Data Studio \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:47.289994+00:00
---

# View backup plan based reports in Data Studio  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-vault-lookerstudio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View backup plan based reports in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view Backup and DR prebuilt reports in Data Studio for vaulted backups.

After you [set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery) in BigQuery, you can view them in Data Studio. Data Studio is a cloud-based business intelligence and data visualization tool that lets you view, modify, and create reports and dashboards.

You can use the Data Studio template to connect to your BigQuery dataset and view the prebuilt reports for vaulted backups that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). The Data Studio template is a pre-designed report or dashboard that gives you a head start for visualizing your data.

## Prerequisite

  * [Set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery)



## View Backup and DR prebuilt reports in Data Studio

To view reports in Data Studio for vaulted backups, you must use the same project ID where logs are routed to BigQuery.

Use the following instructions to view Backup and DR reports in Data Studio for vaulted backups.

  1. Copy the following URL into a text editor and replace `PROJECT_ID` with the name of your project.
  2. Copy and paste the updated URL into the address bar of a web browser after replacing the project ID.
         
         https://lookerstudio.google.com/c/reporting/create
                 ?c.reportId=2ccd44e7-5c1e-4858-9111-2594d785ea58
                 &r.reportName=Backup%20and%20DR%20Reports
                 &ds.ds4.datasourceName=successful_backup_jobs
                 &ds.ds4.billingProjectId=PROJECT_ID
                 &ds.ds4.projectId=PROJECT_ID
                 &ds.ds4.type=CUSTOM_QUERY
                 &ds.ds4.datasetId=bdr_reports
                 &ds.ds4.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.successful_backup_jobs%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds2.datasourceName=backup_jobs_summary
                 &ds.ds2.billingProjectId=PROJECT_ID
                 &ds.ds2.projectId=PROJECT_ID
                 &ds.ds2.type=CUSTOM_QUERY
                 &ds.ds2.datasetId=bdr_reports
                 &ds.ds2.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.backup_jobs_summary%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds10.datasourceName=protected_resource_details
                 &ds.ds10.billingProjectId=PROJECT_ID
                 &ds.ds10.projectId=PROJECT_ID
                 &ds.ds10.type=CUSTOM_QUERY
                 &ds.ds10.datasetId=bdr_reports
                 &ds.ds10.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.protected_resource_details%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds11.datasourceName=backup_vault_consumption
                 &ds.ds11.billingProjectId=PROJECT_ID
                 &ds.ds11.projectId=PROJECT_ID
                 &ds.ds11.type=CUSTOM_QUERY
                 &ds.ds11.datasetId=bdr_reports
                 &ds.ds11.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.backup_vault_consumption%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds9.datasourceName=restore_jobs_details
                 &ds.ds9.billingProjectId=PROJECT_ID
                 &ds.ds9.projectId=PROJECT_ID
                 &ds.ds9.type=CUSTOM_QUERY
                 &ds.ds9.datasetId=bdr_reports
                 &ds.ds9.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.restore_jobs_details%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds7.datasourceName=skipped_backup_jobs
                 &ds.ds7.billingProjectId=PROJECT_ID
                 &ds.ds7.projectId=PROJECT_ID
                 &ds.ds7.type=CUSTOM_QUERY
                 &ds.ds7.datasetId=bdr_reports
                 &ds.ds7.datasetId=bdr_reports
                 &ds.ds7.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.skipped_backup_jobs%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds8.datasourceName=restore_jobs_summary
                 &ds.ds8.billingProjectId=PROJECT_ID
                 &ds.ds8.projectId=PROJECT_ID
                 &ds.ds8.type=CUSTOM_QUERY
                 &ds.ds8.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.restore_jobs_summary%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds12.datasourceName=daily_scheduled_compliance
                 &ds.ds12.billingProjectId=PROJECT_ID
                 &ds.ds12.projectId=PROJECT_ID
                 &ds.ds12.type=CUSTOM_QUERY
                 &ds.ds12.datasetId=bdr_reports
                 &ds.ds12.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.daily_scheduled_compliance%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds6.datasourceName=failed_backup_jobs
                 &ds.ds6.billingProjectId=PROJECT_ID
                 &ds.ds6.projectId=PROJECT_ID
                 &ds.ds6.type=CUSTOM_QUERY
                 &ds.ds6.datasetId=bdr_reports
                 &ds.ds6.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.failed_backup_jobs%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds42.datasourceName=backup_jobs_details
                 &ds.ds42.billingProjectId=PROJECT_ID
                 &ds.ds42.projectId=PROJECT_ID
                 &ds.ds42.type=CUSTOM_QUERY
                 &ds.ds42.datasetId=bdr_reports
                 &ds.ds42.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.backup_jobs_details%60(@DS_START_DATE,%20@DS_END_DATE);
                 &ds.ds5.datasourceName=backup_plan_details
                 &ds.ds5.billingProjectId=PROJECT_ID
                 &ds.ds5.projectId=PROJECT_ID
                 &ds.ds5.type=CUSTOM_QUERY
                 &ds.ds5.datasetId=bdr_reports
                 &ds.ds5.sql=SELECT%20*%20FROM%20%60PROJECT_ID.bdr_reports.backup_plan_details%60(@DS_START_DATE,%20@DS_END_DATE);
         

  3. Click **Authorize**.

  4. Sign in with your Google Cloud account.

You are directed to Data Studio, where you can view [Backup and restore job logs for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backupvault-backup-recovery-jobs), [Protected resource reports for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-vault-reports), and [Backup vault consumption logs for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/vault-consumption-logs). These reports are available with view-only access. You can [export reports](https://support.google.com/looker-studio/answer/7398375?hl) to a CSV file or as individual sheets. You can save this URL for quick access to prebuilt reports.

**Note:** In Data Studio, you can view up to 2 million rows and export up to 750,000 rows of data from a chart.

Data Studio automatically refreshes your report at certain intervals. To change the default data refresh rate, see [Manage data freshness](https://support.google.com/looker-studio/answer/7020039).




For advanced use cases, such as scheduling, emailing, customizing, and sharing, you can make your own copy of the report using the **Edit and share** button.

## Pricing

Data Studio is available at no charge for viewing and creating reports. However, BigQuery is a paid product and you will incur charges for using it when you access BigQuery datasets through the Data Studio. There are no charges for the first 1 TiB BigQuery data processed per month. For detailed pricing information, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing#free) and [Data Studio pricing](https://cloud.google.com/looker-studio#pricing).

## What's next

  * Learn how to [Add data to a report](https://support.google.com/looker-studio/answer/6300774)
  * Learn how to [Share reports](https://support.google.com/looker-studio/answer/6287179)
  * Learn how to [Export reports](https://support.google.com/looker-studio/answer/7398375)
  * Learn how to [Download reports](https://support.google.com/looker-studio/answer/9125317)
  * Learn how to [Schedule automatic report delivery over email](https://support.google.com/looker-studio/answer/9263641)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
