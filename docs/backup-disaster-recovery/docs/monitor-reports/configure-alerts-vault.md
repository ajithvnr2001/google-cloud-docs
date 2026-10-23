---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts-vault/
title: Configure a log-based alert for vaulted resources \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:02.206635+00:00
---

# Configure a log-based alert for vaulted resources  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure a log-based alert for vaulted resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure a log-based alert for vaulted resources from the **Log Explorer** page in the Google Cloud console.

The **Logs Explorer** page guides you through the following steps to create and edit log-based alerts:

  * Provide a name and description for the alert.
  * Choose the logs you want to receive a notification for.
  * Set the time interval between notifications.
  * Set the time for automatic closure of incidents.
  * Specify whom to notify.



You can configure alerts for the backup and restore job categories: `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, and `RESTORE`.

You can also configure alerts for the backup plan and backup plan association job categories: `UPDATE`.

The available job statuses are: `SUCCESSFUL`, `FAILED`, `SKIPPED`, and `RUNNING`.

You can configure one or more notification channels, such as Google chat, email, SMS, or chat program channels, to receive notifications when an alert occurs. For instructions, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

## Before you begin

  * [Assign permissions for log-based alerting policies](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).



## Create a log-based alert

To notify an alert, you need to have a [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options). You can create the notification channel before creating an alert or while creating an alert.

Use the following instructions to create a log-based alert.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** pane define the alert on which you want to be notified.

     * The following query is an example to get notified whenever a scheduled backup job fails using Backup and DR:
           
           logName="projects/PROJECT_ID/logs/backupdr.googleapis.com/LOG_NAME"
            jsonPayload.jobCategory="SCHEDULED_BACKUP"
            jsonPayload.jobStatus="FAILED"
           

Replace the following:

       * `PROJECT_ID`: the name of the project.
       * `LOG_NAME`: the name of the log, either:

         * `bdr_backup_plan_jobs`: jobs related to a backup plan
         * `bdr_backup_plan_association_jobs`: jobs related to backup plan association in the administrator project, in case of cross-project protection.
         * `bdr_backup_plan_association_source_jobs`: jobs related to backup plan association in the workload project.
     * The following query is an example to get notified whenever a scheduled backup job fails using Backup for GKE:
           
           logName="projects/PROJECT_ID/logs/gkebackup.googleapis.com/bfg_backup_restore_jobs"
            jsonPayload.jobCategory="SCHEDULED_BACKUP"
            jsonPayload.jobStatus="FAILED"
           

Replace the following:

     * `PROJECT_ID`: the name of the project.
  3. In the header of the **Query results** pane, click **Create alert**.

  4. In the **Alert details** section, do the following:

     1. In the **Alert Policy Name** field, enter a name for your alert. This name gets displayed in the notification header.
     2. In the **Documentation** field, enter the description for the alert. For information about how you can format and refine the content of this field, see [Using Markdown and variables in documentation templates](https://docs.cloud.google.com/monitoring/alerts/doc-variables).
  5. Click **Next**.

  6. In the **Choose logs to include in the alert** section, do the following:

     1. Click **Preview logs** to check the query and results. You can also edit the query in this pane, if necessary.
     2. Click **Add a label** and do the following. The [labels](https://docs.cloud.google.com/monitoring/alerts/labels) let you customize notifications and make them more informative.

        1. In the **Display name** field**,** enter a name for the label.
        2. From the **Log field name** list, select a log field name. These fields are displayed based on the selected query result.
        3. In the **Regular expression** field, enter an expression to extract a value from the field that must contain exactly one regular expression group.
  7. Click **Next**.

  8. In the **Set notification frequency and autoclose duration** section, do the following:

     1. From the **Time between notifications** list, select the minimum time between notifications. This value lets you control the number of notifications you get from this alert if it is triggered multiple times.
     2. From the **Incident autoclose duration** list, select a duration after which the incident to be closed automatically when matching log entries are absent.
  9. Click **Next**.

  10. From the **Notification channels** list, select one or more notification channels for your alert. If you don't have a notification channel configured, click **Manage notification channels** to create one. For instructions, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  11. Click **Save**.




## Test the log-based alert

To test the log-based alert you created, you can manually write a log entry that matches the query. 

Use the following instructions to write the log entry.

  1. Go to the [`logEntries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write) reference page.

[Go to logEntries.write](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write)

  2. Configure the following log entry by changing the `PROJECT_ID` variable to your project ID.

     * For Backup and DR, run the following command:
           
           {
                     "entries": [
                     {
                        "jsonPayload": {
                           "jobCategory": "SCHEDULED_BACKUP",
                           "jobStatus": "FAILED"
                        }
                     }
                     ],
                     "resource": {
                     "type": "backupdr.googleapis.com/BackupDRProject"
                     },
                     "logName": "projects/PROJECT_ID/logs/backupdr.googleapis.com/bdr_backup_restore_jobs"
                  }
           

Replace PROJECT_ID with the name of the project.

     * For Backup for GKE, run the following command:
           
           {
                     "entries": [
                     {
                        "jsonPayload": {
                           "jobCategory": "SCHEDULED_BACKUP",
                           "jobStatus": "FAILED"
                        }
                     }
                     ],
                     "resource": {
                     "type": "gkebackup.googleapis.com/Project"
                     },
                     "logName": "projects/PROJECT_ID/logs/gkebackup.googleapis.com/bfg_backup_restore_jobs"
                  }
           

Replace PROJECT_ID with the name of the project.

  3. Copy the log entry you configured previously.

  4. In the **Try this API** pane, follow these steps:

     1. In the **Request body** field, replace the content with the log entry you copied in the previous step.
     2. Click **Execute**. If prompted, follow the authentication flow.
  5. If the `logEntries.write` call is successful, then you get an HTTP `200` response code and an empty response body, `{}`. For more information about **APIs Explorer** , see [Using the APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer).

The log entry matches the filter specified for the alert in the following ways:

     * The `logName` value specifies the backup or restore job logs in your cloud project.
     * The `jsonPayload` contains a failed job category, `SCHEDULED_BACKUP`, which indicates that the log is related to a backup scheduled by a backup plan.
     * The `jsonPayload` contains the field job status as `FAILED`, which signifies that the job is failed.
  6. After you write the log entry, the following sequence occurs:

     1. The new log entry appears in the Logs Explorer and triggers the alert.
     2. An incident is opened in the **Cloud Monitoring** page.
     3. You receive a notification for the incident. If you configured an email notification channel, then the notification displays.

You can click **View incident** in the email to see the incident in the **Cloud Monitoring** page. For more information about incidents including how to acknowledge and close them, see [Manage incidents for log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-incidents).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
