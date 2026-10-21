---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-taints/
title: Control scheduling with taints and tolerations \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:58.782684+00:00
---

# Control scheduling with taints and tolerations  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-taints/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Control scheduling with taints and tolerations Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/node-taints)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/node-taints)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page provides an overview of [taints and tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) on Google Distributed Cloud. When you schedule workloads to be deployed on your cluster, node taints help you control which nodes they are allowed to run on.

## Overview

When you submit a workload to run in a cluster, the [scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/) determines where to place the Pods associated with the workload. The scheduler is free to place a Pod on any node that satisfies the Pod's CPU, memory, and custom resource requirements.

If your cluster runs a variety of workloads, you might want to exercise some control over which workloads can run on a particular pool of nodes.

A **node taint** lets you mark a node so that the scheduler avoids or prevents using it for certain Pods. A complementary feature, _tolerations_ , lets you designate Pods that can be used on "tainted" nodes.

Taints and tolerations work together to ensure that Pods are not scheduled onto inappropriate nodes.

Taints are _key-value pairs_ associated with an _effect_. The following table lists the available effects:

Effect | Description  
---|---  
`NoSchedule` | Pods that do not tolerate this taint are not scheduled on the node; existing Pods are not evicted from the node.  
`PreferNoSchedule` | Kubernetes avoids scheduling Pods that do not tolerate this taint onto the node.  
`NoExecute` | The Pod is evicted from the node if it is already running on the node, and is not scheduled onto the node if it is not yet running on the node.  
  
## Advantages of setting node taints in Google Distributed Cloud

Although you can set node taints using the [`kubectl taint`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint) command, using `gkectl` or the Google Cloud console to set a node taint has the following advantages over `kubectl`:

  * Taints are preserved when a node is restarted or replaced.
  * Taints are created automatically when a node is added to a node pool.
  * When using `gkectl` to add taints, the taints are created automatically during cluster autoscaling. (Autoscaling for nodepools created in the Google Cloud console isn't available currently.)



## Set node taints

You can set node taints in a node pool either when you create a user cluster or after the cluster is created. This section shows adding taints to clusters that have already been created, but the process is similar when creating new clusters.

You can either [add a new node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools#add_a_node_pool) and set a taint, or you can [update an existing node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools#update_a_node_pool) and set a taint. Before you add another node pool, [verify that enough IP addresses are available](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster#verify_ips) on the cluster.

If you created the cluster in the Google Cloud console, you can use the Google Cloud console to add or update a node pool.

### Set taints in a new node pool

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. Click add_box **Add node pool**.

  5. Configure the node pool:

     1. Enter the **Node pool name**.
     2. Enter the number of **vCPUs** for each node in the pool (minimum 4 per user cluster worker).
     3. Enter the **memory** size in mebibytes (MiB) for each node in the pool (minimum 8192 MiB per user cluster worker node and must be a multiple of 4).
     4. In the **Replicas** field, enter the number of nodes in the pool (minimum of 3).
     5. Select the **OS image type** : **Ubuntu Containerd** or **COS**.

**Note:** The **Ubuntu** OS Image type for node pools is unsupported in Google Distributed Cloud version 1.13. You must update your node pools to use either **Ubuntu Containerd** or **COS** for the OS Image type.
     6. Enter the **Boot disk size** in gibibytes (GiB) (default is 40 GiB).

  6. In the **Node pool metadata (optional)** section, click **\+ Add Taint**. Enter the **Key** , **Value** , and **Effect** for the taint. Repeat as needed.

  7. Optionally, click **\+ Add Kubernetes Labels**. Enter the **Key** and **Value** for the label. Repeat as needed.

  8. Click **Create**.

  9. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




### Command line

  1. In your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file), fill in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section.

You must specify the following fields:

     * `nodePools.[i].name`
     * `nodePools[i].cpus`
     * `nodePools.[i].memoryMB`
     * `nodePools.[i].replicas`

The following fields are optional. If you don't include [`nodePools[i].bootDiskSizeGB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-bootdisksizegb-field) or [`nodePools[i].osImageType`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-osimagetype-field), the default values are used.

  2. Fill in the [`nodePools[i].taints`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-taints-field) section. For example:
         
         nodePools:
         - name: "my-node-pool"
           taints:
           - key: "staging"
             value: "true"
             effect: "NoSchedule"
         

  3. Optionally, fill in the following sections:

     * `nodePools[i].labels`
     * `nodePools[i].bootDiskSizeGB`
     * `nodePools[i].osImageType`
     * `nodePools[i].vsphere.datastore`
     * `nodePools[i].vsphere.tags`
**Note:** The **Ubuntu** OS Image type for node pools is unsupported in Google Distributed Cloud version 1.13. You must update your node pools to use either **Ubuntu Containerd** or **COS** for the OS Image type.
  4. Run the following command:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `[ADMIN_CLUSTER_KUBECONFIG]` with the path of the kubeconfig file for your admin cluster.

     * `[USER_CLUSTER_CONFIG]` with the path of your user cluster configuration file.




### Set taints in an existing node pool

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. Click the **Nodes** tab.

  5. Click the name of the node pool that you want to modify.

  6. Click edit **Edit** next to the **Node pool metadata (optional)** section, and click **\+ Add Taint**. Enter the **Key** , **Value** , and **Effect** for the taint. Repeat as needed.

  7. Click **Done**.

  8. Click arrow_back to go back to the previous page.

  9. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




### Command line

  1. In your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file), go to the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section of the node pool that you want to update.

  2. Fill in the [`nodePools[i].taints`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-taints-field) For example:
         
         nodePools:
         - name: "my-node-pool"
           taints:
           - key: "staging"
             value: "true"
             effect: "NoSchedule"
         

  3. Run the following command:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `[ADMIN_CLUSTER_KUBECONFIG]` with the path of the kubeconfig file for your admin cluster.

     * `[USER_CLUSTER_CONFIG]` with the path of your user cluster configuration file.




## Configure Pods to tolerate a taint

You can configure Pods to tolerate a taint by including the `tolerations` field in the Pods' specification. In the following example, the Pod can be scheduled on a node that has the `dedicated=experimental:NoSchedule` taint:
    
    
    tolerations:
    - key: dedicated
      operator: Equal
      value: experimental
      effect: NoSchedule
    

For additional examples, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
