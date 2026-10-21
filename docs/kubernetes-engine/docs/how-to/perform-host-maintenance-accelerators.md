---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators/
title: Perform host maintenance for nodes running training and inference workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:11.006580+00:00
---

# Perform host maintenance for nodes running training and inference workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Perform host maintenance for nodes running training and inference workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to perform host maintenance of the underlying Compute Engine instances for nodes in Google Kubernetes Engine (GKE) clusters. You only need to actively manage this maintenance for certain types of Compute Engine instances that don't live migrate, including instances with GPUs and TPUs. The strategies described in this document work well for training and inference workloads. If you only need to manually perform host maintenance for an individual node, or your workloads can tolerate automatic host maintenance, see [Understand how to do host maintenance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

These strategies perform host maintenance for groups of nodes, and, optionally, initiate GKE cluster upgrades.

Use the parallel strategy for the nodes of workloads where you can have one single period of downtime, such as for the nodes of training workloads. Use the rolling strategy for the nodes of workloads where you can have batches of downtime while maintaining availability of the majority of resources, such as for the nodes of inference workloads.

**Note:** For [TPU multi-host slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) and GPU node pools that use the [NVIDIA Multi-Node NVLink (MNNVL) system](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html), nodes have a shared lifecycle and articulate together. Plan your update strategy to perform updates for these groups of nodes at the same time.

## Use a parallel strategy to update the nodes of training workloads

This strategy performs changes simultaneously for a group of nodes that use accelerators. You can use this strategy for training workloads. Or, you can use it for other types of workloads where the least disruptive method of performing changes is to have a single window of complete downtime for all nodes in the group and the workloads that run on them.

The strategy follows these high-level steps:

  1. **Stop workloads** : select the node pools and either stop the workloads running on them or move the workloads to other nodes that remain available.
  2. **Trigger host maintenance** : apply the maintenance label to all selected nodes at the same time and wait for the process to complete on all nodes.
  3. **Upgrade the GKE version** : change the GKE version of the nodes.
  4. **Restart workloads** : after all host maintenance and upgrades finish, restart your workloads.



The provided instructions perform changes for a single node pool. However, you can adapt the steps to perform changes for multiple node pools at the same time. Ensure that, before you begin these steps, you have at least a few hours where this workload doesn't need to run on these nodes.

To minimize disruption while receiving critical changes for both the underlying Compute Engine instances and the GKE nodes, use this period of downtime to perform both the host maintenance and GKE version upgrades. However, you can perform only host maintenance if you don't want to upgrade the version of your GKE nodes.

### Considerations before you begin

Review the following considerations before you begin:

  * **Avoid redeploying workloads** : to avoid unnecessary delays due to [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/), don't redeploy any workloads until you've completed all steps.
  * **Plan for disruption** : ensure that your workloads can be disrupted for a period of time. These steps take multiple hours to complete, primarily due to the time required for host maintenance.



### Perform updates for all nodes simultaneously

To perform host maintenance and, optionally, GKE version upgrades, complete the following steps:

  1. **Prepare your workloads** : stop your workloads, or ensure that they have taken a recent snapshot or checkpoint.
  2. **Start and monitor host maintenance** :

     * **Sub-blocks from reservations that use grouped maintenance scheduling** : trigger maintenance across reservations, reservation blocks, or reservation sub-blocks by using the corresponding [`gcloud compute reservations`](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations) sub-command. For example, the following command starts maintenance for a sub-block:
           
           gcloud compute reservations sub-blocks perform-maintenance RESERVATION_NAME \
               --block-name=BLOCK_NAME \
               --sub-block-name=SUB_BLOCK_NAME \
               --zone=ZONE
           

Replace the following:

       * `RESERVATION_NAME`: the name of the reservation.
       * `BLOCK_NAME`: the name of the reservation block.
       * `SUB_BLOCK_NAME`: the name of the reservation sub-block.
       * `ZONE`: the zone where the reservation exists.

Compute Engine begins draining and updating any instances in the sub-block simultaneously. This process might take a few hours.

To monitor, view the state of the maintenance by checking the `upcomingGroupMaintenance` metadata field in the reservation resources. For more information, see [View maintenance state](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#view-maintenance).

     * **Instances that use independent maintenance scheduling** : trigger maintenance for on-demand instances or for reservations that don't use sub-blocks by applying the `cloud.google.com/perform-maintenance=true` label to the nodes in your node pool:

**Warning:** Instances that have been configured to use grouped maintenance scheduling (such as A4X, A4X Max, TPU v6e and TPU7x), are tightly coupled and must be maintained together as a single unit. You must use [sub-block level maintenance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#start-maintenance).
           
           kubectl label nodes -l cloud.google.com/gke-nodepool=NODE_POOL_NAME cloud.google.com/perform-maintenance=true --overwrite
           

Compute Engine begins draining and updating the underlying instances simultaneously. This process might take a few hours. For more information, see [Process of graceful termination](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#process-termination).

To monitor the status of the maintenance, check the nodes. GKE removes the maintenance label when maintenance completes, if it was applied. When maintenance finishes, you can find a log with the following message in Cloud Logging:
           
           Maintenance window has completed for this instance. All maintenance
           notifications on the instance have been removed.
           

  3. **Optional: Upgrade the version of the GKE nodes** : follow the instructions to upgrade the GKE version of the nodes.




## Use a rolling strategy to update the nodes of inference workloads

This strategy outlines a manual approach to performing maintenance on GKE nodes running inference workloads. It involves updating nodes in batches to maintain service availability. This method is best suited for workloads that can tolerate a certain percentage of replicas being temporarily offline.

The strategy follows these high-level steps:

  1. **Identify and batch nodes** : choose the node pools to update. Group the nodes into batches sized according to your workload's failure tolerance.
  2. **Iterate through batches** : for each batch, apply the maintenance label and monitor the batch of nodes until the label is removed.
  3. **Upgrade the GKE version** : after all batches complete host maintenance, change the version of the GKE nodes.



### Considerations before you begin

Review the following considerations before you begin:

  * **Understand your deployment** : success requires detailed knowledge of your workload distribution, replica placement, and failure domains. Ensure that you maintain sufficient serving capacity throughout the process.
  * **Plan batch sizes** : update nodes in batches. The size of each batch is determined by your workload's fault tolerance. Factors to consider include the following: 
    * The number of replicas per serving model.
    * The distribution of replicas across nodes and failure domains.
    * [PodDisruptionBudgets](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) can help enforce the maximum number of Pods that are down simultaneously.
    * **Recommendation** : to simplify management, consider dedicating different node pools to different sets of replicas, which lets you isolate failure domains at the node pool level.
  * **Calculate time constraints** : consider the following timing factors: 
    * Each batch can take several hours to complete the host maintenance step.
    * Calculate the minimum batch size to help ensure that all maintenance finishes within required deadlines: 
      1. `MAINTENANCE_BLOCKS = floor(HOURS_TO_MAINTENANCE / 4)` (where `HOURS_TO_MAINTENANCE` is the total time available).
      2. `MIN_PER_BATCH = TOTAL_NODE_COUNT / MAINTENANCE_BLOCKS`
    * Your chosen batch size must be equal to or greater than `MIN_PER_BATCH`.
  * **Review specific workload types** : consider the following for the respective configuration types: 
    * **Mixture of Experts (MOE)** : ensure that your batching strategy maintains the minimum required number of replicas for each model.
    * **Disaggregated serving** : ensure that you track all replicas involved in the disaggregated setup when planning batches.
    * **Multi-host node pools (TPU, MNNVL)** : for these configurations, you'll likely take down an entire node pool at a time. Plan your failure domains across multiple node pools accordingly.



### Perform rolling updates in batches

To perform rolling host maintenance updates, you can update your capacity from reservations that use grouped maintenance scheduling in batches of one or more sub-blocks, or you can update specific sets of nodes in the cluster by name with independent maintenance scheduling.

Choose the appropriate strategy for your resources:

#### Update reservations in batches of sub-blocks

To perform rolling host maintenance for capacity reservations in batches of sub-blocks, complete the following steps:

  1. **Identify reservations for maintenance** : Identify the capacity reservation name, and the reservation blocks or reservation sub-blocks used by the GKE cluster. To do this, perform a lookup using GKE node labels and the [`gcloud compute reservations`](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations) command:

     1. List the reservation name and the physical block and sub-block topology IDs from the nodes in your node pool:
            
            kubectl get nodes -l cloud.google.com/gke-nodepool=NODE_POOL_NAME \
                -o custom-columns='NAME:.metadata.name,RESERVATION:.metadata.labels.cloud\.google\.com/reservation-name,BLOCK_ID:.metadata.labels.cloud\.google\.com/gce-topology-block,SUBBLOCK_ID:.metadata.labels.cloud\.google\.com/gce-topology-subblock'
            

Replace `NODE_POOL_NAME` with the name of the node pool.

Note the output values: the reservation name (for example, `nvidia-gb300-m7kp2xq9vd4j1`), the block ID (for example, `3f2a8c9b1d4e0756f8a2b3c1d9e4f0a5`), and the sub-block ID (for example, `e7b91f4a3c2d58069e1a4b7f3d2c8056`).

     2. To identify the reservation block resource name, query the Compute Engine reservation blocks list using the reservation name and filter by the block ID:
            
            gcloud compute reservations blocks list RESERVATION_NAME \
                --zone=ZONE \
                --project=PROJECT_ID \
                --filter="physicalTopology.block=BLOCK_ID"
            

Replace the following:

        * `RESERVATION_NAME`: the name of the reservation.
        * `ZONE`: the zone where the reservation exists.
        * `PROJECT_ID`: the project ID where the reservation exists.
        * `BLOCK_ID`: the block ID retrieved from the node labels.

Record the name of the block from the output.

     3. To identify the reservation sub-block resource name, query the reservation sub-blocks list using the reservation name and block name, and filter by the sub-block ID:
            
            gcloud compute reservations sub-blocks list RESERVATION_NAME \
                --block-name=BLOCK_NAME \
                --zone=ZONE \
                --project=PROJECT_ID \
                --filter="physicalTopology.subBlock=SUBBLOCK_ID"
            

Replace the following:

        * `RESERVATION_NAME`: the name of the reservation.
        * `BLOCK_NAME`: the reservation block resource name.
        * `ZONE`: the zone where the reservation exists.
        * `PROJECT_ID`: the project ID where the reservation exists.
        * `SUBBLOCK_ID`: the sub-block ID retrieved from the node labels.

The output displays details about the matching reservation sub-block, including its resource name.

  2. **Divide reservations into batches** : Divide the identified capacity reservation sub-blocks into equal batches. Determine the batch size using the formula described in the **Calculate time constraints** list item in the earlier Considerations before you begin section. Each batch corresponds to one or more reservation sub-blocks, and each batch must be at least the size of a sub-block.

  3. **Perform host maintenance** : For each batch, complete the following steps:

     1. Select a batch of reservation sub-blocks and trigger host maintenance. You can trigger maintenance across your reservations, reservation blocks, or reservation sub-blocks. For machine types such as A4X, A4X Max, TPU v6e and TPU7x, you must trigger maintenance in this manner. Maintenance is performed in groups of sub-blocks. Use the [`gcloud compute reservations sub-blocks perform-maintenance`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/sub-blocks/perform-maintenance) command:
            
            gcloud compute reservations sub-blocks perform-maintenance RESERVATION_NAME \
                --block-name=BLOCK_NAME \
                --sub-block-name=SUB_BLOCK_NAME \
                --zone=ZONE
            

Replace the following:

        * `RESERVATION_NAME`: the name of the reservation.
        * `BLOCK_NAME`: the name of the reservation block.
        * `SUB_BLOCK_NAME`: the name of the reservation sub-block.
        * `ZONE`: the zone where the reservation exists.

Compute Engine begins draining and updating any instances in the sub-block simultaneously. This process might take a few hours.

     2. Monitor the status of the maintenance by viewing the state of the maintenance by checking the `upcomingGroupMaintenance` metadata field in the reservation resources. For more information, see [View reservation maintenance state](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#view-maintenance).

     3. Repeat the previous steps for each remaining batch until you've completed host maintenance for all batches.

  4. **Optional: Upgrade the version of the GKE nodes** : perform this step only after host maintenance completes for all reservation sub-blocks, to avoid scenarios where the GKE nodes are deployed on hosts that haven't finished maintenance yet. Follow the instructions to upgrade the GKE version of the nodes.




#### Update nodes in batches

To perform rolling host maintenance for on-demand instances or reservations that don't support sub-blocks in batches, complete the following steps:

  1. **Identify nodes for maintenance** : Identify all nodes where you want to perform maintenance, and save this list. To identify nodes, use any of the following methods or manually select them:

     * Get all nodes in the cluster that use accelerators (TPUs or GPUs):
           
           kubectl get nodes -o json | jq -r '.items[] | select(.spec.taints[]? | select(.key=="nvidia.com/gpu" or .key=="google.com/tpu")) | .metadata.name'
           

     * Get all nodes in a specific node pool:
           
           kubectl get nodes -l cloud.google.com/gke-nodepool=NODE_POOL_NAME --no-headers -o custom-columns=":metadata.name"
           

Replace `NODE_POOL_NAME` with the name of the node pool.

     * Get all nodes with a specific label:
           
           kubectl get nodes -l LABEL -o jsonpath='{.items[*].metadata.name}'
           

Replace `LABEL` with the node label.

  2. **Divide nodes into batches** : Divide the identified nodes into equal batches. Determine the batch size using the formula described in the **Calculate time constraints** list item in the earlier Considerations before you begin section.

  3. **Perform host maintenance** : For each batch, complete the following steps:

     1. Select a batch of nodes and trigger maintenance at the instance layer using the `instances` API by applying the maintenance label:

**Warning:** Instances that have been configured to use grouped maintenance scheduling (such as A4X, A4X Max, TPU v6e and TPU7x), are tightly coupled and must be maintained together as a single unit. You must use [sub-block level maintenance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#start-maintenance).
            
            kubectl label nodes LIST_OF_NODES_IN_BATCH cloud.google.com/perform-maintenance=true --overwrite
            

Replace `LIST_OF_NODES_IN_BATCH` with a space-separated list of nodes from the batch. For example, `node-1 node-2 node-3`.

Compute Engine begins draining and updating the underlying instances simultaneously. This process might take a few hours. For more information, see [Process of graceful termination](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#process-termination).

     2. Monitor the status of host maintenance. GKE removes the maintenance label when maintenance completes, if it was applied. When maintenance finishes, you can find a log with the following message in Logging:
            
            Maintenance window has completed for this instance. All maintenance
            notifications on the instance have been removed.
            

     3. Repeat the previous steps for each remaining batch until you've completed host maintenance for all batches.

  4. **Optional: Upgrade the version of the GKE nodes** : perform this step only after host maintenance completes for all nodes, to avoid scenarios where the GKE nodes are deployed on hosts that haven't finished maintenance yet. Follow the instructions to upgrade the GKE version of the nodes.




## Upgrade the GKE version of the nodes

Consider the number of nodes that you want to upgrade at the same time. With the parallel strategy, you performed host maintenance for your entire node pool or multiple node pools at the same time. With the rolling strategy, you performed host maintenance in batches. Determine which upgrade method that you'll use based on the size of the groups of nodes:

  * **Parallel strategy** : if your node pools each have 100 or fewer nodes per zone, use surge upgrades. If your node pools each have greater than 100 nodes per zone, delete and re-create the node pools.
  * **Rolling strategy** : if your batches have 100 nodes, per zone, per node pool, or less, use surge upgrades. If your batches have greater than 100 nodes, per zone, per node pool, delete and re-create the nodes.



### Use surge upgrades

  1. [Configure surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#surge), using the [`maxUnavailable`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#max-unavailable) setting to determine how many nodes can be unavailable at the same time, per zone, in a node pool. For example, if you have 18 nodes in one zone in a node pool, set the value of the `maxUnavailable` field to `18`.

This setting works best when using capacity from a reservation where you don't have excess capacity. For more information about why to use this setting, see [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

  2. Upgrade the node pool by running the following command. If you want to upgrade multiple node pools, run this command for each node pool:
         
         gcloud container clusters upgrade CLUSTER_NAME \
             --node-pool NODE_POOL_NAME \
             --cluster-version VERSION \
             --location CONTROL_PLANE_LOCATION \
             --quiet
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `NODE_POOL_NAME`: the name of the node pool.
     * `VERSION`: a recommended auto-upgrade target for the node pool. For more information, see [Get upgrades information for Standard cluster node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info-nodes). If your cluster doesn't have a recommended auto-upgrade target, check the latest _Version updates_ entries in the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).
     * `CONTROL_PLANE_LOCATION`: the location of the control plane of your cluster.



### Delete and re-create the nodes

Delete the node pool and re-create it using the later version:

  1. Delete the node pool:
         
         gcloud container node-pools delete NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION
         

  2. Re-create the node pool, passing the new version by using the `--cluster-version` flag. Pass the recommended auto-upgrade target for the node pool. For more information, see [Get upgrades information for Standard cluster node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info-nodes). If your cluster doesn't have a recommended auto-upgrade target, check the latest _Version updates_ entries in the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
