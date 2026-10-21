---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics/
title: Collect and view control plane metrics \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:13.481536+00:00
---

# Collect and view control plane metrics  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Collect and view control plane metrics Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to configure a Google Kubernetes Engine (GKE) cluster to send metrics emitted by the Kubernetes API server, Scheduler, and Controller Manager to Cloud Monitoring using Google Cloud Managed Service for Prometheus. This page also describes how these metrics are formatted when they are written to Monitoring, and how to query metrics.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements

Sending metrics emitted by Kubernetes control plane components to Cloud Monitoring has the following requirements:

  * The cluster must have [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) enabled.



## Configure collection of control plane metrics

You can enable control plane metrics in an existing GKE cluster using the Google Cloud console, the gcloud CLI or Terraform.

### Console

You can enable control plane metrics for a cluster either from the **Observability** tab for the cluster or from **Details** tab for the cluster. When you use the **Observability** tab, you can preview the available charts and metrics before you enable the metric package.

To enable control plane metrics from the **Observability** tab for the cluster, do the following:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page: 

[Go to **Kubernetes clusters**](https://console.cloud.google.com/kubernetes/list)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

  2. Click your cluster's name and then select the **Observability** tab.

  3. Select **Control Plane** from the list of features.

  4. Click **Enable package**.

If the control plane metrics are already enabled, then you see a set of charts for control plane metrics instead.




To enable control plane metrics from the **Details** tab for the cluster, do the following:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page: 

[Go to **Kubernetes clusters**](https://console.cloud.google.com/kubernetes/list)

If you use the search bar to find this page, then select the result whose subheading is **Kubernetes Engine**.

  2. Click your cluster's name.

  3. In the **Features** row labelled **Cloud Monitoring** , click the **Edit** icon.

  4. In the **Edit Cloud Monitoring** dialog that appears, confirm that **Enable Cloud Monitoring** is selected.

  5. In the **Components** drop-down menu, select the control plane components from which you would like to collect metrics: **API Server** , **Scheduler** , or **Controller Manager**.

  6. Click **OK**.

  7. Click **Save Changes**.




### gcloud

Update your cluster to collect metrics emitted by the Kubernetes API server, Scheduler, and Controller Manager:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        --monitoring=SYSTEM,API_SERVER,SCHEDULER,CONTROLLER_MANAGER
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the cluster.



### Terraform

To configure the collection of Kubernetes control plane metrics by using Terraform, see the `monitoring_config` block in the [ Terraform registry for `google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#monitoring_config). For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Quota

Control plane metrics consume the "Time series ingestion requests per minute" quota of the Cloud Monitoring API. Before enabling the metrics packages, [check your recent peak usage](https://console.cloud.google.com/iam-admin/quotas) of that quota. If you have many clusters in the same project or are already approaching that quota limit, you can [request a quota limit increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota) before enabling either observability package.

## Pricing

GKE control plane metrics use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to load metrics into Cloud Monitoring. Cloud Monitoring charges for the ingestion of these metrics are based on the number of samples ingested.

For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

## Metric format

All Kubernetes Kubernetes control plane metrics written to Cloud Monitoring use the resource type [ `prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target). Each metric name is prefixed with `prometheus.googleapis.com/` and has a suffix indicating the Prometheus metric type, such as `/gauge`, `/histogram`, or `/counter`. Otherwise, each metric name is identical to the metric name exposed by open source Kubernetes.

## Exporting from Cloud Monitoring

The Kubernetes control plane metrics can be exported from Cloud Monitoring by using the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3). Because all Kubernetes control plane metrics are ingested by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), Kubernetes control plane metrics can be queried [by using Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql). They can also be queried by using [by using Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql).

## Querying metrics

When you query Kubernetes control plane metrics, the name you use depends on whether you are using PromQL or Cloud Monitoring-based features like MQL or the Metrics Explorer [ menu-driven interface](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#menu-driven-interface).

The following tables of Kubernetes control plane metrics show two versions of each metric name: 

  * **PromQL metric name** : When [using PromQL](https://docs.cloud.google.com/monitoring/promql) in Cloud Monitoring pages of the Google Cloud console or in PromQL fields of the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3), use the PromQL metric name. 
  * **Cloud Monitoring metric name** When using other Cloud Monitoring features, use the Cloud Monitoring metric name in the tables below. This name must be prefixed with `prometheus.googleapis.com/`, which has been omitted from the entries in the table. 



## API server metrics

This section provides a list of the API server metrics and additional information about interpreting and using the metrics.

### List of API server metrics

When API server metrics are enabled, all metrics shown in the following table are exported to Cloud Monitoring in the same project as the GKE cluster.

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

PromQL metric name Launch stage  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
Labels  
`apiserver_admission_controller_admission_duration_seconds` GA  
`apiserver_admission_controller_admission_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.23.6+  |  _Admission controller latency histogram in seconds, identified by name and broken out for each operation and API resource and type (validate or admit)._  
  
`name`   
`operation`   
`rejected`   
`type`  
`apiserver_admission_step_admission_duration_seconds` GA  
`apiserver_admission_step_admission_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.22.13+  |  _Admission sub-step latency histogram in seconds, broken out for each operation and API resource and step type (validate or admit)._  
  
`operation`   
`rejected`   
`type`  
`apiserver_admission_webhook_admission_duration_seconds` GA  
`apiserver_admission_webhook_admission_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.22.13+  |  _Admission webhook latency histogram in seconds, identified by name and broken out for each operation and API resource and type (validate or admit)._  
  
`name`   
`operation`   
`rejected`   
`type`  
`apiserver_current_inflight_requests` GA  
`apiserver_current_inflight_requests/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Maximal number of currently used inflight request limit of this apiserver per request kind in last second._  
  
`request_kind`  
`apiserver_flowcontrol_current_executing_seats` BETA  
`apiserver_flowcontrol_current_executing_seats/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.28.3+  |  _Concurrency (number of seats) occupied by the currently executing (initial stage for a WATCH, any stage otherwise) requests in the API Priority and Fairness subsystem._  
  
`flow_schema`   
`priority_level`  
`apiserver_flowcontrol_current_inqueue_requests` BETA  
`apiserver_flowcontrol_current_inqueue_requests/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.28.3+ (1.25.16-gke.1360000+, 1.26.11+, 1.27.8+ for prior minor versions)  |  _Number of requests currently pending in queues of the API Priority and Fairness subsystem._  
  
`flow_schema`   
`priority_level`  
`apiserver_flowcontrol_nominal_limit_seats` BETA  
`apiserver_flowcontrol_nominal_limit_seats/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.28.3+ (1.26.11+, 1.27.8+ for prior minor versions)  |  _Nominal number of execution seats configured for each priority level._  
  
`priority_level`  
`apiserver_flowcontrol_priority_level_seat_utilization` BETA  
`apiserver_flowcontrol_priority_level_seat_utilization/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.37.0-gke.3503000+  |  _Observations, at the end of every nanosecond, of utilization of seats for any stage of execution (but only initial stage for WATCHes)._  
  
`phase` (a constant label with value `executing`)   
`priority_level`  
`apiserver_flowcontrol_rejected_requests_total` BETA  
`apiserver_flowcontrol_rejected_requests_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.28.3+ (1.25.16-gke.1360000+, 1.26.11+, 1.27.8+ for prior minor versions)  |  _Number of requests rejected by the API Priority and Fairness subsystem._  
  
`flow_schema`   
`priority_level`   
`reason`  
`apiserver_flowcontrol_request_wait_duration_seconds` BETA  
`apiserver_flowcontrol_request_wait_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.28.3+ (1.25.16-gke.1360000+, 1.26.11+, 1.27.8+ for prior minor versions)  |  _Length of time a request spent waiting in its queue._  
  
`execute`   
`flow_schema`   
`priority_level`  
`apiserver_longrunning_requests` GA  
`apiserver_longrunning_requests/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.37.0-gke.3503000+  |  _Gauge of all active long-running apiserver requests broken out by`verb`, `group`, `version`, `resource`, `scope` and `component`. Not all requests are tracked this way._  
  
`component`   
`group`   
`resource`   
`scope`   
`subresource`   
`verb`   
`version`  
`apiserver_request_duration_seconds` GA  
`apiserver_request_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.23.6+  |  _Response latency distribution in seconds for each verb, dry run value, group, version, resource, subresource, scope and component._  
  
`component`   
`dry_run`   
`group`   
`resource`   
`scope`   
`subresource`   
`verb`   
`version`  
`apiserver_request_total` GA  
`apiserver_request_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Counter of apiserver requests broken out for each verb, dry run value, group, version, resource, scope, component, and HTTP response code._  
  
`code`   
`component`   
`dry_run`   
`group`   
`resource`   
`scope`   
`subresource`   
`verb`   
`version`  
`apiserver_response_sizes` GA  
`apiserver_response_sizes/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.22.13+  |  _Response size distribution in bytes for each group, version, verb, resource, subresource, scope and component._  
  
`component`   
`group`   
`resource`   
`scope`   
`subresource`   
`verb`   
`version`  
`apiserver_storage_events_received_total` BETA  
`apiserver_storage_events_received_total/counter`  
`Cumulative`, `Int64`, `1`   
**prometheus_target**   
1.36.0-gke.1759000+  |  _Number of etcd events received split by kind._  
  
`group`   
`resource`  
`apiserver_storage_objects` GA  
`apiserver_storage_objects/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Number of stored objects at the time of last check split by kind._  
  
`resource`  
`apiserver_storage_size_bytes` GA  
`apiserver_storage_size_bytes/gauge`  
`Gauge`, `Int64`, `By`   
**prometheus_target**   
1.36.0-gke.1759000+  |  _Size of the storage database file physically allocated in bytes._  
  
`storage_cluster_id`  
`apiserver_watch_events_sizes` BETA  
`apiserver_watch_events_sizes/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.37.0-gke.3503000+  |  _Watch event size distribution in bytes._  
  
`group`   
`resource`   
`version`  
`apiserver_watch_events_total` BETA  
`apiserver_watch_events_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.37.0-gke.3503000+  |  _Number of events sent in watch clients._  
  
`group`   
`resource`   
`version`  
`apiserver_watch_list_duration_seconds` BETA  
`apiserver_watch_list_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `s`   
**prometheus_target**   
1.36.0-gke.1759000+  |  _Response latency distribution in seconds for watch list requuests broken by group, version, resource, and scope._  
  
`group`   
`resource`   
`scope`   
`version`  
  
This following sections provide additional information about the API server metrics.

#### `apiserver_request_duration_seconds`

Use this metric to monitor latency in the API server. The request duration recorded by this metric includes all phases of request processing, from the time the request is received to the time the server completes its response to the client. Specifically, it includes time spent on the following:

  * The authentication and authorization of the request.
  * Calling the third-party and system webhooks associated with the request.
  * Fetching the requested object from an in-memory cache (for requests specifying a `resourceVersion` URL parameter) or from the etcd- or Spanner-based cluster state database by calling the `etcd` API (for all other requests).
  * You can use the `group`, `version`, `resource`, and `subresource` labels to uniquely identify a slow request for further investigation.
  * Writing the response to the client and receiving the client's response.



For more information about using this metric, see Latency.

This metric has very high cardinality. When using this metric, you must use filters or grouping to find specific sources of latency.

#### `apiserver_admission_controller_admission_duration_seconds`

This metric measures the latency in _built-in_ admission webhooks, not third-party webhooks. To diagnose latency issues with third-party webooks, use the `apiserver_admission_webhook_admission_duration_seconds` metric.

#### `apiserver_admission_webhook_admission_duration_seconds` and  
`apiserver_admission_step_admission_duration_seconds`

These metrics measure the latency in external, third-party admission webhooks. The `apiserver_admission_webhook_admission_duration_seconds` metric is generally the more useful metric. For more information about using this metric, see Latency.

#### `apiserver_request_total`

Use this metric to monitor the request traffic at your API server. You can also use it to determine the success and failure rates of your requests. For more information about using this metric, see Traffic and error rate.

This metric has very high cardinality. When using this metric, you must use filters or grouping to identify sources of errors.

#### `apiserver_storage_objects `

Use this metric to detect saturation of your system and to identify possible resource leaks. For more information, see Saturation.

#### `apiserver_current_inflight_requests`

This metric records the maximum number of requests that were being actively served in the last one-second window. For more information, see Saturation.

The metric does not include long-running requests like "watch".

### Monitoring the API server

The API server metrics can give you insight into the main signals for system health:

  * **Latency**: How long does it take to service a request?
  * **Traffic**: How much demand is the system experiencing?
  * **Error rate**: How often to requests fail?
  * **Saturation**: How full is the system?



This section describes how to use the API server metrics to monitor the health of your API server.

#### Latency

When the API server is overloaded, request latency increases. To measure the latency of requests to the API server, use the `apiserver_request_duration_seconds` metric. To identify the source of latency more specifically, you can group metrics by the `verb` or `resource` label.

The suggested upper bound for a single-resource call such as GET, POST, or PATCH is one second. The suggested upper bound for both namespace-scoped and cluster-scoped LIST calls is 30 seconds. The upper-bound expectations are set by SLOs that are defined by the open source Kubernetes community. For more information, see [API call latency SLIs/SLOs details](https://github.com/kubernetes/community/blob/master/sig-scalability/slos/api_call_latency.md).

If the value of the `apiserver_request_duration_seconds` metric is increasing beyond the expected duration, investigate the following possible causes:

  * The Kubernetes control plane might be overloaded. To check, look at the `apiserver_request_total` and `apiserver_storage_objects` metrics. 
    * Use the `code` label to determine whether requests are being processed successfully. For information about the possible values, see [HTTP Status codes](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#http-status-codes).
    * Use the `group`, `version`, `resource`, and `subresource` labels to uniquely identify a request.
  * A third-party admission webhook is slow or non-responsive. If the value of the `apiserver_admission_webhook_admission_duration_seconds` metric is increasing, then some of your third-party or user-defined admission webhooks are slow or non-responsive. Latency in admission webhook can cause delays in job scheduling.

    * To query the 99th percentile webhook latency per instance of the Kubernetes control plane, use the following PromQL query:
          
          sum by (instance) (histogram_quantile(0.99, rate(apiserver_admission_webhook_admission_duration_seconds_bucket{cluster="CLUSTER_NAME"}[1m])))
          

We recommend also looking at the 50th, 90th, 95th, and 99.9th percentiles; you can adjust this query by modifying the `0.99` value.

    * External webhooks have a timeout limit of approximately 10 seconds. You can set alerting policies on the `apiserver_admission_webhook_admission_duration_seconds` metric to alert you when you are approaching the webhook timeout.

    * You can also group the `apiserver_admission_webhook_admission_duration_seconds` metric on the `name` label to diagnose possible issues with specific webhooks.

  * You are listing a lot of objects. It is expected that the latency of LIST calls increases as the number of objects of a given type (the response size) increases.

  * Client-side problems:

    * The client might not have enough resources to receive responses in a timely manner. To check, look at CPU usage metrics for the client pod.
    * The client has a slow network connection. This might happen when the client is running on a device like a mobile phone, but it's unlikely for clients running on a Compute Engine network.
    * The client has exited unexpectedly but the TCP connection has a timeout period in tens of seconds. Before the connection times out, the server's resources are blocked, which can increase latency.



For more information, see [Good practices for using API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/#good-practices-for-using-api-priority-and-fairness) in the Kubernetes documentation.

#### Traffic and error rate

To measure the traffic and the number of successful and failed requests at the API server, use the `apiserver_request_total` metric. For example, to measure the API server traffic per instance of the Kubernetes control plane, use the following PromQL query:
    
    
    sum by (instance) (increase(apiserver_request_total{cluster="CLUSTER_NAME"}[1m]))
    

  * To query the unsuccessful requests, filter the `code` label for 4xx and 5xx values by using the following PromQL query:
        
        sum(rate(apiserver_request_total{code=~"[45].."}[5m]))
        

  * To query the successful requests, filter the `code` label for 2xx values by using the following PromQL query:
        
        sum(rate(apiserver_request_total{code=~"2.."}[5m]))
        

  * To query the rejected requests by the API server per instance of the Kubernetes control plane, filter the `code` label for the value 429 (`http.StatusTooManyRequests`) by using the following PromQL query:
        
        sum by (instance) (increase(apiserver_request_total{cluster="CLUSTER_NAME", code="429"}[1m]))
        




#### Saturation

You can measure the saturation in your system by using the `apiserver_current_inflight_requests` and `apiserver_storage_objects ` metrics.

If the value of the `apiserver_storage_objects ` metric is increasing, you might be experiencing a problem with a custom controller that creates objects but doesn't delete them. You can filter or group the metric by the `resource` label to identify the resource experiencing/ the increase.

Evaluate the `apiserver_current_inflight_requests` metric in accordance with your API Priority and Fairness settings; these settings affect how requests are prioritized, so you can't draw conclusions from the metric values alone. For more information, see [API Priority and Fairness](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/).

## Scheduler metrics

This section provides a list of the scheduler metrics and additional information about interpreting and using the metrics.

### List of scheduler metrics

When scheduler metrics are enabled, all metrics shown in the following table are exported to Cloud Monitoring in the same project as the GKE cluster.

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

PromQL metric name Launch stage  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
Labels  
`kube_pod_resource_limit` GA  
`kube_pod_resource_limit/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.31.1-gke.1621000+  |  _Resource limit for workloads on the cluster, broken down by pod. This shows the resource usage the scheduler and kubelet expect per pod for resource, along with the unit of the resource, if any._  
  
`namespace`   
`node`   
`pod`   
`priority`   
`resource`   
`scheduler`   
`unit`  
`kube_pod_resource_request` GA  
`kube_pod_resource_request/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.31.1-gke.1621000+  |  _Resources requested by workloads on the cluster, broken down by pod. This shows the resource usage the scheduler and kubelet expect per pod for resource, along with the unit of the resource, if any._  
  
`namespace`   
`node`   
`pod`   
`priority`   
`resource`   
`scheduler`   
`unit`  
`scheduler_pending_pods` GA  
`scheduler_pending_pods/gauge`  
`Gauge`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Number of pending pods, by the queue type. 'active' means number of pods in activeQ; 'backoff' means number of pods in backoffQ; 'unschedulable' means number of pods in unschedulablePods._  
  
`queue`  
`scheduler_pod_scheduling_duration_seconds` DEPRECATED  
`scheduler_pod_scheduling_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.25.1 to 1.29 (1.22.17-gke.3100+, 1.23.11+, and 1.24.5+ for prior minor versions)  |  _[Deprecated in v. 1.29; removed in v. 1.30 and replaced by`scheduler_pod_scheduling_sli_duration_seconds`.] E2e latency for a pod being scheduled which may include multiple scheduling attempts._  
  
`attempts`  
`scheduler_pod_scheduling_sli_duration_seconds` BETA  
`scheduler_pod_scheduling_sli_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.30+  |  _E2e latency for a pod being scheduled, from the time the pod enters the scheduling queue, and might involve multiple scheduling attempts._  
  
`attempts`  
`scheduler_preemption_attempts_total` GA  
`scheduler_preemption_attempts_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Total preemption attempts in the cluster till now_  
`scheduler_preemption_victims` GA  
`scheduler_preemption_victims/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.22.13+  |  _Number of selected preemption victims_  
`scheduler_scheduling_attempt_duration_seconds` GA  
`scheduler_scheduling_attempt_duration_seconds/histogram`  
`Cumulative`, `Distribution`, `1`   
**prometheus_target**   
1.23.6+  |  _Scheduling attempt latency in seconds (scheduling algorithm + binding)._  
  
`profile`   
`result`  
`scheduler_schedule_attempts_total` GA  
`scheduler_schedule_attempts_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.22.13+  |  _Number of attempts to schedule pods, by the result. 'unschedulable' means a pod could not be scheduled, while 'error' means an internal scheduler problem._  
  
`profile`   
`result`  
  
This following sections provide additional information about the API server metrics.

#### `scheduler_pending_pods`

You can use the `scheduler_pending_pods` metric to monitor the load on your scheduler. Increasing values in this metric can indicate resourcing problems. The scheduler has three queues, and this metric reports the number of pending requests by queue. The following queues are supported:

  * `active` queue 
    * The set of pods that the scheduler is attempting to schedule; the pod with the highest priority is at the head of the queue.
  * `backoff` queue 
    * The set of pods were unschedulable the last time the scheduler tried but which might be schedulable the next time.
    * Pods on this queue must wait for a backoff period (a maximum of 10 seconds), after which they are moved back to the `active` queue for another scheduling attempt. For more information on the management of the `backoff` queue, see the implementation request, [Kubernetes issue 75417](https://github.com/kubernetes/kubernetes/issues/75419).
  * `unschedulable` set

    * The set of pods that the scheduler attempted to schedule but which have been determined to be unschedulable. Placement on this queue might indicate readiness or compatibility issues with your nodes or the configuration of your node selectors.

When resource constraints prevent pods from being scheduled, the pods are not subject to back-off handling. Instead, when a cluster is full, new pods fail to be scheduled and are put on the `unscheduled` queue.

    * The presence of unscheduled pods might indicate that you have insufficient resources or that you have a node-configuration problem. Pods are moved to either the `backoff` or `active` queue after events that change the cluster state. Pods on this queue indicate that nothing has changed in the cluster that would make the pods schedulable.

    * [Affinities](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) define rules for how pods are assigned to nodes. The use of affinity or anti-affinity rules can be a reason for an increase in unscheduled pods.

    * Some events, for example, PVC/Service ADD/UPDATE, termination of a pod, or the registration of new nodes, move some or all unscheduled pods to either the `backoff` or `active` queue. For more information, see [Kubernetes issue 81214](https://github.com/kubernetes/kubernetes/issues/81214).




For more information, see Scheduler latency and Resource issues.

#### `scheduler_scheduling_attempt_duration_seconds`

This metric measures the duration of a single scheduling attempt within the scheduler itself and is broken down by the result: scheduled, unschedulable, or error. The duration runs from the time the scheduler picks up a pod until the time the scheduler locates a node and places the pod on the node, determines that the pod is unschedulable, or encounters an error. The scheduling duration includes the time in the scheduling process as well as the binding time. Binding is the process in which the scheduler communicates its node assignment to the API server. For more information, see Scheduler latency.

This metric doesn't capture the time the pod spends in admission control or validation.

For more information about scheduling, see [Scheduling a Pod](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-scheduling/scheduling_code_hierarchy_overview.md#scheduling-a-pod).

#### `scheduler_schedule_attempts_total`

This metric measures the number of scheduling attempts; each attempt to schedule a pod increases the value. You can use this metric to determine if the scheduler is available: if the value is increasing, then the scheduler is operational. You can use the `result` label to determine the success; pods are either `scheduled` or `unschedulable`.

This metric correlates strongly with the `scheduler_pending_pods` metric: when there are many pending pods, you can expect to see many attempts to schedule the pods. For more information, see Resource issues.

This metric doesn't increase if the scheduler has no pods to schedule, which can be the case if you have a custom secondary scheduler.

#### `scheduler_preemption_attempts_total` and `scheduler_preemptions_victims`

You can use preemption metrics to help determine if you need to add resources.

You might have higher-priority pods that can't be scheduled because there is no room for them. In this case, the scheduler frees up resources by preempting one or more running pods on a node. The `scheduler_preemption_attempts_total` metric tracks the number of times the scheduler has tried to preempt pods.

The `scheduler_preemptions_victims` metric counts the pods selected for preemption.

The number of preemption attempts correlates strongly with the value of the `scheduler_schedule_attempts_total` metric when the value of the `result` label is `unschedulable`. The two values aren't equivalent: for example, if a cluster has 0 nodes, there are no preemption attempts but there might be scheduling attempts that fail.

For more information, see Resource issues.

### Monitoring the scheduler

The scheduler metrics can give you insight into the performance of your scheduler:

  * **Scheduler latency**: Is the scheduler running? How long does it take to schedule pods?
  * **Resource issues**: Are attempts to schedule pods hitting resource constraints?



This section describes how to use the scheduler metric to monitor your scheduler.

#### Scheduler latency

The scheduler's task is to help ensure that your pods run, so you want to know when the scheduler is stuck or running slowly.

  * To verify that the scheduler is running and scheduling pods, use the `scheduler_schedule_attempts_total` metric.
  * When the scheduler is running slowly, investigate the following possible causes:

    * The number of pending pods is increasing. Use the `scheduler_pending_pods` metric to monitor the number of pending pods. The following PromQL query returns the number of pending pods per queue in a cluster:
          
          sum by (queue)
          (delta(scheduler_pending_pods{cluster="CLUSTER_NAME"}[2m]))
          

    * Individual attempts to schedule pods are slow. Use the `scheduler_scheduling_attempt_duration_seconds` metric to monitor the latency of scheduling attempts.

We recommend observing this metric at least at the 50th and 95th percentiles. The following PromQL query retrieves 95th percentile values but can be adjusted:
          
          sum by (instance) (histogram_quantile(0.95, rate(
          scheduler_scheduling_attempt_duration_seconds_bucket{cluster="CLUSTER_NAME"}[5m])))
          




#### Resource issues

The scheduler metrics can also help you assess whether you have sufficient resources. If the value of the `scheduler_preemption_attempts_total` metric is increasing, then check the value of `scheduler_preemption_victims` by using the following PromQL query:
    
    
    scheduler_preemption_victims_sum{cluster="CLUSTER_NAME"}
    

The number of preemption attempts and the number of preemption victims both increase when there are higher priority pods to schedule. The preemption metrics don't tell you whether the high-priority pods that triggered the preemptions were scheduled, so when you see increases in the value of the preemption metrics, you can also monitor the value of the `scheduler_pending_pods` metric. If the number of pending pods is also increasing, then you might not have sufficient resources to handle the higher-priority pods; you might need to scale up the available resources, create new pods with reduced resource claims, or change the node selector.

  * If the number of preemption victims is not increasing, then there are no remaining pods with low priority that can be removed. In this case, consider adding more nodes so the new pods can be allocated.

  * If the number of preemption victims is increasing, then there are higher-priority pods waiting to be scheduled, so the scheduler is preempting some of the running pods. The preemption metrics don't tell you whether the higher priority pods have been scheduled successfully.

To determine if the higher-priority pods are being scheduled, look for decreasing values of the `scheduler_pending_pods` metric. If the value of this metric is increasing, then you might need to add more nodes.




You can expect to see temporary spikes in the values for the `scheduler_pending_pods` metric when workloads are going to be scheduled in your cluster, for example, during events like updates or scalings. If you have sufficient resources in your cluster, these spikes are temporary. If the number of pending pods doesn't go down, do the following:

  * Check that nodes are not cordoned; cordoned nodes don't accept new pods.
  * Check the following scheduling directives, which can be misconfigured and might render a pod unschedulable: 
    * Node affinity and selector.
    * Taints and tolerations.
    * Pod topology-spread constraints.



If pods can't be scheduled because of insufficient resources, then consider freeing up some of the existing nodes or increasing the number of nodes.

## Controller Manager metrics

When controller manager metrics are enabled, all metrics shown in the following table are exported to Cloud Monitoring in the same project as the GKE cluster.

The Cloud Monitoring metric names in this table must be prefixed with `prometheus.googleapis.com/`. That prefix has been omitted from the entries in the table. 

PromQL metric name Launch stage  
Cloud Monitoring metric name  
---  
Kind, Type, Unit   
Monitored resources   
Required GKE version | _Description_  
Labels  
`node_collector_evictions_total` GA  
`node_collector_evictions_total/counter`  
`Cumulative`, `Double`, `1`   
**prometheus_target**   
1.24+  |  _Number of Node evictions that happened since current instance of NodeController started._  
  
`zone`  
  
## What's next

  * [Explore the other available metrics packages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics)
  * [Collect specific Kubernetes metrics that aren't in this package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/collect-specific-prometheus-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
