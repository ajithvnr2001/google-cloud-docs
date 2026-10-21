---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu/
title: Run a small batch workload with TPUs and Flex-start VMs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:22.813422+00:00
---

# Run a small batch workload with TPUs and Flex-start VMs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Run a small batch workload with TPUs and Flex-start VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — flex-start**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to optimize TPU provisioning for medium- and small-scale training workloads by using Flex-start VMs. Flex-start VMs are created by using the [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. In this guide, you use Flex-start VMs to deploy a workload that consists of a TPU slice node pool. 

This guide is intended for Machine learning (ML) engineers, Platform admins and operators, and for Data and AI specialists who are interested in using Kubernetes container orchestration capabilities for running batch workloads. For more information about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

## Flex-start pricing

Flex-start is recommended if your workload requires dynamically provisioned resources as needed, for up to seven days with short-term reservations, no complex quota management, and cost-effective access. Flex-start is powered by Dynamic Workload Scheduler and is billed using [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing):

  * Can receive a discount (up to 53%) for vCPUs, GPUs, TPUs, and any attached Local SSD disks.
  * You pay as you go (PAYG).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have an [Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) or a [Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) that's running version 1.33.0-gke.1712000 or later.
  * Verify that you're familiar with [limitations of flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws#limitations).
  * When using a Standard cluster, verify that you maintain at least one node pool without flex-start enabled for the cluster to function correctly.
  * Verify that you have quota for [preemptible TPUs](https://docs.cloud.google.com/tpu/docs/quota#preemptible-quotas) in your node locations.



## Create a node pool with flex-start (Standard only)

If you use an Autopilot cluster, skip this section; you don't need to manually create node pools. When you deploy your Job or Pod manifest in the Run a batch workload section, GKE Autopilot automatically provisions the required Flex-start VMs based on your `nodeSelector`.

To create a node pool with flex-start enabled on an existing Standard cluster, use the gcloud CLI. 

### Create a single-host TPU slice node pool

You can create a single-host TPU slice node pool with flex-start:

  1. Create a node pool with flex-start:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --node-locations=NODE_ZONES \
             --machine-type=MACHINE_TYPE \
             --enable-autoscaling \
             **--flex-start** \
             --num-nodes 0 \
             --min-nodes=0 \
             --max-nodes=1 \
             --consolidation-delay=CONSOLIDATION_DELAY
         

Replace the following:

     * `NODE_POOL_NAME`: the name you choose for your node pool.
     * `CLUSTER_NAME`: the name of the cluster.
     * `CONTROL_PLANE_LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster control plane.
     * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool.
     * `CONSOLIDATION_DELAY`: optional. The duration that Cluster Autoscaler waits before it can scale down underutilized nodes. Use this setting to delay scale-down and keep the node pool for later reuse by other Pods. The number that you enter must end in `s`. For example, to specify one hour, enter `3600s`. Available in GKE version `1.34.1-gke.2364000` and later.
     * `MACHINE_TYPE`: the type of machine to use for nodes. For more information about TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).

For example, your node pool creation command can include the following parameters:
           
           ...
           --machine-type=ct6e-standard-4t \
           --tpu-topology=4x4 \
           --enable-autoscaling \
           --num-nodes=0 \
           --max-nodes=4 \
           

This command sets the `--max-nodes` field to `4` because a `4x4` topology consists of 16 chips and each `ct6e-standard-4t` VM has 4 chips.

Cluster autoscaler scales up to the number of nodes that your workload requires. After your workload completes, cluster autoscaler scales down to zero nodes.




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
             --enable-autoscaling \
             --num-nodes=0 --min-nodes=0 --max-nodes=MAX_NODES \
             --flex-start \
             --placement-policy=WORKLOAD_POLICY \
             --consolidation-delay=CONSOLIDATION_DELAY
         

Replace the following:

     * `NODE_POOL_NAME`: the name of the new node pool.
     * `WORKLOAD_POLICY`: the name of the workload policy that you created. 
     * `MAX_NODES`: The maximum size of the node pool. The `--max-nodes` flag is required if `--enable-autoscaling` is supplied and must be equal to the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM. For example, if `TPU_TOPOLOGY` is `2x2x2`, the product is 8. Since each VM in `tpu7x-standard-4t` has 4 chips, the number of nodes is 2.
     * `CONSOLIDATION_DELAY`: optional. The duration that Cluster Autoscaler waits before it can scale down underutilized nodes. Use this setting to delay scale-down and keep the node pool for later reuse by other Pods. The number that you enter must end in `s`. For example, to specify one hour, enter `3600s`. Available in GKE version `1.34.1-gke.2364000` and later. 

This command creates a node pool named NODE_POOL_NAME with the following characteristics:

     * `--machine-type=tpu7x-standard-4t` specifies the Ironwood (TPU7x) machine type. 
     * `--flex-start` enables flex-start.



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
             
             flex_start = true
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
          --enable-autoscaling \
          --num-nodes=0 --min-nodes=0 --max-nodes=MAX_NODES \
          --flex-start \
          --consolidation-delay=CONSOLIDATION_DELAY
          
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the name of the zone based on the TPU version you want to use. To identify an available location, see [TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool. 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  * `MACHINE_TYPE`: the type of machine to use for nodes. For more information about TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `TPU_TOPOLOGY`: the TPU topology. For example, `2x2x2`. To see all supported TPU topologies, see the [topology section](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology). 
  * `MAX_NODES`: the maximum size of the node pool. The `--max-nodes` flag is required if `--enable-autoscaling` is supplied and must be equal to the product of the values defined in `TPU_TOPOLOGY` (`{A}x{B}x{C}`) divided by the number of chips in each VM. 
  * `CONSOLIDATION_DELAY`: optional. The duration that Cluster Autoscaler waits before it can scale down underutilized nodes. Use this setting to delay scale-down and keep the node pool for later reuse by other Pods. The number that you enter must end in `s`. For example, to specify one hour, enter `3600s`. Available in GKE version `1.34.1-gke.2364000` and later.

This command creates a node pool named NODE_POOL_NAME with flex-start enabled.




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
             
             flex_start = true
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




### Verify the status of flex-start in the node pool

Run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --format="get(config.flexStart)"
    

If flex-start is enabled in the node pool, the field `flexStart` is set to `True`.

## Run a batch workload

In this section, you create a Job that schedules a TPU node with Flex-start VMs. A Job controller in Kubernetes creates one or more Pods and helps ensure that they successfully execute a specific task. 

  1. In the [Google Cloud console](http://console.cloud.google.com), launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**. A session opens in the bottom pane of the Google Cloud console.

  2. Create a file named `dws-flex-start.yaml`:

### Single-host

Use the following manifest for the `dws-flex-start.yaml` file:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: job-1
         spec:
           template:
             spec:
               nodeSelector:
                 cloud.google.com/gke-flex-start: "true"
                 cloud.google.com/gke-tpu-accelerator: ACCELERATOR_TYPE
                 cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
               containers:
               - name: container-1
                 image: gcr.io/k8s-staging-perf-tests/sleep:latest
                 args: ["3600s"] # Sleep for 1 hour
                 resources:
                   requests:
                       google.com/tpu: NUM_CHIPS
                   limits:
                       google.com/tpu: NUM_CHIPS
               restartPolicy: OnFailure
         

### Multi-host

Use the following manifest for the `dws-flex-start.yaml` file:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: job-1
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: job-1
         spec:
           backoffLimit: 0
           completions: 2
           parallelism: 2
           completionMode: Indexed
           template:
             spec:
               subdomain: headless-svc
               restartPolicy: Never
               nodeSelector:
                   cloud.google.com/gke-flex-start: "true"
                   cloud.google.com/gke-tpu-accelerator: ACCELERATOR_TYPE
                   cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 securityContext:
                   privileged: true
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())'
                 resources:
                   requests:
                     google.com/tpu: NUM_CHIPS
                   limits:
                     google.com/tpu: NUM_CHIPS
         

Replace the following:

     * `ACCELERATOR_TYPE`: the type of [TPU accelerator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version) you used when you created the node pools. For example, `tpu-v4-podslice` or `tpu-v5-lite-podslice`.
     * `TPU_TOPOLOGY`: the [physical topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) for the TPU slice. For example, the value might be `4x4x4` or `2x2`, depending on the TPU version.
     * `NUM_CHIPS`: the number of TPU chips in each VM is one, four, or eight. To learn more, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  3. Apply the `dws-flex-start.yaml` manifest:
         
         kubectl apply -f dws-flex-start.yaml
         

  4. Verify that the Jobs are running on the same node:
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME    READY   STATUS      RESTARTS   AGE   IP       NODE               NOMINATED NODE   READINESS GATES
         job-1   0/1     Completed   0          19m   10.(...) **gke-flex-zonal-a2**  <none>           <none>
         

**Success:** You have successfully deployed a batch workload by using Flex-start VMs.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources that you used on this page, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resource

  1. Delete the Jobs:
         
         kubectl delete job -l "job-name in (job-1,job-2)"
         

  2. Delete the node pool:
         
         gcloud container node-pools delete NODE_POOL_NAME \
               --location CONTROL_PLANE_LOCATION
         

  3. Delete the cluster:
         
         gcloud container clusters delete CLUSTER_NAME
         




## What's next

  * Learn more about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn more about [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * Learn how to [provision Managed Lustre on GKE using Cluster Toolkit](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ct-lustre-tpu).
  * Learn more about [best practices for running batch workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
