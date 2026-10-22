---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices/
title: Optimize backup plan policy performance and job scheduling in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:18.288704+00:00
---

# Optimize backup plan policy performance and job scheduling in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Optimize backup plan policy performance and job scheduling in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Following these best practices helps you to avoid some of the more common mistakes users make when creating and modifying policy templates in the Backup and DR appliance management console.

  * Initial data capture
  * Resize volumes
  * Concurrency
  * Policy schedules
  * Calculate frequency
  * Database log protection in a backup plan policy
  * Job priority and Scheduling
  * Job retries
  * Variables that impact RPO compliance



You need to configure policy templates according to your recovery point objectives (RPOs) and recovery time objectives (RTOs). Over time you may find it necessary to make changes to those templates.

**Note:** Making changes to existing templates or adding new templates can impact the consumption of system resources as well as the performance of your backup/recovery appliances.

## Initial data backup capture

The first time a policy in a policy template creates a backup of an application's data, it backs up the data in its entirety. Subsequent backups will be incremental.

To protect multiple applications with one policy template, apply the policy template to just a few of the applications. Once the initial full data capture is complete, apply the policy template to more applications. Repeat the process until the policy template has been applied to all applications.

## Resizing volumes

If you resize a volume that contains protected data, for some application types, the next time the snapshot policy for that volume runs and it may perform a full backup operation; regardless of how many times that volume's data has been backed up in the past. These include resized VMware VMDKs and agent based backups of Microsoft Windows applications and Linux applications that are not on LVM.

If you must resize a volume for those affected application types, consider the impact capturing all of the data will have on the applications server(s), network, and the backup/recovery appliance.

## Jobs concurrency

A backup/recovery appliance can by default run six snapshot jobs concurrently. If you have more than the allowed number of jobs scheduled for the same time period, the policy scheduler will start as many jobs as allowed and queue the other jobs.

Because each user's network design, data layout, and storage classes differ, experiment with concurrency until the optimal number of concurrent jobs is reached.

## Policy schedules

The appliance management console supports two methods of specifying a policy schedule when configuring a policy:

  * **Windowed.** Defines a discrete snapshot backup schedule adhering to a specific frequency and time window (for example, perform a backup every 30 minutes, daily from 09:00 to 17:00 UTC). You can instruct the backup/recovery appliance to run multiple backup jobs at a specified frequency interval or once during a specified time window.
  * **Continuous.** Defines a continuous snapshot backup schedule (for example, perform a backup job every eight hours, starting the first job at 01:00 UTC). In this policy schedule, jobs run continuously (24/7) at the specified time interval.



## Frequency calculation

The period is the time between scheduled runs and frequency is the number of jobs run per unit time. For example, if a schedule calls for jobs to run every 4 hours, the period is 4 hours and the expected frequency is 6 times per day. If a job takes one hour to complete and the policy has a 12 hour frequency, then the policy's job will run again 11 hours after the previous job completes.

Be sure to select a frequency that achieves your required Recovery Point Objectives (RPOs) and allows sufficient time for a job to finish.

  * Minimum recommended frequency for a Snapshot policy is 1 hour (local RPO).
  * A StreamSnap policy can point to any Snapshot policy with frequency of 1 hour or longer (remote RPO).



## Database log protection in a backup plan policy

When creating a snapshot policy for a database you have the option of also capturing its log files at a specified frequency. The frequency at which database logs are captured is defined separately from that of the database. For example, a database can be captured every day and its logs captured every hour.

The frequency of database log backup is set in minutes, and the frequency at which logs are captured must not exceed the frequency at which its associated database is captured. For example, if a database capture frequency is every 24 hours, the log file capture frequency must be less than every 24 hours.

Frequency and retention are defined in the advanced settings of the database's snapshot policy. The capture of logs is done without regard to day boundaries, window, or frequency at which its associated database is captured.

You enable the Log Protection feature through the **Enable Database Log Backup** advanced settings in a backup plan snapshot policy. Frequency and retention are also defined in the advanced settings for a backup plan policy.

The physical space required to accommodate a database's logs is automatically managed by the appliance management console. At a minimum, the appliance management console will evaluate typical log sizes and their retention periods and add space as needed.

To enable log backup and to more efficiently and effectively manage the storage requirements for database logs, refer to this table.

Setting | Input  
---|---  
**Truncate or purge log after backup** | Required to set to Yes for purging the production log. To manage log purging, select this. This will run log purge at the end of each log backup. The default is Do Not Truncate.  
| If a policy with **Enable database log backup** is set to **No** , and if **Truncate or purge log after backup** is set to **Yes** , then log purging runs at the end of each database backup, purging all the logs.  
**Log backup retention period** | The log backup under Backup and DR staging disk will be retained to the value set here. Backup log retention can be different from snapshot retention.  
**Log staging disk growth size** | Set a percentage by which to grow the log backup staging disk when needed.  
**Estimated change rate** | Estimate the percentage by which the database data changes daily.  
**Compress database log backup** | Use this to enable database log backup to run in compress mode using the app-level database API.  
**Enable database log backup** | The **Enable Database Log Backup** option allows the backup plan policy to back up a database and all associated log files. The logs are backed up when the log backup job runs. The options are **Yes** or **No**. When set to Yes, the related options are enabled.  
**RPO** | When Enable Database Log Backup is set to Yes, RPO defines the frequency for database log backup. Frequency is set in minutes and must not exceed the database backup interval.  
**Replicate logs** | (Uses StreamSnap technology) When Enable Database Log Backup is set to Enable, the Replicate Logs advanced setting allows database log backups to be replicated to a remote backup/recovery appliance. For a log backup replication job to run, there must be a StreamSnap replication policy included in the template along with a resource profile that specifies a remote backup/recovery appliance, and at least one successful replication of the database must first be completed. You can then use the log backup at the remote site for any database backup within the retention range of the replicated log backup. This function is enabled by default.  
| Log replication uses StreamSnap technology to perform the replication between the local and remote backup/recovery appliances; log replication goes directly from the local snapshot pool to the snapshot pool on the remote appliance.  
| **Note** : Log replication does not occur until the database has been protected and the database backup has been replicated to the remote backup/recovery appliance.  
**Send logs to OnVault Pool** | Set to Yes, logs will get replicated to one or more OnVault storage pools enabling point-in-time recoveries from an OnVault pool on another site.  
  
## Job priority and scheduling

All activities run as jobs. Jobs are executed according to the schedules configured when the policies were created.

Some jobs take much longer than others. Expiration jobs are fast. Snapshot jobs depend upon variables like the size of the application or VM and how much data has changed since its last snapshot; the initial snapshot of any application or VM is all-new data, so those can take a long time.

The policy scheduler identifies when one or more policies applied to applications are to run, and then initiates a job that places the policy into a queue when the scheduled start time occurs. For each policy type there is a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state, which means that even if a job is supposed to start at a particular time it will execute only occur when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the selection of the application to run is randomized to ensure fairness across all of the applications that have the same priority.

## Job retries

When a job fails, the scheduler will automatically retry running the job. The first time the job fails the scheduler will wait 4 minutes before making it available for retry. After 3 failed job attempts the job is marked as Failed and is no longer retried. The next job will be attempted according to the policy's schedule.

The scheduler will treat a job retry like any other available job. If there are more jobs available than slots to accommodate them, then jobs are queued. This may result in a retry failing to start within the window and the job being marked as failed.

Job retries are reported in the **Monitor**. To identify job retries, the **Monitor** appends first a, then b, and finally c to each retry job's name.

## Variables that impact RPO compliance

**Network congestion** : Other activity on the network can slow your data flow. Make sure that you can consistently provide the bandwidth that is used for RPO sizing. This is typically not an issue when running on Google Cloud, but could be relevant when protecting Oracle databases on Bare Metal Solution servers.

**Other running jobs** : If you intend to perform frequent mounting of virtual clones (e.g., for test data management) or expect to frequently have to restore data, take into account the I/O impact of those jobs. Recovery jobs such as mount or restore typically have the highest priority in the system and take away resources from ongoing backup jobs.

**Higher than normal change rate for a workload** : Sometimes users perform actions that can drive dramatically high change rates. Re-indexing a database or performing an ETL operation into a database, for example, can cause massive changes at the block level. Sometimes users move workloads (for example between data centers) and so a full new ingest might be needed. You need to decide up front how much of such change you want to be able to handle while still meeting the RPO. Service providers often exclude SLA compliance if the customer generates changes that are more than some agreed-upon amount.

**Loss of changed block tracking** : Sometimes changed block tracking is lost (e.g., when a server crashes). While the service has mechanisms to deal with that and avoid a full new ingest by scanning the production data and rebuilding the changes, that takes longer than an incremental capture. You need to decide if you want to account for that in the system sizing.

**Distribution of change** : Finally, change is usually not distributed evenly. While the system might be sized to meet the RPO for the average change rate, and in aggregate that meets RPO, this could be violated, especially for larger workloads. You might have days with more activity (on a weekly or monthly, or even annual basis), and even within a day change is often distributed unevenly. If you only size the system to the average change, take into account that you will get violations and account for that in how any RPO Storage SLA between you and your customers (internal or external) is defined and measured.

## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
