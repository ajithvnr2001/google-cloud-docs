---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-autoscaler/
title: Enable cluster autoscaling \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:21.859898+00:00
---

# Enable cluster autoscaling  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-autoscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Enable cluster autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

This document describes autoscaling for a user cluster in Google Distributed Cloud.

Cluster autoscaling increases or decreases the number of nodes in a node pool based on the demands of your workloads.

## Before you begin

Read about the limitations of the cluster autoscaler.

The cluster autoscaler makes the following assumptions:

  * All replicated Pods can be restarted on some other node, which might cause a brief disruption. If your services cannot tolerate disruption, we do not recommend using the cluster autoscaler.

  * Users or administrators do not manually manage nodes. If autoscaling is enabled for a node pool, you cannot override the `replicas` field of the node pool.

  * All nodes in a single node pool have the same set of labels.




## How cluster autoscaling works

The cluster autoscaler works on a node-pool basis. When you enable autoscaling for a node pool, you specify a minimum and maximum number of nodes for the pool.

The cluster autoscaler increases or decreases the number of nodes in the pool automatically, based on the resource requests (rather than actual resource utilization) of Pods running on the nodes. It periodically checks the status of Pods and nodes, and takes action:

  * If Pods are unschedulable because there are not enough nodes in the pool, the cluster autoscaler adds nodes, up to the specified maximum.

  * If nodes are under-utilized, and all Pods could be scheduled with fewer nodes in the pool, the cluster autoscaler removes nodes, down to the specified minimum. If a node can't be drained gracefully, the node is forcibly terminated, and the attached Kubernetes-managed disk is safely detached.




If your Pods have requested too few resources (or haven't changed the defaults, which might be insufficient) and your nodes are experiencing shortages, the cluster autoscaler does not correct that situation. You can help ensure that the cluster autoscaler works accurately by making explicit resource requests for all of your workloads.

For an individual node pool, `minReplicas` must be ≥ 1. However, the sum of the untainted user cluster nodes at any given time must be at least 3. This means the sum of the `minReplicas` values for all autoscaled node pools, plus the sum of the `replicas` values for all non-autoscaled node pools, must be at least 3.

The cluster autoscaler considers the relative cost of the instance types in the various node pools, and attempts to expand the node pool in a way that causes the least waste possible.

## Create a user cluster with autoscaling

To create a user cluster with autoscaling enabled for a node pool, fill in the [`autoscaling`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-autoscaling-section) section for the node pool in the user cluster configuration file. For example:
    
    
    nodePools:
    - name: pool‐1
      …
      replicas: 3
      ...
      autoscaling:
        minReplicas: 1
        maxReplicas: 5
    

The preceding configuration creates a node pool with 3 replicas, and applies autoscaling with the minimum node pool size as 1 and the maximum node pool size as 5.

The `minReplicas` value must be ≥ 1. A node pool can't scale down to zero nodes.

## Add a node pool with autoscaling

To add a node pool with autoscaling to an existing cluster:

  1. Edit the user cluster configuration file to add a new node pool, and include an `autoscaling` section for the pool. Set the values of `replicas`, `minReplicas`, and `maxReplicas` as desired. For example:
         
         nodePools:
         - name: my-new-node-pool
           …
           replicas: 3
           ...
           autoscaling:
             minReplicas: 2
             maxReplicas: 6
         

  2. Update the cluster:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




## Enable autoscaling for an existing node pool

To enable autoscaling for a node pool in an existing cluster:

  1. Edit a specific `nodePool` in the user cluster configuration file, and include the `autoscaling` section. Set the values of `minReplicas` and `maxReplicas` as desired.
         
         nodePools:
         - name: my-existing-node-pool
           …
           replicas: 3
           ...
           autoscaling:
             minReplicas: 1
             maxReplicas: 5
         

  2. Update the cluster:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         


**Note:** You cannot modify the value of `replicas` for an existing node pool while enabling autoscaling.

## Disable autoscaling for an existing node pool

To disable autoscaling for a specific node pool:

  1. Edit the user cluster configuration file and remove the `autoscaling` section for that node pool.

  2. Run `gkectl update cluster`.




## Check cluster autoscaler behavior

You can determine what the cluster autoscaler is doing in several ways.

### Check cluster autoscaler logs

First, find the name of the cluster autoscaler Pod:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods -n USER_CLUSTER_NAME | grep cluster-autoscaler
    

Check logs on the cluster autoscaler Pod:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG logs cluster-autoscaler-POD_NAME --container cluster-autoscaler -n USER_CLUSTER_NAME
    

Replace POD_NAME with the name of the cluster autoscaler Pod.

### Check the configuration map

The cluster autoscaler publishes the `kube-system/cluster-autoscaler-status` configuration map.

To see the configuration map:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get configmap cluster-autoscaler-status -n kube-system -o yaml
    

### Check cluster autoscale events.

You can check [cluster autoscale events](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-events-are-emitted-by-ca):

  * On pods (particularly those that cannot be scheduled, or on underutilized nodes)
  * On nodes
  * On the `kube-system/cluster-autoscaler-status` config map.



## Limitations

The cluster autoscaler has the following limitations:

  * Custom scheduling with altered [filters](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#filter) is not supported.

  * Nodes do not scale up if Pods have a [`PriorityClass`](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/#priorityclass) value below `-10`. Learn more in [How does Cluster Autoscaler work with Pod Priority and Preemption?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption).

  * Auto-scaling for Windows node pools is not supported.




## Troubleshooting

  * Occasionally, the cluster autoscaler cannot scale down completely and an extra node exists after scaling down. This can occur when required system Pods are scheduled onto different nodes, because there is no trigger for any of those Pods to be moved to a different node. See [I have a couple of nodes with low utilization, but they are not scaled down. Why?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#i-have-a-couple-of-nodes-with-low-utilization-but-they-are-not-scaled-down-why). To work around this limitation, you can configure a [Pod disruption budget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).

  * If you are having problems with downscaling your cluster, see [Pod scheduling and disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#scheduling-and-disruption). You might have to add a `PodDisruptionBudget` for the `kube-system` Pods. For more information about manually adding a `PodDisruptionBudget` for the `kube-system` Pods, see the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-to-set-pdbs-to-enable-ca-to-move-kube-system-pods).

  * When scaling down, cluster autoscaler respects scheduling and eviction rules set on Pods. These restrictions can prevent a node from being deleted by the autoscaler. A node's deletion could be prevented if it contains a Pod with any of these conditions:

    * The Pod's [affinity or anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) rules prevent rescheduling.

    * The Pod has local storage.

    * The Pod is not managed by a [controller](https://kubernetes.io/docs/concepts/workloads/pods/#pods-and-controllers) such as a Deployment, StatefulSet, Job, or ReplicaSet.

    * The Pod is in kube-system namespace and does not have a [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work)

  * An application's PodDisruptionBudget might prevent autoscaling. If deleting nodes would cause the budget to be exceeded, the cluster does not scale down.




## More information

For more information about cluster autoscaler and preventing disruptions, see the following questions in the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md):

  * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
  * [Does Cluster autoscaler work with PodDisruptionBudget in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)
  * [What types of Pods can prevent Cluster autoscaler from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
