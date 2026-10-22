---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices/
title: Use dynamic slicing with a custom scheduler \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:18.151892+00:00
---

# Use dynamic slicing with a custom scheduler  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-dynamic-slices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Use dynamic slicing with a custom scheduler Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to use dynamic slicing by directly interacting with [Slice custom resources](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice). You can create slices, monitor partition states, and verify slice health.

Before following these instructions, ensure that you understand the [concepts of dynamic slicing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing).

## Why use dynamic slicing with a custom scheduler?

Use your own scheduler to manage Slice custom resources if you have complex scheduling requirements or if you want to integrate dynamic slicing with your existing scheduling infrastructure.

In case you prefer to use a scheduler instead of managing Slice custom resources directly, GKE provides integration with Kueue and Topology Aware Scheduling (TAS). For more information, see [Schedule dynamic slices with Kueue and TAS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-gke-dynamic-slicing).

## Overview of the workflow

To use dynamic slicing with a custom scheduler, you perform the following tasks in this document:

  1. Enable the slice controller.
  2. Create node pools with incremental provisioning.
  3. Create Slice custom resources based on your workload requirements. Apply the Slice custom resource to your cluster.
  4. Monitor the partition states and slice health.
  5. Delete the slice when you are done.



For more information about the fields and status of the Slice custom resource, see the [Slice custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice) reference information.

## Requirements

To use dynamic slicing in GKE, you must meet the following requirements:

  * Use a Standard cluster in the Rapid channel in one of the following versions: 
    * For dynamic super-slicing configuration (topologies equal to or larger than `4x4x4`), use version 1.35.2-gke.1842000 or later.
    * For dynamic sub-slicing configuration (topologies smaller than `4x4x4`), use version 1.36.0-gke.3712000 or later.
  * Use Ironwood (TPU7x) version.
  * Use the Container-Optimized OS image for your nodes.
  * To use incremental provisioning, use [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview#all_capacity_mode) reservations. All Capacity mode is a feature enabled by TPU Cluster Director.
  * For dynamic sub-slicing, ensure that your nodes have a pending maintenance events. [Monitor your instances for pending maintenance events](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#monitor-notification). If any of your nodes have a pending maintenance event with an end time between September 18, 2026 and September 30, 2026, you must manually [trigger the host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) on those nodes before you can use sub-slicing.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster in version 1.35.2-gke.1842000 or later, in the Rapid channel. To create a new cluster, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * Ensure you have sufficient quota for Ironwood (TPU7x) in your region.
  * If you plan to run multislice workloads, [install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.10.1 or later.
  * [Request TPU capacity in All Capacity mode](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation#confirm_your_capacity_reservation_draft).



## Enable the slice controller

To use dynamic slicing, enable the slice controller in your cluster.

  1. Update your cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=LOCATION \
             **--enable-slice-controller**
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `LOCATION`: the region with your [available TPU capacity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  2. Get credentials so that you can communicate with your cluster with `kubectl` commands:
         
         gcloud config set container/cluster CLUSTER_NAME
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=LOCATION
         

  3. In the output of the following command, verify that the `slices.accelerator.gke.io` value is present:
         
         kubectl get crd slices.accelerator.gke.io
         

The output is similar to the following:
         
         slices.accelerator.gke.io                2026-01-09T23:58:02Z
         




## Create node pools with incremental provisioning

This section describes how to create the TPU node pools with incremental provisioning. GKE converts all your TPU capacity into node pools of 16-node group of TPU VMs, or sub-blocks. GKE provisions these node pools even when it can't find all 16 healthy VMs by placing nodes on healthy parts of the host machine and incrementally provisioning unhealthy machines while they are repaired.

You can target your node pool to belong to any of the following:

  * A specific block of TPUs, which is exposed in All Capacity mode reservations. Block targeting allows GKE to create the node pool in any available sub-block within the specified block.
  * A specific sub-block, or a specific 16-node group of TPU VMs, of TPUs for more granular control.



### Create a workload policy

To create a TPU slice node pool with Ironwood (TPU7x), you must first create a workload policy with the `accelerator-topology-mode` field set to `provision_only`. This setting triggers the incremental provisioning process.

Create a workload policy:
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --project=PROJECT_ID \
            --region=REGION  \
            --type=HIGH_THROUGHPUT \
            --accelerator-topology=4x4x4 \
            --accelerator-topology-mode=provision_only
    

Replace the following:

  * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region for the workload policy.



In this command, do the following:

  * Always set the `accelerator-topology` field to `4x4x4` to match the total number of chips within a single sub-block.
  * Always set the `accelerator-topology-mode` field to `provision_only` to ensure the incremental provisioning process is triggered. When the `provision_only` field is set, the node pool provisions TPU nodes without forming ICI or OCS links.

**Note:** You don't need to create a new workload policy for every node pool. A workload policy is unique per project, per region, and per topology. You can reuse the same workload policy for multiple node pools that share these characteristics. To see the list of workload policies, use the `gcloud compute resource-policies list --filter="region:REGION"` command.

### Target your node pool to belong to a block or a sub-block

You can target specific sub-blocks or blocks within your All Capacity mode reservation.

  * **Target a block:** each node pool uses capacity from a specified block. GKE places the node pool within an available sub-block in that block. You must create as many node pools as there are sub-blocks in the block you want to use.
  * **Target a sub-block:** each node pool maps to a specific and available sub-block. When using sub-block targeting, GKE creates the node pool if at least one VM is healthy. Incremental provisioning helps ensure that all nodes are placed within the specified sub-block.




### Block

  1. To retrieve the name of the block in a reservation and the count of available sub-blocks in the block, complete the following steps in the [View the topology and health status of All Capacity Mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus) document:

     1. Identify the name of the block by [listing all reservation blocks](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_reservation_blocks) and copying the value in the `name:` field. This value is the name of the block or `BLOCK_NAME` in this document.

     2. Determine how many node pools to create by [describing a reservation block](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#describe_a_reservation_block) and identifying the value in the `reservationSubBlockCount` field. This value is the number of sub-blocks available. For example, the `reservationSubBlockCount: 4` value indicates that the block has four sub-blocks available, and you need to create four separate node pools.

  2. Set the reservation path:
         
         export RESERVATION_PATH="projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME"
         

Replace the following:

     * `RESERVATION_NAME`: the name of your TPU reservation.
     * `BLOCK_NAME`: the name of the block.
  3. Create a node pool for each sub-block identified in the preceding step. For example, if the count is `4`, run this command four times. Use a unique name for each node pool.
         
         gcloud container node-pools create NODE_POOL_NAME \
               --cluster=CLUSTER_NAME \
               --node-locations=ZONE \
               --machine-type=tpu7x-standard-4t \
               --num-nodes=16 \
               --placement-policy=WORKLOAD_POLICY_NAME \
               --reservation-affinity=specific \
               --reservation=${RESERVATION_PATH}
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your new node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.
     * `ZONE`: the zone for the node pool, for example, `us-central1-a`.



### Sub-block

  1. To retrieve the name of the block and the IDs of the available sub-blocks, complete the following steps in the [View the topology and health status of All Capacity Mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus) document:

     1. To identify the name of the block, [list all reservation blocks](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_reservation_blocks) and copy the value in the `name:` field. This value is the name of the block or `BLOCK_NAME` on this document.

     2. To identify the name of the sub-blocks, [list all sub-blocks of a block](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus#list_all_sub-blocks_of_a_block) and copy the value in the `name:` field for each entry under `reservationSubBlocks`. This value is the name of the sub-block or `SUBBLOCK_NAME` in this document.

  2. Set the reservation path:
         
         export RESERVATION_PATH="projects/PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUBBLOCK_NAME"
         

Replace the following:

     * `RESERVATION_NAME`: the name of your TPU reservation.
     * `BLOCK_NAME`: the name of the block.
     * `SUBBLOCK_NAME`: the name of the sub-block.
  3. Create the node pool:
         
         gcloud container node-pools create NODE_POOL_NAME \
                 --project=PROJECT_ID \
                 --cluster=CLUSTER_NAME \
                 --node-locations=ZONE \
                 --machine-type=tpu7x-standard-4t \
                 --num-nodes=16 \
                 --placement-policy=WORKLOAD_POLICY_NAME \
                 --reservation-affinity=specific \
                 --reservation=${RESERVATION_PATH}
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your new node pool, for example, `sub-block-pool-1`.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `ZONE`: the zone for the node pool, for example, `us-central2-b`.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.



At this stage, the nodes are created, but their Inter-Chip Interconnect (ICI) links are not yet active. Therefore, you can't run workloads on these node pools directly.

To enable all the necessary ICI links to form the slice and allow workloads to be scheduled, create a dynamic slice by using one of the following methods:

  * Create a [Slice custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice). Instead of Pods, you use a Slice custom resource to define the specified topology, which the slice controller activates.
  * Schedule GKE workloads with [Kueue](https://kueue.sigs.k8s.io/docs/overview/) and [TAS](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/). Kueue automatically handles the creation and deletion of Slice custom resources. Avoid manually modifying Slice custom resources created by Kueue.



## Form a dynamic slice with super-slicing or sub-slicing

After you create the node pools, you can form a larger dynamic super-slice or a smaller dynamic sub-slice by creating a Slice custom resource. A Slice custom resource defines the specified topology, which the slice controller activates. Your workloads then schedule and run on this dynamic slice.

### Dynamic slice partitions

Partitions provide the topologies that are available to form a dynamic slice for your workloads. A partition shows all available topologies for each node, including `2x2x1`, `2x2x2`, `2x2x4`, `2x4x4`, and `4x4x4`. Topologies smaller than `4x4x4` require GKE version 1.36.0-gke.3712000 or later. 

Any slice greater than `4x4x4` doesn't have a partition label, as it is created by associating multiple `4x4x4` partitions.

Every TPU node in an incremental provisioning node pool must possess every specified partition ID and partition state node label.

### Verify the status of the nodes and the partitions

  1. To get the node names from the node pool, run the following command:
         
         kubectl get nodes -l cloud.google.com/gke-nodepool=${NODE_POOL_NAME}
         

The outcome is similar to the following:
         
         NAME                                 STATUS   ROLES    AGE    VERSION
         gke-np-status-update-7b4c890c-0jhp   Ready    <none>   2d1h   v1.35.1-gke.1396002
         gke-np-status-update-7b4c890c-377r   Ready    <none>   2d1h   v1.35.1-gke.1396002
         gke-np-status-update-7b4c890c-gb51   Ready    <none>   2d1h   v1.35.1-gke.1396002
         

  2. Verify the node's provisioning model:
         
         kubectl describe node NODE_NAME | grep "cloud.google.com/gke-accelerator-topology-mode"
         

The outcome is similar to the following:
         
         cloud.google.com/gke-accelerator-topology-mode: PROVISION_ONLY
         

  3. Retrieve the node label information for the topology partition you want to target:
         
         kubectl describe node NODE_NAME | grep -E "cloud.google.com/gke-tpu-partition-.*-id"
         

Replace `NODE_NAME` with the name of one of the nodes in the node pool.

The outcome is similar to the following:
         
         cloud.google.com/gke-tpu-partition-4x4x4-id=fba785f80d18552357dcdef6d3d16c27
         cloud.google.com/gke-tpu-partition-2x4x4-id=e18372d627ac412cb24d5ea8ab8912c9
         cloud.google.com/gke-tpu-partition-2x2x4-id=7fbd4e29dc1839217fae41a9dd8211b4
         cloud.google.com/gke-tpu-partition-2x2x2-id=a9476d1b02bd4f4e75ffffae3bd23c01
         cloud.google.com/gke-tpu-partition-2x2x1-id=0bcfe937d1bb3914a8bdcd94e9f73319
         

  4. Verify that the node includes the `node.gke.io/created-by-mig` annotation:
         
         kubectl describe node NODE_NAME | grep "node.gke.io/created-by-mig"
         

Replace `NODE_NAME` with the name of one of the nodes in the node pool.

The outcome is similar to the following:
         
         node.gke.io/created-by-mig: projects/735972712744/zones/us-central1-ai1a/team/string
         

The output includes the `node.gke.io/created-by-mig` annotation, which allows the GKE control plane to link Kubernetes nodes to their underlying Compute Engine resources.

  5. Retrieve the node label information for the topology partition state you want to verify:
         
         kubectl describe node NODE_NAME | grep -E "cloud.google.com/gke-tpu-partition-.*-state"
         

The outcome is similar to the following:
         
         cloud.google.com/gke-tpu-partition-4x4x4-state=HEALTHY
         cloud.google.com/gke-tpu-partition-2x4x4-state=HEALTHY
         cloud.google.com/gke-tpu-partition-2x2x4-state=HEALTHY
         cloud.google.com/gke-tpu-partition-2x2x2-state=HEALTHY
         cloud.google.com/gke-tpu-partition-2x2x1-state=HEALTHY
         

The `cloud.google.com/gke-tpu-partition-[shape]-state` label (where `[shape]` corresponds to the topology of the partition ID) indicates if the partition is available to form a dynamic slice. This state label supports the following values:

     * `HEALTHY`: the partition is healthy and fully functional.
     * `DEGRADED`: the partition is impaired but still usable for dynamic slice formation. This state applies only to the top-level `4x4x4` topology. Smaller topologies don't have a degraded state.
     * `UNHEALTHY`: the partition is malfunctioning and can't be used to form a slice.
     * `UNSET`: state is undefined due to unsuccessful GKE slice controller initialization.
     * `INCOMPLETE`: not all nodes within the partition are provisioned.



### Create a Slice custom resource

The Slice custom resource varies slightly depending on whether you are creating a dynamic super-slice or a dynamic sub-slice.

  1. Define the Slice custom resource:
         
         apiVersion: accelerator.gke.io/v1beta1
         kind: Slice
         metadata:
           # Name of the slice resource
           name: SLICE_NAME
         spec:
           # Specify the type of accelerator for this slice
           type: "tpu7x"
           # Define the desired topology for the accelerator slice
           topology: TOPOLOGY
           partitionIds:
             - PARTITION_ID # Example: a9476d1b02bd4f4e75ffffae3bd23c01
             - PARTITION_ID_2
             # ... add more partition IDs as needed
         

Replace the following:

     * `SLICE_NAME`: a name for your slice. The name must meet the [`metadata.name`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice#slice-specification) conditions and must be 49 characters or less.
     * `TOPOLOGY`: the topology for the dynamic slice. The topology must meet the following conditions: 
       * **For dynamic sub-slicing:** you can specify topologies smaller than `4x4x4`, such as `2x2x1`, `2x2x2`, `2x2x4`, or `2x4x4`. These smaller topologies require GKE version 1.36.0-gke.3712000 or later.
       * **For dynamic super-slicing:** you can specify topologies that are equal to or greater than `4x4x4`. To configure dynamic super-slicing, each dimension of the requested topology must be a multiple of four, for example `4A x 4B x 4C`. The three values in the topology dimensions, `AxBxC`, must be in non-decreasing order (A ≤ B ≤ C). For example, `4x4x8` is valid, but `4x8x4` is not. This order helps ensure consistent slice formation and avoids unexpected behavior. The product of the three values in the topology dimensions, `A × B × C` must not exceed 9,216.
     * `PARTITION_ID`: a list of strings that identify the partitions that make up the slice. 
       * **For dynamic sub-slicing:** you must specify _exactly one_ partition ID.
       * **For dynamic super-slicing:** you must calculate the number of partitions based on the total number of chips, where each partition consists of 64 chips. The number of items in your `spec.partitionIds` list must exactly match the calculated number of partitions (`(A × B × C) / 64`).
       * The `partitionIds` list must meet the following conditions: 
         * Each partition must map to a reservation sub-block.
         * All associated sub-blocks must belong to the same reservation.
         * All associated sub-blocks must reside within the same reservation.
         * The associated node pools must have all nodes in `ready` state.
     * The value of the `type` field must be `tpu7x`.
     * Optionally, to enable the slice controller to automatically retry during slice formation, you can add the `slice.gke.io/retry-on-failure: "true"` annotation to the slice custom resource. If the slice isn't created because of the `SliceCreationFailed` status reason, the controller will retry until the slice is successfully formed.

For example, to create a `4x8x8` slice (dynamic super-slicing), you need to provide four unique partition IDs.
    
    apiVersion: accelerator.gke.io/v1beta1
    kind: Slice
    metadata:
        name: test-super-slice-example
        annotations:
          slice.gke.io/retry-on-failure: "true"
    spec:
        type: "tpu7x"
        topology: "4x8x8" # (4*8*8)/64 = 4 partitions
        partitionIds:
            - "p0-4x4x4"
            - "p1-4x4x4"
            - "p2-4x4x4"
            - "p3-4x4x4"
    

For example, to create a `2x2x2` slice (dynamic sub-slicing), you need to provide one unique partition ID.
    
    apiVersion: accelerator.gke.io/v1beta1
    kind: Slice
    metadata:
      name: test-sub-slice-example
      annotations:
          slice.gke.io/retry-on-failure: "true"
    spec:
      type: "tpu7x"
      topology: "2x2x2"
      partitionIds:
        - "fba785f80d18552357dcdef6d3d16c27" # Only 1 partitionId for sub-slice
    

  2. Apply the Slice custom resource:
         
         kubectl apply -f test-slice-example.yaml
         

At this point, GKE attempts to create the slice. If one of the following issues occurs, slice creation fails, and the status reason in the Slice custom resource is updated to `SliceCreationFailed` or `FAILED`:

     * If the selected nodes on the custom resource don't exist, the status reason is `SliceCreationFailed`.
     * If any nodes on the custom resource are used by another slice, the status reason is `SliceCreationFailed`.
     * If the nodes on the custom resource aren't part of the same reservation sub-block, the status reason is `FAILED`.
     * If the nodes aren't in the same reservation, the status reason is `FAILED`.
     * If the topology doesn't match the number of partitions, the status reason is `SliceCreationFailed`.

To automatically retry slice formation when the status is `SliceCreationFailed`, configure the `slice.gke.io/retry-on-failure: "true"` annotation as described in Create a Slice custom resource.

To learn more about the status of the Slice custom resource, see [Slice status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice#slice-status).




## Monitor the status of the Slice custom resource

To check the status of the Slice custom resource, run the following command:
    
    
    kubectl describe slice SLICE_NAME
    

Replace the `SLICE_NAME` with the name of the slice.

The output is similar to the following:
    
    
    Name:         test-slice
    Namespace:
    Labels:       <none>
    Annotations:  <none>
    API Version:  accelerator.gke.io/v1beta1
    Kind:         Slice
    Metadata:
      Creation Timestamp:  2026-01-11T23:45:15Z
      Finalizers:
        accelerator.gke.io/slice-finalizer
      Generation:        1
      Resource Version:  1768175347356335006
      UID:               d0b71e5c-be3f-4788-aead-930c7afec4f2
    Spec:
      Partition Ids:
        2c79463990ff67c4e3c2648666bfedfa
        ba898ffcac0ad0946e8ff036d771ee53
        [more partition IDs]
      Topology:  8x16x16
      Type:      tpu7x
    Status:
      Conditions:
        Last Transition Time:  2026-01-11T23:45:38Z
        Message:               ""
        **    Reason:                FAILED
        **
        Status:                False
        Type:                  Ready
    Events:
    

The `reason` field in the status of the Slice custom resource indicates the current lifecycle state. The possible states vary depending on whether you are using dynamic sub-slicing or dynamic super-slicing.

**Status conditions for dynamic sub-slicing**

  * **`SliceNotCreated`** : the controller performs initialization and resources checks. 
    * If prerequisites are not met, the state transitions to **`SliceCreationFailed`**.
    * If validation passes, the state transitions to **`ACTIVATING`**.
  * **`ACTIVATING`** : GKE is forming the slice. 
    * If successful, the state transitions to **`ACTIVE`**.
    * If sub-blocks are degraded but the slice is usable, the state transitions to **`ACTIVE_DEGRADED`**.
    * If formation fails, the state transitions to **`FAILED`**.
  * **`DEACTIVATING`** : if the Slice custom resource is deleted or a critical failure occurs in an active or failed state, the slice begins dismantling.
  * **`INCOMPLETE`** : the terminal step before the resource is fully deleted.



**Status conditions for dynamic super-slicing**

  * **`SliceNotCreated`** : the slice hasn't been created yet. The slice controller is initializing and performing preflight checks for slice formation.
  * **`SliceCreationFailed`** : creation failed because prerequisites were not met (for example, required Compute Engine resources are missing) or preflight checks failed. To automatically retry slice formation in this state, configure the `slice.gke.io/retry-on-failure: "true"` annotation.
  * **`ACTIVATING`** : the slice is in the process of being formed (stitched).
  * **`ACTIVE`** : the slice is fully formed, healthy, and ready to execute workloads.
  * **`ACTIVE_DEGRADED`** : the slice is formed but includes degraded cubes, supported by ICI resilience. Workloads can run, but performance might be impacted. Dynamic super-slicing is resilient to single optical circuit switch (OCS) failures. If a single OCS unit fails, all optical links traversing that switch become unavailable, which causes all cubes within the superpod to operate in a degraded state.
  * **`DEACTIVATING`** : the slice is in the process of being dismantled.
  * **`FAILED`** : the slice is no longer ready to execute workloads. This state occurs if initial formation failed or if an active slice experienced a critical software or hardware failure.
  * **`INCOMPLETE`** : there are not enough available cubes to initiate super-slice formation.



To learn more about the status of the Slice custom resource, see [Slice status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice#slice-status).

## Run workloads on dynamic slicing

When the Slice custom resource is in an `ACTIVE` state, you can run workloads on it. The following section includes examples of workloads that use dynamic slicing. The workloads are submitted as Jobs or JobSets.

### Example 1: single workload uses a single slice

The following example shows a workload that uses a single `4x4x4` dynamic super-slice.

  1. Save the following sample manifest as `tpu-job-jax-v7x-64.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-job-jax-v7x-64
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-job-jax-v7x-64
         spec:
           backoffLimit: 0
           completions: 16
           parallelism: 16
           completionMode: Indexed
           template:
             metadata:
               annotations:
                 cloud.google.com/gke-tpu-slice-topology: 4x4x4
             spec:
               nodeSelector:
                 cloud.google.com/gke-tpu-topology: 4x4x4
                 cloud.google.com/gke-tpu-accelerator: tpu7x
                 cloud.google.com/gke-tpu-slice: test-slice
               subdomain: headless-svc
               restartPolicy: Never
               containers:
               - name: tpu-job-jax
                 env:
                 - name: TPU_ACCELERATOR_TYPE
                   value: tpu7x-128
                 image: python:3.12
                 securityContext:
                   privileged: false
                 command:
                 - bash
                 - -c
                 - |
                   set -ex
                   pip install -U --pre jax jaxlib libtpu requests -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/ -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                   pip list
                   python -c 'import jax; print("Total TPU devices (cores):", jax.device_count())'
                 resources:
                   requests:
                     google.com/tpu: 4
                   limits:
                     google.com/tpu: 4
         

In this manifest:

     * `cloud.google.com/gke-tpu-slice-topology` and `cloud.google.com/gke-tpu-topology` define the topology of the dynamic slice.
     * `env.value: tpu7x-128` is the TPU accelerator type and the total number of cores in the slice. The number of cores is calculated by multiplying the dimensions of the topology by the number of cores per chip. For example, for a `4x4x4` topology, the calculation is `4 × 4 × 4 × 2 = 128`, where `2` is the number of cores per chip for `tpu7x` (Ironwood (TPU7x)). Therefore, the `TPU_ACCELERATOR_TYPE` is `tpu7x-128`.
  2. Apply the `tpu-job-jax-v7x-64.yaml` manifest:
         
         kubectl apply -f tpu-job-jax-v7x-64.yaml
         




### Example 2: deploy a workload on multislice node pools by using JobSet

This example demonstrates how to deploy a workload on multislice node pools by using JobSet.

  1. Install JobSet:
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/JOBSET_VERSION/manifests.yaml
         

Replace `JOBSET_VERSION` with the required version of JobSet. For dynamic sub-slicing, use JobSet v0.12.0 or later. For dynamic super-slicing, use JobSet v0.11.1 or later.

  2. Save the following sample manifest as `tpu-multislice-jax.yaml`:
         
         # Copyright 2026 Google LLC
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #      http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: tpu-multislice-jax
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-tpu-slice
         spec:
           failurePolicy:
             maxRestarts: 3
           replicatedJobs:
           - name: slice-job
             replicas: 2
             template:
               spec:
                 parallelism: 16
                 completions: 16
                 backoffLimit: 0
                 completionMode: Indexed
                 template:
                   metadata:
                     annotations:
                       # The shape of the slice
                       cloud.google.com/gke-tpu-slice-topology: 4x4x4
                   spec:
                     hostNetwork: true
                     dnsPolicy: ClusterFirstWithHostNet
                     nodeSelector:
                       cloud.google.com/gke-tpu-topology: 4x4x4
                       cloud.google.com/gke-tpu-accelerator: tpu7x
                       # IMPORTANT: Do NOT put 'cloud.google.com/gke-tpu-slice' here manually.
                       # The exclusive-topology annotation handles the slice assignment automatically.
                     containers:
                     - name: jax-worker
                       image: python:3.12
                       securityContext:
                         privileged: true
                       ports:
                       - containerPort: 8471
                       command:
                       - bash
                       - -c
                       - |
                         set -ex
                         pip install -U --pre jax jaxlib libtpu requests -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                         # Verify JobSet injected the specific slice ID for this worker
                         echo "JobSet Index: $JOB_COMPLETION_INDEX"
                         python -c 'import jax; print("Total TPU devices:", jax.device_count())'
                       resources:
                         requests:
                           google.com/tpu: 4
                         limits:
                           google.com/tpu: 4
         

  3. Apply the `tpu-multislice-jax.yaml` manifest:
         
         kubectl apply -f tpu-multislice-jax.yaml
         

In this manifest:

     * The `replicas: 2` field under `replicatedJobs` indicates that JobSet creates two separate Jobs, each corresponding to a `4x4x4` TPU slice.
     * The `alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-tpu-slice` annotation helps ensure that each Job is assigned to a unique TPU slice.
     * The `cloud.google.com/gke-tpu-slice-topology: 4x4x4` annotation defines the topology of each dynamic slice.
     * The `TPU_ACCELERATOR_TYPE` environment variable is not explicitly set in this example, as JobSet handles the slice assignment. The JAX code automatically detects the available TPU devices within its assigned slice.
**Important:** Don't edit the `cloud.google.com/gke-tpu-slice` label manually.



## Delete the slice

  1. Delete the slice:
         
         kubectl patch slice $SLICE_NAME --type json \
           -p='[{"op": "remove", "path": "/metadata/finalizers"}]'
         

  2. Verify that the slice is deleted:
         
         kubectl get slices
         




## Upgrade your node pools

If you upgrade node pools that are configured with incremental provisioning, you must use specific surge parameters to prevent capacity conflicts.

To configure and run the node pool upgrade:

  1. If you are using dynamic super-slicing, delete your active slices before executing manual maintenance:
         
         kubectl delete slice SLICE_NAME
         

If you are using dynamic sub-slicing, you don't need to delete the active slices first. However, sub-slices that remain active during an upgrade will fail and transition to a `FAILED` state.

  2. Update the upgrade parameters for your node pool:
         
         gcloud container node-pools update NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=LOCATION \
             --max-surge-upgrade=0 \
             --max-unavailable-upgrade=16
         

Ensure that the `--max-surge-upgrade` field is set to a value of `0` to prevent GKE from trying to allocate extra TPUs during the upgrade. We recommend that you set the `--max-unavailable-upgrade=16` field to upgrade a full 16-node sub-block concurrently.

  3. Upgrade the node pool:
         
         gcloud container clusters upgrade CLUSTER_NAME \
             --node-pool=NODE_POOL_NAME \
             --cluster-version=CLUSTER_VERSION \
             --project=PROJECT_ID \
             --location=LOCATION
         




## Hardware maintenance and failures

If you trigger customer-initiated maintenance or if a hardware failover occurs, only the targeted nodes are affected rather than the entire node pool.

For dynamic super-slicing, you must delete your active dynamic slices before executing manual maintenance. If you are using dynamic sub-slicing, you don't need to delete the active slices first. If maintenance or hardware failures occur while a dynamic sub-slice is active, the system handles recovery as follows:

  1. **Automated reshaping** : GKE automatically reshapes the active dynamic slice when maintenance starts on an associated host.
  2. **Slice custom resource failure** : the Slice custom resource transitions to a `FAILED` state.
  3. **Scheduler observation** : the scheduler observes the failed state of the Slice custom resource.
  4. **Reformation process** : the scheduler automatically attempts to re-create the slice configurations on other available healthy nodes.



## Disable the Slice Controller

To disable the slice controller, remove it from the cluster.

  1. Check that the Slice custom resources empty:
         
         kubectl get slice -A
         

  2. Update the cluster to disable the slice controller:
         
         gcloud container clusters update ${CLUSTER_NAME} \
             --location=${REGION} \
             --no-enable-slice-controller
         

  3. Delete the Slice custom resource :
         
         kubectl delete crd slices.accelerator.gke.io
         

  4. Verify that the Slice custom resource is deleted:
         
         kubectl get crd | grep slices.accelerator.gke.io
         

  5. Remove the labels added by slice controller. Need to remove these labels:

     * `cloud.google.com/gke-tpu-slice`
     * `cloud.google.com/gke-tpu-topology`
     1. To remove from a specific node, update the node name
    
    export NODE_NAME="gke-tpu-bdac9600-3bdg"
    kubectl label node $NODE_NAME cloud.google.com/gke-tpu-slice- cloud.google.com/gke-tpu-slice-topology-
    

     1. If you want to remove these labels from every node in your cluster:
    
    kubectl label nodes --all cloud.google.com/gke-tpu-slice- cloud.google.com/gke-tpu-slice-topology-
    

     1. Check the node labels and confirm they are empty:
    
    export NODE_NAME="gke-tpu-bdac9600-3bdg"
    kubectl describe node $NODE_NAME | grep "cloud.google.com/gke-tpu-slice"
    




## What's next

  * Learn more about [dynamic slicing concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing).
  * Learn about the [Slice custom resource](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/slice).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
