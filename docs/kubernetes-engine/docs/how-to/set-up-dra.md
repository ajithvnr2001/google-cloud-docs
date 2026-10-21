---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra/
title: Prepare GKE infrastructure for DRA workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:11.600575+00:00
---

# Prepare GKE infrastructure for DRA workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Prepare GKE infrastructure for DRA workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to manually set up your Google Kubernetes Engine (GKE) infrastructure to support [dynamic resource allocation (DRA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation). The setup steps include creating node pools that use GPUs and installing DRA drivers.

This document is intended for [platform administrators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-admin) who want to create infrastructure with specialized hardware devices that application operators can claim in workloads.

## Limitations

The following limitations apply:

  * [Limitations of DRA in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation#limitations)
  * Device-specific limitations, which apply regardless of whether you use DRA: [GPU workloads on Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#limitations)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Have a GKE Standard cluster that runs version 1.35 or later. You can also [create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster#create-regional-single-zone-nodepool).

  * [Install Helm](https://helm.sh/docs/intro/install). If you use Cloud Shell, Helm is already installed.




## Create a GKE node pool with GPUs

This section shows you how to create a GPU node pool and install the corresponding DRA drivers. The steps in this section apply only to node pools that you manually create. To create a GPU node pool that supports DRA, you must do the following:

  * **Disable automatic GPU driver installation** : specify the `gpu-driver-version=disabled` option in the `--accelerator` flag.
  * **Disable the GPU device plugin** : add the `gke-no-default-nvidia-gpu-device-plugin=true` node label to the node pool.
  * **Run the DRA driver DaemonSet** : add the `nvidia.com/gpu.present=true` node label to the node pool.
  * **Configure autoscaling** : to use the cluster autoscaler in your node pool, add the `cloud.google.com/gke-nvidia-gpu-dra-driver=true` node label to the node pool. The cluster autoscaler uses this node label to identify nodes that run the DRA driver for GPUs.



To create and configure GPU node pools, follow these steps:

  1. Create a GPU node pool. The following example commands create node pools with different configurations:

     * Create a node pool with a `g2-standard-24` instance that has two L4 GPUs:
           
           gcloud container node-pools create NODEPOOL_NAME \
               --cluster=CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --node-locations=NODE_LOCATION1,NODE_LOCATION2,... \
               --machine-type="g2-standard-24" \
               --accelerator="type=nvidia-l4,count=2,gpu-driver-version=disabled" \
               --num-nodes="1" \
               --node-labels=gke-no-default-nvidia-gpu-device-plugin=true,nvidia.com/gpu.present=true
           

Replace the following:

       * `NODEPOOL_NAME`: a name for your node pool.
       * `CLUSTER_NAME`: the name of your cluster.
       * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane, such as `us-central1` or `us-central1-a`.
       * `NODE_LOCATION1,NODE_LOCATION2,...`: a comma-separated list of zones, in the same region as the control plane, to create nodes in. Choose zones that have [GPU availability](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#view-using-table).
     * Create an autoscaled node pool with `a2-ultragpu-1g` instances that have one NVIDIA A100 (80 GB) GPU in each instance:
           
           gcloud container node-pools create NODEPOOL_NAME \
               --cluster=CLUSTER_NAME \
               --location=CONTROL_PLANE_LOCATION \
               --node-locations=NODE_LOCATION1,NODE_LOCATION2,... \
               **--enable-autoscaling \
               --max-nodes=5** \
               --machine-type="a2-ultragpu-1g" \
               --accelerator="type=nvidia-a100-80gb,count=1,gpu-driver-version=disabled" \
               --num-nodes="1" \
               --node-labels=gke-no-default-nvidia-gpu-device-plugin=true,nvidia.com/gpu.present=true,cloud.google.com/gke-nvidia-gpu-dra-driver=true
           

  2. [Manually install NVIDIA GPU drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

  3. Install DRA drivers.




## Install DRA drivers

  1. Pull and update the Helm chart that contains the NVIDIA DRA driver:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
             && helm repo update
         

  2. Install the NVIDIA DRA GPU driver with version 25.8.0 or later:
         
         helm install nvidia-dra-driver-gpu nvidia/nvidia-dra-driver-gpu \
             --version="25.8.0" --create-namespace --namespace=nvidia-dra-driver-gpu \
             --set nvidiaDriverRoot="/home/kubernetes/bin/nvidia/" \
             --set gpuResourcesEnabledOverride=true \
             --set resources.computeDomains.enabled=false \
             --set kubeletPlugin.priorityClassName="" \
             --set 'kubeletPlugin.tolerations[0].key=nvidia.com/gpu' \
             --set 'kubeletPlugin.tolerations[0].operator=Exists' \
             --set 'kubeletPlugin.tolerations[0].effect=NoSchedule'
         

For Ubuntu nodes, specify the `"/opt/nvidia"` directory path in the `--set nvidiaDriverRoot` flag.




## Verify that your infrastructure is ready for DRA

  1. Verify that your DRA driver Pods are running:
         
         kubectl get pods -n nvidia-dra-driver-gpu
         

The output is similar to the following:
         
         NAME                                         READY   STATUS    RESTARTS   AGE
         nvidia-dra-driver-gpu-kubelet-plugin-52cdm   1/1     Running   0          46s
         

  2. Confirm that the ResourceSlice lists the hardware devices that you added:
         
         kubectl get resourceslices -o yaml
         

The output is similar to the following:
         
         apiVersion: v1
         items:
         - apiVersion: resource.k8s.io/v1
           kind: ResourceSlice
           metadata:
           # Multiple lines are omitted here.
           spec:
             devices:
             - attributes:
                 architecture:
                   string: Ada Lovelace
                 brand:
                   string: Nvidia
                 cudaComputeCapability:
                   version: 8.9.0
                 cudaDriverVersion:
                   version: 13.0.0
                 driverVersion:
                   version: 580.65.6
                 index:
                   int: 0
                 minor:
                   int: 0
                 pcieBusID:
                   string: "0000:00:03.0"
                 productName:
                   string: NVIDIA L4
                 resource.kubernetes.io/pcieRoot:
                   string: pci0000:00
                 type:
                   string: gpu
                 uuid:
                   string: GPU-ccc19e5e-e3cd-f911-65c8-89bcef084e3f
               capacity:
                 memory:
                   value: 23034Mi
               name: gpu-0
             - attributes:
                 architecture:
                   string: Ada Lovelace
                 brand:
                   string: Nvidia
                 cudaComputeCapability:
                   version: 8.9.0
                 cudaDriverVersion:
                   version: 13.0.0
                 driverVersion:
                   version: 580.65.6
                 index:
                   int: 1
                 minor:
                   int: 1
                 pcieBusID:
                   string: "0000:00:04.0"
                 productName:
                   string: NVIDIA L4
                 resource.kubernetes.io/pcieRoot:
                   string: pci0000:00
                 type:
                   string: gpu
                 uuid:
                   string: GPU-f783198d-42f9-7cef-9ea1-bb10578df978
               capacity:
                 memory:
                   value: 23034Mi
               name: gpu-1
             driver: gpu.nvidia.com
             nodeName: gke-cluster-1-dra-gpu-pool-b56c4961-7vnm
             pool:
               generation: 1
               name: gke-cluster-1-dra-gpu-pool-b56c4961-7vnm
               resourceSliceCount: 1
         kind: List
         metadata:
           resourceVersion: ""
         




## What's next

  * [Deploy your workloads with DRA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-dra-workloads)
  * [Allocate network resources with DRA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/allocate-network-resources-dra)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
