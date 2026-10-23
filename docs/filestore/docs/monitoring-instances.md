---
url: https://docs.cloud.google.com/filestore/docs/monitoring-instances/
title: Monitoring instances and quota \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:26.153976+00:00
---

# Monitoring instances and quota  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/monitoring-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Monitoring instances and quota Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to monitor your Filestore instances and set up alerts for low disk space and low backups quota.

You can monitor Filestore instances using [Cloud Monitoring](https://docs.cloud.google.com/monitoring).

## Before you begin

Before you begin, make sure you have access to the following roles:

  * Monitoring Viewer
  * Monitoring Editor



To see how to grant access to these roles, see [Grant access to Cloud Monitoring](https://docs.cloud.google.com/monitoring/access-control#grant-monitoring-access).

## Add a Filestore metric chart to a Cloud Monitoring dashboard

To see Filestore performance metrics in a Cloud Monitoring dashboard, follow these steps:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Select a metric** expandable section.
  3. In the **Filter by resource or metric name** field, type `filestore` and select the **Filestore Instance** expandable section.
  4. Select an available metric to view:

Metric | Description | Basic tiers | Regional, zonal, and enterprise tiers  
---|---|---|---  
**Average read latency** | The average time a read operation takes (in milliseconds). |  | ✓  
**Average write latency** | The average time a write operation takes (in milliseconds). |  | ✓  
**Bytes written** | Number of bytes written. | ✓ | ✓  
**Bytes read** | Number of bytes read from persistent storage. This can be less than the number of bytes read by clients, as some reads might be served from a memory cache. * | ✓ | ✓  
**Disk read operation count** | Number of disk read operations. If the Filestore instance caches the data, some read operations are not reflected as disk reads. * | ✓ | ✓  
**Disk write operation count** | Number of disk write operations. If the Filestore instance caches the data, some write operations are not reflected as disk writes. * | ✓ | ✓  
**Metadata operations count** | Number of disk metadata operations. |  | ✓  
**Free bytes** | Number of free disk bytes. | ✓ | ✓  
**Free disk space percent** | Percentage of free disk bytes. | ✓ | ✓  
**Free raw capacity percent** | Free raw capacity as a percentage of total space. |  | ✓  
**Procedure call count** | Returns the same information as the [nfsstat -s](https://linux.die.net/man/8/nfsstat) command. | ✓ |   
**Snapshots used bytes** | The amount of space used for storing snapshots, measured in bytes. |  | ✓  
**Time (in milliseconds) spent on read operations** | Time spent on disk reads. | ✓ |   
**Time (in milliseconds) spent on write operations** | Time spent on disk writes. | ✓ |   
**Used bytes** | Number of used disk bytes. | ✓ | ✓  
**Used space percent** | Percentage of used disk bytes. | ✓ | ✓  
  
*Memory-cached operations only occur in basic tier instances.

  1. Optional configurations:

Field | Description  
---|---  
[**Filter**](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) | Filter to the Filestore instances that you want to monitor.  
[**Group by**](https://docs.cloud.google.com/monitoring/charts/metrics-selector#groupby-option) | Combining data from similar time series.  
[**Aggregator**](https://docs.cloud.google.com/monitoring/charts/metrics-selector#groupby-option) | Combine time series using common functions.  
[**Minimum alignment period**](https://docs.cloud.google.com/monitoring/charts/metrics-selector#alignment) | The time interval for which aggregation takes place.  
  2. If you want to add more metrics to the chart, click **Add another metric**.

  3. Click **Save Chart** to create a dashboard. Alternatively, you can add the chart to an existing dashboard.




## Metric definitions

The following sections describe certain Filestore-specific metrics in detail.

### Free raw capacity percent

The [free raw capacity percent](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-file) metric represents capacity available to users, not necessarily the available raw disk space.

Your instance replicates data to provide durability and to help support performance, resulting in a total storage capacity greater than the user-specified capacity of the instance.

The free raw capacity percent metric represents the percentage of free raw capacity available to users after any replication performed as a function of instance durability or performance.

If this metric reaches 0%, new data cannot be written to the cluster until more free space becomes available.

For more information on how to scale instance capacity up or down, see [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale).

### Snapshots used bytes

The [snapshots used bytes](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-file) metric represents the number of bytes in use by all snapshots, whether internal or external. This metric is allocated and indexed by share, not instance.

### Used bytes

The [used bytes](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-file) metric represents the raw data written by the user. It doesn't take into account the space required for [inodes](https://docs.cloud.google.com/filestore/docs/scale#inode-usage) and metadata.

### Anticipating capacity

For a better understanding of an instance's available capacity, we recommend monitoring the available space as well as the written space.

To see the free space on an instance, use the free raw capacity percent metric.

Each file stored on the file share consumes one inode. If the file system runs out of inodes, you won't be able to store more files on the file share even if you haven't reached the maximum allocated capacity.

To see the number of inodes in use, use the `df` command. For more information, see [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale) and [Troubleshoot capacity issues](https://docs.cloud.google.com/filestore/docs/capacity-issues).

## Set up alerts

###  Low disk space 

To ensure that your Filestore instances don't run out of free space, we recommend setting up low disk space alerts. This guide uses the **free disk space percent** metric to measure the free disc space for basic instances.

If you want to measure low disk space for zonal, regional, or enterprise instances, use the following steps to set up two separate alerts using **free disk space percent** and **free raw capacity percent** metrics.

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create Policy**.
  3. Click the **Select a metric** expandable section.
  4. In the **Filter by resource or metric name** field, type `filestore` and select the **Filestore Instance** expandable section.
  5. Select the **Nfs** active metric category.
  6. Select the metric **Free disk space percent**.
  7. Click **Apply**.
  8. In the **Add filters** section, click **Add a filter**.
  9. Click the **Filter** expandable section and select **instance_name**.
  10. In the **Value** field, enter the Filestore instance name for which you want to receive alerts.
  11. Click **Done**.

For more information about filtering Cloud Monitoring metrics, see [Filtering](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  12. In the **Transform data** section, specify the **Rolling window** and **Rolling window function**. Indicate whether you want to include a secondary data transformation and click **Next**.

  13. In the **Configure alert trigger** window, choose a condition type.

  14. Set the following specifications:

Field | Configuration  
---|---  
**Alert trigger** | **Any time series violates**  
**Threshold position** | **Below threshold**  
**Threshold value** | Enter the lowest acceptable free disk space percentage for each of your Filestore instances.  
  
You can test the alert by setting a low limit and seeing whether the alert gets triggered.

For more information, see [Default create alerting policy flow](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#default).

  15. Enter any advanced options.

  16. In the **Condition name** field, enter a name for the condition.

  17. Click **Next**.

  18. In the **Configure notifications and finalize alert** window, indicate which notification channels you want to use.

For information on how to create new channels, see [Manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  19. In the **Incident autoclose duration** menu, select the duration you want to use.

  20. In the **Policy user labels** section, indicate the labels you want to use.

  21. In the **Documentation** section, add any documentation you want to include such as instructions on how to address the issue.

  22. In the **Alert policy name** field, enter an alert policy name and click **Next**.

  23. Click **Create policy**.




###  Low backups quota 

If you are scheduling or automating backups creation for your Filestore instances, you should set up alerts for when you're running low on backups quota.

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create Policy**.
  3. Click the **Select a metric** expandable section.
  4. In the **Filter by resource or metric name** field, type `quota` and select the **Consumer quota** expandable section.
  5. Select the **Quota** active metric category.
  6. Select the metric **Allocation quota usage**.
  7. Click **Apply**.
  8. In the **Add filters** section, click **Add Filter**.
  9. Click the **Filter** expandable section and select **quota_metric**.
  10. In the **Value** field, enter `file.googleapis.com/backups-per-region`.
  11. Click **Done**.
  12. Optional: To add another filter, click **Add filter** and repeat the process.

For more information about filtering Cloud Monitoring metrics, see [Filtering](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  13. In the **Transform data** section, specify the **Rolling window** and **Rolling window function**. Indicate whether you want to include a secondary data transformation and click **Next**.

  14. In the **Configure alert trigger** window, choose a condition type.

  15. Set the following specifications:

Field | Configuration  
---|---  
**Alert trigger** | **Any time series violates**  
**Threshold position** | **Below threshold**  
**Threshold value** | Enter the lowest acceptable backups quota remaining.  
  
You can test the alert by setting a low limit and seeing whether the alert gets triggered.

For more information, see [Default create alerting policy flow](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#default).

  16. Enter any advanced options.

  17. In the **Condition name** field, enter a name for the condition.

  18. Click **Next**.

  19. In the **Configure notifications and finalize alert** window, indicate which notification channels you want to use.

For information on how to create new channels, see [Manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  20. In the **Incident autoclose duration** menu, select the duration you want to use.

  21. In the **Policy user labels** section, indicate the labels you want to use.

  22. In the **Documentation** section, add any documentation you want to include such as instructions on how to address the issue, for example, "Delete older backups" or "Request additional quota".

  23. In the **Alert policy name** field, enter an alert policy name and click **Next**.

  24. Click **Create policy**.




## What's next

  * [Request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  * [Understand capacity errors](https://docs.cloud.google.com/filestore/docs/known-issues#capacity_errors_before_reaching_full_provisioned_capacity).
  * [Optimize and test instance performance](https://docs.cloud.google.com/filestore/docs/performance).
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
