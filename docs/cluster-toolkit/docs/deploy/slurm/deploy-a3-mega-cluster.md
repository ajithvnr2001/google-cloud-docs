---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster/
title: Deploy an A3 Mega Slurm cluster for ML training \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:57.549756+00:00
---

# Deploy an A3 Mega Slurm cluster for ML training  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy an A3 Mega Slurm cluster for ML training Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to deploy an A3 Mega (`a3-megagpu-8g`) Slurm cluster. These clusters provide high-performance network topologies that let you efficiently run large-scale artificial intelligence (AI) and machine learning (ML) training workloads.

A3 Mega (`a3-megagpu-8g`) machine types provide high-performance network topologies that let you efficiently run large-scale artificial intelligence (AI) and machine learning (ML) training workloads.

To learn more about the A3 Mega accelerator-optimized machine type, see the [A3 Mega machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) section in the Compute Engine documentation.

## Limitations

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Mega machine type.
  * You can only use an A3 Mega machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Mega machine type.
  * The A3 Mega machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Mega machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Mega machine type.



## Before you begin

Before creating a Slurm cluster, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). 
  3. **Verify that you have enough Filestore capacity quota** : you need to have enough Filestore quota in your target region before deploying. The required minimum capacity depends on the machine types in your cluster: 
     * **A3 Mega** : requires a minimum of 10 TiB (10,240 GiB) of HIGH_SCALE_SSD (zonal) capacity.

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

## Set up Cloud Storage bucket

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



## Reserve capacity

If you plan to use reservation-bound clusters, you must reserve capacity. To reserve capacity, follow the instructions in this section. If you plan to use flex-start or Spot VMs, skip this section.

For Slurm consumption options, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). To see GKE consumption options for Cluster Toolkit, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options). 

To create a standard single-project reservation for A3 Mega instances, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--require-specific-reservation` flag: 
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --require-specific-reservation \
        --project=PROJECT_ID \
        --machine-type=a3-megagpu-8g \
        --vm-count=NUMBER_OF_INSTANCES \
        --zone=ZONE
    

Replace the following variables:

  * `RESERVATION_NAME`: the name of the single-project reservation that you want to use.
  * `PROJECT_ID`: the ID of your project.
  * `NUMBER_OF_INSTANCES`: the number of compute instances needed for the cluster.
  * `ZONE`: a zone that has `a3-megagpu-8g` machine types. To review the zones where you can create A3 Mega instances, see [Accelerator availability](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table).



After you destroy your cluster, you can delete the reservation if you don't need it anymore. For information, see [Delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete). 

## Create a deployment file

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



## Provision a Slurm cluster

Cluster Toolkit provisions the cluster based on the deployment file that you created in the previous step and the default cluster blueprint. For more information about the software that is installed by the blueprint, including NVIDIA drivers and CUDA, [learn more about Slurm custom images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#slurm-images).

To provision the cluster, use the [`./gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) from the Cluster Toolkit directory. This step takes approximately 20-30 minutes.
    
    
    ./gcluster deploy -d examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml \
    examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml
    

## Connect to the A3 Mega Slurm cluster

To access your cluster, you must login to the Slurm login node. To sign in, you can use either Google Cloud console or Google Cloud CLI.

###  Console 

  1. Go to the **Compute Engine** > **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the login node. It has a similar name to `DEPLOYMENT_NAME` +`login-001`.

  3. From the **Connect** column of the login node, click **SSH**.




###  gcloud 

To connect to the login node, complete the following steps:

  1. Identify the login node by using the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).
         
         gcloud compute instances list \
           --zones=ZONE \
           --filter="name ~ login" --format="value(name)"
         

If the output lists multiple Slurm clusters, you can identify your login node by the `DEPLOYMENT_NAME` that you specified.

  2. Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the login node.
         
         gcloud compute ssh LOGIN_NODE \
           --zone=ZONE --tunnel-through-iap
         

Replace the following:

     * `ZONE`: the zone where the compute instances for your cluster are located.
     * `LOGIN_NODE`: the name of the login node, which you identified in the previous step.



## Test network performance on the Slurm cluster

We recommended that you validate the functionality of provisioned clusters. To do so, use [NCCL tests](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm), which are [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl) that are optimized for the Google environment.

## Redeploy the Slurm cluster

If you need to increase the number of compute nodes or add new partitions to your cluster, you might need to update configurations for your Slurm cluster by redeploying. Redeployment can be sped up by using an existing image from a previous deployment. To avoid creating new images during a redeploy, specify the `--only` flag.

To redeploy the cluster using an existing image run the following command:
    
    
    ./gcluster deploy -d \
    examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml \
    examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml \
    --only primary,cluster -w

This command is only for redeployments where an image already exists, it only redeploys the cluster and its infrastructure.

## Destroy the Slurm cluster

By default, the A3 Mega blueprints enable deletion protection on the Filestore instance. For the Filestore instance to be deleted when destroying the Slurm cluster, learn how to [set or remove deletion protection on an existing instance](https://docs.cloud.google.com/filestore/docs/deletion-protection#setting-or-removing) to disable deletion protection before running the destroy command.

  1. Disconnect from the cluster if you haven't already.

  2. Before running the destroy command, navigate to the root of the Cluster Toolkit directory. By default, DEPLOYMENT_FOLDER is located at the root of the Cluster Toolkit directory.

  3. To destroy the cluster, use the [`./gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy):
         
         ./gcluster destroy DEPLOYMENT_FOLDER --auto-approve

Replace `DEPLOYMENT_FOLDER` with the name of the deployment folder. It's typically the same as DEPLOYMENT_NAME.

When destruction is complete you should see a message similar to the following:
         
         Destroy complete! Resources: xx destroyed.
         




To learn how to cleanly destroy infrastructure and for advanced manual deployment instructions, see the deployment folder located at the root of the Cluster Toolkit directory: `DEPLOYMENT_FOLDER/instructions.txt`.

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
