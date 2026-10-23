---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus/
title: Run GPUs in GKE Standard node pools \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:03.909139+00:00
---

# Run GPUs in GKE Standard node pools  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Run GPUs in GKE Standard node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to run and optimize your compute-intensive workloads, such as artificial intelligence (AI) and graphics processing, by attaching and using NVIDIA® graphics processing unit (GPU) hardware accelerators in your Google Kubernetes Engine (GKE) Standard clusters' [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes). If you are using Autopilot Pods instead, refer to [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).

If you want to deploy clusters with NVIDIA B300, NVIDIA B200, or NVIDIA H200 141GB GPUs, see the following resources instead:

  * To create GKE clusters, see [Create an AI-optimized Google Kubernetes Engine cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).
  * To create Slurm clusters, see the following: 
    * [Create a fully managed Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster).
    * [Create a self-managed Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster).



## Overview

With GKE, you can create [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) equipped with [GPUs](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads). GPUs provide compute power to drive deep-learning tasks such as image recognition, natural language processing, as well as other compute-intensive tasks such as video transcoding and image processing. In GKE Standard mode, you can attach GPU hardware to nodes in your clusters, and then allocate GPU resources to containerized workloads running on those nodes.

To learn more about use cases for GPUs, refer to Google Cloud's [GPUs](https://cloud.google.com/gpu/) page. For more information about GPUs in GKE and the differences between Standard mode and Autopilot mode, refer to [About GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).

You can also use GPUs with [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) if your workloads can tolerate frequent node disruptions. Using Spot VMs reduces the price of running GPUs. To learn more, refer to [Using Spot VMs with GPU node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#spot-vms-gpus).

As of version 1.29.2-gke.1108000, you can now create GPU node pools on GKE Sandbox. For more information, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpus) and [GKE Sandbox Configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Requirements for GPUs on GKE

**Caution:** NVIDIA P100 GPUs reach end of support on September 15, 2026. For more information, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos). 

GPUs on GKE have the following requirements:

  * **GPU quota** : You must have [Compute Engine GPU quota](https://docs.cloud.google.com/compute/quotas#gpu_quota) in your selected zone before you can create GPU nodes. To ensure that you have enough GPU quota in your project, refer to [Quotas](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console.

If you require additional GPU quota, you must request GPU quota in the Google Cloud console. If you have an established billing account, your project automatically receives quota after you submit the quota request.

By default, Free Trial accounts don't receive GPU quota.

  * **NVIDIA GPU drivers** : When creating a cluster or a node pool, you can tell GKE to automatically install a driver version based on your GKE version. If you don't tell GKE to automatically install GPU drivers, you _must_ manually install the drivers.

  * **Machine series** : The GPU type you can use depends on the machine series, as follows:

    * [A4X Max machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms): GB300 GPUs.
    * [A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms): GB200 GPUs.
    * [A4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms): B200 GPUs.
    * [A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms): H200 GPUs ([A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms)), and H100 GPUs (A3 Mega, High, Edge).
    * [A2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms): A100 GPUs.
    * [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series): RTX PRO 6000 GPUs.
    * [G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms): L4 GPUs.
    * [N1 machine series](https://docs.cloud.google.com/compute/docs/machine-types#n1_machine_types): NVIDIA T4 GPUs, NVIDIA V100 GPUs, NVIDIA P100 GPUs (approaching [end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)), or NVIDIA P4 GPUs.

You should ensure that you have enough quota in your project for the machine series that corresponds to your selected GPU type and quantity.

  * **GKE versions** : You must use specific GKE versions for certain machine series and shapes:

    * **[Accelerator-optimized A series](https://docs.cloud.google.com/compute/docs/gpus#gpu-models)** : See the respective cluster creation guides for version requirements.
    * **G4 machine series with Standard mode** :

      * **Machine types that have one or more GPUs** : 1.34.0-gke.1662000 or later
      * **Machine types that have less than one GPU** : Use one of the following patch versions or later, based on the GKE minor version:

        * **1.34** : 1.34.5-gke.1153000
        * **1.35 or later** : 1.35.3-gke.1389000
  * **GPUs on Ubuntu nodes** : If you use GPUs with Ubuntu nodes, the following requirements apply:

    * **Ubuntu driver compatibility** :

      * **L4 GPUs** and **H100 GPUs** : NVIDIA driver version 535 or later

      * **H200 GPUs** : NVIDIA driver version 550 or later

      * **B200 GPUs** : NVIDIA driver version 570 or later

      * **RTX PRO 6000 GPUs** : NVIDIA driver version 580 or later. This version compatibility excludes G4 machine types that have less than one GPU because they don't support Ubuntu node images.

If a required driver version or a later version isn't the default version in your GKE version, you must manually install a supported driver on your nodes.

    * **Ubuntu version compatibility** :

When you use A4 machine series on Ubuntu node pools, you must use a GKE version that includes the `ubuntu-gke-2404-1-32-amd64-v20250730` image or a later version of the node image. The minimum GKE versions are the following:

      * 1.32.7-gke.1067000 or later for GKE version 1.32
      * 1.33.3-gke.1247000 or later for GKE version 1.33

**Best practice** : 

Use Container-Optimized OS for GPU nodes. Container-Optimized OS includes the required drivers to support the specific GKE version for GPU nodes.

### Limitations of using GPUs on GKE

Before you use GPUs on GKE, keep in mind the following limitations:

  * You can't add GPUs to existing node pools.
  * GPU nodes can't be [live migrated](https://docs.cloud.google.com/compute/docs/instances/live-migration#gpusmaintenance) during maintenance events.
  * **Machine series** : The GPU type you can use depends on the machine series, as follows:

    * [A4X Max machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms): GB300 GPUs.
    * [A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms): GB200 GPUs.
    * [A4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms): B200 GPUs.
    * [A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms): H200 GPUs ([A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms)), and H100 GPUs (A3 Mega, High, Edge).
    * [A2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms): A100 GPUs.
    * [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series): RTX PRO 6000 GPUs.
    * [G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms): L4 GPUs.
    * [N1 machine series](https://docs.cloud.google.com/compute/docs/machine-types#n1_machine_types): NVIDIA T4 GPUs, NVIDIA V100 GPUs, NVIDIA P100 GPUs (approaching [end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)), or NVIDIA P4 GPUs.

You should ensure that you have enough quota in your project for the machine series that corresponds to your selected GPU type and quantity.

  * GPUs are not supported in Windows Server node pools.

  * GKE Standard clusters running versions earlier than 1.34.1-gke.1279000 don't support [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) creating node pools with RTX PRO 6000 GPUs. However, clusters running earlier versions support [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) scaling existing node pools.

  * GKE Standard clusters running version 1.28.2-gke.1098000 or earlier don't support [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) creating node pools with L4 GPUs. However, clusters running earlier versions support [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) scaling existing node pools.

  * G4 machine types that have less than one GPU have the following additional limitations:

    * You can't use [Ubuntu node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu).
    * You must prepare your workloads to run on these machine types for clusters running GKE versions earlier than 1.36.
    * You can't use [multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi), [NVIDIA MPS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus), or [GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus).



### Availability of GPUs by regions and zones

GPUs are available in specific [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). When you request GPU quota, consider the regions in which you intend to run your clusters.

For a complete list of applicable regions and zones, refer to [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

You can also see GPUs available in your zone using the Google Cloud CLI. To see a list of all GPU accelerator types supported in each zone, run the following command:
    
    
    gcloud compute accelerator-types list
    

### Pricing

For GPU pricing information, refer to the [pricing table](https://docs.cloud.google.com/compute/gpus-pricing) on the Google Cloud GPU page.

## Ensure sufficient GPU quota

Your GPU quota is the total number of GPUs that can run in your [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). To create clusters with GPUs, your project must have sufficient GPU quota.

Your GPU quota should be at least equivalent to the total number of GPUs you intend to run in your cluster. If you enable [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), you should request GPU quota at least equivalent to the number of GPUs per node multiplied by your cluster's maximum number of nodes.

For example, if you create a cluster with three nodes that runs two GPUs per node, your project requires at least six GPU quota.

### Requesting GPU quota

To request GPU quota, use the Google Cloud console. For more information about requesting quotas, refer to [GPU quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) in the Compute Engine documentation.

To search for GPU quota and submit a quota request, use the Google Cloud console:

  1. Go to the IAM & Admin **Quotas** page in the Google Cloud console.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the **Filter** box, do the following:

     1. Select the **Quota** property, enter the name of the [GPU model](https://docs.cloud.google.com/compute/docs/gpus#nvidia_gpus_for_compute_workloads), and press **Enter**.
     2. (Optional) To apply more advanced filters to narrow the results, select the **Dimensions (for example, locations)** property, add the name of the [region or zone you are using](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones), and press **Enter**.
  3. From the list of GPU quotas, select the quota you want to change.

  4. Click **Edit Quotas**. A request form opens.

  5. Fill the **New quota limit** field for each quota request.

  6. Fill the **Request description** field with details about your request.

  7. Click **Next**.

  8. In the **Override confirmation** dialog, click **Confirm**.

  9. In the **Contact details** screen, enter your name and a phone number that the approvers might use to complete your quota change request.

  10. Click **Submit request**.

  11. You receive a confirmation email to track the quota change.




## Running GPUs in GKE Standard clusters

**Caution:** NVIDIA P100 GPUs reach end of support on September 15, 2026. For more information, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos). 

To run GPUs in GKE Standard clusters, create a node pool with attached GPUs.

**Best practice** : 

To improve cost-efficiency, reliability, and availability of GPUs on GKE, perform the following actions:

  * Create separate GPU node pools. For each node pool, limit the node location to the zones where the GPUs you want are available.
  * Enable autoscaling in each node pool.
  * Use regional clusters to improve availability by replicating the Kubernetes control plane across zones in the region.
  * Configure GKE to automatically install either the default or latest GPU drivers on the node pools so that you don't need to manually install and manage your driver versions.



As described in the following sections, GKE uses node taints and tolerations to ensure that Pods are not scheduled onto inappropriate nodes.

### Taint a GPU node pool to avoid scheduling it inappropriately

A node taint lets you mark a node so that the scheduler avoids or prevents using it for certain Pods. Based on the following scenarios, GKE automatically adds the `nvidia.com/gpu=present:NoSchedule` taint, or you can manually add it:

  * When you add a GPU node pool to an existing cluster that already runs a non-GPU node pool, GKE automatically [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) the GPU nodes with the following node taint:

    * **Key** : `nvidia.com/gpu`
    * **Value** : `present`
    * **Effect** : `NoSchedule`

GKE only adds this taint if there is at least one non-GPU node pool in the cluster.

  * When you add a GPU node pool to a cluster that has only GPU node pools, or if you create a new cluster where the default node pool has GPUs attached, you can [manually set taints to the new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#taint-label-node-pool) with the following values:

    * **Key** : `nvidia.com/gpu`
    * **Value** : `present`
    * **Effect** : `NoSchedule`
  * When you add a non-GPU node pool to the cluster in the future, GKE does _not_ retroactively apply this taint to existing GPU nodes. You need to [manually set taints to the new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#taint-label-node-pool).




### Automatically restricting scheduling with a toleration

Tolerations let you designate Pods that can be used on "tainted" nodes. GKE automatically applies a toleration so only Pods requesting GPUs are scheduled on GPU nodes. This enables more efficient autoscaling as your GPU nodes can quickly scale down if there are not enough Pods requesting GPUs. To do this GKE runs the [ExtendedResourceToleration](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#extendedresourcetoleration) admission controller.

### Create a GPU node pool

To create a separate GPU node pool in an existing cluster, you can use the Google Cloud console or the Google Cloud CLI. You can also use Terraform for provisioning your GKE clusters and GPU node pool.

GKE supports automatic installation of NVIDIA drivers in the following scenarios:

  * For GKE clusters with control plane version 1.32.2-gke.1297000 and later, GKE automatically installs the default NVIDIA driver version for all GPU nodes, including those created with node auto-provisioning.
  * For GKE clusters with control plane version 1.30.1-gke.1156000 to 1.32.2-gke.1297000, GKE automatically installs the default NVIDIA driver version for nodes not created with node auto-provisioning.
  * You can optionally choose the latest available driver version or explicitly disable automatic driver installation. In versions earlier than 1.30.1-gke.1156000, GKE doesn't install a driver by default if you don't specify a driver version when you create or update the node pool.

**Caution:** If you use [automatic node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades), a GKE version upgrade might install a newer GPU driver version on the nodes. If your workloads require a specific NVIDIA driver version, you might experience disruptions due to incompatibilities. Test new GKE versions for compatibility in a staging environment before automatic upgrades change the version on your production GPU nodes, or disable automatic upgrades in those node pools.

### gcloud

To create a node pool with GPUs in a cluster, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
      --accelerator type=GPU_TYPE,count=AMOUNT,gpu-driver-version=DRIVER_VERSION \
      --machine-type MACHINE_TYPE \
      --cluster CLUSTER_NAME \
      --location CONTROL_PLANE_LOCATION \
      --node-locations COMPUTE_ZONE1[,COMPUTE_ZONE2] \
      [--sandbox=type=gvisor]
      [--enable-autoscaling \
       --min-nodes MIN_NODES \
       --max-nodes MAX_NODES] \
      [--scopes=SCOPES] \
      [--service-account=SERVICE_ACCOUNT] \
      [--reservation-affinity=specific --reservation=RESERVATION_NAME]
    

Replace the following:

  * `POOL_NAME`: the name you choose for the node pool.
  * `GPU_TYPE`: The type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you use. For example, `nvidia-tesla-t4`.
  * `AMOUNT`: the number of GPUs to attach to nodes in the node pool. Set this number to the GPU count of the machine type. For example, if you set `MACHINE_TYPE` to `g4-standard-384`, set the `AMOUNT` to `8`, which is the number of GPUs attached to that machine type. However, if you use a [G4 machine type](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that has less than one GPU, you must set `AMOUNT` to `1`. This is necessary for when you set `GPU_TYPE` to `nvidia-rtx-pro-6000` and `MACHINE_TYPE` to one of the following:

    * `g4-standard-6` (one-eighth of a GPU)
    * `g4-standard-12` (one-quarter of a GPU)
    * `g4-standard-24` (one-half of a GPU)
    * `g4-standard-48` (one GPU)

Additionally, for clusters running GKE versions earlier than 1.36, ensure that you follow the instructions to prepare workloads for G4 machine types that have less than one GPU.

  * `DRIVER_VERSION`: the NVIDIA driver version to install. Can be one of the following:

    * `default`: Install the default driver version for your node GKE version. In GKE version 1.30.1-gke.1156000 and later, if you omit the `gpu-driver-version` flag, this is the default option. In earlier versions, GKE doesn't install a driver if you omit this flag.
    * `latest`: Install the latest available driver version for your GKE version. Available only for nodes that use Container-Optimized OS.
    * `disabled`: Skip automatic driver installation. You **must** manually install a driver after you create the node pool. In GKE versions earlier than 1.30.1-gke.1156000, this is the default option.

The `gpu-driver-version` option is only available for GKE version 1.27.2-gke.1200 and later. In earlier versions, omit this flag and manually install a driver after you create the node pool. If you upgrade an existing cluster or node pool to this version or later, GKE automatically installs the default driver version that corresponds to the GKE version, unless you specify differently when you start the upgrade.

**Note:** To create a node pool with Ubuntu nodes and NVIDIA L4 GPUs or NVIDIA H100 GPUs and automatically install the default NVIDIA driver version, you must use a [minimum GKE patch version or later](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus#driver-installation-fails-ubuntu). For earlier versions, you must specify `gpu-driver-version=disabled` and manually install the NVIDIA driver.
  * `MACHINE_TYPE`: the Compute Engine machine type for the nodes. Required for the following GPU types:

    * NVIDIA B200 GPUs (corresponding to the `nvidia-b200` accelerator type and [A4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms))
    * NVIDIA H200 141 GB GPUs (corresponding to the `nvidia-h200-141gb` accelerator type and [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine type), or NVIDIA H100 80 GB GPUs (corresponding to the `nvidia-h100-80gb` accelerator type and [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) machine type), or NVIDIA H100 80GB Mega GPUs (corresponding to the `nvidia-h100-mega-80gb` accelerator type and [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) machine type). For more information, see [the A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) in the Compute Engine documentation.
    * NVIDIA A100 40 GB GPUs (corresponding to `nvidia-tesla-a100` accelerator type and the [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) machine type), or NVIDIA A100 80GB GPUs (corresponding to the `nvidia-a100-80gb` accelerator type and [A2 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) machine type). For more information, see [the A2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) in the Compute Engine documentation.
    * NVIDIA L4 GPUs (corresponding to the `nvidia-l4` accelerator type and the [G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)).
    * NVIDIA RTX PRO 6000 GPUs (corresponding to the `nvidia-rtx-pro-6000` accelerator type and the [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)).

For all other GPUs, this flag is optional.

  * `CLUSTER_NAME`: the name of the cluster in which to create the node pool.

  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

  * `COMPUTE_ZONE1,COMPUTE_ZONE2,[...]`: the specific [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) where GKE creates the GPU nodes. The zones must be in the same region as the cluster, specified by the `--location` flag. The GPU types that you define must be available in each selected zone. If you use a reservation, you must specify the zones where the reservation has capacity. We recommend that you always use the `--node-locations` flag when creating the node pool to specify the zone or zones that contain the requested GPUs.

  * Optionally, you can create node pools to run sandboxed workloads with gVisor. To learn more, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) for details.

  * `MIN_NODES`: the minimum number of nodes for each zone in the node pool at any time. This value is relevant only if the `--enable-autoscaling` flag is used.

  * `MAX_NODES`: the maximum number of nodes for each zone in the node pool at any time. This value is relevant only if the `--enable-autoscaling` flag is used.

  * Optionally, you can create the GPU node pool using a custom service account by appending the following flags. If omitted, the node pool uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account):

    * `SERVICE_ACCOUNT`: the name of the IAM service account that your nodes use.
    * `SCOPES`: a comma-separated list of access scopes to grant. Ensure that one of the scopes is `storage-ro` or `https://www.googleapis.com/auth/devstorage.read_only`. To learn more about scopes, see [Setting access scopes](https://docs.cloud.google.com/artifact-registry/docs/access-control#gke-scope). If you omit the _scope_ flag, the GPU node pool creation fails with an **AccessDenied** error **failed to download gpu_driver_versions.bin from GCS bucket**.

**Note:** If you don't use custom IAM service accounts to create your GKE clusters or node pools, ensure that the default Compute Engine service account in your project has the required permissions for GKE. In organizations that enforce the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account won't automatically get the required permissions for GKE. This constraint is enforced by default for organizations that were created on or after May 3, 2024. For details, see [Default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent). 

  * `RESERVATION_NAME`: the name of the GPU reservation to use. Specify the `--reservation` flag with `--reservation-affinity=specific` to use GPU capacity from a specific reservation. For more information, see [Consuming a specific single-project reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#specific).




For example, the following command creates a highly-available autoscaling node pool, `t4`, with two T4 GPUs for each node, in the regional cluster `t4-cluster`. GKE automatically installs the default drivers on those nodes.
    
    
    gcloud container node-pools create t4 \
      --accelerator type=nvidia-tesla-t4,count=2,gpu-driver-version=default \
      --cluster t4-cluster \
      --location us-central1 \
      --node-locations us-central1-c \
      --min-nodes 0 --max-nodes 5 --enable-autoscaling
    

You can also update an existing node pool. For example, you might want to update the GPU driver to switch to the latest available driver:
    
    
    gcloud container node-pools update t4 \
      --accelerator type=nvidia-tesla-t4,count=2,**gpu-driver-version =latest** \
      --cluster t4-cluster \
      --location us-central1
    

### Console

To create a node pool with GPUs:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Optionally, on the **Node pool details** page, select the **Enable autoscaling** checkbox.

  6. Configure your node pool as you want.

  7. From the navigation pane, select **Nodes**.

  8. Under **Machine configuration** , click **GPU**.

  9. Select a **GPU type** and **Number of GPUs** to run on each node.

  10. Read the warning and select **I understand the limitations**.

  11. In the **GPU Driver installation** section, select one of the following methods:

     * **Google-managed** : GKE automatically installs a driver. If you select this option, choose one of the following from the **Version** drop-down: 
       * **Default** : Install the default driver version.
       * **Latest** : Install the latest available driver version.
     * **Customer-managed** : GKE doesn't install a driver. You **must** manually install a compatible driver using the instructions in Installing NVIDIA GPU device drivers.
  12. Click **Create**.




**Note:** If you don't use custom IAM service accounts to create your GKE clusters or node pools, ensure that the default Compute Engine service account in your project has the required permissions for GKE. In organizations that enforce the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account won't automatically get the required permissions for GKE. This constraint is enforced by default for organizations that were created on or after May 3, 2024. For details, see [Default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent). 

### Terraform

You can create a regional cluster with Terraform with GPUs using a [Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine).

  1. Set the Terraform variables by including the following block in the `variables.tf` file:
         
         variable "project_id" {
           default     = PROJECT_ID
           description = "the gcp_name_short project where GKE creates the cluster"
         }
         
         variable "region" {
           default     = CLUSTER_REGION
           description = "the gcp_name_short region where GKE creates the cluster"
         }
         
         variable "zone" {
           default     = "COMPUTE_ZONE"
           description = "the GPU nodes zone"
         }
         
         variable "cluster_name" {
           default     = "CLUSTER_NAME"
           description = "the name of the cluster"
         }
         
         variable "gpu_type" {
           default     = "GPU_TYPE"
           description = "the GPU accelerator type"
         }
         
         variable "gpu_driver_version" {
           default = "DRIVER_VERSION"
           description = "the NVIDIA driver version to install"
         }
         
         variable "machine_type" {
           default = "MACHINE_TYPE"
           description = "The Compute Engine machine type for the VM"
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `CLUSTER_NAME`: the name of the GKE cluster.
     * `CLUSTER_REGION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster.
     * `COMPUTE_ZONE`: the specific [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where GKE creates the GPU nodes. The zone must be in the same region specified by the `region` variable. These zones must have the GPU types you defined available. For more information, see Availability of GPUs by regions and zones.
     * `GPU_TYPE`: The type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you use. For example, `nvidia-tesla-t4`.
     * `DRIVER_VERSION`: the GPU driver version for GKE to automatically install. This field is optional. The following values are supported:

       * `INSTALLATION_DISABLED`: Disable automatic GPU driver installation. You **must** manually install drivers to run your GPUs. In GKE versions earlier than 1.30.1-gke.1156000, this is the default option if you omit this field.
       * `DEFAULT`: Automatically install the default driver version for your node operating system version. In GKE version 1.30.1-gke.1156000 and later, if you omit this field, this is the default option. In earlier versions, GKE doesn't install a driver if you omit this field.
       * `LATEST`: Automatically install the latest available driver version for your node OS version. Available only for nodes that use Container-Optimized OS.

If you omit this field, GKE doesn't automatically install a driver. This field isn't supported in node pools that use node auto-provisioning. To manually install a driver, see Manually install NVIDIA GPU drivers in this document.

     * `MACHINE_TYPE`: the Compute Engine machine type for the nodes. Required for the following GPU types:

       * NVIDIA B200 GPUs (corresponding to the `nvidia-b200` accelerator type and [A4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms))
       * NVIDIA H200 141 GB GPUs (corresponding to the `nvidia-h200-141gb` accelerator type and [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine type), or NVIDIA H100 80 GB GPUs (corresponding to the `nvidia-h100-80gb` accelerator type and [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) machine type), or NVIDIA H100 80GB Mega GPUs (corresponding to the `nvidia-h100-mega-80gb` accelerator type and [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) machine type). For more information, see [the A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) in the Compute Engine documentation.
       * NVIDIA A100 40 GB GPUs (corresponding to the `nvidia-tesla-a100` accelerator type and the [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) machine type), or NVIDIA A100 80GB GPUs (corresponding to the `nvidia-a100-80gb` accelerator type and [A2 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) machine type). For more information, see [the A2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) in the Compute Engine documentation.
       * NVIDIA L4 GPUs (corresponding to the `nvidia-l4` accelerator type and the [G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)).
       * NVIDIA RTX PRO 6000 GPUs (corresponding to the `nvidia-rtx-pro-6000` accelerator type and the [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)).

For all other GPUs, this flag is optional.

  2. Add the following block to your Terraform configuration:
         
         provider "google" {
           project = var.project_id
           region  = var.region
         }
         
         resource "google_container_cluster" "ml_cluster" {
           name               = var.cluster_name
           location           = var.region
           initial_node_count = 1
         }
         
         resource "google_container_node_pool" "gpu_pool" {
           name           = google_container_cluster.ml_cluster.name
           location       = var.region
           node_locations = [var.zones]
           cluster        = google_container_cluster.ml_cluster.name
           node_count     = 3
         
           autoscaling {
             total_min_node_count = "1"
             total_max_node_count = "5"
           }
         
           management {
             auto_repair  = "true"
             auto_upgrade = "true"
           }
         
           node_config {
             oauth_scopes = [
               "https://www.googleapis.com/auth/logging.write",
               "https://www.googleapis.com/auth/monitoring",
               "https://www.googleapis.com/auth/devstorage.read_only",
               "https://www.googleapis.com/auth/trace.append",
               "https://www.googleapis.com/auth/service.management.readonly",
               "https://www.googleapis.com/auth/servicecontrol",
             ]
         
             labels = {
               env = var.project_id
             }
         
             guest_accelerator {
               type  = var.gpu_type
               count = 1
               gpu_driver_installation_config {
                 gpu_driver_version = var.gpu_driver_version
               }
             }
         
             image_type   = "cos_containerd"
             machine_type = var.machine_type
             tags         = ["gke-node", "${var.project_id}-gke"]
         
             disk_size_gb = "30"
             disk_type    = "pd-standard"
         
             metadata = {
               disable-legacy-endpoints = "true"
             }
           }
         }
         




Terraform calls Google Cloud APIs to set create a new cluster with a node pool that uses GPUs. The node pool initially has three nodes and autoscaling is enabled. To learn more about Terraform, see the [`google_container_node_pool` resource spec on terraform.io](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster).

**Best practice** : 

To avoid incurring further costs, remove all the resources defined in the configuration file by using the `terraform destroy` command.

**Best practice** : You can also create a new cluster with GPUs and specify zones using the [`--node-locations`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-locations) flag. However, we recommend that you create a separate GPU node pool in an existing cluster, as shown in this section.

### Manually install NVIDIA GPU drivers

You can manually install NVIDIA GPU drivers on your nodes by deploying an installation DaemonSet to those nodes. Use manual installation in the following situations:

  * You chose to disable automatic device driver installation when you created a GPU node pool.
  * You use a GKE version earlier than the minimum supported version for automatic installation.
  * Your workload requires a specific NVIDIA driver version that isn't available as the default or the latest driver with automatic installation. For example, using GPUs with Confidential GKE Nodes.

**Best practice** : 

Use automatic driver installation whenever possible. To do this, specify the `gpu-driver-version` option in the `--accelerator` flag when you create your Standard cluster. If you used the installation DaemonSet to manually install GPU drivers **on or before January 25, 2023** , you might need to re-apply the DaemonSet to get a version that ignores nodes that use automatic driver installation.

To run the installation DaemonSet, the GPU node pool requires the `https://www.googleapis.com/auth/devstorage.read_only` scope for communicating with [Cloud Storage](https://docs.cloud.google.com/storage). Without this scope, downloading of the installation DaemonSet manifest fails. This scope is one of the default [scopes](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--scopes), which is typically added when you create the cluster.

The following instructions show you how to install the drivers on Container-Optimized OS (COS) and Ubuntu nodes, and using Terraform.

### COS

  * To deploy the installation [DaemonSet](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml) and install the default GPU driver version, run the following command:
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml
        

  * To install a newer GPU driver version from the driver version table in this section, run the following command:
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded-latest.yaml
        

  * To install a GPU driver version that supports [running GPU workloads on Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes), run the following command:
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/nvidia-driver-installer/cos/daemonset-confidential.yaml
        




The installation takes several seconds to complete. After the installation completes, the NVIDIA GPU device plugin uses the Kubernetes API to make the NVIDIA GPU capacity available.

Each version of Container-Optimized OS has at least one supported NVIDIA GPU driver version. For more information about mapping the GPU driver version to GKE version, you can do any of the following:

  * Map the GKE version and Container-Optimized OS node image version to the GPU driver version.
  * Use the following table which lists the available GPU driver versions in each GKE version:

GKE NVIDIA driver versions  
---  
1.33 | R535 (default), R570, R575, or R580  
1.32 | R535 (default), R570, R575, or R580  
1.31 | R535 (default), R570, R575, or R580  
1.30 | R535 (default) or R550  
1.29 | R535 (default) or R550  
1.28 | R535 (default) or R550  
1.27 | R470 (default), R525, R535, or R550  
1.26 | R470 (default), R525, R535, or R550  
  
### Ubuntu

The installation DaemonSet that you deploy depends on the GPU type and on the GKE node version as follows:

  * For all GPUs **except** NVIDIA H200 GPUs, run the following command:
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/ubuntu/daemonset-preloaded.yaml
        

  * For NVIDIA H200 GPUs, install the `R550` driver:
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/nvidia-driver-installer/ubuntu/daemonset-preloaded-R550.yaml
        




The installation takes several seconds to complete. Once installed, the NVIDIA GPU device plugin uses the Kubernetes API to make the NVIDIA GPU capacity available.

The following table lists the available driver versions in each GKE version:

Ubuntu GPU drivers and GKE versions |  | 1.33 | R535 (default)  
---|---  
1.32 | R535 (default)  
1.31 | R535 (default)  
1.30 | R470 or R535  
1.29 | R470 or R535  
1.28 | R470 or R535  
1.27 | R470 or R535  
1.26 | R470 or R535  
  
### Terraform

You can use Terraform to install the default GPU driver version based on the type of nodes. In both cases, you must configure the [`kubectl_manifest` Terraform resource type](https://registry.terraform.io/providers/alekc/kubectl/latest/docs/resources/kubectl_manifest).

  * To install the [DaemonSet on COS](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml), add the following block in your Terraform configuration:
        
        data "http" "nvidia_driver_installer_manifest" {
            url = "https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml"
          }
        
          resource "kubectl_manifest" "nvidia_driver_installer" {
            yaml_body = data.http.nvidia_driver_installer_manifest.body
          }
        

  * To install [DaemonSet on Ubuntu](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/ubuntu/daemonset-preloaded.yaml), add the following block in your Terraform configuration:
        
        data "http" "nvidia_driver_installer_manifest" {
            url = "https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/ubuntu/daemonset-preloaded.yaml"
          }
        
          resource "kubectl_manifest" "nvidia_driver_installer" {
            yaml_body = data.http.nvidia_driver_installer_manifest.body
          }
        




### Map the GKE version and Container-Optimized OS node image version to the GPU driver version

To find the GPU driver versions that are mapped with [GKE versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) and Container-Optimized OS node image versions, do the following steps: 

  1. [Map Container-Optimized OS node image versions to GKE patch versions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#map-gke-cos) for the specific GKE version where you want to find the GPU driver version. For example, 1.33.0-gke.1552000 uses cos-121-18867-90-4. 
  2. Choose the milestone of the Container-Optimized OS node image version in the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). For example, choose Milestone 121 for cos-121-18867-90-4. 
  3. In the release notes page for the specific milestone, find the release note corresponding with the specific Container-Optimized OS node image version. For example, in [Container-Optimized OS Release Notes: Milestone 121](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121), see [cos-121-18867-90-4](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-90-4_). In the table in the **GPU Drivers** column, click **See List** to see the GPU driver version information. 



In GKE version 1.36.0-gke.3302004 and later, GKE automatically publishes the installed NVIDIA driver version as annotations on running GPU nodes. To view the driver version annotations on a GPU node, run the following command:
    
    
    kubectl get node GPU_NODE_NAME -o jsonpath='{.metadata.annotations}'

Replace `GPU_NODE_NAME` with the name of your GPU node.

The output includes annotations similar to the following:
    
    
    {
      "cloud.google.com/cuda.driver-version.full": "580.126.20",
      "cloud.google.com/cuda.driver-version.major": "580",
      "cloud.google.com/cuda.driver-version.minor": "126",
      "cloud.google.com/cuda.driver-version.revision": "20"
    }
    

## Installing drivers using node auto-provisioning with GPUs

When you use node auto-provisioning with GPUs, by default the auto-provisioned node pools don't have sufficient scopes to install the drivers. To grant the required scopes, modify the default scopes for node auto-provisioning to add `logging.write`, `monitoring`, `devstorage.read_only`, and `compute`, such as in the following example.
    
    
    gcloud container clusters update CLUSTER_NAME --enable-autoprovisioning \
        --min-cpu=1 --max-cpu=10 --min-memory=1 --max-memory=32 \
        --autoprovisioning-scopes=https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/compute
    

For clusters running GKE version 1.32.2-gke.1297000 and later, GKE automatically installs the default NVIDIA driver version for all GPU nodes, including those created with node auto-provisioning. You can skip the following instructions for clusters running GKE version 1.32.2-gke.1297000 and later.

In GKE version 1.29.2-gke.1108000 and later, you can select a GPU driver version for GKE to automatically install in auto-provisioned GPU nodes. Add the following field to your manifest:
    
    
    spec:
      nodeSelector:
        cloud.google.com/gke-gpu-driver-version: "DRIVER_VERSION"
    

Replace `DRIVER_VERSION` with one of the following values:

  * `default`: the default, stable driver for your node GKE version.
  * `latest`: the latest available driver version for your node GKE version.
  * `disabled`: disable automatic GPU driver installation. With this value selected, you must manually install drivers to run your GPUs. In GKE versions earlier than 1.32.2-gke.1297000, this is the default option if you omit the node selector.



To learn more about auto-provisioning, see [Using node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

## Configuring Pods to consume GPUs

You use a [resource limit](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) to configure Pods to consume GPUs. You specify a resource limit in a [Pod specification](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#podspec-v1-core) using the following key-value pair

  * **Key** : `nvidia.com/gpu`
  * **Value** : Number of GPUs to consume



`alpha.kubernetes.io/nvidia-gpu` is not supported as a resource name in GKE. Use `nvidia.com/gpu` as the resource name instead.

The following manifest is an example of a Pod specification that consumes GPUs:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-gpu-pod
    spec:
      # Optional: Use GKE Sandbox
      # runtimeClassName: gvisor
      containers:
      - name: my-gpu-container
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        resources:
          limits:
           nvidia.com/gpu: 2
    

**Note:** If you run the workload with GKE Sandbox, you need to create a GKE Sandbox node pool. For details, see [Enable GKE Sandbox on a new Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enabling-new).

## Consuming multiple GPU types

If you want to use multiple GPU accelerator types per cluster, you must create multiple node pools, each with their own accelerator type. GKE attaches a unique [node selector](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) to GPU nodes to help place GPU workloads on nodes with specific GPU types:

  * **Key** : `cloud.google.com/gke-accelerator`
  * **Value** : The type of [GPU accelerator](https://docs.cloud.google.com/compute/docs/gpus) that you use. For example, `nvidia-tesla-t4`.



You can target particular GPU types by adding this node selector to your workload Pod specification. For example:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-gpu-pod
    spec:
      containers:
      - name: my-gpu-container
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        resources:
          limits:
           nvidia.com/gpu: 2
      nodeSelector:
        cloud.google.com/gke-accelerator: nvidia-tesla-t4
    

## Upgrade node pools using accelerators (GPUs and TPUs)

GKE [automatically upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically) Standard clusters, including node pools. You can also [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) node pools if you want your nodes on a later version sooner. To control how upgrades work for your cluster, use [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), and [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).

You can also configure a [node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) for your node pool, such as [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) , [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) or [short-lived upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#short-lived-upgrades-flex-start). By configuring these strategies, you can ensure that the node pools are upgraded in a way that achieves the optimal balance between speed and disruption for your environment. For [multi-host TPU slice node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#multi-host), instead of using the configured node upgrade strategy, GKE atomically recreates the entire node pool in a single step. To learn more, see the definition of _atomicity_ in [Terminology related to TPU in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology).

Using a node upgrade strategy temporarily requires GKE to provision additional resources, depending on the configuration. If Google Cloud has limited capacity for your node pool's resources—for example, you're seeing [resource availability](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability) errors when trying to create more nodes with GPUs or TPUs—see [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

## About the NVIDIA CUDA-X libraries

**Note:** To use CUDA with [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU with clusters running GKE versions earlier than 1.36, you must follow the instructions in the next section.

[CUDA](https://developer.nvidia.com/cuda-zone) is NVIDIA's parallel computing platform and programming model for GPUs. To use CUDA applications, the image that you use must have the libraries. To add the NVIDIA CUDA-X libraries, you can build and use your own image by including the following values in the `LD_LIBRARY_PATH` environment variable in your container specification: 

  * `/usr/local/nvidia/lib64`: the location of the NVIDIA device drivers.
  * `/usr/local/cuda-CUDA_VERSION/lib64`: the location of the NVIDIA CUDA-X libraries on the node. 

Replace `CUDA_VERSION` with the CUDA-X image version that you used. Some versions also contain debug utilities in `/usr/local/nvidia/bin`. For details, see [the NVIDIA CUDA image on DockerHub](https://hub.docker.com/r/nvidia/cuda).

To check the minimum GPU driver version required for your version of CUDA, see [CUDA Toolkit and Compatible Driver Versions](https://docs.nvidia.com/deploy/cuda-compatibility/index.html#binary-compatibility__table-toolkit-driver).


Ensure that the GKE patch version running on your nodes includes a GPU driver version that's compatible with your chosen CUDA version. For more information about mapping the GPU driver version to GKE version, see [Map the GKE version and Container-Optimized OS node image version to the GPU driver version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#map-gke-cos-gpu). 

## Monitor your GPU node workload performance

If your GKE cluster has [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics) enabled, then the following metrics are available in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor your GPU workload performance: 

  * **Duty Cycle (`container/accelerator/duty_cycle`): ** Percentage of time over the past sample period (10 seconds) during which the accelerator was actively processing. Between 1 and 100. 
  * **Memory Usage (`container/accelerator/memory_used`): ** Amount of accelerator memory allocated in bytes. 
  * **Memory Capacity (`container/accelerator/memory_total`): ** Total accelerator memory in bytes. 



These metrics apply at the container level (`container/accelerator`) and are not collected for containers scheduled on a GPU that uses GPU time-sharing or NVIDIA MPS. 

You can use predefined dashboards to monitor your clusters with GPU nodes. For more information, see [ View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). For general information about monitoring your clusters and their resources, refer to [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability). 

### View usage metrics for workloads

You view your workload GPU usage metrics from the **Workloads** dashboard in the Google Cloud console. 

To view your workload GPU usage, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)
  2. Select a workload.



The Workloads dashboard displays charts for GPU memory usage and capacity, and GPU duty cycle. 

### View NVIDIA Data Center GPU Manager (DCGM) metrics

You can collect and visualize NVIDIA DCGM metrics by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus). For Autopilot clusters, GKE installs the drivers. For Standard clusters, you must install the NVIDIA drivers. 

For instructions on how to deploy the GKE-managed DCGM package, see [Collect and view NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics). 

### JobSet and node health metrics for GPU workloads

In addition to DCGM metrics, you can use the following metrics to monitor the health and performance of your GPU workloads, especially when running them as JobSets. 

#### JobSet metrics

The following metrics apply to both GPU and TPU JobSets that have a single replicated Job: 

  * `kubernetes.io/jobset/times_between_interruptions`
  * `kubernetes.io/jobset/times_to_recover`
  * `kubernetes.io/jobset/uptime`



For more information about these system metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). 

You can also use the **JobSet dashboard** in the Google Cloud console to visualize and monitor your GPU workloads:

[Go to Deployments](https://console.cloud.google.com//kubernetes/aiml/deployments/jobs)

#### Node health metrics

The following node-level metrics apply to all nodes, including those with GPUs:

  * `kubernetes.io/node/status_condition`: This metric requires GKE version 1.32.1-gke.1357001 or later. 



Node interruption and node pool interruption metrics also apply to non-TPU nodes.

#### Kube-state-metrics for JobSets

The kube-state-metrics for JobSets can be used with GPUs. Collection of these metrics requires GKE version 1.32.1-gke.1357001 or later. For more information, see the [JobSet metrics documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics). 

## Prepare workloads for G4 machine types that have less than one GPU

To run workloads with CUDA on G4 machine types that have less than one GPU with clusters running GKE versions earlier than 1.36, deploy the NRI device injector as a DaemonSet and add annotations to your containers. The following steps show you how to deploy the DaemonSet and configure your Pods:

  1. Create the DaemonSet:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/nri_device_injector/nri-device-injector.yaml
         

  2. Add the following annotation to your Pod specification:
         
         devices.gke.io/container.CONTAINER_NAME:
           - path: /dev/nvidia-caps/nvidia-cap1
           - path: /dev/nvidia-caps/nvidia-cap2
           - path: /dev/nvidia-caps/nvidia-cap3
           - path: /dev/nvidia-caps/nvidia-cap4
         

Replace `CONTAINER_NAME` with the name of the Pod's container.


**Caution:** You could also use a privileged container, but this approach creates a security risk.

## Configure graceful termination of GPU nodes

In GKE clusters with the control plane running 1.29.1-gke.1425000 or later, GPU nodes support `SIGTERM` signals that alert the node of an imminent shutdown. The imminent shutdown notification is configurable up to _60_ minutes in GPU nodes.

To configure GKE to terminate your workloads gracefully within this notification timeframe, follow the steps in [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## What's next

  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * [Learn how to use a minimum CPU platform for your nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform).
  * [Learn how to create and set up a local deep learning container with Docker](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local).
  * [Learn how to use Confidential GKE Nodes in your GPU node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes) ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * [Learn about sandboxing GPU workloads with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
