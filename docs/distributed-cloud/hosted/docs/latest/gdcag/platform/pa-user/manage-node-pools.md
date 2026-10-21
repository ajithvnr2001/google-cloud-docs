---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools/
title: Manage node pools \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:57.232999+00:00
---

# Manage node pools  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

When you create a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster, the number of nodes and type of nodes that you specify create the first node pool of the cluster. You can perform the following node pool tasks for an existing cluster as its compute requirements change:

  * **Add a new node pool** : Add new node pools as the demand for your cluster workloads increases.

  * **View a node pool** : View the characteristics and state of your existing node pools.

  * **Resize a node pool** : Manually upscale or downscale your node pools to adapt to workload traffic fluctuations.

  * **Delete a node pool** : Remove node pools if the demand for your cluster workloads decreases, or you want to delete machine types that are no longer prudent for your container operations.




For more information about node pools in a cluster, see [About nodes](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#about-nodes).

This document is for application developers within the application operator group and IT administrators within the platform administrator group who are responsible for managing Kubernetes clusters within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to manage node pools in a Kubernetes cluster. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

To create, delete, edit, or view the node pools of a shared cluster, contact your Organization IAM Admin to request the **User Cluster Admin** (`user-cluster-admin`) role. This role isn't bound to a namespace.

#### Standard cluster roles

Contact your Project IAM Admin to request the following roles:

  * **Standard Cluster Admin** (`standard-cluster-admin`): create, delete, edit, or view the node pools of a standard cluster.

  * **Cluster Developer** (`cluster-developer`): create, delete, edit, or view a standard cluster. This role is required to view the cluster's node pool details from the GDC console.




These roles are bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * Use the Kubernetes cluster name to replace `KUBERNETES_CLUSTER_NAME` in these instructions.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the management API server kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




## Add a node pool

To add a node pool to an existing Kubernetes cluster, complete the following steps:

### Console

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project or organization.

Standard clusters are project-scoped and shared clusters are organization-scoped. Select the correct scope to view the appropriate Kubernetes cluster type.

  2. In the navigation menu, select **Kubernetes Engine > Clusters**.

  3. Click the cluster from the cluster list. The **Cluster details** page is displayed.

  4. Select **Node pools > Add node pool**.

  5. Assign a name for the node pool. You can't modify the name after you create the node pool.

  6. Specify the number of worker nodes to create in the node pool.

  7. Select your machine class that best suits your workload requirements. The machine classes show in the following settings:

     * Machine type
     * vCPU
     * Memory
  8. Click **Save**.




### API

  1. Open the `Cluster` custom resource spec with the `kubectl` CLI using the interactive editor:
         
         kubectl edit clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
             -n KUBERNETES_CLUSTER_NAMESPACE \
             --kubeconfig MANAGEMENT_API_SERVER
         

Replace the following:

     * `KUBERNETES_CLUSTER_NAME`: the name of the cluster.
     * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the Kubernetes cluster is hosted.
  2. Add a new entry in the `nodePools` section:
         
         nodePools:
         # Several lines of code are omitted here.
         - machineTypeName: MACHINE_TYPE
           name: NODE_POOL_NAME
           nodeCount: NUMBER_OF_WORKER_NODES
           taints: TAINTS
           labels: LABELS
           acceleratorOptions:
             gpuPartitionScheme: GPU_PARTITION_SCHEME
         

Replace the following:

     * `MACHINE_TYPE`: the machine type for the worker nodes of the node pool. View the [available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) for what is available to configure.
     * `NODE_POOL_NAME`: the name of the node pool.
     * `NUMBER_OF_WORKER_NODES`: the number of worker nodes to provision in the node pool.
     * `TAINTS`: the taints to apply to the nodes of this node pool. This is an optional field.
     * `LABELS`: the labels to apply to the nodes of this node pool. It contains a list of key-value pairs. This is an optional field.
     * `GPU_PARTITION_SCHEME`: the GPU partitioning scheme, if you're running GPU workloads. For example, `mixed-2`. The GPU is not partitioned if this field is not set. For available Multi-Instance GPU (MIG) profiles, see [Supported MIG profiles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#mig-profiles).
**Note:** You can't edit node configurations, such as GPU partitioning, after the node pool is created.
  3. Save the file and exit the editor.




## View node pools

To view existing node pools in a Kubernetes cluster, complete the following steps:

### Console

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project or organization.

Standard clusters are project-scoped and shared clusters are organization-scoped. Select the correct scope to view the appropriate Kubernetes cluster type.

  2. In the navigation menu, select **Kubernetes Engine > Clusters**.

  3. Click the cluster from the cluster list. The **Cluster details** page is displayed.

  4. Select **Node pools**.




The list of node pools running in the cluster is displayed. You can manage the node pools of the cluster from this page.

### API

  * View the node pools of a specific Kubernetes cluster:
        
        kubectl get clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
            -n KUBERNETES_CLUSTER_NAMESPACE \
            -o json --kubeconfig MANAGEMENT_API_SERVER | \
            jq .status.workerNodePoolStatuses
        

Replace the following:

    * `KUBERNETES_CLUSTER_NAME`: the name of the cluster.
    * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.

The output is similar to the following:
    
    [
      {
        "conditions": [
          {
            "lastTransitionTime": "2023-08-31T22:16:17Z",
            "message": "",
            "observedGeneration": 2,
            "reason": "NodepoolReady",
            "status": "True",
            "type": "Ready"
          },
          {
            "lastTransitionTime": "2023-08-31T22:16:17Z",
            "message": "",
            "observedGeneration": 2,
            "reason": "ReconciliationCompleted",
            "status": "False",
            "type": "Reconciling"
          }
        ],
        "name": "worker-node-pool",
        "readyNodes": 3,
        "readyTimestamp": "2023-08-31T18:59:46Z",
        "reconcilingNodes": 0,
        "stalledNodes": 0,
        "unknownNodes": 0
      }
    ]
    




## Resize node pools

You can manually resize node pools in a Kubernetes cluster by upscaling or downscaling the pool. You can't select a specific node to remove when downscaling a node pool.

**Important:** Autoscaling your Kubernetes cluster node pools is not supported.

To scale a node pool in an existing cluster, complete the following steps:

###  Console 

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project or organization.

Standard clusters are project-scoped and shared clusters are organization-scoped. Select the correct scope to view the appropriate Kubernetes cluster type.

  2. In the dashboard, select the project in which the cluster you intend to edit exists.

  3. In the navigation menu, select **Kubernetes Engine > Clusters**.

  4. Select the cluster name that the node pool is associated with. The **Cluster details** page is displayed.

  5. Click the **Node pools** tab.

  6. Select the _edit_ **Edit** icon for the node pool you want to resize. The **Edit node pool** prompt is displayed.

  7. Update the **Number of nodes** field to reflect the new amount of nodes required in the node pool. You can increase or decrease the number of nodes to fit your workload requirements.

**Note:** Downscaling your node pool can cause resource issues if the remaining nodes don't have enough memory to handle your existing workloads.
  8. Click **Save**.

  9. Navigate back to the **Node pools** tab for your cluster and confirm the resized node pool has the `Ready` status and has the correct number of nodes. It can take a few minutes for the node pool to scale to your specification.

![Confirm your node pool is ready by using the console.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/node-pool-status.png)




###  API 

  1. Open the `Cluster` custom resource spec with the kubectl CLI using the interactive editor:
         
         kubectl edit clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
             -n KUBERNETES_CLUSTER_NAMESPACE \
             --kubeconfig MANAGEMENT_API_SERVER
         

Replace the following:

     * `KUBERNETES_CLUSTER_NAME`: the name of the cluster that hosts the node pool.
     * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the Kubernetes cluster is hosted.
  2. Update the `nodeCount` field for the node pool to resize:
         
         nodePools:
         # Several lines of code are omitted here.
         - machineTypeName: n2-standard-2-gdc
           name: nodepool-1
           nodeCount: NUMBER_OF_WORKER_NODES
         

Replace `NUMBER_OF_WORKER_NODES` with the updated number of worker nodes to provision in the node pool.

  3. Save the file and exit the editor.

  4. Verify your node scaling is complete by checking the node pool's configuration:
         
         kubectl get clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
             -n KUBERNETES_CLUSTER_NAMESPACE -o json \
             --kubeconfig MANAGEMENT_API_SERVER | jq .status.workerNodePoolStatuses
         

Confirm the `readyNodes` number reflects the amount of nodes you set for the node pool. It can take a few minutes for the node pool to scale to your specification.




## Delete a node pool

Deleting a node pool deletes the nodes and routes to them. These nodes evict and reschedule any pods running on them. If the pods have specific node selectors, the pods might remain in a non-schedulable condition if no other node in the cluster satisfies the criteria.

**Important:** Control plane node pools and load balancer node pools are critical to a cluster's function and consequently can't be removed from a cluster. You can only delete worker node pools.

Ensure you have at least three worker nodes before deleting a node pool to ensure your cluster has enough compute space to run effectively.

To delete a node pool, complete the following steps:

###  Console 

  1. In the [project picker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-projects#select-project), select your project or organization.

Standard clusters are project-scoped and shared clusters are organization-scoped. Select the correct scope to view the appropriate Kubernetes cluster type.

  2. In the navigation menu, select **Kubernetes Engine > Clusters**.

  3. Click the cluster that is hosting the node pool you want to delete.

  4. Select **Node pools**.

  5. Click _delete_ **Delete** next to the node pool to delete.




###  API 

  1. Open the `Cluster` custom resource spec with the kubectl CLI using the interactive editor:
         
         kubectl edit clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
             -n KUBERNETES_CLUSTER_NAMESPACE \
             --kubeconfig MANAGEMENT_API_SERVER
         

Replace the following:

     * `KUBERNETES_CLUSTER_NAME`: the name of the cluster.
     * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the Kubernetes cluster is hosted.
  2. Remove the node pool entry from the `nodePools` section. For example, in the following snippet, you must remove the `machineTypeName`, `name`, and `nodeCount` fields:
         
         nodePools:
         # Several lines of code are omitted here.
         - machineTypeName: n2-standard-2-gdc
           name: nodepool-1
           nodeCount: 3
         

Be sure to remove all fields for the node pool you are deleting.

  3. Save the file and exit the editor.




## What's next

  * [Maintain Kubernetes clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Isolate container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/isolate-container-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
