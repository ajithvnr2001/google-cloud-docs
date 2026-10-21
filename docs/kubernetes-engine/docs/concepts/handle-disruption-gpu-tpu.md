---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu/
title: Understand how to do host maintenance on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:23.346195+00:00
---

# Understand how to do host maintenance on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Understand how to do host maintenance on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

During the lifecycle of a long-running GKE cluster, periodic disruptions to workloads occur due to infrastructure interruptions that Google Cloud issues. These automatic events can occur to respond to scheduling decisions (preemption events), or node updates, which include GKE node auto-upgrades (maintenance events), or remediation of detected issues (termination events).

This document helps you understand what node disruption means in GKE and minimize disruption impact in your GKE nodes.

For details about monitoring maintenance notifications and events, see [Monitor maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events).

This document applies to the following machine types:

  * Machine types with GPUs or TPUs attached
  * [H4D machine types](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-hpc-workloads)
  * [Z3 machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_maintenance) with more than 18 TiB of attached Titanium SSD.
  * [Z4D machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) with more than 41 TiB of attached Titanium SSD.
  * Bare metal instances from the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series). For more information, see the [Requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations) section in the "Arm workloads on GKE" document.
  * Confidential GKE Nodes that use [machine types that don't support live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).



This document is for Platform admins and operators who manage the lifecycle of the underlying technical infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## What does infrastructure interruption mean in GKE?

Your GKE clusters manage the lifecycle of the GKE nodes. These nodes are provisioned on Compute Engine VMs, which periodically experience the following interruptions:

  * **Remediation of detected issues** (`TerminationEvent`): these events occur because Google Cloud detects an issue and interrupts your cluster infrastructure. `TerminationEvent` events don't support [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview). `TerminationEvent` events are triggered by the following issues:

    * [Auto repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) occurs when GKE repairs a node after repeated failed health checks.
    * [HostError](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) occurs when a hardware or software error on the physical machine causes the VM to stop.
**Note:** Maintenance events on the underlying Compute Engine are considered [automatic maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats) events. These events bypass GKE maintenance windows and exclusions, which only control GKE cluster maintenance and don't control maintenance on underlying services, such as Compute Engine.
  * **Maintenance or upgrade events** (`MaintenanceEvent`): these events occur when Google Cloud must interrupt a VM to perform maintenance. These events are triggered by the following maintenance tasks:

    * [Maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) occur when Google Cloud upgrades the underlying host.
    * Node updates, which include [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades), occur when GKE updates the configuration of the node, such as the GKE version.

For more information about how you and GKE manage changes during the lifecycle of a cluster, see [Types of changes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#types-of-changes).

  * **Response to scheduling decisions** (`PreemptionEvent`): these events occur when Google Cloud must preempt VMs to make capacity available for higher-priority resources. `PreemptionEvent` events can be any of the following:

    * **Eviction:** occurs when [preemptible](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption) or [Spot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) infrastructure is preempted to accommodate a higher-priority VM.
    * **Defragmentation:** occurs when GKE preempts a smaller TPU slice to accommodate a larger TPU slice. Defragmentation only occurs on TPU slices.



During the lifecycle of a long-running GKE cluster, the nodes might experience _periodic disruptions_ to workloads. When these disruptions affect the GKE nodes that run your workloads, GKE must restart both the running workloads and the underlying node.

### Why nodes that don't support live migration require interruption management

Most Compute Engine VMs, with some exceptions, have their [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) set to [live migrate](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#live_migrate), which means that running workloads typically experience little to no disruption. However, [certain classes of VMs](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations) don't support live migration, including the following machine types:

  * Machine types with attached [GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) and [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * H4D machine types.
  * The `c4a-highmem-96-metal` machine type.
  * Z3 machine types with more than 18 TiB of attached Titanium SSD.
  * Z4D machine types with more than 41 TiB of attached Titanium SSD.



For example, when a host event happens to the VM within a TPU slice, the entire slice gets interrupted and then rescheduled because all maintenance events are coordinated at the slice level. So if you create a TPU slice that has hundreds of VMs, all of those VMs will receive the same maintenance event schedule.

When a host event occurs, GKE [terminates](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#terminate_and_optionally_restart) the node and its Pods. If the Pods are deployed as part of a larger workload, like a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) or [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), GKE restarts the Pods on the affected node.

## Manage maintenance events

The rest of this document describes how to manage `MaintenanceEvent` disruptions.

Managing node disruption during _host maintenance_ events follows a three-stage workflow:

  1. **Detect scheduled host maintenance** : use GKE node labels, metadata endpoints, or logs.
  2. **Act on detected maintenance** : if maintenance is scheduled, evaluate your infrastructure and workloads and determine the best action for your use case. Take the appropriate action, such as letting the system handle the maintenance event automatically, manually starting host maintenance, or orchestrating maintenance strategies.
  3. **Verify the outcome of the maintenance event** : verify that the maintenance event was started correctly, either when Compute Engine starts the maintenance event on schedule or when you manually start it.



### Detect scheduled host maintenance

To monitor and detect upcoming maintenance events, you must view the notifications from both GKE and Compute Engine.

For details about monitoring maintenance notifications and events, see [Monitor maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events).

### Act on detected maintenance

If you see an upcoming scheduled maintenance notification for one or more nodes in your cluster, use the following decision tree to determine the best way to handle the disruption:

  1. **Automatic maintenance:** let Compute Engine start the maintenance event on schedule. Your VMs will automatically live migrate in the background with minimal or no disruption.

     1. If the host VM supports live migration, we recommend that you let the maintenance event happen automatically.
     2. If your workloads run on idle-flexible nodes, you can optimize maintenance timing automatically by configuring opportunistic maintenance. This triggers necessary updates only during periods of natural idle time.
  2. **Manually start a host maintenance event:** evaluate the following questions to determine the best way to manually handle the disruption:

     1. **Are your affected nodes single or isolated VMs?**

        * **Yes** (I'm running a single or isolated VM): 
          * If you don't require precise timing controls, _let Compute Engine start the maintenance event on schedule_ (default automatic).
          * If you need to avoid unexpected preemption, **manually start the host maintenance event** on the individual node at a convenient time, for example, during minor traffic windows.
        * **No** (I'm running a node pool of accelerators): choose one of the options in the next step.
     2. **Choose one of the following options based on your use case:**

        * **If your accelerator pool runs coupled AI/ML training tasks:** implement the [**parallel strategy**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators#parallel-strategy). Save your training state to a checkpoint, gracefully shut down the pool, and perform host updates and GKE cluster upgrades simultaneously before restarting.

        * **If your accelerator pool runs high-availability AI/ML serving or inference endpoints:** implement the [**rolling strategy**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators#rolling-strategy). Coordinate scheduled host maintenance and version upgrades in rolling batches within your zone or pool boundaries, using active replicas to protect SLAs.


**Important:** If you _don't_ start a host maintenance event, Compute Engine starts the scheduled maintenance event on its own. Starting in GKE version 1.33, the node is not tainted and Pods are not evicted when the maintenance window starts.

#### Manually start a host maintenance event on single or isolated VMs

You can manually start reschedulable maintenance when it fits your schedule, such as during times of low activity. To do this, apply the `cloud.google.com/perform-maintenance=true` label if the following conditions are met:

  * Compute Engine issues a [notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#overview_of_maintenance_notifications) about a scheduled maintenance event.
  * The underlying Compute Engine maintenance event is reschedulable. To check if the event is reschedulable, look for the `can_reschedule=TRUE` notification in the [event metadata](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-vms-for-maintenance-event). If the event is not reschedulable, setting the `cloud.google.com/perform-maintenance=true` label has no effect, and the maintenance happens at its originally scheduled time.



If the preceding conditions are met, on a node in the node pool, set the node label `cloud.google.com/perform-maintenance` to `true`. For example:
    
    
    kubectl label nodes <node-name> cloud.google.com/perform-maintenance=true
    

If _you_ start a maintenance event, GKE executes the following operations:

  1. Taints the node.
  2. Gracefully evicts Pods.
  3. Requests Compute Engine to start the maintenance event immediately, instead of waiting for the scheduled time.



### Verify the outcome of the maintenance event

After you detect an upcoming maintenance event and decide on the best course of action, you can verify the outcome of the maintenance event.

#### Compute Engine starts the maintenance event on schedule

When the maintenance event starts, a node might shut down one or more times with a short notification time before its imminent termination. In these cases, GKE makes a best effort to terminate workloads and gracefully evict Pods.

#### Scheduled maintenance starts

When scheduled maintenance starts, Compute Engine updates the metadata in the `http://metadata.google.internal/computeMetadata/v1/instance/attributes/` directory. Compute Engine updates the metadata labels as follows:

  * Sets `maintenance-event` to `TERMINATE_ON_HOST_MAINTENANCE`.
  * In `upcoming-maintenance`, sets `maintenance_status` to `ONGOING`.



GKE detects and handles the scheduled host maintenance event whether you trigger it manually or let GKE proceed automatically.

**Note:** In GKE versions earlier than 1.34.1-gke.2037001, GKE enabled automatic disruption handling for maintenance and TPU preemption by default. In GKE versions 1.34.1-gke.2037001 and later, and GKE version 1.33.5-gke.2469000 and later, this feature is disabled by default. To enable this feature, see Enable disruption handling for instructions on how to configure the required ConfigMap object.

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) reports the count of interruptions for a GKE node since the last sample (the metric is sampled every 60 seconds):

  * `kubernetes.io/node/interruption_count`



The `interruption_type` (such as `TerminationEvent`, `MaintenanceEvent`, or `PreemptionEvent`) and `interruption_reason` (like `HostError`, `Eviction`, or `AutoRepair`) fields can help provide the reason for why a node was interrupted.

To get a breakdown of the interruptions and their causes in TPU nodes in the clusters in your project, use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node"}[${__interval}]))
    

To only see the [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents), update the query to filter the `HW/SW Maintenance` value for the `interruption_reason`. Use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node", interruption_reason="HW/SW Maintenance"}[${__interval}]))
    

To see the interruption count aggregated by node pool, use the following PromQL query:
    
    
      sum by (node_pool_name,interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_pool_interruption_count{monitored_resource="k8s_node_pool", interruption_reason="HW/SW Maintenance", node_pool_name=NODE_POOL_NAME }[${__interval}]))
    

## Advanced configurations to minimize disruption

This section describes additional tools to configure your cluster and workloads to minimize disruption.

### Enable disruption handling

**Note:** This process applies to GKE versions 1.34.1-gke.2037001 and later, and version 1.33.5-gke.2469000 and later. In earlier versions, disruption handling is enabled by default.
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: gke-disruption-handling
      namespace: kube-system
    data:
      maintenance-experience.yaml: |
        gracefulTermination: true
    

To enable disruption handling, create a file called `maintenance-config.yaml` with this ConfigMap. Apply the ConfigMap onto the cluster with the following command:
    
    
    kubectl apply -f my-configmap.yaml
    

### Configure GKE to terminate your workloads gracefully

In this section, you configure GKE to manage your application lifecycle and minimize the disruption to your workload. If you don't configure a grace period, the grace period defaults to 30 seconds.

GKE makes a best effort to terminate these Pods gracefully and to execute the termination action that you define, for example, saving a training state. GKE sends a `SIGTERM` signal to Pods at the beginning of the grace period. If Pods don't exit by the end of the grace period, GKE sends a follow-up `SIGKILL` signal to any processes still running in any container in the Pod.

To configure the graceful termination period, set the termination grace period (seconds) in the `spec.terminationGracePeriodSeconds` field of your Pod manifest. For example, to get a notification time of 10 minutes, set the `spec.terminationGracePeriodSeconds`field in your Pod manifest to 600 seconds, as follows:
    
    
        spec:
          terminationGracePeriodSeconds: 600
    

We recommend that you set a termination grace period that is long enough for any ongoing tasks to finish within the notification timeframe. If your workload uses a ML framework such as MaxText, Pax, or JAX with [Orbax](https://docs.cloud.google.com/tpu/docs/autocheckpoint#autocheckpoint_with_orbax), the workloads can capture the shutdown `SIGTERM` signal and initiate a checkpointing process. To learn more, see [TPU Autocheckpoint](https://docs.cloud.google.com/tpu/docs/autocheckpoint).

**Note:** If you use a [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) (PDB), consider that Pods evicted by graceful node termination count towards the allowed evictions that are configured in the PDB. If you set a PDB, set a high enough `maxUnavailable` or a low enough `minAvailable` that allow GKE to complete the Pod eviction within the shutdown notification time window. Otherwise, when GKE evicts the Pods, it might need to violate the PDB's availability parameters to allow the shutdown to proceed.

#### Process of graceful termination

When a manually-started maintenance event begins, Compute Engine signals the impending machine shutdown by updating the `maintenance-event` metadata key. GKE starts graceful termination.

The following workflow shows how GKE executes graceful node termination when there is an impending node shutdown:

  1. Within 60 seconds, the following occurs: 
     1. The system components apply the `cloud.google.com/active-node-maintenance` node label set to `ONGOING` to indicate that workloads are being stopped.
     2. GKE applies the node taint to prevent new Pods from being scheduled on the node. The taint has the `cloud.google.com/impending-node-termination:NoSchedule` key. We recommend that you _don't_ modify your workloads to tolerate this taint due to the known termination that occurs.
  2. The maintenance-handler component begins to evict Pods by first evicting workload Pods, and then evicting system Pods (for example, kube-system).
  3. GKE sends a `SIGTERM` shutdown signal to workload Pods that are running on the node to alert them of an imminent shutdown. Pods can use this alert to finish any ongoing tasks. GKE makes a best effort to terminate these Pods gracefully.
  4. After eviction finishes, GKE updates the value of the `cloud.google.com/active-node-maintenance` label to `terminating` to indicate that the node is ready to terminate.



Afterwards, the node termination occurs and a replacement node is allocated. GKE clears the labels and taints when the process is finished. To increase the termination window for your workloads using GPUs or TPUs, complete the steps in the Manually start a host maintenance event section.

#### Verify the progress of an active graceful termination

You can filter the GKE logs by the following graceful termination events:

  * When the VM detects a disruption due to an impending node termination like Compute Engine host maintenance event, GKE sets the `cloud.google.com/active-node-maintenance` to `ONGOING` when workloads are being stopped, and to `terminating` when the workloads are finished and the node is ready to terminate.
  * When restricting new workloads from being scheduled, GKE applies the `cloud.google.com/impending-node-termination:NoSchedule` taint.



### Minimize interruption of running workloads with opportunistic maintenance

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can minimize the interruption of running workloads by automatically triggering maintenance when GKE detects that nodes with GPUs or TPUs are idle. To enable this feature, create a new node pool. You cannot enable opportunistic maintenance on an existing node pool.

#### Create a new node pool with opportunistic maintenance

The following command demonstrates how you can create a node pool with opportunistic maintenance enabled:
    
    
    gcloud beta container node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --accelerator ACCELERATOR_ARG \
        --machine-type MACHINE_TYPE \
        --num-nodes NODE_COUNT \
        --zone ZONE \
        --project=PROJECT_ID \
        --opportunistic-maintenance=node-idle-time=NODE_IDLE_TIME,min-nodes=MIN_NODES,window=WINDOW
    

Replace the following values:

  * `NODE_POOL_NAME`: the name of your GKE node pool.
  * `CLUSTER_NAME` : the name of your GKE cluster.
  * `NODE_IDLE_TIME` : the amount of time that a node can remain idle (that is, no accelerator-consuming workloads are running) before maintenance is triggered. The value represents duration in seconds, with up to nine fractional digits, and ends with the `s` character, for example: `80000s`.
  * `MIN_NODES` : the minimum number of nodes that must be available in a node pool. This option blocks maintenance if it causes the number of running nodes to go below this value, for example: `10`.
  * `WINDOW` : the window of time, in seconds, that opportunistic maintenance can run. The value ends with an `s` character. For example, a value of 14 days, or `1209600s`, implies that opportunistic maintenance can be run only in the two weeks before the scheduled maintenance date. A value of 28 days, or `2419200s`, allows opportunistic maintenance to run at any time during the scheduled maintenance window. This window for Compute Engine host maintenance is distinct from GKE maintenance windows, which determine when GKE cluster maintenance can occur and are configured separately.



#### Example configuration for opportunistic maintenance

Consider the following example. You have a node pool with four nodes and the opportunistic maintenance configuration is set to `--opportunistic-maintenance=node-idle-time=600s,window=2419200s,min-nodes=3`. In this scenario, the following occurs:

  * `node1` has a GPU workload running on it. This node is not idle, so it's skipped.
  * `node2` has been idle for 60 seconds. This node has not been idle for enough time, so it's skipped.
  * `node3` has been idle for 600 seconds. This node satisfies the idle requirement.
  * `node4` has been idle for 600 seconds. This node satisfies the idle requirement.



Both `node3` and `node4` satisfy the idle requirement. However, only one of these nodes will trigger opportunistic maintenance because the value of the `min-nodes` option is set to `3`.

#### Check the configuration and state of nodes with opportunistic maintenance

Check whether opportunistic maintenance is configured for a node by running the following command:
    
    
    kubectl describe node NODE_NAME | grep node.gke.io/opportunistic-config
    

Replace `NODE_NAME` with the name of the node that you want to check.

Check whether a node configured with opportunistic maintenance is undergoing maintenance:
    
    
    kubectl describe node NODE_NAME | grep node.gke.io/maintenance-state
    

If the node is triggered by opportunistic maintenance, `maintenance-state` annotation shows `opportunistic-triggered` as `true`.

#### Limitations

Be aware of the following limitations of opportunistic maintenance:

  * This feature can be used only with GPU and TPU node pools.
  * Opportunistic maintenance isn't compatible with cluster autoscaling because cluster autoscaler already scales down idle nodes.
  * For multi-host TPU node pools, the value of the `min-nodes-per-pool` setting should be `0` because these node pools are atomic.
  * The minimum supported GKE version is 1.33.3-gke.1118000.
  * Only planned maintenance that includes the `can_reschedule=TRUE` [notification](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event#get-notification) is supported.
  * To disable this feature, you must recreate the node pool without the respective flags. Or, you can manually disable the feature on specific nodes with `cloud.google.com/opportunistic-disable=true`.
  * In rare cases, maintenance might take a longer time to finish on a node. Customers using this feature might experience fewer available nodes, down to the value of the `min-nodes-per-pool` setting, for a period of time.



## What's next

  * To monitoring maintenance notifications and events, see [Monitor maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events).
  * Learn how to [deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).
  * Learn how to [deploy TPU workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot).
  * Learn about the [live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  * Learn how to [monitor maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
