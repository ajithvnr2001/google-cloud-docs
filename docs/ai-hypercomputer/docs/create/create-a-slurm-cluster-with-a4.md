---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-slurm-cluster-with-a4/
title: Create a self-managed Slurm cluster with an A4 VM \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:53.641350+00:00
---

# Create a self-managed Slurm cluster with an A4 VM  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-slurm-cluster-with-a4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a self-managed Slurm cluster with an A4 VM

This page describes how to quickly create and deploy an AI-optimized [Slurm cluster](https://slurm.schedmd.com/documentation.html) using A4 accelerator-optimized machine types with the gcloud CLI and [ Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

A4 accelerator-optimized machine types come with NVIDIA B200 GPUs attached and are specifically engineered for intensive AI computation to help your Slurm cluster efficiently handle large-scale model training and inference. For more information on A4 accelerator-optimized machine types on Google Cloud, see [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu).

**Important:** To complete this tutorial, you must have enough resources to create an A4 instance. To obtain these resources, contact your Google Technical Account Manager (TAM) to [reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) or [create a calendar mode reservation](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode) for the A4 machine type.   
  
Additionally, running this tutorial can incur [costs to your Google Cloud project](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-with-a4#costs).

Alternatively, you can use Cluster Director to create an A4-based Slurm cluster. Cluster Director is a managed service that simplifies and automates cluster deployment, reducing operational overhead. For more information, see [Create a fully managed Slurm cluster with two A4 VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-managed-slurm-cluster-with-a4).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=cluster-toolkit--quickstart-slurm-a4)

* * *

## Tutorial overview

This tutorial describes the steps to set up an AI-optimized Slurm cluster using A4 accelerator-optimized machine types. Specifically, you set up a cluster with Compute Engine instances, create a Cloud Storage bucket to store the necessary Terraform modules, and set up a Filestore instance to provision your Slurm cluster. To complete the steps in this tutorial, you follow this process:

  1. Set up your Google Cloud project with the required permissions for this guide and the environment variables for reserving your machine.
  2. Create a Cloud Storage bucket.
  3. Set up your storage environment variables.
  4. Set up Cluster Toolkit.
  5. Switch to the Cluster Toolkit directory.
  6. Create a Slurm deployment YAML file.
  7. Provision a Slurm cluster using a blueprint.
  8. Connect to the Slurm cluster.



## Before you begin

  1. [Reserve a capacity block](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) or [create a calendar mode reservation](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode) for one `a4-highgpu-8g` machine.
  2. Ensure that you have enough Filestore quota to provision the Slurm cluster. You need a minimum of 10,240 GiB of zonal capacity (also known as high scale SSD capacity).

To check your Filestore quota, view [Quotas & System limits](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Cloud%2520Filestore%2520API_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22,%22r%22:200\)\)) in the Google Cloud console and filter the table to only show **Filestore** resources.

     * For detailed instructions on checking Filestore quotas, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  3. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  4. Enable the Compute Engine, Filestore, Cloud Storage, Service Usage, and Cloud Resource Manager API:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,file.googleapis.com,storage.googleapis.com,serviceusage.googleapis.com,cloudresourcemanager.googleapis.com)




### Required roles

To get the permissions that you need to deploy a Slurm cluster, ask your administrator to grant you the following IAM roles: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on your project
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account itself
  * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
  * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Costs

The cost of running this tutorial varies by each section you complete, such as setting up the tutorial or running jobs. You can calculate the cost by using the [pricing calculator](https://cloud.google.com/products/calculator).

  * To estimate the cost for setting up this tutorial, use the following specifications:

    * **Filestore (standard) capacity per region:** 10,240 GiB.
    * **Standard persistent disk:** 50 GB `pd-standard` for the Slurm login node.
    * **Performance (SSD) persistent disks:** 50 GB `pd-ssd` for the Slurm controller.
    * **Compute Engine instance** : 1 `a4-highgpu-8g`.



## Launch Cloud Shell

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) which is a shell environment for managing resources hosted on Google Cloud.

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). gcloud CLI provides the primary command-line interface for Google Cloud. Launch Cloud Shell:

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the upper-right corner of the console, click the **Activate Cloud Shell** button: ![Cloud Shell icon](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session starts and displays a command-line prompt. You use this shell to run `gcloud` and Cluster Toolkit commands.

**Note:** You need enough Cloud Shell storage to run this tutorial successfully. We recommend checking if you have enough space available to run the tutorial and if not, you can also reset [Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell) to a clean slate. For more information, see [Reset Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

## Set machine reservation capacity variables

In Cloud Shell, set the following reservation capacity environment variables. These environment variables set placeholder values for configuring your project to access your reserved `a4-highgpu-8g` machine.

**Note:** These values must match the reserved capacity block details provided by your [Technical Account Manager (TAM)](https://cloud.google.com/tam) when the [capacity was delivered](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity).
    
    
    export A4_RESERVATION_PROJECT_ID=A4_RESERVATION_PROJECT_ID
    export A4_RESERVATION_NAME=A4_RESERVATION_NAME
    export A4_DEPLOYMENT_NAME=A4_DEPLOYMENT_NAME
    export A4_REGION=A4_REGION
    export A4_ZONE=A4_ZONE
    export A4_DEPLOYMENT_FILE_NAME=A4_DEPLOYMENT_FILE_NAME
    

Replace the following:

  * `A4_RESERVATION_PROJECT_ID`: the Google Cloud project ID that was granted the A4 machine type reservation block.
  * `A4_RESERVATION_NAME`: the name of the GPU reservation that's used in your project. For example, `a4high-exr`.
  * `A4_DEPLOYMENT_NAME`: a unique name for your Slurm cluster deployment. For example, `my-slurm-cluster-deployment`.
  * `A4_REGION`: the region that is running the reserved A4 machine reservation block. For example, `us-central1`.
  * `A4_ZONE`: the zone that contains the reserved machines. This string must contain both the region and zone. For example, `us-central1-a`.
  * `A4_DEPLOYMENT_FILE_NAME`: a unique name for your Slurm blueprint YAML file. If you run through this tutorial more than once, choose a unique deployment name each time.



## Switch to your A4-approved project

Switch to the Google Cloud project that has the approved reservation block for the A4 machine type:
    
    
    gcloud config set project ${A4_RESERVATION_PROJECT_ID}

## Create a Cloud Storage bucket

When you deploy a blueprint and its modules, Terraform creates a state file that maps your blueprint to your resources in the cloud. To maintain a reliable record of your infrastructure, it's a best practice to store your Terraform state files in a [remote](https://developer.hashicorp.com/terraform/language/state/remote), version-enabled location, such as a Cloud Storage bucket with versioning enabled.

To store your state file, create a Cloud Storage bucket with versioning enabled from the Cloud Shell:
    
    
    gcloud storage buckets create gs://${BUCKET_NAME} \
        --project=${A4_RESERVATION_PROJECT_ID} \
        --default-storage-class=STANDARD \
        --location=${BUCKET_LOCATION} \
        --uniform-bucket-level-access
    
    gcloud storage buckets update gs://${BUCKET_NAME} --versioning
    

Replace the following:

  * `BUCKET_NAME`: the name of the new Cloud Storage bucket, which must meet [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
  * `A4_RESERVATION_PROJECT_ID`: the Google Cloud project ID that was granted the A4 machine type reservation block.
  * `BUCKET_LOCATION`: the Google Cloud [region](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) in which to create your Cloud Storage bucket, such as `us-central1`. Terraform stores your state file in this location.



## Set storage capacity variables

In Cloud Shell, create the environment variables for the bucket you created in the previous step.
    
    
    export BUCKET_NAME=BUCKET_NAME
    export BUCKET_LOCATION=BUCKET_LOCATION
    

Replace the following:

  * `BUCKET_NAME`: the name of your bucket.
  * `BUCKET_LOCATION`: the region your bucket is located in.



## Set up Cluster Toolkit

To create a Slurm cluster in a Google Cloud project, you can use [ Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to handle deploying and provisioning the cluster. Cluster Toolkit is open-source software offered by Google Cloud to simplify the process of deploying workloads on Google Cloud.

Use the following steps to set up Cluster Toolkit.

### Install Cluster Toolkit

To install Cluster Toolkit, download and extract the prebuilt binary bundle for your platform. Both ZIP and tar (`.tgz`) archives are available.

  1. Go to the [Cluster Toolkit releases page](https://github.com/GoogleCloudPlatform/cluster-toolkit/releases) on GitHub.
  2. Download the bundle that matches your platform and architecture. The following options are available: 
     * `gcluster_bundle_linux_amd64.zip` or `gcluster_bundle_linux_amd64.tgz`
     * `gcluster_bundle_linux_arm64.zip` or `gcluster_bundle_linux_arm64.tgz`
     * `gcluster_bundle_mac_amd64.zip` or `gcluster_bundle_mac_amd64.tgz`
     * `gcluster_bundle_mac_arm64.zip` or `gcluster_bundle_mac_arm64.tgz`
  3. In your terminal, extract the bundle files to a new directory: 
     * If you downloaded a ZIP bundle, extract the files by using the `unzip` command:
           
           unzip BUNDLE_FILENAME -d cluster-toolkit

     * If you downloaded a tar bundle, extract the files by using the `tar` command:
           
           mkdir -p cluster-toolkit
           tar -xzf BUNDLE_FILENAME -C cluster-toolkit

Replace `BUNDLE_FILENAME` with the name of the bundle that you downloaded.

  4. Go to the new directory: 
         
         cd cluster-toolkit

  5. Verify the installation: 
         
         ./gcluster --version

The output shows the current version of Cluster Toolkit that you are using.




After installing the binary, you are now ready to deploy clusters to run your jobs or workloads.

## Create a deployment file

  1. In the Cluster Toolkit directory, create your Slurm deployment YAML file.
         
         nano ${A4_DEPLOYMENT_FILE_NAME}.yaml
         

  2. Paste the following content into the YAML file.
         
         ---
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: BUCKET_NAME
         
         vars:
           deployment_name: A4_DEPLOYMENT_FILE_NAME
           project_id: A4_RESERVATION_PROJECT_ID
           region: A4_REGION
           zone: A4_ZONE
           a4h_reservation_name: A4_RESERVATION_NAME
           a4h_cluster_size: 1
         

  3. To save and exit the file, press **Ctrl+O** > **Enter** > **Ctrl+X**.




## Provision the Slurm cluster

To provision the Slurm cluster, run the following deployment command. This command provisions the Slurm cluster with the [`examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml) blueprint file. By default, this blueprint deploys compute instances that use prebuilt [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). To learn more about the preinstalled drivers and configuration tools that you are deploying, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images).

**Note:** Provisioning the cluster can take up to an hour.   
  
Cloud Shell has an inactivity timeout that stops shells from running any processes after 40 minutes. If a timeout occurs, a dialog appears that asks if you want to reauthorize your session. To continue the deployment after a timeout, click **Reauthorize**.

In Cloud Shell, use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to start the cluster creation.
    
    
    ./gcluster deploy -d ${A4_DEPLOYMENT_FILE_NAME}.yaml examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml --auto-approve
    

## Connect to the cluster

After deploying, connect to the Google Cloud console to view your cluster.

  1. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Locate the login node (`a4high-login-001` or similar).

  3. Click **SSH** to connect.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Destroy the Slurm cluster

We recommend that you clean up your resources when they are no longer needed.

By default, the A4 High blueprints enable deletion protection on the Filestore instance. When destroying the Slurm cluster, you must disable deletion protection before running the destroy command.

#### Disable deletion protection

To disable deletion protection when you update an instance, use a command similar to the following:
    
    
      gcloud filestore instances update INSTANCE_NAME \
          --no-deletion-protection
    

Replace `INSTANCE_NAME` with the name of the instance you want to edit. For example, `my-genomics-instance`.

To find the `INSTANCE_NAME`, you can run `gcloud filestore instances list`. This command lists all the Filestore instances in your current Google Cloud project, including their names, locations (zones), tiers, capacity, and status.

After running the command, find the Filestore instance that matches the `a4-highgpu-8g` machine that's running in this tutorial.

#### Destroy the Slurm cluster

  1. Before running the destroy command, navigate to the root of the Cluster Toolkit directory. By default, `DEPLOYMENT_FOLDER` is located at the root of the Cluster Toolkit directory.

  2. Use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to destroy the cluster:
         
         ./gcluster destroy DEPLOYMENT_FOLDER --auto-approve

Replace `DEPLOYMENT_FOLDER` with the name of the deployment folder. It's typically the same as `DEPLOYMENT_NAME`.




When destruction is complete, you see a message similar to the following:
    
    
    Destroy complete! Resources: xx destroyed.
    

### Delete the storage bucket

Delete the Cloud Storage bucket after you make sure that the previous command ended without errors:
    
    
    gcloud storage buckets delete gs://${BUCKET_NAME}
    

## Troubleshooting

  * **Error** : Cloud Shell can't provision the cluster because there is no storage left.

You might see this error if you are a frequent user of Cloud Shell and you have run out of storage space.

To resolve this issue, see [Disable or reset Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

  * **Error** : Cluster or blueprint name already exists.

You might see this error if you are using a project that has already used the exact file names used in this tutorial. For example, if someone else in your organization ran through this tutorial end-to-end.

To resolve this issue, run through the tutorial again and choose a unique name for the [deployment file](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-with-a4#create-deployment-file) and then rerun the [provision the Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-with-a4#provision-cluster) command with the new deployment file.




## What's next

  * Advanced Slurm tasks: 
    * [Redeploy the Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster#redeploy-slurm-cluster)
    * [Run NCCL on Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)
  * Learn how to manage host events: 
    * [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)
    * [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)
  * [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
