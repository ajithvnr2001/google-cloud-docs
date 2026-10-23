---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery/
title: Daily schedule compliance reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:58.625397+00:00
---

# Daily schedule compliance reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Daily schedule compliance reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page provides an overview of prebuilt Daily Schedule Compliance in BigQuery.

The Backup and DR provides prebuilt Daily Schedule Compliance reports that are accessible in BigQuery. You can access these reports after [executing the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink. These reports display the data for the last seven days by default.

The Daily Schedule Compliance report provides information about the compliance status of daily schedule backup policies for your resources.

  * **Resource name** : The name of the resource associated with the daily schedule backup policy.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, or a database.
  * **Backup rule policy name** : The backup policy name that the compliance has reporting for.
  * **Backup plan policy template** : The name of the template that the daily schedule backup policy is part of.
  * **Date** : The date that the compliance status is reported on.
  * **Backup window start time** : The start time of the daily schedule backup policy window.
  * **Job type** : The daily schedule backup policy job type. It can be snapshot, OnVault, streamsnap, restore, or direct to OnVault.
  * **Status** : The compliance status of the daily schedule backup policy. The status can be success, failure, unknown, or blank.
  * **Comment** : A description explaining the compliance status of the daily schedule backup policy.
  * **Appliance name** : The name of the appliance associated with the daily schedule backup policy.
  * **Hostname** : The hostname associated with the daily d backup policy.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
