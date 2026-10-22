---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts/
title: Configure log-based alerts for a backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:29.531888+00:00
---

# Configure log-based alerts for a backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure log-based alerts for a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure a log-based alert for a Backup and DR backup/recovery appliance using Logs Explorer in the Google Cloud console.

The Logs Explorer interface for creating and editing log-based alerts guides you through the following steps:

  * Provide a name and description for the alert.
  * Choose the logs for which you want to receive a notification.
  * Set the time between notifications.
  * Set the time for automatic closure of incidents.
  * Specify whom to notify.



You can learn more about Logs Explorer in [View and analyze logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Permissions and roles

To create and manage log-based alerts in Logs Explorer, your Identity and Access Management (IAM) role must include the set of permissions described in [Permissions for log-based alerts](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).

## Create a log-based alert for a backup/recovery appliance

To trigger an alert, you need to have a [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options). You can create the notification channel before creating an alert or while creating an alert.

To create a log-based alert, follow these steps:

  1. In the Google Cloud console, select **Logging** and then **Logs Explorer**.
  2. Use the **Query** pane to define the event on which you want to be notified. You can use the query examples shown in [sample queries](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events#log) in the query pane to configure alerts.

The following is the sample query to get notified on an event with a specific event ID.
         
         logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events"
         jsonPayload.eventId=10046
         

  3. In the header of the **Query results** pane, click **Create alert**. If your window is too narrow, the **Create alert** option appears on the **Actions** menu instead.

  4. In the **Alert details** pane, give the alert a name and description:

     1. Enter a name for your alert in the **Alert Policy Name** field. This name gets displayed in the notification header.
     2. In the **Documentation** field, enter the description for the alert. For information about how you can format and refine the content of this field, see [Using Markdown and variables in documentation templates](https://docs.cloud.google.com/monitoring/alerts/doc-variables). Include the URL of the appliance management console in the documentation field. You can also add the workaround to resolve the event.
  5. Click **Next**.

  6. In the **Choose logs to include in the alert** pane, do the following:

     1. Check the query and results by clicking **Preview logs**. You can also edit the query in this pane, if necessary.
     2. You can add [labels](https://docs.cloud.google.com/monitoring/alerts/labels) to customize notifications and make them more informative. Click **Add a label** and do the following:

        1. Entry a **Display name** for the label. 
        2. Select **Log field name** from the list. These fields are displayed based on the selected query result.
        3. Enter **Regular expression** to extract a value from the field that must contain exactly one regular expression group.
  7. Click **Next**.

  8. Select the minimum time between notifications. This value lets you control the number of notifications you get from this alert if it is triggered multiple times. For example, you can select **5 min** from the options to limit the notifications to every five minutes. You can adjust the incident autoclose duration by selecting an option on the menu if applicable.

  9. Click **Next**.

  10. Select one or more notification channels for your alert, for example, select an email notification channel. If you already have an email notification channel configured, then you can select it from the list. If not, click **Manage notification channels** and add an email channel. For information about creating notification channels, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  11. Click **Save**.

It is a good practice to configure alerts for important [Event IDs](https://docs.cloud.google.com/backup-disaster-recovery/docs/event-codes).




## Test the log-based alert

To test the log-based alert you created, you can manually write a log entry that matches the query. To write the log entry, follow these steps:

  1. Go to the [`logEntries.write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write) reference page, or click the following button:

[Go to logEntries.write](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write)

  2. Configure the following log entry by changing the PROJECT_ID variable to your project ID. If your alert policy includes or excludes specific event IDs then you need to modify the event ID as well:
         
         "entries": [
           {
             "jsonPayload": {
               "eventId": 10046,
               "errorMessage": "this is a manually generated error message created for testing"
             },
             "resource": {
               "type": "backupdr.googleapis.com/BackupRecoveryAppliance",
             },
             "severity": "ERROR",
             "logName": "projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events",
           }
           ]
         

  3. Copy the log entry you configured previously.

  4. In the **Try this API** pane, follow these steps:

     1. Replace the content in the **Request body** field in **APIs Explorer** with the log entry you copied in the previous step.
     2. Click **Execute**. If prompted, follow the authentication flow.

If the logEntries.write call is successful, then you get an HTTP 200 response code and an empty response body, {}. For more information about APIs Explorer, see [Using the APIs Explorer](https://docs.cloud.google.com/logging/docs/api). The APIs Explorer works the same way with the Cloud Logging API.

The log entry matches the filter specified for the alert in the following ways:

     * The logName value specifies the backup/recovery appliance event sign in for your Cloud project.
     * The severity value for this log entry is ERROR.
     * The jsonPayload contains a 10046 pool full event.

After you write the log entry, the following sequence occurs:

     1. The new log entry appears in the "Logs Explorer and triggers the alert.
     2. An incident is opened in Cloud Monitoring.
     3. You receive a notification for the incident. If you configured an email notification channel, then the notification displays.



You can click **View incident** in the email to see the incident in **Cloud Monitoring**. For more information about incidents including how to acknowledge and close them, see [Manage incidents for log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-incidents).

## Create multiple alert policies

You may want to create alert policies based on the priority and urgency of events. From alerting perspective, events can be broadly categorized into the following categories:

  1. Events that are required to be attended urgently and hence require more frequent notifications. For example, the event ID 43901 (failed snapshot job) needs to be reported every 30 minutes. Use the following query to create the alert.
         
         Policyname = 'Snapshot job has failed'
             Notification rate limit = 30 min
             logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events" AND jsonPayload.eventId=43901
         

  2. Events that are less urgent and hence require less frequent notifications. For example, the event ID 10085 (backup plan violations) need to only be reported once per day. Use the following query to create the alert.
         
         Policyname = 'Backup Plan Violation has occurred'
             Notification rate limit = 1 day
             logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events" AND jsonPayload.eventId=10085
         

  3. Events that are non-impacting and can be ignored. For example, the event IDs 10229 (exceeded storage errors) and 42356 (file changes have been detected) can be ignored, as they are false positives. Use the following query to create the alert.
         
         Policyname = 'Backup/DR event has occurred'
             Notification rate limit = 6 hr
             logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbackup_recovery_appliance_events" AND NOT jsonPayload.eventId=(10085 OR 10229 OR 42356 OR 43901)
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
