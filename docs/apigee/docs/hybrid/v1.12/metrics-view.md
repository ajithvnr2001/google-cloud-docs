---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-view/
title: View metrics \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:23:21.958123+00:00
---

# View metrics  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View metrics Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-view.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/metrics-view.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/metrics-view.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/metrics-view.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/metrics-view.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-view.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/metrics-view.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/metrics-view.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/metrics-view.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/metrics-view.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/metrics-view.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/metrics-view.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/metrics-view.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/metrics-view.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/metrics-view.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/metrics-view.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/metrics-view.html)



This topic explains how to view Apigee hybrid metrics in a [Cloud Operations](https://docs.cloud.google.com/monitoring/kubernetes-engine) dashboard.

## About Cloud Operations

For more information about metrics, dashboards, and [Cloud Operations](https://docs.cloud.google.com/monitoring/kubernetes-engine) see:

  * [Metrics Explorer documentation](https://cloud.google.com/monitoring/charts/metrics-explorer)
  * [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts)
  * [Creating charts](https://docs.cloud.google.com/monitoring/charts)



## Enabling hybrid metrics

Before hybrid metrics can be sent to [Cloud Operations](https://docs.cloud.google.com/monitoring/kubernetes-engine), you must first enable metrics collection. See [Configure metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-enable) for this procedure.

**Note:** Metrics for the Apigee ingress gateway is not supported. See [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## About hybrid metric names and labels

When enabled, hybrid automatically populates Cloud Operations metrics. The domain name prefix of the metrics created by hybrid is:
    
    
    apigee.googleapis.com/

For example, the `/proxy/request_count` metric contains the total number of requests received by an API proxy. The metric name in Cloud Operations is therefore:
    
    
    apigee.googleapis.com/proxy/request_count

Cloud Operations lets you [filter](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) and [group](https://docs.cloud.google.com/monitoring/charts/metrics-selector#groupby-option) metrics data based on labels. Some labels are predefined, and others are added explicitly by hybrid. The Available metrics section below lists all of the available hybrid metrics and any labels added specifically for a metric that you can use for filtering and grouping.

## Viewing metrics

The following example shows how to view metrics in Cloud Operations: 

  1. Open the [Monitoring Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in a browser. Alternatively, if you're already in the Cloud Operations console, select **Metrics explorer**.
  2. In **Find resource type and metric** , locate and select the metric you want to examine. Choose a specific metric listed in Available metrics, or search for a metric. 

  3. Select the desired metric.
  4. Apply filters. Filter choices for each metric are listed in Available metrics. 
  5. Cloud Operations displays the chart for the selected metric. 
  6. Click **Save**.



## Creating a dashboard

[Dashboards](https://docs.cloud.google.com/monitoring/dashboards) are one way for you to view and analyze metric data that is important to you. Cloud Operations provides predefined dashboards for the resources and services that you use, and you can also create custom dashboards.

You use a [chart](https://docs.cloud.google.com/monitoring/dashboards) to display an Apigee metric in your custom dashboard. With custom dashboards, you have complete control over the charts that are displayed and their configuration. For more information on creating charts, see [Creating charts](https://docs.cloud.google.com/monitoring/charts).

The following example shows how to create a dashboard in Cloud Operations and then to add charts to view metrics data:

  1. Open the [Monitoring Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in a browser and then select **Dashboards**.
  2. Select **\+ Create Dashboard**.
  3. Give the dashboard a name. For example: **Hybrid Proxy Request Traffic**
  4. Click **Confirm**.
  5. For each chart that you want to add to your dashboard, follow these steps:

     1. In the dashboard, select **Add chart**.
     2. Select the desired metric as described above in Viewing metrics.
     3. Complete the dialog to define your chart.
     4. Click **Save**. Cloud Operations displays data for the selected metric.



## Available metrics

The following tables list metrics for analyzing proxy traffic. For more information about each Apigee metric, see [Google cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-apigee).

### Proxy, target, and server traffic metrics

Open Telemetry collects and processes metrics (as described in [Metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-collection)) for proxy, target, and server traffic.

The following table describes the metrics that the Open Telemetry collector uses.

Metric name | Use  
---|---  
`/proxy/request_count` | Number of requests to the Apigee proxy since the last sample was recorded. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/proxy/response_count` | Number of responses sent by the Apigee API proxy. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/proxy/latencies` | Distribution of latencies, which are calculated from the time the request was received by the Apigee proxy to the time the response was sent from the Apigee proxy to the client. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/proxyv2/request_count` | The total number of API proxy requests received.  
`/proxyv2/response_count` | The total number of API proxy responses received.  
`/proxyv2/latencies_percentile` | Percentile of all API policy responses to a request.  
`/target/request_count` | Number of requests sent to the Apigee target since the last sample was recorded. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/target/response_count` | Number of responses received from the Apigee target since the last sample was recorded. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/target/latencies` | Distribution of latencies, which are calculated from the time the request was sent to the Apigee target to the time the response was received by the Apigee proxy. Time does not include the Apigee API proxy overhead. **Note** : Available for Apigee hybrid v1.12 and higher.  
`/targetv2/request_count` | The total number of requests sent to the proxy's target.  
`/targetv2/response_count` | The total number of responses received from the proxy's target.  
`/server/fault_count` | The total number of faults for the server application. For example, the application could be `apigee-runtime`,` apigee-synchronizer`, or `apigee-udca`. Use the `pod_name` label to filter results by application.   
`/server/nio` | This is a gauge metric that can be filtered by the label `state` to retrieve details for various labels. The values represent different system and I/O operations. Labels such as `accepted`, `accepted_total`, `close_failed`, `close_success`, `conn_pending`, `connected`, `connected_total`, `max_conn`, and `timeouts` are related to socket and connection operations. The remaining labels pertain to other system operations.  
`/server/num_threads` | The number of active non-daemon threads in the server.  
`/server/request_count` | The total number of requests received by the server application. For example, the application could be `apigee-runtime`,` apigee-synchronizer`, or `apigee-udca`. Use the `pod_name` label to filter results by application.  
`/server/response_count` | Total number of responses sent by the server application. For example, the application could be `apigee-runtime`,` apigee-synchronizer`, or `apigee-udca`. Use the `pod_name` label to filter results by application.  
`/server/latencies` | Latency is the latency in millisecs introduced by the server application. For example, the application could be `apigee-runtime`,` apigee-synchronizer`, or `apigee-udca`. Use the `pod_name` label to filter results by application.  
`/upstream/request_count` | The number of requests sent by the server application to its upstream application. For example, for the` apigee-synchronizer`, the control plane is upstream. So `upstream/request_count` for `apigee-synchronizer` is a metric that indicates the requests that `apigee-synchronizer` made to the control plane.  
`/upstream/response_count` | The number of responses received by the server application from its upstream application. For example, for the `apigee-synchronizer`, the control plane is upstream. So `upstream/response_count` for `apigee-synchronizer` is a metric that indicates the requests that `apigee-synchronizer` received from the control plane.  
`/upstream/latencies` | The latency incurred at the upstream server application in milliseconds. For example, for the `apigee-synchronizer`, the control plane is upstream. So `upstream/latencies` for `apigee-synchronizer` is a metric that indicates the latency from the control plane.  
  
### UDCA metrics

Open Telemetry collects and processes metrics (as described in [Metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-collection)) for the UDCA service just as it does for other hybrid services.

The following table describes the metrics that the Open Telemetry collector uses in the UDCA metrics data.

Metric name | Use  
---|---  
`/udca/server/local_file_oldest_ts` | The timestamp, in milliseconds since the start of the Unix Epoch, for the oldest file in the dataset. This is computed every 60 seconds and does not reflect the state in real time. If the UDCA is up to date and there are no files waiting to be uploaded when this metric is computed, then this value will be 0. If this value keeps increasing, then old files are still on disk.  
`/udca/server/local_file_latest_ts` | The timestamp, in milliseconds since the start of the Unix Epoch, for the latest file on disk by state. This is computed every 60 seconds and does not reflect the state in real time. If the UDCA is up to date and there are no files waiting to be uploaded when this metric is computed, then this value will be 0.  
`/udca/server/local_file_count` | A count of the number of files on disk in the data collection pod. Ideally, the value will be close to 0. A consistent high value indicates that files are not being uploaded or that the UDCA is not able to upload them fast enough. This value is computed every 60 seconds and does not reflect the state of the UDCA in real time.  
`/udca/server/total_latencies` | The time interval, in seconds, between the data file being created and the data file being successfully uploaded. Buckets will be 100ms, 250ms, 500ms, 1s, 2s, 4s, 8s, 16s, 32s, and 64s. Histogram for total latency from file creation time to successful upload time.  
`/udca/server/upload_latencies` | The total time, in seconds, that UDCA spent uploading a data file. Buckets will be 100ms, 250ms, 500ms, 1s, 2s, 4s, 8s, 16s, 32s, and 64s. The metrics will display a histogram for total upload latency, including all upstream calls.  
`/udca/upstream/http_error_count` | The total count of HTTP errors that UDCA encountered. This metric is useful to help determine which part of the UDCA external dependencies are failing and for what reason. These errors can arise for various services (`getDataLocation`, `Cloud storage`, `Token generator`) and for various datasets (such as `api` and `trace`) with various response codes.  
`/udca/upstream/http_latencies` | The upstream latency of services, in seconds. Buckets will be 100ms, 250ms, 500ms, 1s, 2s, 4s, 8s, 16s, 32s, and 64s. Histogram for latency from upstream services.  
`/udca/upstream/uploaded_file_sizes` | The size of the file being uploaded to the Apigee services, in bytes. Buckets will be 1KB, 10KB, 100KB, 1MB, 10MB, 100MB, and 1GB. Histogram for file size by dataset, organization and environment.  
`/udca/upstream/uploaded_file_count` | A count of the files that UDCA uploaded to the Apigee services. Note that: 

  * The **`event`** dataset value should keep growing. 
  * The **`api`** dataset value should keep growing if org/env has constant traffic. 
  * The **`trace`** dataset value should increase when you use the Apigee trace tools to debug or inspect your requests.

  
`/udca/disk/used_bytes` | The space occupied by the data files on the data collection pod's disk, in bytes. An increase in this value over time: 

  * **`ready_to_upload`** implies the agent is lagging behind. 
  * **`failed`** implies files are piling up on disk and not being uploaded. This value is computed every 60 seconds.

  
`/udca/server/pruned_file_count` | Count of files which have been deleted because their Time To Life (TTL) was beyond a set threshold. The dataset can include API, trace, and others, and state can be `UPLOADED`, `FAILED`, or `DISCARDED`.   
`/udca/server/retry_cache_size` | A count of the number of files, by dataset, that UDCA is retrying to upload. After 3 retries for each file, UDCA moves the file to the **`/failed`** subdirectory and removes it from this cache. An increase in this value over time implies that the cache is not being cleared, which happens when files are moved to the **`/failed`** subdirectory after 3 retries.  
  
### Cassandra metrics

Open Telemetry collects and processes metrics (as described in [Metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/metrics-collection)) for Cassandra just as it does for other hybrid services.

The following table describes the metrics that the Open Telemetry collector uses in the Cassandra metrics data.

Metric name (excluding domain) | Use  
---|---  
`/cassandra/process_max_fds` | Maximum number of open file descriptors.  
`/cassandra/process_open_fds` | Open file descriptors.  
`/cassandra/jvm_memory_pool_bytes_max` | JVM maximum memory usage for the pool.  
`/cassandra/jvm_memory_pool_bytes_init` | JVM initial memory usage for the pool.  
`/cassandra/jvm_memory_bytes_max` | JVM heap maximum memory usage.  
`/cassandra/process_cpu_seconds_total` | User and system CPU time spent in seconds.  
`/cassandra/jvm_memory_bytes_used` | JVM heap memory usage.  
`/cassandra/compaction_pendingtasks` | Outstanding compactions for Cassandra sstables. See [Compaction](https://cassandra.apache.org/doc/latest/operating/compaction/) for more.  
`/cassandra/jvm_memory_bytes_init` | JVM heap initial memory usage.  
`/cassandra/jvm_memory_pool_bytes_used` | JVM pool memory usage.  
`/cassandra/jvm_memory_pool_bytes_committed` | JVM pool committed memory usage.  
`/cassandra/clientrequest_latency` | Read request latency in the 75th percentile range in microseconds.  
`/cassandra/jvm_memory_bytes_committed` | JVM heap committed memory usage.  
  
####  Working with Cassandra metrics 

Apigee recommends the following metrics as critical to monitor for your Cassandra database: 

  * **Cassandra request rate** : Use this metric to monitor the cassandra read and write request rate. Metric: | `apigee.googleapis.com/cassandra/clientrequest_latency`  
---|---  
Resource labels: | `project_id`, `location`, `cluster_name`, `namespace_name`, `pod_name`, `container_name`  
Metric labels: | `scope`, `unit` Use these labels to filter the specific resource or for grouping.   
  
To monitor cassandra read request rate, apply the following filter. 

Filters: | `metric.scope == 'Read'`  
`metric.unit == 'OneMinuteRate'`  
---|---  
  
To monitor cassandra write request rate, apply the following filter. 

Filters: | `metric.scope == 'Write'`  
`metric.unit == 'OneMinuteRate'`  
---|---  
  * **Cassandra request latency** : Use this metric to monitor the cassandra read and write request latency. This is the same metric as the request rate, `apigee.googleapis.com/cassandra/clientrequest_latency` with different filters applied. 

To monitor cassandra read request latency, apply the following filter. 

Filters: | `metric.scope == 'Read'`  
`metric.unit == '99thPercentile'` or `'95thPercentile'` or `'75thPercentile'`  
---|---  
  
To monitor cassandra write request latency, apply the following filter. 

Filters: | `metric.scope == 'Write'`  
`metric.unit == '99thPercentile'` or `'95thPercentile'` or `'75thPercentile'`  
---|---  
  * **Cassandra pod CPU request utilization** **Note:** Cassandra pod CPU request metrics are only available in GKE.Metric: | `kubernetes.io/container/cpu/request_utilization (GKE on Google Cloud)`  
For more information, see [Kubernetes metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes).  `kubernetes.io/anthos/container/cpu/request_utilization (Google Distributed Cloud)`  
---|---  
Resource labels: | `project_id`, `location`, `cluster_name`, `namespace_name`, `pod_name`, `container_name` Use these labels to filter the specific resource or for grouping.   
  * **Cassandra data volume utilization** **Note:** Cassandra data volume utilization metrics are only available in GKE. Metric: | `kubernetes.io/pod/volume/utilization (GKE on Google Cloud)`  
For more information, see [Kubernetes metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes).  `kubernetes.io/anthos/pod/volume/utilization (Google Distributed Cloud)`  
---|---  
Resource labels: | `project_id`, `location`, `cluster_name`, `namespace_name`, `pod_name`  
Metric labels: | `volume_name` Use these labels to filter the specific resource or for grouping.   



####  Recommendations for scaling the Cassandra cluster 

The following guidelines can serve as a recommended cluster for the decision to scale your Cassandra cluster. In general, if read or write requests consistently show 99th percentile latency or the latency is trending upwards continuously, and you see corresponding spikes in CPU request utilization spike and the read or write request rates, your Cassandra cluster can be considered to be under stress. You may want to consider scaling up the cluster. For more information see [Scaling Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-scaling)

Metric| Threshold| Trigger duration  
---|---|---  
`kubernetes.io/pod/volume/utilization`| 85%| 5min  
`kubernetes.io/container/cpu/request_utilization`| 85%| 3min  
`Read request Latency 99thPercentile`| 5s| 3min  
`Write request Latency 99thPercentile`| 5s| 3min  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
