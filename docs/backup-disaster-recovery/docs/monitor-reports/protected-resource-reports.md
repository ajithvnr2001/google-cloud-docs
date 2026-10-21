---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-reports/
title: Protected resource reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:07.563904+00:00
---

# Protected resource reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protected resource reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to view prebuilt protected resource reports in BigQuery.

Backup and DR provides prebuilt protected resource reports that are accessible in BigQuery. You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink.

The protected resource logs provide information about the number of applications and virtual machines (VMs) protected in an appliance.

  * **Last updated on** : The timestamp when the protected resource information was last updated.
  * **Resource name** : The name of the resource.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.
  * **Hostname** : The hostname associated with the resource.
  * **Backup plan policy template** : The name of the backup template used to protect the application.
  * **Protected on** : The date when the resource was protected.
  * **Recovery point** : The timestamp when the last successful backup was taken.
  * **Protected data** : The size of the protected data.
  * **OnVault data** : The size of data protected using OnVault pool.
  * **Backup plan restrictions** : The restrictions applied to a backup plan. The restrictions can be `scheduler disabled`, `expiration disabled`, `snapshots disabled`, `streamsnap disabled`, `OnVault disabled`, or `process latest snapshot`.
  * **Backup inclusion or exclusion** : The volumes or databases that are included or excluded for virtual machines or database instances.
  * **Policy overrides** : The policy overrides that are set at the backup template level.
  * **Appliance name** : The name of the appliance associated with the resource.
  * **Remote appliance** : The remote appliance where the backup is replicated.
  * **Source appliance** : The source appliance where the backup is taken.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#custom-queries)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
