---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-prometheus/
title: Monitor Config Sync with Prometheus \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:06.909427+00:00
---

# Monitor Config Sync with Prometheus  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-prometheus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Monitor Config Sync with Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

The page describes how to send metrics from Config Sync to Prometheus.

This page explains how to use Prometheus to view Config Sync metrics. We recommend that you use either Prometheus (this page) or [Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring) to export metrics. It's also possible to use [custom metrics](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md).

Config Sync automatically collects and exports metrics to [Prometheus](https://prometheus.io/). You can configure [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to pull custom metrics from Prometheus. Then you can see custom metrics in both Prometheus and Monitoring. For more information, see [Using Prometheus](https://docs.cloud.google.com/monitoring/kubernetes-engine/prometheus) in the GKE documentation.

## Scrape the metrics

All Prometheus metrics are available for scraping at port 8675. Before you can scrape metrics, you need to configure your cluster for Prometheus in one of two ways. Either:

  * Follow the [Prometheus documentation](https://prometheus-operator.dev/docs/prologue/introduction/) to configure your cluster for scraping, **or**

  * Use the [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) along with the following manifests, which scrape all Config Sync metrics every 10 seconds.

**Note:** You need [kubectl v1.14](https://kubernetes.io/docs/tasks/tools/install-kubectl/) and the `curl` command to follow this procedure. If your cluster runs 1.14 or higher, you can use the `kubectl` command provided by the [Google Cloud CLI](https://docs.cloud.google.com/sdk).
    1. Create a temporary directory to hold the manifest files.
           
           mkdir config-sync-monitor
           cd config-sync-monitor
           

    2. Download the Prometheus Operator manifest from the [CoreOS repository](https://github.com/coreos/prometheus-operator/). repository, using the `curl` command:
           
           curl -o bundle.yaml https://raw.githubusercontent.com/coreos/prometheus-operator/master/bundle.yaml
           

This manifest is configured to use the `default` namespace, which is not recommended. The next step modifies the configuration to use a namespace called `monitoring` instead. To use a different namespace, substitute it where you see `monitoring` in the remaining steps.

    3. Create a file to update the namespace of the ClusterRoleBinding in the bundle above.
           
           # patch-crb.yaml
           apiVersion: rbac.authorization.k8s.io/v1
           kind: ClusterRoleBinding
           metadata:
             name: prometheus-operator
           subjects:
           - kind: ServiceAccount
             name: prometheus-operator
             namespace: monitoring # we are patching from default namespace
           

    4. Create a `kustomization.yaml` file that applies the patch and modifies the namespace for other resources in the manifest.
           
           # kustomization.yaml
           resources:
           - bundle.yaml
           
           namespace: monitoring
           
           patchesStrategicMerge:
           - patch-crb.yaml
           

    5. Create the `monitoring` namespace if one does not exist. You can use a different name for the namespace, but if you do, also change the value of `namespace` in the YAML manifests from the previous steps.
           
           kubectl create namespace monitoring
           

    6. Apply the Kustomize manifest using the following commands:
           
           kubectl apply -k .
           
           until kubectl get customresourcedefinitions servicemonitors.monitoring.coreos.com ; \
           do date; sleep 1; echo ""; done

The second command blocks until the CRDs are available on the cluster.

    7. Create the manifest for the resources necessary to configure a Prometheus server which scrapes metrics from Config Sync.
           
           # config-sync-monitoring.yaml
           apiVersion: v1
           kind: ServiceAccount
           metadata:
             name: prometheus-config-sync
             namespace: monitoring
           ---
           apiVersion: rbac.authorization.k8s.io/v1
           kind: ClusterRole
           metadata:
             name: prometheus-config-sync
           rules:
           - apiGroups: [""]
             resources:
             - nodes
             - services
             - endpoints
             - pods
             verbs: ["get", "list", "watch"]
           - apiGroups: [""]
             resources:
             - configmaps
             verbs: ["get"]
           - nonResourceURLs: ["/metrics"]
             verbs: ["get"]
           ---
           apiVersion: rbac.authorization.k8s.io/v1
           kind: ClusterRoleBinding
           metadata:
             name: prometheus-config-sync
           roleRef:
             apiGroup: rbac.authorization.k8s.io
             kind: ClusterRole
             name: prometheus-config-sync
           subjects:
           - kind: ServiceAccount
             name: prometheus-config-sync
             namespace: monitoring
           ---
           apiVersion: monitoring.coreos.com/v1
           kind: Prometheus
           metadata:
             name: config-sync
             namespace: monitoring
             labels:
               prometheus: config-sync
           spec:
             replicas: 2
             serviceAccountName: prometheus-config-sync
             serviceMonitorSelector:
               matchLabels:
                 prometheus: config-management
             alerting:
               alertmanagers:
               - namespace: default
                 name: alertmanager
                 port: web
             resources:
               requests:
                 memory: 400Mi
           ---
           apiVersion: v1
           kind: Service
           metadata:
             name: prometheus-config-sync
             namespace: monitoring
             labels:
               prometheus: config-sync
           spec:
             type: NodePort
             ports:
             - name: web
               nodePort: 31900
               port: 9190
               protocol: TCP
               targetPort: web
             selector:
               prometheus: config-sync
           --- 
           --- 
           

    8. Apply the manifest using the following commands:
           
           kubectl apply -f config-sync.yaml
           
           until kubectl rollout status statefulset/prometheus-config-sync -n monitoring; \
           do sleep 1; done
           

The second command blocks until the Pods are running.

    9. You can verify the installation by forwarding the web port of the Prometheus server to your local machine.
           
           kubectl -n monitoring port-forward svc/prometheus-config-sync 9190
           

You can now access the Prometheus web UI at `http://localhost:9190`.

    10. Remove the temporary directory.
           
           cd ..
           rm -rf config-sync-monitor
           




## Available Prometheus metrics

Config Sync collects the following metrics and makes them available to Prometheus. The **Labels** column lists all [labels](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels) that are applicable to each metric. Metrics without labels represent a single measurement over time while metrics with labels represent multiple measurements, one for each combination of label values.

If this table becomes out of sync, you can filter metrics by prefix in the Prometheus user interface. All of the metrics start with the prefix `config_sync_`.

Name | Type | Labels | Description  
---|---|---|---  
`config_sync_api_duration_seconds_bucket` | Histogram | status, operation | Latency distribution of API server calls (distributed into buckets by duration of each cycle)  
`config_sync_api_duration_seconds_count` | Histogram | status, operation | Latency distribution of API server calls (ignoring duration)  
`config_sync_api_duration_seconds_sum` | Histogram | status, operation | Sum of the durations of all API server calls  
`config_sync_apply_duration_seconds_bucket` | Histogram | commit, status | Latency distribution of applying resources declared from source of truth to a cluster (distributed into buckets by duration of each cycle)  
`config_sync_apply_duration_seconds_count` | Histogram | commit, status | Latency distribution of applying resources declared from source of truth to a cluster (ignoring duration)  
`config_sync_apply_duration_seconds_sum` | Histogram | commit, status | Sum of the durations of all the latency of applying resources declared from source of truth to a cluster  
`config_sync_apply_operations_total` | Counter | operation, status, controller | Number of operations that have been performed to sync resources from source of truth to a cluster  
`config_sync_cluster_scoped_resource_count` | Gauge | resourcegroup | Number of cluster scoped resources in a ResourceGroup  
`config_sync_crd_count` | Gauge | resourcegroup | Number of CRDs in a ResourceGroup  
`config_sync_declared_resources` | Gauge | commit | Number of declared resources parsed from Git  
`config_sync_internal_errors_total` | Counter | source | Number of internal errors triggered by Config Sync. Metric might not appear if no internal error has happened  
`config_sync_kcc_resource_count` | Gauge | resourcegroup | Number of Config Connector resources in a ResourceGroup  
`config_sync_last_apply_timestamp` | Gauge | commit, status | Timestamp of the most recent apply operation  
`config_sync_last_sync_timestamp` | Gauge | commit, status | Timestamp of the most recent sync from Git  
`config_sync_parser_duration_seconds_bucket` | Histogram | status, trigger, source | Latency distribution of different stages involved in syncing from source of truth to a cluster  
`config_sync_parser_duration_seconds_count` | Histogram | status, trigger, source | Latency distribution of different stages involved in syncing from source of truth to a cluster (ignoring duration)  
`config_sync_parser_duration_seconds_sum` | Histogram | status, trigger, source | Sum of the latencies of different stages involved in syncing from source of truth to a cluster  
`config_sync_pipeline_error_observed` | Gauge | name, reconciler, component | Status of RootSync and RepoSync custom resources. A value of 1 indicates a failure  
`config_sync_ready_resource_count` | Gauge | resourcegroup | Total number of ready resources in a ResourceGroup  
`config_sync_reconcile_duration_seconds_bucket` | Histogram | status | Latency distribution of reconcile events handled by the reconciler manager (distributed into buckets by duration of each call)  
`config_sync_reconcile_duration_seconds_count` | Histogram | status | Latency distribution of reconcile events handled by the reconciler manager (ignoring duration)  
`config_sync_reconcile_duration_seconds_sum` | Histogram | status | Sum of the durations of all latency of reconcile events handled by the reconciler manager  
`config_sync_reconciler_errors` | Gauge | component, errorclass | Number of errors encountered while syncing resources from the source of the truth to a cluster  
`config_sync_remediate_duration_seconds_bucket` | Histogram | status | Latency distribution of remediator reconciliation events (distributed into buckets by duration)  
`config_sync_remediate_duration_seconds_count` | Histogram | status | Latency distribution of remediator reconciliation events (ignoring duration)  
`config_sync_remediate_duration_seconds_sum` | Histogram | status | Sum of the durations of all latency of remediator reconciliation events  
`config_sync_resource_count` | Gauge | resourcegroup | Number of resources tracked by a ResourceGroup  
`config_sync_resource_conflicts_total` | Counter | commit | Number of resource conflicts resulting from a mismatch between the cached resources and cluster resources. Metric might not appear if no resource conflict has happened  
`config_sync_resource_fights_total` | Counter |  | Number of resources that are being synced too frequently. Metric might not appear if no resource fight has happened  
`config_sync_resource_group_total` | Gauge |  | Number of ResourceGroup CRs  
`config_sync_resource_ns_count` | Gauge | resourcegroup | Number of namespaces used by resources in a ResourceGroup  
`config_sync_rg_reconcile_duration_seconds_bucket`. | Histogram | stallreason | Time distribution of reconciling a ResourceGroup CR (distributed into buckets by duration)  
`config_sync_rg_reconcile_duration_seconds_count` | Histogram | stallreason | Time distribution of reconciling a ResourceGroup CR (ignoring duration)  
`config_sync_rg_reconcile_duration_seconds_sum` | Histogram | stallreason | Sum of the all time reconciling a ResourceGroup CR  
`config_sync_kustomize_build_latency_bucket` | Histogram |  | Latency distribution of `kustomize build` execution time (distributed into buckets by duration of each operation)  
`config_sync_kustomize_build_latency_count` | Histogram |  | Latency distribution of `kustomize build` execution time (ignoring duration)  
`config_sync_kustomize_build_latency_sum` | Histogram |  | Sum of all `kustomize build` execution time  
`config_sync_kustomize_ordered_top_tier_metrics` | Gauge | top_tier_field | Usage of Resources, Generators, SecretGenerator, ConfigMapGenerator, Transformers, and Validators  
`config_sync_kustomize_builtin_transformers` | Gauge | k8s_builtin_transformer | Usage of built-in transformers related to kubernetes object metadata  
`config_sync_kustomize_resource_count` | Gauge |  | Number of resources outputted by `kustomize build`  
`config_sync_kustomize_field_count` | Gauge | field_name | Number of times a particular field is used in the kustomization files  
`config_sync_kustomize_patch_count` | Gauge | patch_field | Number of patches in the fields `patches`, `patchesStrategicMerge`, and `patchesJson6902`  
`config_sync_kustomize_base_count` | Gauge | base_source | Number of remote and local bases  
`kustomize_deprecating_field_count` | Gauge | deprecating_field | Usage of fields that may become deprecated  
`kustomize_simplification_adoption_count` | Gauge | simplification_field | Usage of simplification transformers images, replicas, and replacements  
`kustomize_helm_inflator_count` | Gauge | helm_inflator | Usage of helm in kustomize, whether by the built-in fields or the custom function  
  
## Example debugging procedures for Prometheus

The following examples illustrate some patterns for using Prometheus metrics, object status fields, and object annotations to detect and diagnose problems related to Config Sync. These examples show how you can start with high level monitoring that detects a problem and then progressively refine your search to drill down and diagnose the root cause of the problem.

### Query configs by status

The `reconciler` process provides high-level metrics that give useful insight into an overall view of how Config Sync is operating on the cluster. You can see if any errors have occurred, and can even [set up alerts for them](https://prometheus.io/docs/alerting/overview/).
    
    
    config_sync_reconciler_errors
    

### Query metrics by reconciler

If you are using Config Sync RootSync and RepoSync APIs, then you can monitor the RootSync and RepoSync objects. The RootSync and RepoSync objects are instrumented with high-level metrics that give you useful insight into how Config Sync is operating on the cluster. Almost all metrics are tagged by the reconciler name, so you can see if any errors have occurred and can set up alerts for them in [Prometheus](https://prometheus.io/docs/alerting/overview/).

See the full list of [available metric labels](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync#metric-labels) for filtering.

In Prometheus, you can use the following filters for the RootSyncs or RepoSyncs:
    
    
    # Querying RootSync
    config_sync_reconciler_errors{configsync_sync_name=ROOT_SYNC_NAME}
    
    # Querying RepoSync
    config_sync_reconciler_errors{configsync_sync_name=REPO_SYNC_NAME}
    

### Query import and sync operations by status

In Prometheus, you could use the following queries:
    
    
    # Check for errors that occurred when sourcing configs.
    config_sync_reconciler_errors{component="source"}
    
    # Check for errors that occurred when syncing configs to the cluster.
    config_sync_reconciler_errors{component="sync"}
    

You can also check the metrics for the source and sync processes themselves:
    
    
    config_sync_parser_duration_seconds{status="error"}
    config_sync_apply_duration_seconds{status="error"}
    config_sync_remediate_duration_seconds{status="error"}
    

## Monitor resources with Google Cloud Managed Service for Prometheus

Google Cloud Managed Service for Prometheus is Google Cloud's fully managed multi-cloud solution for [Prometheus](https://prometheus.io/) metrics. It supports two modes for data collection: [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) (the recommended mode) or [self-deployed data collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged). Complete the following steps to set up monitoring Config Sync with Google Cloud Managed Service for Prometheus in the managed collection mode.

  1. Enable Managed Prometheus on your cluster by following the instructions on [Set up managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#config-mgd-collection).

  2. Save the following sample manifest as `pod-monitoring-config-sync-monitoring.yaml`. This manifest configures a [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.5.0/doc/api.md#podmonitoring) resource to scrape the Config Sync metrics on port `8675` of the `otel-collector-*` Pod under the `config-management-monitoring` namespace. The PodMonitoring resource uses a Kubernetes label selector to find the `otel-collector-*` Pod.
         
         apiVersion: monitoring.googleapis.com/v1
         kind: PodMonitoring
         metadata:
           name: config-sync-monitoring
           namespace: config-management-monitoring
         spec:
           selector:
             matchLabels:
               app: opentelemetry
               component: otel-collector
           endpoints:
           - port: 8675
             interval: 10s
         

  3. Apply the manifest to the cluster: 
         
         kubectl apply -f pod-monitoring-config-sync-monitoring.yaml
         

  4. Verify that your Prometheus data is being exported using the Cloud Monitoring Metrics Explorer page in the Google Cloud console following the instructions on [Managed Service for Prometheus data in Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#gmp-in-monitoring).


**Note:** When querying Prometheus metrics from Cloud Monitoring, the Histogram metrics with suffix `_count` or `_sum` in the available metrics won't appear.

## What's next

  * [Use Prometheus alerting rules with Config Sync SLIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/config-sync-slis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
