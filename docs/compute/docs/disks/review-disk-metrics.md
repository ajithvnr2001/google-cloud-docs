---
url: https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics/
title: Review disk performance metrics \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:04.893590+00:00
---

# Review disk performance metrics  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Review disk performance metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can use disk metrics to observe your disks' performance and debug performance problems. This page lists the metrics available for Google Cloud Hyperdisk and Persistent Disk volumes.

Disk metrics can help you answer questions such as the following:

  * What's the average read IOPS for a virtual machine (VM) instance's disks?
  * On average, what's the latency for read or write operations?
  * What's the average [queue depth](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#io-queue-depth) for a specific disk?



Review your disk's metrics to ensure its performance is sufficient for your workload. In addition, you should also do the following:

  * Review the disk optimization guidelines. For more information, see [Optimize Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk) and [Optimize Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).

  * Check the disk's health. For detailed information about disk health, see [Monitor disk health](https://docs.cloud.google.com/compute/docs/disks/disk-health).




This document discusses the disk metrics Compute Engine automatically collects from each VM and how to view them in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), which is Google Cloud's monitoring solution.

## Available disk metrics

You can view metrics in Cloud Monitoring, or programmatically retrieve metrics using the [REST API](https://docs.cloud.google.com/monitoring/api), [client libraries](https://docs.cloud.google.com/monitoring/docs/reference/libraries), and [Promethus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql).

The following table lists the disk-specific metrics available for every disk. You can collect additional metrics if you install the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) on your VM.

For a full list of Compute Engine metrics, see [Compute Engine metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

Each metric type in this table must be prefixed with `compute.googleapis.com/`, which has been omitted from the table for readability.

Display name  
`(Metric type)` | Description  
---|---  
**Disk performance status**   
`(instance/disk/performance_status)` | The disk's health over the last minute. This metric indicates if the disk is performing normally or if its performance is affected by an incident within Compute Engine. Possible values are `Healthy`, `Degraded`, and `Severely Degraded`.  
For more information, see [ Monitor a disk's health](https://docs.cloud.google.com/compute/docs/disks/disk-health).   
**Average I/O latency**   
`(instance/disk/average_io_latency)` | The disk's average read/write latency, in microseconds, for the last minute.  
**Average I/O queue depth**   
`(instance/disk/average_io_queue_depth)` | The disk's average queue depth for read/write operations over the last minute.  
**Disk read bytes**   
`(instance/disk/read_bytes_count)` | Average read throughput, or, the average number of bytes read or written over a period of time specified by the user*.   
**Disk write bytes**  
`(instance/disk/write_bytes_count)` | Average write throughput, or, the average number of bytes written over a period of time specified by the user*.   
**Disk read operations**  
`(instance/disk/read_ops_count)` | The average number of read operations over a period of time specified by the user*.   
**Disk write operations**  
`(instance/disk/write_ops_count)` | The average number of write operations over a period of time specified by the user*.   
**Peak disk read bytes**   
`(instance/disk/max_read_bytes_count)` | Peak read throughput, the maximum number of bytes read per second over a period of time specified by the user*.   
**Peak disk write bytes**   
`(instance/disk/max_write_bytes_count)` | Peak write throughput, the maximum number of bytes written per second over a period of time specified by the user*.   
**Peak disk read ops**   
`(instance/disk/max_read_ops_count)` | The maximum number of read operations per second over a period of time specified by the user*.   
**Peak disk write ops**   
`(instance/disk/max_write_ops_count)` | The maximum number of write operations per second over a period of time specified by the user*.   
  
* The period must be one minute or longer. 

## Visualize disk performance on a chart

You can visualize your disk's performance by plotting any of the metrics listed in the preceding section with Metrics Explorer. Metrics Explorer is part of Cloud Monitoring.

### Example: Visualize average latency for the disks attached to a VM

To visualize the average latency for a VM's disks on a chart, follow these instructions. You can follow the same procedure for the other metrics. 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `VM Instance` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **VM Instance**.
     2. In the **Active metric categories** menu, select **Instance**.
     3. In the **Active metrics** menu, select **Disk average latency**. 
     4. Click **Apply**.
The fully qualified name for this metric is `compute.googleapis.com/instance/disk/average_io_latency`. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. To display only the metrics for each disk attached to a specific instance, follow these steps: 
     * In the **Filter** element, click **Add filter** , and then select **instance_name**. For the value, select a specific instance name.
     * In the **Aggregation** entry, set the first menu to **Mean** and the second menu to **device_name**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




## What's next

  * Learn how to [optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).
  * Learn more about [creating charts with Metric Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * Learn more about [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
  * Enable the [Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api).
  * View all the [available metrics for Compute Engine](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
