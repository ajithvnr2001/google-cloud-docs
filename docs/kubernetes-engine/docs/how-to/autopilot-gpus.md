---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus/
title: Deploy GPU workloads in Autopilot \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:33.337680+00:00
---

# Deploy GPU workloads in Autopilot  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy GPU workloads in Autopilot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

You can request GPUs to accelerate tasks in your Google Kubernetes Engine (GKE) Autopilot workloads. This document describes how to run GPUs in Autopilot, set Pod resource requests and limits, and monitor GPU workloads.

This document is for Platform admins and operators and for Data and AI specialists who want to request GPUs for workloads that run tasks like machine learning (ML) training or inference. To learn more about the common roles, responsibilities, and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before you proceed, ensure that you're familiar with the following concepts:

  * [About GPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus)
  * [Kubernetes node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)



You request GPUs by using ComputeClasses or by using node selectors in your Pod specification. GKE places those Pods on nodes that have those GPUs. You can also use GPU sharing capabilities, like time-sharing.

## Pricing

The [Autopilot _node-based billing model_](https://cloud.google.com/kubernetes-engine/pricing#autopilot-workloads-that-select-specific-hardware) applies to GPU Pods. Both the Autopilot management premium for the nodes and the actual GPU hardware in Compute Engine are eligible for [compute flexible committed-use discounts (CUDs)](https://docs.cloud.google.com/kubernetes-engine/cud#flexible-cuds).

Note the following pricing considerations for Autopilot GPUs:

  * All A100 (80GB) GPU nodes use local SSDs for node boot disks at fixed sizes based on the number of GPUs. You're billed separately for the attached Local SSDs. This pricing doesn't apply to A100 (40GB) GPUs.
  * GKE Sandbox pricing is the same as default Autopilot pricing. To learn more about sandboxing your accelerator workloads, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) and [getting started with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).
  * If you're using the NVIDIA RTX PRO 6000 GPUs (G4 machine series) with Autopilot mode, starting on October 1, 2026, GKE bills for the Autopilot node management premium, in addition to existing applicable charges for the underlying hardware. These existing charges continue to apply both before and after this date. For more information about how billing works when requesting specific hardware with Autopilot workloads, see [Autopilot workloads that select specific hardware](https://docs.cloud.google.com/kubernetes-engine/pricing#autopilot-workloads-that-select-specific-hardware).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Ensure that you have a GKE Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) running one of the following versions to use the following GPUs or features:

    * NVIDIA B200 (180 GB) GPUs: 1.32.2-gke.1422000 or later
    * NVIDIA RTX PRO 6000 GPUs: 
      * Machine types that have one or more GPUs: 1.34.1-gke.1829001 or later
      * Machine types that have less than one GPU: 1.35.2-gke.1485000 or later

All other GPU types are supported in all available GKE versions.


**Note:** For GKE Sandbox GPU clusters, see [GPU model support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support) for gVisor compatibility.

  * [Ensure that you have enough GPU quotas](https://docs.cloud.google.com/docs/quotas/view-manage) available in your project. You must have enough [Compute Engine GPU quota](https://docs.cloud.google.com/compute/quotas#gpu_quota) for the GPU models that you want to create in each region. If you require additional GPU quota, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).
  * If you want to use G4 machine types that have less than one NVIDIA RTX PRO 6000 GPU, you must do the following, in addition to adhering to the mentioned version requirements:

    * Explicitly request G4 machine types that have less than one GPU.
    * If your cluster is running GKE versions earlier than 1.36, [prepare your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#prepare-workloads-g4-less-than-one-gpu).



### Limitations

  * GPU availability depends on the Google Cloud region of your Autopilot cluster, and your GPU quota. To find a GPU model by region or zone, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * For NVIDIA A100 (80GB) GPUs, you're charged a fixed price for the Local SSDs attached to the nodes, **regardless of whether your Pods use that capacity**.
  * If you want multiple GPU pods to fit into a single node, the sum of GPU requests for those pods must be _less than or equal to_ the number of GPU resources attached to that node. For example, a node with a `gke-accelerator-count` of 4 could accommodate up to four Pods that request one GPU each.



Placing multiple Pods on a single GPU node is useful in situations like the following:

  * You have capacity reservations for large Accelerator machine types and you run single-GPU workloads, so deploying one Pod per node would waste the other GPUs on that machine
  * You have GPU workloads that must run on the same host



In these situations, we recommend that you use all of the GPUs on the node by ensuring that the sum of Pod GPU resource requests on the node is equal to the number of GPUs attached to the node.

## Request GPUs in your containers

To request GPU resources for your containers, add the following fields to your Pod specification. Depending on your workload requirements, you can optionally omit the `cloud.google.com/gke-accelerator-count` selector.
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-gpu-pod
    spec:
      # Optional: Use GKE Sandbox
      # runtimeClassName: gvisor
      **nodeSelector :
        cloud.google.com/gke-accelerator: GPU_TYPE
        cloud.google.com/gke-accelerator-count: "GPU_COUNT**"
      containers:
      - name: my-gpu-container
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        resources:
          **limits :
            nvidia.com/gpu: **GPU_QUANTITY****
    

Replace the following:

  * `GPU_TYPE`: the type of GPU hardware. Allowed values are the following: 

    * `nvidia-gb200`: NVIDIA GB200 (Preview)
    * `nvidia-b200`: NVIDIA B200 (180GB)
    * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
    * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
    * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
    * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
    * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
    * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
    * `nvidia-l4`: NVIDIA L4
    * `nvidia-tesla-t4`: NVIDIA T4
or if you use GKE Sandbox, one of the following: 
    * `nvidia-gb200`: NVIDIA GB200 ([Preview](https://cloud.google.com/products#product-launch-stages))
    * `nvidia-b200`: NVIDIA B200 (180GB) ([Preview](https://cloud.google.com/products#product-launch-stages))
    * `nvidia-h200-141gb`: NVIDIA H200 (141GB) ([Preview](https://cloud.google.com/products#product-launch-stages))
    * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
    * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
    * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
    * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
    * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000 ([Preview](https://cloud.google.com/products#product-launch-stages)) (except for G4 machine types that have less than one GPU)
    * `nvidia-l4`: NVIDIA L4
    * `nvidia-tesla-t4`: NVIDIA T4
For more information, see [GPU model support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support). 
  * `GPU_COUNT`: the total number of GPUs available to attach to the node. Must be greater than or equal to `GPU_QUANTITY` and a supported GPU quantity for the GPU type you selected. If you omit this nodeSelector, Autopilot places one Pod on each GPU node.

  * `GPU_QUANTITY`: the number of GPUs to allocate to the container. Must be less than or equal to `GPU_COUNT` and a supported GPU quantity for the GPU type you selected.

  * **Optional`runtimeClassname: gvisor`**: the setting that lets your run this Pod in GKE Sandbox. To use, uncomment this line. To learn more, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).




You must specify both the GPU type and the GPU quantity in your Pod specification. If you omit either of these values, Autopilot rejects your Pod.

When you deploy this manifest, Autopilot automatically installs the default NVIDIA drivers for the node GKE version. You can optionally choose to install the latest driver version for that GKE version by adding the following node selector to your manifest:
    
    
    spec:
      nodeSelector:
        cloud.google.com/gke-gpu-driver-version: "DRIVER_VERSION"
    

Replace `DRIVER_VERSION` with one of the following values:

  * `default` \- the default, stable driver for your node GKE version. If you omit the nodeSelector in your manifest, this is the default option.
  * `latest` \- the latest available driver version for your node GKE version.



### Request CPU and memory for Autopilot GPU Pods

When defining your GPU Pods, you should also request CPU and memory resources so that your containers perform as expected. Autopilot enforces specific CPU and memory minimums, maximums, and defaults based on the GPU type and quantity. If you run multiple GPU Pods on a single node, specify the CPU and memory, otherwise it defaults to the node's entire capacity. For details, refer to [Resource requests in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).

Your Pod specification should look similar to the following example, which requests four T4 GPUs:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: t4-pod
    spec:
      # Optional: Use GKE Sandbox
      # runtimeClassName: gvisor
      nodeSelector:
        cloud.google.com/gke-accelerator: "nvidia-tesla-t4"
      containers:
      - name: t4-container-1
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
    ** resources:
          limits:
            nvidia.com/gpu: 3
            cpu: "54"
            memory: "54Gi"
          requests:
            cpu: "54"
            memory: "54Gi"**
      - name: t4-container-2
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        **resources :
          limits:
            nvidia.com/gpu: 1
            cpu: "18"
            memory: "18Gi"
          requests:
            cpu: "18"
            memory: "18Gi"**
    

  * **Optional`runtimeClassname: gvisor`**: the setting that lets your run this Pod in GKE Sandbox. To use, uncomment this line. To learn more, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).



This manifest specifies `limits` for CPU and memory resources. If you omit the `limits` for CPU or memory, GKE gives your Pods the `Burstable` QoS class and lets your Pods burst into unused resources from the sum of resource requests on the node. For more information, see [Configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke).

### Request ephemeral storage for Autopilot GPU Pods

You can also request ephemeral storage in Pods that need short-lived storage. The maximum available ephemeral storage and the type of storage hardware used depends on the type and quantity of GPUs the Pod requests. You can use Local SSD for ephemeral storage with the following configurations:

  * Use NVIDIA RTX PRO 6000 GPUs and run a GKE patch version that meets the version requirements listed in the Before you begin section. The one-eighth GPU fractional configuration doesn't support ephemeral storage.
  * Use NVIDIA L4 GPUs.



To use Local SSD for ephemeral storage, add the `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"` nodeSelector to your workload manifest. See the example manifest in [Use Local SSD-backed ephemeral storage with Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#local-ssd-autopilot). The NVIDIA H100 (80GB) GPUs and NVIDIA A100 (80GB) GPUs always use Local SSDs for ephemeral storage, and you can't specify this node selector for those GPUs.

### Request specific machine types using custom ComputeClasses

In some cases, you might need to run your GPU workload on a specific machine type, for example if the machine type that you want is not a default machine type for Autopilot clusters. You can explicitly request a specific machine by using custom ComputeClasses, which let you define a node configuration profile that specifies the machine type and GPU. To use the [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) that have less than one GPU, you must follow the instructions in the next section to explicitly request a machine type.

For general information about ComputeClasses, see [About custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

To request a specific machine type for your GPU workload, complete the following steps:

  1. Create a manifest for a custom ComputeClass. For this example, save the following as `a3-computeclass.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: a3-edge-gpu
         spec:
           priorities:
           - machineType: a3-edgegpu-8g-nolssd
             gpu:
              count: 8
              type: nvidia-h100-80gb
           nodePoolAutoCreation:
             enabled: true
         

In this manifest:

     * The `metadata.name` is the name of your custom ComputeClass, which you will reference in your Pod specification.
     * The `machineType` is the specific machine to provision.
     * The `gpu` fields specify the type and number of GPUs attached to that machine. The values of these fields must match the capabilities of the specified `machineType`.
  2. Apply the manifest by running the following command:
         
         kubectl apply -f a3-computeclass.yaml
         

  3. In your Pod manifest, request the ComputeClass by using the `cloud.google.com/compute-class` node selector:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gpu-cc-pod
         spec:
           nodeSelector:
             cloud.google.com/compute-class: a3-edge-gpu
           containers:
           - name: my-gpu-container
             image: nvidia/cuda:latest
             command: ["/bin/bash", "-c", "--"]
             args: ["while true; do sleep 600; done;"]
             resources:
               limits:
                 nvidia.com/gpu: 1
         

GKE provisions a new node that matches the definition in the `a3-edge-gpu` ComputeClass to run your Pod.




#### Request G4 machine types that have less than one GPU

The G4 machine types use the NVIDIA RTX PRO 6000 GPU. To request any G4 machine types that have less than one GPU, you must follow the instructions in the previous section, setting the following fields:

  * `machineType` to one of the following values:

    * `g4-standard-6` (one-eighth of a GPU)
    * `g4-standard-12` (one-quarter of a GPU)
    * `g4-standard-24` (one-half of a GPU)
  * `gpu.count`: `1`

  * `gpu.type`: `nvidia-rtx-pro-6000`




## Verify the allocation of deployed GPUs

To check that a deployed GPU workload has the requested GPUs, run the following command:
    
    
    kubectl describe node NODE_NAME
    

Replace `NODE_NAME` with the name of the node on which the Pod was scheduled.

The output is similar to the following:
    
    
    apiVersion: v1
    kind: Node
    metadata:
    ...
      labels:
        ...
        cloud.google.com/gke-accelerator: nvidia-tesla-t4
        cloud.google.com/gke-accelerator-count: "1"
        cloud.google.com/machine-family: custom-48
        ...
    ...
    

## Check GPU driver version

In Autopilot clusters, GKE automatically installs NVIDIA device drivers on all GPU nodes. To find the driver version that GKE installed in your cluster, run the following command:
    
    
    kubectl logs --selector=k8s-app=nvidia-gpu-device-plugin \
        --container="nvidia-gpu-device-plugin" \
        --tail=-1 \
        --namespace=kube-system | grep Driver
    

The output is similar to the following:
    
    
    I1206 18:37:08.251742    5851 metrics.go:144] nvml initialized successfully. **Driver version: 535.104.12**
    

## How GPU allocation works in Autopilot

After you request a GPU type and a quantity for the containers in a Pod and deploy the Pod, the following happens:

  1. If no allocatable GPU node exists, Autopilot provisions a new GPU node to schedule the Pod. Autopilot automatically installs NVIDIA's drivers to facilitate the hardware.
  2. Autopilot adds [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the GPU node and adds the corresponding tolerations to the Pod. This prevents GKE from scheduling other Pods on the GPU node.



Autopilot places exactly one GPU Pod on each GPU node, as well as any GKE-managed workloads that run on all nodes, and any DaemonSets that you configure to tolerate all node taints.

### Run DaemonSets on every node

You might want to run DaemonSets on every node, even nodes with applied taints. For example, some logging and monitoring agents must run on every node in the cluster. You can configure those DaemonSets to ignore node taints so that GKE places those workloads on every node.

To run DaemonSets on every node in your cluster, including your GPU nodes, add the following toleration to your specification:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: logging-agent
    spec:
    ** tolerations:
      - key: ""
        operator: "Exists"
        effect: "**"
      containers:
      - name: logging-agent-v1
        image: IMAGE_PATH
    

Replace `IMAGE_PATH` with the path to the container image.

To run DaemonSets on specific GPU nodes in your cluster, add the following to your specification:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: logging-agent
    spec:
    ** nodeSelector:
        cloud.google.com/gke-accelerator: "GPU_TYPE"
      tolerations:
      - key: ""
        operator: "Exists"
        effect: "**"
      containers:
      - name: logging-agent-v1
        image: IMAGE_PATH
    

Replace `GPU_TYPE` with the type of GPU in your target nodes. This can be one of the following:

  * `nvidia-gb200`: NVIDIA GB200 (Preview)
  * `nvidia-b200`: NVIDIA B200 (180GB)
  * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
  * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
  * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
  * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
  * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
  * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
  * `nvidia-l4`: NVIDIA L4
  * `nvidia-tesla-t4`: NVIDIA T4

or if you use GKE Sandbox, one of the following: 
  * `nvidia-gb200`: NVIDIA GB200 ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `nvidia-b200`: NVIDIA B200 (180GB) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `nvidia-h200-141gb`: NVIDIA H200 (141GB) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
  * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
  * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
  * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
  * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000 ([Preview](https://cloud.google.com/products#product-launch-stages)) (except for G4 machine types that have less than one GPU)
  * `nvidia-l4`: NVIDIA L4
  * `nvidia-tesla-t4`: NVIDIA T4

For more information, see [GPU model support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods#gpu_model_support). 

### GPU use cases in Autopilot

You can allocate GPUs to containers in Autopilot Pods to facilitate workloads such as the following:

  * Machine learning (ML) inference
  * ML training
  * Rendering



### Supported GPU quantities

When you request GPUs in your Pod specification, you must use the following quantities based on the GPU type. If you request a GPU quantity that isn't supported for that type, Autopilot rejects your Pod.

GPU quantities  
---  
NVIDIA B200 (180GB)  
`nvidia-b200` | 8  
NVIDIA H200 (141GB)  
`nvidia-h200-141gb` | 8  
NVIDIA H100 Mega (80GB)  
`nvidia-h100-mega-80gb` | 8  
NVIDIA H100 (80GB)  
`nvidia-h100-80gb` | 1, 2, 4, 8  
NVIDIA A100 (80GB)  
`nvidia-a100-80gb` | 1, 2, 4, 8  
NVIDIA A100 (40GB)  
`nvidia-tesla-a100` | 1, 2, 4, 8, 16  
NVIDIA RTX PRO 6000  
`nvidia-rtx-pro-6000` | 1/8, 1/4, 1/2, 1, 2, 4, 8  
NVIDIA L4  
`nvidia-l4` | 1, 2, 4, 8  
NVIDIA T4  
`nvidia-tesla-t4` | 1, 2, 4  
  
## Monitor your GPU node workload performance

If your GKE cluster has [system metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics#system-metrics) enabled, then the following metrics are available in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to monitor your GPU workload performance: 

  * **Duty Cycle (`container/accelerator/duty_cycle`): ** Percentage of time over the past sample period (10 seconds) during which the accelerator was actively processing. Between 1 and 100. 
  * **Memory Usage (`container/accelerator/memory_used`): ** Amount of accelerator memory allocated in bytes. 
  * **Memory Capacity (`container/accelerator/memory_total`): ** Total accelerator memory in bytes. 



These metrics apply at the container level (`container/accelerator`) and are not collected for containers scheduled on a GPU that uses GPU time-sharing or NVIDIA MPS. 

You can use predefined dashboards to monitor your clusters with GPU nodes. For more information, see [ View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics). For general information about monitoring your clusters and their resources, refer to [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability). 

### View usage metrics for workloads

You view your workload GPU usage metrics from the **Workloads** dashboard in the Google Cloud console. 

To view your workload GPU usage, perform the following steps:

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)
  2. Select a workload.



The Workloads dashboard displays charts for GPU memory usage and capacity, and GPU duty cycle. 

### View NVIDIA Data Center GPU Manager (DCGM) metrics

You can collect and visualize NVIDIA DCGM metrics by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus). For Autopilot clusters, GKE installs the drivers. For Standard clusters, you must install the NVIDIA drivers. 

For instructions on how to deploy the GKE-managed DCGM package, see [Collect and view NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics). 

### JobSet and node health metrics for GPU workloads

In addition to DCGM metrics, you can use the following metrics to monitor the health and performance of your GPU workloads, especially when running them as JobSets. 

#### JobSet metrics

The following metrics apply to both GPU and TPU JobSets that have a single replicated Job: 

  * `kubernetes.io/jobset/times_between_interruptions`
  * `kubernetes.io/jobset/times_to_recover`
  * `kubernetes.io/jobset/uptime`



For more information about these system metrics, see [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). 

You can also use the **JobSet dashboard** in the Google Cloud console to visualize and monitor your GPU workloads:

[Go to Deployments](https://console.cloud.google.com//kubernetes/aiml/deployments/jobs)

#### Node health metrics

The following node-level metrics apply to all nodes, including those with GPUs:

  * `kubernetes.io/node/status_condition`: This metric requires GKE version 1.32.1-gke.1357001 or later. 



Node interruption and node pool interruption metrics also apply to non-TPU nodes.

#### Kube-state-metrics for JobSets

The kube-state-metrics for JobSets can be used with GPUs. Collection of these metrics requires GKE version 1.32.1-gke.1357001 or later. For more information, see the [JobSet metrics documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics). 

## What's next

  * [Learn more about GPU support in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * [Read about how Autopilot ComputeClasses are optimized for specialized use cases](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).
  * [Read about deploying GPUs for batch workloads with Dynamic Workload Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).
  * [Learn about sandboxing GPU workloads with GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
