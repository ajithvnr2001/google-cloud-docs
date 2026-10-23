---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts-backup-plan/
title: Set up alerts for paused backup plans \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:46.915839+00:00
---

# Set up alerts for paused backup plans  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts-backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Set up alerts for paused backup plans Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to set up alerts for the paused backup plans based on the logs viewable from the Logs Explorer.

Backup plans can be paused automatically or manually as listed in the [Pause a backup schedule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#pause). To receive notifications when critical backup plans are paused, it's important to set up alerts. This procedure is similar to configuring alerts for failed backups. For instructions, see [Set up alerts for failed backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts).

## Before you begin

Before setting up an alert policy, ensure you have an appropriate [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options).

## Create an alert for paused backup plans

To create general log-based alert policies, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). Or, to create an alert policy specifically for Backup for GKE paused backup plans:

  1. Go to the Logs Explorer page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following filter criteria in the **Query** pane:
         
         logName="projects/PROJECT_ID/logs/gkebackup.googleapis.com%2Fbackup_plan_change"
         resource.type="gkebackup.googleapis.com/BackupPlan"
         resource.labels.backup_plan_id=BACKUP_PLAN"
         resource.labels.location="LOCATION"
         jsonPayload.inputBackupPlan.backupSchedule.paused="true"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `BACKUP_PLAN`: the name of the backup plan for which you want to generate alerts.
     * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the backup plan for which you want to generate alerts. For example, us-central1.

**Note:** If you want to set up alerts for any backup plans across all locations, then you can omit the `resource.labels.backup_plan_id` and `resource.labels.location` fields from the filter.
  3. Click **Run query** to validate the query.

  4. In the **Query results** toolbar, expand the **Actions** menu and select **Create log alert**.

  5. In the **Alert details** pane, enter a name for your alerting policy in the **Alert Policy Name** field. For example, alert for paused backup plan.

  6. Select an option from the **Policy severity level** drop-down. Incidents and notifications display the severity level. We recommend setting the severity level to **Critical**.

  7. Enter a description for your alerting policy. You can also include information that might help the recipient of a notification diagnose the problem. For information about how you can format and refine the content of this field, see [Using Markdown and variables in documentation templates](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

  8. Click **Next**.

  9. Set the **Time between notifications** and **Incident autoclose duration**. We suggest setting notification to one day and autoclose duration to seven days.

**Note:** A notification is only triggered when a backup plan status changes to **paused**. A single status change will generate a single notification. If the backup plan becomes active and then pauses again, a new notification will be sent only after 24 hours have passed since the previous notification.
  10. Click **Next**.

  11. Select one or more notification channels for your alerting policy.

  12. Click **Save**.

After you save the policy, you receive alerts to your notification channels whenever a backup plan matching your filter is paused.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
