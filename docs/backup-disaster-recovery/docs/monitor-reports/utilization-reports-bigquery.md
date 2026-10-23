---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-reports-bigquery/
title: Storage resource utilization reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:02.109358+00:00
---

# Storage resource utilization reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-reports-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Storage resource utilization reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to view prebuilt storage resource utilization reports in BigQuery.

The Backup and DR provides prebuilt storage resource utilization reports that are accessible in BigQuery. You can access these reports after [executing the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink.

The storage resource utilization report provides details about storage utilization of your resources.

  * **Last updated on** : The timestamp when the storage resource information was last updated on.
  * **Appliance name** : The name of the appliance associated with the storage resource.
  * **Pool name** : The name of the pool.
  * **Storage type** : The type of storage pool, for example, perf pool, onVault Pool, or primary pool.
  * **Total capacity** : The total capacity of the storage pool. This isn't applicable for OnVault pools.
  * **Used capacity** : The consumption of the storage pool.
  * **Utilization percentage** : The percentage of vDisk and pool volume consumed. This isn't applicable for the OnVault pool.
  * **Appliance ID** : The ID of the appliance associated with a storage resource.



## What's next

  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#custom-queries)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
