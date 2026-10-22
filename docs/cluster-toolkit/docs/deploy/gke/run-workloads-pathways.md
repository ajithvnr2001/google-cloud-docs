---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways/
title: Run workloads with Pathways \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:57.947796+00:00
---

# Run workloads with Pathways  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Run workloads with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to run distributed AI workloads by using the Pathways framework on Google Kubernetes Engine (GKE) clusters deployed with Cluster Toolkit.

Pathways is a distributed AI execution framework designed to coordinate large-scale multi-slice Cloud TPU workloads under a single-controller programming model. You can use Cluster Toolkit to deploy Pathways workloads across independent Cloud TPU slices without manually writing multi-role Kubernetes JobSet manifests.

## How Pathways workloads are orchestrated

When you submit a workload with the [`gcluster job submit --pathways` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags), Cluster Toolkit automatically generates a Kubernetes JobSet manifest that coordinates three functional roles:

  * **ResourceManager (`pathways-rm`):** A CPU-based coordinator service that manages Cloud TPU slice allocations, topology assignments, and elastic worker recovery across slices.
  * **Proxy (`pathways-proxy`):** An IFRT proxy server that compiles and dispatches client JAX programs across the allocated Cloud TPU slices.
  * **Workers and co-located sidecars:** Cloud TPU worker Pods that execute compiled XLA computations alongside optional co-located Python sidecar containers.



## Before you begin

Before you start, make sure that you have performed the following tasks:

  1. Install the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and configure your environment. For more information, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. Install the Google Cloud SDK (`gcloud`), `kubectl`, and the `gke-gcloud-auth-plugin` authentication plugin.
  3. Create a Cloud Storage bucket in the same region as your cluster. Pathways uses this bucket to store temporary job files and cached compiled code so that workloads don't need to recompile on restart.



### Required roles

To get the permissions that you need to deploy the GKE cluster and submit Pathways jobs, ask your administrator to grant you the following IAM roles on your project: 

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

To ensure that the workload service account has the necessary permissions to store temporary job files and cached compiled code for Pathways, ask your administrator to grant the following IAM roles to the workload service account on your Cloud Storage bucket: 

**Important:** You must grant these roles to the workload service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the workload service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable Pathways in your blueprint

In the advanced Cloud TPU blueprints, [`examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-v6e/gke-tpu-v6e-advanced.yaml) and [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml), the `enable_pathways_for_tpus` variable is set to `true` in the `vars` block by default:
    
    
    vars:
      enable_pathways_for_tpus: true
    

To deploy a GKE cluster with the advanced blueprint, complete the steps in [Deploy the advanced blueprint for a Cloud TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e#deploy-advanced-blueprint) or [Deploy the advanced blueprint for a Cloud TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x#deploy-advanced-blueprint).

### Cluster configuration requirements

When you set the `enable_pathways_for_tpus` variable to `true` in your [`gke-cluster` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/gke-cluster), Cluster Toolkit applies the following configuration:

  * **Dedicated CPU node pool for the coordinator:** Cluster Toolkit creates a dedicated, autoscaled (0-100 nodes) CPU node pool named `cpu-np` by using the `n4-standard-64` machine type.
  * **Kueue configuration for Pathways:** The `kueue-configuration-pathways.yaml.tftpl` template binds the `pathways-flavor` `ResourceFlavor` custom resource to the `cloud.google.com/gke-nodepool: cpu-np` node pool. The `cpu-np` node pool is automatically provisioned when you set the value `enable_pathways_for_tpus: true`, or when you use the [`--pathways-head-np` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags) to override the default CPU node pool. To specify a custom configuration template for Kueue, set the `kueue.config_path` setting in your blueprint.
  * **Unified resource groups in Kueue:** Because Cloud TPU worker Pods in a Pathways JobSet request CPU, memory, and `google.com/tpu` resources simultaneously, Cluster Toolkit groups `["google.com/tpu", "cpu", "memory"]` into a single resource group in the Kueue `ClusterQueue` (`tpu_flavor_cpu_quota`, `tpu_flavor_memory_quota`, and `tpu_quota`) to prevent conflicts between resource flavors. You can override these default quotas in the `config_template_vars` block of your Kueue module.



Use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to deploy your cluster with the updated blueprint before you submit Pathways jobs.

## Test your Pathways infrastructure with headless mode

You can deploy persistent Pathways infrastructure without running an in-cluster workload container by passing the [`--pathways-headless` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags). Headless mode lets you connect interactively to the Pathways cluster from an external client, such as a local workstation or notebook environment.

When you enable headless mode with the `--pathways-headless` flag, the `--image`, `--base-image`, and `--command` flags are not required.

To deploy a headless Pathways cluster and connect an external client, do the following:

  1. Submit a headless Pathways job by using the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit):
         
         ./gcluster job submit \
           --name JOB_NAME \
           --cluster CLUSTER_NAME \
           --location LOCATION \
           --compute-type COMPUTE_TYPE \
           --pathways \
           --pathways-gcs-location gs://BUCKET_NAME/PATHWAYS_PREFIX \
           --pathways-headless
         

  2. Get the name of the Pathways head Pod:
         
         kubectl get pods \
           -l jobset.sigs.k8s.io/jobset-name=JOB_NAME,jobset.sigs.k8s.io/replicatedjob-name=pathways-head
         

  3. Forward local port `29000` to container port `29000` on the Pathways proxy server:
         
         kubectl port-forward PATHWAYS_HEAD_POD_NAME 29000:29000
         

Replace `PATHWAYS_HEAD_POD_NAME` with the name of the Pathways head Pod from the output of the `kubectl get pods` command.

  4. Initialize your JAX client to connect to the forwarded proxy endpoint at `grpc://127.0.0.1:29000`.




## Submit a Pathways job

To submit a Pathways workload, run the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) with the `--pathways` and `--pathways-gcs-location` flags.

Submit a Pathways job:
    
    
    ./gcluster job submit \
      --name JOB_NAME \
      --cluster CLUSTER_NAME \
      --location LOCATION \
      --compute-type COMPUTE_TYPE \
      --num-slices NUM_SLICES \
      --pathways \
      --pathways-gcs-location gs://BUCKET_NAME/PATHWAYS_PREFIX \
      --command "COMMAND" \
      --image IMAGE_NAME
    

Replace the following:

  * `JOB_NAME`: the name of the JobSet to create.
  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `LOCATION`: the zone or region of your cluster.
  * `COMPUTE_TYPE`: the Cloud TPU compute target, such as `v6e-16` or `ct6e-standard-4t` for Cloud TPU v6e, or `tpu7x`, `tpu7x-16`, or `tpu7x-standard-4t` for Cloud TPU 7x.
  * `NUM_SLICES`: the number of Cloud TPU slices to allocate to the job (for example, `2`).
  * `BUCKET_NAME`: the name of your Cloud Storage bucket for temporary job files and cached compiled code for Pathways.
  * `PATHWAYS_PREFIX`: the folder prefix in your Cloud Storage bucket.
  * `COMMAND`: the command to run inside the container for your JAX workload.
  * `IMAGE_NAME`: the URI of the container image for your workload. To build and push an image as needed from a local directory instead, set the `GCLUSTER_IMAGE_REPO` environment variable and pass the `--base-image` and `--build-context` flags.

**Note:** If your workload requires a custom container image for the co-located Python sidecar on each Cloud TPU worker, then include the `--pathways-colocated-python-sidecar-image` flag.

## Verify the job

To verify that your Pathways JobSet is scheduled and running, use the following [`gcluster job` commands](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job):

  1. Inspect the JobSet status and generated manifest by using the [`gcluster job inspect` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-inspect):
         
         ./gcluster job inspect \
           --name JOB_NAME \
           --cluster CLUSTER_NAME \
           --location LOCATION \
           --show
         

  2. List the jobs in your cluster by using the [`gcluster job list` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-list):
         
         ./gcluster job list \
           --cluster CLUSTER_NAME \
           --location LOCATION
         

  3. Stream the logs for your job by using the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs):
         
         ./gcluster job logs JOB_NAME \
           --cluster CLUSTER_NAME \
           --location LOCATION
         




## What's next

  * Learn more about [GKE deployment options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).
  * Understand [Pathways distributed AI orchestration](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview#pathways).
  * Learn how to [deploy TPU workloads with dynamic slicing](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
