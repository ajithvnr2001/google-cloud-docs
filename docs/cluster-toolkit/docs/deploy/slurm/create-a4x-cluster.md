---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-cluster/
title: Create an A4X Slurm cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:56.862747+00:00
---

# Create an A4X Slurm cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create an A4X Slurm cluster Stay organized with collections  Save and categorize content based on your preferences. 

In this guide, you create and deploy AI-optimized Slurm clusters that use A4X machine types on Google Cloud. These clusters help you run high performance machine learning (ML) training and high performance computing (HPC) workloads. The A4X machine series, an exascale platform, incorporates NVIDIA GB200 Grace Blackwell Superchips. For more details on the A4X series, see [A4X Max and A4X machine series](https://docs.cloud.google.com/compute/docs/gpus#a4x-series).

## A4X limitations

The following limitations apply to A4X instances in your Slurm cluster:

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



## Before you begin

Before creating a Slurm cluster, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). **Note:** When you request A4X Max or A4X capacity, you obtain it in the _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max or A4X machine types. For more information about all capacity mode, see [ Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode). 
  3. **Verify that you have enough Filestore capacity quota** : you need to have enough Filestore quota in your target region before deploying. The required minimum capacity depends on the machine types in your cluster: 
     * **A4X** : requires a minimum of 10 TiB (10,240 GiB) of HIGH_SCALE_SSD (zonal) capacity.

To check quota or request a quota increase, see the following:

     * To check quota in your project, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, then [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  4. **Install Cluster Toolkit** : to provision Slurm clusters, you must use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) version `v1.62.0` or later. 

To install Cluster Toolkit, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).




In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

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



## Open the Cluster Toolkit directory

To use Slurm with Google Cloud, you must [install Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment). After you install Cluster Toolkit, verify that you are in the Cluster Toolkit directory by running the following command:
    
    
    cd cluster-toolkit

This cluster deployment requires Cluster Toolkit `v1.62.0` or later. To check your version, you can run the following command:
    
    
    ./gcluster --version

## Create a deployment file

Create a deployment file that you can use to specify the Cloud Storage bucket, set names for your network and subnetwork, and set deployment variables such as project ID, region, and zone.

To create a deployment file, follow the steps for your required machine type and consumption option.

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



## Provision a Slurm cluster

Cluster Toolkit provisions the cluster based on the deployment file that you created in the previous step and the default cluster blueprint. By default, the turnkey cluster blueprints deploy compute instances that use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). These images come preconfigured with specialized drivers and software to run your workloads, including NVIDIA drivers, CUDA, network fabrics, and Slurm agents, which removes the need for manual image building during deployment.

To learn more about the prebuilt software packages and configuration tools that you are deploying, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). To learn about custom images or deploying Slurm with a custom OS image, see [Slurm custom images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#slurm-images).

To provision the cluster, use the [`./gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) for your machine type from the Cluster Toolkit directory. This process can take about 20 to 30 minutes.
    
    
    ./gcluster deploy -d a4xhigh-slurm-deployment.yaml examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-blueprint.yaml

**Note:** A4X uses the ARM64 architecture, so any software installed on these compute instances must be compatible with that architecture.

## Connect to the Slurm cluster

To access your cluster, you must sign in to the Slurm login node. To sign in, you can use either Google Cloud console or Google Cloud CLI.

###  Console 

  1. Go to the **Compute Engine** > **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the login node. The node has a name with the pattern `DEPLOYMENT_NAME` +`login-001`.

  3. From the **Connect** column of the login node, click **SSH**.




###  gcloud 

To connect to the login node, complete the following steps:

  1. Identify the login node by using the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).
         
         gcloud compute instances list \
           --zones=ZONE \
           --filter="name ~ login" --format "value(name)"
         

If the output lists multiple Slurm clusters, you can identify your login node by the `DEPLOYMENT_NAME` that you specified.

  2. Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the login node.
         
         gcloud compute ssh LOGIN_NODE \
           --zone=ZONE --tunnel-through-iap
         

Replace the following:

     * `ZONE`: the zone where the compute instances for your cluster are located.
     * `LOGIN_NODE`: the name of the login node, which you identified in the previous step.



## Test network performance on the Slurm cluster

We recommend that you validate the functionality of provisioned clusters. To do so, use [NCCL tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

## Redeploy the Slurm cluster

If you need to increase the number of compute nodes or add new partitions to your cluster, then you might need to update configurations for your Slurm cluster by redeploying. Because the default turnkey cluster blueprints use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images), you don't need to build new images to redeploy the cluster infrastructure.

If you modified your blueprint to build custom images, then you can speed up redeployments by using an existing image from a previous deployment. To avoid the need to create new images when you redeploy a cluster that uses custom images, specify the `--only` flag.

To redeploy the cluster infrastructure (`cluster-env,cluster`) without running any image building modules, do the following:

  1. Connect to the cluster. For instructions, see Connect to the Slurm cluster.

  2. Use the `./gcluster deploy` command for your required machine type:



    
    
    ./gcluster deploy -d a4xhigh-slurm-deployment.yaml examples/machine-learning/a4x-highgpu-4g/a4xhigh-slurm-blueprint.yaml --only cluster-env,cluster -w

This command redeploys your cluster and its infrastructure without running image building modules.

## Destroy the Slurm cluster

By default, the A4X, A4, and A3 Ultra blueprints turn on deletion protection on the Filestore instance. To delete the Filestore instance when you destroy the Slurm cluster, you must turn off deletion protection before you use the destroy command.

For instructions, see [set or remove deletion protection on an existing instance](https://docs.cloud.google.com/filestore/docs/deletion-protection#setting-or-removing).

  1. If you are connected to the cluster, then disconnect from it.

  2. Before you use the destroy command, navigate to the root of the Cluster Toolkit directory. By default, DEPLOYMENT_FOLDER is located at the root of the Cluster Toolkit directory.

  3. To destroy the cluster, use the [`./gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy DEPLOYMENT_FOLDER

Replace the following:

     * `DEPLOYMENT_FOLDER`: the name of the deployment folder. It's typically the same as DEPLOYMENT_NAME.

When the destruction completes, the output is similar to the following:
    
    Destroy complete! Resources: xx destroyed.
    

To learn how to cleanly destroy infrastructure and for advanced manual deployment instructions, see the deployment folder located at the root of the Cluster Toolkit directory: `DEPLOYMENT_FOLDER`/instructions.txt




## What's next

  * [Verify reservations consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * Learn how to manage host events: 
    * [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)
    * [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)
  * [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Optimize cluster networking by using NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
