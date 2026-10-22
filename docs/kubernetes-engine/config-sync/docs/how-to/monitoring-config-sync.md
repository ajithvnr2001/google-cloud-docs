---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync/
title: Config Sync metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:07.234106+00:00
---

# Config Sync metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Config Sync metrics Stay organized with collections  Save and categorize content based on your preferences. 

The page describes the OpenTelemetry metrics available to monitor your Config Sync resources.

## Pricing

Config Sync metrics use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) to load metrics into Cloud Monitoring. Cloud Monitoring charges for the ingestion of these metrics are based on the number of samples ingested.

For more information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary). 

## How Config Sync collects metrics

Config Sync uses [OpenCensus](https://opentelemetry.io/) to create and record metrics and [OpenTelemetry](https://opentelemetry.io/) to export its metrics to [Prometheus](https://prometheus.io/) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). The following guides explain how to export metrics:

  * [Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring)
  * [Prometheus](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-prometheus)
  * [Custom monitoring system](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md) (not recommended)



To configure the OpenTelemetry Collector, by default, Config Sync creates a ConfigMap named `otel-collector`. The `otel-collector` Deployment runs in the `config-management-monitoring` namespace.

The creation of the `otel-collector` ConfigMap configures the `prometheus` exporter, which exposes a metrics endpoint for Prometheus to scan.

When you run Config Sync on GKE, or in another Kubernetes environment that's configured with Google Cloud credentials, Config Sync creates a ConfigMap named `otel-collector-google-cloud`. The `otel-collector-google-cloud` overrides the configuration in the `otel-collector` ConfigMap. Config Sync reverts any changes to the `otel-collector` or `otel-collector-google-cloud` ConfigMaps.

The creation of the `otel-collector-google-cloud` ConfigMap also adds the `cloudmonitoring` exporter, which exports to Cloud Monitoring, and the `kubernetes` exporter, which exports to Google's internal metric service. The `kubernetes` exporter sends select, anonymized metrics to Google to help improve Config Sync.

Cloud Monitoring stores the metrics that you send to it in your Google Cloud project. The `cloudmonitoring` and `kubernetes` exporters use the same Google Cloud service account, which needs IAM permission to write to Cloud Monitoring. To configure these permissions, see [Grant metric-writing permission for Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring#metric-permission).

### Disable monitoring

By default, Config Sync collects metrics for all `RootSync` and `RepoSync` objects. Disabling metrics is supported only with custom `RootSync` or `RepoSync` objects. If your `RootSync` object was created by default when you installed Config Sync with the Google Cloud console, Google Cloud CLI, or Terraform, and has the name `root-sync`, any change made to the `spec.monitoring.enabled` field is automatically reverted.

To disable metric collection for a specific `RootSync` or `RepoSync` object, set the `spec.monitoring.enabled` field to `false` in the `RootSync` or `RepoSync` custom resource:

When monitoring is disabled for a `RootSync` or `RepoSync` object:

  * The `otel-agent` sidecar container is omitted from the reconciler Pod.
  * Telemetry collection and exporting for that specific reconciler are disabled, which can help reduce resource consumption.



The following example disables monitoring on a custom `RootSync` or `RepoSync` object:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync # or RepoSync
    metadata:
      name: SYNC_NAME
      namespace: SYNC_NAMESPACE
    spec:
      monitoring:
        enabled: false
    

## OpenTelemetry metrics

Config Sync and the Resource Group Controller collect the following metrics with [OpenCensus](https://opencensus.io/introduction/) and make them available through [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) . The **Tags** column lists Config Sync specific [tags](https://opencensus.io/tag/) that are applicable to each metric. Metrics with tags represent multiple measurements, one for each combination of tag values.

**Note:** The reconciler tag is dynamically created from the RootSync and RepoSync objects. For examples on what this tag looks like and how to use it, see [Querying metrics by reconciler](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring#queryreconciler).

### Config Sync metrics

Name | Type | Tags | Description  
---|---|---|---  
api_duration_seconds | Distribution | operation, status | The latency distribution of API server calls.  
apply_duration_seconds | Distribution | status | The latency distribution of applying resources declared from source of truth to a cluster.  
apply_operations_total | Count | operation, status, controller | The total number of operations that have been performed to sync resources from source of truth to a cluster.  
declared_resources | Last Value |  | The number of declared resources parsed from Git.  
internal_errors_total | Count | source | The total number of internal errors encountered by Config Sync. Metric might not appear in query results if no internal error has happened.  
last_sync_timestamp | Last Value | status | The timestamp of the most recent sync from Git.  
parser_duration_seconds | Distribution | status, trigger, source | The latency distribution of different stages involved in syncing from source of truth to a cluster.  
pipeline_error_observed | Last Value | name, reconciler, component | The status of RootSync and RepoSync custom resources. A value of 1 indicates a failure.  
reconcile_duration_seconds | Distribution | status | The latency distribution of reconcile events handled by the reconciler manager.  
reconciler_errors | Last Value | component, errorclass | The number of errors encountered while syncing resources from the source of the truth to a cluster.  
remediate_duration_seconds | Distribution | status | The latency distribution of remediator reconciliation events.  
resource_conflicts_total | Count |  | The total number of resource conflicts resulting from a mismatch between the cached resources and cluster resources. Metric might not appear in query results if no resource conflict has happened.  
resource_fights_total | Count |  | The total number of resources that are being synced too frequently. Any result higher than zero indicates a problem. For more information, see [KNV2005: ResourceFightWarning](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors#knv2005). Metric might not appear in query results if no resource fight has happened.  
  
### Resource Group Controller metrics

The Resource Group Controller is a component in Config Sync that keeps track of the managed resources and checks if each individual resource is ready or reconciled. The following metrics are available.

Name | Type | Tags | Description  
---|---|---|---  
rg_reconcile_duration_seconds | Distribution | stallreason | The distribution of time taken to reconcile a ResourceGroup CR  
resource_group_total | Last Value |  | The current number of ResourceGroup CRs  
resource_count | Last Value | resourcegroup | The total number of resources tracked by a ResourceGroup  
ready_resource_count | Last Value | resourcegroup | The total number of ready resources in a ResourceGroup  
resource_ns_count | Last Value | resourcegroup | The number of namespaces used by resources in a ResourceGroup  
cluster_scoped_resource_count | Last Value | resourcegroup | The number of cluster scoped resources in a ResourceGroup  
crd_count | Last Value | resourcegroup | The number of CRDs in a ResourceGroup  
kcc_resource_count | Last Value | resourcegroup | The total number of KCC resources in a ResourceGroup  
pipeline_error_observed | Last Value | name, reconciler, component | The status of RootSync and RepoSync custom resources. A value of 1 indicates a failure.  
  
### Config Sync metric labels

Metric labels can be used to aggregate metric data in Cloud Monitoring and Prometheus. They are selectable from the "Group By" drop-down list in the [Monitoring Console](https://console.cloud.google.com/monitoring).

For more information about Cloud Monitoring label and Prometheus metric label, see the [Components of the metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model) and [Prometheus data model](https://prometheus.io/docs/concepts/data_model/).

**Note:** The Tags from Config Sync metrics and Resource Group Controller metrics are conceptually equivalent to Labels in this section.

### Metric labels

The following labels are used by Config Sync and Resource Group Controller metrics, available when monitoring with Cloud Monitoring and Prometheus.

Name | Values | Description  
---|---|---  
`operation` | create, patch, update, delete | The type of operation performed  
`status` | success, error | The execution status of an operation  
`reconciler` | rootsync, reposync | The type of the Reconciler  
`source` | parser, differ, remediator | The source of the internal error  
`trigger` | retry, watchUpdate, managementConflict, resync, reimport | The trigger of an reconciliation event  
`name` | The name of reconciler | The name of the Reconciler  
`component` | parsing, source, sync, rendering, readiness | The name of component / current stage of reconciliation  
`container` | reconciler, git-sync | The name of the container  
`resource` | cpu, memory | The type of the resource  
`controller` | applier, remediator | The name of the controller in a root or namespace reconciler  
`type` | Any Kubernetes resource, for example ClusterRole, Namespace, NetworkPolicy, Role, and so on. | The kind of Kubernetes API  
`commit` | \---- | The hash of the latest synced commit  
**Note:** Depending on the frequency of production repository commits and variance in Kubernetes Kinds being deployed, the metric labels `commit` and `type` can cause an increase in Cloud Monitoring metric write throughput compared to other metrics. The affected metrics are `apply_duration_seconds`, `api_duration_seconds`, `declared_resources`, `apply_operations_total`. To avoid an increase in billing or if these metrics are not needed, follow the instructions to [patch the otel collector deployment with ConfigMap](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md) and remove the aforementioned metrics from `filter/cloudmonitoring` allowlist.

### Resource labels

Config Sync metrics sent to Prometheus and Cloud Monitoring have the following metric labels set to identify the source Pod:

Name | Description  
---|---  
`k8s.node.name` | The name of the Node hosting a Kubernetes Pod  
`k8s.pod.namespace` | The namespace of the Pod  
`k8s.pod.uid` | The UID of the Pod  
`k8s.pod.ip` | The IP of the Pod  
`k8s.deployment.name` | The name of the Deployment that owns the Pod  
  
Config Sync metrics sent to Prometheus and Cloud Monitoring from `reconciler` Pods also have the following metric labels set to identify the RootSync or RepoSync used to configure the reconciler:

Name | Description  
---|---  
`configsync.sync.kind` | The kind of resource that configures this reconciler: `RootSync` or `RepoSync`  
`configsync.sync.name` | The name of the `RootSync` or `RepoSync` that configures this reconciler  
`configsync.sync.namespace` | The namespace of the `RootSync` or `RepoSync` that configures this reconciler  
  
### Cloud Monitoring resource labels

Cloud Monitoring Resource labels are used for indexing metrics in storage, which means they have negligible effect on cardinality, unlike metric labels, where cardinality is a significant performance concern. See [Monitored Resource Types](https://docs.cloud.google.com/monitoring/api/v3/metric-model) for more information.

The `k8s_container` resource type sets the following resource labels to identify the source Container:

Name | Description  
---|---  
`container_name` | The name of the Container  
`pod_name` | The name of the Pod  
`namespace_name` | The namespace of the Pod  
`location` | The region or zone of the cluster hosting the node  
`cluster_name` | The name of the cluster hosting the node  
`project` | The ID of the project hosting the cluster  
  
## Configure custom metric filtering

You can adjust the custom metrics that Config Sync exports to Prometheus, Cloud Monitoring, and Google's internal monitoring service. Adjust custom metrics to fine-tune the included metrics or configure different backends.

To modify custom metrics, create and then edit a ConfigMap named `otel-collector-custom`. Using this ConfigMap ensures that Config Sync doesn't revert any of the modifications that you make. If you modify the `otel-collector` or `otel-collector-google-cloud` ConfigMaps, Config Sync reverts any changes.

For examples of how to adjust this ConfigMap, see [Custom Metric Filtering](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md) in the open source Config Sync documentation.

## Understand the pipeline_error_observed metric

The `pipeline_error_observed` metric is a metric that can help you quickly identify RepoSync or RootSync CRs that are not in sync or contain resources that are not reconciled to the desired state.

  * For a successful sync by a RootSync or RepoSync, the metrics with all components (`rendering`, `source`, `sync`, `readiness`) are observed with value 0.

![A screenshot of the pipeline_error_observed metric with all components observed with value 0](https://docs.cloud.google.com/static/kubernetes-engine/config-sync/docs/img/pipeline-error-observed-metric.png)

  * When the latest commit fails the [automated rendering](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-helm), the metric with the component `rendering` is observed with value 1.

  * When checking out the latest commit encounters error or the latest commit contains invalid configuration, the metric with the component `source` is observed with value 1.

  * When a resource fails to be applied to the cluster, the metric with the component `sync` is observed with value 1.

  * When a resource is applied, but fails to reach its desired state, the metric with the component `readiness` is observed with value 1. For example, a Deployment is applied to the cluster, but the corresponding Pods are not created successfully.




## What's next

  * Learn more about how to [monitor RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).
  * Learn how to [use the Config Sync SLIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/config-sync-slis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
