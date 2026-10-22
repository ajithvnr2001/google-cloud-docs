---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster/
title: Create a self-managed Slurm cluster for AI workloads \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:50.892606+00:00
---

# Create a self-managed Slurm cluster for AI workloads  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create a self-managed Slurm cluster for AI workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to configure and deploy a self-managed Slurm cluster that uses A4X Max, A4X, A4, A3 Ultra, A3 Mega, or A3 High machine types. To learn more about these accelerator-optimized machine types, see [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).

The steps in this document show you how to create a Slurm cluster by using Cluster Toolkit. [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) is an open-source tool from Google that simplifies the configuration and deployment of a cluster by using blueprints. You have full control over your cluster, but you're also responsible for managing it. If you want to avoid the overhead of managing a cluster and focus on running your workload, then [create a fully managed cluster by using Cluster Director](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster).

## Limitations

Depending on the machine type that the Compute Engine instances in your cluster use, the following limitations apply:

###  A4X Max 

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X Max machine series.

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X Max. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * A4X Max instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X Max machine types.



###  A4X 

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X machine series.

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * For A4X instances, when you use `ethtool -S` to monitor GPU networking, the physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * A4X instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X machine types.



###  A4 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A4 machine type.
  * You can only use an A4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A4 machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * You can't change the machine type of an instance to or from A4 machine type. You must create a new instance with this machine type.
  * A4 machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * You can't run Windows operating systems on an A4 machine type.
  * For A4 instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to A4 machine types.



###  A3 Ultra 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Ultra machine type.
  * You can only use an A3 Ultra machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A3 Ultra machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Ultra machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Ultra machine type.
  * A3 Ultra machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * For A3 Ultra instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).



###  A3 Mega 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Mega machine type.
  * You can only use an A3 Mega machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Mega machine type.
  * The A3 Mega machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Mega machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Mega machine type.



###  A3 High 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 High machine type.
  * You can only use an A3 High machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 High machine type.
  * The A3 High machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 High machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 High machine type.
  * For `a3-highgpu-1g`, `a3-highgpu-2g`, and`a3-highgpu-4g` machine types, you must create instances by using Spot VMs or Flex-start VMs. For detailed instructions on these options, review the following: 
    * To create Spot VMs, set the provisioning model to `SPOT` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
    * To create Flex-start VMs, you can use one of the following methods: 
      * Create a standalone VM and set the provisioning model to `FLEX_START` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
      * Create a resize request in a managed instance group (MIG). For instructions, see [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with an `a3-highgpu-1g` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1), and all the [limitations for Confidential VM running on the A3 High machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.



## Before you begin

Before creating a Slurm cluster, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). **Note:** When you request A4X Max or A4X capacity, you obtain it in the _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max or A4X machine types. For more information about all capacity mode, see [ Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode). 
  3. **Verify that you have enough Filestore capacity quota** : you need to have enough Filestore quota in your target region before deploying. The required minimum capacity depends on the machine types in your cluster: 
     * **A4X Max, A4X, A4, A3 Ultra, and A3 Mega** : requires a minimum of 10 TiB (10,240 GiB) of HIGH_SCALE_SSD (zonal) capacity.
     * **A3 High** : requires a minimum of 2.5 TiB (2,560 GiB) of BASIC_SSD (standard) capacity.

To check quota or request a quota increase, see the following:

     * To check quota in your project, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, then [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  4. **Install Cluster Toolkit** : to provision Slurm clusters, you must use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) version `v1.62.0` or later. 

To install Cluster Toolkit, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).




### Required roles

To get the permissions that you need to deploy a Slurm cluster, ask your administrator to grant you the following IAM roles: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on your project
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account itself
  * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
  * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up a storage bucket

Cluster blueprints use Terraform modules to provision Cloud infrastructure. A best practice when working with Terraform is to [store the state remotely](https://developer.hashicorp.com/terraform/language/state/remote) in a version enabled file. On Google Cloud, you can create a Cloud Storage bucket that has versioning enabled.

To create this bucket and enable versioning from the CLI, run the following commands:
    
    
    gcloud storage buckets create gs://BUCKET_NAME \
        --project=PROJECT_ID \
        --default-storage-class=STANDARD --location=BUCKET_REGION \
        --uniform-bucket-level-access
    gcloud storage buckets update gs://BUCKET_NAME --versioning
    

Replace the following:

  * `BUCKET_NAME`: a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
  * `PROJECT_ID`: your project ID.
  * `BUCKET_REGION`: any [available location](https://docs.cloud.google.com/storage/docs/locations#available-locations).



## Install Cluster Toolkit

To use Slurm with Google Cloud, you must install [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). For Linux and macOS, we recommend that you [install the prebuilt bundle](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment#install-bundle).

After you install Cluster Toolkit, go to the directory that contains the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster):

  * If you installed the prebuilt bundle, change into the `gcluster-bundle` directory:
        
        cd gcluster-bundle

  * If you built the binary from source, change into the `cluster-toolkit`:
        
        cd cluster-toolkit

This cluster deployment requires Cluster Toolkit `v1.62.0` or later. To check the current version, run the following command:
        
        ./gcluster --version




## Create a deployment file

Create a deployment file that you can use to specify the Cloud Storage bucket, set names for your network and subnetwork, and set deployment variables such as project ID, region, and zone.

To create a deployment file, follow the steps for your required machine type and consumption option.

###  A4X Max 

To create your deployment file, use a text editor to create a YAML file named `a4xmax-bm-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a4x_max_cluster_size: NUMBER_OF_INSTANCES
      a4x_max_reservation_name: RESERVATION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of A4X Max bare metal instances in your cluster. You can specify any number of instances. However, A4X Max instances are physically interconnected by a [multi-node NVLink system](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html) in groups of 18 instances (72 GPUs) to form an NVLink domain. 

For optimal network performance, we recommend that you specify a value that is a multiple of 18 instances (for example, 18, 36, or 54). When you create an A4X Max cluster, the A4X Max blueprint automatically creates and applies a compact placement policy with a GPU topology of `1x72` for each group of 18 instances. 

  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).



###  A4X 

To create your deployment file, use a text editor to create a YAML file named `a4xhigh-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a4x_cluster_size: NUMBER_OF_INSTANCES
      a4x_reservation_name: RESERVATION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of A4X instances in your cluster. You can specify any number of instances. However, A4X instances are physically interconnected by a [multi-node NVLink system](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html) in groups of 18 instances (72 GPUs) to form an NVLink domain. 

For optimal network performance, we recommend that you specify a value that is a multiple of 18 instances (for example, 18, 36, or 54). When you create an A4X cluster, the A4X blueprint automatically creates and applies a compact placement policy with a GPU topology of `1x72` for each group of 18 instances. For more information about A4X topology, see [A4X fundamentals](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a4x#a4x_fundamentals). 

  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).



###  A4 

The parameters that you need to add to your deployment file depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

To create your deployment file, use a text editor to create a YAML file named `a4high-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a4h_cluster_size: NUMBER_OF_INSTANCES
      a4h_reservation_name: RESERVATION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.
  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).



### Flex-start

To create your deployment file, use a text editor to create a YAML file named `a4high-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a4h_cluster_size: NUMBER_OF_INSTANCES
      a4h_dws_flex_enabled: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



This deployment provisions [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types#overview), which means that the cluster has a set number of nodes at all times. If you want to enable your cluster to autoscale instead, use [`examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml` file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml) and edit the values of `node_count_static` and `node_count_dynamic_max` to match the following:
    
    
          node_count_static: 0
          node_count_dynamic_max: $(vars.a4h_cluster_size)
    

### Spot

To create your deployment file, use a text editor to create a YAML file named `a4high-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a4h_cluster_size: NUMBER_OF_INSTANCES
      a4h_enable_spot_vm: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



###  A3 Ultra 

The parameters that you need to add to your deployment file depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

To create your deployment file, use a text editor to create a YAML file named `a3ultra-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a3u_cluster_size: NUMBER_OF_INSTANCES
      a3u_reservation_name: RESERVATION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.
  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).



### Flex-start

To create your deployment file, use a text editor to create a YAML file named `a3ultra-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a3u_cluster_size: NUMBER_OF_INSTANCES
      a3u_dws_flex_enabled: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



This deployment provisions [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types#overview), which means that the cluster has a set number of nodes at all times. If you want to enable your cluster to autoscale instead, use [`examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml` file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml) and edit the values of `node_count_static` and `node_count_dynamic_max` to match the following:
    
    
          node_count_static: 0
          node_count_dynamic_max: $(vars.a3u_cluster_size)
    

### Spot

To create your deployment file, use a text editor to create a YAML file named `a3ultra-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      a3u_cluster_size: NUMBER_OF_INSTANCES
      a3u_enable_spot_vm: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



###  A3 Mega 

The parameters that you need to add to your deployment file depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

To create your deployment file, create a YAML file named `a3mega-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3mega_cluster_size: NUMBER_OF_INSTANCES
      a3mega_reservation_name: RESERVATION_NAME
      a3mega_partition_name: PARTITION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.
  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).
  * `PARTITION_NAME`: a name for the Slurm partition.



### Flex-start

To create your deployment file, create a YAML file named `a3mega-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3mega_cluster_size: NUMBER_OF_INSTANCES
      a3mega_dws_flex_enabled: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



This deployment provisions [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types#overview), which means that the cluster has a set number of nodes at all times. If you want to enable your cluster to autoscale instead, use [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml` file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml) and edit the values of `node_count_static` and `node_count_dynamic_max` to match the following:
    
    
          node_count_static: 0
          node_count_dynamic_max: $(vars.a3mega_cluster_size)
    

### Spot

To create your deployment file, create a YAML file named `a3mega-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3mega_cluster_size: NUMBER_OF_INSTANCES
      a3mega_enable_spot_vm: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



###  A3 High 

The parameters that you need to add to your deployment file depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you're using for your deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

To create your deployment file, create a YAML file named `a3high-slurm-deployment.yaml` and add the following content.

**Tip:** Alternatively, you can copy and paste the contents of [`examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      tcpx_kernel_login: TCPX_KERNEL_LOGIN
      tcpx_kernel_password: TCPX_KERNEL_PASSWORD
      keyserver_ubuntu_key: KEYSERVER_UBUNTU_KEY
    
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3_static_cluster_size: NUMBER_OF_INSTANCES
      a3_reservation_name: RESERVATION_NAME
      a3_partition_name: PARTITION_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `TCPX_KERNEL_LOGIN`, `TCPX_KERNEL_PASSWORD`, and `KEYSERVER_UBUNTU_KEY`: the technical credentials for A3 High optimized images. These values are supplied to you by your Google Cloud account team. For more information, see Get credentials for GPUDirect-TCPX.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.
  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation).
  * `PARTITION_NAME`: a name for the Slurm partition.



### Flex-start

To create your deployment file, create a YAML file named `a3high-slurm-deployment.yaml` and add the following content.

**Tip:** Alternatively, you can copy and paste the contents of [`examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      tcpx_kernel_login: TCPX_KERNEL_LOGIN
      tcpx_kernel_password: TCPX_KERNEL_PASSWORD
      keyserver_ubuntu_key: KEYSERVER_UBUNTU_KEY
    
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3_static_cluster_size: NUMBER_OF_INSTANCES
      a3_dws_flex_enabled: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `TCPX_KERNEL_LOGIN`, `TCPX_KERNEL_PASSWORD`, and `KEYSERVER_UBUNTU_KEY`: the technical credentials for A3 High optimized images. These values are supplied to you by your Google Cloud account team. For more information, see Get credentials for GPUDirect-TCPX.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



This deployment provisions [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types#overview), which means that the cluster has a set number of nodes at all times. If you want to enable your cluster to autoscale instead, use [`examples/machine-learning/a3-highgpu-8g/a3high-slurm-blueprint.yaml` file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-highgpu-8g/a3high-slurm-blueprint.yaml) and edit the values of `node_count_static` and `node_count_dynamic_max` to match the following:
    
    
          node_count_static: 0
          node_count_dynamic_max: $(vars.a3_static_cluster_size)
    

### Spot

To create your deployment file, create a YAML file named `a3high-slurm-deployment.yaml` and add the following content.

**Tip:** Alternatively, you can copy and paste the contents of [`examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-highgpu-8g/a3high-slurm-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      tcpx_kernel_login: TCPX_KERNEL_LOGIN
      tcpx_kernel_password: TCPX_KERNEL_PASSWORD
      keyserver_ubuntu_key: KEYSERVER_UBUNTU_KEY
    
      network_name_system: SYSTEM_NETWORK_NAME
      subnetwork_name_system: SYSTEM_SUBNET_NAME
      slurm_cluster_name: CLUSTER_NAME
      a3_static_cluster_size: NUMBER_OF_INSTANCES
      a3_enable_spot_vm: true
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `TCPX_KERNEL_LOGIN`, `TCPX_KERNEL_PASSWORD`, and `KEYSERVER_UBUNTU_KEY`: the technical credentials for A3 High optimized images. These values are supplied to you by your Google Cloud account team. For more information, see Get credentials for GPUDirect-TCPX.
  * `SYSTEM_NETWORK_NAME`: the name of the VPC network to use for the system network.
  * `SYSTEM_SUBNET_NAME`: the name of the subnetwork to use for the system network.
  * `CLUSTER_NAME`: a name for your Slurm cluster.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



## Provision a Slurm cluster

Cluster Toolkit provisions the cluster based on the deployment file that you created in the previous step and the default cluster blueprint. To learn about custom images or deploying Slurm with a custom OS image, see [Slurm custom images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#slurm-images).

To provision the cluster, select one of the following options to run the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) for your machine type from the Cluster Toolkit directory. This step takes approximately 20-30 minutes.

###  A4X Max 

**Note:** A4X Max uses the ARM64 architecture and runs on [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances). Any software installed on these nodes must be compatible with that architecture.
    
    
    ./gcluster deploy -d a4xmax-bm-slurm-deployment.yaml examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-blueprint.yaml --auto-approve

###  A4X 

**Note:** A4X uses the ARM64 architecture. Any software installed on these compute instances must be compatible with that architecture.

By default, the cluster blueprint deploys compute instances that use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). These images come preconfigured with specialized drivers and software to run your workloads, including NVIDIA drivers, CUDA, network fabrics, and Slurm agents, which removes the need for manual image building during deployment. To learn more about the prebuilt software packages and configuration tools that you are deploying, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images).
    
    
    ./gcluster deploy -d a4xhigh-slurm-deployment.yaml examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-blueprint.yaml --auto-approve

###  A4 

By default, the cluster blueprint deploys compute instances that use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). These images come preconfigured with specialized drivers and software to run your workloads, including NVIDIA drivers, CUDA, network fabrics, and Slurm agents, which removes the need for manual image building during deployment. To learn more about the prebuilt software packages and configuration tools that you are deploying, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images).
    
    
    ./gcluster deploy -d a4high-slurm-deployment.yaml examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml --auto-approve

###  A3 Ultra 

By default, the cluster blueprint deploys compute instances that use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). These images come preconfigured with specialized drivers and software to run your workloads, including NVIDIA drivers, CUDA, network fabrics, and Slurm agents, which removes the need for manual image building during deployment. To learn more about the prebuilt software packages and configuration tools that you are deploying, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images).
    
    
    ./gcluster deploy -d a3ultra-slurm-deployment.yaml examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml --auto-approve

###  A3 Mega 
    
    
    ./gcluster deploy -d a3mega-slurm-deployment.yaml examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml --auto-approve

###  A3 High 
    
    
    ./gcluster deploy -d a3high-slurm-deployment.yaml examples/machine-learning/a3-highgpu-8g/a3high-slurm-blueprint.yaml --auto-approve

## Connect to the Slurm cluster

To access your cluster, you must login to the Slurm login node. If you encounter errors when you attempt to connect to your node, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).

To connect to the login node in your cluster, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the login node, which name is `DEPLOYMENT_NAME-login-001`.

  3. In the node's row, in the **Connect** column, click **SSH**.




###  gcloud 

To connect to the login node in your cluster, complete the following steps:

  1. To identify the login node, use the following [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list):
         
         gcloud compute instances list \
             --filter="name ~ login" \
             --format "value(name)" \
             --zones=ZONE
         

If the output lists multiple Slurm clusters, then you can identify your login node by the `DEPLOYMENT_NAME` that you specified in the previous steps.

  2. To connect to the login node, use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) with the `--tunnel-through-iap` flag:
         
         gcloud compute ssh LOGIN_NODE \
             --tunnel-through-iap \
             --zone=ZONE
         

Replace the following:

     * `ZONE`: the zone where the node exists.

     * `LOGIN_NODE`: the name of the login node.




## Test network performance on the Slurm cluster

We recommend that you validate the functionality of the provisioned clusters. To do so, use [NCCL tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

## Redeploy the Slurm cluster

If you need to increase the number of compute nodes or add new partitions to your cluster, then you might need to update configurations for your Slurm cluster by redeploying it. If you modified your blueprint to build custom images, then you can speed up the redeployment process by using an existing image from a previous deployment. To avoid the need to create new images when you redeploy a cluster that uses custom images, specify the `--only` flag.

To redeploy the cluster infrastructure (`cluster-env,cluster`) without running any image building modules, do the following:

  1. Connect to the cluster

  2. Based on the machine type that your cluster uses, select one of the following options to redeploy your cluster and its infrastructure:

###  A4X Max 
         
         ./gcluster deploy -d a4xmax-bm-slurm-deployment.yaml examples/machine-learning/a4x-maxgpu-4g-metal/a4xmax-bm-slurm-blueprint.yaml --only cluster-env,cluster --auto-approve -w

###  A4X 
         
         ./gcluster deploy -d a4xhigh-slurm-deployment.yaml examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-blueprint.yaml --only cluster-env,cluster --auto-approve -w

###  A4 
         
         ./gcluster deploy -d a4high-slurm-deployment.yaml examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml --only cluster-env,cluster -w --auto-approve

###  A3 Ultra 
         
         ./gcluster deploy -d a3ultra-slurm-deployment.yaml examples/machine-learning/a3-ultragpu-8g/a3ultra-slurm-blueprint.yaml --only cluster-env,cluster -w --auto-approve

###  A3 Mega 
         
         ./gcluster deploy -d a3mega-slurm-deployment.yaml examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml --only cluster-env,cluster -w --auto-approve

###  A3 High 
         
         ./gcluster deploy -d a3high-slurm-deployment.yaml examples/machine-learning/a3-highgpu-8g/a3high-slurm-blueprint.yaml --only cluster-env,cluster -w --auto-approve




## Destroy the Slurm cluster

By default, the A4X Max, A4X, A4, and A3 Ultra blueprints enable deletion protection on the Filestore instance. To delete the Filestore instance when you destroy the Slurm cluster, disable deletion protection before running the destroy command. For instructions, see [Set or remove deletion protection on an existing instance](https://docs.cloud.google.com/filestore/docs/deletion-protection#setting-or-removing).

**Tip:** To learn how to cleanly destroy infrastructure and for advanced manual deployment instructions, see the `DEPLOYMENT_FOLDER/instructions.txt` file in the cluster.

To destroy your Slurm cluster, complete the following steps:

  1. If you haven't already, disconnect from the cluster .

  2. Before you run the `destroy` command, navigate to the root of the Cluster Toolkit directory.

  3. To destroy the cluster, run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy DEPLOYMENT_FOLDER --auto-approve

Replace `DEPLOYMENT_FOLDER` with the name of the deployment folder.




When Cluster Toolkit destroys your cluster, the output is similar to the following:
    
    
    Destroy complete! Resources: DEPLOYMENT_NAME destroyed.
    

## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View the topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * Learn how to manage host events: 
    * [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)
    * [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)
  * [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Test and optimize with NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
