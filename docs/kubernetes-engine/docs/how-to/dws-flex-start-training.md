---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training/
title: Run a small batch workload with GPUs and Flex-start VMs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:26.347568+00:00
---

# Run a small batch workload with GPUs and Flex-start VMs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dws-flex-start-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Run a small batch workload with GPUs and Flex-start VMs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — flex-start**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to optimize GPU provisioning for medium- and small-scale training workloads by using Flex-start VMs. Flex-start VMs are created by using the [flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) consumption option. In this guide, you use Flex-start VMs to deploy a workload that consists of two Kubernetes Jobs. Each Job requires one GPU. GKE automatically provisions a _single node_ with two A100 GPUs to run _both Jobs_. 

If your workload requires multi-node distributed processing, consider using _flex-start with queued provisioning_. For more information, see [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).

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
  * Verify that you have quota for [preemptible GPUs](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas) in your node locations.



If you don't have a cluster or your cluster doesn't meet the requirements, you can create a [Standard regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) using the gcloud CLI. Add the following flags so that you can learn about flex-start:
    
    
    --location=us-central1 \
    --node-locations=us-central1-a,us-central1-b \
    --machine-type=g2-standard-8
    

When you create a flex-start node pool, use the previously mentioned flags and `--accelerator type=nvidia-l4,count=1`.

If you have a Standard cluster that meets the requirements, the next sections guide you through selecting a GPU accelerator type and machine type for your cluster.

### Choose a GPU accelerator type

If you use a cluster in Autopilot mode, skip this section and go to the Run a batch workload section.

GPU availability is specific to each zone. You need to find a [GPU accelerator type](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) that is available in a zone that the Standard cluster is in. If you have a regional Standard cluster, the zone in which the GPU accelerator type is available must be in the region that the cluster is in. When you create the node pool, you specify the accelerator type and the zones for the nodes. If you specify an accelerator type that isn't available in the cluster's location, the node pool creation fails.

Run the following commands to get your cluster's location and a supported GPU accelerator type.

  1. Get the location that the cluster is in:
         
         gcloud container clusters list
         

The output is similar to the following:
         
         NAME                LOCATION  MASTER_VERSION      MASTER_IP     MACHINE_TYPE  NODE_VERSION        NUM_NODES  STATUS   STACK_TYPE
         example-cluster-1   us-west2  1.33.2-gke.1111000  34.102.3.122  e2-medium     1.33.2-gke.1111000  9          RUNNING  IPV4
         

  2. List the available GPU accelerator types, excluding Virtual Workstations in the location:
         
         gcloud compute accelerator-types list | grep CONTROL_PLANE_LOCATION | grep -v "Workstation"
         

Replace `CONTROL_PLANE_LOCATION` with the cluster's location.

For example, to get a list of GPU accelerator types in the `us-west2` region, run the following command:
         
         gcloud compute accelerator-types list | grep us-west2 | grep -v "Workstation"
         

The output is similar to the following:
         
         nvidia-b200            us-west2-c                 NVIDIA B200 180GB
         nvidia-tesla-p4        us-west2-c                 NVIDIA Tesla P4
         nvidia-tesla-t4        us-west2-c                 NVIDIA T4
         nvidia-tesla-p4        us-west2-b                 NVIDIA Tesla P4
         nvidia-tesla-t4        us-west2-b                 NVIDIA T4
         




### Choose a compatible machine type

If you use a cluster in Autopilot mode, skip this section and go to the Run a batch workload section.

After you know which GPUs are available in the cluster's location, you can determine the compatible machine types. Google Cloud restricts GPUs to specific machine series. Use the following steps to find a machine type:

  1. Refer to the [GPU models available](https://docs.cloud.google.com/compute/docs/gpus#gpu-models) table.
  2. Locate the row for the GPU accelerator type you have chosen.
  3. Look at the "Machine series" column for that row. This column tells you which machine series you must use.
  4. To see the machine type names you can specify, click the link on the machine series.



The only exception is the [N1 machine series](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus), which provides additional guidance on which N1 machine types you can use with your chosen accelerator type.

Before using an accelerator-optimized machine, make sure that it's supported with flex-start provisioning mode, as shown in [Consumption option availability by machine type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws#consumption_option_availability_by_machine_type).

### Determine the accelerator count

If you use a cluster in Autopilot mode, skip this section and go to the Run a batch workload section.

To create a node pool, you need to determine the number of accelerators to attach to each node in the node pool. Valid values depend on your accelerator type and machine type. Each machine type has a limit on how many GPUs it can support. To determine what value to use (besides the default of `1`):

  1. Refer to [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).
  2. In the table, search for your accelerator type for your machine series type.
  3. Use the value in the "GPU count" column.



## Create a node pool with flex-start (Standard only)

If you use an Autopilot cluster, skip this section; you don't need to manually create node pools. When you deploy your Job or Pod manifest in the Run a batch workload section, GKE Autopilot automatically provisions the required Flex-start VMs based on your `nodeSelector`.

To create a node pool with flex-start enabled on an existing Standard cluster, you can use the gcloud CLI or Terraform. 

### gcloud

  1. Create a node pool with flex-start:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location CONTROL_PLANE_LOCATION \
             --project PROJECT_ID \
             --accelerator type=ACCELERATOR_TYPE,count=COUNT \
             --machine-type MACHINE_TYPE \
             --max-run-duration MAX_RUN_DURATION \
             **--flex-start** \
             --node-locations NODE_ZONES \
             --num-nodes 0 \
             --enable-autoscaling \
             --total-min-nodes 0 \
             --total-max-nodes 5 \
             --location-policy ANY \
             --no-enable-autorepair \
             --consolidation-delay=CONSOLIDATION_DELAY
         

Replace the following:

     * `NODE_POOL_NAME`: the name you choose for your node pool.
     * `CLUSTER_NAME`: the name of the Standard cluster you want to modify.
     * `CONTROL_PLANE_LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster control plane.
     * `PROJECT_ID`: your project ID.
     * `ACCELERATOR_TYPE`: the specific type of accelerator (for example, `nvidia-tesla-t4` for NVIDIA T4) to attach to the instances.
     * `COUNT`: the number of accelerators to attach to the instances. The default value is `1`.
     * `MACHINE_TYPE`: the type of machine to use for nodes.
     * `MAX_RUN_DURATION`: optional. The maximum runtime of a node in seconds, up to the default of seven days. The number that you enter must end in `s`. For example, to specify one day, enter `86400s`.
     * `CONSOLIDATION_DELAY`: optional. The duration that Cluster Autoscaler waits before it can scale down underutilized nodes. Use this setting to delay scale-down and keep the node pool for later reuse by other Pods. The number that you enter must end in `s`. For example, to specify one hour, enter `3600s`. Available in GKE version `1.34.1-gke.2364000` and later.
     * `NODE_ZONES`: a comma-separated list of one or more zones where GKE creates the node pool.

In this command, the `--flex-start` flag instructs `gcloud` to create a node pool with Flex-start VMs.

GKE creates a node pool with nodes that contain two instances of the specified accelerator type. The node pool initially has zero nodes and autoscaling is enabled




### Terraform

You can use flex-start with GPUs by using a [Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine).

  1. Add the following block to your Terraform configuration:


    
    
    resource "google_container_node_pool" "gpu_dws_pool" {
    name = "gpu-dws-pool"
    
    queued_provisioning {
        enabled = false
    }
    
    }
    node_config {
        machine_type = "MACHINE_TYPE"
        accelerator_type = "ACCELERATOR_TYPE"
        accelerator_count = COUNT
        node_locations = ["NODE_ZONES"]
        flex_start = true
    }
    

Replace the following:

  * `MACHINE_TYPE`: the type of machine to use for nodes.
  * `ACCELERATOR_TYPE`: the specific type of accelerator (for example, `nvidia-tesla-t4` for NVIDIA T4) to attach to the instances.
  * `COUNT`: the number of accelerators to attach to the instances. The default value is `1`.
  * `NODE_ZONES`: the comma-separated list of one or more zones where GKE creates the node pool.



Terraform calls Google Cloud APIs to create a cluster with a node pool that uses Flex-start VMs with GPUs. The node pool initially has zero nodes and autoscaling is enabled. To learn more about Terraform, see the [`google_container_node_pool` resource spec on terraform.io](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster).

### Verify the status of flex-start in the node pool

Run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --format="get(config.flexStart)"
    

If flex-start is enabled in the node pool, the field `flexStart` is set to `True`.

## Run a batch workload

In this section, you create two Kubernetes Jobs that require one GPU each. A Job controller in Kubernetes creates one or more Pods and helps ensure that they successfully execute a specific task. 

  1. In the [Google Cloud console](http://console.cloud.google.com), launch a Cloud Shell session by clicking ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**. A session opens in the bottom pane of the Google Cloud console.

  2. Create a file named `dws-flex-start.yaml`:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: job-1
         spec:
           template:
             spec:
               nodeSelector:
                 cloud.google.com/gke-flex-start: "true"
                 cloud.google.com/gke-accelerator: ACCELERATOR_TYPE
               containers:
               - name: container-1
                 image: gcr.io/k8s-staging-perf-tests/sleep:latest
                 args: ["10s"] # Sleep for 10 seconds
                 resources:
                   requests:
                       nvidia.com/gpu: 1
                   limits:
                       nvidia.com/gpu: 1
               restartPolicy: OnFailure
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: job-2
         spec:
           template:
             spec:
               nodeSelector:
                 cloud.google.com/gke-flex-start: "true"
                 cloud.google.com/gke-accelerator: ACCELERATOR_TYPE
               containers:
               - name: container-2
                 image: gcr.io/k8s-staging-perf-tests/sleep:latest
                 args: ["10s"] # Sleep for 10 seconds
                 resources:
                   requests:
                       nvidia.com/gpu: 1
                   limits:
                       nvidia.com/gpu: 1
               restartPolicy: OnFailure
         

  3. Apply the `dws-flex-start.yaml` manifest:
         
         kubectl apply -f dws-flex-start.yaml
         

  4. Verify that the Jobs are running on the same node:
         
         kubectl get pods -l "job-name in (job-1,job-2)" -o wide
         

The output is similar to the following:
         
         NAME    READY   STATUS      RESTARTS   AGE   IP       NODE               NOMINATED NODE   READINESS GATES
         job-1   0/1     Completed   0          19m   10.(...) **gke-flex-zonal-a2**  <none>           <none>
         job-2   0/1     Completed   0          19m   10.(...) **gke-flex-zonal-a2**  <none>           <none>
         


**Success:** You have successfully deployed two Jobs on the _same_ node by using Flex-start VMs. GKE deployed two Jobs on a newly provisioned Flex-start VM.

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

  * Learn more about [GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Learn more about [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).
  * Learn more about [Best practices for running batch workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
