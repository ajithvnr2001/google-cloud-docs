---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/use-gpu/
title: Enable and use NVIDIA GPUS in VMs with VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:16.315172+00:00
---

# Enable and use NVIDIA GPUS in VMs with VM Runtime on GDC  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/use-gpu/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Enable and use NVIDIA GPUS in VMs with VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/use-gpu)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/use-gpu)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document shows you how to enable ​​NVIDIA® GPU support for virtual machines (VMs) that run using VM Runtime on GDC. You learn how to install the NVIDIA drivers on your Google Distributed Cloud nodes, verify that the GPUs are available, and assign GPUs to VMs.

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Distributed Cloud on Compute Engine](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-clusters-overview).
  * The `virtctl` client tool installed as a plugin for `kubectl`. If needed, [install the virtctl client tool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/quickstart#install_the_virtctl_client_tool).



## Supported Nvidia GPU cards

Google Distributed Cloud version 1.13 or higher support the following NVIDIA GPUs:

  * Tesla T4
  * Tesla P4
  * Tesla V100 SXM2 32 GB
  * A100 SXM4 40 GB
  * A100 PCIe 40 GB
  * A100 SXM4 80 GB
  * A100 PCIe 80 GB



## Install NVIDIA drivers on nodes

Before your VMs can use the NVIDIA GPUs, you must configure your Google Distributed Cloud nodes to support the GPU devices. To install the NVIDIA drivers on your nodes, complete the following steps on each node in your cluster that includes an NVIDIA GPU. This document uses a [supported Ubuntu version](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/os-reqs) for the nodes:

  1. Connect to your Google Distributed Cloud node that you want to configure for GPU support.
  2. Get the kernel version of your node:
         
         KERNEL_VERSION="$(uname -r)"
         

  3. Update your Ubuntu node and install the appropriate kernel headers:
         
         sudo apt update && \
         apt install -y linux-headers-${KERNEL_VERSION}
         

  4. Install the `build-essential` package so that you can compile the Nvidia drivers in a following step:
         
         sudo apt install -y build-essential
         

  5. Download the appropriate NVIDIA driver package for your GPU. For a complete list of drivers, see [NVIDIA Driver Downloads](https://www.nvidia.com/download/index.aspx).

The following example downloads the `Linux x86_64` version `470.82.01` driver:
         
         wget https://us.download.nvidia.com/tesla/470.82.01/NVIDIA-Linux-x86_64-470.82.01.run
         

  6. Install the NVIDIA driver package. Use the name of the NVIDIA driver package you downloaded in the previous step:
         
         sudo sh NVIDIA-Linux-x86_64-470.82.01.run \
           --accept-license \
           --silent \
           --no-nouveau-check
         

  7. Load the NVIDIA kernel module:
         
         sudo modprobe nvidia
         

  8. Repeat the steps in this section on each node in your cluster that has a NVIDIA GPU.




## Enable GPU support in VM Runtime on GDC

After you install the NVIDIA drivers on your Google Distributed Cloud node(s), you enable GPU support in VM Runtime on GDC. Your VMs can then access the GPUs on the nodes.

Each node reboots as part of the following process. Your VMs may be affected by this reboot process. If possible and configured to do so, migratable VMs migrate to other nodes. For more information, see how to [configure the eviction policy for VMs during maintenance events](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/eviction-policy).

To enable GPU support in VM Runtime on GDC, complete the following steps.

  1. Edit the `VMRuntime` custom resource:
         
         kubectl edit vmruntime vmruntime
         

  2. Add the `enableGPU: true` property to the `VMRuntime` manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           enabled: true
           enableGPU: true
         ...
         

  3. Save and close the `VMRuntime` custom resource in your editor.

  4. Check the status of the GPU controllers in the `vm-system` namespace:
         
         kubectl get pods --namespace vm-system  -w
         

It takes about five minutes for the controllers to be successfully enabled. Wait for the `STATUS` to show `Running` for all the GPU controllers. The following example output shows the desired state:
         
         NAME                                          READY  STATUS    RESTARTS     AGE
         gpu-controller-controller-manager-gwvcb       2/2    Running   0            10m
         kubevirt-gpu-dp-daemonset-2lfkl               1/1    Running   0            10m
         kubevm-gpu-driver-daemonset-5fwh6             1/1    Running   0            10m
         nvidia-gpu-dp-daemonset-9zq2w                 1/1    Running   0            10m
         nvidia-mig-manager-5g7pz                      1/1    Running   0            10m
         vm-controller-controller-manager-7b6df6979b   2/2    Running   2 (13m ago)  14m
         

  5. Verify that the GPUs are available for use when the GPU controllers all report their status as `Running`:
         
         kubectl get gpuallocations --namespace vm-system
         

The following example output shows that the GPUs on the nodes are available for use. Each node in your cluster with GPU support is shown. You allocate them to VMs in the next section:
         
         NAME       ALLOCATED   DEVICEMODEL
         bm-node1   true        Tesla A100 SXM4 40GB
         bm-node2   true        Tesla A100 SXM4 40GB
         




## Allocate GPUs for use with VMs

With GPU support configured in the Anthos clusters on bare metal nodes and in VM Runtime on GDC, allocate the GPUs for use with VMs. By default, GPUs are allocated for use with pods (containers).

  1. Edit the `GPUAllocation` custom resource for use with VMs. This step assigns the GPUs on the nodes for use with VMs:
         
         kubectl edit gpuallocation NODE_NAME --namespace vm-system
         

Replace `NODE_NAME` with the name of your node that you want to allocate GPUs from.

  2. Configure how many GPUs to allocate to VMs. Initially, all GPUs are allocated to pods.

The total number of GPUs allocated to VMs and pods must equal the number of GPUs in the node. For example, you might have four GPUs in your node. If you allocate two GPUs to VMs, then two GPUs remain allocated to pods. The `GPUAllocation` manifest is rejected if you try to allocate two GPUs to VMs and one GPU to pods, as one GPU is left unallocated.

Update the number of GPUs on the node that you want to allocate for use with VMs, as shown in the following example:
         
         apiVersion: gpu.cluster.gke.io/v1
         kind: GPUAllocation
         metadata:
           name: gpu-w2
           namespace: vm-system
         spec:
           node: gpu-w2
           pod: 0
           vm: 4
         

In this example, all four GPUs installed in the node are allocated to VMs. No GPUs are allocated to pods.

  3. Save and close the `GPUAllocation` custom resource in your editor.

  4. Verify that the GPUs report their `ALLOCATED` status as `true`:
         
         kubectl get gpuallocations --namespace vm-system
         

The following example output shows that the GPUs on the nodes are available for use:
         
         NAME     ALLOCATED   DEVICEMODEL
         gpu-w1   true        Tesla A100 SXM4 40GB
         gpu-w2   true        Tesla A100 SXM4 40GB
         




## Create a VM with GPU support

You can now create a VM that uses the GPU from the node. In the VM custom resource, you specify the name and quantity of GPUs to allocate from the node.

  1. Get the name of the GPU card from the host:
         
         kubectl describe node NODE_NAME
         

Replace `NODE_NAME` with the name of the host that you want to get the GPU name from.

The following example output shows that the allocatable GPU name on this node is `NVIDIA_A100_SXM4_40GB`:
         
         Name:               bm-node1
         Roles:              worker
         [...]
         Allocatable:
           cpu:                                         47810m
           [...]
           memory:                                      336929400Ki
           nvidia.com/gpu-vm-NVIDIA_A100_SXM4_40GB:     1
         [...]
         

  2. Create a `VirtualMachine` manifest, such as `my-gpu-vm.yaml`, in the editor of your choice:
         
         nano my-gpu-vm.yaml
         

  3. Copy and paste the following YAML manifest:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - virtualMachineDiskName: VM_NAME-boot-dv
               boot: true
               gpu:
                 model: nvidia.com/gpu-vm-GPU_NAME
                 quantity: 1
         

In this YAML file, define the following settings:

     * `VM_NAME`: the name for your VM.
     * `GPU_NAME`: the GPU name from the node to allocate to the VM. 
       * This GPU name is shown in the output of the `kubectl describe node`command from a previous step, such as `NVIDIA_A100_SXM4_40GB`.

The VM connects `eth0` to the default `pod-network` network.

The boot disk named `VM_NAME-boot-dv` must already exist. For more information, see [Create and manage virtual disks](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/create-manage-disks).

  4. Save and close the VM manifest in your editor.

  5. Create the VM using `kubectl`:
         
         kubectl apply -f my-gpu-vm.yaml
         

  6. When your VM is running, [connect to the VM](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/connect-vms) and verify that the GPU hardware is available.




## What's next

  * [Edit a VM in Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/vm-runtime/edit-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
