---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads/
title: Troubleshoot issues with deployed workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:20.796513+00:00
---

# Troubleshoot issues with deployed workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/deployed-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot issues with deployed workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to resolve errors with your deployed workloads in Google Kubernetes Engine (GKE).

For more general advice about troubleshooting your applications, see [Troubleshooting Applications](https://kubernetes.io/docs/tasks/debug/debug-application/) in the Kubernetes documentation.

## All errors: Check Pod status

If there are issues with a workload's Pods, Kubernetes updates the Pod status with an error message. View these errors by checking the status of a Pod using the Google Cloud console or the `kubectl` command-line tool.

### Console

Perform the following steps:

  1. In the Google Cloud console, go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Select the workload that you want to investigate. The **Overview** tab displays the status of the workload.

  3. From the **Managed Pods** section, click any error status message.




### kubectl

To see all Pods running in your cluster, run the following command:
    
    
    kubectl get pods
    

The output is similar to the following:
    
    
    NAME       READY  STATUS             RESTARTS  AGE
    POD_NAME   0/1    CrashLoopBackOff   23        8d
    

Potential errors are listed in the `Status` column.

To get more information about a specific Pod, run the following command:
    
    
    kubectl describe pod POD_NAME
    

Replace `POD_NAME` with the name of the Pod that you want to investigate.

In the output, the `Events` field shows more information about errors.

If you'd like more information, view the container logs:
    
    
    kubectl logs POD_NAME
    

These logs can help you identify if a command or code in the container caused the Pod to crash.

After you identify the error, use the following sections to try and resolve the issue.

## Error: CrashLoopBackOff

A status of `CrashLoopBackOff` doesn't mean there's a specific error, instead it indicates that a container is repeatedly crashing after restarting.

For more information, see [Troubleshoot CrashLoopBackOff events](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/crashloopbackoff-events).

## Errors: ImagePullBackOff and ErrImagePull

A status of `ImagePullBackOff` or `ErrImagePull` indicates that the image used by a container cannot be loaded from the image registry.

For guidance on troubleshooting these statuses, see [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

## Error: `OutOfPods`

A status of `OutOfPods` indicates that a node cannot run a Pod because the node has reached its maximum Pod capacity.

#### Symptoms

You might see a message in the Pod's events similar to the following:
    
    
    Node didn't have enough resource: pods, requested: 1, used: 32, capacity: 32
    

#### Cause

This error occurs when there is a request to schedule a Pod on a node that is already at capacity. This situation can commonly occur during node startup, for example when the `kube-scheduler` component assigns Pods to a new node before the `kubelet` agent has reported the presence of static Pods like the `kube-proxy` component, which require their own Pod capacity.

#### Resolution

To resolve this issue, try one of the following solutions:

  * **Increase the maximum number of Pods per node.** If your nodes consistently reach their Pod limit, increase the `--max-pods-per-node` setting for your node pools. Increasing the number of Pods might require larger nodes to handle the increased resource demands.

  * **Enable cluster autoscaler and node auto-provisioning.** If you frequently run out of Pod capacity, enabling the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) can help ensure that your cluster has enough nodes to meet the demand of your workloads.

  * **Change the autoscaling profile.** If you already use the cluster autoscaler, try [changing the autoscaling profile](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles) to the `balanced` profile instead of the `optimize-utilization` profile. The `optimize-utilization` profile can increase the likelihood of `OutOfPods` errors because it attempts to place Pods on the most utilized nodes.




## Error: Pod unschedulable

A status of `PodUnschedulable` indicates that your Pod cannot be scheduled because of insufficient resources or some configuration error.

If you have [configured control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#control-plane-metrics), you can find more information about these errors in [scheduler metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#scheduler) and [API server metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics#api-server).

### Use the unschedulable Pods interactive playbook

You can troubleshoot `PodUnschedulable` errors using the interactive playbook in the Google Cloud console:

  1. Go to the unschedulable Pods interactive playbook:

[Go to Playbook](https://console.cloud.google.com/monitoring/dashboards/gke-troubleshooting/unschedulable)

  2. In the **Cluster** drop-down list, select the cluster that you want to troubleshoot. If you can't find your cluster, enter the name of the cluster in the filter_list **Filter** field.

  3. In the **Namespace** drop-down list, select the namespace that you want to troubleshoot. If you can't find your namespace, enter the namespace in the filter_list **Filter** field.

  4. To help you identify the cause, work through each of the sections in the playbook:

     1. Investigate CPU and Memory
     2. Investigate Max Pods per Node
     3. Investigate Autoscaler Behavior
     4. Investigate Other Failure Modes
     5. Correlate Change Events
  5. Optional: To get notifications about future `PodUnschedulable` errors, in the **Future Mitigation Tips** section, select **Create an Alert**.




### Error: Insufficient resources

A `PodUnschedulable` status can occur if there are insufficient CPU, memory, or other resources to meet the Pod's requests.

#### Symptoms

You might encounter an error indicating a lack of CPU, memory, or another resource. For example: `No nodes are available that match all of the predicates: Insufficient cpu (2)`. This message indicates that, on two nodes, there isn't enough CPU available to fulfill a Pod's requests.

#### Cause

If your Pod resource requests exceed that of a single node from any eligible node pools, GKE doesn't schedule the Pod and also doesn't trigger scale-up to add a new node.

Your cluster runs system containers in the `kube-system` namespace. Those containers also use cluster resources.

#### Resolution

Try the following solutions:

  * Adjust the Pod's resource request by specifying a lower value in the `spec: containers: resources: requests` field. The default CPU request is 100m or 10% of a CPU (or [one core](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu)).

  * Create a new node pool with nodes that have sufficient resources to meet the Pod's requests.

  * Enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) so that GKE can automatically create node pools with nodes where the unscheduled Pods can run.




### Error: MatchNodeSelector

A `MatchNodeSelector` error indicates that there are no nodes that match the Pod's label selector.

#### Symptoms

The Pod status or events show a `MatchNodeSelector` error.

#### Cause

The labels specified in the Pod manifest's `nodeSelector` field don't exist on any nodes in the cluster.

#### Resolution

To resolve this error, ensure that the labels specified in the Pod's `nodeSelector` field match the labels on at least one node in your cluster:

  1. Identify the label requirements that the Pod is looking for by checking its `spec: nodeSelector` field.

  2. To see if any labels match the Pod's requirements, view the actual labels assigned to the nodes in your cluster:
         
         kubectl get nodes --show-labels
         

  3. If a node is intended to run this Pod, attach the necessary label:
         
         kubectl label nodes NODE_NAME LABEL_KEY=LABEL_VALUE
         

Replace the following:

     * `NODE_NAME`: the node that you want to add a label to.
     * `LABEL_KEY`: the label's key.
     * `LABEL_VALUE`: the label's value.



For more information, see [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.

### Error: PodToleratesNodeTaints

A `PodToleratesNodeTaints` error indicates that the Pod can't be scheduled to any node because the Pod doesn't have tolerations that correspond to existing [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

#### Symptoms

The Pod status or events show a `PodToleratesNodeTaints` error.

#### Cause

The Pod can't be scheduled to any node because the Pod doesn't have tolerations that correspond to existing node taints.

#### Resolution

  1. Check the taints on the node:
         
         kubectl describe nodes NODE_NAME
         

In the output, check the `Taints` field, which lists key-value pairs and scheduling effects. If the effect listed is `NoSchedule`, then no Pod can be scheduled on that node unless it has a matching [toleration](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/).

  2. Remove the taint from the node. For example, to remove a `NoSchedule` taint, run the following command:
         
         kubectl taint nodes NODE_NAME key:NoSchedule-
         




### Error: PodFitsHostPorts

The `PodFitsHostPorts` error means that a node is trying to use a port that's already occupied.

#### Symptoms

The Pod status shows a `PodFitsHostPorts` error.

#### Cause

A Pod is requesting a host port that's already in use by another Pod or process on the target node.

#### Resolution

To resolve the issue, consider following [Kubernetes best practices](https://kubernetes.io/docs/concepts/configuration/overview/#services) and use a `NodePort` Service instead of the `hostPort` setting.

If you must use a host port, check the manifests of the Pods and make sure that all Pods on the same node have unique values defined for the `hostPort` setting.

### Error: Does not have minimum availability

This error can occur if a node has adequate resources but isn't available for scheduling.

#### Symptoms

  * You see the `Does not have minimum availability` error.

  * The node's status shows a `SchedulingDisabled` status or a `Cordoned` status.




#### Cause

The node's cordoned status prevents new Pods from being scheduled on it.

#### Resolution

To make the node available for scheduling Pods again, uncordon it:

### Console

Perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Select the cluster that you want to investigate. The **Nodes** tab displays the Nodes and their status.




To enable scheduling on the node, perform the following steps:

  1. From the list, click the node that you want to investigate.

  2. From the **Node Details** section, click **Uncordon**.




### kubectl

To get statuses of your nodes, run the following command:
    
    
    kubectl get nodes
    

To enable scheduling on the node, run:
    
    
    kubectl uncordon NODE_NAME
    

### Error: Maximum Pods per node limit reached

A `Too many pods` error indicates that a Pod cannot schedule because the target node has reached its maximum configured Pod capacity.

#### Symptoms

  * The Pods are stuck in an `Unschedulable` state.
  * You see a message including the phrase `Too many pods`.



#### Cause

The [Maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#configuring_maximum_pods_per_node) limit is reached by all nodes in the cluster.

#### Resolution

To resolve this error, complete the following steps:

  1. Check the `Maximum pods per node` configuration from the Nodes tab in GKE cluster details in the Google Cloud console.

  2. Get a list of nodes:
         
         kubectl get nodes
         

  3. For each node, verify the number of Pods running on the node:
         
         kubectl get pods -o wide | grep NODE_NAME | wc -l
         

  4. If the limit is reached, add a new node pool or add additional nodes to the existing node pool.




### Issue: Maximum node pool size reached with cluster autoscaler enabled

This issue occurs when a node pool has reached its maximum configured size under the cluster autoscaler.

#### Symptoms

GKE doesn't trigger scale up for a Pod that would otherwise be scheduled with this node pool. Instead, the Pod remains in a `Pending` state.

#### Cause

The node pool has reached its [maximum size](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#minimum_and_maximum_node_pool_size) according to its cluster autoscaler configuration.

#### Resolution

Increase the maximum size of the node pool by [changing the cluster autoscaler configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler).

### Issue: Maximum node pool size reached with cluster autoscaler disabled

This issue occurs when a node pool has reached its maximum size and the cluster autoscaler is disabled.

#### Symptoms

GKE cannot schedule the Pod with the node pool.

#### Cause

The node pool has reached its maximum number of nodes, and the cluster autoscaler is disabled.

#### Resolution

To resolve this issue, try one of the following solutions:

  * [Increase the size of your node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster#increase).
  * [Enable cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler#enable_autoscaling) to resize your cluster automatically.



### Error: Unbound PersistentVolumeClaims

An `Unbound PersistentVolumeClaims` error indicates that the Pod references a PersistentVolumeClaim that isn't bound.

#### Symptoms

The Pod status or events show an `Unbound PersistentVolumeClaims` error.

#### Cause

This error can occur because of one of the following reasons:

  * Your PersistentVolume failed to provision.
  * There was a configuration error during manual pre-provisioning of a PersistentVolume and its binding to a PersistentVolumeClaim.



#### Resolution

  1. Verify if provisioning failed by getting the events for your PersistentVolumeClaim:
         
         kubectl describe pvc STATEFULSET_NAME-PVC_NAME-0
         

Replace the following:

     * `STATEFULSET_NAME`: the name of the StatefulSet object.
     * `PVC_NAME`: the name of the PersistentVolumeClaim object.
  2. Try to pre-provision the volume again.




### Error: Insufficient quota

If GKE attempts to scale up your cluster to schedule a Pod but encounters quota constraints, the scale-up fails.

#### Symptoms

You receive the `scale.up.error.quota.exceeded` error message in your Pod's events.

#### Cause

Scaling up the cluster would exceed your project's available quota.

#### Resolution

Verify that your project has sufficient Compute Engine quota for GKE to scale up your cluster. For more information, see [ScaleUp errors](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility#scaleup-errors).

### Issue: Deprecated APIs

Using APIs that are no longer supported in your manifests can prevent workload deployment.

#### Symptoms

Workloads fail to deploy or run because of deprecated API usage.

#### Cause

Your manifests use deprecated APIs that are removed in your cluster's minor version.

#### Resolution

Ensure that you are not using deprecated APIs. Update your manifests to use supported APIs. For more information, see [Feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations).

## Error: Didn't have free ports for the requested Pod ports

Binding a Pod to a host port limits where GKE can schedule the Pod because each `hostIP` address, `hostPort` setting, and `protocol` value combination must be unique.

#### Symptoms

You see an error similar to the following:
    
    
    0/1 nodes are available: 1 node(s) didn't have free ports for the requested pod ports. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod.
    

#### Cause

Multiple Pods on the same node specify the same value defined in the `hostPort` field.

#### Resolution

To resolve this issue, try one of the following solutions:

  * Follow [Kubernetes best practices](https://kubernetes.io/docs/concepts/configuration/overview/#services) and use a `NodePort` Service instead of a host port.
  * If you must use a host port, check the manifests of the Pods and make sure that all Pods on the same node have unique values defined for the `hostPort` field.



## Issue: Application and probe failures in Pods

This issue occurs when you run applications that use HTTPS to communicate with a server.

#### Symptoms

Failures in these applications are similar to the following:

  * Pods don't start, and containers crash with exit code `137`.
  * Liveness or readiness probes fail with an error message similar to the following:
        
        probeResult="failure" output="Get "https://example.com/healthy": EOF"
        

  * Pods run as expected, but application logs show connection failures.




#### Cause

Kubernetes versions 1.30 and later use Golang versions that disable the following TLS cipher suites:

  * `TLS_RSA_WITH_AES_128_GCM_SHA256`
  * `TLS_RSA_WITH_AES_256_GCM_SHA384`
  * `TLS_RSA_WITH_AES_128_CBC_SHA`
  * `TLS_RSA_WITH_AES_256_CBC_SHA`
  * `TLS_RSA_WITH_3DES_EDE_CBC_SHA`



#### Resolution

Use [supported cipher suites](https://go.dev/src/crypto/tls/cipher_suites.go) from TLS 1.2 and later.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
