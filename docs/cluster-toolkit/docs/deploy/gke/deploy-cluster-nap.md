---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap/
title: Deploy a cluster with node auto-provisioning \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:22:13.483559+00:00
---

# Deploy a cluster with node auto-provisioning  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy a cluster with node auto-provisioning Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to enable node auto-provisioning (NAP) in your cluster blueprint and submit workloads that target specific compute consumption models with Cluster Toolkit.

NAP is a cluster autoscaler feature in Google Kubernetes Engine (GKE) that dynamically creates and deletes node pools based on the resource requirements of unschedulable Pods. Cluster Toolkit integrates with NAP to let you provision compute nodes dynamically when you submit workloads and target on-demand capacity, Spot VMs, or standard and future reservations.

**Note:** With NAP enabled, Cluster Toolkit supports on-demand, Spot VMs, and reservation consumption models when you submit workloads. To configure Dynamic Workload Scheduler flex-start provisioning mode, Dynamic Workload Scheduler flex-start with queued provisioning, or static node pools, define them in your cluster deployment file or blueprint.

## Before you begin

Before you start, make sure that you have performed the following tasks:

  1. Install the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and configure your environment. For more information, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. [Install the Google Cloud SDK (`gcloud`)](https://docs.cloud.google.com/sdk/docs/install-sdk), [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_kubectl), and the [`gke-gcloud-auth-plugin` authentication plugin](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).
  3. [Authenticate with the `gcloud` CLI](https://docs.cloud.google.com/sdk/docs/authenticate) and [set up Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).
  4. [Configure Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication) for Container Registry and Artifact Registry.
  5. [Enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service#enable) (`artifactregistry.googleapis.com`) in your project.



### Required roles

To get the permissions that you need to deploy the GKE cluster and submit workloads, ask your administrator to grant you the following IAM roles on your project: 

  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Role Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleAdmin) (`roles/iam.roleAdmin`)
  * [Secret Manager Secret Version Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable NAP in your blueprint

To enable NAP, add the `cluster_autoscaling` block to the [`gke-cluster` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster) in the YAML file for your cluster blueprint:
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: CLUSTER_MODULE_ID
        source: modules/scheduler/gke-cluster
        settings:
          cluster_autoscaling:
            enabled: true
            service_account_email: SERVICE_ACCOUNT_EMAIL
            oauth_scopes: OAUTH_SCOPES
            autoprovisioning_disk_size_gb: DISK_SIZE_GB
            autoprovisioning_disk_type: DISK_TYPE
            autoprovisioning_cpu_max: MAX_CPU_CORES
            autoprovisioning_memory_max: MAX_MEMORY_GB
            limits:
            - autoprovisioning_machine_type: MACHINE_TYPE
              autoprovisioning_max_count: MAX_ACCELERATOR_COUNT
    

Replace the following:

  * `CLUSTER_MODULE_ID`: the ID of your [`gke-cluster` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster), such as `my-gke-cluster`.
  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account tied to node provisioning, or `null` to use the default deployment service account.
  * `OAUTH_SCOPES`: a list of OAuth scopes assigned to nodes that are provisioned by NAP. The default value is `["https://www.googleapis.com/auth/cloud-platform"]`.
  * `DISK_SIZE_GB`: the boot disk size in gigabytes (GB) for auto-provisioned nodes, such as `100`. The value must be at least `10`, and the default value is `100`.
  * `DISK_TYPE`: the boot disk type for auto-provisioned nodes. Accepted values are `pd-standard`, `pd-balanced`, `pd-ssd`, and `hyperdisk-balanced`. The default value is `pd-balanced`.
  * `MAX_CPU_CORES`: the maximum number of CPU cores that NAP can provision across the cluster, such as `100`. The default value is `1000000` (1,000,000).
  * `MAX_MEMORY_GB`: the maximum memory limit in GB that NAP can provision across the cluster, such as `100`. The default value is `10000000` (10,000,000).
  * `MACHINE_TYPE`: the Compute Engine machine type in the `limits` list. For example, `a4-highgpu-8g` or `ct5lp-hightpu-4t`. Cluster Toolkit dynamically consumes the `autoprovisioning_machine_type` field to resolve the underlying accelerator resource name in GKE (`autoprovisioning_resource_type`, such as `nvidia-h100-80gb`) expected by Terraform. You can add multiple entries to the `limits` list.
  * `MAX_ACCELERATOR_COUNT`: the maximum number of accelerators of the specified type that NAP can provision, such as `32` or `8`. The default value is `1000`.



For example, the following configuration enables NAP with a 100 GB balanced persistent disk, limits cluster scaling to 100 CPU cores and 100 GB of memory, and defines scaling limits for both `a4-highgpu-8g` GPU nodes and `ct5lp-hightpu-4t` Cloud TPU nodes:
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: my-gke-cluster
        source: modules/scheduler/gke-cluster
        settings:
          cluster_autoscaling:
            enabled: true
            service_account_email: null
            oauth_scopes: []
            autoprovisioning_disk_size_gb: 100
            autoprovisioning_disk_type: pd-balanced
            autoprovisioning_cpu_max: 100
            autoprovisioning_memory_max: 100
            limits:
            - autoprovisioning_machine_type: a4-highgpu-8g
              autoprovisioning_max_count: 32
            - autoprovisioning_machine_type: ct5lp-hightpu-4t
              autoprovisioning_max_count: 8
    

**Warning:** Enabling cluster autoscaling defaults to 1,000,000 CPU cores and 10,000,000 GB of memory unless you pass specific limits. To help prevent large unexpected billed charges if a workload misconfiguration occurs, configure explicit upper bounds in the `autoprovisioning_cpu_max`, `autoprovisioning_memory_max`, and `limits` fields.

### Configuration requirements

When you configure NAP in your blueprint, ensure that your settings meet the following requirements:

  * **Limits for accelerator resources:** You must explicitly include each target GPU or Cloud TPU machine type in the `limits` list of the `cluster_autoscaling` block. Cluster Toolkit resolves each `autoprovisioning_machine_type` entry to the corresponding limit for GKE accelerator resources. If a target machine type or accelerator resource type is omitted from the `limits` list, then the GKE cluster autoscaler doesn't provision node pools for that accelerator.
  * **Alignment of Kueue quotas:** Ensure that the nominal resource quotas defined in your Kueue `ClusterQueue` manifests align with the maximum boundaries specified in your `cluster_autoscaling` configuration (such as `autoprovisioning_cpu_max`, `autoprovisioning_memory_max`, and `limits`).
  * **Pre-flight verification of limits:** Before submitting a workload, the [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) queries the metadata for the GKE cluster to verify that the requested machine type and accelerator resources are permitted by the `cluster_autoscaling` configuration for NAP. If the requested resources exceed the configured limits, then the CLI exits before creating the JobSet and returns a diagnostic error.



Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy your cluster with the updated blueprint before you submit workloads.

## Submit workloads targeting consumption models

The [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) submits a workload to a cluster. On GKE clusters, Cluster Toolkit deploys workloads as Kubernetes JobSets integrated with Kueue.

After you deploy a NAP-enabled cluster, standard workload submissions that omit the `--gke-nap-*` flags automatically trigger the creation of on-demand node pools when existing nodes lack capacity. To target Spot VMs or specific Compute Engine reservations, include the `--gke-nap-provisioning` and `--gke-nap-reservation` flags.

You can supply a prebuilt container image by using the `--image` flag, or build and push an image on the fly from a local directory by setting the `GCLUSTER_IMAGE_REPO` environment variable and passing the `--base-image` and `--build-context` flags.

### Target Spot VMs

You can run your workload on Spot VMs by specifying `spot` with the `--gke-nap-provisioning` flag. When you set this flag, Cluster Toolkit injects the `cloud.google.com/gke-provisioning=spot:NoSchedule` toleration and the `cloud.google.com/gke-provisioning: spot` node selector into the generated Kubernetes JobSet manifest.

Submit a workload targeting Spot VMs by using the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit):
    
    
    ./gcluster job submit \
        --name JOB_NAME \
        --cluster CLUSTER_NAME \
        --location LOCATION \
        --compute-type COMPUTE_TYPE \
        --gke-nap-provisioning spot \
        --command "COMMAND" \
        --image IMAGE_NAME
    

Replace the following:

  * `JOB_NAME`: the name of the workload to create.
  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `LOCATION`: the region or zone of your cluster.
  * `COMPUTE_TYPE`: the hardware compute target—for example, `g2-4` or `h100-8`.
  * `COMMAND`: the command to run inside the container for your workload.
  * `IMAGE_NAME`: the URI of your container image.



### Target reservations

You can target a specific Compute Engine reservation by setting the `--gke-nap-provisioning` flag to `reservation` and specifying the `--gke-nap-reservation` flag. When you pass these flags, Cluster Toolkit injects the `cloud.google.com/reservation-name=RESERVATION_NAME:NoSchedule` toleration along with the `cloud.google.com/reservation-affinity: specific` and `cloud.google.com/reservation-name` labels for the node selector.

Submit a workload targeting a local or shared reservation by using the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit):
    
    
    ./gcluster job submit \
        --name JOB_NAME \
        --cluster CLUSTER_NAME \
        --location LOCATION \
        --compute-type COMPUTE_TYPE \
        --gke-nap-provisioning reservation \
        --gke-nap-reservation RESERVATION_IDENTIFIER \
        --command "COMMAND" \
        --image IMAGE_NAME
    

Replace `RESERVATION_IDENTIFIER` with one of the following values:

  * **Local reservation:** the name of a reservation in the same project as the cluster—for example, `my-gpu-reservation`.
  * **Shared reservation:** the full resource URI in Google Cloud for a shared reservation in another project: `projects/PROJECT_ID/reservations/RESERVATION_NAME`. When you provide a full resource URI, Cluster Toolkit automatically extracts the project ID and sets the `cloud.google.com/reservation-project` label alongside the `cloud.google.com/reservation-name` label in the node selector.



## Verify scaling and monitor workloads

To verify that NAP provisions nodes for your workload and to monitor workload execution, do the following:

  1. Inspect the workload status and generated manifest for the Kubernetes JobSet by using the [`gcluster job inspect` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-inspect):
         
         ./gcluster job inspect \
             --name JOB_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION \
             --show
         

If the workload remains in a pending state, then verify that the requested machine type and accelerator count are within the `limits` list configured in your cluster blueprint.

  2. Stream the container logs for the running workload by using the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs):
         
         ./gcluster job logs JOB_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION
         

  3. Optional: To stop a running or queued workload and let NAP scale down idle nodes, cancel the workload by using the [`gcluster job cancel` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-cancel):
         
         ./gcluster job cancel JOB_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION
         




## What's next

  * Learn more about [GKE deployment options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).
  * Understand [node auto-provisioning concepts](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview#nap).
  * Learn about [node auto-provisioning in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
