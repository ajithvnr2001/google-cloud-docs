---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events/
title: Monitor maintenance events \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:02.390413+00:00
---

# Monitor maintenance events  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Monitor maintenance events Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to view host maintenance operations using the command line and using the GKE maintenance dashboard.

Viewing host maintenance operations can help you mitigate workload disruptions, especially for a long-running GKE cluster with workloads that could be disrupted due to periodic infrastructure interruptions.

For more details about host maintenance on GKE, see [Understand how to do host maintenance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## Monitor maintenance notifications

Before a VM has a scheduled [maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents), Compute Engine pushes notifications out to all its VMs. These notifications report the start of the Compute Engine maintenance window. When an upcoming maintenance is scheduled by the VM but isn't active, GKE adds `scheduled-maintenance-time` to the node label.

To monitor and detect upcoming maintenance events, you must view the notifications from both GKE and Compute Engine.

### View upcoming maintenance on Compute Engine

Compute Engine issues [notifications](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#overview_of_maintenance_notifications) when nodes and their underlying VMs are scheduled for disruptive [host events](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#monitor-maintenance-notifications), and when these events become active. The notifications include information about planned start time, the type of event, and other details.

### View upcoming maintenance on GKE

You can monitor upcoming maintenance events on GKE for specific machine types. The following table lists the supported machine types and the minimum required GKE version for each:

Machine type | Minimum GKE version  
---|---  
Machine types with GPUs or TPUs attached | 1.31.1-gke.2008000 or later  
H4D machine types | 1.32.6-gke.1060000 or later  
`c4a-highmem-96-metal` | 1.35.0-gke.2232000 or later  
Z3 machine types with more than 18 TiB of Titanium SSD | 1.32.4-gke.1376000 or later  
Z4D machine types with more than 42 TiB of attached Titanium SSD | 1.36.3-gke.1244000 or later  
Z4M machine types with more than 48 TiB of attached Titanium SSD, or any Z4M instances that use Cloud RDMA | 1.36.3-gke.1767000 or later  
  
To view upcoming maintenance events, you can do any of the following:

  * Query notifications at the node level. To do so, run the following command:
        
        kubectl get nodes -l cloud.google.com/scheduled-maintenance-time \
            -L cloud.google.com/scheduled-maintenance-time
        

The output is similar to the following:
        
        NAME                         STATUS    SCHEDULED-MAINTENANCE-TIME
        <gke-accelerator-node-name>  Ready     1733083200
        <gke-accelerator-node-name>  Ready     1733083200
        [...]
        

The `SCHEDULED-MAINTENANCE-TIME` column represents seconds, which are displayed in Unix epoch time format.

  * Query these notifications at the level of node metadata by [checking instances for a maintenance event notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-vms-for-maintenance-event).

  * For accelerator-optimized machine families that support [advanced maintenance](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event), you can access the `upcoming-maintenance` endpoint that provides information about scheduled and started maintenance events.




### View Kubernetes events for host maintenance

In GKE version 1.35 and later, Kubernetes events that track the host maintenance lifecycle are emitted. These Kubernetes events provide granular visibility into scheduled Compute Engine windows, ongoing operations, and edge cases like repairs or cancellations, allowing you to monitor disruptions directly within the Kubernetes environment.

You can view these events using standard Kubernetes tools or through Cloud Logging:

  1. To view recent maintenance events, use the following `kubectl` command:
         
         kubectl get events -n kube-system --field-selector involvedObject.kind=Node
         

Kubernetes events are retained in the cluster for 60 minutes, so this command outputs only these recent events per node.

  2. To view events in Cloud Logging, do the following:

     1. Go to the **Logs Explorer** page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

     2. Use the following query:
    
    resource.type="k8s_node"
    log_id("events")
    jsonPayload.metadata.annotations."maintenance.gke.io/category"="HostMaintenance"
    




#### Maintenance lifecycle events

Maintenance lifecycle events are emitted on Kubernetes node resources. The following table describes the events emitted by GKE during the Compute Engine host maintenance lifecycle:

Reason | Description  
---|---  
`MaintenanceWindowScheduled` | A Compute Engine host maintenance window has been scheduled for the node  
`MaintenanceWindowCancelled` | A Compute Engine host maintenance window has been cleared on the node  
`MaintenanceWindowRescheduled` | The previously scheduled Compute Engine host maintenance window has been moved and the maintenance start time updated  
`CustomerTriggeredMaintenance` | Compute Engine host maintenance was triggered manually through GKE  
`MaintenanceWindowStarted` | Compute Engine host maintenance has started  
`TerminateOnHostMaintenance` | Emitted when Compute Engine issues the termination signal (TERMINATE_ON_HOST_MAINTENANCE). If [graceful termination](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gke) is enabled, GKE cordons the node and schedules pod eviction (SIGTERM). Workloads receive a 5 to 60 minute notice ceiling depending on machine tier.  
`PodEvictionComplete` | All pods have been successfully evicted from the node  
`MaintenanceWindowCleared` | Compute Engine host maintenance is finished and the node is back to a ready state.  
  
#### Event payload information

If information about an upcoming maintenance events is available through Compute Engine, each event also includes a payload containing annotation data with the following information:

  * **Compute Engine window details:** Includes `windowStartTime`, `windowEndTime`, and `latestWindowStartTime`.
  * **Maintenance metadata:** The status of the maintenance cycle at the time of the event, the reason for maintenance (the reason can be listed as `SCHEDULED` or `UNSCHEDULED`), and whether the Compute Engine window can reschedule.
  * **Kubernetes metadata:** Includes Cluster_name, nodepool_name, and node_name.



## View of host maintenance operations in the GKE Maintenance Dashboard

The [GKE Maintenance Dashboard](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/blob/master/dashboards/google-kubernetes-engine-ai/README.md) provides a consolidated view of host maintenance operations. The dashboard gives comprehensive visibility into maintenance activities across the cluster, node pool, and node levels.

The dashboard is built on Observability Analytics. It displays maintenance cycles, node statuses, and historical downtime metrics.

## What's next

  * Learn how to [manage node disruption during host maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).
  * Learn how to [perform host maintenance for nodes running accelerator workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).
  * Learn about [GKE maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
