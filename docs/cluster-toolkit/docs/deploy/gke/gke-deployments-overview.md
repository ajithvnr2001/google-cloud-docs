---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview/
title: GKE deployments overview \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:22:30.434977+00:00
---

# GKE deployments overview  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  GKE deployments overview Stay organized with collections  Save and categorize content based on your preferences. 

Cluster Toolkit simplifies the deployment and management of Google Kubernetes Engine (GKE) clusters that are optimized for artificial intelligence (AI) and machine learning (ML) workloads. By using Cluster Toolkit blueprints, you can provision infrastructure that integrates compute resources, storage, and high-bandwidth networking tailored for training and serving large-scale models.

To choose the configuration that aligns with your workload requirements and budget, review the available accelerator deployment options, compute consumption models, and advanced orchestration features.

## Deployment choices for AI/ML workloads

When you plan your deployment, you can choose between two main accelerator paradigms in GKE:

  * **Graphics Processing Units (GPUs):** High-performance accelerators that support general-purpose parallel processing and deep learning frameworks. Cluster Toolkit provides blueprints for GPU machine families that are suitable for diverse AI/ML training and inference tasks.
  * **Cloud TPU (TPUs):** Custom-designed application-specific integrated circuits (ASICs) developed by Google to accelerate machine learning workloads. You can deploy Cloud TPU node pools for large-scale distributed training and inference. For more information about Cloud TPU deployments in Cluster Toolkit, see [Cloud TPU deployments overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview).



### Compute consumption options

Across GPU and Cloud TPU blueprints, Cluster Toolkit lets you provision capacity by using multiple compute consumption models:

  * Standard and future reservations
  * Dynamic Workload Scheduler flex-start provisioning mode
  * Dynamic Workload Scheduler flex-start with queued provisioning
  * Spot VMs
  * On-demand capacity



You can configure these consumption models statically in the YAML file for your cluster deployment or provision on-demand, Spot VMs, and reserved capacity dynamically at job submission time by enabling node auto-provisioning (NAP).

## Advanced orchestration features

Cluster Toolkit integrates with GKE scheduling features and distributed execution frameworks to automate the management of AI/ML infrastructure.

### Node auto-provisioning (NAP)

Node auto-provisioning (NAP) is an autoscaling feature for GKE clusters that dynamically creates and deletes node pools based on the resource requirements of unschedulable Pods. Instead of manually maintaining fixed node pools, NAP provisions node pools with matching machine types and accelerators on demand.

NAP with Cluster Toolkit provides the following benefits:

  * **Cost efficiency:** Virtual machine (VM) instances are provisioned when you submit workloads and scaled down when idle, which reduces costs for idle capacity.
  * **Targeting of consumption models:** You can submit jobs that use default on-demand provisioning or target Spot VMs and local or shared Compute Engine reservations by passing CLI flags, while Dynamic Workload Scheduler flex-start and Dynamic Workload Scheduler flex-start with queued provisioning are supported through static cluster blueprints.
  * **Pre-flight validation of limits:** Before creating a workload, the [`gcluster` CLI](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) verifies that the requested machine type and accelerator counts are within the `cluster_autoscaling` limits configured in your cluster blueprint.



For more information about node auto-provisioning in GKE, see [About node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning).

### Pathways distributed AI orchestration

Pathways is a distributed AI execution framework designed to coordinate large-scale multi-slice Cloud TPU workloads under a single-controller architecture. When you enable the `enable_pathways_for_tpus` variable in your blueprint and submit a job with the [`gcluster job submit --pathways` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags), Cluster Toolkit automatically generates a multi-role Kubernetes JobSet manifest. This manifest contains the Pathways ResourceManager (`pathways-rm`), the Interim Framework Runtime (IFRT) proxy (`pathways-proxy`), and Cloud TPU workers with optional co-located sidecar containers. The IFRT proxy acts as the runtime bridge that compiles and dispatches JAX programs from the client across the allocated Cloud TPU slices.

Pathways integration provides the following capabilities:

  * **Automated multi-slice coordination:** Coordinates dynamic initialization, compilation caching in Cloud Storage, and unified quotas for Kueue resource groups (`google.com/tpu`, `cpu`, and `memory`) across independent Cloud TPU slices.
  * **Resilient and interactive execution:** Supports restart-safe training across elastic slices as well as headless mode (`--pathways-headless`), which lets external JAX clients and notebooks connect to persistent in-cluster Pathways infrastructure over port forwarding.



For more information about Pathways, see [Introduction to Pathways on Cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-intro).

### Dynamic slicing

Dynamic slicing provides runtime flexibility in Cloud TPU capacity scheduling starting with Cloud TPU 7x (Ironwood) and future Cloud TPU generations. Whereas earlier Cloud TPU generations require fixed slice topologies configured when the node pool is created, dynamic slicing lets physical Cloud TPU cubes be grouped or partitioned dynamically per workload.

Dynamic slicing provides the following capabilities:

  * **Dynamic superslicing and subslicing:** You can aggregate multiple physical Cloud TPU 7x `4x4x4` cubes into larger logical topologies (such as `4x4x8` or `4x4x16`) for large models, or partition a single physical cube into fractional topologies (such as `2x2x4` or `2x4x4`) for multi-tenant bin-packing.
  * **Topology-Aware Scheduling (TAS) integration:** When you set the `enable_dynamic_slicing_for_tpus` variable to `true` in your blueprint and submit workloads targeting the `tpu7x` compute type, Cluster Toolkit automatically configures the Cloud TPU slice controller in GKE and injects single-slice or multi-slice TAS annotations for Kueue to minimize latency across network hops.



For more information about dynamic slicing in GKE, see [About GKE dynamic slicing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dynamic-slicing).

### Kueue workload queuing and priority classes

Cluster Toolkit GKE blueprints configure [Kueue](https://kueue.sigs.k8s.io/) by default to manage batch job queuing, quota allocation, and topology-aware scheduling. The Kueue configurations in the blueprints include five preconfigured Kubernetes `WorkloadPriorityClass` resources (`very-low: 100`, `low: 250`, `medium: 500`, `high: 750`, and `very-high: 1000`) so that you can prioritize critical training jobs and configure preemption for workloads across queues without authoring custom manifests for priorities. Kueue selects jobs for scheduling based on their numeric priority values that you set with the [`gcluster job submit --priority` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags).

For more information about scheduling workloads with Kueue and Topology-Aware Scheduling, see [Schedule GKE workloads with Topology Aware Scheduling](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas).

### Workload submission and custom manifest templates

The [`gcluster job` command group](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job) lets you build, submit, and monitor distributed training jobs on your GKE cluster without manually authoring Kubernetes YAML manifests:

  * **Prebuilt and on-the-fly container images:** Submit workloads using an existing container image (`--image`), or build and push an image on the fly from a local directory by setting the `GCLUSTER_IMAGE_REPO` environment variable and passing the `--base-image` and `--build-context` flags.
  * **Custom templates for Kubernetes manifests:** If your workload requires custom sidecar containers, volume mounts, or specialized security contexts for Pods that are not exposed by CLI flags, then you can export the embedded Go templates (`job.yaml.tmpl` and `pathways-job.yaml.tmpl`) to a local directory by running the [`gcluster job gke-template-extract --output-dir TEMPLATE_DIR` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-gke-template-extract), modify the templates, and pass them to job submissions by using the [`--gke-custom-templates-path` flag](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-job-submit#flags).



## What's next

  * Learn how to [deploy a cluster with node auto-provisioning](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-cluster-nap).
  * Learn how to [run workloads with Pathways](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/run-workloads-pathways).
  * Learn how to [deploy TPU workloads with dynamic slicing](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/deploy-tpu-dynamic-slicing).
  * Learn about [Cloud TPU deployments in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
