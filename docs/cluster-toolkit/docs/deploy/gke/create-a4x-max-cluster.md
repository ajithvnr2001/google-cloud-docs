---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster/
title: Create an A4X Max GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:10.186650+00:00
---

# Create an A4X Max GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create an A4X Max GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to deploy a Google Kubernetes Engine (GKE) cluster that uses A4X Max instances. This setup is ideal for running workloads for machine learning (ML) training and high performance computing (HPC).

The A4X Max machine series runs on an exascale platform based on NVIDIA's rack-scale architecture and is optimized for compute and memory-intensive, network-bound ML training and HPC workloads. A4X Max offers bare metal instances, which provide direct access to the host server's CPU and memory, without the Compute Engine hypervisor layer.

To learn more about the A4X machine series, see the [A4X Max and A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) section in the Compute Engine documentation.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to deploy the cluster, ask your administrator to grant you the following IAM roles: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) on the project
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the project
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on the project
  * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 
  * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Choose a consumption option and obtain capacity

To obtain capacity, complete the following steps:

  1. **Choose a consumption option:** Make your choice based on how you want to get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

For GKE, consider the following additional information:

     * A4X Max compute instances cannot be provisioned by using flex-start.
     * You must use the [reservation-bound](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound) provisioning model to create clusters with A4X Max. Other provisioning models are not supported.
  2. **Obtain capacity:** The process to obtain capacity differs for each consumption option. To learn about the process for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).

**Note:** When you request A4X Max capacity, you obtain it in _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max machine types. For more information about all capacity mode, see [Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).



### Requirements

The following requirements apply to an AI-optimized GKE cluster that uses A4X Max instances:

  * Verify that you use GKE version 1.35.0-gke.2745000 or later (for 1.35), or version 1.34.3-gke.1318000 or later (for 1.34). These versions help ensure that A4X Max uses the following:

    * R580.95.05, which is the minimum GPU driver version for the GB300 GPUs in A4X Max bare metal instances. This driver is turned on by default.
    * Coherent Driver-based Memory Management (CDMM), which is turned on by default. NVIDIA recommends that Kubernetes clusters turn on this mode to resolve memory over-reporting. CDMM lets you manage GPU memory through the driver instead of the operating system (OS). This approach helps you avoid OS onlining of GPU memory, and exposes the GPU memory as a Non-Uniform Memory Access (NUMA) node to the OS. Multi-instance GPUs are not supported when CDMM is turned on. For more information about CDMM, see [Hardware and Software Support](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-65-06/index.html#hardware-software-support).
    * GPUDirect RDMA, which is recommended to let A4X Max node pools use the networking capabilities of A4X Max.
  * To use GPUDirect RDMA, the GKE nodes must use a Container-Optimized OS node image. Ubuntu and Windows node images are not supported.




## Create an A4X Max GKE cluster

To create an A4X Max GKE cluster, follow these steps:

**Note:** If you create multiple clusters by using these same cluster blueprints, help ensure that all VPC network and subnet names are unique per project to prevent errors.

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). Although it's possible to use a different environment, we recommend that you use Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, then follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment. 
  2. Create a Cloud Storage bucket to store the state of the Terraform deployment: 
         
         gcloud storage buckets create gs://BUCKET_NAME \
                 --default-storage-class=STANDARD \
                 --project=PROJECT_ID \
                 --location=COMPUTE_REGION_TERRAFORM_STATE \
                 --uniform-bucket-level-access
             gcloud storage buckets update gs://BUCKET_NAME --versioning
             

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  3. Choose a consumption option for your GKE deployment:

By default, the deployment file is configured to consume [specific reservations](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#reservations). To use an alternative consumption model , update your deployment YAML file. For more information, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).

  4. In the [`examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml) deployment file from the GitHub repository, fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket that you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, then cluster creation fails. The default value is `gke-a4x-max-bm`.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A4X Max machines. This zone must match the zone where machines are available in your reservation.
     * `AUTHORIZED_CIDR`: the IP address range that you want to let connect to the cluster. This CIDR block must include the IP address of the machine that calls Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * `STATIC_NODE_COUNT`: the number of A4X Max nodes in your cluster's node pool, which must be 18 nodes or less. We recommend that you use 18 nodes to obtain the GPU topology of `1x72` in one subblock by using an NVLink domain.
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when you provision the node pool: 
       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format: 
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME

If you don't know which blocks are available in your reservation, then see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology). 
     * `RESERVATION_PROJECT_ID`: the Google Cloud project ID that has the reservation. Your reservation might exist in a different project from `PROJECT_ID`.
     * `NUM_NODE_POOLS`: the number of node pools to enable in your cluster. If you want a cluster larger than 18 nodes, then you can specify multiple node pools. The default value is `1`.

To modify advanced settings, edit the [`examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml) file.

  5. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, use the `gcloud auth application-default login` command: 
         
         gcloud auth application-default login
             

  6. Deploy the blueprint by using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to provision the GKE infrastructure with A4X Max machine types: 
         
         cd ~/cluster-toolkit
             ./gcluster deploy -d \
                 examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml \
                 examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml
             

**Note:** If you encounter an error at the JobSet or Kueue installation stage when you deploy your blueprint, then deploy the blueprint again with the addition of the `-w` flag (`./gcluster deploy -w -d ...`) to complete the deployment.
  7. When prompted, select **(A)pply** to deploy the blueprint. 
     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` Job template in the blueprint, Google Cloud buckets, network storage, and persistent volume resources are created.



## Test network performance

We recommend that you validate the functionality of provisioned clusters. To do so, use [NCCL/gIB tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

## Clean up resources

To avoid recurring charges for the resources that you used on this page, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to clean up the resources that are provisioned by Cluster Toolkit, including the VPC networks and the GKE cluster:
    
    
    cd ~/cluster-toolkit
    ./gcluster destroy CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your cluster.

## What's next

  * To learn about scheduling workloads on your GKE clusters by using TAS and Kueue, see [Schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).
  * To learn about managing common events that are relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).
  * For information about testing your environment for proper setup and optimization, see [Cluster networking optimization overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
