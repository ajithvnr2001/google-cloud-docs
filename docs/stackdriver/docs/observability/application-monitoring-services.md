---
url: https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-services/
title: Application Monitoring supported infrastructure \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:27.745373+00:00
---

# Application Monitoring supported infrastructure  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Application Monitoring supported infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

When infrastructure resources integrated with Application Monitoring are registered as an App Hub service or workload, the platform and audit logs, metrics, and traces that they generate include [application-specific labels](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-labels). For a list of services and workloads that are integrated with App Hub, see [App Hub supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources). 

## Golden signals on Application Monitoring dashboards

The dashboards that Application Monitoring creates display log and metric data, including the following golden signals, when that data includes application-specific labels:

  * **Traffic** : Incoming request rates on the service or workload over the selected time period. For some configurations, this chart contains tabs. The **Request** tab displays the networking L7 metric and the **Bytes** tab displays the networking L4 metric.
  * **Server error rate** : Ratio of incoming requests whose response code is equivalent to an 5xx HTTP response code to all incoming requests over the selected time period.
  * **P95 latency** : 95th percentile of latency for a request served over the selected time period, in milliseconds.
  * **Saturation** : Measures how full your service or workload is. For example, for managed instance groups (MIGs), Cloud Run, and Google Kubernetes Engine deployments, this field shows the CPU utilization.



If you explore a dashboard, you might notice that a charted metric for a golden signal differs from the metric you expect. For some golden signals, Google Cloud Observability has a prioritized list of source metrics. If a preferred metric isn't available, then Google Cloud Observability searches the list until it finds an available metric.

## Supported infrastructure resources

The **Notes and limitations** column lists details about which golden signals are supported. This column also lists limitations.

Infrastructure resources | Golden signals | Notes and limitations  
---|---|---  
[AlloyDB for PostgreSQL clusters](https://docs.cloud.google.com/alloydb/docs/overview#clusters)  
(Regional) |  | Application labels aren't attached to spans.  
[AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/alloydb/docs/overview#instances)  
(Regional) | 

  * **Traffic** : [instance/postgres/transaction_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#alloydb/instance/postgres/transaction_count)
  * **Server error rate** : Ratio of the [instance/postgres/abort_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#alloydb/instance/postgres/abort_count) to the total [instance/postgres/transaction_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#alloydb/instance/postgres/transaction_count).
  * **Saturation** : [instance/cpu/average_utilization](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#alloydb/instance/cpu/average_utilization)

| Application labels aren't attached to spans.  
[Bigtable clusters](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#clusters)  
(Regional) | 

  * **Saturation** : [cluster/cpu_load](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#bigtable/cluster/cpu_load)

| Application labels aren't attached to spans.  
[Bigtable instances](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#instances)  
(Regional) |  | Application labels aren't attached to metric data or to spans.  
[Cloud Domains](https://docs.cloud.google.com/domains/docs) |  | Application labels aren't attached to metric data or to spans.  
[Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs)  
(Regional) | 

  * **Saturation** : [container/cpu/utilizations](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#run/container/cpu/utilizations)

|   
[Cloud Run services and functions](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services)  
(Regional) | 

  * **Traffic** : [request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#run/request_count)
  * **Server error rate** : The ratio of the number of requests with a response status of `5xx` to the total number of requests.
  * **P95 latency** : [request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#run/request_latencies)
  * **Saturation** : [container/cpu/utilizations](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#run/container/cpu/utilizations)

| Only trace spans generated by instrumented workloads contain application labels. Only customer-instrumented workloads running within Cloud Run generate golden signals.  
[Cloud Logging log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries)  
(Global and regional) |  | Only audit logs contain application labels.  
[Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/introduction#what_is_a_instance)  
(Regional) | 

  * **Saturation** : [database/cpu/utilization](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/database/cpu/utilization)

| Application labels aren't attached to spans.  
[Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets)  
(Regional and multi-regional) | 

  * **Traffic** : [api/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#storage/api/request_count)
  * **Server error rate** : Ratio of requests with a response status that indicates an error to the total number of requests. The following status values indicate an error: 
    * `DATA_LOSS`
    * `DEADLINE_EXCEEDED`
    * `INTERNAL`
    * `UNAVAILABLE`
    * `UNIMPLEMENTED`
    * `UNKNOWN`

| Application labels aren't attached to spans.  
[Compute Engine MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups)  
(Regional and zonal) | 

  * **Traffic** : [instance/network/received_bytes_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/instance/network/received_bytes_count)
  * **Saturation** : [instance/cpu/utilization](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/instance/cpu/utilization)

|   
[ Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service)  
(Regional and multi-regional) | 

  * **Traffic** : The metric depends on whether the service is single- or multi-region: 
    * Single: [service/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#metastore/service/request_count).
    * Multi: [service/multi_region/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#metastore/service/multi_region/request_count).
  * **Server error rate** : The ratio of the number of [service/grpc/finished_requests_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#metastore/service/grpc/finished_requests_count) with a response status that indicates an error to the total number of finished requests. The following status values indicate an error: 
    * `DEADLINE_EXCEEDED`
    * `INTERNAL`
    * `UNAVAILABLE`
    * `UNIMPLEMENTED`
  * **P95 latency** : The metric depends on whether the service is single- or multi-region: 
    * Single: [service/request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#metastore/service/request_latencies)
    * Multi: [service/multi_region/request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#metastore/service/multi_region/request_latencies).

| Application labels aren't attached to spans.For general information, see [Dataproc Metastore overview](https://docs.cloud.google.com/dataproc-metastore/docs/overview).  
[ Cloud Deploy delivery pipelines](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines)  
(Regional) |  | Application labels aren't attached to spans.  
[Firestore databases](https://firebase.google.com/docs/firestore)  
(Regional) | 

  * **Traffic** : [api/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#firestore/api/request_count)
  * **Server error rate** : Ratio of requests with a response status that indicates an error to the total number of requests. The following status values indicate an error: 
    * `DEADLINE_EXCEEDED`
    * `INTERNAL`
    * `UNAVAILABLE`
    * `UNIMPLEMENTED`
  * **P95 latency** : [api/request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#firestore/api/request_latencies)

| Application labels aren't attached to spans.  
GKE Gateway  
[`gateway.networking.k8s.io/Gateway`](https://kubernetes.io/docs/concepts/services-networking/gateway/) | 

  * **Traffic** : [application_lb/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/application_lb/request_count)
  * **Server error rate** : The ratio of the number of requests with a response status of `5xx` to the total number of requests.
  * **P95 latency** : [application_lb/total_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/application_lb/total_latencies)

| Application labels aren't attached to log entries or to spans.  
GKE Ingress  
[`networking.k8s.io/Ingress`](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/) | 

  * **Traffic** : [application_lb/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/application_lb/request_count)
  * **Server error rate** : The ratio of the number of requests with a response status of `5xx` to the total number of requests.
  * **P95 latency** : [application_lb/total_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/application_lb/total_latencies)

| Application labels aren't attached to spans.  
[Kubernetes CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)  
(Regional and zonal) |  | To learn how to run CronJobs in GKE, see [About CronJobs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cronjobs).  
[Kubernetes DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)  
(Regional and zonal) | See Golden signals for Kubernetes. |   
[Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)  
(Regional and zonal) | See Golden signals for Kubernetes. |   
[Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)  
(Regional and zonal) | See Golden signals for Kubernetes. | To learn how to use a StatefulSet or deploy a stateful application, see [About StatefulSets in Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset).   
[Layer 7 external and internal Application Load Balancers with HTTP or HTTPS traffic](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer)  
(Global, regional, and cross-region) | 

  * **Traffic** : Based on a Cloud Load Balancing metric type that records the request count, like [https/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/https/request_count). The configuration of the Cloud Load Balancing determines the actual metric.
  * **Server error rate** : The ratio of the number of requests with a response status of `5xx` to the total number of requests.
  * **P95 latency** : Based on a Cloud Load Balancing metric type that records total latencies, like [https/total_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#loadbalancing/https/total_latencies). The configuration of the Cloud Load Balancing determines the actual metric. 

| For Application Load Balancers, only [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) and [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service) are integrated with App Hub. Application labels aren't attached to spans.  
[Memorystore for Redis clusters](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification)  
(Regional) | 

  * **Saturation** : [cluster/cpu/average_utilization](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#redis/cluster/cpu/average_utilization)

| Application labels aren't attached to log entries or to spans.  
[Memorystore for Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/instances)  
(Regional) |  | Application labels aren't attached to metric data or to spans.  
[Pub/Sub topics](https://docs.cloud.google.com/pubsub/docs/create-topic)  
(Global) | 

  * **Traffic** : [topic/send_request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/send_request_count)
  * **Server error rate** : The ratio of the number of requests with a response code of `internal` to the total number of requests.
  * **P95 latency** : [topic/send_request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/topic/send_request_latencies)

| Application labels aren't attached to spans.  
[Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview)  
(Global) | 

  * **Traffic** : [subscription/pull_request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/pull_request_count)
  * **Server error rate** : The ratio of the number of requests with a response code of `internal` to the total number of requests.
  * **P95 latency** : [subscription/push_request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/push_request_latencies)

| Application labels aren't attached to spans.  
[Secret Manager secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets)  
(Global and regional) |  | Application labels aren't attached to spans.  
[Spanner databases](https://docs.cloud.google.com/spanner/docs/databases)  
(Global and regional) |  | Application labels aren't attached to metric data or to spans.  
[Spanner instances](https://docs.cloud.google.com/spanner/docs/instances)  
(Global and regional) | 

  * **Traffic** : [api/api_request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#spanner/api/api_request_count)
  * **Server error rate** : Ratio of requests with a response status that indicates an error to the total number of requests. The following status values indicate an error: 
    * `data_loss`
    * `deadline_exceeded`
    * `internal`
    * `unavailable`
    * `unimplemented`
    * `unknown`
  * **P95 latency** : [api/request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#spanner/api/request_latencies)
  * **Saturation** : [instance/cpu/utilization](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#spanner/instance/cpu/utilization)

| Application labels aren't attached to spans.  
[Vertex AI Agent Engine agents](https://docs.cloud.google.com/agent-builder/agent-engine/overview)  
(Regional)  | 

  * **Traffic** : [reasoning_engine/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#aiplatform/reasoning_engine/request_count)
  * **Server error rate** : Ratio of requests whose response status is at least 500 and no more than 599 to the total number of requests. 
  * **P95 latency** : [reasoning_engine/request_latencies](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#aiplatform/reasoning_engine/request_latencies)

|   
[Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview)  
(Global) | 

  * **Traffic** : [mcp/request_count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#serviceruntime/mcp/request_count)
  * **Server error rate** : The ratio of the number of requests with a response status of `5xx` to the total number of requests.
  * **P95 latency** : [mcp/request_durations](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#serviceruntime/mcp/request_durations)

| Golden signals are shown only in the detailed dashboard. Application labels aren't attached to metric data or to spans.  
  
## Golden signals for Kubernetes

For Kubernetes DaemonSets, Deployments, and StatefulSets, Google Cloud Observability uses the following metric data to derive values for golden signals, when that metric data is available:

  * **Traffic** : [service/server/request_count](https://docs.cloud.google.com/monitoring/api/metrics_istio#istio/service/server/request_count). The units for this metric are requests per second.
  * **Server error rate** : Ratio of `service/server/request_count` requests whose response status is at least 500 and no more than 599 to the total number of requests.
  * **P95 latency** : The 95th percentile from the [service/server/response_latencies](https://docs.cloud.google.com/monitoring/api/metrics_istio#istio/service/server/response_latencies) metric.
  * **Saturation** : The ratio of the [container/cpu/core_usage_time](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) to the [container/cpu/request_cores](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores). 



On a dashboard, you might see that the chart that displays traffic information contains two tabs:

  * The tab labeled **Traffic (Requests)** displays networking L7 traffic data and the units are requests per second.
  * The tab labeled **Traffic (Bytes)** displays the [pod/network/received_bytes_count](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/pod/network/received_bytes_count) metric, which has units of KiB per second and is a networking L4 metric.



When both the L7 and L4 traffic metrics are available, the L7 metrics appear on the summary pages but the traffic chart contains tabs, which let you view both metrics. If only one metric is available, then that metric is shown on the summary page and on dashboards.

For workloads that run on GKE, Google Cloud Observability might derive golden signals from the Prometheus metric `http_server_request_duration_seconds`, which is only available when you instrument your application by using OpenTelemetry. To learn more, see [Instrument your application](https://docs.cloud.google.com/stackdriver/docs/observability/instrument-for-application-monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
