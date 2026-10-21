---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-view/
title: View metrics \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:20:24.327722+00:00
---

# View metrics  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View metrics Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

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

Before hybrid metrics can be sent to [Cloud Operations](https://docs.cloud.google.com/monitoring/kubernetes-engine), you must first enable metrics collection. See [Configure metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-enable) for this procedure.

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

Open Telemetry collects and processes metrics (as described in [Metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection)) for proxy, target, and server traffic.

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
`/server/fault_count` | The total number of faults for the server application. For example, the application could be `apigee-runtime` or `apigee-synchronizer`. Use the `pod_name` label to filter results by application.   
`/server/nio` | This is a gauge metric that can be filtered by the label `state` to retrieve details for various labels. The values represent different system and I/O operations. Labels such as `accepted`, `accepted_total`, `close_failed`, `close_success`, `conn_pending`, `connected`, `connected_total`, `max_conn`, and `timeouts` are related to socket and connection operations. The remaining labels pertain to other system operations.  
`/server/num_threads` | The number of active non-daemon threads in the server.  
`/server/request_count` | The total number of requests received by the server application. For example, the application could be `apigee-runtime` or `apigee-synchronizer`. Use the `pod_name` label to filter results by application.  
`/server/response_count` | Total number of responses sent by the server application. For example, the application could be `apigee-runtime` or `apigee-synchronizer`. Use the `pod_name` label to filter results by application.  
`/server/latencies` | Latency is the latency in millisecs introduced by the server application. For example, the application could be `apigee-runtime` or `apigee-synchronizer`. Use the `pod_name` label to filter results by application.  
`/upstream/request_count` | The number of requests sent by the server application to its upstream application. For example, for the` apigee-synchronizer`, the control plane is upstream. So `upstream/request_count` for `apigee-synchronizer` is a metric that indicates the requests that `apigee-synchronizer` made to the control plane.  
`/upstream/response_count` | The number of responses received by the server application from its upstream application. For example, for the `apigee-synchronizer`, the control plane is upstream. So `upstream/response_count` for `apigee-synchronizer` is a metric that indicates the requests that `apigee-synchronizer` received from the control plane.  
`/upstream/latencies` | The latency incurred at the upstream server application in milliseconds. For example, for the `apigee-synchronizer`, the control plane is upstream. So `upstream/latencies` for `apigee-synchronizer` is a metric that indicates the latency from the control plane.  
  
### Cassandra metrics

Open Telemetry collects and processes metrics (as described in [Metrics collection](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection)) for Cassandra just as it does for other hybrid services.

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

The following guidelines can serve as a recommended cluster for the decision to scale your Cassandra cluster. In general, if read or write requests consistently show 99th percentile latency or the latency is trending upwards continuously, and you see corresponding spikes in CPU request utilization spike and the read or write request rates, your Cassandra cluster can be considered to be under stress. You may want to consider scaling up the cluster. For more information see [Scaling Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-scaling)

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
