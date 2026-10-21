---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-high-cluster/
title: Create an A3 High GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:45.265629+00:00
---

# Create an A3 High GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a3-high-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create an A3 High GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy an A3 High (`a3-highgpu-8g`) Google Kubernetes Engine (GKE) cluster with Cluster Toolkit.

A3 High machine types feature NVIDIA H100 80GB GPUs, high-performance networking, and are designed for large-scale AI and ML workloads.

To learn more about the A3 High accelerator-optimized machine type, see the [A3 High machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) section in the Compute Engine documentation.

## Before you begin

  1. Before you start, make sure that you have performed the following tasks: 

     * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
     * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.
  2. To identify the regions and zones where the `a3-highgpu-8g` machine type is available, use the [gcloud compute machine-types list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list) command:
         
         gcloud compute machine-types list --filter="name=a3-highgpu-8g"
         

  3. Verify that you have enough GPU quotas. Each `a3-highgpu-8g` machine has 8 H100 80GB GPUs attached, so you need at least 8 NVIDIA H100 80GB GPUs in your selected region.

     1. To view quotas, see [View the quotas for your project](https://docs.cloud.google.com/docs/quotas/view-manage). In the filter_list **Filter** field, select **Dimensions (e.g. location)** and specify [`gpu_family:NVIDIA_H100_80GB`](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
     2. If you don't have enough quota, [request a higher quota](https://docs.cloud.google.com/view-manage#requesting_higher_quota).
  4. Verify that you have enough Filestore quota. You need a minimum of 2560 GiB of Basic SSD capacity. If you don't have enough quota, [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).




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

## Create an A3 High GKE cluster

To deploy the cluster, you must complete the following:

  1. Install Cluster Toolkit.
  2. Create a reservation.
  3. Create a cluster.
  4. Clean up resources created by Cluster Toolkit.



### Install Cluster Toolkit

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

If you are using Cloud Shell, then follow the instructions in [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).

If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, then follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

### Create a reservation

Reservations help ensure that you have the available resources to create A3 High instances with the specified hardware (memory, vCPUs, and GPUs) and attached Local SSD disks whenever you need them. To review the different methods to reserve resources for creating compute instances, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type). 

For example, to create an on-demand, specifically targeted reservation for A3 High instances, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--require-specific-reservation` flag: 
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --require-specific-reservation \
        --project=PROJECT_ID \
        --machine-type=a3-highgpu-8g \
        --vm-count=NUMBER_OF_INSTANCES \
        --zone=ZONE
    

Replace the following variables:

  * `RESERVATION_NAME`: the name of the single-project reservation that you want to use.
  * `PROJECT_ID`: the ID of your project.
  * `NUMBER_OF_INSTANCES`: the number of compute instances needed for the cluster.
  * `ZONE`: a zone that has `a3-highgpu-8g` machine types. To review the zones where you can create A3 High instances, see [Accelerator availability](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table).



After you destroy your cluster, you can delete the reservation if you don't need it anymore. For information, see [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete). 

### Create an A3 High GKE cluster

If you create multiple clusters by using the Cluster Toolkit example blueprints, then verify that all VPC and subnet names are unique per project to prevent errors. To create the cluster, you do the following:

  1. After you have installed the Cluster Toolkit, verify that you are in the Cluster Toolkit directory. To go to the main Cluster Toolkit blueprint's working directory, run the following command from the CLI.
         
         cd cluster-toolkit
         

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
  3. To define your cluster specifications, create a local file named `gke-a3-highgpu-deployment.yaml` and copy the following deployment variables into it.
         
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: BUCKET_NAME
         
         vars:
           deployment_name: DEPLOYMENT_NAME
           project_id: PROJECT_ID
           region: COMPUTE_REGION
           zone: COMPUTE_ZONE
           authorized_cidr: IP_ADDRESS/SUFFIX
           reservation: RESERVATION_NAME
           static_node_count: NODE_COUNT
         

Replace the following:

     * `DEPLOYMENT_NAME`: a unique name for the deployment. If the deployment name isn't unique within a project, cluster creation fails.
     * `BUCKET_NAME`: the name of the Cloud Storage bucket you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION`: the compute region for the cluster.
     * `COMPUTE_ZONE`: the compute zone for the node pool of A3 High machines.
     * `NODE_COUNT`: the number of A3 High nodes in your cluster.
     * `IP_ADDRESS`/`SUFFIX`: The IP address range that connects to the cluster. This CIDR block must include the IP address of the machine running Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work). To get the IP address for your host machine, run the command `curl ifconfig.me`. 
     * `RESERVATION_NAME`: the name of the reservation. Use one of the following options, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool: 
       * To place the node pool anywhere in the reservation, provide the name of your reservation.
       * To target a specific block within your reservation, use the reservation and block names in the following format: 
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
               

If you don't know which blocks are available in your reservation, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology). 
  4. To modify advanced blueprint settings, edit the [`examples/gke-a3-highgpu/gke-a3-highgpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu.yaml) file in the repository.

  5. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy the blueprint and provision the GKE infrastructure that uses A3 High machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         gke-a3-highgpu-deployment.yaml \
         examples/gke-a3-highgpu/gke-a3-highgpu.yaml
         

  6. When prompted, select **(A)pply** to deploy the blueprint. The blueprint creates VPC networks, service accounts, a cluster, and a node pool.




### Test network performance

We recommend that you validate the functionality of provisioned clusters. To do so, use [NCCL/gIB tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

### Clean up resources created by Cluster Toolkit

To avoid recurring charges for the resources used on this page, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to clean up the resources provisioned by Cluster Toolkit, including the VPC networks and GKE cluster:
    
    
    cd ~/cluster-toolkit
    ./gcluster destroy CLUSTER_NAME/
    

Replace `CLUSTER_NAME` with the name of your cluster. For the clusters created with Cluster Toolkit, the cluster names are based on the `DEPLOYMENT_NAME` name.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
