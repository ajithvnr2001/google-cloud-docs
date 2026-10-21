---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator/
title: Manage the GPU Stack with the NVIDIA GPU Operator on Google Kubernetes Engine (GKE) \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:19.582559+00:00
---

# Manage the GPU Stack with the NVIDIA GPU Operator on Google Kubernetes Engine (GKE)  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-operator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Manage the GPU Stack with the NVIDIA GPU Operator on Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page helps you decide when to use the NVIDIA GPU operator and shows you how to enable the NVIDIA GPU Operator on GKE.

## Overview

[Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) are Kubernetes software extensions that allow users to create custom resources that manage applications and their components. You can use operators to automate complex tasks beyond what Kubernetes itself provides, such as deploying and upgrading applications.

The NVIDIA GPU Operator is a Kubernetes operator that provides a common infrastructure and API for deploying, configuring, and managing software components needed to provision NVIDIA GPUs in a Kubernetes cluster. The NVIDIA GPU Operator provides you with a consistent experience, simplifies GPU resource management, and streamlines the integration of GPU-accelerated workloads into Kubernetes.

### Why use the NVIDIA GPU Operator?

We recommend using GKE GPU management for your GPU nodes, because GKE fully manages the GPU node lifecycle. To get started with using GKE to manage your GPU nodes, choose one of these options:

  * [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
  * [Run GPUs in Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)



Alternatively, the NVIDIA GPU Operator might be a suitable option for you if you're looking for a consistent experience across multiple cloud service providers, you are already using the NVIDIA GPU Operator, or if you are using software that depends on the NVIDIA GPU operator.

For more considerations when deciding between these options, refer to [Manage the GPU stack through GKE or the NVIDIA GPU Operator on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#manage-gpu-stack).

### Limitations

The NVIDIA GPU Operator is supported on both Container-Optimized OS (COS) and Ubuntu node images with the following limitations:

  * The NVIDIA GPU Operator is supported on GKE starting with [GPU Operator version 24.6.0](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/24.6.0/release-notes.html) or later.
  * The NVIDIA GPU Operator is not supported on Autopilot clusters.
  * The NVIDIA GPU Operator is not supported on Windows node images.
  * The NVIDIA GPU Operator is not managed by GKE. To upgrade the NVIDIA GPU Operator, refer to the [NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/upgrade.html).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Make sure you meet the requirements in [Run GPUs in Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * Verify that you have Helm installed in your development environment. Helm comes pre-installed on [Cloud Shell](https://docs.cloud.google.com/shell).

While there is no specific Helm version requirement, you can use the following command to verify that you have Helm installed.
        
        helm version
        

If the output is similar to `Command helm not found`, then you can install the Helm CLI by running this command:
        
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
          && chmod 700 get_helm.sh \
          && ./get_helm.sh
        




## Create and set up the GPU node pool

To create and set up the GPU node pool, follow these steps:

  1. Create a GPU node pool by following the instructions on how to [Create a GPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create) with the following modifications:

     * Set `gpu-driver-version=disabled` to skip automatic GPU driver installation since it's not supported when using the NVIDIA GPU operator.
     * Set `--node-labels="gke-no-default-nvidia-gpu-device-plugin=true"` to disable the GKE managed GPU device plugin Daemonset.

Run the following command and append other flags for GPU node pool creation as needed:
    
    gcloud container node-pools create POOL_NAME \
      --accelerator type=GPU_TYPE,count=AMOUNT,gpu-driver-version=disabled \
      --node-labels="gke-no-default-nvidia-gpu-device-plugin=true"
    

Replace the following:

     * _POOL_NAME_ the name you chose for the node pool.
     * _GPU_TYPE :_ the type of [GPU accelerator ](https://docs.cloud.google.com/compute/docs/gpus) that you want to use. For example, `nvidia-h100-80gb`.
     * _AMOUNT_ : the number of GPUs to attach to nodes in the node pool.

For example, the following command creates a GKE node pool, `a3nodepool`, with H100 GPUs in the zonal cluster `a3-cluster`. In this example, the GKE GPU device plugin Daemonset and automatic driver installation are disabled.
    
    gcloud container node-pools create a3nodepool \
      --cluster=a3-cluster \
      --location=us-central1 \
      --node-locations=us-central1-a \
      --accelerator=type=nvidia-h100-80gb,count=8,gpu-driver-version=disabled \
      --machine-type=a3-highgpu-8g \
      --node-labels="gke-no-default-nvidia-gpu-device-plugin=true" \
      --num-nodes=1
    

  2. Get the authentication credentials for the cluster by running the following command:
         
         USE_GKE_GCLOUD_AUTH_PLUGIN=True \
         gcloud container clusters get-credentials CLUSTER_NAME \
           --location CONTROL_PLANE_LOCATION
         

Replace the following:

     * _CLUSTER_NAME_ : the name of the cluster containing your node pool.
     * _CONTROL_PLANE_LOCATION_ : the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

The output is similar to the following:
    
    Fetching cluster endpoint and auth data.
    kubeconfig entry generated for CLUSTER_NAME.
    

  3. (Optional) Verify that you can connect to the cluster.
         
         kubectl get nodes -o wide
         

You should see a list of all your nodes running in this cluster.

  4. Create the namespace `gpu-operator` for the NVIDIA GPU Operator by running this command:
         
         kubectl create ns gpu-operator
         

The output is similar to the following:
         
         namespace/gpu-operator created
         

  5. Create resource quota in the `gpu-operator` namespace by running this command:
         
         kubectl apply -n gpu-operator -f - << EOF
         apiVersion: v1
         kind: ResourceQuota
         metadata:
           name: gpu-operator-quota
         spec:
           hard:
             pods: 100
           scopeSelector:
             matchExpressions:
             - operator: In
               scopeName: PriorityClass
               values:
                 - system-node-critical
                 - system-cluster-critical
         EOF
         

The output is similar to the following:
         
         resourcequota/gpu-operator-quota created
         

  6. View the resource quota for the `gpu-operator` namespace:
         
         kubectl get -n gpu-operator resourcequota gpu-operator-quota
         

The output is similar to the following:
         
         NAME                 AGE     REQUEST       LIMIT
         gpu-operator-quota   2m27s   pods: 0/100
         

  7. Manually install the drivers on your Container-Optimized OS or Ubuntu nodes. For detailed instructions, refer to [Manually install NVIDIA GPU drivers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

     * If using COS, run the following commands to deploy the installation [DaemonSet](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml) and install the default GPU driver version:
           
           kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml
           

     * If using Ubuntu, the installation DaemonSet that you deploy depends on the GPU type and on the GKE node version as described in the [Ubuntu section of the instructions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

  8. Verify the GPU driver version by running this command:
         
         kubectl logs -l k8s-app=nvidia-driver-installer  \
           -c "nvidia-driver-installer" --tail=-1 -n kube-system
         

If GPU driver installation is successful, the output is similar to the following:
         
         I0716 03:17:38.863927    6293 cache.go:66] DRIVER_VERSION=535.183.01
         …
         I0716 03:17:38.863955    6293 installer.go:58] Verifying GPU driver installation
         I0716 03:17:41.534387    6293 install.go:543] Finished installing the drivers.
         




## Install the NVIDIA GPU Operator

This section shows how to install the NVIDIA GPU Operator using Helm. To learn more, refer to NVIDIA's documentation on [installing the NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#installing-the-nvidia-gpu-operator).

  1. Add the NVIDIA Helm repository:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
           && helm repo update
         

  2. Install the NVIDIA GPU Operator using Helm with the following configuration options:

     * Make sure the GPU Operator version is 24.6.0 or later.
     * Configure the driver install path in the GPU Operator with `hostPaths.driverInstallDir=/home/kubernetes/bin/nvidia`.
     * Set the toolkit install path `toolkit.installDir=/home/kubernetes/bin/nvidia` for both COS and Ubuntu. In COS, the`/home` directory is writable and serves as a stateful location for storing the NVIDIA runtime binaries. To learn more, refer to the COS [Disks and file system overview](https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem).

### v25.10.0 or later
    
    helm install --wait --generate-name \
      -n gpu-operator \
      nvidia/gpu-operator \
      --set hostPaths.driverInstallDir=/home/kubernetes/bin/nvidia \
      --set toolkit.installDir=/home/kubernetes/bin/nvidia \
      --set driver.enabled=false
    

### v25.3.4 or earlier

     * Enable the Container Device Interface (CDI) in the GPU Operator with `cdi.enabled=true` and `cdi.default=true` as legacy mode is unsupported. CDI is required for both COS and Ubuntu on GKE.
    
    helm install --wait --generate-name \
      --version=v25.3.4 \
      -n gpu-operator \
      nvidia/gpu-operator \
      --set hostPaths.driverInstallDir=/home/kubernetes/bin/nvidia \
      --set toolkit.installDir=/home/kubernetes/bin/nvidia \
      --set cdi.enabled=true \
      --set cdi.default=true \
      --set driver.enabled=false \
      --set operator.runtimeClass=containerd \
      --set 'toolkit.env[0].name=CONTAINERD_CONFIG' \
      --set 'toolkit.env[0].value=/etc/containerd/config.toml' \
      --set 'toolkit.env[1].name=CONTAINERD_SOCKET' \
      --set 'toolkit.env[1].value=/run/containerd/containerd.sock' \
      --set 'toolkit.env[2].name=RUNTIME_CONFIG_SOURCE' \
      --set 'toolkit.env[2].value="command\, file"'
    

To learn more about these settings, refer to the [Common Chart Customization Options](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#gpu-operator-helm-chart-options) and [Common Deployment Scenarios](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#common-deployment-scenarios) in the NVIDIA documentation.

  3. Verify that the NVIDIA GPU operator is successfully installed.

     1. To check that the GPU Operator operands are running correctly, run the following command.
            
            kubectl get pods -n gpu-operator
            

The output looks similar to the following:
            
            NAME                                                          READY    STATUS
            RESTARTS   AGE
            gpu-operator-5c7cf8b4f6-bx4rg                                 1/1      Running   0          11m
            gpu-operator-node-feature-discovery-gc-79d6d968bb-g7gv9       1/1      Running   0          11m
            gpu-operator-node-feature-discovery-master-6d9f8d497c-thhlz   1/1      Running   0          11m
            gpu-operator-node-feature-discovery-worker-wn79l              1/1      Running   0          11m
            gpu-feature-discovery-fs9gw                                   1/1      Running   0          8m14s
            gpu-operator-node-feature-discovery-worker-bdqnv              1/1      Running   0          9m5s
            nvidia-container-toolkit-daemonset-vr8fv                      1/1      Running   0          8m15s
            nvidia-cuda-validator-4nljj                                   0/1      Completed 0          2m24s
            nvidia-dcgm-exporter-4mjvh                                    1/1      Running   0          8m15s
            nvidia-device-plugin-daemonset-jfbcj                          1/1      Running   0          8m15s
            nvidia-mig-manager-kzncr                                      1/1      Running   0          2m5s
            nvidia-operator-validator-fcrr6                               1/1      Running   0          8m15s
            

**Note:** GKE schedules the `gpu-operator` and `gpu-node-feature-discovery` Pods to run on non-GPU nodes if the cluster has non-GPU node pools.
     2. To check that the GPU count is configured correctly in the node's 'Allocatable' field, run the following command:
            
            kubectl describe node GPU_NODE_NAME | grep Allocatable -A7
            

Replace GPU_NODE_NAME with the name of the node that has GPUs.

The output is similar to the following:
            
            Allocatable:
            cpu:                11900m
            ephemeral-storage:  47060071478
            hugepages-1Gi:      0
            hugepages-2Mi:      0
            memory:             80403000Ki
            nvidia.com/gpu:     1           # showing correct count of GPU associated with the nods
            pods:               110
            

     3. To check that GPU workload runs correctly, you can use the `cuda-vectoradd` tool:
            
            cat << EOF | kubectl create -f -
            apiVersion: v1
            kind: Pod
            metadata:
              name: cuda-vectoradd
            spec:
              restartPolicy: OnFailure
              containers:
              - name: vectoradd
                image: nvidia/samples:vectoradd-cuda11.2.1
                resources:
                  limits:
                    nvidia.com/gpu: 1
            EOF
            

Then, run the following command:
            
            kubectl logs cuda-vectoradd
            

The output is similar to the following:
            
            [Vector addition of 50000 elements]
            Copy input data from the host memory to the CUDA device
            CUDA kernel launch with 196 blocks of 256 threads
            Copy output data from the CUDA device to the host memory
            Test PASSED
            Done
            




## What's next

  * [Learn how to run GPUs in Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus).
  * [Learn about GPU sharing strategies for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus).
  * [Learn best practices for autoscaling LLM inference workloads with GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling).
  * Explore the [NVIDIA GPU Operator documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/google-gke.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
