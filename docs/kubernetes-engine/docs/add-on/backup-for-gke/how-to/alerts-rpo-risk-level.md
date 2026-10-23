---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts-rpo-risk-level/
title: Set up alerts on RPO risk status of backup plans \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:36.320329+00:00
---

# Set up alerts on RPO risk status of backup plans  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts-rpo-risk-level/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)



Send feedback 

#  Set up alerts on RPO risk status of backup plans Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to set up alerts on the RPO risk level and risk reason of backup plans that are based on the [log events emitted by Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/platform-logging-backup-for-gke) from the Logs Explorer.

In the context of disaster recovery or business continuity planning, _recovery point objective (RPO)_ means the most recent point in time from which data must be restored. It specifies the maximum loss of data due to an infrastructure failure, which is expressed as the amount of time, before the failure, in which write activity is lost.

The **RPO risk level** column indicates the current level of the backup plan's RPO risk. The risk reason field gives details of why the backup plan is at a specific risk level.

Both the RPO risk level and risk reason have a many-to-one mapping, that is, an RPO risk level of 4 can have multiple reasons why it is that number. For a complete list of RPO risk levels and corresponding reasons, see the following table.

## Mapping between RPO risk levels and risk reasons

RPO risk level | RPO risk reason  
---|---  
1 | No risk detected for this BackupPlan.  
2 | This BackupPlan has recent backup failures.  
2 | In training phase, and the risk level will be available after at least four successful backups.  
2 | No RPO config is defined. Switch to an RPO schedule for better protection.  
2 | No schedule is defined. Opt in to an RPO schedule for better protection.  
3 | Recent backups are taking longer. If this trend continues, there is a risk the RPO will no longer be met.  
3 | The most recent backup creation failed.  
3 | The most recent backup execution failed.  
3 | The schedule is paused.  
3 | This BackupPlan has recent backup failures and the schedule is paused.  
3 | In training phase, but this BackupPlan has recent backup failures.  
3 | In training phase, but the most recent backup creation failed.  
3 | In training phase, but the most recent backup execution failed.  
3 | No RPO config is defined and this BackupPlan has recent backup failures. Switch to an RPO schedule after the failure is resolved.  
3 | No schedule is defined and recent backups have failed. Opt in to an RPO schedule for better protection.  
4 | Recent backups are taking longer and the schedule is paused. If this trend continues after unpausing the schedule, there is a risk the RPO will no longer be met.  
4 | The most recent backup creation failed and the schedule is paused.  
4 | The most recent backup execution failed and the schedule is paused.  
4 | In training phase, but the schedule is paused. Unpause the schedule to allow training to complete.  
4 | In training phase, but this BackupPlan has recent backup failures and the schedule is paused.  
4 | In training phase, but the most recent backup creation failed and the schedule is paused.  
4 | In training phase, but the most recent backup execution failed and the schedule is paused.  
4 | No RPO config is defined and the most recent backup creation failed. Switch to an RPO schedule after the failure is resolved.  
4 | No RPO config is defined and the most recent backup execution failed. Switch to an RPO schedule after the failure is resolved.  
4 | No RPO config is defined and the cron schedule is paused. Switch to an RPO schedule for better protection.  
4 | No RPO config is defined and the cron schedule is paused with recent backup failures. Switch to an RPO schedule after the failure is resolved.  
4 | No RPO config is defined and the cron schedule is paused with the most recent backup creation failed. Switch to an RPO schedule after the failure is resolved.  
4 | No RPO config is defined and the cron schedule is paused with the most recent backup execution failed. Switch to an RPO schedule after the failure is resolved.  
4 | No schedule is defined and the most recent backup execution failed. Opt in to an RPO schedule for better protection.  
5 | This BackupPlan has violated RPO. Resolve backup failures, update the target RPO and exclusion windows, or shrink the backup scope as needed for this BackupPlan.  
5 | This BackupPlan has violated RPO and schedule is paused. Resolve backup failures, update the target RPO and exclusion window, or shrink the backup scope as needed for this BackupPlan.  
  
## Before you begin

Before you set up an alert policy, ensure you have an appropriate [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options).

## Create an alert

For more information about creating general log-based alert policies, see [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). Or, to create an alert policy specifically for RPO risk level or RPO risk reasons changes in backup plans, do the following:

  1. Go the Logs Explorer page. [Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** pane, enter the following filter criteria:
         
         logName="projects/PROJECT_ID/logs/gkebackup.googleapis.com%2Fbackup_plan_change"
         resource.type="gkebackup.googleapis.com/BackupPlan"
         resource.labels.backup_plan_id="BACKUP_PLAN"
         resource.labels.location="LOCATION"
         jsonPayload.backupPlanMetadata.rpoRiskLevel>="VALUE"
         jsonPayload.backupPlanMetadata.rpoRiskReason="REASON"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `BACKUP_PLAN`: the name of the backup plan for which you want to generate alerts.
     * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the backup plan for which you want to generate alerts. For example, `us-central1.`
     * `VALUE`: The RPO risk level value for the backup plan you want to be alerted on. The valid values are in the range [1,5]. We recommended setting up alerts on risk level >= 4.
     * `REASON`: (Optional) Select an appropriate risk reason from the table.
  3. To validate the query, click **Run Query**.

  4. In the **Query results** toolbar, expand the **Actions** menu and select **Create log alert**.

  5. In the **Alert details** pane, enter a name for your alerting policy in the **Alert Policy Name** field. For example, `Alert for RPO risk level of backup plan`.

  6. Select an option from the **Policy severity level** menu. Incidents and notifications display the severity level. We recommend setting the severity level to **Critical**.

  7. Enter a description for your alerting policy. You can also include information that might help the recipient of a notification diagnose the problem. For information about how you can format and refine the content of this field, see [Using Markdown and variables in documentation templates](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

  8. Click **Next**.

  9. Set the **Time between notifications** and **Incident autoclose duration**. We recommend setting the time between notifications to one day and the autoclose duration to seven days.

  10. Click **Next**.

  11. Select one or more notification channels for your alerting policy.

  12. Click **Save**.

After you save the policy, you receive alerts to your notification channels when a backup plan matches your filter.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
