---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-all-capacity-mode/
title: Deploy TPUs in All Capacity mode in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:48.511824+00:00
---

# Deploy TPUs in All Capacity mode in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-all-capacity-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy TPUs in All Capacity mode in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to deploy and manage workloads using the _TPU All Capacity mode_ feature in GKE. All Capacity mode reservations provide enhanced control over your TPU resources, which lets you place your workloads with fine-grained control within your reserved capacity.

This document is intended for Machine learning (ML) engineers and Platform admins and operators who want to use Kubernetes container orchestration with granular control over TPU deployments.

Before reading this document, ensure that you're familiar with the following:

  * [TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
  * [TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions)
  * [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)



## What's TPU All Capacity mode?

TPU All Capacity mode, enabled by [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview), gives you complete control over your reserved TPU capacity. TPU Cluster Director is a management service that gives you reservation-based control over your TPUs.

Unlike the previous _managed_ mode, where Google Cloud reserves a portion of your capacity to handle hardware failures, All Capacity mode grants you access to the entirety of your reserved TPU resources. This mode comes with full visibility into the hardware's status, but also shifts the responsibility of managing node failures and planned maintenance to you.

For more information about the key features of All Capacity Mode, see [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview#all_capacity_mode) in the TPU Cluster Director overview.

## Terminology related to All Capacity mode in GKE

The following table includes the terms and equivalences defined by the size of a block, sub-block, and cube in the Ironwood (TPU7x) version. A cube is a `4x4x4` topology of interconnected TPU chips, which is only applicable to topologies in 3-tuples ({A}x{B}x{C}).

TPU resource | Cores | Chips | Hosts | Cubes  
---|---|---|---|---  
1 chip | 2 | 1 | - | -  
1 host | 8 | 4 | 1 | -  
1 sub-block | 128 | 64 | 16 | 1  
A block contains 144 sub-blocks | 18432 | 9216 | 2304 | 144  
  
For more information about the allowed topologies in a block, see [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster in version 1.34.0-gke.2201000 or later. To create a new cluster, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * Ensure you have sufficient quota for TPUs in the region you want to use.
  * [Install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.2.3 or later.



## Limitations

TPU All Capacity mode in GKE supports only Ironwood (TPU7x) versions.

## Use TPU All Capacity mode in GKE

This section describes the workflow to use TPU All Capacity mode in GKE.

  1. Familiarize yourself with [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).
  2. [Request TPU capacity in All Capacity mode](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation#confirm_your_capacity_reservation_draft).
  3. [View the topology and health status of All Capacity mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus).
  4. Complete the step in this document: 
     1. Create GKE node pool
     2. Schedule workloads
     3. Manage node failures with an All Capacity mode reservation
  5. [Manage maintenance events with TPUs in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events).
  6. [Report and repair faulty hosts with TPUs in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts).



## Create a node pool within an All Capacity mode reservation

All Capacity mode on GKE lets you create node pools in the following ways:

  * A node pool where GKE selects the block or sub-block in your TPU All Capacity reservation.
  * A node pool with that targets a particular block or sub-block within a TPU All Capacity mode reservation.



### GKE selects the block or sub-block in your TPU All Capacity reservation

In this mode, GKE selects the placement of the node pool within your TPU All Capacity reservation. This process is similar to creating node pools with other TPU provisioning options, such as on-demand or Spot VMs.

To create a node pool, use the `gcloud container node-pools create` command with the `--reservation` flag. Specify the full resource name of your TPU reservation as the value for the `--reservation` flag.

For an example of a node pool creation command, see [Manually create a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#create-node-pool).

### Target a block or sub-block within a reservation

TPU All Capacity mode lets you target a specific block or sub-block within your TPU reservation for parallel workloads. This capability is useful for workloads that require close proximity between TPU chips to minimize latency.

  1. See the available block, sub-block, and host configurations. Complete the steps in the [View the topology and health status of All Capacity mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus) document.

  2. Create a workload policy:

**Note:** You don't need to create a new workload policy for every node pool. A workload policy is unique per project, per region, and per topology. If you already have a workload policy that matches your requirements, you can skip this step and reuse the existing policy in the next step. To see the list of workload policies, use the `gcloud compute resource-policies list --filter="region:REGION"` command.
         
         gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=TPU_TOPOLOGY \
             --project=PROJECT_ID \
             --region=REGION
         

Replace the following:

     * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
     * `TPU_TOPOLOGY`: the TPU Ironwood (TPU7x) topology. For example, `2x2x2`. To see all supported Ironwood (TPU7x) topologies, see the [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region for the workload policy. A workload policy is a regional resource and can be reused across node pools that share the same topology.
  3. To create a node pool and target a particular block or sub-block of the reservation, use the `--reservation` flag to specify the full resource name of the target block or sub-block within your reservation.

To target a specific **block** within your reservation, use the following command:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --machine-type=tpu7x-standard-4t \
             --placement-policy=WORKLOAD_POLICY_NAME \
             --zone=ZONE \
             --reservation=project/PROJECT/reservation/RESERVATION_NAME/reservationBlocks/BLOCK_NAME
         

To target a specific **sub-block** within a block, use the following command:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --machine-type=tpu7x-standard-4t \
             --placement-policy=WORKLOAD_POLICY_NAME \
             --zone=ZONE \
             --reservation=project/PROJECT/reservation/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUB_BLOCK_NAME
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your new node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.
     * `ZONE`: the zone for the node pool, for example, `us-central1-a`.
     * `PROJECT`: your Google Cloud project ID.
     * `RESERVATION_NAME`: the name of your TPU reservation.
     * `BLOCK_NAME`: the specific block within your reservation.
     * `SUB_BLOCK_NAME`: the specific sub-block within your reservation.

In the preceding commands, you




## Schedule workloads

After you create a node pool with TPU VMs in All Capacity mode, you can deploy your workload like any other TPU node pool. For TPU All Capacity mode, there are no additional differences in scheduling workloads compared to node pools that use standard SLO-backed reservations.

For more information and examples of workloads that use TPUs, see [Run your workload on TPU slice nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#run) and [Run a Multislice workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#run_workload).

## Manage node failures

TPU All Capacity mode reservations are _no-holdback_ reservations. _No-holdback_ means that you receive the full TPU capacity, which includes the portion that Google Cloud typically retains for failovers in the managed capacity mode.

In TPU All Capacity mode, if a VM fails due to issues like hardware failure, Google Cloud attempts to recover the VM on the same host (in-place repair). Therefore, we recommend that you maintain spare capacity to accommodate workload rescheduling during infrastructure failures.

### Node failure and recovery

When a node fails in a TPU All Capacity mode reservation, the following events occur:

  * Google Cloud initiates a repair event for the failed Compute Engine VM instance. This process attempts to restore the VM to a `RUNNING` status and return the GKE node status to `READY`.
  * The TPU VM enters a repairing status and any workload running on that node might fail, depending on its failover policy. The node pool's status doesn't change to `ERROR` even if one or more of its VMs are experiencing failures.



To monitor the health status of your nodes, follow these steps:

  1. List the nodes in the node pool:
         
         kubectl get nodes
         

Failed nodes have a status of `NotReady`.

  2. Monitor the status of the Compute Engine node:

For TPU VMs in All Capacity mode, use `gcloud compute instances describe`. This command also provides the physical status of the topology to find host, sub-block, and block details.
         
         gcloud compute instances describe VM_NAME \
                 --format="table[box,title=VM-Position](resourceStatus.physical_host_topology:label=location)" \
                 --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the TPU VM instance.
     * `ZONE`: the zone of the VM, for example, `us-central1-a`.

For more steps on how to retrieve topology and health information about your All Capacity mode capacity, see [View the topology and health status of All Capacity Mode reservations](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus).




### Manage maintenance

To handle potential disruptions and help ensure that your workloads remain resilient, you can manage maintenance for individual nodes using GKE maintenance policies. For more information, see [Maintenance windows and maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

GKE doesn't support group maintenance for TPU VMs in an All Capacity mode reservation. To perform group maintenance at the sub-block, block, or reservation level, use Compute Engine APIs. For more information, see [Manage maintenance events with TPUs in All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events).

## Clean up

To avoid incurring unwanted charges to your Google Cloud account, delete the TPU node pools that no longer have scheduled workloads. If the running workloads must be gracefully terminated, use the `kubectl drain` command to clean up the workloads before you delete the node pool.

  1. Delete a TPU node pool:
         
         gcloud container node-pools delete NODE_POOL_NAME \
             --location=LOCATION \
             --cluster=CLUSTER_NAME
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the node pool.
     * `CLUSTER_NAME`: the name of the cluster.
     * `LOCATION`: the compute location of the cluster.



## What's next

  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).
  * Learn more about [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
