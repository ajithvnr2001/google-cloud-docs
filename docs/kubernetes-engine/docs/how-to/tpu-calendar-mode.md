---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode/
title: Request TPUs with future reservation in calendar mode \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:36.223265+00:00
---

# Request TPUs with future reservation in calendar mode  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Request TPUs with future reservation in calendar mode Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Future reservation in calendar mode**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to optimize Tensor Processing Unit (TPU) provisioning by using future reservation in calendar mode. Future reservation in calendar mode is a built-in calendar advisor and recommender that can help you locate TPU capacity and plan ahead. You can request capacity for a specified start time and duration, between 1 and 90 days, and the recommender will provide suggested dates.

This guide is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for running batch workloads. For more information about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

For more information, see [About future reservation in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

## Use cases

Future reservation in calendar mode works best for workloads with scheduled, short-term, high-demand requests, like training, or batch inference models that require high availability at the requested start time.

If your workload requires dynamically provisioned resources as needed, for up to 7 days without long-term reservations or complex quota management, consider using the _flex-start_ consumption option. For more information, see [About GPU and TPU provisioning with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have either of the following: 
    * an existing [Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) that's running version 1.28.3-gke.1098000 or later.
    * an existing [Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) that's running version 1.30.3-gke.1451000 or later.



## Request future reservation in calendar mode for TPUs

The process to request TPUs with future reservation in calendar mode involves the following steps:

  1. Ensure that you have sufficient quota for any resources that aren't part of a reservation when VMs are created, such as disks or IP addresses. Future reservation requests in calendar mode don't require Compute Engine quota.
  2. Complete the steps in [create a request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#create-request). These steps include the following: 
     1. View TPU future availability.
     2. Create and submit a future reservation request in calendar mode for TPUs.
     3. Wait for Google Cloud to approve your request.
  3. Create a TPU node pool that uses your reservation.



## Create a node pool

This section applies to Standard clusters only, because Autopilot mode automatically creates nodes based on the workloads.

You can use your reservation when you create single-host or multi-host TPU slice node pools.

### Create a single-host TPU slice node pool

You can create a [single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host) using the Google Cloud CLI.
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --cluster=CLUSTER_NAME \
        --node-locations=NODE_ZONES \
        --machine-type=MACHINE_TYPE \
        --reservation-affinity=specific \ This is required
        --reservation=RESERVATION
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `CONTROL_PLANE_LOCATION`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `CLUSTER_NAME`: the name of the cluster.
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool.
  * `MACHINE_TYPE`: the type of machine to use for nodes. For more information about TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `RESERVATION`: the name of the calendar reservation to consume.



For a full list of all the flags that you can specify, see the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) reference.

After you create a node pool with the calendar reservation, you can deploy your workload like any other TPU node pool. Consuming future reservation in calendar mode works in the same way as for any other type of reservation. For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

### Create a multi-host TPU slice node pool

The steps to create a multi-host TPU slice node pool differ depending on whether you use Ironwood (TPU7x) or an earlier TPU version. 

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
             --location=us-central1 \
             --node-locations=us-central1-c \
             --machine-type=tpu7x-standard-4t \
             --reservation-affinity=specific \
             --reservation=FUTURE_RESERVATION_NAME \
             --placement-policy=WORKLOAD_POLICY \
             --consolidation-delay=CONSOLIDATION_DELAY
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the new node pool.
     * `WORKLOAD_POLICY`: the name of the workload policy that you created. 
     * `FUTURE_RESERVATION_NAME`: the name of your future reservation. 

This command creates a node pool named NODE_POOL_NAME with the following characteristics:

     * `--machine-type=tpu7x-standard-4t` specifies the Ironwood (TPU7x) machine type. 



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
    
    
      gcloud container node-pools create NODE_POOL_NAME \
          --cluster=CLUSTER_NAME \
          --location=CONTROL_PLANE_LOCATION \
          --node-locations=NODE_ZONES \
          --machine-type=MACHINE_TYPE \
          --tpu-topology=TPU_TOPOLOGY \
          --reservation-affinity=specific \
          --reservation=FUTURE_RESERVATION_NAME
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  * `MACHINE_TYPE`: the type of machine to use for nodes. For more information about TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `TPU_TOPOLOGY`: the TPU topology. For example, `2x2x2`. To see all supported TPU topologies, see the [topology section](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology). 
  * `FUTURE_RESERVATION_NAME`: the name of your future reservation.
  * `CONSOLIDATION_DELAY`: optional. The duration that Cluster Autoscaler waits before it can scale down underutilized nodes. Use this setting to delay scale-down and keep the node pool for later reuse by other Pods. The number that you enter must end in `s`. For example, to specify one hour, enter `3600s`. Available in GKE version `1.34.1-gke.2364000` and later.




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




After you create a node pool with the calendar reservation, you can deploy your workload like any other TPU node pool. Consuming future reservation in calendar mode works in the same way as for any other type of reservation. For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

## What's next

  * Try GKE deployment examples for generative AI models that use the TPU resources that you reserved:

    * [Serve an LLM using TPU Trillium on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu)
    * [Serve an LLM using TPUs on GKE with KubeRay](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-lllm-tpu-ray)
    * [Serve an LLM using TPUs on GKE with JetStream and PyTorch](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-llm-tpu-jetstream-pytorch)
    * [Serve Gemma using TPUs on GKE with JetStream](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-tpu-jetstream)
    * [Serve Stable Diffusion XL (SDXL) using TPUs on GKE with MaxDiffusion](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu)
    * [Serve open source models using TPUs on GKE with Optimum TPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimum-tpu)
  * Explore experimental samples for leveraging GKE to accelerate your AI/ML initiatives in [GKE AI Labs](https://gke-ai-labs.dev/).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
