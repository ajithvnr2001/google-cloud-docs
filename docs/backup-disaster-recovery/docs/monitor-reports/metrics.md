---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics/
title: Backup and DR metrics in Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:47.193531+00:00
---

# Backup and DR metrics in Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and DR metrics in Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details on how to monitor the usage and performance of Backup and DR resources in your Google Cloud project.

Backup and DR uses [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to provide visibility into the usage, performance, and overall health of the resources. You can use Cloud Monitoring to create custom charts and dashboards to visualize the different performance metrics and resource usage of Backup and DR resources. Cloud Monitoring also lets you configure alerts and alert policies for these metrics. You can also set up an alert to check if the total data processed exceeds a specified threshold value. For information about configuring alerts, see [Alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).

You can visualize your Backup and DR metrics and data using the following Cloud Monitoring tools:

  * Sample dashboards
  * Custom dashboards
  * Metrics explorer



## Required IAM role

The following permissions are required for metrics operations. Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

  * Monitoring Viewer (`roles/monitoring.viewer`) role to view metrics in Cloud Monitoring
  * Monitoring Editor (`roles/monitoring.editor`) role to access metrics dashboard and set alerts in Cloud Monitoring



## Available Backup and DR resource metrics

The following metrics are available for Backup and DR in the Google Cloud console.

### Metric for backup vault consumption

In Cloud Monitoring, the [monitored resource type](https://docs.cloud.google.com/monitoring/api/v3/metrics) for the following metrics is the backup vault (`/backupdr.googleapis.com/BackupVault`)

**Metric category** | **Metric name** | **Description** | **Metric type and label**  
---|---|---|---  
Storage | Backup vault storage consumption | Represent the data usage of the backup vault. This value updates hourly and repeats the most recent value every five minutes. | **Metric type:** backupdr.googleapis.com/storage/stored_bytes  
**Metric label** :` `You can use the following labels to filter data for backup vault storage consumption metrics:  


  * backup_schedule_type: Represents if the resource type is protected using a backup plan or backup template.


  * resource_type: Type of resource that you want to see the storage consumption details. This can be a Compute Engine instance, an Oracle database, a Microsoft SQL server, or a Google Cloud VMware Engine.

  
  
### Metrics for the resources protected using backup template

In Cloud Monitoring, the [monitored resource type](https://docs.cloud.google.com/monitoring/api/v3/metrics) for Backup and DR is the appliance management console (`/backupdr.googleapis.com/managementconsole`).

**Metric category** | **Metric name** | **Description** | **Metric type and label**  
---|---|---|---  
Backup_recovery_appliance | Backup/ recovery storage pool utilization | Represents the use of backup/recovery appliance storage pools | **Metric type:** backupdr.googleapis.com/backup_recovery_appliance/storage_pool/utilization  
  
**Metric label** :` `You can use the following labels for backup/recovery appliance storage pool use metrics to filter data:  


  * pool_name: Name of the storage pool. For example, `act_pri_pool000`.


  * pool_usage: Type of usage. It can be free or used.


  * pool_type: Type of storage pool. It can be snapshot or primary.


* backup_recovery_appliance_name: The name of the backup/recovery appliance.  
Backup_recovery_appliance | backup/recovery appliance vDisk utilization | Represents the vDisk pool utilization for a backup/recovery appliance | **Metric type:** backupdr.googleapis.com/backup_recovery_appliance/v_disk_count/utilization  
  
**Metric label** : You can use the following labels for backup/recovery appliance vDisk utilization metrics to filter data:  


  * v_disk_usage: Display the state of the vDisk. It can be free or used.


  * backup_recovery_appliance_name: The name of the backup/recovery appliance.

  
OnVault_pools   
Note: The OnValut pools metric doesn't include backup vault data. | OnVault pool usage  
| Represents the usage of vault pools in GB | **Metric type:** backupdr.googleapis.com/onvault_pools/utilization  
  
**Metric label** : You can use the following labels for OnVault pool usage metrics to filter data:  


  * pool_name: Name of the storage pool. For example, `act_pri_pool000`.


  * backup_recovery_appliance_name: The name of the backup/recovery appliance.

  
Protected_data  
  
Note: This doesn't include data protected for Google Cloud VMware Engine nodes.  | Protected data volume | Represents the size of data protected by resource type | **Metric type:** backupdr.googleapis.com/protected_data/volume  
  
**Metric label** : You can use the following labels for protected data volume metrics to filter data:  


  * resource_type: Type of resource associated with the job. For example, Compute Engine instance, file system, SQL instance, or consistency group.


  * backup_recovery_appliance_name: The name of the backup/recovery appliance.

  
Protected_data  
  
Note: This doesn't include data protected for Google Cloud VMware Engine nodes.  | Protected resources count  
| Represents the number of protected resources by resource type | **Metric type:** backupdr.googleapis.com/protected_data/resources  
  
**Metric label** : You can use the following labels for protected resources count metrics to filter data:  


  * resource_type: Type of resource associated with the job. For example, Compute Engine instance, file system, or SQL instance.

  
Jobs | Job trend  
| Represents backup and recovery job count categorized by job status. | **Metric type:** backupdr.googleapis.com/jobs/job_trend  
  
**Metric label** : You can use the following labels for job trend metrics to filter data:  


  * job_status: Displays the status of a job. It can be successful, canceled, failed, not run, or successfulwithwarnings.


  * job_type: Type of job. For example, snapshot, expiration, or mount.


  * resource_type: Type of resource associated with the job. For example, Compute Engine instance, file system, or Microsoft SQL Server instance.


  * backup_recovery_appliance_name: The name of the backup/recovery appliance.

  
  
## Access metrics using sample dashboards

Backup and DR provides sample dashboards with charts containing metrics relevant to usage, performance, and the overall health of the resources. You can import and install these sample dashboards in Cloud Monitoring to create custom dashboards from.

To install a sample dashboard, do the following:

  1. In the Google Cloud console, go to the **Monitoring** page: 

[Go to Monitoring page](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Dashboards** , and go to the **Sample library** tab.
  3. In **Categories** , select **Backup and DR**.
  4. From the list of samples, select **Backup and DR Monitoring** and click **Import**.
  5. Click **Confirm**.

The dashboard is imported and listed in the **Dashboard list** tab.

After importing the sample dashboard, you can view and edit the Backup and DR metrics in the dashboard. For more information about installing sample dashboards, see [Install sample dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).




## Access metrics using custom dashboards

In your Google Cloud project, you can create custom monitoring dashboards for your Backup and DR resources by doing the following:

  1. In the Google Cloud console, go to the **Cloud Monitoring** > **Dashboard Overview** page: 

[Go to Dashboard Overview page](https://console.cloud.google.com/monitoring/dashboards)

  2. Click **Create dashboard**.
  3. Click **Add widget**.
  4. Optional: Modify the name of the dashboard.
  5. From the **Add widget** menu, select a visualization type.
  6. In the **Configure widget** , do the following: 
     1. From the **Select a metric** menu, choose the metrics that you want to visualize.
     2. Click **Apply**.
  7. Click **Apply**.



For more information about custom dashboards, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

## Access Backup and DR resource metrics using Metrics explorer

The Cloud Monitoring [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) helps you build temporary metric charts to visualize the available resource metrics for your Google Cloud project. Once you have created a metric chart, you can also save it to a custom monitoring dashboard. For more information, see [Select metrics when using Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

To create a chart using the Backup and DR resource metrics, do the following:

  1. In the Google Cloud console, go to the **Cloud Monitoring** > **Metrics explorer** page: 

[Go to Metrics explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Select a metric** pane, expand the **Metric** menu.
  3. Enter `management console` in the filter bar and then use the submenus to select a specific resource type and metric. 
     1. In the **Active metric categories** menu, select **OnVault_pools**.
     2. In the **Active metrics** menu, select an **OnVault pool usage** metric.
     3. Click **Apply**.
  4. Optional: Change the settings in the **Display** pane: 
     1. For quota and other metrics that report one sample per day, set the **Widget type** to **Stacked bar chart**.
     2. For distribution valued metrics, click the **Widget type** menu and select **Heatmap chart**.
  5. Click **Save chart**.
  6. Enter a name for the chart in the **Chart title** field.
  7. Choose a dashboard from an existing dashboard or create a new dashboard.
  8. Click **Save chart**.

You can also select filters, group by metric labels, perform aggregations, and select chart viewing options using the Metrics explorer. For more information, see [Create charts with Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
