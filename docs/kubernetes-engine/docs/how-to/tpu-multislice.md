---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice/
title: Deploy TPU Multislices in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:36.809517+00:00
---

# Deploy TPU Multislices in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy TPU Multislices in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to deploy workloads in Google Kubernetes Engine (GKE) by using the Cloud TPU Multislice configuration for cost-effective, large-scale training.

This tutorial is for Machine learning (ML) engineers and Platform admins and operators who want to use Kubernetes container orchestration to manage large-scale model training, tuning, and inference workloads by using TPUs. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before you configure Multislice in GKE, ensure that you're familiar with the following concepts:

  1. [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
  2. [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#slices)
  3. [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)

**Key Term:** This page introduces the following terms: 

  * **Data Center Networking (DCN)** : A higher capacity, low latency, and lower-throughput network that connects Cloud TPU slices in a Multislice configuration.
  * **TPU slice node** : A Kubernetes node that contains a set of VMs with interconnected TPU chips. Each VM in a TPU slice may contain one, four, or eight TPU chips. To learn more, see [System Architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_slices).
  * **Multislice workload** : A workload requiring multiple TPU slices.
  * **TPU Topology** : It defines the number and physical arrangement of TPU chips within a TPU slice. To learn more, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology).



## What's TPU Multislice

TPU _Multislice_ is the architectural organization of VMs in a TPU slice where two or more Cloud TPU slices communicate over the Data Center Network (DCN). Multislice enables full-stack, cost effective, large scale training with near-linear scaling up to tens of thousands of TPU chips. In a Multislice configuration, GKE deploys a Multislice workload on multiple TPU slices. The communication between TPU chips within a slice happens over inter chip interconnects (ICI). The communication between slices happens over the DCN.

We recommend that you use the Multislice if your Job is too big to fit on a single TPU slice.

## Multislice availability in GKE

  * Standard supports Multislice in version 1.27.4-gke.900 and later.
  * Autopilot supports Multislice in version 1.29.2-gke.1521000 and later.
  * Multislice supports JAX and PyTorch frameworks. The minimum supported JAX version is 2.1.
  * Multislice only supports [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host). For example, you cannot use Multislice with a `ct4p-hightpu-4t` with a `2x2x1` topology or a `ct5lp-hightpu-4t` with a `2x2` topology, because these are single-host TPU slice node pools.
  * Multislice only supports synchronous multicontroller training.
  * Multislice workloads can only run across TPU slices that share the same TPU type, size, and topology.
  * Multislice don't support TPU v3.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Create a [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) cluster or an [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) cluster that runs a version that supports Multislice. For supported versions, see Multislice availability in GKE.
  * [Ensure your project has sufficient quota](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota) for Cloud TPU in GKE.
  * [Install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.2.3 or later.



## Choose a GKE implementation method

You can choose to prepare your GKE TPU node pools manually or deploy them automatically using Cluster Toolkit blueprints.

### Manually create your GKE node pool

This section shows you how prepare a Standard mode node pool to run a workload on a Multislice. If you use GKE Autopilot mode, skip to the Run a Multislice workload section. Autopilot clusters that run version 1.29.2-gke.1521000 or later enable TPUs by default.

This section covers the following steps:

  1. Create _three_ multi-host TPU slice node pools
  2. Verify the node pool status
  3. Run a Multislice workload



#### Create the TPU slice node pool

You can create more than one multi-host TPU slice node pool. For the purpose of this guide, create _three_ multi-host TPU slice node pools to run a Multislice workload. The steps to create a multi-host TPU slice node pool differ depending on whether you use Ironwood (TPU7x) or an earlier TPU version.

###  Ironwood (TPU7x) 

You can create a [multi-host TPU slice](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) node pool in version Ironwood (TPU7x) by using the Google Cloud CLI or Terraform:

### gcloud

To create a multi-host TPU slice node pool with Ironwood (TPU7x), you must first create a workload policy.

**Note:** You don't need to create a new workload policy for every node pool. A workload policy is unique per project, per region, and per topology. You can reuse the same workload policy for multiple node pools that share these characteristics. To see the list of workload policies, use the `gcloud compute resource-policies list --filter="region:REGION"` command.

  1. Create a workload policy:
         
         gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=TPU_TOPOLOGY \
             --project=PROJECT_ID \
             --region=REGION
         

Replace the following:

     * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
     * `TPU_TOPOLOGY`: the TPU Ironwood (TPU7x) topology. For example, `2x2x2`. To see all supported Ironwood (TPU7x) topologies, see the [topology section](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region for the workload policy. A workload policy is a regional resource and can be re-used across node pools that share the same topology.
  2. Create the node pool with the workload policy:
         
         gcloud container node-pools create NODE_POOL_NAME \
           --cluster=CLUSTER_NAME \
           --machine-type=tpu7x-standard-4t \
           --placement-policy=WORKLOAD_POLICY_NAME \
           --location=CONTROL_PLANE_LOCATION \
           --node-locations=NODE_ZONE \
           --project=PROJECT_ID \
           --reservation=RESERVATION_NAME \
           --reservation-affinity=specific
         

Replace the following:

     * `NODE_POOL_NAME`: the name for your new node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `WORKLOAD_POLICY_NAME`: the name of the workload policy you created.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `NODE_ZONE`: the name of the zone based on the TPU version you want to use. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `RESERVATION_NAME`: the name of the reservation to use.

In this command, the `--tpu-topology` flag has been replaced by the `--placement-policy` flag. 




### Terraform

  1. Ensure that you use the version 4.84.0 or later of the [`google`](https://registry.terraform.io/providers/hashicorp/google/latest) provider.
  2. Create a workload policy:
         
         resource "google_compute_resource_policy" {
           name   = "WORKLOAD_POLICY_NAME"
           region = CLUSTER_LOCATION
           workload_policy {
             type = "HIGH_THROUGHPUT"
             accelerator_topology = "TPU_TOPOLOGY"
           }
         }
         

Replace the following:

     * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
     * `CLUSTER_LOCATION`: Compute location for the cluster. We recommend having a regional cluster for higher reliability of the Kubernetes control plane. You can also use a zonal cluster. For more information, see [Select a TPU version and topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
     * `TPU_TOPOLOGY`: the TPU Ironwood (TPU7x) topology. For example, `2x2x2`. To see all supported Ironwood (TPU7x) topologies, see [Plan TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

For more information about the `google_compute_resource_policy` reference, see [Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_resource_policy#argument-reference).

  3. In your Terraform configuration, add the following block:
         
         resource "google_container_node_pool" "NODE_POOL_RESOURCE_NAME" {
           provider           = google
           project            = PROJECT_ID
           cluster            = CLUSTER_NAME
           name               = POOL_NAME
           location           = CLUSTER_LOCATION
           node_locations     = [NODE_ZONES]
           initial_node_count = NUM_NODES
         
           autoscaling {
             max_node_count = MAX_NODES
             location_policy      = "ANY"
           }
           node_config {
             machine_type = MACHINE_TYPE
             reservation_affinity {
               consume_reservation_type = "SPECIFIC_RESERVATION"
               key = "compute.googleapis.com/reservation-name"
               values = [RESERVATION_LABEL_VALUES]
             }
             flex_start = false
             spot = true
           }
         
           placement_policy {
             policy_name = WORKLOAD_POLICY_NAME
           }
         }
         

Replace the following:

     * `NODE_POOL_RESOURCE_NAME`: the name of the node pool resource in the Terraform template.
     * `PROJECT_ID`: your project ID.
     * `CLUSTER_NAME`: the name of the existing cluster to add the node pool to.
     * `POOL_NAME`: the name of the node pool to create.
     * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

     * `NUM_NODES`: the number of nodes in the node pool. It must be zero or the product of the number of the TPU chips divided by four, because in multi-host TPU slices each TPU slice node has four chips. For example, if `TPU_TOPOLOGY` is `4x8`, then there are 32 chips, which means `NUM_NODES` must be 8. To learn more about TPU topologies, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
     * `TPU_TOPOLOGY`: this indicates the selected physical topology for the TPU slice. The format of the topology depends on the TPU version you are using. To learn more about TPU topologies, use the table in [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

Optionally, you can also use the following variables:

     * `RESERVATION_NAME`: if you use a [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-reservation-availability), provide a list of reservation-resource labels to use when creating the node pool. To learn more about how to populate the`RESERVATION_LABEL_VALUES` in the `reservation_affinity` field, see [Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#reservation_affinity).
     * `autoscaling`: create a node pool with autoscaling enabled. When GKE scales a multi-host TPU slice node pool, it [atomically](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology) scales up the node pool from zero to the maximum size. 
       * `MAX_NODES`: the maximum size of the node pool. The value must be equal to the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM. For example, if `TPU_TOPOLOGY` is `2x2x2`, the product is 8. Since each VM in `tpu7x-standard-4t` has 4 chips, the number of nodes is 2.
     * `spot`: the node pool that will use Spot VMs for the TPU slice nodes. This setting cannot be changed after the node pool is created. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
     * `flex_start`: the node pool that will use [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. This setting can't be set to `true` if `spot` is enabled.



### Other TPU versions

You can create a [multi-host TPU slice](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host) node pool in version v3, v4, v5p, v5e, and Trillium (v6e) by using the Google Cloud CLI, Terraform, or the Google Cloud console.

### gcloud
    
    
      gcloud container node-pools create POOL_NAME \
          --location=CONTROL_PLANE_LOCATION \
          --cluster=CLUSTER_NAME \
          --node-locations=NODE_ZONE \
          --machine-type=MACHINE_TYPE \
          --tpu-topology=TPU_TOPOLOGY \
          [--num-nodes=NUM_NODES] \
          [--spot \]
          [--flex-start \]
          [--enable-autoscaling \
            --max-nodes MAX_NODES]
          [--reservation-affinity=specific \
          --reservation=RESERVATION_NAME] \
          [--node-labels cloud.google.com/gke-nodepool-group-name=COLLECTION_NAME,cloud.google.com/gke-workload-type=HIGH_AVAILABILITY]
          [--placement-type=COMPACT]
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CONTROL_PLANE_LOCATION`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `CLUSTER_NAME`: the name of the cluster.
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool.

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  * `MACHINE_TYPE`: the type of machine to use for nodes. To learn more about the available machine types, see [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `TPU_TOPOLOGY`: the physical topology for the TPU slice. The format of the topology depends on the TPU version. To learn more about TPU topologies, use the table in [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

For more information, see [Topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology).

Optionally, you can also use the following flags:

  * `NUM_NODES`: the number of nodes in the node pool. It must be zero or the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM. For multi-host TPU v4 and TPU v5e, the number of chips in each VM is four. Therefore, if your `TPU_TOPOLOGY` is `2x4x4` (TPU v4 with four chips in each VM), then the `NUM_NODES` is 32/4 which equals to 8. If you omit this flag, the number of nodes is calculated and defaulted based on the topology and machine type.

  * `RESERVATION_NAME`: the name of the reservation GKE uses when creating the node pool. If you omit this flag, GKE uses available TPU slice node pools. For more information about TPU reservations, see [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-reservation-availability).

  * `--spot`: sets the node pool to use Spot VMs for the TPU slice nodes. This cannot be changed after node pool creation. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).

  * `--flex-start`: sets the node pool to use Flex-start VMs. Flex-start VMs are created by using the [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option, which is supported in GKE version 1.33.0-gke.1712000 or later.

  * `--enable-autoscaling`: Create a node pool with autoscaling enabled. When GKE scales a multi-host TPU slice node pool, it [atomically](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology) scales up the node pool from zero to the maximum size.

    * `MAX_NODES`: the maximum size of the node pool. The `--max-nodes` flag is required if `--enable-autoscaling` is supplied and must be equal to the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM.
  * `--node-label=cloud.google.com/gke-nodepool-group-name=COLLECTION_NAME, cloud.google.com/gke-workload-type=HIGH_AVAILABILITY`: Tells GKE that the multi-host TPU slice node pool is a collection. Use this flag if the following conditions apply:

    * The node pool runs inference workloads.
    * The node pool uses TPU Trillium.
    * Spot VMs don't support collection scheduling.

For more information about collection scheduling management, see [Manage collection scheduling in multi-host TPU slices](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#manage-collection).

  * `--placement-type=COMPACT`: Create a node pool with compact placement enabled. This option must be used with the flag `--tpu-topology`. For more information, see [Create a compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement#create_a_compact_placement_policy) and [TPU Topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology). 




### Terraform

  1. Ensure that you use the version 4.84.0 or later of the [`google`](https://registry.terraform.io/providers/hashicorp/google/latest) provider.
  2. Add the following block to your Terraform configuration:
         
         resource "google_container_node_pool" "NODE_POOL_RESOURCE_NAME" {
           provider           = google
           project            = PROJECT_ID
           cluster            = CLUSTER_NAME
           name               = POOL_NAME
           location           = CLUSTER_LOCATION
           node_locations     = [NODE_ZONES]
           initial_node_count = NUM_NODES
         
           autoscaling {
             max_node_count = MAX_NODES
             location_policy      = "ANY"
           }
           node_config {
             machine_type = MACHINE_TYPE
             reservation_affinity {
               consume_reservation_type = "SPECIFIC_RESERVATION"
               key = "compute.googleapis.com/reservation-name"
               values = [RESERVATION_LABEL_VALUES]
             }
             flex_start = false
             spot = true
           }
         
           placement_policy {
             type = "COMPACT"
             tpu_topology = TPU_TOPOLOGY
           }
         }
         

Replace the following:

     * `NODE_POOL_RESOURCE_NAME`: the name of the node pool resource in the Terraform template.
     * `PROJECT_ID`: your project ID.
     * `CLUSTER_NAME`: the name of the existing cluster to add the node pool to.
     * `POOL_NAME`: the name of the node pool to create.
     * `CLUSTER_LOCATION`: compute location for the cluster. We recommend having a regional cluster for higher reliability of the Kubernetes control plane. You can also use a zonal cluster. To learn more, see [Select a TPU version and topology](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#version_and_topology).
     * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool.

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

     * `NUM_NODES`: the number of nodes in the node pool. It must be zero or the product of the number of the TPU chips divided by four, because in multi-host TPU slices each TPU slice node has 4 chips. For example, if `TPU_TOPOLOGY` is `4x8`, then there are 32 chips which means `NUM_NODES` must be 8. To learn more about TPU topologies, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
     * `TPU_TOPOLOGY`: this indicates the physical topology for the TPU slice. The format of the topology depends on the TPU version you are using. To learn more about TPU topologies, use the table in [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

Optionally, you can also use the following variables:

     * `RESERVATION_NAME`: if you use [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-reservation-availability), this is the list of labels of the reservation resources to use when creating the node pool. To learn more about how to populate the`RESERVATION_LABEL_VALUES` in the `reservation_affinity` field, see [Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#reservation_affinity).
     * `autoscaling`: Create a node pool with autoscaling enabled. When GKE scales a multi-host TPU slice node pool, it [atomically](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology) scales up the node pool from zero to the maximum size. 
       * `MAX_NODES`: it is the maximum size of the node pool. It must be equal to the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM).
     * `spot`: lets the node pool to use Spot VMs for the TPU slice nodes. This cannot be changed after node pool creation. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
     * `flex_start`: Sets the node pool to use [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. Can't be set to `true` if `spot` is enabled.



### Console

To create a node pool with TPUs:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. In the **Node pool details** section, check the **Specify node locations** box.

  6. Select the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#availability).

  7. From the navigation pane, click **Nodes**.

  8. In the **Machine Configuration** section, select **TPUs**.

  9. In the **Series** drop-down menu, select one of the following:

     * **CT3** : TPU v3, single-host device
     * **CT3P** : TPU v3, multi-host pod slice
     * **CT4P** : TPU v4
     * **CT5LP** : TPU v5e
     * **CT5P** : TPU v5p
     * **CT6E** : TPU Trillium (v6e)
  10. In the **Machine type** drop-down menu, select the name of the machine to use for nodes. Use the [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version) table to learn how to define the machine type and TPU topology that create a _multi-host_ TPU slice node pool.

  11. In the **TPU Topology** drop-down menu, select the physical topology for the TPU slice.

  12. In the **Changes needed** dialog, click **Make changes**.

  13. Ensure that **Boot disk type** is either **Standard persistent disk** or **SSD persistent disk**.

  14. Optionally, select the **Enable nodes on spot VMs** checkbox to use Spot VMs for the nodes in the node pool.

  15. Click **Create**.




**Important:** Repeat the preceding steps _twice_ to create two additional TPU slice node pools in the cluster. Change the name of the node pool in every iteration.

#### Verify the node pool status

  1. Get credentials, so that you can use `kubectl` to access the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `PROJECT_ID`: your project ID.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  2. Use `kubectl`, in Cloud Shell, to see your TPU slice nodes:
         
         kubectl get nodes -l cloud.google.com/gke-tpu-accelerator=ACCELERATOR_TYPE \
            -l cloud.google.com/gke-tpu-topology=TPU_TOPOLOGY
         

Replace the following:

     * `ACCELERATOR_TYPE`: the accelerator type of the TPU slice node pool. This value must map to the machine type you used during node pool creation. For example, if you created a node pool with the `ct5lp-hightpu-4t` machine type, use `tpu-v5-lite-podslice`. To learn which accelerator type to use, see the table in [Plan your TPU on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).
     * `TPU_TOPOLOGY`: the [physical topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) for the TPU slice.

The output is similar to the following:
    
    NAME                                    STATUS   ROLES    AGE    VERSION
     gke-tpu-20ee2cce-5tv6                   Ready    <none>   34h     v1.28.1-gke.1066000
    




#### Run a Multislice workload

In this section you run a JAX workload which shows the global number of TPU chips in the TPU slice and then exits.

To run a JAX workload do the following:

  1. Create the following `tpu-multislice.yaml` manifest:

### Autopilot
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-job
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 2 # This value defines a "Multislice" setup, by creating 2 independent TPU slices.
               template:
                 spec:
                   parallelism: 4
                   completions: 4
                   backoffLimit: 0
                   template:
                     spec:
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 4x4
                       containers:
                       - name: jax-tpu
                         image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         - containerPort: 8431
                         command:
                         - bash
                         - -c
                         - |
                           python -c 'import jax; print("Global device count:", jax.device_count())'
                           sleep 60
                         resources:
                          limits:
                             google.com/tpu: 4 # This container requires 4 TPU chips
         

In this manifest, you select `tpu-v5-lite-podslice` with a `4x4` topology. This configuration means the following:

     * The topology has 16 chips in total (`4*4=16`).
     * The `tpu-v5-lite-podslice` is deployed in `ct5lp-hightpu-4t` machines that have four chips per VM. This means that to have a `4x4` topology, you need four VMs (`16/4=4`). So, the `parallelism` and `completions` fields must be set to `4`.
     * Each container in the Pod requests four TPU chips, which corresponds to the [number of chips per VM](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#standard). This is specified in the manifest with the line `google.com/tpu: 4`.
     * The `replicas` field is set to `2` to create two slices.

For more information about the possible values for these variables, see the table in [Plan your TPU on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).

### Standard
    
    apiVersion: jobset.x-k8s.io/v1alpha2
    kind: JobSet
    metadata:
      name: multislice-job
      annotations:
        alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
    spec:
      failurePolicy:
        maxRestarts: 4
      replicatedJobs:
        - name: slice
          replicas: NUM_SLICES
          template:
            spec:
              parallelism: NUM_NODES
              completions: NUM_NODES
              backoffLimit: 0
              template:
                spec:
                  hostNetwork: true
                  dnsPolicy: ClusterFirstWithHostNet
                  nodeSelector:
                    cloud.google.com/gke-tpu-accelerator: ACCELERATOR_TYPE
                    cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
                  containers:
                  - name: jax-tpu
                    image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                    ports:
                    - containerPort: 8471
                    - containerPort: 8080
                    - containerPort: 8431
                    securityContext:
                      privileged: true
                    command:
                    - bash
                    - -c
                    - |
                      python -c 'import jax; print("Global device count:", jax.device_count())'
                      sleep 60
                    resources:
                      limits:
                       google.com/tpu: NUM_CHIPS
    

Replace the following:

     * `NUM_SLICES`: the number of TPU slice node pools. In this case, the `NUM_SLICES` equals `3`.
     * `ACCELERATOR_TYPE`: the accelerator type of the TPU slice node pool. This value must map to the machine type you used during node pool creation. For example, if you created a node pool with the `ct5lp-hightpu-4t` machine type, use `tpu-v5-lite-podslice`. To learn which accelerator type to use, see the table in [Plan your TPU on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).
     * `TPU_TOPOLOGY`: the [physical topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) for the TPU slice. For example `4x4x4` or `2x2` depending on the TPU version.
     * `NUM_NODES`: the number of nodes in the node pool. It must be zero or the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of TPU chips in each VM. For multi-host TPU v4, the number of TPU chips in each VM is four. For multi-host TPU v5e, the number of TPU chips in each VM is one, four, or eight. Therefore, if your `TPU_TOPOLOGY` is `2x4x4` (TPU v4 with four TPU chips in each VM), then the `NUM_NODES` is 32/4 which equals to 8.
     * `NUM_CHIPS`: the [number of chips per VM](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#standard).

#### Expand the following section to see the description of other flags in this manifest:

     * The JobSet is a Headless Service with the same name as the JobSet name, in this case it is `multislice-job`.
     * The `alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool` annotation configures Pod affinity to ensure all Pods are scheduled on the same slice.
     * The `image` field is set to the latest [JAX AI](https://jaxstack.ai/) image. To set a different version, see the list of [current JAX AI images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#current_jax_ai_images).
     * The `maxRestarts: 4` indicates the maximum number of times that GKE restarts the JobSet when a child Job fails. If the JobSet restarts reaches the maximum defined, then the JobSet is marked as failed.
     * The `backoff` is 0 because Multislice only supports synchronous multi-controller training. Must be set to 0. Fail the job when any pod fails.
     * The values in the affinity section ensure that there is only one TPU Multislice workload running in a group of Multislices.
     * The `containerPort: 8080` is the port for MXLA coordinator.
     * The `containerPort: 8431` is the port to export the TPU usage metrics.
     * The `securityContext: privileged: true` indicates that nodes have privileged mode enabled to access TPUs. Nodes in GKE version 1.28 or later don't need to have privileged mode enabled to access TPUs. To learn more, see [Run containers without privileged mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#privileged-mode).
  2. Apply the manifest:
         
         kubectl apply -f tpu-multislice.yaml
         

  3. Confirm that the workload is admitted:
         
         kubectl get jobsets
         

The output is similar to the following:
         
         NAME            RESTARTS   COMPLETED   AGE
         multislice-job                         3s
         

  4. Monitor the status of the provisioned Pods:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                                READY   STATUS      RESTARTS   AGE
          multislice-job-slice-0-0-wzq9t      0/1     Completed   0          2m31s
          multislice-job-slice-0-1-zf4dp      0/1     Completed   0          2m30s
          multislice-job-slice-1-0-hbfn5      0/1     Completed   0          2m31s
          multislice-job-slice-1-1-45fgl      0/1     Completed   0          2m30s
          multislice-job-slice-2-0-wjbp4      0/1     Completed   0          2m30s
          multislice-job-slice-2-1-lwnvs      0/1     Completed   0          2m30s
         

The `multislice-job` JobSet schedules, creates, then runs the Pods to completion. The Pod names are in the format `<jobsetName>-<jobName>-<jobReplicaIndex>-<randomSuffix>`. The `jobsetName` prefix determines the JobSet the Pod belongs to.

  5. Optional: Remove the JAX workload:
         
         kubectl delete -f tpu-multislice.yaml
         




### Use Cluster Toolkit to create resources and submit multislice workloads

  1. [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. Deploy a GKE multislice TPU cluster by following the instructions in [Deploy a GKE TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x) or [Deploy a GKE TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e) (for TPU v4, v5e, and v5p blueprints, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples)).

When configuring your deployment blueprint, do the following:

     * Set `num_slices` to the number of TPU slices to provision (for Multislice, specify a value greater than 1, such as `2` or `4`).
     * Set `reservation` to the name of your [TPU reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).
  3. Submit a multislice workload by using the `gcluster job submit` command. For more information about job submission options, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md):
         
         gcluster job submit \
             --name=WORKLOAD_NAME \
             --cluster=DEPLOYMENT_NAME \
             --project=PROJECT_ID \
             --location=ZONE \
             --compute-type=COMPUTE_TYPE \
             --topology=TOPOLOGY \
             --num-slices=NUM_SLICES \
             --image=us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest \
             --command="python -c 'import jax; print(\"TPU cores:\", jax.device_count())'"
         

Replace the following:

     * `WORKLOAD_NAME`: the name of your workload.
     * `DEPLOYMENT_NAME`: the name of your Cluster Toolkit deployment (which is also the name of the GKE cluster).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `ZONE`: the zone where the cluster is located.
     * `COMPUTE_TYPE`: the compute type matching your node pool accelerator type, for example, `v6e-16` or `tpu7x-standard-4t`.
     * `TOPOLOGY`: the physical topology matching your node pool, for example, `2x4` or `2x2x2`.
     * `NUM_SLICES`: the number of TPU slices to allocate for the workload (matching cluster slice configuration), for example, `2` or `4`.



## Configure additional settings

The following sections describe the additional configurations you can apply to your Multislice.

### Improve network performance with hostNetwork

To improve network performance between TPU slices, we recommend you turn on `hostNetworking`. Use `hostNetwork: true` in your Pod spec to skip all the Kubernetes networking stack and let your Kubernetes Pods use the host network directly for VM-to-VM communication.

To turn on `hostNetworking`, add the following two lines to your Pod spec:
    
    
    hostNetwork: true
    dnsPolicy: ClusterFirstWithHostNet
    

To keep using the `podHostnames` for worker node discovery with `hostNetwork`, set `dnsPolicy: ClusterFirstWithHostNet`. This is important when you are running auto-resuming training Jobs and you need to have the same names for reloading the same checkpoints.

**Note:** If you don't turn on `hostNetworking`, the Multislice workload might have slower networking between slices.

If you use TPU Trillium (v6e) or Ironwood (TPU7x) ([Preview](https://cloud.google.com/products#product-launch-stages)) and your Pods use `hostNetworking`, install the following DaemonSet for tuning `/proc/sys/net/ipv4/tcp_rmem` on the node.
    
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/ai-on-gke/51bf3dcab6ff658cf62cc32867f96860bf58dfdc/scripts/network-setup/v6e-increase-rmem.yaml
    

### Improve network performance without hostNetwork on TPU Trillium or Ironwood (TPU7x)

If you use TPU Trillium or Ironwood (TPU7x) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) and your Pods can't use `hostNetworking`, implement [GKE DRANET](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra) to allocate network devices for best network performance. The GKE DRANET feature lets you request high-performance networking resources for your Pods, bypassing Kubernetes and GKE Dataplane V2.

The `ct6e-standard-4t` machine type is backed by two physical NICs. Kubernetes requires one vNIC that can't be passed to Pods. Therefore, each node must have three vNICs to allow Pods to have direct access to two vNICs to achieve best performance of both physical NICs.

**Note:** If you provision your cluster using Cluster Toolkit blueprints (such as `gke-tpu-7x` or `gke-tpu-v6e`), DRANET resources and multi-vNIC networking are configured automatically. You can skip the following steps for creating a manual network and node pool.

To enable the DRANET feature and allocate network devices for `ct6e-standard-4t`, complete the following steps:

  1. Create two additional VPCs by using the following commands:
         
         gcloud compute networks subnets create ADDITIONAL_SUBNET_1 \
             --project=PROJECT_ID \
             --network=ADDITIONAL_VPC_1 \
             --location=CONTROL_PLANE_LOCATION
         
         
         gcloud compute networks subnets create ADDITIONAL_SUBNET_2 \
             --project=PROJECT_ID \
             --network=ADDITIONAL_VPC_2 \
             --location=CONTROL_PLANE_LOCATION
         

  2. [Create a GKE cluster that uses GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra#create-cluster).

  3. Create a node pool with the created networks and GKE DRANET enabled by adding the `cloud.google.com/gke-networking-dra-driver=true` label:
         
         gcloud container node-pools create NODE_POOL_NAME \
           --location=CONTROL_PLANE_LOCATION \
           --cluster=CLUSTER_NAME \
           --machine-type=MACHINE_TYPE \
           --num-nodes=NUM_NODES \
           --additional-node-network network=ADDITIONAL_VPC_1,subnetwork=ADDITIONAL_SUBNET_1 \
           --additional-node-network network=ADDITIONAL_VPC_2,subnetwork=ADDITIONAL_SUBNET_2 \
           --node-labels=cloud.google.com/gke-networking-dra-driver=true
         

  4. After verifying the node pool status, create a workload with the additional network devices by applying a `ResourceClaimTemplate`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: two-netdev
         spec:
           spec:
             devices:
               requests:
               - name: req-netdev
                 exactly:
                   deviceClassName: netdev.google.com
                   allocationMode: ExactCount
                   count: 2
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: sample-netdevice-pod-1
         spec:
           containers:
           - name: sample-netdevice-pod
             image: busybox
             command: ["sleep", "infinity"]
             resources:
               claims:
               - name: netdev
               limits:
                 google.com/tpu: 4
           restartPolicy: Always
           resourceClaims:
           - name: netdev
             resourceClaimTemplateName: two-netdev
         

  5. Verify that the interfaces are available in the Pod:
         
         kubectl exec -it pods/sample-netdevice-pod-1 -- ip a
         


**Best practice** : 

Use `eth1` and `eth2` interfaces for better networking performance, instead of the `eth0` interface. This can be done by adding `export LIBTPU_INIT_ARGS="$LIBTPU_INIT_ARGS --megascale_grpc_interface_prefixes=eth1,eth2,lo"` to the workload specification.

### Enable logging

Logs emitted by containers running on GKE nodes, including TPU slice nodes, are visible in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), if you have [GKE system logging enabled](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing#available-logs) in your cluster.

You can [view your logs from GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs) by using the Logs Explorer with the following filter to view the container logs for your workload:
    
    
    resource.type="k8s_container"
    resource.labels.cluster_name=CLUSTER_NAME
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"=JOBSET_NAME
    

Use the following filter for TPU slice and workers:
    
    
    resource.type="k8s_container"
    resource.labels.cluster_name=CLUSTER_NAME
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"=JOBSET_NAME
    resource.labels.pod_name:<jobSetName>-<replicateJobName>-<job-index>-<worker-index>
    

To learn more, see [View GKE TPU logs](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus#view-tpu-logs).

### Enable additional metrics

In addition to the general [TPU metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#metrics), there are 4 additional multislice specific TPU runtime metrics. These metrics are available in GKE version 1.29.1-gke.1016000 or later. TPU workload must use JAX version [0.4.24](https://github.com/google/jax/releases/tag/jaxlib-v0.4.24)

The following are the available multislice metrics:

  * **DCN (Data Center Network) transfer latencies** : Distribution of network transfer latencies for multislice traffic.
  * **Collective latencies** : Distribution of end to end collective latency for multislice traffic.
  * **Host-to-Device transfer latencies** : Distribution of host to device transfer latency for each chunk of data for multislice traffic.
  * **Device-to-Host transfer latencies** : Distribution of device to host transfer latency for each chunk of data for multislice traffic.



These metrics are located in the Kubernetes container (`k8s_container`) schema:

  * `kubernetes.io/container/multislice/network/dcn_transfer_latencies`
  * `kubernetes.io/container/multislice/network/collective_end_to_end_latencies`
  * `kubernetes.io/container/multislice/accelerator/host_to_device_transfer_latencies`
  * `kubernetes.io/container/multislice/accelerator/device_to_host_transfer_latencies`



## TPU slice versus Multislice

The following table differentiates the architectural organization of a TPU slice and a Multislice:

| TPU slice | Multislice  
---|---|---  
Interconnectivity | The workload runs on a single TPU slice. All TPU chips in a slice are connected with ICI. | The workload runs on multiple TPU slices. Communication within a slice happens over ICI. Communication between slices occurs over DCN.  
Supported node pools | Single-host TPU slice and multi-host TPU slice | Groups of multi-host TPU slices  
Recommended workload type | IndexedJob or JobSet | JobSet  
  
## Clean up resources

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the tutorial. Alternatively, you can delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

Delete the GKE cluster:
    
    
    ```sh
    gcloud container clusters delete  CLUSTER_NAME \
       --project=PROJECT_ID  \
       --location=CONTROL_PLANE_LOCATION
    ```
    

### Delete Cluster Toolkit resources

If you used Cluster Toolkit to create your cluster, delete the deployment to avoid incurring further charges:
    
    
    gcluster destroy DEPLOYMENT_NAME
    

Replace `DEPLOYMENT_NAME` with the name of the deployment directory created when you deployed your blueprint.

## What's next

  * Learn how to [Orchestrate Multislice workloads with TPU slices](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
