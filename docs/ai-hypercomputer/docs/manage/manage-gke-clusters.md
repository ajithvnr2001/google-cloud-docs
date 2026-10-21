---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters/
title: Manage AI-optimized GKE clusters \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:04.872001+00:00
---

# Manage AI-optimized GKE clusters  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Manage AI-optimized GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page shows you how to manage AI-optimized Google Kubernetes Engine (GKE) clusters of A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machines, including the following common events relevant to GKE clusters and AI workloads:

  * Host maintenance
  * Cluster upgrades
  * Faulty host reporting

**Note:** Faulty host reporting is not supported for [General GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus).

## Manage host maintenance for AI workloads

GKE nodes run on Compute Engine instances that periodically experience [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) that can be disruptive to AI workloads. Since host events occur on the underlying Google Cloud infrastructure, they bypass GKE [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats). While most compute instances have their host maintenance policy set to [live migrate](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#live_migrate), which minimizes the disruption of workloads, GPUs and TPUs [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations). When these host events affect your GKE nodes running AI workloads, GKE has to terminate the node and the Pods running on the node. If the Pods are deployed as part of a larger workload like a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) or [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), GKE attempts to restart the Pods on the affected node.

To learn more about managing host maintenance of the underlying compute instances, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

### Monitor host maintenance events

For clusters running GKE version 1.31.1-gke.2008000 or later, you can view the scheduled start time of the host maintenance event in the following way. The start time is represented by Kubernetes node labels on the corresponding GKE node for all GPUs and TPUs.

For details, see [Monitor maintenance notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#monitor-notification).

With these node labels, you can do the following:

  * Manually start a host maintenance event
  * Use host maintenance event information while scheduling your workloads



### Manually start a host maintenance event

After Compute Engine issues a notification about a scheduled maintenance event, you can manually start maintenance at a time that aligns with your schedule. For example, you can choose to perform maintenance during periods of reduced activity.

If you don't manually start a host maintenance event, then Compute Engine will automatically complete regularly scheduled maintenance.

Follow the instructions to [Manually start a host maintenance event](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#manually-start-maintenance-event). Also, continue reading this section to learn the following:

  * [Configure GKE to terminate your workloads gracefully](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gke)
  * [Process of graceful termination](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#process-termination)
  * [Monitor the progress of an active graceful termination](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#monitor-termination)



### Use host maintenance information while scheduling your workloads

You can use the maintenance information surfaced through GKE node labels along with [node affinity and anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) to minimize disruption to your workloads.

See the following sections for examples of how to use this information.

#### Schedule Pods to nodes that have no future scheduled maintenance events

You can instruct GKE to only schedule Pods to nodes that have no future scheduled maintenance events, such as with the following snippet:
    
    
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/scheduled-maintenance-time
                operator: DoesNotExist
    

#### Schedule Pods to nodes that have maintenance scheduled after a certain date

You can instruct GKE to only schedule Pods to nodes that have maintenance scheduled after a certain date by providing the Unix epoch time:
    
    
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: cloud.google.com/scheduled-maintenance-time
                operator: Gt
                values:
                - 1733296000
    

## Manage GKE cluster upgrades for AI workloads

AI workloads are sensitive to disruption.

During the lifecycle of a GKE cluster, AI workloads must be prepared for disruption to both the underlying compute instances, as well as the GKE cluster itself:

  * **Host maintenance** : To manage host maintenance of the underlying compute instances, see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu). This is also described in the previous sections.
  * **Cluster upgrades** : To manage disruption from [cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades), you can use the following tools: 
    * [Maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows): Schedule when GKE can perform cluster upgrades and other types of [cluster operations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#what-changes-maintenance-policies).
    * [Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions): Prevent cluster upgrades and other types of cluster operations during a specific time period.



We recommend that you keep your cluster enrolled in a release channel. GKE clusters, by default, are enrolled in the Regular release channel. To learn more about the benefits of release channels, see the [Comparison between clusters enrolled and not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#comparison-table-no-channel).

With release channels, you get access to more features, including additional [maintenance exclusion scopes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude). We recommend the "no minor or node upgrades" scope for AI workloads.

## Report faulty hosts through GKE

This section outlines how, through GKE, you can report a faulty host that has compute instances provisioned by using the [reservation-bound provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound). If you want to report a faulty host for a node that was provisioned by using the flex-start provisioning model ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), then contact your account team instead.

If you observe GPU memory or Xid errors on a node and want to verify whether manual recovery measures such as triggering a guest OS reboot (`kubectl label nodes <NODE_NAME> cloud.google.com/perform-reboot=true`) can resolve the issue before you report the host as faulty, see [Review Xid messages](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#review-xid-messages).

**Caution** : Reporting a faulty host is a disruptive action that stops your VM. Before you report a host, thoroughly investigate your environment to identify the root cause of the issue. Only report the host as faulty if you have no alternatives to resolve your issue. 

A [_host_](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#node) is a single physical server machine in the data center running a compute instance which hosts your GKE node. You can report faulty hosts by applying a `fault-behavior` node label to the affected GKE node. After you apply the node label to a particular GKE node, GKE does the following steps:

  1. Gracefully evicts workloads from the node.
  2. Prevents new Pods from being scheduled on the node.
  3. Calls the API on the compute instance to mark the host as faulty.
  4. Waits for the compute instance to be brought back up on a healthy host machine. For reservations that use the [_all capacity_ reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode), Compute Engine brings back the compute instance on the same node after the repair operation completes.
  5. Removes the taint and the `fault-behavior` label from the node.



After this, the node will be ready to serve workloads again.

### Requirements

To report a faulty host, your GKE node must meet the following requirements:

  * You must be running GKE patch version 1.32.3-gke.1057001 or later.
  * You must be running one of the following [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus): A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs).
  * You must be running your GKE nodes on a compute instance that is [reservation-bound](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * Your GKE node must be in a `RUNNING` state. If you try to report a faulty host after deleting the compute instance, an error message is returned, and the host machine won't be marked as faulty.
  * You might be rate-limited on the number of calls to this API per reservation per month based on an evaluation of the health of your blocks. Rate-limits don't apply if your reservation uses the [_all capacity_ reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).



### Report a faulty host

**Note:** The local SSD data will be deleted on successful invocation of the API as the compute instance moves hosts. We recommend that you back up your local SSD data prior to reporting a faulty node through GKE.

To report a faulty host:

  1. Use the [GKE observability tools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics), your own monitoring tools, or logs to identify the GKE nodes that are experiencing performance issues. Save the `NODE_NAME`.

  2. Report the node as faulty using the following command. You can provide a reason, and, with later versions, a description:

**Important:** After you report a host as faulty, don't send additional requests until the operation completes. GKE rejects additional requests while the operation is in progress.
         
         kubectl patch node NODE_NAME --type merge -p '{
             "metadata": {
               "labels": {
                 "cloud.google.com/fault-behavior": "FAULT_REASON"
               },
               "annotations": {
                 "cloud.google.com/fault-description": "FAULT_DESCRIPTION"
               }
             }
           }'
         

Modify the command as follows:

     * Replace `NODE_NAME` with the name of the faulty node.
     * Replace `FAULT_REASON` with the appropriate fault reason using one or more of the following values: 
       * `PERFORMANCE`: use this value if GPUs on a compute instance are performing slower than other GPUs in the cluster and you don't see any XID errors in the logs, and none of the other usual failure patterns such as silent data corruption are detected.
       * `SDC`: use this value for silent data corruption, if you see data corruption but no system crash. This data corruption can be caused by CPU defects, software bugs such as use-after-free or memory stomping, kernel issues, or other defects. Most often, this term is used to refer to hardware-induced defects.
       * `XID`: use this value if you identified an unrecoverable GPU error with an XID for a compute instance.
       * `unspecified`: use this value if you are not sure what behavior is causing the issue with your compute instance. This is the default value. However, we recommend specifying one of the other values, if applicable.
     * Adjust the `annotations` block based on your GKE cluster's control plane version: 
       * **1.35.6-gke.1017000 or later, or 1.36.0-gke.3251000 or later** : keep the annotations block and replace `FAULT_DESCRIPTION` with a text description of the observed fault. This can include the XID error code, symptoms, or timestamps. This description is forwarded to Compute Engine to assist with repair diagnostics and is automatically removed from the node after the operation completes. For example: `GPU XID 48 observed on device nvidia0 at 2026-06-10T10:30:00Z`.
       * **Earlier versions** : remove the entire `annotations` block from the command. The `fault-description` field is not forwarded to Compute Engine in these versions and isn't automatically removed from the node. Instead, contact your account team or [Cloud Customer Care](https://docs.cloud.google.com/support/docs/overview) to provide fault details.

After you report a faulty host for a node, the time when the node restarts varies based on the [](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode) reservation operational mode that is specified in the reservation that the node uses. To verify the reservation operational mode for a reservation, [view the `reservationOperationalMode` field in the reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation). The following table summarizes the faulty host process for the two available reservation operational modes: _all capacity mode_ and _managed mode_.  | All capacity mode (`ALL_CAPACITY`) | Managed mode (`HIGHLY_AVAILABLE_CAPACITY`)  
---|---|---  
Supported machine types | A4X Max and A4X | A4, A3 Ultra, A3 Mega, and A3 High  
Faulty host report API rate limiting | No rate limits apply. | Calls to the API may be rate-limited.  
Faulty host report process |  When you report a faulty host for a node that runs in the all capacity mode, the following occurs:

  1. **Evict Pods** : After the label is applied to the faulty node, GKE taints the node to block scheduling new Pods. GKE also starts to gracefully evict the running Pods on the node. GKE respects the [Pod Disruption Budgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and the `spec.terminationGracePeriodSeconds` field of your Pod manifests. For more details, see [ Configure GKE to terminate your workloads gracefully](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gke).
  2. **Report and repair the faulty host** : GKE automatically reports and repairs the faulty host by calling the Compute Engine API, which results in a [sequence of operations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#review-operations) that usually takes 10-12 minutes to report the faulty host and then can take 3-14 days, or even longer at times, to repair the host.
  3. **Restart the instance** : After the host repair operation _completes_ (usually 3-14 days), one of the following occurs:
     * If the instance is in the `REPAIRING` state and the resources are available when the repair completes, then Compute Engine automatically restarts the instance on the repaired host.
     * Otherwise, if the instance is in the `TERMINATED` state or if resources aren't available when the repair completes, then the instance state stays in or changes to `TERMINATED`. You must [manually restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, restarting the instance might fail if resources aren't available when you restart the instance; for example, this can happen if other instances are already using the repaired host.

|  When you report a faulty host for a node that runs in the managed mode, the following occurs:

  1. **Evict Pods** : After the label is applied to the faulty node, GKE taints the node to block scheduling new Pods. GKE also starts to gracefully evict the running Pods on the node. GKE respects the [Pod Disruption Budgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and the `spec.terminationGracePeriodSeconds` field of your Pod manifests. For more details, see [ Configure GKE to terminate your workloads gracefully](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gke).
  2. **Report and start repairing the faulty host** : GKE automatically reports and repairs the faulty host by calling the Compute Engine API, which results in a [sequence of operations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#review-operations) that usually takes 10-12 minutes to report the faulty host and then can take 3-14 days, or even longer at times, to repair the host.
  3. **Migrate and restart the instance** : After the host repair operation _starts_ (usually 10-12 minutes), Compute Engine attempts to reserve one more host to replace your reported faulty host in your reserved capacity. If Compute Engine finds a healthy host—if it successfully replaces the faulty host or otherwise finds a matching healthy host in your reserved capacity—then Compute Engine migrates the instance to that host. Then, restarting the instance happens through one of the following: 
     * If the instance is in the `REPAIRING` state and resources are available before or when the repair completes, then Compute Engine automatically restarts the instance on a healthy host.
     * Otherwise, if the instance is in the `TERMINATED` state or if resources aren't available before or when the repair completes, then the instance state stays in or changes to `TERMINATED`. You must [manually restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) when you want it to run. However, restarting the instance might fail if resources aren't available when you restart the instance; for example, this can happen if other instances are already using the repaired host.

  
  
### Monitor the operation progress

You can monitor the progress of GKE's operation using the `cloud.google.com/report-and-replace-status` node label on your GKE node, which has one of the following values:

  * `PodsEvicted`: GKE has finished evicting Pods from the affected node.
  * `OperationRUNNING`: the operation to report the fault host is running.
  * `OperationDONE`: the underlying host has been reported as faulty and the GKE node is ready to be moved to a new host.
  * `OperationFAILED`: the API on the compute instance failed due to quota limits or other infrastructure issues. To understand the error, see [Troubleshoot report faulty host API errors](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api). To learn how to recover, see Handle report-and-replace failures.
  * `Error`: the API call failed because the request did not meet one of the requirements described in the previous section.



You can also view the `node.gke.io/report-and-replace-operation` node label to view the Compute Engine operation ID to monitor the [status of the operation](https://console.cloud.google.com/compute/operations).

You can view both these node labels using the following command:
    
    
      kubectl get nodes NODE_NAME \
      -L cloud.google.com/report-and-replace-status,node.gke.io/report-and-replace-operation
    

If an API error occurs, GKE sets the `cloud.google.com/report-and-replace-status` node label to `Error`. If an operation failure occurs, GKE sets the label to `OperationFAILED`. In both cases, GKE removes the `cloud.google.com/fault-behavior` node label. Additionally, in GKE version 1.35.6-gke.1256000 or later, or 1.36.0-gke.4060000 or later, GKE applies a `cloud.google.com/report-and-replace-failed:NoSchedule` taint to the node. This taint prevents new Pods from being scheduled on the node, which ensures that workloads aren't placed on a node with a potentially faulty host. To learn more, see Handle report-and-replace failures.

To learn how to track the detailed status of a report faulty host operation, see [Review report faulty host operations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#review-operations).

### Handle report-and-replace failures

When a report-and-replace operation fails, GKE applies the `cloud.google.com/report-and-replace-failed:NoSchedule` taint to the affected node. This taint keeps the node cordoned so that no new workloads are scheduled on it while the underlying host might still be faulty.

#### Check for the failure taint

To check whether a node has the report-and-replace failure taint, run the following command:
    
    
      kubectl describe node NODE_NAME | grep "report-and-replace-failed"
    

#### Recover from a report-and-replace failure

To recover from a report-and-replace failure, do one of the following:

  * **Retry the operation** by re-applying the `cloud.google.com/fault-behavior` label to the node. If the retry succeeds, GKE automatically removes the `cloud.google.com/report-and-replace-failed:NoSchedule` taint:
        
        kubectl label node NODE_NAME cloud.google.com/fault-behavior=FAULT_REASON
        

  * **Manually remove the taint** if you've determined that the node is healthy or you want to return it to service:
        
        kubectl taint nodes NODE_NAME cloud.google.com/report-and-replace-failed:NoSchedule-
        




## What's next

  * Learn how to [schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).

  * Learn how to [optimize cluster networking by using NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview).

  * Learn how to [troubleshoot report faulty host API errors](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
