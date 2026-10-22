---
url: https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d/
title: Create a Cloud RDMA-enabled HPC Slurm cluster with H4D instances \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:12.590256+00:00
---

# Create a Cloud RDMA-enabled HPC Slurm cluster with H4D instances  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Cloud RDMA-enabled HPC Slurm cluster with H4D instances

You can deploy a Slurm cluster on Google Cloud by using H4D machine types. These instances use [Remote Direct Memory Access (RDMA)](https://en.wikipedia.org/wiki/Remote_direct_memory_access) for ultra-low latency communication, which is crucial for high performance computing (HPC) workloads. This tutorial guides you through configuring a Slurm cluster by using the Google Cloud CLI and Cluster Toolkit. Cluster Toolkit is an open source Google Cloud tool that simplifies deploying HPC, artificial intelligence (AI), and machine learning (ML) workloads. The toolkit uses customizable blueprints to provision infrastructure in accordance with Google Cloud best practices.

## Tutorial overview

This tutorial describes the steps to set up an HPC-optimized Slurm cluster using H4D machine types with Cloud RDMA. Specifically, you set up a cluster with Compute Engine virtual machines, create a Cloud Storage bucket to store the necessary Terraform modules, and set up a Filestore instance to provision your Slurm cluster. To complete the steps in this tutorial, you follow this process:

  1. Set up your Google Cloud project with the required permissions and environmental variables.
  2. Set up a Cloud Storage bucket.
  3. Set up Cluster Toolkit.
  4. Switch to the Cluster Toolkit directory.
  5. Create a Slurm deployment YAML file.
  6. Provision a Slurm cluster using a blueprint.
  7. Connect to the Slurm cluster.



## Before you begin

  1. [Request a reserved capacity block](https://docs.cloud.google.com/compute/docs/hpc/reserve-capacity-account-team) for two H4D instances with 192 vCPUs each.
  2. Verify that you have enough Filestore quota to provision the Slurm cluster. You need a minimum of 5,120 GiB of zonal capacity specifically with a Filestore service tier of Basic SSD.

To check your Filestore quota, view [Quotas & System limits](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22Cloud%2520Filestore%2520API_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceTitle_22%257D%255D%22,%22r%22:200\)\)) in the Google Cloud console and filter the table to only show **Filestore** resources.

     * For detailed instructions on checking Filestore quotas, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  3. [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

  4. Enable the Compute Engine, Filestore, Cloud Storage, Service Usage, and Cloud Resource Manager API:

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,file.googleapis.com,storage.googleapis.com,serviceusage.googleapis.com,cloudresourcemanager.googleapis.com)

  5. To deploy a Slurm cluster, you must have the following roles:

     * Storage Object Viewer (`roles/storage.objectViewer`): grants permission to read cluster installation artifacts from Cloud Storage.
     * Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`): grants permissions to manage Compute Engine instances that are required for the Slurm cluster to function correctly.
     * Service Account User (`roles/iam.serviceAccountUser`): grants a principal the ability to impersonate a service account. In this case, it allows the Compute Engine default service account to act as itself.
     * To consume a single-project reservation: Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) on the project.
     * To consume a shared reservation: Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Costs

The cost of running this tutorial varies by each section you complete, such as setting up the tutorial or running jobs. You can calculate the cost by using the [pricing calculator](https://cloud.google.com/products/calculator).

  * To estimate the cost for setting up this tutorial, use the following specifications:

    * **Filestore (Basic SSD) capacity per region:** 2,560 GiB.
    * **N2 instance** : The Slurm login node uses a `n2-standard-4` machine type.
    * **Standard persistent disk:** 50 GB `pd-standard` for the Slurm login node.
    * **C2 instance** : The Slurm controller node uses a `c2-standard-4` machine type.
    * **Performance (SSD) persistent disks:** 50 GB `pd-ssd` for the Slurm controller.
    * **VM instance** : Two H4D instances created with the `h4d-highmem-192`, `h4d-standard-192`, or `h4d-highmem-192-lssd` machine type.
    * **Hyperdisk Balanced volumes** : 50 GiB for each H4D instance.



## Launch Cloud Shell

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell/docs) which is a shell environment for managing resources hosted on Google Cloud.

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). gcloud CLI provides the primary command-line interface for Google Cloud. To launch Cloud Shell:

  1. Go to the Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. From the upper-right corner of the console, click the **Activate Cloud Shell** button: ![Cloud Shell icon](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png)




A Cloud Shell session starts and displays a command-line prompt. You use this shell to run `gcloud` and Cluster Toolkit commands.

**Note:** You need enough Cloud Shell storage to run this tutorial successfully. We recommend checking if you have enough space available to run the tutorial and if not, you can also reset [Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell) to a clean slate. For more information, see [Reset Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

## Set environment variables

In Cloud Shell, set the environment variables described in the following sections to use for the remainder of the tutorial. These environment variables set placeholder values for the following tasks:

  * Configures your project with the relevant values to access your reserved H4D instances.

  * Sets up a Cloud Storage bucket to store Cluster Toolkit modules.




### Reservation capacity variables

**Note:** These values must match the reserved capacity block details provided by your [Technical Account Manager (TAM)](https://cloud.google.com/tam) when the [capacity was delivered](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity).
    
    
    export H4D_RESERVATION_PROJECT_ID=H4D_RESERVATION_PROJECT_ID
    export H4D_RESERVATION_NAME=H4D_RESERVATION_NAME
    export H4D_DEPLOYMENT_NAME=H4D_DEPLOYMENT_NAME
    export H4D_REGION=H4D_REGION
    export H4D_ZONE=H4D_ZONE
    export H4D_DEPLOYMENT_FILE_NAME=H4D_DEPLOYMENT_FILE_NAME
    

Replace the following:

  * `H4D_RESERVATION_PROJECT_ID`: the Google Cloud project ID that was granted the H4D machine type reservation block.
  * `H4D_RESERVATION_NAME`: the name of your VM reservation block, found in your project. For example, `h4d-highmem-exr`.
  * `H4D_DEPLOYMENT_NAME`: a unique name for your Slurm cluster deployment. For example, `h4d-hpc-slurm-cluster-deployment`.
  * `H4D_REGION`: the region that is running the reserved H4D machine reservation block. For example, `us-central1`.
  * `H4D_ZONE`: the zone that contains the reserved machines. This string must contain both the region and zone. For example, `us-central1-a`.
  * `H4D_DEPLOYMENT_FILE_NAME`: a unique name for your Slurm blueprint YAML file. If you run through this tutorial more than once, choose a unique deployment name each time.



### Storage capacity variables

Create the environment variables for your Cloud Storage bucket.

Cluster Toolkit uses blueprints to define and deploy clusters of VMs. A blueprint defines one or more Terraform modules to provision Cloud infrastructure. This bucket is used to store these blueprints.
    
    
    export GOOGLE_CLOUD_BUCKET_NAME=BUCKET_NAME
    export GOOGLE_CLOUD_BUCKET_LOCATION=BUCKET_LOCATION
    

Replace the following:

  * `BUCKET_NAME`: the name that you want to use for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).
  * `BUCKET_LOCATION`: any Google Cloud [region](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone) of your choice, where the bucket is hosted. For example, `us-central1`.



## Switch to the project with the reserved H4D capacity block

Run the following command to ensure that you are in the Google Cloud project that has the approved reservation block for the H4D instances.
    
    
    gcloud config set project ${H4D_RESERVATION_PROJECT_ID}
    

## Create a Cloud Storage bucket

Create the bucket to store your Terraform modules. From Cloud Shell, using your environment variables, run the following command:

A best practice when working with Terraform is to [store the state remotely](https://developer.hashicorp.com/terraform/language/state/remote) in a version-enabled file. On Google Cloud, you can create a Cloud Storage bucket that has versioning enabled.
    
    
    gcloud storage buckets create gs://${GOOGLE_CLOUD_BUCKET_NAME} \
        --project=${H4D_RESERVATION_PROJECT_ID} \
        --default-storage-class=STANDARD \
        --location=${GOOGLE_CLOUD_BUCKET_LOCATION} \
        --uniform-bucket-level-access
    
    gcloud storage buckets update gs://${GOOGLE_CLOUD_BUCKET_NAME} --versioning
    

## Set up the Cluster Toolkit

To create a Slurm cluster in a Google Cloud project, you can use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to handle deploying and provisioning the cluster. Cluster Toolkit is open-source software offered by Google Cloud to simplify the process of deploying workloads on Google Cloud.

Use the following steps to set up Cluster Toolkit.

### Clone the Cluster Toolkit GitHub repository

  1. In Cloud Shell, clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/cluster-toolkit.git

  2. Go to the main working directory:
         
         cd cluster-toolkit/




### Build the Cluster Toolkit binary

  1. In Cloud Shell, build the Cluster Toolkit binary from source by running the following command:
         
         make

  2. To verify the build, run the following command:

To deploy an HPC-optimized Slurm cluster that uses H4D instances, you must use version `v1.70.0` or later of the Cluster Toolkit.
         
         ./gcluster --version

After building the binary, you are now ready to deploy clusters to run your jobs or workloads.




## Create a deployment file

  1. In the Cluster Toolkit directory, create your Slurm deployment YAML file.
         
         nano ${H4D_DEPLOYMENT_FILE_NAME}.yaml
         

**Tip:** Alternatively, for an example of a more detailed deployment file, you can copy [`examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d-deployment.yaml) to your workspace and edit it.
  2. Paste the following content into the YAML file.
         
         ---
         terraform_backend_defaults:
           type: gcs
           configuration:
             bucket: GOOGLE_CLOUD_BUCKET_NAME
         
         vars:
           deployment_name: H4D_DEPLOYMENT_FILE_NAME
           project_id: H4D_RESERVATION_PROJECT_ID
           region: H4D_REGION
           zone: H4D_ZONE
           
           
         

  3. To save and exit the file, press **Ctrl+O** > **Enter** > **Ctrl+X**.




## Provision the Slurm cluster

To provision the Slurm cluster, run the following deployment command. This command provisions the Slurm cluster with the [H4D Cluster Toolkit blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml).

**Note:** Provisioning the cluster can take up to an hour.   
  
Cloud Shell has an inactivity timeout that stops shells from running any processes after 40 minutes. If a timeout occurs, a dialog appears that asks if you want to reauthorize your session. To continue the deployment after a timeout, click **Reauthorize**.

In Cloud Shell, start the cluster creation.
    
    
    ./gcluster deploy -d ${H4D_DEPLOYMENT_FILE_NAME}.yaml examples/hpc-slurm-h4d/hpc-slurm-h4d.yaml --auto-approve
    

## Connect to the cluster

After deploying, connect to the Google Cloud console to view your cluster.

  1. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Locate the login node, which might have a name like `example-deployment-login-123`.

  3. Click **SSH** to connect.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the Slurm cluster

We recommend that you clean up your resources when they are no longer needed.

#### Destroy the Slurm cluster

  1. Before running the destroy command, navigate to the root of the Cluster Toolkit directory. By default, DEPLOYMENT_FOLDER is located at the root of the Cluster Toolkit directory.

  2. To destroy the cluster, run:
         
         ./gcluster destroy ${H4D_DEPLOYMENT_FILE_NAME} --auto-approve
         




When the cluster destruction is complete, you see a message similar to the following:
    
    
    Destroy complete! Resources: xx destroyed.
    

### Delete the storage bucket

Delete the Cloud Storage bucket after you make sure that the previous command ended without errors:
    
    
    gcloud storage buckets delete gs://${GOOGLE_CLOUD_BUCKET_NAME}
    

## Troubleshooting

  * **Error** : Cloud Shell can't provision the cluster because there is no storage left.

You might see this error if you are a frequent user of Cloud Shell and you have run out of storage space.

To resolve this issue, see [Disable or reset Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

  * **Error** : Cluster or blueprint name already exists.

You might see this error if you are using a project that has already used the exact file names used in this tutorial. For example, if someone else in your organization ran through this tutorial end-to-end.

To resolve this issue, run through the tutorial again and choose a unique name for the deployment file and rerun the provision the Slurm cluster command with the new deployment file.




## What's next

  * Learn how to [Reconfigure the Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster)
  * Learn how to manage host events: 
    * [Manage host events across VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d)
    * [Manage host events across reservations](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)
  * [View VMs topology](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology)
  * [Monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) in your Slurm cluster
  * [Report a faulty host](https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
