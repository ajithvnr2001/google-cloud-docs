---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute/
title: Create an AI-optimized GKE cluster with Cluster Toolkit \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:20.108657+00:00
---

# Create an AI-optimized GKE cluster with Cluster Toolkit  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized GKE cluster with Cluster Toolkit Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document shows you how to create an AI-optimized Google Kubernetes Engine (GKE) cluster that uses A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) Compute Engine instances to support your AI and ML workloads.

The A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine series are designed to enable you to run large-scale AI/ML clusters with features such as targeted workload placement, advanced cluster maintenance controls, and topology-aware scheduling. For more information, see [Cluster management overview](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities).

GKE provides a single platform surface to run a diverse set of workloads for your organization's needs. This includes high performance distributed pre-training, model fine-tuning, model inference, application serving, and supporting services. GKE reduces the operational burden of managing multiple platforms.

## Choose how to create an AI-optimized GKE cluster

The following options for cluster creation each provide varying degrees of ease and flexibility in cluster configuration and workload scheduling:

  * Use **Cluster Toolkit** to create clusters with the default configuration for compute, storage, and networking resources, and with GPUDirect RDMA-over-Converged-Ethernet (RoCE) enabled.
  * Alternatively, you can **create your GKE cluster manually** for precise customization or expansion of existing production GKE environments. To create an AI-optimized GKE cluster manually, see one of the following pages:

    * **A4X Max** : [Create an AI-optimized GKE cluster that uses A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max).
    * **A4X** : [Create an AI-optimized GKE cluster that uses A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x).
    * **A4 or A3 Ultra** : [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra).
    * **A3 Mega or A3 High** : [Create a GKE Standard cluster that uses A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega) or [Create a GKE Autopilot cluster that uses A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-autopilot-a3-high-mega).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have the required permissions for creating and managing the GKE cluster and associated service accounts: 
    * Kubernetes Engine Admin (`roles/container.admin`)
    * Compute Admin (`roles/compute.admin`)
    * Storage Admin (`roles/storage.admin`)
    * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)
    * Service Account Admin (`roles/iam.serviceAccountAdmin`)
    * Service Account User (`roles/iam.serviceAccountUser`)
    * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)
    * Role Administrator (`roles/iam.roleAdmin`)
    * Secret Manager Secret Version Manager (`roles/secretmanager.secretVersionManager`)
    * To consume a single-project reservation: Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) on the project
    * To consume a shared reservation: Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation



### Choose a consumption option and obtain capacity

  1. **Choose a consumption option**. Make your choice based on how you want to get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

For GKE, consider the following additional information when choosing a consumption option:

     * A4X Max and A4X compute instances can't be provisioned by flex-start.
     * For more information about flex-start ([Preview](https://cloud.google.com/products#product-launch-stages)) and GKE, see [About GPU obtainability with flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
     * Flex-start uses best-effort compact placement. To examine your topology, see [View the physical topology of nodes in your GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas#view-physical-topology).
     * You can only get topology information when using Spot VMs if you configure [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).
  2. **Obtain capacity**. The process to obtain capacity differs for each consumption option.

To learn about the process for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).

**Note:** When you request A4X capacity, you obtain it in _all capacity mode_. This mode is the only supported reservation operational mode for A4X machine types. For more information about all capacity mode, see [Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode).



### Requirements

The following requirements apply to an AI-optimized GKE cluster:

  * For A4X Max, you must use one of the following versions:

    * For 1.35 or later, use GKE version 1.35.0-gke.2745000 or later.
    * For 1.34, use GKE version 1.34.3-gke.1318000 or later.

These versions help to ensure that A4X Max uses the following:

    * R580.95.05, the minimum GPU driver version for A4X Max, which is enabled by default.
    * Coherent Driver-based Memory Management (CDMM), which is enabled by default. NVIDIA recommends that Kubernetes clusters enable this mode to resolve memory over-reporting. CDMM allows GPU memory to be managed through the driver instead of the operating system (OS). This approach helps you to avoid OS onlining of GPU memory, and exposes the GPU memory as a Non-Uniform Memory Access (NUMA) node to the OS. Multi-instance GPUs aren't supported when CDMM is enabled. For more information about CDMM, see [Hardware and Software Support](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-65-06/index.html#hardware-software-support).
    * GPUDirect RDMA and [MNNVL](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html), which are recommended to enable A4X Max node pools to use the networking capabilities of A4X Max.
  * For A4X, you must use one of the following versions:

    * For 1.33 or later, use GKE version 1.33.4-gke.1036000 or later.
    * For 1.32, use GKE version 1.32.8-gke.1108000 or later.

These versions help to ensure that A4X uses the following:

    * R580, the minimum GPU driver version for A4X, which is enabled by default.
    * Coherent Driver-based Memory Management (CDMM), which is enabled by default. NVIDIA recommends that Kubernetes clusters enable this mode to resolve memory over-reporting. CDMM allows GPU memory to be managed through the driver instead of the operating system (OS). This approach helps you to avoid OS onlining of GPU memory, and exposes the GPU memory as a Non-Uniform Memory Access (NUMA) node to the OS. Multi-instance GPUs aren't supported when CDMM is enabled. For more information about CDMM, see [Hardware and Software Support](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-65-06/index.html#hardware-software-support).
    * GPUDirect RDMA and [MNNVL](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html), which are recommended to enable A4X node pools to use the networking capabilities of A4X.
  * Ensure you use the minimum GPU driver version, depending on the machine type:

    * **A4X Max** : The GB300 GPUs in A4X Max bare metal instances require a minimum of the R580.95.05 GPU driver version. See the previously mentioned version requirements.
    * **A4X** : The GB200 GPUs in A4X instances require a minimum of the R580 GPU driver version. See the previously mentioned version requirements.
    * **A4** : The B200 GPUs in A4 instances require a minimum of the R570 GPU driver version. GKE, by default, automatically installs this driver version on all A4 nodes running the required minimum version for A4, 1.32.1-gke.1729000 or later.
    * **A3 Ultra** : The H200 GPUs in A3 Ultra instances require a minimum of R550 GPU driver version, which is available in GKE 1.31 as `latest` driver version. For A3 Ultra, you must set `gpu-driver-version=latest` with GKE 1.31. For GKE version 1.31.5-gke.1169000 or later, GKE, by default, automatically installs R550 GPU driver versions on A3 Ultra nodes.
    * **A3 Mega and A3 High** : The H100 GPUs in A3 High and A3 Mega instances are supported by the default GPU driver version in all supported GKE versions. You can also set `gpu-driver-version=latest` to access newer production drivers available on supported GKE versions.
  * For A3 Ultra node pools, you must set the disk type to `hyperdisk-balanced`.

  * To use GPUDirect RDMA, use the following minimum versions depending on the machine type:

    * **A4X Max** : See the previously mentioned version requirements.
    * **A4X** : see the previously mentioned version requirements.
    * **A4** : use 1.32.2-gke.1475000 or later.
    * **A3 Ultra** : use 1.31.4-gke.1183000 or later.
  * To use GPUDirect-TCPXO (for A3 Mega) and GPUDirect-TCPX (for A3 High), use the following GKE versions:

    * **A3 High** : use any available GKE version before 1.34.
    * **A3 Mega** : use any available GKE version.
  * To use GPUDirect RDMA, the GKE nodes must use a Container-Optimized OS node image. Ubuntu and Windows node images are not supported.

  * You must use the [reservation-bound](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound) provisioning model to create clusters with A4X Max and A4X. Other provisioning models are not supported.




## Create a cluster with Cluster Toolkit

Use the following instructions to create a cluster by using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). This section guides you through the cluster creation process, ensuring that your project follows best practices and meets the requirements for an AI-optimized GKE cluster. This section also shows you how to use Terraform to provision and manage the infrastructure for your deployment.

**Note:** If you create multiple clusters using these same cluster blueprints, ensure that all VPC and subnet names are unique per project to prevent errors.

### A4X Max

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment.
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).

  3. Create a Cloud Storage bucket with versioning enabled to store the state of your Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. In the [`examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4x-max-bm`.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A4X Max machines. Note that this zone must match the zone where machines are available in your reservation.
     * `STATIC_NODE_COUNT`: the number of A4X Max nodes in your cluster's node pool, which must be 18 nodes or less. We recommend using 18 nodes to obtain the GPU topology of `1x72` in one subblock using an NVLink domain.
     * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

     * `RESERVATION_PROJECT_ID`: the Google Cloud project ID that has the reservation. Your reservation might exist in a different project from `PROJECT_ID`.

     * `NUM_NODE_POOLS`: the number of node pools to enable in your cluster. If you want a cluster larger than 18 nodes, then you can specify multiple node pools. The default value is `1`.

To modify advanced settings, edit the [`examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml) file.

  5. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, sign in and set up ADC:
         
         gcloud auth application-default login
         

  6. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy the blueprint and provision the GKE infrastructure using A4X Max machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a4x-max-bm/gke-a4x-max-bm-deployment.yaml \
         examples/gke-a4x-max-bm/gke-a4x-max-bm.yaml \
         --deployment DEPLOYMENT_NAME
         

Replace `DEPLOYMENT_NAME` with your deployment name.

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



### A4X

**Note:** This GKE A4X blueprint automatically configures GKE-managed [Dynamic Resource Allocation for Networking (DRANET)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra). For more information, see [Configure DRANET functionality](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-cluster#configure-dranet).

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment.
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).
  3. Create a Cloud Storage bucket with versioning enabled to store the state of your Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. In the [`examples/gke-a4x/gke-a4x-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x/gke-a4x-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4x`.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A4X machines. Note that this zone must match the zone where machines are available in your reservation.
     * `STATIC_NODE_COUNT`: the number of A4X nodes in your cluster's node pool, which must be 18 nodes or less. We recommend using 18 nodes to obtain the GPU topology of `1x72` in one subblock using an NVLink domain.
     * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

     * `RESERVATION_PROJECT_ID`: the Google Cloud project ID that has the reservation. Your reservation might exist in a different project from `PROJECT_ID`.

     * `NUM_NODE_POOLS`: the number of node pools to enable in your cluster. If you want a cluster larger than 18 nodes, then you can specify multiple node pools. The default value is `1`.

To modify advanced settings, edit the [`examples/gke-a4x/gke-a4x.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x/gke-a4x.yaml) file.

  5. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, sign in and set up ADC:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using A4X machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a4x/gke-a4x-deployment.yaml \
         examples/gke-a4x/gke-a4x.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



### A4

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment.
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).

  3. Create a Cloud Storage bucket with versioning enabled to store the state of your Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. The files that you need to edit to create a cluster depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

In the [`examples/gke-a4/gke-a4-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4`.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A4 machines. Note that this zone must match the zone where machines are available in your reservation.
     * `STATIC_NODE_COUNT`: the number of A4 nodes in your cluster.
     * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

To modify advanced settings, edit [`examples/gke-a4/gke-a4.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4.yaml).

### Flex-start

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. In the [`examples/gke-a4/gke-a4-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4`.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A4 machines.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Remove the `reservation` field, and replace the field with `enable_flex_start: true`. Add on the next line `enable_queued_provisioning: true` if you'd also like to use queued provisioning. For more information, see [Use node pools with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest#node-pools).
        * Remove `static_node_count`.
     2. In the [`examples/gke-a4/gke-a4.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4.yaml), make the following changes:

        * In the `vars` block, remove `static_node_count`.
        * In the `vars` block, make sure the `version_prefix` number is `"1.32."` or higher. To use flex-start in GKE, your cluster must use version 1.32.2-gke.1652000 or later.
        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `enable_flex_start: true`, and, optionally, `enable_queued_provisioning: true`.
        * In the `vars` block, if you don't require queued provisioning, remove the following line: `kueue_configuration_path: $(ghpc_stage("./kueue-configuration.yaml.tftpl"))`.
        * Under `id: a4-pool`, remove the following line: `static_node_count: $(vars.static_node_count)`.
        * Under `id: a4-pool`, remove the `reservation_affinity` block. Replace this block with the following lines:

          * `enable_flex_start: $(vars.enable_flex_start)`
          * `auto_repair: false`
          * For queued provisioning, if you want to enable it, add the following additional lines: 
            * `enable_queued_provisioning: $(vars.enable_queued_provisioning)`
            * `autoscaling_total_min_nodes: 0`
        * Under `id: workload-manager-install`, remove the following block:
              
              kueue:
                  install: true
                  config_path: $(vars.kueue_configuration_path)
                  config_template_vars:
                     num_gpus: $(a3-ultragpu-pool.static_gpu_count)
                     accelerator_type: $(vars.accelerator_type)
              

          * For flex-start with queued provisioning, do the following:

            1. Add `gpu_nominal_quota: NOMINAL_QUOTA` to the `vars` block. The `gpu_nominal_quota` value is used to set the `nominalQuota` of GPUs in the `ClusterQueue` spec (in the following, see the step setting `ClusterQueue`). In this example, the `ClusterQueue` only admits workloads if the sum of the GPU requests is less than or equal to the `NOMINAL_QUOTA` value. For more information about `ClusterQueue`, see the following [Kueue document of Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/).

            2. Update the `kueue` block to the following:
                   
                   kueue:
                      install: true
                      config_path: $(vars.kueue_configuration_path)
                      config_template_vars:
                         num_gpus: $(vars.gpu_nominal_quota)
                   

            3. Replace the content of the `kueue-configuration.yaml.tftpl` file with the following:
                   
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ResourceFlavor
                   metadata:
                      name: "default-flavor"
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: AdmissionCheck
                   metadata:
                      name: dws-prov
                   spec:
                      controllerName: kueue.x-k8s.io/provisioning-request
                      parameters:
                         apiGroup: kueue.x-k8s.io
                         kind: ProvisioningRequestConfig
                         name: dws-config
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ProvisioningRequestConfig
                   metadata:
                      name: dws-config
                   spec:
                      provisioningClassName: queued-provisioning.gke.io
                      managedResources:
                      - nvidia.com/gpu
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ClusterQueue
                   metadata:
                      name: "dws-cluster-queue"
                   spec:
                      namespaceSelector: {}
                      resourceGroups:
                      - coveredResources: ["nvidia.com/gpu"]
                         flavors:
                         - name: "default-flavor"
                         resources:
                         - name: "nvidia.com/gpu"
                            nominalQuota: ${num_gpus}
                      admissionChecks:
                      - dws-prov
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: LocalQueue
                   metadata:
                      namespace: "default"
                      name: "dws-local-queue"
                   spec:
                      clusterQueue: "dws-cluster-queue"
                   ---
                   

        * Under `id: job-template`, replace the `node_count` variable with `2`.

### Spot

     1. In the [`examples/gke-a4/gke-a4-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails. The default value is `gke-a4`.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A4 machines.
        * `STATIC_NODE_COUNT`: the number of A4 nodes in your cluster.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Replace the entire `reservation` block (including the `reservation` line itself) with `spot: true`.
     2. In the [`examples/gke-a4/gke-a4.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4.yaml), make the following changes:

        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `spot: true`.
        * Under `id: a4-pool`, remove the `reservation_affinity` block. Replace this block with the following line:

          * `spot: $(vars.spot)`

  5. [Generate Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, sign in and set up ADC:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using A4 machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a4/gke-a4-deployment.yaml \
         examples/gke-a4/gke-a4.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a nodepool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



### A3 Ultra

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, follow the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies) to prepare a different environment.
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).

  3. Create a Cloud Storage bucket with versioning enabled to store the state of your Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. The files that you need to edit to create a cluster depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

In the [`examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml), replace the following variables in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET_NAME`: the name of the Cloud Storage bucket you created in the previous step.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION`: the compute region for the cluster.
     * `COMPUTE_ZONE`: the compute zone for the node pool of A3 Ultra machines. Note that this zone must match the zone where machines are available in your reservation.

     * `IP_ADDRESS/SUFFIX`: The IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).

     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View a reservation topology](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

     * `NODE_COUNT`: the number of A3 Ultra nodes in your cluster.

To modify advanced settings, edit [`examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml).

### Flex-start

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. In the [`examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml), replace the following variables in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

        * `BUCKET_NAME`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `COMPUTE_REGION`: the compute region for the cluster.
        * `COMPUTE_ZONE`: the compute zone for the node pool of A3 Ultra machines.
        * `IP_ADDRESS/SUFFIX`: The IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Remove the `reservation` field, and replace the field with `enable_flex_start: true`. Add on the next line `enable_queued_provisioning: true` if you'd also like to use queued provisioning. For more information, see [Use node pools with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest#node-pools).
        * Remove `static_node_count`.
     2. In the [`examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml), make the following changes:

        * In the `vars` block, remove `static_node_count`.
        * In the `vars` block, update `version_prefix` number to `"1.32."` or higher. To use flex-start in GKE, your cluster must use version 1.32.2-gke.1652000 or later.
        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `enable_flex_start: true`, and, optionally, `enable_queued_provisioning: true`.
        * In the `vars` block, remove the following line: `kueue_configuration_path: $(ghpc_stage("./kueue-configuration.yaml.tftpl"))`.
        * Under `id: a3-ultragpu-pool`, remove the following line: `static_node_count: $(vars.static_node_count)`.
        * Under `id: a3-ultragpu-pool`, remove the `reservation_affinity` block. Replace this block with the following lines:

          * `enable_flex_start: $(vars.enable_flex_start)`
          * `auto_repair: false`
          * For queued provisioning, if you want to enable it, add the following additional lines: 
            * `enable_queued_provisioning: $(vars.enable_queued_provisioning)`
            * `autoscaling_total_min_nodes: 0`
        * Under `id: workload-manager-install`, remove the following block:
              
              config_path: $(vars.kueue_configuration_path)
              config_template_vars:
                num_gpus: $(a4-pool.static_gpu_count)
                accelerator_type: $(vars.accelerator_type)
              

          * For flex-start with queued provisioning, follow these three steps:

            1. Add `gpu_nominal_quota: NOMINAL_QUOTA` to the `vars` block. The `gpu_nominal_quota` value is used to set the `nominalQuota` of GPUs in the `ClusterQueue` specification. In this example, the `ClusterQueue` only admits workloads if the sum of the GPU requests is less than or equal to the `NOMINAL_QUOTA` value. For more information about `ClusterQueue`, see the following [Kueue document of Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/).

            2. Update the `kueue` block to the following:
                   
                   kueue:
                      install: true
                      config_path: $(vars.kueue_configuration_path)
                      config_template_vars:
                         num_gpus: $(vars.gpu_nominal_quota)
                   

            3. Replace the content of the `kueue-configuration.yaml.tftpl` file with the following:
                   
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ResourceFlavor
                   metadata:
                      name: "default-flavor"
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: AdmissionCheck
                   metadata:
                      name: dws-prov
                   spec:
                      controllerName: kueue.x-k8s.io/provisioning-request
                      parameters:
                         apiGroup: kueue.x-k8s.io
                         kind: ProvisioningRequestConfig
                         name: dws-config
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ProvisioningRequestConfig
                   metadata:
                      name: dws-config
                   spec:
                      provisioningClassName: queued-provisioning.gke.io
                      managedResources:
                      - nvidia.com/gpu
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ClusterQueue
                   metadata:
                      name: "dws-cluster-queue"
                   spec:
                      namespaceSelector: {}
                      resourceGroups:
                      - coveredResources: ["nvidia.com/gpu"]
                         flavors:
                         - name: "default-flavor"
                         resources:
                         - name: "nvidia.com/gpu"
                            nominalQuota: ${num_gpus}
                      admissionChecks:
                      - dws-prov
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: LocalQueue
                   metadata:
                      namespace: "default"
                      name: "dws-local-queue"
                   spec:
                      clusterQueue: "dws-cluster-queue"
                   ---
                   

          * In the `id: job-template` field, replace the `node_count` variable with `2`.

### Spot

     1. In the [`examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml), fill in the following settings in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

        * `BUCKET_NAME`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `COMPUTE_REGION`: the compute region for the cluster.
        * `COMPUTE_ZONE`: the compute zone for the node pool of A3 Ultra machines.
        * `IP_ADDRESS/SUFFIX`: The IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Replace the entire `reservation` block (including the `reservation` line itself) with `spot: true`.
        * `NODE_COUNT`: the number of A3 Ultra nodes in your cluster.
     2. In the [`examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml` blueprint from the GitHub repo](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml), make the following changes:

        * In the `vars` block, replace the entire `reservation` variable with `spot: true`.
        * In the `id: a3-ultragpu-pool` section, remove the `reservation_affinity` block. Replace this block with the following line:

          * `spot: $(vars.spot)`

  5. Generate [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, sign in and set up ADC:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using A3 Ultra machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a3-ultragpu/gke-a3-ultragpu-deployment.yaml \
         examples/gke-a3-ultragpu/gke-a3-ultragpu.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a nodepool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



### A3 Mega

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, prepare a different environment by following the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).

  3. Create a Cloud Storage bucket with versioning enabled to store the state of your Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
             --default-storage-class=STANDARD \
             --project=PROJECT_ID \
             --location=COMPUTE_REGION_TERRAFORM_STATE \
             --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning

Replace the following variables:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  4. The files that you need to edit to create a cluster depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

In the [`examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml), replace the following variables in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A3 Mega machines. Note that this zone should match the zone where machines are available in your reservation.
     * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

     * `STATIC_NODE_COUNT`: the number of A3 Mega nodes in your cluster.

To modify advanced settings, edit [`examples/gke-a3-megagpu/gke-a3-megagpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml).

### Flex-start

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. In the [`examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml), replace the following variables in the `vars` sections to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A3 Mega machines.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Remove the `reservation` field, and replace the field with `enable_flex_start: true`. If you also want to use queued provisioning, add `enable_queued_provisioning: true` to the following line. For more information, see [Use node pools with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest#node-pools).
        * Remove `static_node_count`.
     2. In the [`examples/gke-a3-megagpu/gke-a3-megagpu.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml), make the following changes:

        * In the `vars` block, remove `static_node_count`.
        * In the `vars` block, update `version_prefix` number to `"1.32."` or higher. To use flex-start in GKE, your cluster must use version 1.32.2-gke.1652000 or later.
        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `enable_flex_start: true`, and, optionally, `enable_queued_provisioning: true`.
        * In the `vars` block, remove the following line: `kueue_configuration_path: $(ghpc_stage("./kueue-configuration.yaml.tftpl"))`.
        * Under `id: a3_megagpu_pool`, remove the following line: `static_node_count: $(vars.static_node_count)`.
        * Under `id: a3_megagpu_pool`, remove the `reservation_affinity` block. Replace this block with the following lines:

          * `enable_flex_start: $(vars.enable_flex_start)`
          * `auto_repair: false`
          * For queued provisioning, if you want to enable it, add the following additional lines: 
            * `enable_queued_provisioning: $(vars.enable_queued_provisioning)`
            * `autoscaling_total_min_nodes: 0`
        * Under `id: workload_manager_install`, remove the following block:
              
              config_path: $(vars.kueue_configuration_path)
              config_template_vars:
                num_gpus: $(a3_megagpu_pool.static_gpu_count)
                accelerator_type: $(vars.accelerator_type)
              

          * For flex-start with queued provisioning, follow these three steps:

            1. Add `gpu_nominal_quota: NOMINAL_QUOTA` to the `vars` block. The `gpu_nominal_quota` value is used to set the `nominalQuota` of GPUs in the `ClusterQueue` specification. In this example, the `ClusterQueue` only admits workloads if the sum of the GPU requests is less than or equal to the `NOMINAL_QUOTA` value. For more information about `ClusterQueue`, see the following [Kueue document of Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/).

            2. Update the `kueue` block to the following:
                   
                   kueue:
                      install: true
                      config_path: $(vars.kueue_configuration_path)
                      config_template_vars:
                         num_gpus: $(vars.gpu_nominal_quota)
                   

            3. Replace the content of the `kueue-configuration.yaml.tftpl` file with the following:
                   
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ResourceFlavor
                   metadata:
                      name: "default-flavor"
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: AdmissionCheck
                   metadata:
                      name: dws-prov
                   spec:
                      controllerName: kueue.x-k8s.io/provisioning-request
                      parameters:
                         apiGroup: kueue.x-k8s.io
                         kind: ProvisioningRequestConfig
                         name: dws-config
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ProvisioningRequestConfig
                   metadata:
                      name: dws-config
                   spec:
                      provisioningClassName: queued-provisioning.gke.io
                      managedResources:
                      - nvidia.com/gpu
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ClusterQueue
                   metadata:
                      name: "dws-cluster-queue"
                   spec:
                      namespaceSelector: {}
                      resourceGroups:
                      - coveredResources: ["nvidia.com/gpu"]
                         flavors:
                         - name: "default-flavor"
                         resources:
                         - name: "nvidia.com/gpu"
                            nominalQuota: ${num_gpus}
                      admissionChecks:
                      - dws-prov
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: LocalQueue
                   metadata:
                      namespace: "default"
                      name: "dws-local-queue"
                   spec:
                      clusterQueue: "dws-cluster-queue"
                   ---
                   

          * In the `id: job-template` field, replace the value of the `node_count` variable with `2`.

### Spot

     1. In the [`examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml), update the following variables to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A3 Mega machines.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Replace the entire `reservation` block (including the `reservation` line itself) with `provisioning_model: SPOT`.
        * `STATIC_NODE_COUNT`: the number of A3 Mega nodes in your cluster.
     2. In the [`examples/gke-a3-megagpu/gke-a3-megagpu.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml), make the following changes:

        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `spot: true`.
        * In the `id: a3_megagpu_pool` section, remove the `reservation_affinity` block. Replace this block with the following line:

          * `spot: $(vars.spot)`

  5. Generate [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, you can run the following command:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using A3 Mega machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a3-megagpu/gke-a3-megagpu.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



### A3 High

  1. [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell). You can use a different environment; however, we recommend Cloud Shell because the dependencies are already pre-installed for Cluster Toolkit. If you don't want to use Cloud Shell, prepare a different environment by following the instructions to [install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).
  2. [Install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install).

  3. Create a Cloud Storage bucket to store the state of the Terraform deployment:
         
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
  4. The files that you need to edit to create a cluster depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

In the [`examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml), replace the following variables in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A3 High machines. Note that this zone should match the zone where machines are available in your reservation.
     * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
     * `STATIC_NODE_COUNT`: the number of A3 High nodes in your cluster.
     * For the `reservation` field, use one of the following, depending on whether you want to target specific [blocks](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) in a reservation when provisioning the node pool:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
             
             RESERVATION_NAME/reservationBlocks/BLOCK_NAME
             

If you don't know which blocks are available in your reservation, see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

To modify advanced settings, edit [`examples/gke-a3-highgpu/gke-a3-highgpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu.yaml).

### Flex-start

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. In the [`examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml` file from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml), replace the following variables in the `vars` sections to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A3 High machines.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Remove the `reservation` field, and replace the field with `enable_flex_start: true`. If you also want to use queued provisioning, add `enable_queued_provisioning: true` to the following line. For more information, see [Use node pools with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest#node-pools).
        * Remove `static_node_count`.
     2. In the [`examples/gke-a3-highgpu/gke-a3-highgpu.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu.yaml), make the following changes:

        * In the `vars` block, remove `static_node_count`.
        * In the `vars` block, update `version_prefix` number to `"1.32."` or higher. To use flex-start in GKE, your cluster must use version 1.32.2-gke.1652000 or later.
        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `enable_flex_start: true`, and, optionally, `enable_queued_provisioning: true`.
        * In the `vars` block, remove the following line: `kueue_configuration_path: $(ghpc_stage("./kueue-configuration.yaml.tftpl"))`.
        * Under `id: a3_highgpu_pool`, remove the following line: `static_node_count: $(vars.static_node_count)`.
        * Under `id: a3_highgpu_pool`, remove the `reservation_affinity` block. Replace this block with the following lines:

          * `enable_flex_start: $(vars.enable_flex_start)`
          * `auto_repair: false`
          * For queued provisioning, if you want to enable it, add the following additional lines: 
            * `enable_queued_provisioning: $(vars.enable_queued_provisioning)`
            * `autoscaling_total_min_nodes: 0`
        * Under `id: workload_component_install`, remove the following block:
              
              config_path: $(vars.kueue_configuration_path)
              config_template_vars:
                num_gpus: $(a3_highgpu_pool.static_gpu_count)
                accelerator_type: $(vars.accelerator_type)
              

          * For flex-start with queued provisioning, follow these three steps:

            1. Add `gpu_nominal_quota: NOMINAL_QUOTA` to the `vars` block. The `gpu_nominal_quota` value is used to set the `nominalQuota` of GPUs in the `ClusterQueue` specification. In this example, the `ClusterQueue` only admits workloads if the sum of the GPU requests is less than or equal to the `NOMINAL_QUOTA` value. For more information about `ClusterQueue`, see the following [Kueue document of Cluster Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/).

            2. Update the `kueue` block to the following:
                   
                   kueue:
                      install: true
                      config_path: $(vars.kueue_configuration_path)
                      config_template_vars:
                         num_gpus: $(vars.gpu_nominal_quota)
                   

            3. Replace the content of the `kueue-configuration.yaml.tftpl` file with the following:
                   
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ResourceFlavor
                   metadata:
                      name: "default-flavor"
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: AdmissionCheck
                   metadata:
                      name: dws-prov
                   spec:
                      controllerName: kueue.x-k8s.io/provisioning-request
                      parameters:
                         apiGroup: kueue.x-k8s.io
                         kind: ProvisioningRequestConfig
                         name: dws-config
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ProvisioningRequestConfig
                   metadata:
                      name: dws-config
                   spec:
                      provisioningClassName: queued-provisioning.gke.io
                      managedResources:
                      - nvidia.com/gpu
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: ClusterQueue
                   metadata:
                      name: "dws-cluster-queue"
                   spec:
                      namespaceSelector: {}
                      resourceGroups:
                      - coveredResources: ["nvidia.com/gpu"]
                         flavors:
                         - name: "default-flavor"
                         resources:
                         - name: "nvidia.com/gpu"
                            nominalQuota: ${num_gpus}
                      admissionChecks:
                      - dws-prov
                   ---
                   apiVersion: kueue.x-k8s.io/v1beta1
                   kind: LocalQueue
                   metadata:
                      namespace: "default"
                      name: "dws-local-queue"
                   spec:
                      clusterQueue: "dws-cluster-queue"
                   ---
                   

          * In the `id: job-template` field, replace the value of the `node_count` variable with `2`.

### Spot

     1. In the [`examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml), update the following variables to match the specific values for your deployment:

        * `BUCKET`: the name of the Cloud Storage bucket you created in the previous step.
        * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, cluster creation fails.
        * `PROJECT_ID`: your Google Cloud project ID.
        * `REGION`: the compute region for the cluster.
        * `ZONE`: the compute zone for the node pool of A3 High machines.
        * `AUTHORIZED_CIDR`: the IP address range that you want to allow to connect with the cluster. This CIDR block must include the IP address of the machine that you want to use to call Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work).
        * Replace the `reservation:` line with `provisioning_model: SPOT`.
        * `STATIC_NODE_COUNT`: the number of A3 High nodes in your cluster.
     2. In the [`examples/gke-a3-highgpu/gke-a3-highgpu.yaml` blueprint from the GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-highgpu/gke-a3-highgpu.yaml), make the following changes:

        * In the `vars` block, replace the entire `reservation` block (including the `reservation` line itself) with `spot: true`.
        * In the `id: a3_highgpu_pool` section, remove the `reservation_affinity` block. Replace this block with the following line:

          * `spot: $(vars.spot)`

  5. Generate [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) to provide access to Terraform. If you're using Cloud Shell, you can run the following command:
         
         gcloud auth application-default login
         

  6. Deploy the blueprint to provision the GKE infrastructure using A3 High machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a3-highgpu/gke-a3-highgpu-deployment.yaml \
         examples/gke-a3-highgpu/gke-a3-highgpu.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint.

     * The blueprint creates VPC networks, a GPU RDMA VPC network, service accounts, a cluster, and a node pool.
     * To support the `fio-bench-job-template` job template in the blueprint, Google Cloud buckets, network storage, and persistent volumes resources are created.



## Test network performance

We recommend that you validate the functionality of provisioned clusters. To do so, use [NCCL tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

## Run reproducible benchmarks

After you create a cluster by using Cluster Toolkit, you can reproduce pre-training benchmarks for large machine learning open models on your chosen machine series by following recipes provided in GitHub.

Each recipe provides you with the instructions to complete the following tasks:

  * Prepare your environment.
  * Run the benchmark.
  * Analyze the benchmarks results. This includes the benchmark results and detailed logs for further analysis.



To view all the recipes available for training and other types of workloads, see the [GPU recipes](https://github.com/AI-Hypercomputer/gpu-recipes) GitHub repository.

## Clean up resources created by Cluster Toolkit

To avoid recurring charges for the resources used on this page, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to clean up the resources provisioned by Cluster Toolkit, including the VPC networks and GKE cluster:
    
    
       cd ~/cluster-toolkit
       ./gcluster destroy CLUSTER_NAME/
    

Replace `CLUSTER_NAME` with the name of your cluster. For the clusters created with Cluster Toolkit, the cluster name is based on the `DEPLOYMENT_NAME`.

## What's next

  * To learn about scheduling workloads on your GKE clusters using TAS and Kueue, see [Schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).
  * To learn about managing common events relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).
  * For information about testing your environment for proper setup and optimization, see [Cluster networking optimization overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
