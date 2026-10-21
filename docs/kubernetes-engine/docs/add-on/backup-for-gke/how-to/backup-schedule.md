---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule/
title: Automatic backup creation and deletion \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:02.902040+00:00
---

# Automatic backup creation and deletion  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Automatic backup creation and deletion Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page provides an overview of automatic backup creation and deletion. It details backup scheduling methods, [Recovery Point Objective (RPO)](https://en.wikipedia.org/wiki/Disaster_recovery) risk levels, and backup deletion policies.

## Automatic backup creation

Backup for GKE provides two backup scheduling methods to automatically create backups:

  * Smart scheduling
  * Cron scheduling



When creating a backup plan, you can select either scheduling method.

### Smart scheduling

Smart scheduling automatically creates backups when needed to satisfy an RPO you set. Smart scheduling accommodates exclusion windows to prevent backups from running during peak usage periods. Smart scheduling automatically retries failed backups.

To enable smart scheduling in your backup plan, follow these steps:

  1. Set a target RPO that defines the maximum permissible duration of data loss in the event of an incident. The minimum RPO is 60 minutes and the maximum is 60 days.
  2. Optional: Add exclusion windows. Specify time intervals when backups shouldn't run.



For instructions to create a backup plan with smart scheduling, see [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create).

#### Backup exclusion window

You can configure exclusion windows to prevent backups from running during specific time periods. Backup jobs are scheduled to start and finish outside the window duration as much as possible, but ongoing jobs won't be canceled if an exclusion window begins when jobs are in progress. You can configure an exclusion window as a single occurrence, daily, or weekly. You can configure multiple single occurrence windows but only one daily or weekly recurring window.

For example, if you don't want backups from 5:00 PM to 6:00 PM every day, you can set a daily exclusion window with a start time of 5:00 PM and one hour duration.

For instructions to configure backup exclusion window to smart scheduling, see [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create).

### Cron scheduling

Cron scheduling automatically creates backups according to a time schedule you define using the standard [cron](https://en.wikipedia.org/wiki/Cron) syntax. For example, `10 3 * * *` creates a backup at 3:10 AM every day. The minimum interval between scheduled backups is 10 minutes. The cron scheduler doesn't automatically retry backups in case of failure.

For instructions to create a backup plan with cron scheduling, see [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create).

### Comparison between smart scheduling and cron scheduling

The following table summarizes the comparison between smart scheduling and cron scheduling methods.

**Feature** | **Smart scheduling** | **Cron scheduling**  
---|---|---  
Input | Target RPO and backup exclusion window. | Cron syntax  
RPO management  
| Backup for GKE makes its best effort to meet the RPO. | User is responsible for configuring a schedule that meets their RPO.  
Exclusion window support | Yes | No  
Automatic retry on backup failure | Yes | No  
**Note:** Scheduled backups are skipped during cluster upgrades and other maintenance activities, such as control plane IP address rotation.

## RPO risk level

Every backup plan, regardless of its backup scheduling method, has a dynamically calculated RPO risk level after it has at least four successful backups. If a backup plan violates RPO, or is at risk of violating it in the near future, then the RPO is at risk for the plan.

The RPO risk level is calculated from the backup creation scheduling configuration and the backup history of the backup plan. There are five risk levels: `None`, `Low`, `Medium`, `High`, and `Critical`. Each backup plan also has an RPO risk message that explains why the backup plan is at a particular risk level and provides advice for reducing risks.

The following table describes each RPO risk level.

**RPO risk level** | **Description**  
---|---  
None | Meeting RPO with no risk.  
Low | Meeting RPO but with a very mild risk of not meeting RPO soon. No immediate action is required. Continue to monitor the status.  
Medium | Meeting RPO but with some risk of not meeting RPO soon. Action is required.  
High | Meeting RPO but with more than one risks of not meeting RPO soon. Action is required.  
Critical | Violating RPO. Immediate action is required.  
  
Backup plans with the same risk level may have different RPO risk messages depending on the scheduling configuration and historical backup data points. For example, the message for a medium risk level plan can be: Recent backups are taking longer. If this trend continues, there is a risk the RPO will no longer be met.

## Automatic backup deletion

You can configure retention policy in a backup plan to automatically delete backups after a period of time. The retention policy is required for backup plans that include automatic backup creation. You can configure automatic backup deletion using the parameter `backup_retain_days` in the backup plan retention policy. The maximum retain time is 365 days.

When configuring a retention policy for a backup plan that uses automatic backup creation methods, consider the following limitations:

  * For backup plans using smart scheduling, the backup retention duration must be less than or equal to 360 times the target RPO.
  * For backup plans using cron scheduling, the backup retention duration must be less than or equal to 360 times the creation interval.



For instructions to create a backup plan with retention policy, see [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#create).

**Note:** Backups in failed state might be deleted earlier than the `backup_retain_days` period.

## What's next

  * Learn more about [Plan a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).
  * Learn more about [Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).
  * Learn more about [Back up your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
