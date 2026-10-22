---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing/
title: Deploy TPU workloads with dynamic slicing \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:58.577323+00:00
---

# Deploy TPU workloads with dynamic slicing  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy TPU workloads with dynamic slicing Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to schedule workloads on Cloud TPU 7x clusters by using dynamic slicing and Topology-Aware Scheduling (TAS) with Cluster Toolkit.

Dynamic slicing provides flexibility in Cloud TPU capacity scheduling by letting you logically group or partition physical nodes at runtime. Whereas earlier Cloud TPU generations (such as Cloud TPU v4, v5e, v5p, and v6e) require static slice topologies configured when the node pool is created, dynamic slicing is supported starting with Cloud TPU 7x (Ironwood) and future Cloud TPU generations.

Dynamic slicing supports two scheduling modes on Cloud TPU 7x clusters:

  * **Dynamic superslicing:** This mode aggregates multiple physical Cloud TPU 7x `4x4x4` cubes into larger logical topologies (such as `4x4x8` or `4x4x16`) to run large-scale distributed training workloads across high-speed Inter-Chip Interconnect (ICI) links.
  * **Dynamic subslicing:** This mode partitions a single physical Cloud TPU 7x cube into smaller fractional topologies (such as `2x2x4` or `2x4x4`) to support workload bin-packing and multi-tenant scheduling without recreating node pools.



## Before you begin

Before you start, make sure that you have performed the following tasks:

  1. Install the [`gcluster` binary](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) and configure your environment. For more information, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. Install the Google Cloud SDK (`gcloud`), `kubectl`, and the `gke-gcloud-auth-plugin` authentication plugin.
  3. Verify that your project has quota for Cloud TPU 7x `tpu7x-standard-4t` nodes in your target zone.



### Required roles

To get the permissions that you need to deploy the GKE cluster and submit TPU jobs, ask your administrator to grant you the following IAM roles on your project: 

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

## Enable dynamic slicing in your blueprint

To enable dynamic slicing on a Cloud TPU 7x cluster, set the `enable_dynamic_slicing_for_tpus` variable to `true` and the `accelerator_topology_mode` variable to `PROVISION_ONLY` in the `vars` block of the advanced blueprint file ([`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml)). Dynamic slicing for Cloud TPU in GKE requires the `PROVISION_ONLY` topology mode rather than the `AUTO_ONLY` topology mode:
    
    
    vars:
      machine_type: tpu7x-standard-4t
      accelerator_type: tpu7x
      enable_dynamic_slicing_for_tpus: true
      accelerator_topology_mode: PROVISION_ONLY
    

When you set the `enable_dynamic_slicing_for_tpus` variable to `true` and the `accelerator_topology_mode` variable to `PROVISION_ONLY`, Cluster Toolkit configures the following cluster components and behaviors:

  * **Cloud TPU slice controller and workload policy in GKE:** Enables the slice controller, configures the workload policy with the `PROVISION_ONLY` topology mode, and configures partition-level topology definitions on the cluster.
  * **Kueue configuration for dynamic slicing:** Automatically selects the `kueue-configuration-dynamic-slicing.yaml.tftpl` template in the `modules/management/kubectl-apply/kueue/` directory, or the `kueue-configuration-dynamic-slicing-pathways.yaml.tftpl` template when Pathways is enabled. The selected template registers a `ResourceFlavor` custom resource (`tpu-flavor`, or `flavor-tpu7x` for Pathways) that targets the `cloud.google.com/gke-tpu-accelerator: tpu7x` node label. It also configures Topology-Aware Scheduling (TAS) levels. To use a custom configuration template for Kueue instead, set the `kueue.config_path` setting in your blueprint.

**Note:** For dynamic slicing at scale, we recommend that you scale the `kueue-controller-manager` deployment accordingly. For example, use 3 replicas with 16 vCPUs and `64Gi` of memory on a sufficiently sized CPU node pool, such as an `n2-standard-64` machine type.

To deploy your cluster with the updated configuration, complete the steps in [Deploy the advanced blueprint for a Cloud TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x#deploy-advanced-blueprint) before you submit workloads.

## How Cluster Toolkit schedules dynamic slices

When you submit a workload that targets the `tpu7x` compute type, Cluster Toolkit automatically translates your topology parameters into the scheduling annotations required by Kueue and the Cloud TPU slice controller in GKE:

  * **Partition topology mapping:** Maps the value of the [`gcluster job submit --topology` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags), such as `2x4x4` or `4x4x4`, to the `cloud.google.com/gke-tpu-partition-TOPOLOGY-id` requirement key for the partition topology.
  * **Slice topology annotation:** Injects the `cloud.google.com/gke-tpu-slice-topology` annotation into the Pod template of the generated JobSet.
  * **Single-slice and multi-slice TAS annotations:** When the [`--num-slices` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags) value is greater than 1, Cluster Toolkit injects the `kueue.x-k8s.io/podset-slice-size` annotation alongside the `kueue.x-k8s.io/podset-slice-required-topology` annotation.



## Submit the job

To submit a workload with dynamic slicing, run the [`gcluster job submit` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit) and set the `--compute-type` flag to `tpu7x` (or a chip-count alias such as `tpu7x-16` or machine type `tpu7x-standard-4t`) along with the `--topology` flag.

Submit a dynamic slicing job:
    
    
    ./gcluster job submit \
        --name JOB_NAME \
        --cluster CLUSTER_NAME \
        --location LOCATION \
        --compute-type tpu7x \
        --topology TOPOLOGY \
        --command "COMMAND" \
        --image IMAGE_NAME
    

Replace the following:

  * `JOB_NAME`: the name of the job to create.
  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `LOCATION`: the zone or region of your cluster.
  * `TOPOLOGY`: the target slice topology for Cloud TPU 7x, such as `2x2x4`, `2x4x4`, `4x4x4`, or `4x4x8`.
  * `COMMAND`: the command to run inside the container for your workload.
  * `IMAGE_NAME`: the URI of your container image. You can also build and push a container image on the fly by setting the `GCLUSTER_IMAGE_REPO` environment variable and passing the `--base-image` and `--build-context` flags instead of `--image`.



If you run a multi-slice workload across multiple dynamic slices, then include the `--num-slices` flag to specify the number of slices to allocate.

## Verify the job

To verify that your job is scheduled with the expected topology annotations and is running on your cluster, do the following:

  1. Inspect the job status and generated JobSet manifest by using the [`gcluster job inspect` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-inspect):
         
         ./gcluster job inspect \
             --name JOB_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION \
             --show
         

  2. List the jobs in your cluster by using the [`gcluster job list` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-list):
         
         ./gcluster job list \
             --cluster CLUSTER_NAME \
             --location LOCATION
         

  3. Stream the container logs for your job to verify JAX initialization and the execution of training steps by using the [`gcluster job logs` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-logs):
         
         ./gcluster job logs JOB_NAME \
             --cluster CLUSTER_NAME \
             --location LOCATION
         




## What's next

  * [Deploy a GKE Cloud TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x).
  * Learn more about [GKE deployment options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).
  * Understand [Dynamic slicing concepts](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview#dynamic-slicing).
  * Learn how to [run workloads with Pathways](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
