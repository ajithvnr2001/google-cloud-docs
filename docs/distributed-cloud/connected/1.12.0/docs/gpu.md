---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu/
title: Manage GPU workloads \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:00.117757+00:00
---

# Manage GPU workloads  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Manage GPU workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage graphics processing unit (GPU) workloads on Google Distributed Cloud connected. To take advantage of this functionality, you must have a Distributed Cloud connected hardware configuration that contains GPUs. For more information, see [Plan the hardware configuration](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements#hardware).

Distributed Cloud connected workloads can run in containers and on virtual machines:

  * **GPU workloads running in containers.** All GPU resources on your Distributed Cloud connected cluster are initially allocated to workloads running in containers. The GPU driver for running GPU-based containerized workloads is included in Distributed Cloud connected. Within each container, GPU libraries are mounted at `/opt/nvidia`.

  * **GPU workloads running on virtual machines.** To run a GPU-based workload on a virtual machine, you must allocate GPU resources on the target Distributed Cloud connected node to virtual machines, as described later on this page. Doing so bypasses the built-in GPU driver and passes the GPUs directly through to virtual machines. You must manually install a compatible GPU driver on each virtual machine's guest operating system. You must also secure all the licensing required to run specialized GPU drivers on your virtual machines.




To confirm that GPUs are present on a Distributed Cloud connected node, verify that the node has the `vm.cluster.gke.io.gpu=true` label. If the label is not present on the node, then there are no GPUs installed on the corresponding Distributed Cloud connected physical machine.

## Allocate GPU resources

By default, all GPU resources on each node in the cluster are allocated to containerized workloads. To customize the allocation of GPU resources on each node, complete the steps in this section.

### Configure GPU resource allocation

  1. To allocate GPU resources on a Distributed Cloud connected node, use the following command to edit the `GPUAllocation` custom resource on the target node:
         
         kubectl edit gpuallocation NODE_NAME --namespace vm-system

Replace `NODE_NAME` with the name of the target Distributed Cloud node.

In the following example, the command's output shows the factory-default GPU resource allocation. By default, all GPU resources are allocated to containerized (`pod`) workloads, and no GPU resources are allocated to virtual machine (`vm`) workloads:
         
         ...
         spec:
           pod:   2  # Number of GPUs allocated for container workloads
           vm:    0  # Number of GPUs allocated for VM workloads
         

  2. Set your GPU resource allocations as follows:

     * To allocate a GPU resource to containerized workloads, increase the value of the `pod` field and decrease the value of the `vm` field by the same amount.
     * To allocate a GPU resource to virtual machine workloads, increase the value of the `vm` field and decrease the value of the `pod` field by the same amount.

The total number of allocated GPU resources must not exceed the number of GPUs installed on the physical Distributed Cloud connected machine on which the node runs; otherwise, the node rejects the invalid allocation.

In the following example, two GPU resources have been reallocated from containerized (`pod`) workloads to virtual machine (`vm`) workloads:
    
    ...
    spec:
      pod:   0  # Number of GPUs allocated for container workloads
      vm:    2  # Number of GPUs allocated for VM workloads
    

When you finish, apply the modified `GPUAllocation` resource to your cluster and wait for its status to change to `AllocationFulfilled`.




### Check GPU resource allocation

  * To check your GPU resource allocation, use the following command:
        
        kubectl describe gpuallocations NODE_NAME --namespace vm-system

Replace `NODE_NAME` with the name of the target Distributed Cloud connected node.

The command returns output similar to the following example:
        
        Name:         mynode1
         ...
         spec:
           node:  mynode1
           pod:   2  # Number of GPUs allocated for container workloads
           vm:    0  # Number of GPUs allocated for VM workloads
         Status:
           Allocated:  true
           Conditions:
             Last Transition Time:  2022-09-23T03:14:10Z
             Message:
             Observed Generation:   1
             Reason:                AllocationFulfilled
             Status:                True
             Type:                  AllocationStatus
             Last Transition Time:  2022-09-23T03:14:16Z
             Message:
             Observed Generation:   1
             Reason:                DeviceStateUpdated
             Status:                True
             Type:                  DeviceStateUpdated
           Consumption:
             pod:         0/2   # Number of GPUs currently consumed by container workloads
             vm:          0/0   # Number of GPUs currently consumed by VM workloads
           Device Model:  NVIDIA L4
         Events:          <none>
        




## Configure a container to use GPU resources

To configure a container running on Distributed Cloud connected to use GPU resources, configure its specification as shown in the following example, and then apply it to your cluster:
    
    
      apiVersion: v1
      kind: Pod
      metadata:
        name: my-gpu-pod
      spec:
        containers:
        - name: my-gpu-container
          image: CUDA_TOOLKIT_IMAGE
          command: ["/bin/bash", "-c", "--"]
          args: ["while true; do sleep 600; done;"]
          env:
          resources:
            requests:
            GPU_MODEL: 2
            limits:
            GPU_MODEL: 2
        nodeSelector:
          kubernetes.io/hostname: NODE_NAME

Replace the following:

  * `CUDA_TOOLKIT_IMAGE`: the full path and name of the NVIDIA CUDA toolkit image. The version of the CUDA toolkit must match the version of the NVIDIA driver running on your Distributed Cloud connected cluster. To determine your NVIDIA driver version, see the [Distributed Cloud release notes](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/release-notes). To find the matching CUDA toolkit version, see [CUDA Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/index.html).
  * `NODE_NAME`: the name of the target Distributed Cloud connected node.
  * `GPU_MODEL`: the model of NVIDIA GPU installed in the target Distributed Cloud connected machine. As of this release, the only supported value is `nvidia.com/gpu-pod-NVIDIA_L4` for the NVIDIA L4 GPU.



## Configure a virtual machine to use GPU resources

To configure a virtual machine running on Distributed Cloud connected to use GPU resources, configure its `VirtualMachine` resource specification as shown in the following example, and then apply it to your cluster:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    ...
    spec:
      ...
      gpu:
        model: GPU_MODEL
        quantity: 2

Replace the following:

  * `GPU_MODEL`: the model of NVIDIA GPU installed in the target Distributed Cloud connected machine. As of this release, the only supported value is `nvidia.com/gpu-pod-NVIDIA_L4` for the NVIDIA L4 GPU.



## What's next

  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/virtual-machines)
  * [Deploy workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/machines)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/clusters)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
