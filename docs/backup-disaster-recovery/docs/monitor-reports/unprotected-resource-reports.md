---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-reports/
title: Unprotected resource reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:08.417933+00:00
---

# Unprotected resource reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Unprotected resource reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to view prebuilt unprotected resource reports in BigQuery.

The Backup and DR provides prebuilt unprotected resource reports that are accessible in BigQuery. You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink.

The unprotected resource reports provide information about unprotected resources across backup/recovery appliances.

  * **Appliance ID** : The ID of the appliance on which the resource is discovered.
  * **Last updated on** : The timestamp when the unprotected resource information was last updated.
  * **Discovered on** : The date when the resource was first discovered.
  * **Discovered by** : The name of the appliance on which the resource is discovered.
  * **Host ID** : The host ID associated with the resource.
  * **Host name** : The hostname associated with the resource.
  * **Instance name** : The name of the database instance. If the resource is not of the database type, it shows N/A.
  * **Resource ID** : The ID of the resource.
  * **Resource name** : The name of the resource.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
