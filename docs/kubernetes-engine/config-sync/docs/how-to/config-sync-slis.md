---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/config-sync-slis/
title: Use Config Sync SLIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:13.143620+00:00
---

# Use Config Sync SLIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/config-sync-slis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Use Config Sync SLIs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Config Sync service level indicators (SLIs).

To receive notifications when Config Sync isn't working as intended, set up [Prometheus alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) based on these SLIs. Each SLI includes an example of how to create an alerting rule. To learn more about using Prometheus with Config Sync, see [Monitor Config Sync with metrics](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync).

## Config Sync Pods with incorrect container count

If the container count of a Config Sync Pod is lower than expected, then Config Sync might not be running. You can set up an alert to detect this issue and inspect the Config Sync Pod to figure out why some containers are missing. When setting your alerts, we recommend that you set the time interval to at least five minutes to avoid unnecessary alerts. For example, during upgrading, the container count of a Pod might drop below the target.

If you're not familiar with the expected container count, see [Config Sync Deployments, Pods, and containers](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#deployments-pods-containers).

### Prometheus alerting rule examples

This section includes examples that notify you when there are Pods with an incorrect container count.

  * To receive a notification when the container count of a root reconciler Pod is below the expected count, create the following alerting rule:
        
        alert: RootReconcilerPodMissingContainer
        expr: count by (cluster_name, pod_name) (kubernetes_io:container_uptime{namespace_name="config-management-system", pod_name=~"root-reconciler-.*"}) < 4
        # Setting the for field to 5m to avoid unnecessary alerts.
        for: 5m
        

  * To receive a notification when the container count of a namespace reconciler Pod is below the expected count, create the following alerting rule:
        
        alert: NamespaceReconcilerPodMissingContainer
        expr: count by (cluster_name, pod_name) (kubernetes_io:container_uptime{namespace_name="config-management-system", pod_name=~"ns-reconciler-.*"}) < 4
        for: 5m
        

  * To receive a notification when the container count of a reconciler-manager Pod is below the expected count, create the following alerting rule:
        
        alert: ReconcilerManagerPodMissingContainer
        expr: count by (cluster_name, pod_name) (kubernetes_io:container_uptime{namespace_name="config-management-system", pod_name=~"reconciler-manager-.*"}) < 2
        for: 5m
        




## Unhealthy Config Sync containers

If the restart count of a Config Sync container reaches a certain threshold, something is wrong. For example, a root reconciler container which doesn't have enough memory resources would restart with the `OOMKilled` error until it gets enough memory.

### Prometheus alerting rule example

To receive a notification when a Config Sync container has restarted more than three times, create the following alerting rule:
    
    
    alert: TooManyContainerRestarts
    expr: kubernetes_io:container_restart_count{namespace_name=~"config-management-system|config-management-monitoring|resource-group-system"} > 3
    

## Config Sync encountering persistent errors

If Config Sync encounters persistent errors, something is wrong. When Config Sync encounters [errors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors), it keeps retrying to sync configs from the source to a cluster until it's successful. However, some errors cannot be fixed by retrying and require your intervention.

### Prometheus alerting rule example

To receive a notification when a root or namespace reconciler encounters persistent errors for two hours, create the following alerting rule:
    
    
    alert: PersistentConfigSyncErrors
    expr: sum by (cluster, configsync_sync_kind, configsync_sync_name, configsync_sync_namespace, errorclass) (config_sync_reconciler_errors) > 0
    for: 2h
    

In this example:

  * The `configsync_sync_kind` label can have the following values: `RootSync` or `RepoSync`.
  * The `configsync_sync_name` label indicates the name of a RootSync or RepoSync object.
  * The `configsync_sync_namespace` label indicates the namespace of a RootSync or RepoSync object.
  * The `errorclass` label can have three values: `1xxx`, `2xxx`, and `9xxx`. Each label corresponds to a different type of error:

    * `1xxx` errors: configuration errors that you can fix
    * `2xxx` errors: server side errors that you might not be able to fix
    * `9xxx` errors: internal errors that you can't fix



## Config Sync stuck in the syncing stage

A sync attempt in Config Sync is non-interruptible. If the configs in the source are too big or complex (for example, your source contains a high number of Config Connector resources), it can take over an hour to finish syncing these configs to the cluster. However, if two hours have passed since the last successful sync, something might be wrong.

You can check whether the current sync attempt is still ongoing by checking the RootSync or RepoSync status. If the current sync attempt is still ongoing, you can choose to [break up your source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/breaking-up-repo) so that every source of truth can be synced faster, or increase the alerting threshold from two hours to something longer. If there's no sync attempt ongoing, the Config Sync reconciler is broken since it's supposed to keep retrying until it syncs the configs from source to the cluster successfully. If this happens, escalate to [Google Cloud Support](https://docs.cloud.google.com/support/docs).

### Prometheus alerting rule example

To be notified when the last successful sync of a root or namespace reconciler was more than two hours ago, create an alerting rule:
    
    
      alert: OldLastSyncTimestamp
      # The status label indicates whether the last sync succeeded or not.
      # Possible values: success, error.
      expr: time() - topk by (cluster, configsync_sync_kind, configsync_sync_name, configsync_sync_namespace) (1, config_sync_last_sync_timestamp{status="success"}) > 7200
    

## Config Sync experiencing performance regressions

Config Sync might have performance regressions after being upgraded. The performance regressions can happen in the following ways:

  * An increase of the time overhead of reconciling a RootSync or RepoSync object
  * An increase of the time overhead of reconciling a ResourceGroup object
  * An increase of the time overhead of syncing configs from source to a cluster



### The time overhead of reconciling a RootSync or RepoSync object

The `reconciler-manager` Deployment reconciles RootSync and RepoSync objects. You can use the ninetieth percentile of the time overhead of reconciling a RootSync or RepoSync object to detect performance regressions.

#### Prometheus alerting rule examples

This section includes Prometheus alerting rules examples that notify you when the `reconciler-manager` Deployment has performance regressions.

The following examples send you a notification when the ninetieth percentile of the time overhead of reconciling a RootSync or RepoSync object over the last 5 hours is over 0.1 seconds for 10 minutes. You can create alerting rules that monitor all clusters, or a single cluster.

  * Create the following rule to monitor all clusters:
        
        alert: HighLatencyReconcileRootSyncAndRepoSyncOverall
        expr: histogram_quantile(0.9, sum by (le) (rate(config_sync_reconcile_duration_seconds_bucket[5h]))) > 0.1
        for: 10m
        

  * Create the following rule to monitor a single cluster:
        
        alert: HighLatencyReconcileRootSyncAndRepoSyncClusterLevel
        expr: histogram_quantile(0.9, sum by (cluster, le) (rate(config_sync_reconcile_duration_seconds_bucket[5h]))) > 0.1
        for: 10m
        




### The time overhead of reconciling a ResourceGroup object

The `resource-group-controller-manager` Deployment reconciles ResourceGroup objects. You can use the ninetieth percentile of the time overhead of reconciling a ResourceGroup to catch performance regressions.

#### Prometheus alerting rule examples

This section includes Prometheus alerting rules that notify you when the `resource-group-controller-manager` Deployment has performance regressions.

The following examples send you a notification when the ninetieth percentile of the time overhead of reconciling a ResourceGroup object over the last 5 hours is over 5 seconds for 10 minutes. You can create alerting rules that monitor all clusters, or a single cluster.

  * Create the following rule to monitor all clusters:
        
        alert: HighLatencyReconcileResourceGroupOverall
        expr: histogram_quantile(0.9, sum by (le) (rate(config_sync_rg_reconcile_duration_seconds_bucket[5h]))) > 5
        for: 10m
        

  * Create the following rule to monitor a single cluster:
        
        alert: HighLatencyReconcileResourceGroupClusterLevel
        expr: histogram_quantile(0.9, sum by (cluster, le) (rate(config_sync_rg_reconcile_duration_seconds_bucket[5h]))) > 5
        for: 10m
        




### The time overhead of syncing configs from source to a cluster

A root or namespace reconciler syncs configs from source of truth to a cluster. You can use the ninetieth percentile of the time overhead of syncing configs from the source to a cluster to detect performance regressions.

#### Prometheus alerting rule examples

This section includes Prometheus alerting rules that notify you when the root or namespace reconciler Deployment has performance regressions.

The following examples send you a notification when the ninetieth percentile of the time overhead of syncing configs across all clusters over the last five hours is over one hour for five minutes.You can create alerting rules that monitor all clusters, or a single cluster.

  * Create the following rule to monitor all clusters:
        
        alert: HighApplyDurationOverall
        expr: histogram_quantile(0.9, sum by (le) (rate(config_sync_apply_duration_seconds_bucket[5h]))) > 3600
        for: 5m
        

**Note:** The bounds for the histogram distribution are `[]float64{1, 5, 10, 30, 60, 300, 600, 1200, 1800, 3600, 5400}`.
  * Create the following rule to monitor a single cluster:
        
        alert: HighApplyDurationRootSyncRepoSyncLevel
        expr: histogram_quantile(0.9, sum by (cluster, configsync_sync_kind,configsync_sync_name, configsync_sync_namespace, le) (rate(config_sync_apply_duration_seconds_bucket[5h]))) > 3600
        for: 5m
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
