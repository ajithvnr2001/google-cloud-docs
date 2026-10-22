---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-a3-mega-gke-cluster/
title: Deploy an A3 Mega GKE cluster for ML training \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:59.342304+00:00
---

# Deploy an A3 Mega GKE cluster for ML training  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-a3-mega-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy an A3 Mega GKE cluster for ML training Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the deployment steps for provisioning an A3 Mega (`a3-megagpu-8g`) Google Kubernetes Engine (GKE) cluster that is ideal for running large-scale artificial intelligence (AI) and machine learning (ML) training workloads.

A3 Mega (`a3-megagpu-8g`) machine types provide high-performance network topologies that let you efficiently run large-scale artificial intelligence (AI) and machine learning (ML) training workloads.

To learn more about the A3 Mega accelerator-optimized machine type, see the [A3 Mega machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) section in the Compute Engine documentation.

## Before you begin

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Identify the regions and zones where the `a3-megagpu-8g` machine type is available, run the following command:
         
         gcloud compute machine-types list --filter="name=a3-megagpu-8g"
         

  3. Verify that you have enough GPU quotas. Each `a3-megagpu-8g` machine has 8 H100 80GB GPUs attached, so you'll need at least 8 NVIDIA H100 80GB GPUs in your selected region.

     1. To view quotas, see [View the quotas for your project](https://docs.cloud.google.com/docs/quotas/view-manage). In the filter_list **Filter** field, select **Dimensions (e.g. location)** and specify [`gpu_family:NVIDIA_H100_MEGA`](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
     2. If you don't have enough quota, [request a higher quota](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).
  4. Verify that you have enough Filestore quota. You need a minimum of 10,240 GiB of zonal (also known as high scale SSD) capacity. If you don't have enough quota, [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).




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

## Install Cluster Toolkit

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

From the CLI, complete the following steps:

  1. Install [dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).
  2. Set up [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).



## Create a reservation

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

## Create a cluster

Use the following instructions to create a cluster using [ Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

**Note:** If you create multiple clusters using these same cluster blueprints, verify that all VPC and subnet names are unique per project to prevent errors.

  1. After you have installed the Cluster Toolkit, verify that you are in the Cluster Toolkit directory. To go to the main Cluster Toolkit blueprint's working directory, run the following command from the CLI.
         
         cd cluster-toolkit

  2. Create a Cloud Storage bucket to store the state of the Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
               --default-storage-class=STANDARD \
               --project=PROJECT_ID \
               --location=COMPUTE_REGION_TERRAFORM_STATE \
               --uniform-bucket-level-access
         gcloud storage buckets update gs://BUCKET_NAME --versioning
         

Replace the following:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `COMPUTE_REGION_TERRAFORM_STATE`: the compute region where you want to store the state of the Terraform deployment.
  3. In the [`examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml` blueprint from GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml), replace the following variables in the `terraform_backend_defaults` and `vars` sections to match the specific values for your deployment:

     * `BUCKET`: the name of the Cloud Storage bucket that you created in the previous step.
     * `DEPLOYMENT_NAME`: a unique name for the deployment, which must be between 6 and 30 characters in length. If the deployment name isn't unique within a project, then cluster creation fails.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the compute region for the cluster.
     * `ZONE`: the compute zone for the node pool of A3 Mega machines. This zone must match the zone where machines are available in your reservation.
     * `AUTHORIZED_CIDR`: the IP address range that you want to let connect to the cluster. This CIDR block must include the IP address of the machine that calls Terraform. For more information, see [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work). To get the IP address of your host machine, run the `curl -s https://ifconfig.me` command.
  4. Choose a consumption option for your GKE deployment:

By default, the deployment file is configured to consume [standard or future reservations](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#reservations). To use an alternative consumption model (such as on-demand capacity, Spot VMs, or flex-start provisioning mode), update your deployment YAML file. For more information, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).

To configure a reservation, set the following values in the specific reservation section:

     * In the `reservation_affinity` block, in the `specific_reservations` list, specify the reservation `name` field:

       * To place the node pool anywhere in the reservation, provide the name of your reservation (`RESERVATION_NAME`).
       * To target a specific block within your reservation, use the reservation and block names in the following format:
    
    RESERVATION_NAME/reservationBlocks/BLOCK_NAME
    

If you don't know which blocks are available in your reservation, then see [View the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

     * `STATIC_NODE_COUNT`: the number of A3 Mega nodes in your cluster.

  5. To modify advanced blueprint settings, edit the [`examples/gke-a3-megagpu/gke-a3-megagpu.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml) file.

  6. Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy the blueprint and provision the GKE infrastructure using A3 Mega machine types:
         
         cd ~/cluster-toolkit
         ./gcluster deploy -d \
         examples/gke-a3-megagpu/gke-a3-megagpu-deployment.yaml \
         examples/gke-a3-megagpu/gke-a3-megagpu.yaml
         

  7. When prompted, select **(A)pply** to deploy the blueprint. The blueprint creates VPC networks, service accounts, a cluster, and a node pool.




## Configure cluster access and check driver status

To interact with your GKE cluster, configure `kubectl` with your cluster credentials:
    
    
    gcloud container clusters get-credentials \
        DEPLOYMENT_NAME \
        --region=COMPUTE_REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `DEPLOYMENT_NAME`: the name of your deployment.
  * `COMPUTE_REGION`: the compute region of your cluster.
  * `PROJECT_ID`: your Google Cloud project ID.



Verify that the GPUDirect-TCPXO driver installers and device injectors are running on all nodes:
    
    
    kubectl get daemonsets -n kube-system nccl-tcpxo
    

## Run Dynamic Workload Scheduler sample Jobs

If you provisioned your cluster using Dynamic Workload Scheduler (either flex-start or queued provisioning), then you can validate workload scheduling by submitting sample Kubernetes Jobs.

For more information about Dynamic Workload Scheduler provisioning modes, see [Dynamic Workload Scheduler flex-start with queued provisioning](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#dws-queued-provisioning).

### Submit a sample Job

Select the tab that corresponds to your consumption option:

### Flex-start

This task is optional and applies only if you provisioned your cluster with flex-start. Workloads configured for flex-start require the `cloud.google.com/gke-flex-start: "true"` node selector in their Pod specification.

  1. Submit the sample flex-start Job:
         
         kubectl apply -f examples/dws-sample-workloads/sample-job-flex.yaml
         

  2. Monitor the status of your Job and Pods:
         
         kubectl get jobs
         kubectl describe job JOB_NAME
         kubectl get pods
         kubectl describe pod POD_NAME
         

Replace the following:

     * `JOB_NAME`: the name of your Job.
     * `POD_NAME`: the name of your Pod.
  3. When the Job completes, delete the Job resources:
         
         kubectl delete -f examples/dws-sample-workloads/sample-job-flex.yaml
         




### Queued provisioning

This task is optional and applies only if you provisioned your cluster with queued provisioning. Workloads configured for queued provisioning require the following label and annotation in their Pod specification:

  * Label: `kueue.x-k8s.io/queue-name: dws-local-queue`
  * Annotation: `provreq.kueue.x-k8s.io/maxRunDurationSeconds: "MAX_RUN_DURATION"`



For more information, see [Workload manifest requirements for queued provisioning](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options#queued-provisioning-manifest).

  1. Submit the sample queued provisioning Job:
         
         kubectl apply -f examples/dws-sample-workloads/sample-job-flex-queue.yaml
         

  2. Monitor the status of your Job and Pods:
         
         kubectl get jobs
         kubectl describe job JOB_NAME
         kubectl get pods
         kubectl describe pod POD_NAME
         

Replace the following:

     * `JOB_NAME`: the name of your Job.
     * `POD_NAME`: the name of your Pod.
  3. When the Job completes, delete the Job resources:
         
         kubectl delete -f examples/dws-sample-workloads/sample-job-flex-queue.yaml
         




## Test network performance

Validate the networking performance and GPU communication of your provisioned clusters by running GPUDirect TCPXO with [NCCL tests](https://developer.nvidia.com/nccl), which are optimized for A3 Mega VM instances in Google Cloud.

Select the tab for your cluster provisioning model:

### Standard

For clusters provisioned with standard or future reservations, Spot VMs, or on-demand capacity, run the standard NCCL test manifest:

  1. Deploy the NCCL test manifest:
         
         kubectl apply -f examples/gke-a3-megagpu/nccl-test-latest.yaml
         

  2. Monitor the test Pods:
         
         kubectl get pods
         

  3. Inspect the benchmark results in the Pod logs:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the NCCL test Pod.

  4. When the test completes and Pods show a `Completed` status, clean up the test resources:
         
         kubectl delete -f examples/gke-a3-megagpu/nccl-test-latest.yaml
         




### Flex-start

For clusters configured with Dynamic Workload Scheduler flex-start, deploy the NCCL test by using the JobSet manifest:

  1. Deploy the NCCL test JobSet:
         
         kubectl create -f examples/gke-a3-megagpu/nccl-jobset-flex.yaml
         

  2. Monitor the status of the JobSet Pods:
         
         kubectl get pods
         

  3. Inspect the benchmark results in the primary JobSet Pod logs:
         
         kubectl logs JOBSET_POD_NAME
         

Replace `JOBSET_POD_NAME` with the name of the primary JobSet Pod.

  4. When the test completes and Jobs show a `Completed` status, clean up the test resources:
         
         kubectl delete -f examples/gke-a3-megagpu/nccl-jobset-flex.yaml
         




### Queued provisioning

For clusters configured with flex-start with queued provisioning, deploy the NCCL test by using the queued provisioning JobSet manifest:

  1. Deploy the NCCL test JobSet:
         
         kubectl create -f examples/gke-a3-megagpu/nccl-jobset-flex-queue.yaml
         

  2. Monitor the status of the JobSet Pods:
         
         kubectl get pods
         

  3. Inspect the benchmark results in the primary JobSet Pod logs:
         
         kubectl logs JOBSET_POD_NAME
         

Replace `JOBSET_POD_NAME` with the name of the primary JobSet Pod.

  4. When the test completes and Jobs show a `Completed` status, clean up the test resources:
         
         kubectl delete -f examples/gke-a3-megagpu/nccl-jobset-flex-queue.yaml
         




## Clean up resources created by Cluster Toolkit

To avoid recurring charges for the resources used on this page, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to clean up the resources provisioned by Cluster Toolkit, including the VPC networks and GKE cluster:
    
    
    cd ~/cluster-toolkit
    ./gcluster destroy CLUSTER_NAME/
    

Replace `CLUSTER_NAME` with the name of your cluster. For the clusters created with Cluster Toolkit, the cluster names are based on the `DEPLOYMENT_NAME` name.

## What's next

  * To learn about scheduling workloads on your GKE clusters by using Topology-Aware Scheduling (TAS) and Kueue, see [Schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).
  * To learn about managing common events that are relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).
  * For information about testing your environment for proper setup and optimization, see [Cluster networking optimization overview](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview).
  * To explore all supported consumption models for GKE clusters, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
