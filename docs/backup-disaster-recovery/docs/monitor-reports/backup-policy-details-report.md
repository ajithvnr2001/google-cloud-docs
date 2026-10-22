---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-report/
title: Backup policy details reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:49.175403+00:00
---

# Backup policy details reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup policy details reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

## Backup Policy Details report

This page explains how to view prebuilt backup policy details reports in BigQuery.

The Backup and DR provides prebuilt backup policy details reports that are accessible in BigQuery. You can access these reports after you execute the prebuilt script in the same dataset where the logs are being routed through the log sink. For more information, see [backup policy details logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-logs).

  * **Last_Updated_On** : The timestamp when the backup policy details information was last updated.
  * **Backup_Template** : The type of resource, for example, a Compute Engine instance.
  * **Backup_Policy_Name** : The name of the template that the backup policy is part of.
  * **Backup_Policy_Type** : The type of the backup policy. This can take two values: "Local Replication" or "Remote Replication"
  * **Backup_Schedule_Type** : Backup Schedule Type. It can be WINDOWED or CONTINUOUS.
  * **Backup_Window_Start_Time** : Backup Window Start time in HH:MM format. This field is applicable only for windowed schedule types. It is "N/A" by default for continuous backup schedules.
  * **Backup_Window_End_Time** : Backup Window End time in HH:MM format. This field is applicable only for windowed schedule types. It is "23:59" by default for continuous backup schedules.
  * **Backup_Frequency_In_Days** : The configured schedule frequency in days for the backup policy.
  * **Backup_Consistency** : This represents the kind of backup configured for the policy. Possible values are "Crash consistent backup", "Take application consistent backup" or "Crash consistent backup on last try". These are detailed in [Configure advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).
  * **Log_Backup_Frequency_In_Minutes** : The frequency at which database logs are backed up in minutes. This field is applicable only for database type applications, otherwise it is reported as 0 by default.
  * **Backup_Retention_Period_In_Days** : Retention period of backups in days. This field is in decimal format and shows up to 2 decimal places.
  * **Protected_Resources_Count** : Count of resources protected with the given template.
  * **Schedule_Disabled_Resources_Count** : Count of resources protected with the given template but with the schedule in disabled state.
  * **Appliance_Name** : The name of the appliance associated with the backup policy.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
