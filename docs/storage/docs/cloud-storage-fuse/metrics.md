---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics/
title: Cloud Storage FUSE metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:00.978670+00:00
---

# Cloud Storage FUSE metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Cloud Storage FUSE metrics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Storage FUSE metrics help you continuously monitor performance, identify potential bottlenecks that can impact throughput and latency, and address issues quickly as they occur. Cloud Storage provides in-depth metrics for Cloud Storage FUSE when you use Cloud Storage FUSE to mount your buckets as file systems. This document provides an overview of these metrics and describes how to collect, export, and analyze metrics data.

## Metrics collection methods

For diagnostic purposes, you can collect metrics in the background when you use Cloud Storage FUSE. Cloud Storage offers two ways for collecting, exporting, and analyzing metrics:

  * [**Cloud Monitoring exporter**](https://docs.cloud.google.com/architecture/monitoring-metric-export): metrics are collected and exported directly from Cloud Storage FUSE to Cloud Monitoring. Exported metrics can then be viewed in the Google Cloud console.

  * [**Prometheus port**](https://prometheus.io/): metrics are exported in the Prometheus metrics text-based format at a specified Prometheus port such as `http://Host:prometheus-port/metrics` using the Prometheus open-source monitoring and alerting toolkit. Metrics can then be viewed as an output using a client URL such as `curl http://Host:prometheus-port/metrics`


**Note:** If you're using Google Kubernetes Engine (GKE), metrics are enabled by default starting in GKE version 1.33.0-gke.2248000. For more information, see [Cloud Storage FUSE metrics in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#cloud-storage-fuse-metrics).

## Pricing

Cloud Storage FUSE metrics are charged based on your usage. For more information about pricing, refer to [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing).

## Use the Cloud Monitoring exporter

To use the Cloud Monitoring exporter to export, collect, and analyze your metrics from Cloud Storage FUSE to Cloud Monitoring, you must complete the steps outlined in the following sections.

### Get required roles

To get the permissions that you need to use the Cloud Monitoring exporter, ask your administrator to grant you the [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Before you begin

  1. Enable the [Cloud Monitoring API](https://cloud.google.com/monitoring/api/enable-api#enabling-api-v3).

  2. Enable the Cloud Storage API.

[Go to Cloud Storage API](https://console.cloud.google.com/apis/enableflow?apiid=storage-component.googleapis.com&_ga=2.70110096.1642044780.1726157710-823539626.1726157710)




### Set up the Cloud Monitoring exporter

To set up the Cloud Monitoring exporter to collect, export, and analyze Cloud Storage FUSE metrics, specify an integer value in seconds using the [`metrics:cloud-metrics-export-interval-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#cloud-metrics-export-interval-secs) field using a Cloud Storage FUSE configuration file or the [`--cloud-metrics-export-interval-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#cloud-metrics-export-interval-secs) option using the Cloud Storage FUSE CLI.

### View metrics using the Google Cloud console

To view Cloud Storage FUSE metrics using the Google Cloud console, use the following instructions:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/projectselector/monitoring/metrics-explorer?supportedpurview=project,folder,organizationId)

  2. Select the project you want to view metrics for.

  3. From the **Metric** drop-down menu, click **Select a metric**.

  4. Select the resource type:

     * For Compute Engine VMs, select **VM Instance** > **Custom metrics**.
     * For GKE pods, select **Kubernetes Pod** > **Gcsfusecsi**.

Enter the name of the metric you want to view.

To see which metrics Cloud Storage offers for Cloud Storage FUSE, see [Available metrics](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics#available-metrics).




## Use Prometheus to export, collect, and analyze metrics

The following sections describe how to configure and use Prometheus to export, collect, and analyze Cloud Storage FUSE metrics.

### Configure Prometheus

To configure Prometheus, follow the instructions in [Configuring Prometheus for the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus#oagent-config-json-exporter.).

### Use Prometheus

  1. Specify the HTTP port you want to export metrics to using either the [`prometheus-port`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#prometheus-port) field in a Cloud Storage FUSE configuration file or [`--prometheus-port`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#prometheus-port) `gcsfuse` option using the `gcsfuse` CLI.

  2. Validate the Prometheus metrics endpoint using the following command:
         
         curl https://localhost:8080/metrics

If successful, the command returns an output which contains text similar to the following:
         
         # HELP file_cache_read_bytes_count The cumulative number of bytes read from file cache along with read type - Sequential/Random
         # TYPE file_cache_read_bytes_count counter
         file_cache_read_bytes_count{read_type="Random"} 0
         file_cache_read_bytes_count{read_type="Sequential"} 80
         # HELP file_cache_read_count Specifies the number of read requests made via file cache along with type - Sequential/Random and cache hit - true/false
         # TYPE file_cache_read_count counter
         file_cache_read_count{cache_hit="false",read_type="Random"} 215
         file_cache_read_count{cache_hit="false",read_type="Sequential"} 5
         # HELP file_cache_read_latencies The cumulative distribution of the file cache read latencies along with cache hit - true/false
         # TYPE file_cache_read_latencies histogram
         file_cache_read_latencies_bucket{cache_hit="false",le="1"} 215
         file_cache_read_latencies_bucket{cache_hit="false",le="2"} 216
         file_cache_read_latencies_bucket{cache_hit="false",le="3"} 216
         file_cache_read_latencies_bucket{cache_hit="false",le="4"} 216
         file_cache_read_latencies_bucket{cache_hit="false",le="5"} 216
         ...
         file_cache_read_latencies_sum{cache_hit="false"} 483.62783500000023
         file_cache_read_latencies_count{cache_hit="false"} 220
         # HELP fs_ops_count The cumulative number of ops processed by the file system.
         # TYPE fs_ops_count counter
         fs_ops_count{fs_op="FlushFile"} 9
         fs_ops_count{fs_op="GetInodeAttributes"} 91
         fs_ops_count{fs_op="LookUpInode"} 584
         fs_ops_count{fs_op="OpenDir"} 122
         fs_ops_count{fs_op="OpenFile"} 9
         fs_ops_count{fs_op="ReadDir"} 184
         fs_ops_count{fs_op="ReadFile"} 220
         fs_ops_count{fs_op="ReleaseDirHandle"} 122
         fs_ops_count{fs_op="ReleaseFileHandle"} 9
         fs_ops_count{fs_op="StatFS"} 10
         # HELP fs_ops_error_count The cumulative number of errors generated by file system operations
         # TYPE fs_ops_error_count counter
         fs_ops_error_count{fs_error_category="NOT_IMPLEMENTED",fs_op="GetXattr"} 1
         fs_ops_error_count{fs_error_category="NOT_IMPLEMENTED",fs_op="ListXattr"} 1
         fs_ops_error_count{fs_error_category="INTERRUPT_ERROR",fs_op="LookUpInode"} 58
         fs_ops_error_count{fs_error_category="NO_FILE_OR_DIR",fs_op="LookUpInode"} 6
         # HELP fs_ops_latency The cumulative distribution of file system operation latencies
         # TYPE fs_ops_latency histogram
         fs_ops_latency_bucket{fs_op="FlushFile",le="1"} 9
         fs_ops_latency_bucket{fs_op="FlushFile",le="2"} 9
         fs_ops_latency_bucket{fs_op="FlushFile",le="3"} 9
         fs_ops_latency_bucket{fs_op="FlushFile",le="4"} 9
         fs_ops_latency_bucket{fs_op="FlushFile",le="5"} 9
         ...
         fs_ops_latency_sum{fs_op="FlushFile"} 0.28800000000000003
         fs_ops_latency_count{fs_op="FlushFile"} 9
         # HELP gcs_download_bytes_count The cumulative number of bytes downloaded from Cloud Storage along with type - Sequential/Random
         # TYPE gcs_download_bytes_count counter
         gcs_download_bytes_count{read_type="Sequential"} 2.0971528e+08
         # HELP gcs_read_count Specifies the number of Cloud Storage reads made along with type - Sequential/Random
         # TYPE gcs_read_count counter
         gcs_read_count{read_type="Sequential"} 5




## Available metrics

Cloud Storage FUSE provides the following metrics.

### File system metrics

File system metrics provide insight into the operations performed on the mounted bucket such as latency and error rates.

Metric name | Metric description  
---|---  
`fs/ops_count` | The number of operations processed by the file system. This metric allows grouping by `op_type` to get counts for individual operations.  
`fs/ops_error_count` | The number of errors generated by file system operations. This metric can be grouped by `op_type` and `error_category`. Each error is mapped to an `error_category` in a many-to-one relationship.  
`fs/ops_latency` | The cumulative distribution of file system operation latencies. This metric can be grouped by `op_type`.  
  
### Cloud Storage metrics

Cloud Storage metrics provide insight into the interactions between Cloud Storage FUSE and Cloud Storage.

Metric name | Metric description  
---|---  
`gcs/download_bytes_count` | The number of bytes downloaded from Cloud Storage along with the read type. The read type specifies sequential, random, or parallel reads.  
`gcs/read_bytes_count` | The number of bytes read from Cloud Storage objects, which is different from `download_bytes_count`. For example, more data is fetched from Cloud Storage than is actually used by the application.  
`gcs/read_count` | The number of reads from Cloud Storage and read type, either sequential, random, or parallel.  
`gcs/reader_count` | The number of Cloud Storage object readers that are opened or closed. This metric's data is grouped by the input/output (I/O) method type such as `opened` or `closed`.  
`gcs/request_count` | The number of processed Cloud Storage requests.  
`gcs/request_latencies` | The total distribution of Cloud Storage request latencies.  
`gcs/retry_count` | The number of retry requests made to Cloud Storage. This metric can be grouped by `retry_error_category` that specifies the category of the error that triggered a retry.  
  
### File cache metrics

File cache metrics provide insight into the performance and behavior of Cloud Storage FUSE file caching operations.

Metric name | Metric description  
---|---  
`file_cache/read_bytes_count` | The number of bytes read from the file cache and the read type, either sequential or random.  
`file_cache/read_latencies` | The total distribution of the file cache read latencies and the cache hit, either true or false.  
`file_cache/read_count` | The number of read requests made using the file cache, the type of request such as sequential or random, and the cache hit, either true or false.  
  
## What's next

  * Learn how you can [improve Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

  * Forward your [Cloud Storage FUSE logs to Cloud Logging](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/forward-cloud-storage-fuse-logs-to-cloud-logging).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
