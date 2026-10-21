---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4-cluster/
title: Create an A4 GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:44.987487+00:00
---

# Create an A4 GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create an A4 GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy an A4 GKE cluster. These clusters provide high-performance network topologies that let you efficiently run large-scale artificial intelligence (AI) and machine learning (ML) training workloads.

A4 accelerator-optimized machine types have NVIDIA B200 Blackwell GPUs attached and are ideal for foundation model training and serving.

To learn more about the A4 accelerator-optimized machine types, see the [A4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-machine-type) section in the Compute Engine documentation.

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

For GKE, consider the following additional information when choosing a consumption option:

     * For more information about flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)) and GKE, see [About GPU obtainability with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
     * Flex-start uses best-effort compact placement. To examine your topology, see [View the physical topology of nodes in your GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas#view-physical-topology).
     * You can only get topology information when using Spot VMs if you configure [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).
  2. **Obtain capacity:** The process to obtain capacity differs for each consumption option. To learn about the process for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).




### Requirements

The following requirements apply to an AI-optimized GKE cluster that uses A4 instances:

  * **GPU drivers** : The B200 GPUs in A4 instances require a minimum of the R570 GPU driver version. GKE automatically installs this driver version by default on all A4 nodes that run the required minimum version for A4 (1.32.1-gke.1729000 or later).
  * **GPUDirect RDMA** : To use GPUDirect RDMA with A4, use GKE version 1.32.2-gke.1475000 or later.
  * **Node images** : To use GPUDirect RDMA, the GKE nodes must use a Container-Optimized OS node image. Ubuntu and Windows node images are not supported.



## Create an A4 GKE cluster

To create an A4 GKE cluster, do the following:

**Note:** If you create multiple clusters by using these same cluster blueprints, then verify that all VPC network and subnet names are unique per project to prevent errors.

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend that you use Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment. 
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
  3. In the [`examples/gke-a4/gke-a4-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4-deployment.yaml) blueprint from the GitHub repository, fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment: 

Replace the following variables:

     * `BUCKET`: the name of the Cloud Storage bucket that you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4`.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A4 machines. This zone should match the zone where machines are available in your reservation.
     * `STATIC_NODE_COUNT`: the number of A4 nodes in your cluster's node pool, 
     * `AUTHORIZED_CIDR`: the IP address range that you want to let connect to the cluster. This CIDR block must include the IP address of the machine that calls Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when you provision the node pool: 
       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format: 
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
                         

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology). 

To modify advanced settings, edit the [`examples/gke-a4/gke-a4.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4.yaml) file.

  4. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, use the `gcloud auth application-default login` command: 
         
         gcloud auth application-default login
             

  5. Deploy the blueprint by using the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to provision the GKE infrastructure with A4 machine types: 
         
         cd ~/cluster-toolkit
             ./gcluster deploy -d \
                 examples/gke-a4/gke-a4-deployment.yaml \
                 examples/gke-a4/gke-a4.yaml
             

**Note:** If you encounter an error at Jobset or Kueue installation when you deploy your blueprint, then deploy the blueprint again with the addition of the `-w` flag (`./gcluster deploy -w -d ...`) to complete the deployment.
  6. When prompted, select **(A)pply** to deploy the blueprint. 
     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volume resources are created.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
