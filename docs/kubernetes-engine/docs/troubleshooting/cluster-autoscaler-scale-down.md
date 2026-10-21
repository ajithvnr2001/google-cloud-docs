---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down/
title: Troubleshoot cluster autoscaler not scaling down \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:00:42.980372+00:00
---

# Troubleshoot cluster autoscaler not scaling down  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot cluster autoscaler not scaling down Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If your Google Kubernetes Engine (GKE) nodes aren't scaling down as expected, it's often because the cluster autoscaler is failing to remove them, which leads to unnecessary costs and inefficient resource use.

Use this page to diagnose and resolve common problems that block cluster autoscaler scale-down actions. Troubleshooting these issues helps ensure that your cluster operates cost-effectively and adapts to workload changes.

This information is important for Platform admins and operators who are responsible for cluster efficiency, cost optimization, and resource management. Application developers might also need this information if their workload configurations (like `PodDisruptionBudgets` or node selectors) are unintentionally preventing nodes from being removed. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand when cluster autoscaler scales down your nodes

Before you proceed to the troubleshooting steps, it can be helpful to understand when cluster autoscaler would try to scale down your nodes. It could be the case that cluster autoscaler didn't scale down because it didn't need to.

Cluster autoscaler determines if a node is underutilized and eligible for scale down by calculating a _utilization factor_. The utilization factor is calculated by dividing the vCPU and memory requested by the Pods on the node by the allocatable vCPU and memory on the node.

Every 10 seconds cluster autoscaler checks the utilization factor of your nodes to see if it's below the required threshold. If you're using a `balanced` [autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles), the utilization factor threshold is 0.5. If you're using the `optimize-utilization` profile, the utilization factor varies. When the utilization factor is less than the required threshold for both vCPU and memory, cluster autoscaler considers the node underutilized.

When a node is underutilized, cluster autoscaler marks the node for removal and monitors the node for the next 10 minutes to make sure the utilization factor stays under the required threshold. If the node is still underutilized after 10 minutes, cluster autoscaler should remove the node.

### Example: Utilization factor calculation

You have a cluster with cluster autoscaler enabled and you're using the `balanced` autoscaling profile. A node on this cluster is provisioned with the `e2-standard-4` machine type, which offers 4 vCPUs and 16 GB of memory. A Pod on this node requests 0.5 vCPU and 10 GB of memory, so cluster autoscaler calculates the following utilization factors:

  * **vCPU utilization factor** : 0.5 vCPU / 4 vCPUs = 0.125
  * **Memory utilization factor** : 10 GB / 16 GB = 0.625



In this scenario, cluster autoscaler would _not_ consider this node underutilized because the memory utilization factor (0.625) exceeds the threshold of 0.5. Even though the vCPU utilization is low, the higher memory usage prevents scale down to ensure sufficient resources remain available for the Pod's workload.

## Check if the issue is caused by a limitation

If you observe a cluster with low utilization for more than 10 minutes and it's not scaling down, make sure your issue isn't caused by one of the [limitations for the cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations).

## View errors

If your issue wasn't caused by a limitation, you can often diagnose the cause by viewing error messages:

  * If you've already seen an error message, see the error messages table for advice on resolving the error.

  * If you haven't seen a message yet, use one of the following options:

    * **Issues less than 72 hours old** : View error notifications in the Google Cloud console.
    * **Issues over 72 hours old** : View errors in events in Cloud Logging.



### View errors in notifications

If the issue you observed happened less than 72 hours ago, view notifications about errors in the Google Cloud console. These notifications provide valuable insights into why cluster autoscaler didn't scale down and offer advice on how to resolve the error and view relevant logs for further investigation.

To view the notifications in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Review the **Notifications** column. The following notifications are associated with scale down issues:

     * `Can't scale down nodes`
     * `Scale down blocked by pod`
  3. Click the relevant notification to see a pane with details about what caused the issue and recommended actions to resolve it.

  4. Optional: To view the logs for this event, click **Logs**. This action takes you to Logs Explorer with a pre-populated query to help you further investigate the scaling event. To learn more about how scale down events work, see [View cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility).




If you're still experiencing issues after reviewing the advice in the notification, consult the error messages tables for further help.

### View errors in events

If the issue you observed happened over 72 hours ago, view events in Cloud Logging. When there has been an error, it's often recorded in an event.

To view cluster autoscaler logs in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the name of the cluster that you want to investigate to view its **Cluster details** page.

  3. On the **Cluster details** page, click the **Logs** tab.

  4. On the **Logs** tab, click the **Autoscaler Logs** tab to view the logs.

  5. Optional: To apply more advanced filters to narrow the results, click the button with the arrow on the right side of the page to view the logs in Logs Explorer.




To learn more about scale down events work, see [View cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility). For one example of how to use Cloud Logging, see the following troubleshooting example.

#### Example: Troubleshoot an issue over 72 hours old

The following example shows you how you might investigate and resolve an issue with a cluster not scaling down.

**Scenario** :

One week ago, you were looking at the [GKE dashboard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard) and noticed that your cluster has only utilized only 10% of its CPU and memory. Despite the low utilization, cluster autoscaler didn't delete the node as you expected. When you look at the dashboard now, the issue seems to have been resolved, but you decide to find out what happened so that you can avoid it happening again.

**Investigation** :

  1. Because the issue happened over 72 hours ago, you investigate the issue using Cloud Logging instead of looking at the notification messages.
  2. In Cloud Logging, you find the logging details for cluster autoscaler events, as described in View errors in events.
  3. You search for [`scaleDown` events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#scaledown-event) that contain the nodes belonging to the cluster that you're investigating in the `nodesToBeRemoved` field. You could filter the log entries, including filtering by a particular JSON field value. Learn more in [Advanced logs queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries).
  4. You don't find any `scaleDown` events. However, if you did find a `scaleDown` event, you could search for an [`eventResult`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#eventresult-event) event that contains the associated `eventId`. You could then search for an error in the `errorMsg` field.
  5. You decide to continue your investigation by searching for [`noScaleDown`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#noscaledown-event) events that have the node that you're investigating in the nodes field.

You find a `noScaleDown` event that contains a reason for your node not scaling down. The message ID is `"no.scale.down.node.pod.not.backed.by.controller"` and there's a single parameter: `"test-single-pod"`.




**Resolution:**

You consult the error messages table, and discover this message means that the Pod is blocking scale down because it's not backed by a controller. You find out that one solution is to add a `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` annotation to the Pod. You investigate `test-single-pod` and see that a colleague added the annotation and after applying the annotation, cluster autoscaler scaled down the cluster correctly. You decide to add the annotation to all other Pods where it's safe to do so to avoid the issue from happening again.

## Resolve scale down errors

After you have identified your error, use the following tables to help you understand what caused the error and how to resolve it.

### ScaleDown errors

You can find error event messages for `scaleDown` events in the corresponding `eventResult` event, in the `resultInfo.results[].errorMsg` field.

Event message | Details | Parameter | Mitigation  
---|---|---|---  
`"scale.down.error.failed.to.mark.to.be.deleted"` | A node couldn't be marked for deletion. | Failing node name. | This message should be transient. If it persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
`"scale.down.error.failed.to.evict.pods"` | Cluster autoscaler can't scale down because some of the Pods couldn't be evicted from a node. | Failing node name. | Review the PodDisruptionBudget for the Pod and make sure the rules allow for eviction of application replicas when acceptable. To learn more, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) in the Kubernetes documentation.  
`"scale.down.error.failed.to.delete.node.min.size.reached"` | Cluster autoscaler can't scale down because a node couldn't be deleted due to the cluster already being at minimal size. | Failing node name. | Review the minimum value set for node pool autoscaling and [adjust the settings](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#resizing_a_node_pool) as necessary. To learn more, see the [Error: Nodes in the cluster have reached minimum size](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#nodes-minimum-size).  
  
### Reasons for a noScaleDown event

A `noScaleDown` event is periodically emitted when there are nodes which are blocked from being deleted by cluster autoscaler. `noScaleDown` events are best-effort, and don't cover all possible cases.

#### NoScaleDown top-level reasons

Top-level reason messages for `noScaleDown` events appear in the `noDecisionStatus.noScaleDown.reason` field. The message contains a top-level reason why cluster autoscaler can't scale the cluster down.

Event message | Details | Mitigation  
---|---|---  
`"no.scale.down.in.backoff"` | Cluster autoscaler can't scale down because scaling down is in a backoff period (temporarily blocked). | This message should be transient, and can occur when there has been a recent scale up event. If the message persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.  
`"no.scale.down.in.progress"` | Cluster autoscaler can't scale down because a previous scale down was still in progress. | This message should be transient, as the Pod will eventually be removed. If this message occurs frequently, review the termination grace period for the Pods blocking scale down. To speed up the resolution, you can also delete the Pod if it's no longer needed.  
  
#### NoScaleDown node-level reasons

Node-level reason messages for `noScaleDown` events appear in the `noDecisionStatus.noScaleDown.nodes[].reason field`. The message contains a reason why cluster autoscaler can't remove a particular node.

Event message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.down.node.scale.down.disabled.annotation"` | Cluster autoscaler can't remove a node from the node pool because the node is annotated with `cluster-autoscaler.kubernetes.io/scale-down-disabled: true`.  | N/A | Cluster autoscaler skips nodes with this annotation without considering their utilization and this message is logged regardless of the node's utilization factor. If you want cluster autoscaler to scale down these nodes, remove the annotation.  
`"no.scale.down.node.node.group.min.size.reached"` |  Cluster autoscaler can't scale down when node group size has exceeded minimum size limit.  This happens because removing nodes would violate the cluster-wide minimal resource limits defined in your node auto-provisioning settings. | N/A | Review the minimum value set for node pool autoscaling. If you want cluster autoscaler to scale down this node, [adjust the minimum value](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#resizing_a_node_pool).  
`"no.scale.down.node.minimal.resource.limits.exceeded"` | Cluster autoscaler can't scale down nodes because it would violate cluster-wide minimal resource limits. These are the resource limits set for node auto-provisioning. | N/A | Review your limits for memory and vCPU and, if you want cluster autoscaler to scale down this node, decrease[ the limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable).  
`"no.scale.down.node.no.place.to.move.pods"` | Cluster autoscaler can't scale down because there's no place to move Pods. | N/A | If you expect that the Pod should be rescheduled, review the scheduling requirements of the Pods on the underutilized node to determine if they can be moved to another node in the cluster. To learn more, see the [Error: No place to move Pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#no-place-to-move-pods).  
`"no.scale.down.node.pod.not.backed.by.controller"` | Pod is blocking scale down because it's not backed by a controller. Specifically, the cluster autoscaler is unable to scale down an underutilized node due to a Pod that lacks a recognized controller. Allowable controllers include ReplicationController, DaemonSet, Job, StatefulSet, or ReplicaSet. | Name of the blocking Pod. | Set the annotation `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` for the Pod or define an acceptable controller.  
`"no.scale.down.node.pod.not.safe.to.evict.annotation"` | A Pod on the node has the `safe-to-evict=false` annotation. | Name of the blocking Pod. | If the Pod can be safely evicted, edit the manifest of the Pod and update the annotation to `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"`.  
`"no.scale.down.node.pod.kube.system.unmovable"` | Pod is blocking scale down because it's a non-DaemonSet, non-mirrored, Pod without a PodDisruptionBudget in the `kube-system` namespace. | Name of the blocking Pod. | In GKE versions earlier than 1.32.4-gke.1236000, the cluster autoscaler doesn't remove Pods in the `kube-system` namespace. Starting with version 1.32.4-gke.1236000, the cluster autoscaler considers these Pods for removal after they have been created for one hour. To resolve this issue, either add a PodDisruptionBudget for the `kube-system` Pods or use a combination of node pools taints and tolerations to separate `kube-system` Pods from your application Pods. To learn more, see [Error: kube-system Pod unmoveable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#kube-system-unmoveable).  
`"no.scale.down.node.pod.not.enough.pdb"` | Pod is blocking scale down because it doesn't have enough PodDisruptionBudget. | Name of the blocking Pod. | Review the PodDisruptionBudget for the Pod and consider making it less restrictive. To learn more, see [Error: Not enough PodDisruptionBudget](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down#not-enough-pdb).  
`"no.scale.down.node.pod.controller.not.found"` | Pod is blocking scale down because its controller (for example, a Deployment or ReplicaSet) can't be found. | N/A | To determine what actions were taken that left the Pod running after its controller was removed, review the logs. To resolve this issue, manually delete the Pod.  
`"no.scale.down.node.pod.unexpected.error"` | Pod is blocking scale down because of an unexpected error. | N/A | The root cause of this error is unknown. [Contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
## Conduct further investigation

The following sections provide guidance on how to use Logs Explorer and `gcpdiag` to gain additional insights into your errors.

### Investigate errors in Logs Explorer

If you want to further investigate your error message, you can view logs specific to your error:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the [query pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-viewer-interface), enter the following query:
         
         resource.type="k8s_cluster"
         log_id("container.googleapis.com/cluster-autoscaler-visibility")
         jsonPayload.resultInfo.results.errorMsg.messageId="ERROR_MESSAGE"
         

Replace `ERROR_MESSAGE` with the message that you want to investigate. For example, `scale.down.error.failed.to.delete.node.min.size.reached`.

  3. Click **Run query**.




### Debug some errors with gcpdiag

`gcpdiag` is an open source tool created with support from Google Cloud technical engineers. It isn't an officially supported Google Cloud product.

If you've experienced one of the following error messages, you can use [`gcpdiag`](https://gcpdiag.dev/runbook/diagnostic-trees/gke/cluster-autoscaler/#parameters) to help troubleshoot the issue:

  * `scale.down.error.failed.to.evict.pods`
  * `no.scale.down.node.node.group.min.size.reached`



For a list and description of all `gcpdiag` tool flags, see the [`gcpdiag` usage instructions](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#usage).

## Resolve complex scale down errors

The following sections offer guidance on resolving errors where the mitigations involve multiple steps and errors that don't have a cluster autoscaler event message associated with them.

### Error: Nodes in the cluster have reached minimum size

If you see the following errors, cluster autoscaler couldn't delete a node because the number of nodes in the cluster was already at the minimum size:

### Notification

> Scale down of underutilized node is blocked because cluster autoscaler minimal resource limits are reached.

### Event
    
    
    "scale.down.error.failed.to.delete.node.min.size.reached"
    

To resolve this issue, review and update the minimum limits for autoscaling:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page:

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster identified in the notification or Cloud Logging.

  3. On the **Cluster details** page, go to the **Nodes** tab.

  4. Review the value in the **Number of nodes** column and compare it with the minimum number of nodes listed in the **Autoscaling** column. For example, if you see 4 - 6 nodes listed in the **Autoscaling** column, and the number of nodes in the node pool is 4, the number of node pools is already equal to the minimum size, so cluster autoscaler cannot scale down the nodes any further.

  5. If the configuration is correct and the value for number of nodes is equal to the minimum defined for **Autoscaling** , cluster autoscaler is working as intended. If the minimum number of nodes is too high for your needs, [reduce the minimum size](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#resizing_a_node_pool) so that the nodes can scale down.




### Error: No place to move Pods

The following errors occur when cluster autoscaler tries to scale down a node but can't, because a Pod on that node can't be moved to another node:

### Notification

> Scale down of underutilized node is blocked because it has Pod which cannot be moved to another node in the cluster.

### Event
    
    
    "no.scale.down.node.no.place.to.move.pods"
    

If you don't want this Pod to be rescheduled, then this message is expected and no changes are required. If you do want the Pod to be rescheduled, investigate the following definitions in the `pod.spec block` in the manifest of the Pod:

  * **NodeAffinity** : Review the scheduling requirements of the Pods on the underutilized node. You can review these requirements by examining the Pod manifest and looking for any NodeAffinity or NodeSelector rules. If the Pod has a nodeSelector defined and there are no other nodes (from other nodes pools) in the cluster that match this selector, cluster autoscaler is unable to move the Pod to another node, which in turn prevents it from removing any underutilized nodes.
  * **`maxPodConstraint`** : If `maxPodConstraint` is configured to any other number other than the default number of 110, then confirm if this was an intended change. Lowering this value increases the likelihood of issues. Cluster autoscaler cannot reschedule Pods to other nodes, if all other nodes in the cluster have already reached the value defined in `maxPodConstraint`, leaving no space for new Pods to be scheduled. Increasing the `maxPodConstraint` value allows more Pods to be scheduled on nodes and cluster autoscaler will have space to reschedule Pods and scale down underutilized nodes. When defining `maxPodConstraint`, keep in mind that there are approximately 10 system Pods on each node.
  * **`hostPort`** : Specifying a `hostPort` for the Pod means only one Pod can run on that node. This can make it difficult for cluster autoscaler to reduce the number of nodes because the Pod might not be able to move to another node if that node's port is already in use. This is expected behavior.
  * **Ephemeral Storage** : Pods rely on ephemeral storage for temporary data. Insufficient ephemeral storage on nodes can impede Pod scheduling and prevent the scaling down of underutilized nodes. _Example_ : A Pod that requires 6 GB of ephemeral storage can't be scheduled on nodes with less than 6 GB of free ephemeral storage, even if they have sufficient CPU and memory resources. To mitigate ephemeral storage limitations, increase the provisioned ephemeral storage capacity for your nodes. This ensures sufficient capacity for Pod relocation and scaling operations.



### Error: kube-system Pod unmoveable

The following errors occur when a system Pod is preventing scale down:

### Notification

> Pod is blocking scale down because it's a non-DaemonSet, non-mirrored, Pod without a PodDisruptionBudget in the `kube-system` namespace.

### Event
    
    
    "no.scale.down.node.pod.kube.system.unmovable"
    

Pods in the `kube-system` namespace are considered system Pods. In GKE version 1.32.4-gke.1236000 and later, the cluster autoscaler can scale down nodes by evicting system Pods that have been running for at least one hour. In earlier GKE versions, cluster autoscaler doesn't remove Pods in the `kube-system` namespace, which can prevent scale down indefinitely.

**Warning:** Scaling down multiple nodes concurrently (such as during a batch processing job) can cause a cascading delay. When the cluster autoscaler evicts a `kube-system` Pod, Kubernetes might reschedule that Pod onto another idle node. This action resets the creation time of the Pod to zero and restarts the one-hour wait time for the node that receives the rescheduled Pod. 

To resolve this error, choose one of the following resolutions:

  * Add a `PodDisruptionBudget` for the `kube-system` Pods. For more information about manually adding a `PodDisruptionBudget` for the `kube-system` Pods, see the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-to-set-pdbs-to-enable-ca-to-move-kube-system-pods).

Creating a `PodDisruptionBudget` might affect the availability of system workloads which can cause downtime on the cluster. Cluster autoscaler reschedules these system workloads on different worker nodes during the scale down process.

  * Use node pool taints and tolerations (for example, `workload=stateful:NoSchedule`) to separate `kube-system` Pods from your application Pods. We recommend this approach for batch or stateful workloads to prevent the cascading delay issue by keeping `kube-system` Pods off those nodes. This approach lets the nodes scale down without being blocked. For more information, see [node auto-provisioning in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#separate_system_pod).


**Note:** Pods in the `kube-system` namespace are essential to GKE so you shouldn't edit them and aren't charged for them.

#### Verify that nodes have `kube-system` Pods

If you're not sure that your nodes are running `kube-system` Pods, and want to verify, complete the following steps:

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **Query builder**.

  3. Use the following query to find all network policy log records:
         
         - resource.labels.location="CLUSTER_LOCATION"
         resource.labels.cluster_name="CLUSTER_NAME"
         logName="projects/PROJECT_ID/logs/container.googleapis.com%2Fcluster-autoscaler-visibility"
         jsonPayload.noDecisionStatus.noScaleDown.nodes.node.mig.nodepool="NODE_POOL_NAME"
         

Replace the following:

     * `CLUSTER_LOCATION`: The region your cluster is in.
     * `CLUSTER_NAME`: The name of your cluster.
     * `PROJECT_ID`: the ID of the project that your cluster belongs to.
     * `NODE_POOL_NAME`: The name of your node pool.

If there are `kube-system` Pods running on your node pool, the output includes the following:
    
    "no.scale.down.node.pod.kube.system.unmovable"
    




### Error: Not enough `PodDisruptionBudget`

The following errors occur when your `PodDisruptionBudget` is preventing scale down:

### Notification

> Scale down of underutilized node is blocked because it has a Pod running on it which doesn't have enough Pod Disruption Budget to allow eviction of the Pod.

### Event
    
    
    NoScaleDownNodePodNotEnoughPdb: "no.scale.down.node.pod.not.enough.pdb"
    

To see if a `PodDisruptionBudget` is too restrictive, review its settings:
    
    
    kubectl get pdb --all-namespaces
    

The output is similar to the following:
    
    
    NAMESPACE        NAME    MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
    example-app-one  one_pdb       N/A             1                 1               12d
    example-app-two  two_pdb       N/A             0                 0               12d
    

In this example, any Pods matching the `two_pdb` label selector won't be evicted by cluster autoscaler. The `maxUnavailable: 0` setting in this `PodDisruptionBudget` dictates that all replicas must remain available at all times. Additionally, `disruptionsAllowed: 0` prohibits any disruptions to these Pods. Consequently, nodes running these Pods cannot be scaled down, as doing so would cause a disruption and violate the `PodDisruptionBudget`.

If your `PodDisruptionBudget` is working the way you want, no further action is required. If you'd like to adjust your `PodDisruptionBudget` so that Pods on an underutilized node can be moved, edit the manifest of the `PodDisruptionBudget`. For example, if you had set `maxUnavailable` to `0`, you could change it to `1` so that cluster autoscaler can scale down.

### Issue: Node stay in cordoned status and isn't removed

Errors similar to the following happen when cluster autoscaler can't reduce the node pool size because the Google service account doesn't have the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic):
    
    
    Required 'compute.instanceGroups.update' permission for 'INSTANCE_GROUP_NAME'.
    

A common symptom of this issue is when cluster autoscaler tries to reduce the node pool size, but the node doesn't change status.

To resolve this issue, check if the default service account (`PROJECT_NUMBER@cloudservices.gserviceaccount.com`) has the Editor role (`roles/editor`) on the project. If the service account doesn't have this role, add it. GKE uses this service account to manage your project's resources. To learn how to do this, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role) in the IAM documentation.

## What's next

  * Review the following questions in the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md):

    * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
    * [Does the cluster autoscaler work with PodDisruptionBudget in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)
    * [What types of Pods can prevent the cluster autoscaler from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node)
  * [Watch a YouTube video about troubleshooting and resolving scaling issues](https://www.youtube.com/watch?v=IdCjKUZah-Q).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
