---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices/
title: Best practices for hourly Compute Engine instance backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:07.147313+00:00
---

# Best practices for hourly Compute Engine instance backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cloud_best_practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Best practices for hourly Compute Engine instance backups Stay organized with collections  Save and categorize content based on your preferences. 

This document provides best practices for configuring and managing hourly backups for Compute Engine instances. The 1-hour backup frequency is designed for workloads requiring higher data protection granularity. These recommendations help you optimize data protection, manage performance, and set realistic expectations for recovery points. 

## Combine daily and hourly backup rules

It is strongly recommended to include a daily backup rule alongside a 1-hourly frequency rule in your backup plan. This ensures that even if individual hourly backups are skipped or delayed, a consistent daily recovery point is maintained.

## Understand scheduled backup retry logic

Retry behavior varies significantly between Daily and Hourly recurrence types.

Daily Recurrence: If a daily backup job fails to start or complete, it is retried until the end of the configured backup window.

1-Hourly Recurrence: An hourly backup event is retried for 1 hour only, regardless of the length of the overall backup window. This prevents backup jobs from overlapping and causing congestion.

## Manage high data churn

High churn can lead to long-running backups that prevent subsequent hourly jobs from starting. To optimize performance and to reduce impact of concurrent backups within a vault, spread high-frequency backups for VMs experiencing high data churn across multiple backup vaults.

## Monitor and configure alerts for skipped backups

[Configure alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts-vault) for skipped backup jobs for proactive notification of protection gaps.

You can set up alerts using Cloud Logging by monitoring for "Backup Plan Violation" events or specific "skipped backup" log entries from the Backup and DR scheduler.

## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
Backup frequency | Use 1-hour backup frequency judiciously based on workload needs.  
Backup plan | Combine daily and hourly backup rules for consistent recovery points.  
Retry logic | Understand the different retry behaviors for daily and hourly backups.  
Recovery Point Objective | Set realistic RPO expectations that account for churn and performance.  
High data churn | Reduce backup frequency and distribute workloads for high-churn VMs.  
Monitoring | Configure alerts for skipped backup jobs to avoid protection gaps.  
  
## What's next

  * Learn how to [create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).
  * Read about [monitoring backup jobs with Cloud Logging](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
