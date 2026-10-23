---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts/
title: Set up alerts for failed backups \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:14.355815+00:00
---

# Set up alerts for failed backups  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Set up alerts for failed backups Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to configure the system so that you will receive alerts when Backup for GKE backups fail.

You can create backups in two different ways:

  * By [manually creating](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup#manual) a `Backup` resource.
  * By configuring a schedule when [creating your `BackupPlan` resource](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create_a_backup_plan).



As a best practice, create backups using automatic scheduling. However, it can be challenging to keep track of the status for these automatically created backups. You have two choices:

  * Periodically [view](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup#view_a_backup) the list of `Backup` resources, looking for newly failed backups.
  * Set up an alert to notify you when backup execution fails.



This page describes how to configure an alert policy based on [log events emitted by Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/platform-logging-backup-for-gke) and viewable from the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## Before you begin

Before setting up an alert policy, ensure you have an appropriate [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options).

## Create an alert

To create general log-based alert policies, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). Or, to create an alert policy specifically for Backup for GKE failed backups:

  1. Go to the Logs Explorer page

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Enter the following filter criteria in the **Query** pane:
         
         logName="projects/PROJECT_ID/logs/gkebackup.googleapis.com%2Fbackup_change"
         resource.type="gkebackup.googleapis.com/BackupPlan"
         resource.labels.backup_plan_id="BACKUP_PLAN"
         resource.labels.location="LOCATION"
         jsonPayload.changeType="UPDATE"
         jsonPayload.inputBackup.state="FAILED"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the backup plan for which you want to generate alerts.
     * `BACKUP_PLAN`: the name of the backup plan for which you want to generate alerts.
**Note:** This creates an alert policy for any failed backups of a specific backup plan. If you want to create a single policy for all failed backups, omit the `resource.labels.backup_plan_id` and `resource.labels.location` fields.
  3. In the **Query results** pane, click **Actions** , and then select **Create log alert**.

![](https://docs.cloud.google.com/static/kubernetes-engine/docs/add-on/backup-for-gke/images/create-log-alert.png)

  4. Enter a meaningful name for your alert policy and any documentation you want to make available to recipients of alerts.

  5. Click **Next** twice.

  6. Set the appropriate notification frequency and autoclose duration. We suggest `5 min` and `7 days`.

  7. Click **Next**.

  8. Select the appropriate notification channels and save your alert policy.




After you save the policy, you receive alerts to your notification channels when a backup matching your filter fails.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
