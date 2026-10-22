---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus/
title: Deploy TPU workloads in GKE Standard \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:39.562895+00:00
---

# Deploy TPU workloads in GKE Standard  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy TPU workloads in GKE Standard Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides a foundation for learning how to accelerate machine learning (ML) workloads using TPUs in Google Kubernetes Engine (GKE). TPUs are designed for matrix multiplication processing, such as large-scale deep learning model training. TPUs are optimized to handle the enormous datasets and complex models of ML and therefore are more cost-effective and energy efficient for ML workloads due to their superior performance. In this guide, you learn how to deploy ML workloads by using Cloud TPU accelerators, configure quotas for TPUs, configure upgrades for node pools that run TPUs, and monitor TPU workload metrics.

This tutorial is intended for Machine learning (ML) engineers and Platform admins and operators who are interested in using Kubernetes container orchestration to manage large-scale model training, tuning, and inference workloads using TPUs. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * [Cloud TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
  * [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions)
  * [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Plan your TPU configuration

Plan your TPU configuration based on your model and how much memory it requires. Before you use this guide to deploy your workloads on TPU, complete the planning steps in [Plan your TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#plan-tpu-configuration).

## Ensure that you have TPU quota

The following sections help you ensure that you have enough quota when using TPUs in GKE. 

### Quota for on-demand or Spot VMs

If you are creating a [TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology) with on-demand or Spot VMs, you must have sufficient TPU quota available in the region that you want to use.

Creating a TPU slice node pool that consumes a TPU reservation does _not_ require any TPU quota.1 You may safely skip this section for reserved TPUs.

Creating an on-demand or Spot TPU slice node pool in GKE requires Compute Engine API quota. Compute Engine API quota (compute.googleapis.com) is not the same as Cloud TPU API quota (tpu.googleapis.com), which is needed when creating TPUs with the Cloud TPU API. 

To check the limit and current usage of your Compute Engine API quota for TPUs, follow these steps:

  1. Go to the **Quotas** page in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter_list **Filter** box, do the following:

     1. Use the following table to select and copy the property of the quota based on the TPU version and machine type. For example, if you plan to create on-demand TPU v5e nodes whose machine type begins with `ct5lp-` , enter `Name: TPU v5 Lite PodSlice chips`.

TPU version, machine type begins with  | Property and name of the quota for on-demand instances | Property and name of the quota for Spot2 instances  
---|---|---  
TPU v3,  
`ct3-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3

| Not applicable  
TPU v3,  
`ct3p-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3P

| Not applicable  
TPU v4,  
`ct4p-` | 
            
            Name:  
            TPU v4 PodSlice chips

| 
            
            Name:  
            Preemptible TPU v4 PodSlice chips  
  
TPU v5e,  
`ct5lp-` | 
            
            Name:  
            TPU v5 Lite PodSlice chips

| 
            
            Name:  
            Preemptible TPU v5 Lite Podslice  
            chips  
  
TPU v5p,  
`ct5p-` | 
            
            Name:  
            TPU v5p chips

| 
            
            Name:  
            Preemptible TPU v5p chips  
  
TPU Trillium,  
`ct6e-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT6E

| 
            
            Name:  
            Preemptible TPU slices v6e  
  
Ironwood (TPU7x),  
`tpu7x-standard-4t` | 
            
            Dimensions (e.g. location):  
            tpu_family:tpu7x

| 
            
            Name:  
            Preemptible TPU slices tpu7x  
  
     2. Select the **Dimensions (e.g. locations)** property and enter `region:` followed by the name of the region in which you plan to create TPUs in GKE. For example, enter `region:us-west4` if you plan to create TPU slice nodes in the zone `us-west4-a`. TPU quota is regional, so all zones within the same region consume the same TPU quota.




If no quotas match the filter you entered, then the project has not been granted any of the specified quota for the region that you need, and you must [request a TPU quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

When a TPU reservation is created, both the limit and current use values for the corresponding quota increase by the number of chips in the TPU reservation. For example, when a reservation is created for 16 TPU v5e chips whose machine type begins with `ct5lp-` , then both the **Limit** and **Current usage** for the `TPU v5 Lite PodSlice chips` quota in the relevant region increase by 16.

  1. When creating a TPU slice node pool, use the [`--reservation` and `--reservation-affinity=specific` flags](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--reservation) to create a reserved instance. TPU reservations are available when purchasing a commitment. ↩

  2. When creating a TPU slice node pool, use the [`--spot` flag](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--spot) to create a [Spot](https://cloud.google.com/spot-vms) instance. ↩




### Quotas for additional GKE resources

You may need to increase the following GKE-related quotas in the regions where GKE creates your resources.

  * **Persistent Disk SSD (GB) quota** : The boot disk of each Kubernetes node requires 100GB by default. Therefore, this quota should be set at least as high as the product of the maximum number of GKE nodes you anticipate creating and 100GB (nodes * 100GB).
  * **In-use IP addresses quota** : Each Kubernetes node consumes one IP address. Therefore, this quota should be set at least as high as the maximum number of GKE nodes you anticipate creating.
  * **Ensure that`max-pods-per-node` aligns with the subnet range**: Each Kubernetes node uses secondary IP ranges for Pods. For example, `max-pods-per-node` of 32 requires 64 IP addresses which translates to a /26 subnet [per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#cidr_ranges_for_clusters). Note that this range shouldn't be shared with any other cluster. To avoid exhausting the IP address range, use the `--max-pods-per-node` flag to limit the number of pods allowed to be scheduled on a node. The quota for `max-pods-per-node` should be set at least as high as the maximum number of GKE nodes you anticipate creating.



To request an increase in quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Ensure reservation availability

To create a TPU slice node pool using a reservation, the reservation must have sufficient available TPU chips at the time of node pool creation.

To see which reservations exist within a project and how many TPU chips within a TPU reservation are available, [view a list of your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).

## Create a cluster

### gcloud

Create a GKE cluster in Standard mode in a region with available TPUs.

**Best practice** : 

Use regional clusters, which provide high availability of the Kubernetes control plane.
    
    
    gcloud container clusters create CLUSTER_NAME \
      --location LOCATION \
      --cluster-version VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `LOCATION`: the region with your TPU capacity available.
  * `VERSION`: the GKE version, which must support the machine type that you want to use. Note that the default GKE version might not have availability for your target TPU. To learn what are the minimum GKE versions available by TPU machine type, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).



###  Cluster Toolkit 

  1. [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. Deploy a GKE TPU cluster by using a Cluster Toolkit blueprint (such as [`gke-tpu-v6e`](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e) or [`gke-tpu-7x`](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x); for TPU v4, v5e, and v5p blueprints, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples)):
         
         gcluster deploy examples/gke-tpu-7x/gke-tpu-7x.yaml \
           --vars project_id=PROJECT_ID,deployment_name=DEPLOYMENT_NAME,zone=ZONE
         

Replace the following:

     * `DEPLOYMENT_NAME`: a name for the Cluster Toolkit deployment (which is also the name of the GKE cluster).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `ZONE`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability). To use reserved capacity, ensure that you use the zone where you reserved the capacity.



You have created a GKE cluster with a node pool that includes the specified TPU resources. You can now follow the steps in the run your workload on TPU slice nodes section in this document.

## Provision TPUs

To provision TPUs in GKE you have the following configuration options: 

  * **Manually create a node pool** : you can create a node pool with a specific TPU version and topology.
  * **Use GKE node auto-provisioning** : you can enable node auto-provisioning at the cluster level and then, in your Pod's manifest, use a nodeSelector to specify the TPU version and topology. When a pending Pod matches these selectors, GKE automatically creates a new node pool that meets the request. This method requires you to set cluster-level resource limits for TPUs.
  * **Define custom ComputeClasses** : you can request TPUs by using custom ComputeClasses. Custom ComputeClasses let platform administrators define a hierarchy of node configurations for GKE to prioritize during node scaling decisions, so that workloads run on your selected hardware. 



### Manually create a node pool

You can create a single or multi-host TPU slice node pool.

#### Create a single-host TPU slice node pool

You can create a [single-host TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#single-host) using the Google Cloud CLI, Terraform, or the Google Cloud console.

### gcloud
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --location=LOCATION \
        --cluster=CLUSTER_NAME \
        --node-locations=NODE_ZONES \
        --machine-type=MACHINE_TYPE \
        [--sandbox=type=gvisor]
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `LOCATION`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `CLUSTER_NAME`: the name of the cluster.
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  * `MACHINE_TYPE`: the [TPU version and type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t` for Ironwood (TPU7x).



Optionally, you can also use the following flags:

  * `--num-nodes=NUM_NODES`: the initial number of nodes in the node pool in each zone.

**Best practice** : 

If you use the `enable-autoscaling` flag for the node pool, set `num-nodes` to `0` so that the autoscaler provisions additional nodes as soon as your workloads demand them.

  * `--reservation=RESERVATION_NAME`: the name of the reservation GKE uses when creating the node pool. If you omit this flag, GKE uses available TPUs. To learn more about TPU reservations, see [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations).

  * `--node-labels cloud.google.com/gke-workload-type=HIGH_AVAILABILITY`: tells GKE that the single-host TPU slice node pool is part of a collection. Use this flag if the following conditions apply:

    * The node pool runs inference workload in the new node pool.
    * The node pool uses TPU Trillium.
    * The node pool doesn't use Spot VMs.

To learn more about collection scheduling management, see Manage collection scheduling in single-host TPU slices.

  * `--enable-autoscaling`: create a node pool with autoscaling enabled. Requires the following additional flags:

    * `--total-min-nodes=TOTAL_MIN_NODES`: minimum number of all nodes in the node pool.
    * `--total-max-nodes=TOTAL_MAX_NODES`: maximum number of all nodes in the node pool.
    * `--location-policy=ANY`: prioritize usage of unused reservations and reduce the preemption risk of Spot VMs.
  * `--spot`: sets the node pool to use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) for the nodes in the node pool. This cannot be changed after node pool creation.

  * `--flex-start`: sets the node pool to use Flex-start VMs. Flex-start VMs are created by using the [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. For more information, see [Run a small batch workload with TPUs and Flex-start VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu).




For a full list of all the flags that you can specify, see the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) reference.

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
    
      node_config {
        machine_type = MACHINE_TYPE
        reservation_affinity {
          consume_reservation_type = "SPECIFIC_RESERVATION"
          key = "compute.googleapis.com/reservation-name"
          values = [RESERVATION_LABEL_VALUES]
        }
        spot = true
        flex_start = false
      }
    }
    

Replace the following:

  * `NODE_POOL_RESOURCE_NAME`: the name of the node pool resource in the Terraform template.
  * `PROJECT_ID`: your project ID.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `POOL_NAME`: the name of the node pool to create.
  * `CLUSTER_LOCATION`: the compute zone(s) of the cluster. Specify the region where the TPU version is available. To learn more, see [Select a TPU version and topology](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#version_and_topology).
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  * `MACHINE_TYPE`: the type of TPU machine to use. To see TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).



Optionally, you can also use the following variables:

  * `autoscaling`: create a node pool with autoscaling enabled. For single-host TPU slice, GKE scales between the `TOTAL_MIN_NODES` and `TOTAL_MAX_NODES` values. 
    * `TOTAL_MIN_NODES`: minimum number of all nodes in the node pool. This field is optional unless autoscaling is also specified.
    * `TOTAL_MAX_NODES`: maximum number of all nodes in the node pool. This field is optional unless autoscaling is also specified.
  * `RESERVATION_NAME`: if you use [About Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations), this is the list of labels of the reservation resources to use when creating the node pool. To learn more about how to populate the `RESERVATION_LABEL_VALUES` in the `reservation_affinity` field, see [Terraform Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#reservation_affinity).
  * `spot`: sets the node pool to use Spot VMs for the TPU nodes. This cannot be changed after node pool creation. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * `flex_start`: sets the node pool to use [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. Can't be set to `true` if `spot` is enabled. Flex-start is supported in GKE version 1.33.0-gke.1712000 or later.



### Console

To create a node pool with TPUs:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. In the **Node pool details** section, check the **Specify node locations** box.

  6. Select the zone based on the TPU version you want to use. To identify an available zone, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).

  7. From the navigation pane, click **Nodes**.

  8. In the **Machine Configuration** section, select **TPUs**.

  9. In the **Series** drop-down menu, select one of the following:

     * **CT3** : TPU v3, single host device
     * **CT3P** : TPU v3, multi host pod slice
     * **CT4P** : TPU v4
     * **CT5LP** : TPU v5e
     * **CT5P** : TPU v5p
     * **CT6E** : TPU Trillium (v6e)
  10. In the **Machine type** drop-down menu, select the name of the machine to use for nodes. Use the [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version) table to learn how to define the machine type and TPU topology that create a _single-host_ TPU slice node pool.

  11. In the **TPU Topology** drop-down menu, select the physical topology for the TPU slice.

  12. In the **Changes needed** dialog, click **Make changes**.

  13. Ensure that **Boot disk type** is either **Standard persistent disk** or **SSD persistent disk**.

  14. Optionally, select the **Enable nodes on spot VMs** checkbox to use Spot VMs for the nodes in the node pool.

  15. Click **Create**.




#### Create a multi-host TPU slice node pool

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




### Use GKE node auto-provisioning

You can configure GKE to automatically create and delete node pools to meet the resource demands of your TPU workloads.

  1. To enable node pool auto-provisioning, edit your cluster TPU resource limits:
         
         gcloud container clusters update CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --enable-autoprovisioning \
               --min-cpu=MINIMUM_CPU \
               --min-memory=MINIMUM_MEMORY \
               --max-cpu=MAXIMUM_CPU \
               --max-memory=MAXIMUM_MEMORY \
               **--min-accelerator =type=TPU_TYPE,count=MINIMUM_TPU_COUNT \
               --max-accelerator=type=TPU_TYPE,count=MAXIMUM_TPU_COUNT**
         

Replace the following:

     * `TPU_TYPE`: the [TPU type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t` for Ironwood (TPU7x).
     * `MINIMUM_TPU_COUNT`: the minimum number of TPU chips of the specified type that the cluster can have. If the value that you specify is larger than the number of TPU chips in a multi-host TPU slice, GKE removes all nodes in the slice. Multi-host node pools scale between 0 and the number of nodes in the slice, with no intermediate values.
     * `MAXIMUM_TPU_COUNT`: the maximum number of TPU chips of the specified type that the cluster can have. For multi-host TPU slices, specify a value that's greater than the number of chips in each slice so that GKE can scale the slice atomically. The number of chips in a slice is the product of the TPU topology. For example, if the topology is `2x2x2`, the number of chips in the slice is `8`, which means that the value of `MAXIMUM_TPU_COUNT` must be greater than `8`.



### Define custom ComputeClasses

You can also configure GKE to request TPUs during scaling operations that create new nodes by using _custom ComputeClasses_.

You can specify TPU configuration options in your custom ComputeClass specification. When a GKE workload uses that custom ComputeClass, GKE attempts to provision TPUs that use your specified configuration when scaling up.

The following sections show you how to create a custom ComputeClass and then create a Job that consumes the TPUs defined in the ComputeClass.

#### Create a custom ComputeClass

The steps to create a custom ComputeClass that follows the [TPU rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration) differ depending on whether you use Ironwood (TPU7x) or an earlier TPU version.

###  Ironwood (TPU7x) 

  1. Create a workload policy. This step is required only if you are creating a multi-host node pool, which depends on the topology you choose. If you use a single-host node pool, skip this step.
         
         gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=TPU_TOPOLOGY \
             --project=PROJECT_ID \
             --region=REGION
         

Replace the following:

     * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
     * `TPU_TOPOLOGY`: the TPU Ironwood (TPU7x) topology. For example, use `2x2x2`. For more information about all supported Ironwood (TPU7x) topologies, see [topology section](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `REGION`: The region for the workload policy. A workload policy is a regional resource and you can use it across node pools.
  2. Save the following manifest as `tpu-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: tpu-class
         spec:
           priorities:
             - tpu:
                 type: tpu7x
                 topology: TPU_TOPOLOGY
                 count: 4
               placement:
                 policyName: WORKLOAD_POLICY_NAME
           nodePoolAutoCreation:
             enabled: true
         

  3. (Optional) You can consume a specific reservation or sub-block. For example, you can add the following `specs` to your `ComputeClass` manifest:
         
         reservations:
             affinity: Specific
             specific:
               - name: RESERVATION_NAME
                 reservationBlock:
                   name: RESERVATION_BLOCK_NAME
                   reservationSubBlock:
                     name: RESERVATION_SUB_BLOCK_NAME
         

Replace the following:

     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `RESERVATION_BLOCK_NAME`: the name of the Compute Engine capacity reservation block.
     * `RESERVATION_SUB_BLOCK_NAME`: the name of the Compute Engine capacity reservation sub-block.

For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).




### Other TPU versions

To provision v3, v4, v5p, v5e, or v6e (Trillium) TPUs by using a custom ComputeClass [configured for TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration), complete the following steps:

  1. Save the following manifest as `tpu-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: tpu-class
         spec:
           priorities:
           - tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           - spot: true
             tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           - flexStart:
               enabled: true
             tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `TPU_TYPE`: the TPU type to use, like `tpu-v4-podslice`. Must be a value [supported by GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `TOPOLOGY`: the arrangement of TPU chips in the slice, like `2x2x4`. Must be a supported topology for the selected TPU type.
     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`.
  2. Deploy the ComputeClass:
         
         kubectl apply -f tpu-compute-class.yaml
         

For more information about custom ComputeClasses and TPUs, see [TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration).




#### Create a Job that consumes TPUs

  1. Save the following manifest as `tpu-job.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-job
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-job
         spec:
           backoffLimit: 0
           completions: 4
           parallelism: 4
           completionMode: Indexed
           template:
             spec:
               subdomain: headless-svc
               restartPolicy: Never
               nodeSelector:
                 **cloud.google.com/compute-class : tpu-class**
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())'
                 resources:
                   requests:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
                   limits:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
         

Replace the following:

     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`, equal to the `CHIP_COUNT` value in the selected custom ComputeClass.
     * `MEMORY_SIZE`: The maximum amount of memory that the TPU uses. Memory limits depend on the TPU version and topology that you use. To learn more, see [Minimums and maximums for accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#accelerator-class-min-max).
     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`.
  2. Deploy the Job:
         
         kubectl create -f tpu-job.yaml
         

When you create this Job, GKE automatically does the following:

     * Provisions nodes to run the Pods. Depending on the TPU type, topology, and resource requests that you specified, these nodes are either single-host slices or multi-host slices. Depending on the availability of TPU resources in the top priority, GKE might fall back to lower priorities to maximize flexibility, efficiency, and availability of accelerator capacity.
     * Adds taints to the Pods and tolerations to the nodes to prevent any of your other workloads from running on the same nodes as TPU workloads.

To learn more, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

  3. When you finish this section, you can avoid continued billing by deleting the resources you created:
         
         kubectl delete -f tpu-job.yaml
         




## Prepare your workloads

TPU workloads have the following preparation requirements.

  1. Frameworks like JAX, PyTorch, and TensorFlow access TPU VMs using the `libtpu` shared library. `libtpu` includes the XLA compiler, TPU runtime software, and the TPU driver. Each release of PyTorch and JAX requires a certain `libtpu.so` version. To avoid package version conflicts, we recommend using a [JAX AI image](https://docs.cloud.google.com/ai-hypercomputer/docs/images#current_jax_ai_images). To use TPUs in GKE, ensure that you use the following versions: TPU type | `libtpu.so` version  
---|---  
Ironwood (TPU7x) `tpu7x`  
| 
     * Recommended JAX AI image: [jax0.8.1-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.8.1-rev1)
     * Recommended jax[tpu] version: [v0.8.1](https://github.com/jax-ml/jax/tree/jax-v0.8.1)  
TPU Trillium (v6e)  
`tpu-v6e-slice`  
| 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [v0.4.9 or later](https://github.com/google/jax/tree/jaxlib-v0.4.9)
     * Recommended torchxla[tpuvm] version: [v2.1.0 or later](https://github.com/pytorch/xla/releases/tag/v2.1.0)  
TPU v5e  
`tpu-v5-lite-podslice`  
| 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [v0.4.9 or later](https://github.com/google/jax/tree/jaxlib-v0.4.9)
     * Recommended torchxla[tpuvm] version: [v2.1.0 or later](https://github.com/pytorch/xla/releases/tag/v2.1.0)  
TPU v5p  
`tpu-v5p-slice` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [0.4.19 or later](https://github.com/google/jax/tree/jax-v0.4.19).
     * Recommended torchxla[tpuvm] version: suggested to use a nightly version build on October 23, 2023.  
TPU v4  
`tpu-v4-podslice` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu]: [v0.4.4 or later](https://github.com/google/jax/tree/jaxlib-v0.4.4)
     * Recommended torchxla[tpuvm]: [v2.0.0 or later](https://github.com/pytorch/xla/releases/tag/v2.0.0)  
TPU v3  
`tpu-v3-slice`  
`tpu-v3-device` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu]: [v0.4.4 or later](https://github.com/google/jax/tree/jaxlib-v0.4.4)
     * Recommended torchxla[tpuvm]: [v2.0.0 or later](https://github.com/pytorch/xla/releases/tag/v2.0.0)  
  2. In your workload manifest, add Kubernetes node selectors to ensure that GKE schedules your TPU workload on the TPU machine type and TPU topology you defined: 
         
         nodeSelector:
             cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR
             cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
             cloud.google.com/placement-policy-name: WORKLOAD_POLICY # Required only for Ironwood (TPU7x)
           

Replace the following:

     * `TPU_ACCELERATOR`: the name of the [TPU accelerator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t`.
     * `TPU_TOPOLOGY`: the physical topology for the TPU slice. The format of the topology depends on the TPU version. For example, use `2x2x2`. To learn more, see [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `WORKLOAD_POLICY`: the name of the workload policy that you want to use to place your TPU Pods. This node selector is required only for Ironwood (TPU7x).



After you complete the workload preparation, you can run a Job that uses TPUs.

The following sections show examples on how to run a Job that performs basic computation with TPUs.

## Run your workload on TPU slice nodes

This section explains how to prepare your workloads and examples of how you can run your workloads.

### Example 1: Run a Deployment that requests TPUs in the Pod specification

### gcloud

GKE uses the configuration in your Pod or ComputeClass to determine the configuration of your TPU nodes. The following manifest is an example of a Deployment specification that requests TPUs in the Pod specification. If the cluster-level node auto-provisioning setting is enabled, this Deployment triggers node pool auto-creation. When you create this example Deployment, GKE creates a node pool that contains a TPU v4 slice with a `2x2x2` topology and two `ct4p-hightpu-4t` machines.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: tpu-workload
      labels:
        app: tpu-workload
    spec:
      replicas: 2
      template:
        spec:
          nodeSelector:
            cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice
            cloud.google.com/gke-tpu-topology: 2x2x2
          containers:
          - name: tpu-job
            image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
            ports:
            - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
            securityContext:
              privileged: true # Required for GKE versions earlier than 1.28 to access TPUs.
            command:
            - bash
            - -c
            - |
              python -c 'import jax; print("Total TPU chips:", jax.device_count())'
            resources:
              requests:
                google.com/tpu: 4
              limits:
                google.com/tpu: 4
            ports:
            - containerPort: 80
    

In this manifest, the following fields define TPU configuration:

  * `cloud.google.com/gke-tpu-accelerator`: the [TPU version and type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t` for Ironwood (TPU7x).
  * `cloud.google.com/gke-tpu-topology`: the [topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) with number and physical arrangement of TPU chips within a TPU slice. For example, use `2x2x2`.
  * `limits.google.com/tpu`: the number of [TPU chips per VM](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, if you use `tpu7x-standard-4t`, the number of TPU chips per VM is `4`.



###  Cluster Toolkit 

Submit the workload by using the `gcluster job submit` command. For more information about job submission options, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md):
    
    
    gcluster job submit \
      --name=WORKLOAD_NAME \
      --cluster=DEPLOYMENT_NAME \
      --project=PROJECT_ID \
      --location=ZONE \
      --compute-type=COMPUTE_TYPE \
      --topology=TOPOLOGY \
      --num-slices=1 \
      --image=us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest \
      --command="python -c 'import jax; print(\"TPU cores:\", jax.device_count())'"
    

Replace the following:

  * `WORKLOAD_NAME`: the name of your workload.
  * `DEPLOYMENT_NAME`: the name of your Cluster Toolkit deployment (which is also the name of the GKE cluster).
  * `PROJECT_ID`: your Google Cloud project ID.
  * `ZONE`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `COMPUTE_TYPE`: the compute type matching your node pool accelerator type, for example, `v6e-16`, `tpu7x-standard-4t`, or `v5e-8`.
  * `TOPOLOGY`: the physical topology matching your node pool, for example, `2x4` or `2x2x2`.



### Example 2: Run a workload that displays the number of available TPU chips in a TPU slice node pool

The following workload returns the number of TPU chips across all of the nodes in a multi-host TPU slice. To create a multi-host slice, the workload has the following parameters:

  * TPU version: TPU v4
  * Topology: 2x2x4



This version and topology selection result in a multi-host slice.

  1. Save the following manifest as `available-chips-multihost.yaml`: 
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-available-chips
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-available-chips
         spec:
           backoffLimit: 0
           completions: 4
           parallelism: 4
           completionMode: Indexed
           template:
             spec:
               subdomain: headless-svc
               restartPolicy: Never
               nodeSelector:
                 cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice # Node selector to target TPU v4 slice nodes.
                 cloud.google.com/gke-tpu-topology: 2x2x4 # Specifies the physical topology for the TPU slice.
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 securityContext:
                   privileged: true # Required for GKE versions earlier than 1.28 to access TPUs.
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())' # Python command to count available TPU chips.
                 resources:
                   requests:
                     cpu: 10
                     memory: 407Gi
                     **google.com/tpu : 4** # Request 4 TPU chips for this workload.
                   limits:
                     cpu: 10
                     memory: 407Gi
                     **google.com/tpu : 4** # Limit to 4 TPU chips for this workload.

  2. Deploy the manifest: 
         
         kubectl create -f available-chips-multihost.yaml
         

GKE runs a TPU v4 slice with four VMs (multi-host TPU slice). The slice has 16 interconnected TPU chips.

  3. Verify that the Job created four Pods: 
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                       READY   STATUS      RESTARTS   AGE
         tpu-job-podslice-0-5cd8r   0/1     Completed   0          97s
         tpu-job-podslice-1-lqqxt   0/1     Completed   0          97s
         tpu-job-podslice-2-f6kwh   0/1     Completed   0          97s
         tpu-job-podslice-3-m8b5c   0/1     Completed   0          97s
         

  4. Get the logs of one of the Pods: 
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of one of the created Pods. For example, `tpu-job-podslice-0-5cd8r`.

The output is similar to the following: 
         
         TPU cores: 16
         

  5. Optional: Remove the workload: 
         
         kubectl delete -f available-chips-multihost.yaml
         




### Example 3: Run a workload that displays the number of available TPU chips in the TPU slice

The following workload is a static Pod that displays the number of TPU chips that are attached to a specific node. To create a single-host node, the workload has the following parameters:

  * TPU version: TPU v5e
  * Topology: 2x4



This version and topology selection result in a single-host slice.

  1. Save the following manifest as `available-chips-singlehost.yaml`: 
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: tpu-job-jax-v5
         spec:
           restartPolicy: Never
           nodeSelector:
             cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice # Node selector to target TPU v5e slice nodes.
             cloud.google.com/gke-tpu-topology: 2x4 # Specify the physical topology for the TPU slice.
           containers:
           - name: tpu-job
             image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
             ports:
             - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
             securityContext:
               privileged: true # Required for GKE versions earlier than 1.28 to access TPUs.
             command:
             - bash
             - -c
             - |
               python -c 'import jax; print("Total TPU chips:", jax.device_count())'
             resources:
               requests:
                 google.com/tpu: 8 # Request 8 TPU chips for this container.
               limits:
                 google.com/tpu: 8 # Limit to 8 TPU chips for this container.

  2. Deploy the manifest: 
         
         kubectl create -f available-chips-singlehost.yaml
         

GKE provisions nodes with eight single-host TPU slices that use TPU v5e. Each TPU node has eight TPU chips (single-host TPU slice).

  3. Get the logs of the Pod: 
         
         kubectl logs tpu-job-jax-v5
         

The output is similar to the following: 
         
         Total TPU chips: 8
         

  4. Optional: Remove the workload: 
         
         kubectl delete -f available-chips-singlehost.yaml
           




### Example 4: Run a workload that targets two NUMA nodes

To optimize your workload performance, GKE lets you deploy your workloads in a multi-container setup. This binds each container to the CPU, memory, and TPU resources within a given NUMA node. For more information about NUMA binding, see [About Ironwood (TPU7x) in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood#numa-binding).

**Important:** Only Ironwood (TPU7x) in GKE cluster version is 1.34.1-gke.1100000 or later supports multi-container configuration.

  1. Create a file named `topology-manager-config.yaml` with the following content:
         
         kubeletConfig:
           cpuManagerPolicy: static
           topologyManager:
             policy: best-effort
             scope: container
         

This configuration aligns resources requested by a container to a single NUMA node. This configuration is necessary for GKE to admit and correctly assign chips to multi-container TPU workloads. For more policy options, see [Topology Manager Policies](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/#topology-manager-policies).

  2. Apply the `kubelet` configuration to a node pool by creating a new node pool or updating an existing one. This node pool must use Ironwood (TPU7x) nodes, such as `tpu7x-standard-4t` machine type to match node selector in the next step.

     * To create a new node pool with Topology Manager enabled:
           
           gcloud container node-pools create NODE_POOL_NAME \
               --location=LOCATION \
               --cluster=CLUSTER_NAME \
               --node-locations=NODE_ZONES \
               --machine-type=tpu7x-standard-4t \
               --system-config-from-file=topology-manager-config.yaml
           

Replace the following:

       * `NODE_POOL_NAME`: the name of the new node pool.
       * `LOCATION`: the region of cluster.
       * `CLUSTER_NAME`: the name of the cluster.
       * `NODE_ZONES`: comma-separated list of one or more zones for the node pool.
     * To update an existing node pool with Topology Manager enabled:
           
           gcloud container node-pools update NODE_POOL_NAME \
               --location=LOCATION \
               --cluster=CLUSTER_NAME \
               --system-config-from-file=topology-manager-config.yaml
           

Replace the following:

       * `NODE_POOL_NAME`: the name of your node pool.
       * `LOCATION`: the region of cluster.
       * `CLUSTER_NAME`: the name of the cluster.
  3. Create a file named `tpu-jobset.yaml` with the following manifest:
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: tpu7x-test
         spec:
           failurePolicy:
             maxRestarts: 0
           replicatedJobs:
             - name: tpu7x
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       subdomain: test
                       restartPolicy: Never
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu7x
                         cloud.google.com/gke-tpu-topology: 2x2x2
                       containers:
                       - name: jax-tpu-1
                         image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                         securityContext:
                           privileged: false
                         command:
                         - bash
                         - -c
                         - |
                           set -ex
                           python -c 'import jax; print("local devices:", jax.local_device_count(), "devices:", jax.device_count())'
                         resources:
                           requests:
                             google.com/tpu: 2
                           limits:
                             google.com/tpu: 2
                       - name: jax-tpu-2
                         image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                         securityContext:
                           privileged: false
                         command:
                         - bash
                         - -c
                         - |
                           set -ex
         
                           python -c 'import jax; print("local devices:", jax.local_device_count(), "devices:", jax.device_count())'
                         resources:
                           requests:
                             google.com/tpu: 2
                           limits:
                             google.com/tpu: 2
         

This manifest defines a `JobSet` named `tpu7x-test`, which runs two main containers, `jax-tpu-1` and `jax-tpu-2`. Each container requests two `google.com/tpu` chips. These two chips come from the same NUMA node. Each container then runs a Python script to verify JAX's access to the TPUs.

This JobSet configuration shows that multiple containers within the same Pod can access and utilize separate TPU chips.

  4. Apply the manifest:
         
         kubectl apply -f tpu-jobset.yaml
         




### Example 5: Run a multi-container TPU workload with Multi-NIC Cloud Storage FUSE volumes

This example extends Example 4 to include mounting Cloud Storage FUSE buckets as volumes by using [Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver). This configuration leverages multi-NIC capabilities for potentially improved network performance.

**Important:** Multi-NIC Cloud Storage FUSE volumes require GKE cluster version 1.35.2-gke.1442000 or later.

  1. Create a file named `tpu7x-gcsfuse-multinic.yaml` with the following manifest:
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: tpu7x-gcsfuse-multinic
         spec:
           failurePolicy:
             maxRestarts: 0
           replicatedJobs:
             - name: tpu7x
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       subdomain: test
                       restartPolicy: Never
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu7x
                         cloud.google.com/gke-tpu-topology: 2x2x2
                       hostNetwork: true
                       volumes:
                       - name: gcs0
                         csi:
                           driver: gcsfuse.csi.storage.gke.io
                           volumeAttributes:
                             bucketName: BUCKET_NAME
                             multiNICIndex: "0"
                             mountOptions: implicit-dirs
                             hostNetworkPodKSA: "true"
                       - name: gcs1
                         csi:
                           driver: gcsfuse.csi.storage.gke.io
                           volumeAttributes:
                             bucketName: BUCKET_NAME
                             multiNICIndex: "1"
                             mountOptions: implicit-dirs
                             hostNetworkPodKSA: "true"
                       containers:
                       - name: jax-tpu-1
                         image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                         securityContext:
                           privileged: false
                         command:
                         - bash
                         - -c
                         - |
                           set -ex
                           python -c 'import jax; print("local devices:", jax.local_device_count(), "devices:", jax.device_count())'
                           echo "Use /gcs${WORKLOAD_NIC_PREFERRED_NUMA}/ for Cloud Storage access"
                         resources:
                           requests:
                             google.com/tpu: 2
                           limits:
                             google.com/tpu: 2
                         volumeMounts:
                         - name: gcs0
                           mountPath: /gcs0
                           readOnly: false
                         - name: gcs1
                           mountPath: /gcs1
                           readOnly: false
                       - name: jax-tpu-2
                         image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                         securityContext:
                           privileged: false
                         command:
                         - bash
                         - -c
                         - |
                           set -ex
         
                           python -c 'import jax; print("local devices:", jax.local_device_count(), "devices:", jax.device_count())'
                           echo "Use /gcs${WORKLOAD_NIC_PREFERRED_NUMA}/ for Cloud Storage access"
                         resources:
                           requests:
                             google.com/tpu: 2
                           limits:
                             google.com/tpu: 2
                         volumeMounts:
                         - name: gcs0
                           mountPath: /gcs0
                           readOnly: false
                         - name: gcs1
                           mountPath: /gcs1
                           readOnly: false
         

This manifest adds the following Cloud Storage FUSE volume mounts to Example 4.

     * `multiNICIndex` is specified in the volume attributes to use the network interface on the corresponding NUMA node for each volume.
     * The workload uses the `${WORKLOAD_NIC_PREFERRED_NUMA}` environment variable to select the Cloud Storage FUSE volume, which is associated with the NUMA node that the container is assigned to. GKE injects this variable into containers on Cloud TPU workloads.

Replace `BUCKET_NAME` with the name of your Cloud Storage bucket.

  2. Apply the manifest:
         
         kubectl apply -f tpu7x-gcsfuse-multinic.yaml
         




## Upgrade node pools using accelerators (GPUs and TPUs)

GKE [automatically upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically) Standard clusters, including node pools. You can also [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) node pools if you want your nodes on a later version sooner. To control how upgrades work for your cluster, use [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), and [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).

You can also configure a [node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) for your node pool, such as [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) , [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) or [short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start). By configuring these strategies, you can ensure that the node pools are upgraded in a way that achieves the optimal balance between speed and disruption for your environment. For [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host), instead of using the configured node upgrade strategy, GKE atomically recreates the entire node pool in a single step. To learn more, see the definition of _atomicity_ in [Terminology related to TPU in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology).

Using a node upgrade strategy temporarily requires GKE to provision additional resources, depending on the configuration. If Google Cloud has limited capacity for your node pool's resources—for example, you're seeing [resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) errors when trying to create more nodes with GPUs or TPUs—see [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this guide, consider deleting the TPU slice node pools that no longer have scheduled workloads. If the workloads running must be gracefully terminated, use [`kubectl drain`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain) to clean up the workloads before you delete the node.

### gcloud

Delete a TPU slice node pool:
    
    
      gcloud container node-pools delete POOL_NAME \
          --location=LOCATION \
          --cluster=CLUSTER_NAME
    

Replace the following:

  * `POOL_NAME`: the name of the node pool.
  * `LOCATION`: the compute location of the cluster.
  * `CLUSTER_NAME`: the name of the cluster.



###  Cluster Toolkit 

Delete the Cluster Toolkit deployment:
    
    
      gcluster destroy DEPLOYMENT_NAME
    

Replace `DEPLOYMENT_NAME` with the name of the deployment directory created when you deployed your blueprint.

## Configure additional settings

The following sections describe the additional configurations you can apply to your TPU workloads.

### Use Multislice

You can aggregate smaller slices together in a Multislice to handle larger training workloads. For more information, see [Multislice TPUs in GKE](https://docs.cloud.google.com/tpu/docs/tpu-gke-multislice).

### Migrate your TPU reservation

If you have existing TPU reservations, you must first migrate your TPU reservation to a new Compute Engine-based reservation system. You can also create Compute Engine-based reservation system where no migration is needed. To learn how to migrate your TPU reservations, see [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#tpu_reservation).

### Enable logging

Logs emitted by containers running on GKE nodes, including TPU VMs, are [collected](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-logs) by the GKE logging agent, sent to Logging, and are [visible in Logging](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs).

### Configure auto repair for TPU slice nodes

If a TPU slice node in a multi-host TPU slice node pool is unhealthy, the entire node pool is recreated. Whereas, In a single-host TPU slice node pool, only the unhealthy TPU node is auto-repaired.

Conditions that result in unhealthy TPU slice nodes include the following:

  * Any TPU slice node with common node [conditions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#repair_criteria).
  * Any TPU slice node with an unallocatable TPU count larger than zero.
  * Any VM instance in a TPU slice that is stopped (due to preemption) or is terminated.
  * Node maintenance: If any TPU slice node within a multi-host TPU slice node pool goes down for host maintenance, GKE recreates the entire TPU slice node pool.



You can see the repair status (including the failure reason) in the [operation history](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#node_repair_history). If the failure is caused by insufficient quota, contact your Google Cloud account representative to increase the corresponding quota.

### Configure graceful termination for TPU slice nodes

In GKE clusters with the control plane running 1.29.1-gke.1425000 or later, TPU slice nodes support `SIGTERM` signals that alert the node of an imminent shutdown. The imminent shutdown notification is configurable up to _five_ minutes in TPU nodes.

To configure GKE to terminate your workloads gracefully within this notification timeframe, follow the steps in [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

### Prevent scheduling deadlocks

When running multiple TPU Jobs or multiple replicas of a Job, Pods from different Jobs can schedule on the same TPU node pool. This can cause a scheduling deadlock where none of the Jobs can secure enough nodes to complete their topology.

To reduce the risk of scheduling deadlocks, apply one of the following configurations:

  * Use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) rules to ensure that Pods from different Jobs are not scheduled on the same TPU node pool or topology domain.
  * Use the `jobset.sigs.k8s.io/exclusive-topology` annotation, which causes the JobSet to claim the specified topology domain (like a node pool) exclusively for its own Pods.



For detailed configuration examples and troubleshooting steps, see [Scheduling deadlock](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus#scheduling_deadlock).

### Run containers without privileged mode

Containers running in nodes in GKE version 1.28 or later don't need to have privileged mode enabled to access TPUs. Nodes in GKE version 1.28 and earlier require privileged mode.

If your TPU slice node is running versions less than 1.28, read the following section:

A container running on a VM in a TPU slice needs access to higher limits on locked memory so the driver can communicate with the TPU chips over direct memory access (DMA). To enable this, you must configure a higher [`ulimit`](https://ss64.com/bash/ulimit.html). If you want to reduce the permission scope on your container, complete the following steps:

  1. Edit the `securityContext` to include the following fields:
         
         securityContext:
           capabilities:
             add: ["SYS_RESOURCE"]
         

  2. Increase `ulimit` by running the following command inside the container before your setting up your workloads to use TPU resources:
         
         ulimit -l 68719476736
         




For TPU v5e, running containers without privileged mode is available in clusters in version 1.27.4-gke.900 and later.

## Observability and metrics

### Dashboard

Node pool observability in the [Google Cloud console](http://console.cloud.google.com) is generally available. To view the status of your TPU multi-host node pools on GKE, go to **GKE TPU Node Pool Status** dashboard provided by Cloud Monitoring:

[Go to GKE TPU Node Pool Status](https://console.cloud.google.com/monitoring/dashboards/integration/gke.gke-tpu-node-pool-status)

This dashboard gives you comprehensive insights into the health of your multi-host TPU node pools. For more information, see Monitor health metrics for TPU nodes and node pools.

In the [**Kubernetes Clusters**](https://console.cloud.google.com/kubernetes/list) page in the Google Cloud console, the **Observability** tab also displays TPU observability metrics, such as TPU usage, under the **Accelerators > TPU** heading. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

The TPU dashboard is populated only if you have [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) enabled in your GKE cluster.

**Note:** If you created a GKE cluster with [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), use the Google Cloud console URLs provided in the deployment output to track cluster and workload metrics.

### Runtime metrics

In GKE version 1.27.4-gke.900 or later, TPU workloads that both use JAX version [0.4.14](https://github.com/google/jax/releases/tag/jaxlib-v0.4.14) or later and specify `containerPort: 8431` export TPU utilization metrics as GKE [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics). The following metrics are available in Cloud Monitoring to monitor your TPU workload's runtime performance:

  * **Duty cycle** : percentage of time over the past sampling period (60 seconds) during which the TensorCores were actively processing on a TPU chip. Larger percentage means better TPU utilization.
  * **Memory used** : amount of accelerator memory allocated in bytes. Sampled every 60 seconds.
  * **Memory total** : total accelerator memory in bytes. Sampled every 60 seconds.



These metrics are located in the Kubernetes node (`k8s_node`) and Kubernetes container (`k8s_container`) schema.

Kubernetes container:

  * `kubernetes.io/container/accelerator/duty_cycle`
  * `kubernetes.io/container/accelerator/memory_used`
  * `kubernetes.io/container/accelerator/memory_total`



Kubernetes node:

  * `kubernetes.io/node/accelerator/duty_cycle`
  * `kubernetes.io/node/accelerator/memory_used`
  * `kubernetes.io/node/accelerator/memory_total`



### Monitor health metrics for TPU nodes and node pools

When a training job has an error or terminates in failure, you can check metrics related to the underlying infrastructure to figure out if the interruption was caused by an issue with the underlying node or node pool.

#### Node status

In GKE version 1.32.1-gke.1357001 or later, the following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) exposes the condition of a GKE node:

  * `kubernetes.io/node/status_condition`



The `condition` field reports conditions on the node, such as `Ready`, `DiskPressure`, and `MemoryPressure`. The `status` field shows the reported status of the condition, which can be `True`, `False`, or `Unknown`. This is a metric with the `k8s_node` monitored resource type.

This PromQL query shows if a particular node is `Ready`:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        node_name="NODE_NAME",
        condition="Ready",
        status="True"}
    

To help troubleshoot issues in a cluster, you might want to look at nodes that have exhibited other conditions:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        condition!="Ready",
        status="True"}
    

You might want to specifically look at nodes that aren't `Ready`:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        condition="Ready",
        status="False"}
    

If there is no data, then the nodes are ready. The status condition is sampled every 60 seconds.

You can use the following query to understand the node status across the fleet:
    
    
    avg by (condition,status)(
      avg_over_time(
        kubernetes_io:node_status_condition{monitored_resource="k8s_node"}[${__interval}]))
    

#### Node pool status

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) for the `k8s_node_pool` monitored resource exposes the status of a GKE node pool:

  * `kubernetes.io/node_pool/status`



This metric is reported only for multi-host TPU node pools.

The `status` field reports the status of the node pool, such as `Provisioning`, `Running`, `Error`, `Reconciling`, or `Stopping`. Status updates happen after GKE API operations complete.

To verify if a particular node pool has `Running` status, use the following PromQL query:
    
    
    kubernetes_io:node_pool_status{
        monitored_resource="k8s_node_pool",
        cluster_name="CLUSTER_NAME",
        node_pool_name="NODE_POOL_NAME",
        status="Running"}
    

To monitor the number of node pools in your project grouped by their status, use the following PromQL query:
    
    
    count by (status)(
      count_over_time(
        kubernetes_io:node_pool_status{monitored_resource="k8s_node_pool"}[${__interval}]))
    

#### Node pool availability

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) shows whether a multi-host TPU node pool is available:

  * `kubernetes.io/node_pool/multi_host/available`



The metric has a value of `True` if all of the nodes in the node pool are available, and `False` otherwise. The metric is sampled every 60 seconds.

To check the availability of multi-host TPU node pools in your project, use the following PromQL query:
    
    
    avg by (node_pool_name)(
      avg_over_time(
        kubernetes_io:node_pool_multi_host_available{
          monitored_resource="k8s_node_pool",
          cluster_name="CLUSTER_NAME"}[${__interval}]))
    

#### Node interruption count

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) reports the count of interruptions for a GKE node since the last sample (the metric is sampled every 60 seconds):

  * `kubernetes.io/node/interruption_count`



The `interruption_type` (such as `TerminationEvent`, `MaintenanceEvent`, or `PreemptionEvent`) and `interruption_reason` (like `HostError`, `Eviction`, or `AutoRepair`) fields can help provide the reason for why a node was interrupted.

To get a breakdown of the interruptions and their causes in TPU nodes in the clusters in your project, use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node"}[${__interval}]))
    

To only see the [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents), update the query to filter the `HW/SW Maintenance` value for the `interruption_reason`. Use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node", interruption_reason="HW/SW Maintenance"}[${__interval}]))
    

To see the interruption count aggregated by node pool, use the following PromQL query:
    
    
      sum by (node_pool_name,interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_pool_interruption_count{monitored_resource="k8s_node_pool", interruption_reason="HW/SW Maintenance", node_pool_name=NODE_POOL_NAME }[${__interval}]))
    

#### Node pool times to recover (TTR)

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) reports the distribution of recovery period durations for GKE multi-host TPU node pools:

  * `kubernetes.io/node_pool/accelerator/times_to_recover`



Each sample recorded in this metric indicates a single recovery event for the node pool from a downtime period.

This metric is useful for tracking the multi-host TPU node pool time to recover and time between interruptions.

You can use the following PromQL query to calculate the mean time to recovery (MTTR) for the last 7 days in your cluster:
    
    
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_to_recover_sum{
        monitored_resource="k8s_node_pool", cluster_name="CLUSTER_NAME"}[7d]))
    /
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_to_recover_count{
        monitored_resource="k8s_node_pool",cluster_name="CLUSTER_NAME"}[7d]))
    

#### Node pool times between interruptions (TBI)

The following [GKE system metric](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) reports the distribution of times between the end of the most recent interruption and the beginning of the current interruption for GKE multi-host TPU node pools:

  * `kubernetes.io/node_pool/accelerator/times_between_interruptions`



Each sample recorded in this metric indicates a single duration between the most recent and current interruption.

Use the following PromQL query to calculate the mean time between interruptions (MTBI) in your cluster for the previous 7 days:
    
    
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_between_interruptions_sum{
        monitored_resource="k8s_node_pool", cluster_name="CLUSTER_NAME"}[7d]))
    /
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_between_interruptions_count{
        monitored_resource="k8s_node_pool",cluster_name="CLUSTER_NAME"}[7d]))
    

### Host metrics

In GKE version 1.28.1-gke.1066000 or later, VMs in a TPU slice export TPU utilization metrics as GKE [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics). The following metrics are available in Cloud Monitoring to monitor your TPU host's performance:

  * **TensorCore utilization** : current percentage of the TensorCore that is utilized. The TensorCore value equals the sum of the [matrix-multiply units (MXUs) plus the vector unit](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_chip). The TensorCore utilization value is the division of the TensorCore operations that were _performed_ over the past sample period (60 seconds) by the _supported_ number of TensorCore operations over the same period. Larger value means better utilization.
  * **Memory bandwidth utilization** : current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period (60s) by the maximum supported bandwidth over the same sample period.



These metrics are located in the Kubernetes node (`k8s_node`) and Kubernetes container (`k8s_container`) schema.

Kubernetes container:

  * `kubernetes.io/container/accelerator/tensorcore_utilization`
  * `kubernetes.io/container/accelerator/memory_bandwidth_utilization`



Kubernetes node:

  * `kubernetes.io/node/accelerator/tensorcore_utilization`
  * `kubernetes.io/node/accelerator/memory_bandwidth_utilization`



For more information, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) and [GKE system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics).

### Manage collection scheduling

In TPU Trillium, you can use collection scheduling to group TPU slice nodes. Grouping these TPU slice nodes makes it easier to adjust the number of replicas to meet the workload demand. Google Cloud controls software updates to ensure that sufficient slices within the collection are always available to serve traffic.

TPU Trillium supports collection scheduling for single-host and multi-host node pools that run inference workloads. The following describes how collection scheduling behavior depends on the type of TPU slice that you use:

  * **Multi-host TPU slice:** GKE groups multi-host TPU slices to form a collection. Each GKE node pool is a replica within this collection. To define a collection, create a multi-host TPU slice and assign a unique name to the collection. To add more TPU slices to the collection, create another multi-host TPU slice node pool with the same collection name and workload type.
  * **Single-host TPU slice:** GKE considers the entire single-host TPU slice node pool as a collection. To add more TPU slices to the collection, you can resize the single-host TPU slice node pool.



To manage a collection, perform any of these actions based on the type of node pool that you use.

#### Manage collection scheduling in multi-host TPU slice node pools

Use the following tasks to manage multi-host TPU slice node pools.

  * To check if a multi-host TPU slice pool is part of a collection, run the following command:
        
        gcloud container node-pools describe NODE_POOL_NAME \
            --location LOCATION \
            --cluster CLUSTER_NAME \
            --format="json" | jq -r \
            '"nodepool-group-name: \(.config.labels["cloud.google.com/gke-nodepool-group-name"] // "")\ngke-workload-type: \(.config.labels["cloud.google.com/gke-workload-type"] // "")"'
        

The output is similar to the following:
        
        nodepool-group-name: <code><var>NODE_POOL_COLLECTION_NAME</var></code>
        gke-workload-type: HIGH_AVAILABILITY
        

If multi-host TPU slice pool is part of a collection, the output has the following labels:

    * `cloud.google.com/gke-workload-type: HIGH_AVAILABILITY`
    * `cloud.google.com/gke-nodepool-group-name: <code><var>COLLECTION_NAME</var></code>`
  * To get the list of collections in the cluster, run the following command:
        
        #!/bin/bash
        
        # Replace with your cluster name, project, and location
        CLUSTER_NAME=CLUSTER_NAME
        PROJECT=PROJECT_ID
        LOCATION=LOCATION
        
        declare -A collection_names
        
        node_pools=$(gcloud container node-pools list --cluster "$CLUSTER_NAME" --project "$PROJECT" --location "$LOCATION" --format="value(name)")
        
        # Iterate over each node pool
        for pool in $node_pools; do
            # Describe the node pool and extract labels using jq
            collection_name=$(gcloud container node-pools describe "$pool" \
                --cluster "$CLUSTER_NAME" \
                --project "$PROJECT" \
                --location "$LOCATION" \
                --format="json" | jq -r '.config.labels["cloud.google.com/gke-nodepool-group-name"]')
        
            # Add the collection name to the associative array if it's not empty
            if [[ -n "$collection_name" ]]; then
                collection_names["$collection_name"]=1
            fi
        done
        
        # Print the unique node pool collection names
        echo "Unique cloud.google.com/gke-nodepool-group-name values:"
        for name in "${!collection_names[@]}"; do
            echo "$name"
        done
        

The output is similar to the following:
        
        Unique cloud.google.com/gke-nodepool-group-name values: {COLLECTION_NAME_1}, {COLLECTION_NAME_2}, {COLLECTION_NAME_3}
        

  * To get a list of node pools that belong to a collection, run the following command:
        
        #!/bin/bash
        
        TARGET_COLLECTION_NAME=COLLECTION_NAME
        CLUSTER_NAME=CLUSTER_NAME
        PROJECT=PROJECT_ID
        LOCATION=LOCATION
        
        matching_node_pools=()
        
        # Get the list of all node pools in the cluster
        node_pools=$(gcloud container node-pools list --cluster "$CLUSTER_NAME" --project "$PROJECT" --location "$LOCATION" --format="value(name)")
        
        # Iterate over each node pool
        for pool in $node_pools; do
            # Get the value of the cloud.google.com/gke-nodepool-group-name label
            collection_name=$(gcloud container node-pools describe "$pool" \
                --cluster "$CLUSTER_NAME" \
                --project "$PROJECT" \
                --location "$LOCATION" \
                --format="json" | jq -r '.config.labels["cloud.google.com/gke-nodepool-group-name"]')
        
            # Check if the group name matches the target value
            if [[ "$collection_name" == "$TARGET_COLLECTION_NAME" ]]; then
                matching_node_pools+=("$pool")
            fi
        done
        
        # Print the list of matching node pools
        echo "Node pools with collection name '$TARGET_COLLECTION_NAME':"
        for pool in "${matching_node_pools[@]}"; do
            echo "$pool"
        done
        

The output is similar to the following:
        
        Node pools with collection name 'COLLECTION_NAME':
        {NODE_POOL_NAME_1}
        {NODE_POOL_NAME_2}
        {NODE_POOL_NAME_3}
        

  * To scale up the collection, create another multi-host TPU slice node pool and add the `cloud.google.com/gke-workload-type` and `cloud.google.com/gke-nodepool-group-name`. Use the same collection name in `cloud.google.com/gke-nodepool-group-name` and run the same workload type. If node auto-provisioning is enabled on the cluster, GKE automatically creates pools based on workload demands.

  * To scale down the collection, [delete the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete).

  * To delete the collection, remove all of the attached node pools. You can [delete the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete) or [delete the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete). Deleting the cluster removes all of the collections in it.




#### Manage collection scheduling in single-host TPU slice node pools

Use the following tasks to manage single-host TPU slice node pools.

  * To check if a single-host TPU slice pool has collection scheduling enabled, run the following command:
        
        gcloud container node-pools describe NODE_POOL_NAME \
            --cluster CLUSTER_NAME \
            --project PROJECT_NAME \
            --location LOCATION \
            --format="json" | jq -r '.config.labels["cloud.google.com/gke-workload-type"]'
        

The output is similar to the following:
        
        gke-workload-type: HIGH_AVAILABILITY
        

If the single-host TPU slice pool is part of a collection, the output has the `cloud.google.com/gke-workload-type: HIGH_AVAILABILITY` label.

  * To scale up the collection, resize the node pool [manually](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--machine-type) or [automatically](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#tpu) with node auto-provisioning.

  * To scale down the collection, [delete the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete).

  * To delete the collection, remove all of the attached node pools. You can [delete the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/delete) or [delete the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete). Deleting the cluster removes all of the collections in it.




## Known issues

  * Cluster autoscaler might incorrectly calculate capacity for new TPU slice nodes before those nodes report available TPUs. Cluster autoscaler might then perform additional scale up and as a result create more nodes than needed. Cluster autoscaler scales down additional nodes, if they are not needed, after regular scale down operation.
  * Cluster autoscaler cancels scaling up of TPU slice node pools that remain in waiting status for more than 10 hours. Cluster Autoscaler retries such scale up operations later. This behavior might reduce TPU availability for customers who don't use reservations.
  * Non-TPU workloads that have a toleration for the TPU taint can prevent scale down of the node pool if they are being recreated during draining of the TPU slice node pool.
  * Memory bandwidth utilization metric is not available for v5e TPUs.



## What's next

  * [Learn more about setting up Ray on GKE with TPUs](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/ray-on-gke/guides/tpu#tpu-user-guide)
  * [Build large-scale machine learning on Cloud TPUs with GKE](https://www.youtube.com/watch?v=wtKhG1aTgtY)
  * [Serve Large Language Models with KubeRay on TPUs](https://www.youtube.com/watch?v=RK_u6cfPnnw)
  * [Troubleshoot TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshoot-tpus)
  * [Learn about sandboxing TPU workloads with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
