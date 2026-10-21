---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up/
title: Troubleshoot cluster autoscaler not scaling up \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:47:49.187297+00:00
---

# Troubleshoot cluster autoscaler not scaling up  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot cluster autoscaler not scaling up Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When your Pods in Google Kubernetes Engine (GKE) are stuck in a `Pending` state and new nodes aren't being added, it often indicates an issue with the cluster autoscaler's scale-up functionality. This issue can prevent your applications from scaling to meet demand, delay deployments, and affect service availability.

Use this page to diagnose and resolve common problems that prevent the cluster autoscaler from adding new nodes. Fixing these issues lets the Kubernetes scheduler place your workloads promptly and helps your cluster adapt to increasing load.

This information is important for Application developers, who need their applications and services to schedule and run reliably, and for Platform admins and operators, who are responsible for ensuring the cluster can dynamically provision resources to meet workload requirements and maintain service levels. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Understand when cluster autoscaler scales up your nodes

Before you proceed to the troubleshooting steps, it can be helpful to understand when cluster autoscaler would try to scale up your nodes. Cluster autoscaler only adds nodes when existing resources are insufficient.

Every 10 seconds, cluster autoscaler checks if there are any Pods that are unschedulable. A Pod becomes unschedulable when the Kubernetes scheduler cannot place it on any existing node due to insufficient resources, node constraints, or unmet Pod requirements.

When cluster autoscaler finds unschedulable Pods, it evaluates if adding a node would allow the Pod to get scheduled. If adding a node would let a Pod get scheduled cluster autoscaler adds a new node to the managed instance group (MIG). The Kubernetes scheduler can then schedule the Pod on the newly provisioned node.

### Check if you have unschedulable Pods

To determine if your cluster needs to scale up, check for unscheduled Pods:

  1. In the Google Cloud console, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. In the filter_list **Filter** field, enter `unschedulable` and press `Enter`.

If there are any Pods listed, then you have unschedulable Pods. To troubleshoot unschedulable Pods, see [Error: Pod unschedulable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads#PodUnschedulable). Resolving the underlying cause of unschedulable Pods can often enable cluster autoscaler to scale up. To identify and resolve errors that are specific to cluster autoscaler, explore the following sections.

If there are no Pods listed, cluster autoscaler doesn't need to scale up and is working as expected.




#### Check if you previously had unschedulable Pods

If you're investigating what caused cluster autoscaler to fail in the past, check for previously unschedulable Pods:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Specify a time range for the log entries that you want to view.

  3. In the query pane, enter the following query:
         
         logName="projects/PROJECT_ID/logs/events"
         jsonPayload.source.component="default-scheduler"
         jsonPayload.reason="FailedScheduling"
         

Replace `PROJECT_ID` with your project ID.

  4. Click **Run query**.

If there are any results listed, then you had unschedulable Pods in the time range that you specified.




## Check if the issue is caused by a limitation

After you've confirmed that you have unscheduled Pods, make sure your issue with cluster autoscaler isn't caused by one of the [limitations for the cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations).

## View errors

You can often diagnose the cause of scale up issues by viewing error messages:

  * If you've already seen an error message, see the error messages table for advice on resolving the error.

  * If you haven't seen a message yet, use one of the following options:

    * **Issues less than 72 hours old** : View error notifications in the Google Cloud console.
    * **Issues over 72 hours old** : View errors in events in Cloud Logging.



### View errors in notifications

If the issue you observed happened less than 72 hours ago, view notifications about errors in the Google Cloud console. These notifications provide valuable insights into why cluster autoscaler didn't scale up and offer advice on how to resolve the error and view relevant logs for further investigation.

To view the notifications in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Review the **Notifications** column. The following notifications are associated with scale up issues:

     * `Can't scale up`
     * `Can't scale up pods`
     * `Can't scale up a node pool`
  3. Click the relevant notification to see a pane with details about what caused the issue and recommended actions to resolve it.

  4. Optional: To view the logs for this event, click **Logs**. This action takes you to Logs Explorer with a pre-populated query to help you further investigate the scaling event. To learn more about how scale up events work, see [View cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility).




If you're still experiencing issues after reviewing the advice in the notification, consult the error messages tables for further help.

### View errors in events

If the issue you observed happened more than 72 hours ago, view events in Cloud Logging. When there has been an error, it's often recorded in an event.

To view cluster autoscaler logs in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the name of the cluster that you want to investigate to view its **Cluster details** page.

  3. On the **Cluster details** page, click the **Logs** tab.

  4. On the **Logs** tab, click the **Autoscaler Logs** tab to view the logs.

  5. Optional: To apply more advanced filters to narrow the results, click the button with the arrow on the right side of the page to view the logs in Logs Explorer.




To learn more about scale up events work, see [View cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility). For one example of how to use Cloud Logging, see the following troubleshooting example.

#### Example: Troubleshoot an issue over 72 hours old

The following example shows you how you might investigate and resolve an issue with a cluster not scaling up.

**Scenario** : For the past hour, a Pod has been marked as unschedulable. Cluster autoscaler did not provision any new nodes to schedule the Pod.

**Solution** :

  1. Because the issue happened over 72 hours ago, you investigate the issue using Cloud Logging instead of looking at the notification messages.
  2. In Cloud Logging, you find the logging details for cluster autoscaler events, as described in View errors in events.
  3. You search for `scaleUp` events that contain the Pod that you're investigating in the `triggeringPods` field. You could filter the log entries, including filtering by a particular JSON field value. Learn more in [Advanced logs queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries).

  4. You don't find any scale up events. However, if you did, you could try to find an [`EventResult`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#eventresult-event) that contains the same `eventId` as the `scaleUp` event. You could then look at the `errorMsg` field and consult the list of possible scaleUp error messages.

  5. Because you didn't find any `scaleUp` events, you continue to search for `noScaleUp` events and review the following fields:

     * `unhandledPodGroups`: contains information about the Pod (or Pod's controller).
     * `reason`: provides global reasons indicating scaling up could be blocked.
     * `skippedMigs`: provides reasons why some MIGs might be skipped.
  6. You find a `noScaleUp` event for your Pod, and all MIGs in the `rejectedMigs` field have the same reason message ID of `"no.scale.up.mig.failing.predicate"` with two parameters: `"NodeAffinity"` and `"node(s) did not match node selector"`.




**Resolution** :

After consulting the list of error messages, you discover that cluster autoscaler can't scale up a node pool because of a failing scheduling predicate for the pending Pods. The parameters are the name of the failing predicate and the reason why it failed.

To resolve the issue, you review the manifest of the Pod, and discover that it has a node selector that doesn't match any MIG in the cluster. You delete the selector from the manifest of the Pod and recreate the Pod. Cluster autoscaler adds a new node and the Pod is scheduled.

## Resolve scale up errors

If you are using custom ComputeClasses and the scale-up issues are related to the specific node configurations defined in your ComputeClass, refer to [Troubleshoot custom ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass).

After you have identified your error, use the following tables to help you understand what caused the error and how to resolve it.

### ScaleUp errors

You can find event error messages for `scaleUp` events in the corresponding `eventResult` event, in the `resultInfo.results[].errorMsg` field.

When a scale-up operation fails because it exceeds a quota, it is a node creation error that triggers a system backoff period, which can last up to 30 minutes. For more information, see [Backoff periods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#backoff-periods).

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"scale.up.error.out.of.resources"` | Resource errors occur when you try to request new resources in a zone that cannot accommodate your request due to the current unavailability of a Compute Engine resource, such as GPUs or CPUs. | Failing MIG IDs. | Follow the [resource availability troubleshooting steps](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) in the Compute Engine documentation.  
`"scale.up.error.quota.exceeded"` | The scaleUp event failed because some of the MIGs couldn't be increased, due to exceeded Compute Engine quota. | Failing MIG IDs. | Check the **Errors** tab of the MIG in the Google Cloud console to see what quota is being exceeded. After you know which quota is being exceeded, follow the instructions to [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota).  
`"scale.up.error.waiting.for.instances.timeout"` | Scale up of managed instance group failed to scale up due to timeout.  | Failing MIG IDs. | If the instances boot but do not register with the control plane, follow the [instance registration troubleshooting steps](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration#find-instance-failed-registration). This message should be transient. If it persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
`"scale.up.error.ip.space.exhausted"` | Can't scale up because instances in some of the managed instance groups ran out of IPs. This means that the cluster doesn't have enough unallocated IP address space to use to add new nodes or Pods. | Failing MIG IDs. | Follow the troubleshooting steps in [Not enough free IP address space for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vpc-clusters#not_enough_space).  
`"scale.up.error.service.account.deleted"` | Can't scale up because the service account was deleted. | Failing MIG IDs. |  Try to [undelete the service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting). If that procedure is unsuccessful, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
### Reasons for a noScaleUp event

A `noScaleUp` event is periodically emitted when there are unschedulable Pods in the cluster and cluster autoscaler cannot scale the cluster up to schedule the Pods. `noScaleUp` events are best-effort, and don't cover all possible cases.

#### NoScaleUp top-level reasons

Top-level reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.reason` field. The message contains a top-level reason for why cluster autoscaler cannot scale the cluster up.

Message | Details | Mitigation  
---|---|---  
`"no.scale.up.in.backoff"` | No scale up because scaling up is in a backoff period (temporarily blocked). This message that can occur during scale up events with a large number of Pods. |  This message should be transient. Check this error after a few minutes. If this message persists, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further investigation.   
  
#### NoScaleUp top-level node auto-provisioning reasons

Top-level node auto-provisioning reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.napFailureReason` field. The message contains a top-level reason for why cluster autoscaler cannot provision new node pools.

Message | Details | Mitigation  
---|---|---  
`"no.scale.up.nap.disabled"` |  Node auto provisioning couldn't scale up because node auto provisioning is not enabled at cluster level. If node auto-provisioning is disabled, new nodes won't be automatically provisioned if the pending Pod has requirements that can't be satisfied by any existing node pools. | Review the cluster configuration and consider [enabling node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable).  
  
#### NoScaleUp MIG-level reasons

MIG-level reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.skippedMigs[].reason` and `noDecisionStatus.noScaleUp.unhandledPodGroups[].rejectedMigs[].reason` fields. The message contains a reason why cluster autoscaler can't increase the size of a particular MIG.

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.up.mig.skipped"` | Cannot scale up a MIG because it was skipped during the simulation. | Reasons why the MIG was skipped (for example, missing a Pod requirement). | Review the parameters included in the error message and address why the MIG was skipped.  
`"no.scale.up.mig.failing.predicate"` | Can't scale up a node pool because of a failing scheduling predicate for the pending Pods. |  Name of the failing predicate and reasons why it failed. | Review the Pod requirements, such as [affinity rules](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-respect-node-affinity-when-selecting-node-groups-to-scale-up), taints or tolerations, and resource requirements.  
  
#### NoScaleUp Pod-group-level node auto-provisioning reasons

Pod-group-level node auto-provisioning reason messages for `noScaleUp` events appear in the `noDecisionStatus.noScaleUp.unhandledPodGroups[].napFailureReasons[]` field. The message contains a reason why cluster autoscaler cannot provision a new node pool to schedule a particular Pod group.

Message | Details | Parameters | Mitigation  
---|---|---|---  
`"no.scale.up.nap.pod.gpu.no.limit.defined"` | Node auto-provisioning couldn't provision any node group because a pending Pod has a GPU request, but [GPU resource limits are not defined at the cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#gpu_limits). | Requested GPU type. | Review the pending Pod's GPU request, and update the cluster-level node auto-provisioning [configuration for GPU limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#gpu_limits).  
`"no.scale.up.nap.pod.gpu.type.not.supported"` | Node auto-provisioning did not provision any node group for the Pod because it has requests for an unknown GPU type. | Requested GPU type. | Check the pending Pod's configuration for the GPU type to ensure that it matches a [supported GPU type](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads).   
`"no.scale.up.nap.pod.zonal.resources.exceeded"` | Node auto-provisioning did not provision any node group for the Pod in this zone because doing so would either violate the [cluster-wide maximum resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#limits_for_clusters), exceed the available resources in the zone, or there is no machine type that could fit the request. | Name of the considered zone. | Review and update [cluster-wide maximum resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning#limits_for_clusters), the Pod resource requests, or the [available zones for node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#auto-provisioning_locations).  
`"no.scale.up.nap.pod.zonal.failing.predicates"` | Node auto-provisioning did not provision any node group for the Pod in this zone because of failing predicates. | Name of the considered zone and reasons why predicates failed. | Review the pending Pod's requirements, such as affinity rules, taints, tolerations, or resource requirements.  
  
## Conduct further investigation

The following sections provide guidance on how to use Logs Explorer and `gcpdiag` to gain additional insights into your errors.

### Investigate errors in Logs Explorer

If you want to further investigate your error message, view logs specific to your error:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. In the [query pane](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-viewer-interface), enter the following query:
         
         resource.type="k8s_cluster"
         log_id("container.googleapis.com/cluster-autoscaler-visibility")
         jsonPayload.resultInfo.results.errorMsg.messageId="ERROR_MESSAGE"
         

Replace `ERROR_MESSAGE` with the message that you want to investigate. For example, `scale.up.error.out.of.resources`.

  3. Click **Run query**.




### Debug some errors with gcpdiag

`gcpdiag` is an open source tool created with support from Google Cloud technical engineers. It isn't an officially supported Google Cloud product.

If you've experienced one of the following error messages, you can use [`gcpdiag`](https://gcpdiag.dev/runbook/diagnostic-trees/gke/cluster-autoscaler/#parameters) to help troubleshoot the issue:

  * `scale.up.error.out.of.resources`
  * `scale.up.error.quota.exceeded`
  * `scale.up.error.waiting.for.instances.timeout`
  * `scale.up.error.ip.space.exhausted`
  * `scale.up.error.service.account.deleted`



For a list and description of all `gcpdiag` tool flags, see the [`gcpdiag` usage instructions](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#usage).

## Resolve complex scale-up errors

The following sections help you resolve errors that require multiple steps or don't have an associated event message from the cluster autoscaler.

### Pod doesn't fit on node

**Symptoms** :

Your Pods remain in a `Pending` state with the `PodUnschedulable` error message, or your cluster shows the `Pods unschedulable` error message, and cluster autoscaler doesn't scale up to add nodes.

**Cause** :

Cluster autoscaler only adds nodes to a node pool if the machine type provides enough resources, such as CPUs, GPUs, memory, and storage, for a pending Pod. If a Pod's resource requests exceed the resources of a single node, cluster autoscaler doesn't scale up because the Pod still can't fit on a new node.

Also, a node's allocatable resources are less than its total resources because system components reserve a portion of those resources. For more information about how GKE calculates allocatable resources, see [Node allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#node_allocatable_resources).

**Resolution** :

To check whether a Pod's resource requests exceed the resources provided by your nodes and resolve the issue, complete the following steps. This example checks CPU resources, but the same steps apply to GPUs, memory, and storage resources:

  1. In the Google Cloud console, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Click the `PodUnschedulable` error message.

  3. In the **Details** pane, click the name of the Pod. If there are multiple Pods, start with the first Pod and repeat the following process for each Pod.

  4. On the **Pod details** page, click the **YAML** tab.

  5. Note each container's resource requests in the Pod to find the total resource requests. For example, in the following Pod configuration, the Pod needs 2 vCPUs:
         
         resources:
           limits:
             cpu: "3"
           requests:
             cpu: "2"
         

  6. View the node pool details from the cluster with the unscheduled Pod:

     1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

     2. Click the name of the cluster that has the `Pods unschedulable` error message.

     3. On the **Cluster details** page, click the **Nodes** tab.

     4. In the **Node pools** section, note the value in the **Machine type** column, for example, `n1-standard-1`.

  7. Compare the resource request with the vCPUs provided by the machine type. For example, if a Pod requests 2 vCPUs, but the available nodes use the `n1-standard-1` machine type, the nodes only have 1 vCPU. With a configuration like this, cluster autoscaler doesn't trigger a scale-up because the Pod still can't fit on a new node. For more information about available machine types, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource) in the Compute Engine documentation.

  8. Resolve the mismatch based on your workload needs:

     * **If the Pod requires the requested resources** : create a node pool with a machine type that can support the Pod's resource requests.
     * **If the Pod's resource requests aren't accurate** : update the Pod's definition so that the Pod can fit on existing nodes.



### Unhealthy clusters prevent scale-up

**Symptoms** :

Cluster autoscaler halts all scaling operations, and the `cluster-autoscaler-status` ConfigMap contains an event with the type `Warning` and `ClusterUnhealthy` listed as the reason.

To view the `cluster-autoscaler-status` ConfigMap, run the following command:
    
    
    kubectl describe configmap cluster-autoscaler-status -n kube-system
    

**Cause** :

Cluster autoscaler doesn't scale up if it considers a cluster to be unhealthy. Cluster autoscaler determines cluster health based on the ratio of healthy and ready nodes, not on control plane health. If 45% of nodes in a cluster are unhealthy or not ready, cluster autoscaler halts all operations.

Cluster autoscaler also considers a ready node to be `NotReady` when the node has a taint with the `ignore-taint.cluster-autoscaler.kubernetes.io/` prefix. Cluster autoscaler treats the node as `NotReady` for as long as that taint is present.

**Resolution** :

To resolve this issue, decrease the number of unhealthy nodes by doing one or both of the following actions:

  * Investigate and repair unhealthy or `NotReady` nodes so that fewer than 45% of nodes in the cluster are unhealthy.
  * If ready nodes have a taint with the `ignore-taint.cluster-autoscaler.kubernetes.io/` prefix, remove the taint.



## What's next

  * Review the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md).
  * [Watch a YouTube video about troubleshooting and resolving scaling issues](https://www.youtube.com/watch?v=IdCjKUZah-Q).
  * [Troubleshoot custom ComputeClass issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/custom-computeclass).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
