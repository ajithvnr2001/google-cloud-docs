---
url: https://docs.cloud.google.com/compute/docs/hpc/create-a-slurm-cluster-h4d/
title: Create an H4D Slurm cluster with enhanced management capabilities \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:14:59.434679+00:00
---

# Create an H4D Slurm cluster with enhanced management capabilities  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/create-a-slurm-cluster-h4d/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an H4D Slurm cluster with enhanced management capabilities Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a High Performance Computing (HPC) [Slurm cluster](https://slurm.schedmd.com/documentation.html) that uses remote direct memory access (RDMA) with H4D VMs with enhanced cluster management capabilities. You use the gcloud CLI and [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to configure the cluster.

The H4D machine series is specifically designed to meet the needs of demanding HPC workloads. H4D offers instances with improved workload scalability through Cloud RDMA networking with 200 Gbps throughput. For more information on H4D compute-optimized machine types on Google Cloud, see [H4D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series).

**Important:** To complete this tutorial, you must first contact your Google Technical Account Manager (TAM) to [request a reserved capacity block for the H4D machine type](https://docs.cloud.google.com/compute/docs/hpc/reserve-capacity-account-team). Once approved, this capacity is added to your Google Cloud project. The capacity approval process can take several days.   
  
**Tip:** To walk through a quick start tutorial that deploys an H4D machine type on Slurm, see the [quickstart](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d) for creating an RDMA enabled Slurm cluster with H4D instances.

## Before you begin

Before creating a Slurm cluster, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : the option that you pick determines how you want to obtain and use vCPU resources.
  2. **Obtain capacity** : obtain capacity for the selected consumption option.

To learn more, see [Choose a consumption option and obtain capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity).

  3. **Verify that you have enough Filestore capacity quota** : you need to have enough Filestore quota in your target region before deploying. The required minimum capacity depends on the machine types in your cluster: 
     * **A4X Max, A4X, A4, A3 Ultra, and A3 Mega** : requires a minimum of 10 TiB (10,240 GiB) of HIGH_SCALE_SSD (zonal) capacity.
     * **A3 High** : requires a minimum of 2.5 TiB (2,560 GiB) of BASIC_SSD (standard) capacity.

To check quota or request a quota increase, see the following:

     * To check quota in your project, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, then [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  4. **Install Cluster Toolkit** : to provision Slurm clusters, you must use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) version `v1.62.0` or later. 

To install Cluster Toolkit, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).




In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

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

Ensure that you are in the Cluster Toolkit directory by running the following command:
    
    
    cd cluster-toolkit

This cluster deployment requires Cluster Toolkit `v1.70.0` or later. To check your version, you can run the following command:
    
    
    ./gcluster --version

## Create a deployment file

Create a deployment file to specify the Cloud Storage bucket, set names for your network and subnetwork, and set deployment variables such as project ID, region, and zone.

To create a deployment file, follow the steps for the H4D machine type: 

The parameters that you need to add to your deployment file depend on the [consumption option](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) that you're using for your deployment. Select the tab that corresponds to your consumption option you want to use.

### Reservation-bound

To create your deployment file, use a text editor to create a YAML file named `h4d-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      h4d_cluster_size: NUMBER_OF_INSTANCES
      h4d_reservation_name: RESERVATION_NAME
    
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region that has the reserved machines.
  * `ZONE`: the zone where you want to provision the cluster. If you're using a reservation-based consumption option, the region and zone information was provided by your account team when the [capacity was delivered](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity).
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.
  * `RESERVATION_NAME`: the name of your [reservation](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-reservation).



### Flex-start

To create your deployment file, use a text editor to create a YAML file named `h4d-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      h4d_cluster_size: NUMBER_OF_INSTANCES
      h4d_dws_flex_enabled: true
    
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



This deployment provisions [static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types#overview), which means that the cluster has a set number of nodes at all times. If you want to enable your cluster to autoscale instead, use [`examples/h4d/hpc-slurm-h4d.yaml` file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/h4d/hpc-slurm-h4d.yaml) and edit the values of `node_count_static` and `node_count_dynamic_max` to match the following:
    
    
          node_count_static: 0
          node_count_dynamic_max: $(vars.h4d_cluster_size)
    

### Spot

To create your deployment file, use a text editor to create a YAML file named `h4d-slurm-deployment.yaml` and add the following content.

**Tip:** For a more detailed example, copy and paste the contents of [`examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml) into a file in your workspace and edit it. 
    
    
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    vars:
      deployment_name: DEPLOYMENT_NAME
      project_id: PROJECT_ID
      region: REGION
      zone: ZONE
      h4d_cluster_size: NUMBER_OF_INSTANCES
      h4d_enable_spot_vm: true
    
    

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket, which you created in the previous section.
  * `DEPLOYMENT_NAME`: a name for your deployment. If creating multiple clusters, ensure that you select a unique name for each one.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want to provision your cluster.
  * `ZONE`: the zone where you want to provision your cluster.
  * `NUMBER_OF_INSTANCES`: the number of Compute Engine instances that you want for the cluster.



## Provision an H4D Slurm cluster

Cluster Toolkit provisions the cluster based on the deployment file you created in the previous step and the default cluster blueprint. For more information about the software that is installed by the blueprint, see [learn more about Slurm custom images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#slurm-images).

Using Cloud Shell, from the directory where you installed Cluster Toolkit and created the deployment file, you can provision the cluster with the following command, which uses the [H4D Slurm blueprint file](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml). This step takes approximately 20-30 minutes.

**Note:** Cloud Shell has an inactivity timeout that stops shells from running any processes after 40 minutes. If a timeout occurs, a dialog appears that asks if you want to reauthorize your session. To continue the deployment after a timeout, click **Reauthorize**.
    
    
    ./gcluster deploy -d h4d-slurm-deployment.yaml examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml --auto-approve

## Connect to the Slurm cluster

To access your cluster, you must sign in to the Slurm login node. To sign in, you can use either Google Cloud console or Google Cloud CLI.

###  Console 

  1. Go to the **Compute Engine** > **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the login node. It should have a name with the pattern `DEPLOYMENT_NAME` +`login-001`.

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

     * `ZONE`: the zone where the VMs for your cluster are located.
     * `LOGIN_NODE`: the name of the login node, which you identified in the previous step.



## Redeploy the Slurm cluster

If you need to increase the number of compute nodes or add new partitions to your cluster, you might need to update configurations for your Slurm cluster by redeploying.

To redeploy the cluster using an existing image do the following:

  1. Connect to the cluster

  2. Run the following command:
         
         ./gcluster deploy -d h4d-slurm-deployment.yaml examples/h4d/h4d-slurm-deployment.yaml --only cluster-env,cluster --auto-approve -w
         

This command is only for redeployments where an image already exists; it only redeploys the cluster and its infrastructure.




## Destroy the Slurm cluster

To remove the Slurm cluster and the instances within it, complete the following steps:

  1. Disconnect from the cluster if you haven't already.

  2. Before running the destroy command, navigate to the root of the Cluster Toolkit directory. By default, DEPLOYMENT_FOLDER is located at the root of the Cluster Toolkit directory.

  3. To destroy the cluster, run:
         
         ./gcluster destroy DEPLOYMENT_FOLDER --auto-approve

Replace the following:

     * `DEPLOYMENT_FOLDER`: the name of the deployment folder. It's typically the same as DEPLOYMENT_NAME.



When the cluster removal is complete you should see a message similar to the following:
    
    
      Destroy complete! Resources: xx destroyed.
    

To learn how to cleanly destroy infrastructure and for advanced manual deployment instructions, see the deployment folder located at the root of the Cluster Toolkit directory: `DEPLOYMENT_FOLDER`/instructions.txt

## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View VMs topology](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology)
  * [Manage host events across VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)
  * [Manage host events across reservations](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)
  * [Monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) in your Slurm cluster
  * [Report faulty host](https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
