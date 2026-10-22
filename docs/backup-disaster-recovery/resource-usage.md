---
url: https://docs.cloud.google.com/backup-disaster-recovery/resource-usage/
title: Backup and DR quotas and limits overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:34.941589+00:00
---

# Backup and DR quotas and limits overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/resource-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Backup and DR quotas and limits overview Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas that apply to Backup and DR. Backup and DR quotas define the number of resources that your project has access to. Backup and DR enforces allocation and rate quotas on resource usage for various reasons. For example, quotas help to protect the community of Google Cloud users by preventing unforeseen spikes in usage.

Not all projects have the same quotas. As your use of Google Cloud increases, your quotas might increase accordingly. If you anticipate a significant increase in usage, you can proactively request quota adjustments from the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

## Cloud Quotas

Cloud Quotas help you do the following:

  * Monitor your consumption of Google Cloud products and services
  * Restrict your consumption of those resources
  * Request changes to the quota value and automate quota adjustments



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

## Backup and DR quotas

Backup and DR quotas are of two types:

  * Resource quotas: quotas that restrict usage of Backup and DR resources, such as backup vaults, backup plans, backup plan associations, data sources, and backups.
  * API quotas: quotas that restrict how often you can call the Backup and DR restore API.



Backup and DR resource quotas are enforced at the following levels:

  * Per Google Cloud project. Most quotas are enforced on the administrator project, some are enforced on the workload project.
  * Per project per region
  * [Per backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)



Backup and DR resource quotas are available for both regional and multi-regional backups. Quotas can be monitored and managed from the Cloud Quotas dashboard. You can [configure quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts) to be notified when your quota usage is approaching the limit.

### Storage quotas

Storage quotas apply to the amount of data stored in your backup vaults. The following table lists the default storage quotas for Backup and DR resources, including the resource type, metric name, description, and default quota.

Resource type | Metric name | Description | Default quota  
---|---|---|---  
Backup vaults used | `backupdr.googleapis.com/backupvaults` | The number of backup vaults, enforced per project per region. | 50  
Backup plans used | `backupdr.googleapis.com/backupplans` | The number of backup plans, enforced per project per region. | 20  
Backup plan associations used | `backupdr.googleapis.com/backupplanassociations` | The number of backup plan associations, enforced per project per region. | 200  
Backups for Compute Engine instances | `backupdr.googleapis.com/gce_backups_per_vault` | The number of backups for a Compute Engine instance. | 50,000  
Active vaulted Compute Engine instance resources per vault | `backupdr.googleapis.com/gce_active_datasources_per_vault` | The number of active vaulted Compute Engine instances per backup vault. | 500  
Backups for disk instances | `backupdr.googleapis.com/disk_backups_per_vault` | The number of backups for a disk instance. | 50,000  
Active vaulted Compute Engine disk per vault | `backupdr.googleapis.com/disk_active_datasources_per_vault` | The number of active vaulted disk instances per backup vault. | 500  
Backups for Filestore instances | `backupdr.googleapis.com/filestore_backups_per_vault` | The number of backups for Filestore. | 50,000  
Active vaulted Filestore instances per vault | `backupdr.googleapis.com/filestore_active_datasources_per_vault` | The number of active vaulted Filestore instances per backup vault. | 500  
Backups for Cloud SQL instances | `backupdr.googleapis.com/cloud_sql_backups_per_vault` | The number of backups for a Cloud SQL instance. | 50,000  
Active vaulted Cloud SQL data sources per vault | `backupdr.googleapis.com/cloud_sql_active_datasources_per_vault` | The number of active vaulted Cloud SQL data sources per backup vault. | 200  
  
### API request quotas

The following table lists the default quotas for Backup and DR API requests, including the API method, default quota, and notes.

API method | Default quota | Notes  
---|---|---  
API requests | 1,200 requests per minute, per project | Applies to standard Backup and DR API requests.  
Restore backup API requests | 10 requests per minute, per project | Applies to calls to the Backup and DR restore backup API method.  
Passthrough API requests | 3,600 requests per minute, per project | Applies to requests to Backup and DR passthrough API methods.  
  
To view or request changes to your project's quotas, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## Monitor resource usage

To help you to monitor and manage your Backup and DR resources, Google Cloud provides the following tools:

  * Cloud Monitoring: Provides visibility into the usage, performance, and overall health of Backup and DR resources. See [Monitor Backup and DR resources](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics).

  * Cloud Logging: Captures detailed logs related to storage utilization and protected resources, aiding in auditing and troubleshooting. See [Storage resource usage logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/storage-utilization-logs).

  * BigQuery Reports: Offers pre-built reports for in-depth analysis of storage resource utilization. For more information, see [Storage Resource Utilization reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-reports-bigquery).




For more information on monitoring and reporting, see [Backup and DR reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview).

## Set up alerts on quotas

You can [set up alerts on quotas](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts). If you need more quota than you have access to, [submit a quota adjustment request](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * Read about [Backup and DR pricing](https://cloud.google.com/backupdr/pricing).
  * Learn how to [view and manage quota](https://docs.cloud.google.com/docs/quotas/view-manage).
  * Learn how to [set up quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
