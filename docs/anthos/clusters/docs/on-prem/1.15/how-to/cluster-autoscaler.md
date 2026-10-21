---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/cluster-autoscaler/
title: Enable cluster autoscaler \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:55.587657+00:00
---

# Enable cluster autoscaler  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/cluster-autoscaler/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Enable cluster autoscaler Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/cluster-autoscaler)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/cluster-autoscaler)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows you how to autoscale your clusters. To learn about how the cluster autoscaler works, refer to [Overview of cluster autoscaling](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/cluster-autoscaler).

Cluster autoscaling resizes the number of nodes in a given node pool based on the demands of your workloads. You specify `minReplicas` and `maxReplicas` values for each node pool in your cluster.

For an individual node pool, `minReplicas` must be ≥ 1. However, the sum of the untainted user cluster nodes at any given time must be at least 3. This means the sum of the `minReplicas` values for all autoscaled node pools, plus the sum of the `replicas` values for all non-autoscaled node pools, must be at least 3.

## Create a user cluster with autoscaling

To create a user cluster with autoscaling, add the `autoscaling` field to the `nodePools` section in the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-autoscaling-section).
    
    
    nodePools:
    - name: pool‐1
      …
      replicas: 3
      ...
      autoscaling:
        minReplicas: 1
        maxReplicas: 5
    

This configuration creates a node pool with 3 replicas, and applies autoscaling with the minimum node pool size as 1 and the maximum node pool size as 5.

The `minReplicas` value must be ≥ 1.

## Add a node pool with autoscaling

To add a node pool with autoscaling to an existing cluster:

  1. Edit the user cluster configuration file to add a new node pool, and include the `autoscaling` field. Adapt the values of `minReplicas` and `maxReplicas` as needed.
         
         nodePools:
         - name: my-new-node-pool
           …
           replicas: 3
           ...
           autoscaling:
             minReplicas: 1
             maxReplicas: 5
         

  2. Run the following command:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




## Enable an existing node pool for autoscaling

To enable autoscaling for a node pool in an existing cluster:

  1. Edit a specific `nodePool` in the user cluster configuration file, and include the `autoscaling` field. Adapt the values of `minReplicas` and `maxReplicas` as needed.
         
         nodePools:
         - name: my-existing-node-pool
           …
           replicas: 3
           ...
           autoscaling:
             minReplicas: 1
             maxReplicas: 5
         

  2. Run the following command:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         


**Note:** You cannot modify replicas for an existing node pool while adding autoscaling.

## Disable autoscaling for an existing node pool

To disable autoscaling for a specific node pool:

  1. Edit the user cluster configuration file and remove the `autoscaling` field for that node pool.

  2. Run the `gkectl update cluster` command.




## Check cluster autoscaler behavior

You can determine what the cluster autoscaler is doing in several ways.

### Check cluster autoscaler logs

First, find the name of the cluster autoscaler Pod. Run this command, replacing `USER_CLUSTER_NAME with the user cluster name:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods -n USER_CLUSTER_NAME | grep cluster-autoscaler
    

To check logs on the cluster autoscaler Pod, replacing POD_NAME with the Pod name:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG logs cluster-autoscaler-POD_NAME --container cluster-autoscaler -n USER_CLUSTER_NAME
    

### Check the configuration map

The cluster autoscaler publishes the `kube-system/cluster-autoscaler-status` configuration map. To see this map, run this command:
    
    
    kubectl --kubeconfig USER_KUBECONFIG get configmap cluster-autoscaler-status -n kube-system -o yaml
    

### Check cluster autoscale events.

You can check [cluster autoscale events](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-events-are-emitted-by-ca):

  * On pods (particularly those that cannot be scheduled, or on underutilized nodes)
  * On nodes
  * On the `kube-system/cluster-autoscaler-status` config map.



## Troubleshooting

See the following troubleshooting information for cluster autoscaler:

  * You might be experiencing one of the [limitations for cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#limitations).
  * If you are having problems with downscaling your cluster, see [Pod scheduling and disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#scheduling-and-disruption). You might have to add a `PodDisruptionBudget` for the `kube-system` Pods. For more information about manually adding a `PodDisruptionBudget` for the `kube-system` Pods, see the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-to-set-pdbs-to-enable-ca-to-move-kube-system-pods).
  * When scaling down, cluster autoscaler respects scheduling and eviction rules set on Pods. These restrictions can prevent a node from being deleted by the autoscaler. A node's deletion could be prevented if it contains a Pod with any of these conditions: 
    * The Pod's affinity or anti-affinity rules prevent rescheduling.
    * The Pod has local storage.
    * The Pod is not managed by a Controller such as a Deployment, StatefulSet, Job or ReplicaSet.



For more information about cluster autoscaler and preventing disruptions, see the following questions in the [Kubernetes cluster autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md):

  * [How does scale-down work?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-scale-down-work)
  * [Does Cluster autoscaler work with PodDisruptionBudget in scale-down?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#does-ca-work-with-poddisruptionbudget-in-scale-down)
  * [What types of Pods can prevent Cluster autoscaler from removing a node?](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-types-of-pods-can-prevent-ca-from-removing-a-node)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
