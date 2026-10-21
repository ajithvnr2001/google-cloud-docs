---
url: https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards/
title: Monitor clusters with custom dashboards or alerts \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:54.893110+00:00
---

# Monitor clusters with custom dashboards or alerts  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Monitor clusters with custom dashboards or alerts Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to monitor the performance and health of your Slurm clusters in Cluster Director by creating custom dashboards or alerting policies in Cloud Monitoring.

By using Cluster Director built-in metrics or [Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) for Slurm, you can do the following:

  * **Build custom Monitoring dashboards** : create dashboards with custom widgets based on your workload's needs. For example, you can monitor the percentage of nodes in a cluster that Slurm sets to a specific state.

  * **Create alerting policies** : receive notifications when a certain threshold is crossed or an event is triggered. For example, you can receive notifications when 10% or more nodes in your cluster are degraded.




Using the available metrics for Slurm in Cluster Director helps you identify bottlenecks, analyze resource consumption, and troubleshoot errors. To use prebuilt Monitoring dashboards to monitor the health and resource usage of your clusters, see instead [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards).

## Limitations

Prometheus includes the following system values that don't directly map to Slurm or Cluster Director configurations:

  * **`cluster`** : this value is always set to `__gce__` for all Compute Engine metrics, regardless of the cluster name or ID.

  * **`namespace`** : this value contains the numeric identifier of a Compute Engine instance.

  * **`job`** : this value represents the internal receiver name in the Ops Agent configuration, not your Slurm job ID.

  * **`instance`** : this value contains only the target IP address and port, not the name of a compute instance.




## Available Slurm metrics

In Cluster Director, you can use the following Slurm metrics to monitor your cluster:

  * **Built-in metrics** : the built-in metrics for Cluster Director exist under the `hypercomputecluster.googleapis.com/` domain and include the `cluster_id` label. Use built-in metrics to monitor resource usage for your cluster or its nodes.

**Important:** If you created your cluster before July 6, 2026, then you must contact your account team or the sales team to use Cluster Director built-in metrics. If you try to use these metrics without contacting Google, then you encounter errors.
  * **Prometheus metrics** : Prometheus metrics exist under the `prometheus.googleapis.com/` domain and include the `prometheus_target` label. Use Prometheus metrics to track detailed scheduler statistics, job queues, GPU hardware telemetry, and remote procedure call (RPC) volume.




### Built-in metrics

Based on your use case, you can use the following built-in metrics for Cluster Director to monitor your cluster:

  * Cluster metrics

  * Node metrics




#### Cluster metrics

The following metrics help you monitor your cluster:

Metric | Description  
---|---  
`hypercomputecluster.googleapis.com/slurm/gpus_utilization` | The ratio of allocated GPUs to the total number of GPUs in your cluster.  
`hypercomputecluster.googleapis.com/slurm/nodes_down` | The total number of compute nodes that Slurm set to the `down` state in your cluster.  
`hypercomputecluster.googleapis.com/slurm/cpus_alloc` | The total number of allocated virtual vCPUs in your cluster.  
`hypercomputecluster.googleapis.com/slurm/queue_failed` | The total number of failed jobs in the Slurm scheduler queue.  
  
#### Node metrics

The following metrics help you monitor the nodes in your cluster:

Metric | Description  
---|---  
`hypercomputecluster.googleapis.com/slurm/node_status` | The current Slurm state of a compute node. This metric returns the value of `1` when the Slurm state matches the query filter.  
`hypercomputecluster.googleapis.com/slurm/node_mem_alloc` | The total amount of physical memory that is allocated to a specific compute node.  
`hypercomputecluster.googleapis.com/slurm/node_cpu_alloc` | The total number of vCPUs that are allocated to a specific compute node.  
  
### Prometheus metrics

Based on your use case, you can use the following Prometheus metrics to monitor your cluster:

  * Job queue metrics

  * Node state metrics

  * Scheduler performance metrics

  * GPU and hardware metrics

  * RPC and user activity metrics

  * Reservation metrics




#### Job queue metrics

The following metrics help you track the status of your jobs in the queue:

Metric | Description  
---|---  
`slurm_queue_pending` | The number of pending jobs in the queue, labeled by user and reason for being pending.  
`slurm_queue_running` | The number of running jobs in your cluster partition.  
`slurm_queue_suspended` | The number of suspended jobs in your cluster partition.  
`slurm_queue_cancelled` | The number of cancelled jobs in your cluster partition.  
`slurm_queue_completing` | The number of jobs that are completing in your cluster partition.  
`slurm_queue_completed` | The number of completed jobs in your cluster partition.  
`slurm_queue_configuring` | The number of jobs that are configuring in your cluster partition.  
`slurm_queue_failed` | The number of failed jobs in your cluster partition.  
`slurm_queue_timeout` | The number of jobs that were stopped by timeout.  
`slurm_queue_preempted` | The number of jobs that were preempted by Compute Engine.  
`slurm_queue_node_fail` | The number of jobs that stopped due to host errors.  
`slurm_cores_pending` | The number of vCPU cores that have pending jobs in the queue.  
`slurm_cores_running` | The number of vCPU cores that are running jobs in your cluster partition.  
`slurm_cores_suspended` | The number of vCPU cores that have suspended jobs in your cluster partition.  
`slurm_cores_cancelled` | The number of vCPU cores that have cancelled jobs in your cluster partition.  
`slurm_cores_completing` | The number of vCPU cores that have jobs that are completing in the cluster.  
`slurm_cores_completed` | The number of vCPU cores that have completed jobs in your cluster partition.  
`slurm_cores_configuring` | The number of vCPU cores that have configuring jobs in your cluster partition.  
`slurm_cores_failed` | The number of vCPU cores that have failed jobs in your cluster partition.  
`slurm_cores_timeout` | The number of vCPU cores that have jobs that were stopped by timeout in your cluster partition.  
`slurm_cores_preempted` | The number of vCPU cores that have jobs that were stopped by preemption in your cluster partition.  
`slurm_cores_node_fail` | The number of vCPU cores that have jobs that were stopped due to host errors.  
  
#### Node state metrics

The following metrics help you understand the number of nodes in your cluster that have a specific Slurm state:

Metric | Description  
---|---  
`slurm_nodes_alloc` | The number of nodes that are in the `allocated` state.  
`slurm_nodes_comp` | The number of nodes that are in the `completing` state.  
`slurm_nodes_down` | The number of nodes that are in the `down` state.  
`slurm_nodes_drain` | The number of nodes that are in the `drain` state.  
`slurm_nodes_err` | The number of nodes that are in the `error` state.  
`slurm_nodes_fail` | The number of nodes that are in the `fail` state.  
`slurm_nodes_idle` | The number of nodes that are in the `idle` state.  
`slurm_nodes_maint` | The number of nodes that are in the `maintenance` state.  
`slurm_nodes_mix` | The number of nodes that are in the `mix` state.  
`slurm_nodes_resv` | The number of nodes that are reserved in your cluster partition.  
`slurm_nodes_other` | The number of nodes that have an unknown state.  
`slurm_nodes_planned` | The number of nodes that have a job scheduled.  
`slurm_nodes_total` | The total number of nodes in your cluster partition.  
  
#### Scheduler performance metrics

The following metrics help you understand statistics from the Slurm scheduler daemon:

Metric | Description  
---|---  
`slurm_scheduler_threads` | The number of active threads in the scheduler.  
`slurm_scheduler_queue_size` | The length of the main queue for the scheduler.  
`slurm_scheduler_dbd_queue_size` | The length of the [Slurm database daemon](https://slurm.schedmd.com/slurmdbd.html) agent queue.  
`slurm_scheduler_last_cycle` | The time that the scheduler took to complete the last cycle, in microseconds.  
`slurm_scheduler_mean_cycle` | The average time that the scheduler takes for a cycle, in microseconds.  
`slurm_scheduler_cycle_per_minute` | The number of cycles that the scheduler completes per minute.  
`slurm_scheduler_backfill_last_cycle` | The time that the scheduler took to complete the last backfill cycle, in microseconds.  
`slurm_scheduler_backfill_mean_cycle` | The average time that the scheduler takes for backfill cycles, in microseconds.  
`slurm_scheduler_backfill_depth_mean` | The average depth of searches in [backfill scheduling](https://slurm.schedmd.com/sched_config.html#backfill).  
`slurm_scheduler_backfilled_jobs_since_start_total` | The total number of jobs that Slurm started using backfill scheduling since Slurm started.  
`slurm_scheduler_backfilled_jobs_since_cycle_total` | The number of jobs that Slurm started using backfill scheduling since the last statistics reset.  
`slurm_scheduler_backfilled_heterogeneous_total` | The total number of components in jobs that use different types of resources (known as _heterogeneous jobs_) since Slurm started using backfill scheduling.  
  
#### GPU and hardware metrics

The following metrics help you understand the usage of your GPUs and the resource consumption for each node in your cluster:

Metric | Description  
---|---  
`slurm_gpus_alloc` | The number of GPUs that are allocated in your cluster partition.  
`slurm_gpus_idle` | The number of GPUs that are idle.  
`slurm_gpus_other` | The number of GPUs that are in other states.  
`slurm_gpus_total` | The total number of GPUs in your cluster partition.  
`slurm_gpus_utilization` | The overall utilization ratio of the GPUs in your cluster partition.  
`slurm_node_cpu_alloc` | The number of vCPU cores that are allocated on each node in your cluster partition.  
`slurm_node_cpu_idle` | The number of vCPU cores that are idle on each node in your cluster partition.  
`slurm_node_cpu_other` | The number of vCPU cores that are in other states on each node in your cluster partition.  
`slurm_node_cpu_total` | The total number of vCPU cores on each node in your cluster partition.  
`slurm_node_mem_alloc` | The amount of memory that is allocated on each node in your cluster partition, in megabytes (MB).  
`slurm_node_mem_total` | The total amount of memory available on each node in your cluster partition, in megabytes (MB).  
`slurm_node_status` | The status of each node in your cluster partition.  
  
#### RPC and user activity metrics

The following metrics help you understand the volume and latency of [remote procedure calls (RPCs)](https://en.wikipedia.org/wiki/Remote_procedure_call) in your cluster:

Metric | Description  
---|---  
`slurm_rpc_stats` | The number of RPCs that Slurm has processed, labeled by operation.  
`slurm_rpc_stats_avg_time` | The average time that Slurm takes for each RPC operation.  
`slurm_rpc_stats_total_time` | The total time that Slurm spent on RPC operations.  
`slurm_user_rpc_stats` | The number of RPCs that Slurm processed for each user.  
`slurm_user_rpc_stats_avg_time` | The average time that Slurm takes for RPCs for each user.  
`slurm_user_rpc_stats_total_time` | The total time that Slurm spent on RPCs for each user.  
`slurm_user_jobs_pending` | The number of pending jobs for each user.  
`slurm_user_jobs_running` | The number of running jobs for each user.  
`slurm_user_cpus_running` | The number of vCPU cores that are running jobs for each user.  
`slurm_user_jobs_suspended` | The number of suspended jobs for each user.  
  
#### Reservation metrics

The following metrics help you understand the reserved resources for your cluster, and related cluster information:

Metric | Description  
---|---  
`slurm_reservation_info` | The metadata about active reservations.  
`slurm_reservation_start_time_seconds` | The start time of the reservation, as a Unix timestamp.  
`slurm_reservation_end_time_seconds` | The end time of the reservation, as a Unix timestamp.  
`slurm_reservation_node_count` | The total number of nodes that Slurm has allocated to a reservation.  
`slurm_reservation_core_count` | The total number of vCPU cores that Slurm has allocated to a reservation.  
`slurm_account_fairshare` | The [fairshare score](https://slurm.schedmd.com/fair_tree.html) that Slurm calculated for an account.  
  
## Before you begin

When you access and use the Google Cloud console, you don't need to authenticate. You can automatically use Google Cloud services and APIs.

### Required roles

To get the permissions that you need to create Monitoring dashboards or alerting policies, ask your administrator to grant you the following IAM roles on the project: 

  * View the details of a cluster: [Hypercompute Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) 
  * View and edit Monitoring dashboards: [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create custom dashboards

You can display Prometheus metrics in a [widget](https://docs.cloud.google.com/monitoring/charts/dashboards#about_custom_dashboards) within a Monitoring dashboard. This approach lets you configure and display data so that it best fits the needs of your workload.

The following example shows how to create a widget in a new custom dashboard by using [promQL](https://docs.cloud.google.com/monitoring/promql#promql-cm-query). The example widget that you will create displays the percentage of nodes in a cluster that Slurm sets to a specific state, helping you verify how many nodes in your cluster are unused.

To create the example widget in a new custom dashboard, complete the following steps:

  1. In the Google Cloud console, go to the **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click **Create custom dashboard**. The **New dashboard** page opens.

  3. Click **Add widget**. The **Add widget** pane appears.

  4. In the **Visualization** section, click **Line**. The **Configure widget** pane appears.

  5. Click code **PromQL**. Then, to view the percentage of nodes with a state set to `allocated` in a cluster, enter the following query:
         
         ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"allocated|allocated#|allocated~"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
         

  6. Click add_box **Add query** , click code **PromQL** , and then, to view the percentage of nodes with a state set to `completing` in a cluster, enter the following query:
         
         ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"completing"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
         

  7. Repeat step 6 for the following queries:

     1. To view a percentage of nodes with a state set to `down` in a cluster, use the following query:
            
            ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"down|down\\*|down~"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
            

     2. To view a percentage of nodes with a state set to `drained` in a cluster, use the following query:
            
            ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"drained"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
            

     3. To view a percentage of nodes with a state set to `idle` in a cluster, use the following query:
            
            ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"idle|idle\\*|idle#|idle%|idle~"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
            

     4. To view a percentage of nodes with a state set to `mixed` in a cluster, use the following query:
            
            ((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"mixed|mixed#"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"})) * 100
            

  8. Click **Run query**.

  9. Click **Apply**.




For more information about creating custom dashboards in Monitoring, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

## Create alerting policies

You can create [alerting policies](https://docs.cloud.google.com/monitoring/alerts) and receive notifications when a metric in your cluster crosses a specific threshold. Alerting policies notify you when certain events occur in your cluster.

The following example shows how to create an alerting policy by using [promQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting). The policy notifies you when Slurm sets 10% or more nodes in your cluster to the `down` state. This state indicates that the nodes are degraded and must be repaired before you can run jobs on them again.

To create the example alerting policy, complete the following steps:

  1. In the Google Cloud console, go to the **Dashboards** page.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. Click add **Create policy**. The **Create alerting policy** page opens.

  3. In the **Policy configuration mode** pane that appears, do the following:

     1. Select **PromQL**.

     2. In the **Query editor** box, enter the following query:
            
            (((count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state","status"=~"down|down\\*|down~"}) or vector(0)) / count({"__name__"="hypercomputecluster.googleapis.com/slurm/node_state"}))) * 100 >= 10
            

     3. Click **Next**.

  4. In the **Configure alert trigger** pane that appears, do the following:

     1. In the **Retest window** list, select **5 minutes**.

     2. In the **Evaluation interval** list, select **1 minute**.

     3. In the **Condition name** field, enter a name for the condition that triggers the alert.

     4. Click **Next**.

  5. In the **Configure notifications and finalize alert** pane that appears, do the following:

     1. In the **Notification channels** list, select the channels where Google Cloud can notify you about the incident. If you don't have a notification channel in the list, then click **Manage notification channels** , and then follow the prompts to create one.

     2. In the **Notification subject line** field, enter the subject line for the message that Google Cloud sends you.

     3. In the **Name the alert policy** section, in the **Alert policy name** field, enter a name for your alerting policy.

     4. Click **Next**.

  6. Click **Save policy**.




For more information about creating alerting policies in Monitoring, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

## What's next

  * [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)

  * [View audit logs](https://docs.cloud.google.com/cluster-director/docs/monitor/view-audit-logs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
