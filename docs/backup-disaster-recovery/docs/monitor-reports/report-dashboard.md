---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/report-dashboard/
title: Resource usage metrics in the appliance management console reports dashboard \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:25.633465+00:00
---

# Resource usage metrics in the appliance management console reports dashboard  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/report-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Resource usage metrics in the appliance management console reports dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the reports dashboard in the appliance management console and how to view a snapshot of reports and resource usage metrics in the reports dashboard.

The reports dashboard is a _read-only_ dashboard that provides a comprehensive overview of backup health, trends, and potential problems. The dashboard provides a snapshot of backup and recovery metrics, letting you quick assessment of system health and early identification of issues. The dashboard highlights potential problems such as capacity saturation and failed or skipped jobs over the past month or longer, enabling proactive intervention and reducing the risk of data loss.

By default, the reports dashboard page displays the reports data of the most recent seven days. You can change the frequency to 1 hour, 12 hours, 1 day, 7 days, 14 days, or 30 days.

You can use reports dashboard to do the following:

  * **Daily monitoring** : Check the daily job summary and identify any anomalies.
  * **Troubleshooting** : Investigate the root cause of failed or skipped jobs that span a month or more.
  * **Capacity planning** : Plan storage requirements based on historical trends.



## Before you begin

To get the permission that you need to view the reports snapshot dashboard, ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `logging.logEntries.list` permission, which is required to view the reports snapshot dashboard. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The reports dashboard is categorized into the **Reports snapshot** and **Usage** reports.

## About reports snapshot report

The **Reports snapshot** report provides a quick view to track the status of your backup job, identify any past failures, and get detailed insights into backup performance. To view these reports, you need to [upgrade your log bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket) if prompted to upgrade the bucket.

The reports snapshot displays the reports based on the scheduled backup types: **Backup plan** and **Backup template**. You can filter these reports by backup schedule type.

  * **Backup plan** : provides details on resources protected using the [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan) through the Google Cloud console. This report includes a snapshot of the daily jobs summary, failed jobs, and skipped jobs reports.
  * **Backup template** : provides details on resources protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) through the appliance management console. This report includes a snapshot of the daily jobs summary, failed jobs, not run jobs, and canceled jobs reports.



## About usage report

The **Usage** report lets you monitor backup storage consumption and identify trends to optimize and proactively manage resource allocation. The usage report metrics are available for both the scheduled backup types: **Backup plan** and **Backup template**.

To view the **Usage** report, you need to set up and deploy the management console and backup/recovery appliance in the following order:

  1. [Set up and plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan)
  2. [Prepare to deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep)
  3. [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-guide)



After the appliance management console and backup/recovery appliance are deployed, you can view utilization metrics, including usage, performance, and overall health, for resources protected using a backup template. This information helps you understand resource utilization and make informed decisions about resource allocation.

## View reports snapshot for the resources protected using backup plan

Use the following instructions to view the reports for the resources protected using a backup plan.

  1. In the Google Cloud console, go to the **Reports dashboard** page.

[Go to Reports dashboard](https://console.cloud.google.com/backupdr/report-dashboard)

By default, the **Backup plan** is selected in the **Backup schedule type** drop-down and the following reports are displayed:

     * Job summary
     * Failed jobs
     * Skipped jobs



## View reports snapshot for the resources protected using backup template

Use the following instructions to view reports for the resources protected using a backup template.

  1. In the Google Cloud console, go to the **Reports dashboard** page.

[Go to Reports dashboard](https://console.cloud.google.com/backupdr/report-dashboard)

  2. From the **Backup schedule type** drop-down, select **Backup template**. The following reports are available:

     * Job summary
     * Failed jobs
     * Not run jobs
     * Canceled jobs



## View usage report for the resources protected using backup plan

Use the following instructions to view usage reports for the resources protected using a backup plan.

  1. In the Google Cloud console, go to the **Reports dashboard** page.

[Go to Reports dashboard](https://console.cloud.google.com/backupdr/report-dashboard)

  2. Click the **Usage** tab.

By default, the **Backup plan** is selected in the **Backup schedule type** drop-down and the displays the backup vault data volume report.




## View usage report for the resources protected using backup template

Use the following instructions to view usage reports for the resources protected using a backup template.

  1. In the Google Cloud console, go to the **Reports dashboard** page.

[Go to Reports dashboard](https://console.cloud.google.com/backupdr/report-dashboard)

  2. Click the **Usage** tab.

  3. From the **Backup schedule type** drop-down, select **Backup template**. The following usage reports are available:

     * Total volume of data protected
     * Storage pool utilization
     * OnVault pool utilization
     * vDisk utilization

For a complete list of Backup and DR resource metrics and access metrics in a custom dashboard, see [Monitor Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics) resources.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
