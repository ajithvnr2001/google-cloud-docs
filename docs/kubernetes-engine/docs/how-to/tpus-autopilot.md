---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot/
title: Deploy TPU workloads on GKE Autopilot \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:21.399437+00:00
---

# Deploy TPU workloads on GKE Autopilot  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy TPU workloads on GKE Autopilot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page describes how to accelerate machine learning (ML) workloads by using Cloud TPU accelerators (TPUs) in Google Kubernetes Engine (GKE) Autopilot clusters. This guidance can help you to select the correct libraries for your ML application frameworks, set up your TPU workloads to run optimally on GKE, and monitor your workloads after deployment.

This page is for Platform admins and operators, Data and AI specialists, and Application developers who want to prepare and run ML workloads on TPUs. To learn more about the common roles, responsibilities, and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following resources:

  * [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)
  * [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions)
  * [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)



## How TPUs work in Autopilot

To use TPUs in Autopilot workloads, you specify the following in your workload manifest:

  * The TPU version in the `spec.nodeSelector` field.
  * The TPU topology in the `spec.nodeSelector` field. The topology must be supported by the specified TPU version.
  * The number of TPU chips in the `spec.containers.resources.requests` and the `spec.containers.resources.limits` fields.



When you deploy the workload, GKE provisions nodes that have the requested TPU configuration and schedules your Pods on the nodes. GKE places each workload on its own node so that each Pod can access the full resources of the node with minimized risk of disruption.

TPUs in Autopilot are compatible with the following capabilities:

  1. [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods)
  2. [Specific capacity reservations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#consume-capacity-autopilot)
  3. [Extended run time Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods)
  4. [Flex-start](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws)



## Plan your TPU configuration

Before you use this guide to deploy TPU workloads, plan your TPU configuration based on your model and how much memory it requires. For details, see [Plan your TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#plan-tpu-configuration).

## Pricing

For pricing information, see [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an Autopilot cluster running GKE version 1.32.3-gke.1927000 or later. For instructions, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * To use reserved TPUs, ensure that you have an existing _specific_ capacity reservation. For instructions, see [Consume a reservation](https://docs.cloud.google.com/tpu/docs/consume-reservation-compute).



## Ensure quota for TPUs and other GKE resources

The following sections help you ensure that you have enough quota when using TPUs in GKE. To create TPU slice nodes, you must have TPU quota available unless you're using an existing capacity reservation. If you're using reserved TPUs, skip this section. 

Creating TPU slice nodes in GKE requires _Compute Engine API quota_ (compute.googleapis.com), not Cloud TPU API quota (tpu.googleapis.com). The name of the quota is different in regular Autopilot Pods and in Spot Pods. 

To check the limit and current usage of your Compute Engine API quota for TPUs, follow these steps:

  1. Go to the **Quotas** page in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter_list **Filter** box, do the following:

     1. Use the following table to select and copy the property of the quota based on the TPU version and value in the `cloud.google.com/gke-tpu-accelerator` node selector. For example, if you plan to create on-demand TPU v5e nodes whose value in the `cloud.google.com/gke-tpu-accelerator` node selector is `tpu-v5-lite-podslice`, enter `Name: TPU v5 Lite PodSlice chips`.

TPU version, `cloud.google.com/gke-tpu-accelerator` | Property and name of the quota for on-demand instances | Property and name of the quota for Spot2 instances  
---|---|---  
TPU v3,  
`tpu-v3-device` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3

| Not applicable  
TPU v3,  
`tpu-v3-slice` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3P

| Not applicable  
TPU v4,  
`tpu-v4-podslice` | 
            
            Name:  
            TPU v4 PodSlice chips

| 
            
            Name:  
            Preemptible TPU v4 PodSlice chips  
  
TPU v5e,  
`tpu-v5-lite-podslice` | 
            
            Name:  
            TPU v5 Lite PodSlice chips

| 
            
            Name:  
            Preemptible TPU v5 Lite Podslice  
            chips  
  
TPU v5p,  
`tpu-v5p-slice` | 
            
            Name:  
            TPU v5p chips

| 
            
            Name:  
            Preemptible TPU v5p chips  
  
TPU Trillium,  
`tpu-v6e-slice` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT6E

| 
            
            Name:  
            Preemptible TPU slices v6e  
  
Ironwood (TPU7x),  
`tpu7x` | 
            
            Dimensions (e.g. location):  
            tpu_family:tpu7x

| 
            
            Name:  
            Preemptible TPU slices tpu7x  
  
     2. Select the **Dimensions (e.g. locations)** property and enter `region:` followed by the name of the region in which you plan to create TPUs in GKE. For example, enter `region:us-west4` if you plan to create TPU slice nodes in the zone `us-west4-a`. TPU quota is regional, so all zones within the same region consume the same TPU quota.




If no quotas match the filter you entered, then the project has not been granted any of the specified quota for the region that you need, and you must [request a TPU quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

When a TPU reservation is created, both the limit and current use values for the corresponding quota increase by the number of chips in the TPU reservation. For example, when a reservation is created for 16 TPU v5e chips whose value in the `cloud.google.com/gke-tpu-accelerator` node selector is `tpu-v5-lite-podslice`, then both the **Limit** and **Current usage** for the `TPU v5 Lite PodSlice chips` quota in the relevant region increase by 16.

### Quotas for additional GKE resources

You may need to increase the following GKE-related quotas in the regions where GKE creates your resources.

  * **Persistent Disk SSD (GB) quota** : The boot disk of each Kubernetes node requires 100GB by default. Therefore, this quota should be set at least as high as the product of the maximum number of GKE nodes you anticipate creating and 100GB (nodes * 100GB).
  * **In-use IP addresses quota** : Each Kubernetes node consumes one IP address. Therefore, this quota should be set at least as high as the maximum number of GKE nodes you anticipate creating.
  * **Ensure that`max-pods-per-node` aligns with the subnet range**: Each Kubernetes node uses secondary IP ranges for Pods. For example, `max-pods-per-node` of 32 requires 64 IP addresses which translates to a /26 subnet [per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#cidr_ranges_for_clusters). Note that this range shouldn't be shared with any other cluster. To avoid exhausting the IP address range, use the `--max-pods-per-node` flag to limit the number of pods allowed to be scheduled on a node. The quota for `max-pods-per-node` should be set at least as high as the maximum number of GKE nodes you anticipate creating.



To request an increase in quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Prepare your TPU application

TPU workloads have the following preparation requirements.

  1. Frameworks like JAX, PyTorch, and TensorFlow access TPU VMs using the `libtpu` shared library. `libtpu` includes the XLA compiler, TPU runtime software, and the TPU driver. Each release of PyTorch and JAX requires a certain `libtpu.so` version. To avoid package version conflicts, we recommend using a [JAX AI image](https://docs.cloud.google.com/ai-hypercomputer/docs/images#current_jax_ai_images). To use TPUs in GKE, ensure that you use the following versions: TPU type | `libtpu.so` version  
---|---  
Ironwood (TPU7x) `tpu7x`  
| 
     * Recommended JAX AI image: [jax0.8.1-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.8.1-rev1)
     * Recommended jax[tpu] version: [v0.8.1](https://github.com/jax-ml/jax/tree/jax-v0.8.1)  
TPU Trillium (v6e)  
`tpu-v6e-slice`  
| 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [v0.4.9 or later](https://github.com/google/jax/tree/jaxlib-v0.4.9)
     * Recommended torchxla[tpuvm] version: [v2.1.0 or later](https://github.com/pytorch/xla/releases/tag/v2.1.0)  
TPU v5e  
`tpu-v5-lite-podslice`  
| 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [v0.4.9 or later](https://github.com/google/jax/tree/jaxlib-v0.4.9)
     * Recommended torchxla[tpuvm] version: [v2.1.0 or later](https://github.com/pytorch/xla/releases/tag/v2.1.0)  
TPU v5p  
`tpu-v5p-slice` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu] version: [0.4.19 or later](https://github.com/google/jax/tree/jax-v0.4.19).
     * Recommended torchxla[tpuvm] version: suggested to use a nightly version build on October 23, 2023.  
TPU v4  
`tpu-v4-podslice` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu]: [v0.4.4 or later](https://github.com/google/jax/tree/jaxlib-v0.4.4)
     * Recommended torchxla[tpuvm]: [v2.0.0 or later](https://github.com/pytorch/xla/releases/tag/v2.0.0)  
TPU v3  
`tpu-v3-slice`  
`tpu-v3-device` | 
     * Recommended JAX AI image: [jax0.4.35-rev1 or later](https://us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.4.35-rev1)
     * Recommended jax[tpu]: [v0.4.4 or later](https://github.com/google/jax/tree/jaxlib-v0.4.4)
     * Recommended torchxla[tpuvm]: [v2.0.0 or later](https://github.com/pytorch/xla/releases/tag/v2.0.0)  
  2. In your workload manifest, add Kubernetes node selectors to ensure that GKE schedules your TPU workload on the TPU machine type and TPU topology you defined: 
         
         nodeSelector:
             cloud.google.com/gke-tpu-accelerator: TPU_ACCELERATOR
             cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY
             cloud.google.com/placement-policy-name: WORKLOAD_POLICY # Required only for Ironwood (TPU7x)
           

Replace the following:

     * `TPU_ACCELERATOR`: the name of the [TPU accelerator](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version). For example, use `tpu7x-standard-4t`.
     * `TPU_TOPOLOGY`: the physical topology for the TPU slice. The format of the topology depends on the TPU version. For example, use `2x2x2`. To learn more, see [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `WORKLOAD_POLICY`: the name of the workload policy that you want to use to place your TPU Pods. This node selector is required only for Ironwood (TPU7x).



After you complete the workload preparation, you can run a Job that uses TPUs.

## Options for provisioning TPUs in GKE

To provision TPUs in GKE you have the following configuration options: 
* **Workload request** : you specify the TPU version and topology in the `spec.nodeSelector` field and the number of TPU chips in the `spec.containers.resources` section. When you deploy the workload, GKE automatically provisions nodes with the correct TPU configuration and places each workload on its own dedicated node to ensure full access to the node's resources. For instructions, see the [Request TPUs in a workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#request-tpus). 

### Centrally provision TPUs with custom compute classes

The following sections show you how to create a custom ComputeClass and then create a Job that consumes the TPUs defined in the ComputeClass.

#### Create a custom ComputeClass

The steps to create a custom ComputeClass that follows the [TPU rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration) differ depending on whether you use Ironwood (TPU7x) or an earlier TPU version.

###  Ironwood (TPU7x) 

  1. Create a workload policy. This step is required only if you are creating a multi-host node pool, which depends on the topology you choose. If you use a single-host node pool, skip this step.
         
         gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
             --type=HIGH_THROUGHPUT \
             --accelerator-topology=TPU_TOPOLOGY \
             --project=PROJECT_ID \
             --region=REGION
         

Replace the following:

     * `WORKLOAD_POLICY_NAME`: a name for your workload policy.
     * `TPU_TOPOLOGY`: the TPU Ironwood (TPU7x) topology. For example, use `2x2x2`. For more information about all supported Ironwood (TPU7x) topologies, see [topology section](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
     * `PROJECT_ID`: Your Google Cloud project ID.
     * `REGION`: The region for the workload policy. A workload policy is a regional resource and you can use it across node pools.
  2. Save the following manifest as `tpu-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: tpu-class
         spec:
           priorities:
             - tpu:
                 type: tpu7x
                 topology: TPU_TOPOLOGY
                 count: 4
               placement:
                 policyName: WORKLOAD_POLICY_NAME
           nodePoolAutoCreation:
             enabled: true
         

  3. (Optional) You can consume a specific reservation or sub-block. For example, you can add the following `specs` to your `ComputeClass` manifest:
         
         reservations:
             affinity: Specific
             specific:
               - name: RESERVATION_NAME
                 reservationBlock:
                   name: RESERVATION_BLOCK_NAME
                   reservationSubBlock:
                     name: RESERVATION_SUB_BLOCK_NAME
         

Replace the following:

     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `RESERVATION_BLOCK_NAME`: the name of the Compute Engine capacity reservation block.
     * `RESERVATION_SUB_BLOCK_NAME`: the name of the Compute Engine capacity reservation sub-block.

For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).




### Other TPU versions

To provision v3, v4, v5p, v5e, or v6e (Trillium) TPUs by using a custom ComputeClass [configured for TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration), complete the following steps:

  1. Save the following manifest as `tpu-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: tpu-class
         spec:
           priorities:
           - tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           - spot: true
             tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           - flexStart:
               enabled: true
             tpu:
               type: TPU_TYPE
               count: NUMBER_OF_CHIPS
               topology: TOPOLOGY
           nodePoolAutoCreation:
             enabled: true
         

Replace the following:

     * `TPU_TYPE`: the TPU type to use, like `tpu-v4-podslice`. Must be a value [supported by GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
     * `TOPOLOGY`: the arrangement of TPU chips in the slice, like `2x2x4`. Must be a supported topology for the selected TPU type.
     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`.
  2. Deploy the ComputeClass:
         
         kubectl apply -f tpu-compute-class.yaml
         

For more information about custom ComputeClasses and TPUs, see [TPU configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu_configuration).




#### Create a Job that consumes TPUs

  1. Save the following manifest as `tpu-job.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-job
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-job
         spec:
           backoffLimit: 0
           completions: 4
           parallelism: 4
           completionMode: Indexed
           template:
             spec:
               subdomain: headless-svc
               restartPolicy: Never
               nodeSelector:
                 **cloud.google.com/compute-class : tpu-class**
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())'
                 resources:
                   requests:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
                   limits:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
         

Replace the following:

     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`, equal to the `CHIP_COUNT` value in the selected custom ComputeClass.
     * `MEMORY_SIZE`: The maximum amount of memory that the TPU uses. Memory limits depend on the TPU version and topology that you use. To learn more, see [Minimums and maximums for accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#accelerator-class-min-max).
     * `NUMBER_OF_CHIPS`: the number of TPU chips for the container to use. Must be the same value for `limits` and `requests`.
  2. Deploy the Job:
         
         kubectl create -f tpu-job.yaml
         

When you create this Job, GKE automatically does the following:

     * Provisions nodes to run the Pods. Depending on the TPU type, topology, and resource requests that you specified, these nodes are either single-host slices or multi-host slices. Depending on the availability of TPU resources in the top priority, GKE might fall back to lower priorities to maximize flexibility, efficiency, and availability of accelerator capacity.
     * Adds taints to the Pods and tolerations to the nodes to prevent any of your other workloads from running on the same nodes as TPU workloads.

To learn more, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

  3. When you finish this section, you can avoid continued billing by deleting the resources you created:
         
         kubectl delete -f tpu-job.yaml
         




### Request TPUs in a workload

This section shows you how to create a Job that requests TPUs in Autopilot. In any workload that needs TPUs, you must specify the following:

  * Node selectors for the TPU version and topology
  * The number of TPU chips for a container in your workload



For a list of supported TPU versions, topologies, and the corresponding number of TPU chips and nodes in a slice, see [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#autopilot).

#### Considerations for TPU requests in workloads

Only one container in a Pod can use TPUs. The number of TPU chips that a container requests must be equal to the number of TPU chips attached to a node in the slice. For example, if you request TPU v5e (`tpu-v5-lite-podslice`) with a `2x4` topology, you can request any of the following:

  * `4` chips, which creates two multi-host nodes with 4 TPU chips each
  * `8` chips, which creates one single-host node with 8 TPU chips



As a best practice to maximize your cost efficiency, always consume all of the TPU in the slice that you request. If you request a multi-host slice of two nodes with 4 TPU chips each, you should be deploying a workload that runs on both nodes and consumes all 8 TPU chips in the slice.

#### Create a workload that requests TPUs

The following steps create a Job that requests TPUs. If you have workloads that run on multi-host TPU slices, you must also create a _headless Service_ that selects your workload by name. This headless Service lets Pods on different nodes in the multi-host slice to communicate with each other by updating the Kubernetes DNS configuration to point at the Pods in the workload.

  1. Save the following manifest as `tpu-autopilot.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           **name : headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-job**
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-job
         spec:
           backoffLimit: 0
           parallelism: NUM_OF_VMS
           completions: NUM_OF_VMS
           completionMode: Indexed
           template:
             spec:
               # Optional: Run in GKE Sandbox
               # runtimeClassName: gvisor
               **subdomain : headless-svc**
               restartPolicy: Never
               **nodeSelector :
                 cloud.google.com/gke-tpu-accelerator: TPU_TYPE
                 cloud.google.com/gke-tpu-topology: TPU_TOPOLOGY**
                 topology.kubernetes.io/zone: LOCATION
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())'
                 resources:
                   requests:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
                   limits:
                     cpu: 10
                     memory: MEMORY_SIZE
                     **google.com/tpu : NUMBER_OF_CHIPS**
         

Replace the following values in this order:

     1. `TPU_TYPE`: choose the [TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version) to use, like `tpu-v5-lite-podslice`. The value must be supported by GKE.
     2. `LOCATION`: validate the [zone where GKE places the TPU VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability). 

Optional: use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

     3. `TPU_TOPOLOGY`: choose the [arrangement](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) of TPU chips in the slice, like `4x4`. The topology must be supported for the selected TPU type.
     4. Find the selected `TPU_TYPE` and `TPU_TOPOLOGY` in the table in the [Choose a topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology) section: 
        * `NUM_OF_VMS`: use the value from the "Number of VMs" in the "Technical specifications" column. Set this value for the `parallelism` and `completions` fields in the Job spec.
        * `NUMBER_OF_CHIPS`: enter the number of chips per VM. Calculate this by dividing the value in the "Number of TPU chips for the topology" by the value in the "Number of VMs" for your selected row. Set this value for the `google.com/tpu` resource request.
     5. `MEMORY_SIZE`: The maximum amount of memory that the TPU uses. Memory limits depend on the TPU version and topology that you use. To learn more, see [Minimums and maximums for accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#accelerator-class-min-max).

Optionally, you can also change the following fields:

     * **`image`** : define the JAX AI image to use. The example manifest sets this field to the latest JAX AI image. To set a different version, see the list of [current JAX AI images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#current_jax_ai_images).
     * **`runtimeClassname: gvisor`** : use this flag to run this Pod in GKE Sandbox. To use, uncomment this line. GKE Sandbox supports TPUs version v4 and later. To learn more, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).

For example, consider a `tpu-v5-lite-podslice` with a `4x4` topology. This configuration means the following:

     * The topology has 16 chips in total (`4*4=16`).
     * The `tpu-v5-lite-podslice` deploys in `ct5lp-hightpu-4t` machines that have four chips per VM. This means that to have a `4x4` topology, you need four VMs (`16/4=4`). So, set the `parallelism` and `completions` fields to `4`.
     * Each container in the Pod requests four TPU chips, which corresponds to the [number of chips per VM](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#standard). The manifest specifies this with the line `google.com/tpu: 4`.
  2. Deploy the Job:
         
         kubectl create -f tpu-autopilot.yaml
         

When you create this Job, GKE automatically does the following:

     1. Provisions nodes to run the Pods. Depending on the TPU type, topology, and resource requests that you specified, these nodes are either single-host slices or multi-host slices.
     2. Adds taints to the Pods and tolerations to the nodes to prevent any of your other workloads from running on the same nodes as TPU workloads.
  3. When you finish this section, you can avoid continued billing by deleting the workload you created:
         
         kubectl delete -f tpu-autopilot.yaml
         




### Create a workload that requests TPUs and collection scheduling

In TPU Trillium, you can use collection scheduling to group TPU slice nodes. Grouping these TPU slice nodes makes it easier to adjust the number of replicas to meet the workload demand. Google Cloud controls software updates to ensure that sufficient slices within the collection are always available to serve traffic.

TPU Trillium supports collection scheduling for single-host and multi-host node pools that run inference workloads. The following describes how collection scheduling behavior depends on the type of TPU slice that you use:

  * **Multi-host TPU slice:** GKE groups multi-host TPU slices to form a collection. Each GKE node pool is a replica within this collection. To define a collection, create a multi-host TPU slice and assign a unique name to the collection. To add more TPU slices to the collection, create another multi-host TPU slice node pool with the same collection name and workload type.
  * **Single-host TPU slice:** GKE considers the entire single-host TPU slice node pool as a collection. To add more TPU slices to the collection, you can resize the single-host TPU slice node pool.



To learn about the limitation of collection scheduling, see [How collection scheduling works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling)

#### Use a multi-host TPU slice

Collection schedulling in multi-host TPU slice nodes is available for Autopilot clusters in version 1.31.2-gke.1537000 and later. Multi-host TPU slice nodes with a `2x4` topology are only supported in 1.31.2-gke.1115000 or later. To create multi-host TPU slice nodes and group it as a collection, add the following Kubernetes labels to your workload specification:

  * `cloud.google.com/gke-nodepool-group-name`: each collection should have a unique name at the cluster level. The value in the `cloud.google.com/gke-nodepool-group-name` label must adhere to [requirements for cluster labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#requirements).
  * `cloud.google.com/gke-workload-type: HIGH_AVAILABILITY`

For example, the following code block defines a collection with a multi-host TPU slice:
        
        nodeSelector:
            cloud.google.com/gke-nodepool-group-name: ${COLLECTION_NAME}
            cloud.google.com/gke-workload-type: HIGH_AVAILABILITY
            cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
            cloud.google.com/gke-tpu-topology: 4x4
        ...
        




#### Use a single-host TPU slice

Collection schedulling in single-host TPU slice nodes is available for Autopilot clusters in version 1.31.2-gke.1088000 and later. To create single-host TPU slice nodes and group it as a collection, add the `cloud.google.com/gke-workload-type:HIGH_AVAILABILITY` label in your workload specification.

For example, the following code block defines a collection with a single-host TPU slice:
    
    
      nodeSelector:
        cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
        cloud.google.com/gke-tpu-topology: 2x2
        cloud.google.com/gke-workload-type: HIGH_AVAILABILITY
      ...
    

#### Use custom compute classes to deploy a collection

For more information about deploying a workload that requests TPU workload and collection scheduling using custom compute classes see [TPU multi-host collection](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu-multi-host-collection) and [Define workload type for TPU SLO](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#tpu-use-slo).

## Example: Display the total TPU chips in a multi-host slice

The following workload returns the number of TPU chips across all of the nodes in a multi-host TPU slice. To create a multi-host slice, the workload has the following parameters:

  * TPU version: TPU v4
  * Topology: 2x2x4



This version and topology selection result in a multi-host slice.

  1. Save the following manifest as `available-chips-multihost.yaml`: 
         
         apiVersion: v1
         kind: Service
         metadata:
           name: headless-svc
         spec:
           clusterIP: None
           selector:
             job-name: tpu-available-chips
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: tpu-available-chips
         spec:
           backoffLimit: 0
           completions: 4
           parallelism: 4
           completionMode: Indexed
           template:
             spec:
               subdomain: headless-svc
               restartPolicy: Never
               nodeSelector:
                 cloud.google.com/gke-tpu-accelerator: tpu-v4-podslice # Node selector to target TPU v4 slice nodes.
                 cloud.google.com/gke-tpu-topology: 2x2x4 # Specifies the physical topology for the TPU slice.
               containers:
               - name: tpu-job
                 image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
                 ports:
                 - containerPort: 8471 # Default port using which TPU VMs communicate
                 - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
                 command:
                 - bash
                 - -c
                 - |
                   python -c 'import jax; print("TPU cores:", jax.device_count())' # Python command to count available TPU chips.
                 resources:
                   requests:
                     cpu: 10
                     memory: 407Gi
                     **google.com/tpu : 4** # Request 4 TPU chips for this workload.
                   limits:
                     cpu: 10
                     memory: 407Gi
                     **google.com/tpu : 4** # Limit to 4 TPU chips for this workload.

  2. Deploy the manifest: 
         
         kubectl create -f available-chips-multihost.yaml
         

GKE runs a TPU v4 slice with four VMs (multi-host TPU slice). The slice has 16 interconnected TPU chips.

  3. Verify that the Job created four Pods: 
         
         kubectl get pods
         

The output is similar to the following:
         
         NAME                       READY   STATUS      RESTARTS   AGE
         tpu-job-podslice-0-5cd8r   0/1     Completed   0          97s
         tpu-job-podslice-1-lqqxt   0/1     Completed   0          97s
         tpu-job-podslice-2-f6kwh   0/1     Completed   0          97s
         tpu-job-podslice-3-m8b5c   0/1     Completed   0          97s
         

  4. Get the logs of one of the Pods: 
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of one of the created Pods. For example, `tpu-job-podslice-0-5cd8r`.

The output is similar to the following: 
         
         TPU cores: 16
         

  5. Optional: Remove the workload: 
         
         kubectl delete -f available-chips-multihost.yaml
         




## Example: Display the TPU chips in a single node

The following workload is a static Pod that displays the number of TPU chips that are attached to a specific node. To create a single-host node, the workload has the following parameters:

  * TPU version: TPU v5e
  * Topology: 2x4



This version and topology selection result in a single-host slice.

  1. Save the following manifest as `available-chips-singlehost.yaml`: 
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: tpu-job-jax-v5
         spec:
           restartPolicy: Never
           nodeSelector:
             cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice # Node selector to target TPU v5e slice nodes.
             cloud.google.com/gke-tpu-topology: 2x4 # Specify the physical topology for the TPU slice.
           containers:
           - name: tpu-job
             image: us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:latest
             ports:
             - containerPort: 8431 # Port to export TPU runtime metrics, if supported.
             command:
             - bash
             - -c
             - |
               python -c 'import jax; print("Total TPU chips:", jax.device_count())'
             resources:
               requests:
                 google.com/tpu: 8 # Request 8 TPU chips for this container.
               limits:
                 google.com/tpu: 8 # Limit to 8 TPU chips for this container.

  2. Deploy the manifest: 
         
         kubectl create -f available-chips-singlehost.yaml
         

GKE provisions nodes with eight single-host TPU slices that use TPU v5e. Each TPU node has eight TPU chips (single-host TPU slice).

  3. Get the logs of the Pod: 
         
         kubectl logs tpu-job-jax-v5
         

The output is similar to the following: 
         
         Total TPU chips: 8
         

  4. Optional: Remove the workload: 
         
         kubectl delete -f available-chips-singlehost.yaml
           




## Observe and monitor TPUs

### Dashboard

Node pool observability in the [Google Cloud console](http://console.cloud.google.com) is generally available. To view the status of your TPU multi-host node pools on GKE, go to **GKE TPU Node Pool Status** dashboard provided by Cloud Monitoring:

[Go to GKE TPU Node Pool Status](https://console.cloud.google.com/monitoring/dashboards/integration/gke.gke-tpu-node-pool-status)

This dashboard gives you comprehensive insights into the health of your multi-host TPU node pools. For more information, see Monitor health metrics for TPU nodes and node pools.

In the [**Kubernetes Clusters**](https://console.cloud.google.com/kubernetes/list) page in the Google Cloud console, the **Observability** tab also displays TPU observability metrics, such as TPU usage, under the **Accelerators > TPU** heading. For more information, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

The TPU dashboard is populated only if you have [system metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics) enabled in your GKE cluster.

### Runtime metrics

In GKE version 1.27.4-gke.900 or later, TPU workloads that both use JAX version [0.4.14](https://github.com/google/jax/releases/tag/jaxlib-v0.4.14) or later and specify `containerPort: 8431` export TPU utilization metrics as GKE [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics). The following metrics are available in Cloud Monitoring to monitor your TPU workload's runtime performance:

  * **Duty cycle** : percentage of time over the past sampling period (60 seconds) during which the TensorCores were actively processing on a TPU chip. Larger percentage means better TPU utilization.
  * **Memory used** : amount of accelerator memory allocated in bytes. Sampled every 60 seconds.
  * **Memory total** : total accelerator memory in bytes. Sampled every 60 seconds.



These metrics are located in the Kubernetes node (`k8s_node`) and Kubernetes container (`k8s_container`) schema.

Kubernetes container:

  * `kubernetes.io/container/accelerator/duty_cycle`
  * `kubernetes.io/container/accelerator/memory_used`
  * `kubernetes.io/container/accelerator/memory_total`



Kubernetes node:

  * `kubernetes.io/node/accelerator/duty_cycle`
  * `kubernetes.io/node/accelerator/memory_used`
  * `kubernetes.io/node/accelerator/memory_total`



### Monitor health metrics for TPU nodes and node pools

When a training job has an error or terminates in failure, you can check metrics related to the underlying infrastructure to figure out if the interruption was caused by an issue with the underlying node or node pool.

#### Node status

In GKE version 1.32.1-gke.1357001 or later, the following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) exposes the condition of a GKE node:

  * `kubernetes.io/node/status_condition`



The `condition` field reports conditions on the node, such as `Ready`, `DiskPressure`, and `MemoryPressure`. The `status` field shows the reported status of the condition, which can be `True`, `False`, or `Unknown`. This is a metric with the `k8s_node` monitored resource type.

This PromQL query shows if a particular node is `Ready`:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        node_name="NODE_NAME",
        condition="Ready",
        status="True"}
    

To help troubleshoot issues in a cluster, you might want to look at nodes that have exhibited other conditions:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        condition!="Ready",
        status="True"}
    

You might want to specifically look at nodes that aren't `Ready`:
    
    
    kubernetes_io:node_status_condition{
        monitored_resource="k8s_node",
        cluster_name="CLUSTER_NAME",
        condition="Ready",
        status="False"}
    

If there is no data, then the nodes are ready. The status condition is sampled every 60 seconds.

You can use the following query to understand the node status across the fleet:
    
    
    avg by (condition,status)(
      avg_over_time(
        kubernetes_io:node_status_condition{monitored_resource="k8s_node"}[${__interval}]))
    

#### Node pool status

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) for the `k8s_node_pool` monitored resource exposes the status of a GKE node pool:

  * `kubernetes.io/node_pool/status`



This metric is reported only for multi-host TPU node pools.

The `status` field reports the status of the node pool, such as `Provisioning`, `Running`, `Error`, `Reconciling`, or `Stopping`. Status updates happen after GKE API operations complete.

To verify if a particular node pool has `Running` status, use the following PromQL query:
    
    
    kubernetes_io:node_pool_status{
        monitored_resource="k8s_node_pool",
        cluster_name="CLUSTER_NAME",
        node_pool_name="NODE_POOL_NAME",
        status="Running"}
    

To monitor the number of node pools in your project grouped by their status, use the following PromQL query:
    
    
    count by (status)(
      count_over_time(
        kubernetes_io:node_pool_status{monitored_resource="k8s_node_pool"}[${__interval}]))
    

#### Node pool availability

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) shows whether a multi-host TPU node pool is available:

  * `kubernetes.io/node_pool/multi_host/available`



The metric has a value of `True` if all of the nodes in the node pool are available, and `False` otherwise. The metric is sampled every 60 seconds.

To check the availability of multi-host TPU node pools in your project, use the following PromQL query:
    
    
    avg by (node_pool_name)(
      avg_over_time(
        kubernetes_io:node_pool_multi_host_available{
          monitored_resource="k8s_node_pool",
          cluster_name="CLUSTER_NAME"}[${__interval}]))
    

#### Node interruption count

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) reports the count of interruptions for a GKE node since the last sample (the metric is sampled every 60 seconds):

  * `kubernetes.io/node/interruption_count`



The `interruption_type` (such as `TerminationEvent`, `MaintenanceEvent`, or `PreemptionEvent`) and `interruption_reason` (like `HostError`, `Eviction`, or `AutoRepair`) fields can help provide the reason for why a node was interrupted.

To get a breakdown of the interruptions and their causes in TPU nodes in the clusters in your project, use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node"}[${__interval}]))
    

To only see the [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents), update the query to filter the `HW/SW Maintenance` value for the `interruption_reason`. Use the following PromQL query:
    
    
      sum by (interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_interruption_count{monitored_resource="k8s_node", interruption_reason="HW/SW Maintenance"}[${__interval}]))
    

To see the interruption count aggregated by node pool, use the following PromQL query:
    
    
      sum by (node_pool_name,interruption_type,interruption_reason)(
        sum_over_time(
          kubernetes_io:node_pool_interruption_count{monitored_resource="k8s_node_pool", interruption_reason="HW/SW Maintenance", node_pool_name=NODE_POOL_NAME }[${__interval}]))
    

#### Node pool times to recover (TTR)

The following [GKE system metric](https://cloud.google.com/monitoring/api/metrics_kubernetes) reports the distribution of recovery period durations for GKE multi-host TPU node pools:

  * `kubernetes.io/node_pool/accelerator/times_to_recover`



Each sample recorded in this metric indicates a single recovery event for the node pool from a downtime period.

This metric is useful for tracking the multi-host TPU node pool time to recover and time between interruptions.

You can use the following PromQL query to calculate the mean time to recovery (MTTR) for the last 7 days in your cluster:
    
    
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_to_recover_sum{
        monitored_resource="k8s_node_pool", cluster_name="CLUSTER_NAME"}[7d]))
    /
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_to_recover_count{
        monitored_resource="k8s_node_pool",cluster_name="CLUSTER_NAME"}[7d]))
    

#### Node pool times between interruptions (TBI)

The following [GKE system metric](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) reports the distribution of times between the end of the most recent interruption and the beginning of the current interruption for GKE multi-host TPU node pools:

  * `kubernetes.io/node_pool/accelerator/times_between_interruptions`



Each sample recorded in this metric indicates a single duration between the most recent and current interruption.

Use the following PromQL query to calculate the mean time between interruptions (MTBI) in your cluster for the previous 7 days:
    
    
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_between_interruptions_sum{
        monitored_resource="k8s_node_pool", cluster_name="CLUSTER_NAME"}[7d]))
    /
    sum(sum_over_time(
      kubernetes_io:node_pool_accelerator_times_between_interruptions_count{
        monitored_resource="k8s_node_pool",cluster_name="CLUSTER_NAME"}[7d]))
    

### Host metrics

In GKE version 1.28.1-gke.1066000 or later, VMs in a TPU slice export TPU utilization metrics as GKE [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics). The following metrics are available in Cloud Monitoring to monitor your TPU host's performance:

  * **TensorCore utilization** : current percentage of the TensorCore that is utilized. The TensorCore value equals the sum of the [matrix-multiply units (MXUs) plus the vector unit](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#tpu_chip). The TensorCore utilization value is the division of the TensorCore operations that were _performed_ over the past sample period (60 seconds) by the _supported_ number of TensorCore operations over the same period. Larger value means better utilization.
  * **Memory bandwidth utilization** : current percentage of the accelerator memory bandwidth that is being used. Computed by dividing the memory bandwidth used over a sample period (60s) by the maximum supported bandwidth over the same sample period.



These metrics are located in the Kubernetes node (`k8s_node`) and Kubernetes container (`k8s_container`) schema.

Kubernetes container:

  * `kubernetes.io/container/accelerator/tensorcore_utilization`
  * `kubernetes.io/container/accelerator/memory_bandwidth_utilization`



Kubernetes node:

  * `kubernetes.io/node/accelerator/tensorcore_utilization`
  * `kubernetes.io/node/accelerator/memory_bandwidth_utilization`



For more information, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes-kubernetes) and [GKE system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics).

### Logging

Logs emitted by containers running on GKE nodes, including TPU VMs, are [collected](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-logs) by the GKE logging agent, sent to Logging, and are [visible in Logging](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs).

## Recommendations for TPU workloads in Autopilot

The following recommendations might improve the efficiency of your TPU workloads:

  * Use [extended run time Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods) for a grace period of up to seven days before GKE terminates your Pods for scale-downs or node upgrades. You can use maintenance windows and exclusions with extended run time Pods to further delay automatic node upgrades.
  * Use capacity reservations to ensure that your workloads receive requested TPUs without being placed in a queue for availability.



### Prevent scheduling deadlocks

When running multiple TPU Jobs or multiple replicas of a Job, Pods from different Jobs can schedule on the same TPU node pool. This can cause a scheduling deadlock where none of the Jobs can secure enough nodes to complete their topology.

To reduce the risk of scheduling deadlocks, apply one of the following configurations:

  * Use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) rules to ensure that Pods from different Jobs are not scheduled on the same TPU node pool or topology domain.
  * Use the `jobset.sigs.k8s.io/exclusive-topology` annotation, which causes the JobSet to claim the specified topology domain (like a node pool) exclusively for its own Pods.



For detailed configuration examples and troubleshooting steps, see [Scheduling deadlock](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus#scheduling_deadlock).

## What's next

  * [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus) to start your TPU setup
  * [Deploy TPU workloads in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot)
  * [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus)
  * Learn about [best practices](https://docs.cloud.google.com/tpu/docs/tpus) for using Cloud TPU for your machine learning tasks.
  * [Video: Build large-scale machine learning on Cloud TPU with GKE](https://www.youtube.com/watch?v=wtKhG1aTgtY).
  * [Serve Large Language Models with KubeRay on TPUs](https://www.youtube.com/watch?v=RK_u6cfPnnw).
  * [Learn about sandboxing GPU workloads with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
