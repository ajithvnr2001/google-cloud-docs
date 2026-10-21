---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/monitoring-metrics/
title: Backup for GKE monitoring metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:42.780372+00:00
---

# Backup for GKE monitoring metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Backup for GKE monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes the monitoring metrics created by Backup for GKE as part of [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

Cloud Monitoring collects metrics to help you understand the usage of Backup for GKE and how the service is performing. For more information about Cloud Monitoring in general, see [Cloud Monitoring overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

## Required IAM role

The following permissions are required for metrics operations. Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

  * Monitoring Viewer (`roles/monitoring.viewer`) role to view metrics in Cloud Monitoring
  * Monitoring Editor (`roles/monitoring.editor`) role to access metrics dashboard



## Monitored resources

The following types of monitored resources are available for Backup for GKE:

  * [gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)
  * [gkebackup.googleapis.com/RestorePlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/RestorePlan)



## Available metrics and labels

The following metrics are available for Backup for GKE in the Google Cloud console:

The "metric type" strings in this table must be prefixed with `gkebackup.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`backup_completion_times` GA ** _(project)_**   
Backup completion time   
`DELTA`, `DISTRIBUTION`, `s`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Distribution of the backup completion time._   
`state`: State of the backup, one of [SUCCEEDED, FAILED].   
`backup_created_count` GA ** _(project)_**   
Backup created count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Count of the backups created under a backupPlan._   
`scheduled`: Whether the backup was created by schedule, one of [true, false].   
`backup_deleted_count` GA ** _(project)_**   
Backup deleted count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/BackupPlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/BackupPlan)** |  _Count of the backups deleted under a backupPlan._   
`scheduled`: Whether the backup was deleted by schedule, one of [true, false].   
`restore_created_count` GA ** _(project)_**   
Restore created count   
`DELTA`, `INT64`, `1`   
**[gkebackup.googleapis.com/RestorePlan](https://docs.cloud.google.com/monitoring/api/resources#tag_gkebackup.googleapis.com/RestorePlan)** |  _Count of the restores created under a restorePlan._  
  
Table generated at 2026-10-08 15:22:12 UTC.

For more information about monitoring metrics, see [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics#generated).

To view graphs of metric data, use the Metrics Explorer. For information on using this tool, see [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
