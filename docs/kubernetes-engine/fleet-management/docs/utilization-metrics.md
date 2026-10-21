---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics/
title: Fleet resource utilization metrics \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:15.068011+00:00
---

# Fleet resource utilization metrics  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Fleet resource utilization metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page dives deeper into the fleet and team resource utilization metrics by explaining how these metrics are calculated and providing tips for how to use these metrics to optimize resource usage.

You can view these metrics in the following dashboards:

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard)
  * [Team overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview)



These metrics describe how effectively your clusters are utilizing the physically available resources you pay for or resources that you allocate on on-premises hardware. You can use this information to understand resource utilization effectiveness at scale, on a fleet or team scope level. This can help you either optimize cluster size and resource allocation across clusters and namespaces, or optimize how application teams request and reserve resources.

## Use resource utilization metrics

The following tips can help you use the metrics in the console to identify and address problems:

  * If your fleet's **Total CPU/Memory/Disk utilization** indicates unexpectedly high or low utilization over the last seven days, always check the corresponding **CPU/Memory/Disk utilization by fleet** chart to evaluate if the unexpected utilization is constant or caused by usage spikes.
  * If **Top CPU/Memory/Disk utilization by cluster** indicates individual clusters that behave differently than the rest, consider investigating those particular clusters more closely. Consider resizing the clusters if possible.
  * If **Top CPU/Memory/Disk utilization by namespace** shows an unexpected spike over the last seven days, consider investigating if a specific workload is causing the spike. A possible solution might be to redistribute workloads across resources.
  * **CPU/Memory/Disk utilization by fleet** lets you observe the ratio between used and requested resources. A big difference between the two might mean that application teams are requesting and reserving too many resources.



## Understand resource utilization metrics

The following metrics are provided in the GKE, fleet, and team scope overview dashboards, calculated using information from [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) on your fleet clusters.

You can view fleet level metrics in the GKE and fleet overview dashboards. Team level metrics are available in the GKE and team overview dashboards.

### CPU metrics

  * **Total CPU utilization** : 
    * For the fleet level metrics, an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources across all clusters that are registered to a fleet. 
      * **Allocatable** : The amount of CPU allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/cpu/allocatable_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/cpu/allocatable_cores) metric.
      * **Used** : The amount of CPU used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
    * For the team **Monitoring** dashboard, an average of all points in time for a given time window where point in time is a ratio between requested and used resources across all namespaces that are associated with a team scope. 
      * **Requested** : The amount of CPU requested by all containers across all namespaces that are associated with a team scope. Calculated from the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric.
      * **Used** : The amount of CPU used by all containers across all namespaces that are associated with a team scope. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
  * **CPU utilization by fleet/team** : 
    * For the fleet level, the relationship between used, requested and allocated resources. 
      * **Used** : The amount of CPU used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
      * **Requested** : The amount of CPU requested by all containers across all clusters that are registered to a fleet. Calculated from the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric.
      * **Allocatable** : The amount of CPU allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/cpu/allocatable_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/cpu/allocatable_cores) metric.
    * For the team level, the relationship between resource limit, and used and requested resources. 
      * **Used** : The amount of CPU used by all containers across all namespaces that are associated with a team scope. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
      * **Requested** : The amount of CPU requested by all containers across all namespaces that are associated with a team scope. Calculated from the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric.
      * **Limit** : The maximum amount of CPU available to all containers across all namespaces that are associated with a team scope. Calculated from the [`container/cpu/limit_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/limit_cores) metric.
  * **Top CPU utilization by cluster** : Cluster list sorted by an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources for a particular cluster. 
    * **Allocatable** : The amount of CPU allocated to all nodes in a cluster. Calculated from the [`node/cpu/allocatable_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/cpu/allocatable_cores) metric.
    * **Used** : The amount of CPU used by all containers in a cluster. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
  * **Top CPU utilization by namespace** : Namespace list sorted by an average of all points in time for a given time window where point in time is a ratio between used and requested resources for a particular namespace. 
    * **Used** : The amount of CPU used by all containers in a namespace. Calculated from the [`container/cpu/core_usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/core_usage_time) metric.
    * **Requested** : The amount of CPU requested by all containers in a namespace. Calculated from the [`container/cpu/request_cores`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/cpu/request_cores) metric.



### Memory metrics

  * **Total memory utilization** : 
    * For the fleet level metrics, this refers to an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources across all clusters that belong to a fleet. 
      * **Allocatable** : The amount of memory allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/memory/allocatable_byte`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/memory/allocatable_bytes) metric.
      * **Used** : The amount of non-evictable memory used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
    * For the team level metrics, this refers to an average of all points in time for a given time window where point in time is a ratio between requested and used resources across all namespaces that belong to a team scope. 
      * **Requested** : The amount of memory requested by all containers across all namespaces that are associated with a scope. Calculated from the [`container/memory/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/request_bytes) metric.
      * **Used** : The amount of non-evictable memory used by all containers across all namespaces that are associated with a scope. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
  * **Memory utilization by fleet/team** : 
    * For the fleet level, the relationship between used, requested and allocated resources. 
      * **Used** : The amount of non-evictable memory used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
      * **Requested** : The amount of memory requested by all containers across all clusters that are registered to a fleet. Calculated from the [`container/memory/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/request_bytes) metric.
      * **Allocatable** : The amount of memory allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/memory/allocatable_byte`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/memory/allocatable_bytes) metric.
    * For the team level, the relationship between resource limit, and used and requested resources. 
      * **Used** : The amount of non-evictable memory used by all containers across all namespaces that are associated with a scope. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
      * **Requested** : The amount of memory requested by all containers across all namespaces that are associated with a scope. Calculated from the [`container/memory/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/request_bytes) metric.
      * **Limit** : The maximum amount of memory available to all containers across all namespaces that are associated with a scope. Calculated from the [`container/memory/limit_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/limit_bytes) metric.
  * **Top memory utilization by cluster** : Cluster list sorted by an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources for a particular cluster. 
    * **Allocatable** : The amount of memory allocated to all nodes in a cluster. Calculated from the [`node/memory/allocatable_byte`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/memory/allocatable_bytes) metric.
    * **Used** : The amount of non-evictable memory used by all containers in a cluster. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
  * **Top memory utilization by namespace** : Namespace list sorted by an average of all points in time for a given time window where point in time is a ratio between used and requested resources for a particular namespace. 
    * **Used** : The amount of non-evictable memory used by all containers in a namespace. Calculated from the [`container/memory/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/used_bytes) metric.
    * **Requested** : The amount of memory requested by all containers in a namespace. Calculated from the [`container/memory/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/memory/request_bytes) metric.



### Disk metrics

  * **Total disk utilization** : 
    * For the fleet level metrics, this refers to an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources across all clusters that belong to a fleet. 
      * **Allocatable** : The amount of local ephemeral storage allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/ephemeral_storage/allocatable_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/ephemeral_storage/allocatable_bytes) metric.
      * **Used** : The amount of local ephemeral storage used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
    * For the team level metrics, this refers to an average of all points in time for a given time window where point in time is a ratio between requested and used resources across all namespaces that belong to a team scope. 
      * **Requested** : The amount of local ephemeral storage requested by all containers across all namespaces that are associated with a scope. Calculated from the [`container/ephemeral_storage/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/request_bytes) metric.
      * **Used** : The amount of local ephemeral storage used by all containers across all namespaces that are associated with a scope. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
  * **Disk utilization by fleet/team** : 
    * For the fleet level, the relationship between used, requested and allocated resources. 
      * **Used** : The amount of local ephemeral storage used by all containers across all clusters that are registered to a fleet. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
      * **Requested** : The amount of local ephemeral storage requested by all containers across all clusters that are registered to a fleet. Calculated from the [`container/ephemeral_storage/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/request_bytes) metric.
      * **Allocatable** : The amount of local ephemeral storage allocated to all nodes across all clusters that are registered to a fleet. Calculated from the [`node/ephemeral_storage/allocatable_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/ephemeral_storage/allocatable_bytes) metric.
    * For the team level, the relationship between resource limit, and used and requested resources. 
      * **Used** : The amount of local ephemeral storage used by all containers across all namespaces that are associated with a scope. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
      * **Requested** : The amount of local ephemeral storage requested by all containers across all namespaces that are associated with a scope. Calculated from the [`container/ephemeral_storage/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/request_bytes) metric.
      * **Limit** : The maximum amount of local ephemeral storage available to all containers across all namespaces that are associated with a scope. Calculated from the [`container/ephemeral_storage/limit_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/limit_bytes) metric.
  * **Top disk utilization by cluster** : Cluster list sorted by an average of all points in time for a given time window where point in time is a ratio between allocatable and used resources for a particular cluster. 
    * **Allocatable** : The amount of local ephemeral storage allocated to all nodes in a cluster. Calculated from the [`node/ephemeral_storage/allocatable_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/node/ephemeral_storage/allocatable_bytes) metric.
    * **Used** : The amount of local ephemeral storage used by all containers in a cluster. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
  * **Top disk utilization by namespace** : Namespace list sorted by an average of all points in time for a given time window where point in time is a ratio between used and requested resources for a particular namespace. 
    * **Used** : The amount of local ephemeral storage used by all containers in a namespace. Calculated from the [`container/ephemeral_storage/used_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/used_bytes) metric.
    * **Requested** : The amount of local ephemeral storage requested by all containers in a namespace. Calculated from the [`container/ephemeral_storage/request_bytes`](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/ephemeral_storage/request_bytes) metric.



### Error distribution by namespace (team-level only)

Namespace list sorted by the highest number of error logs for a given time window. Logs are collected from [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

### Restart counts distribution by namespace (team-level only)

Namespace list sorted by the highest number of container restarts for a given time window. Calculated from the [container/restart_count](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes/container/restart_count) metric.

## Troubleshooting

### Metrics fail to load for new clusters

If you have created new clusters, depending on the time window you select, you might see `No Data` throughout the **Monitoring** dashboard, or you might see metrics. For example, if you created a cluster within the last hour, and select a time window of **1 hour** or **6 hours** , the dashboard might return some metrics for your workloads. However, if you select a time window of **1 day** or more, you might see `No data` displayed throughout the dashboard.

This is because Cloud Monitoring collects data in different periods (intervals) for different time windows. For time windows of **1 hour** and **6 hours** , data is collected in 1-minute periods. So if your cluster has existed for a few minutes, you will see metrics for these time windows.

For time windows of **1 day** and **1 week** , Cloud Monitoring collects data in 1-hour periods. If your cluster has existed for less than an hour, you might see no data for these time windows.

If you experience this error, check the dashboard after more time has elapsed since creating the new cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
