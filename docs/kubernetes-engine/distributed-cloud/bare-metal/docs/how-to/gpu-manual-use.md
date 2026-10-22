---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use/
title: Set up and use NVIDIA GPUs \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:23.512185+00:00
---

# Set up and use NVIDIA GPUs  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/gpu-manual-use/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Set up and use NVIDIA GPUs Stay organized with collections  Save and categorize content based on your preferences. 

The _bring your own node_ aspect of Distributed Cloud software only for bare metal lets you take advantage of your advanced hardware, including machines with GPUs, to get the best performance and flexibility for your clusters.

This document describes how to install and use the [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html#about-the-nvidia-gpu-operator) to set up bare metal clusters created with Google Distributed Cloud for use with NVIDIA GPUs.

The NVIDIA GPU Operator uses the [Operator Framework](https://operatorframework.io/) to manage the NVIDIA software components needed to provision and manage GPU devices. We recommend that you use the NVIDIA GPU Operator for the following flexibility and advantages:

  * **Choice of GPU type** : Distributed Cloud software only is compatible with a wide range of GPU types supported by the latest NVIDIA GPU Operator.

  * **Choice of supported operating system** : Cluster worker nodes can use any [supported operating system (OS)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs) with NVIDIA GPUs, and you have the option of using pre-installed GPU drivers or dynamic driver installation with the NVIDIA GPU Operator.

  * **Choice of deployment models** : You can use NVIDIA GPUs on any cluster type with worker nodes: user clusters, standalone clusters, or hybrid clusters.




This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before performing the steps in the following sections, make sure you have the following requirements ready:

  * **Operational cluster** : Ensure you have a functional bare metal cluster created with Google Distributed Cloud.

  * **NVIDIA GPUs** : Ensure that the NVIDIA GPUs are installed on your cluster worker nodes. The following section for installing the NVIDIA GPU Operator includes steps to verify that the GPUs are installed properly and recognized by your operating system.

  * **Compatible NVIDIA driver version** : The NVIDIA driver version you use must be compatible with your GPU, your operating system, and the CUDA version your applications use. You have the following NVIDIA driver installation options:

    * Use the NVIDIA GPU Operator to install the proper version of the NVIDIA GPU driver as described in the following sections.

    * Use the NVIDIA driver preinstalled in your operating system image.

    * Use the instructions in the [NVIDIA Driver Installation Quickstart Guide](https://docs.nvidia.com/datacenter/tesla/pdf/NVIDIA_Driver_Installation_Quickstart.pdf) to manually install the NVIDIA driver.

  * **Helm version 3.0.0 or later** : Install the Helm command-line interface for package management on your admin workstation. You use Helm to install the NVIDIA GPU Operator. You can run the following commands to download and install the Helm command-line tool:
        
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
          && chmod 700 get_helm.sh \
          && ./get_helm.sh
        




## Install and verify the NVIDIA GPU Operator

The following steps guide you through the installation of the NVIDIA GPU Operator on your bare metal cluster and help you to confirm that it's working with your GPUs:

  1. For GPU devices connected through peripheral component interconnect express (PCIe), run the following command to get a list of system PCI buses with "NVIDIA" in their name:
         
         sudo lspci | grep NVIDIA
         

The output is similar to the following:
         
         25:00.0 3D controller: NVIDIA Corporation Device 20b5 (rev a1)
         

  2. You can use the NVIDIA System Management Interface (`nvidia-smi`) command-line tool on a given node to get more detailed information about the GPU devices:
         
         nvidia-smi
         

The output is similar to the following:
         
         +---------------------------------------------------------------------------------------+
         | NVIDIA-SMI 535.183.01             Driver Version: 535.183.1    CUDA Veersion 12.2     |
         |-----------------------------------------+----------------------+----------------------|
         | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
         |                                         |                      |               MIG M. |
         |=========================================+======================+======================|
         |   0  NVIDIA A100 80GB PCIe          Off | 00000000:25:00.0 Off |                    0 |
         | N/A   30C    P0              44W / 300W |      0MiB / 81920MiB |      0%      Default |
         |                                         |                      |             Disabled |
         +-----------------------------------------+----------------------+----------------------+
         
         +---------------------------------------------------------------------------------------+
         | Processes:                                                                            |
         |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
         |        ID   ID                                                             Usage      |
         |=======================================================================================|
         |  No running processes found                                                           |
         +---------------------------------------------------------------------------------------+
         

  3. Add the NVIDIA Helm repository on the admin workstation:
         
         helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
             && helm repo update
         

  4. Install the NVIDIA GPU Operator.

When you install the NVIDIA GPU Operator, there are three basic command variations:

     * Install the NVIDIA GPU Operator with the default configuration:
           
           helm install --wait --generate-name \
               -n gpu-operator --create-namespace \
               nvidia/gpu-operator \
               --set cdi.enabled=true \
               --set cdi.default=true
           

     * Use the `--set` flag to pass a comma-delimited set of key-value pairs to specify configuration options:
           
           helm install --wait --generate-name \
               -n gpu-operator --create-namespace \
               nvidia/gpu-operator \
               --set cdi.enabled=true \
               --set cdi.default=true \
               --set OPTION_1_NAME=OPTION_1_VALUE,OPTION_2_NAME=OPTION_2_VALUE
           

For a detailed list of configuration options, see [Common Chart Customization Options](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#gpu-operator-helm-chart-options) in the NVIDIA documentation. For information about the logistics of using the `--set` flag, see [The Format and Limitations of `--set`](https://helm.sh/docs/intro/using_helm/#the-format-and-limitations-of---set) in the Helm documentation.

     * Disable driver installation if you have already installed the NVIDIA GPU driver on your nodes:

By default, the NVIDIA GPU Operator deploys the latest or specified GPU driver on all GPU worker nodes in the cluster. This requires that all worker nodes with GPUs must run the same operating system version to use the NVIDIA GPU Driver container. To get around this, you can install GPU drivers on nodes manually and run the `helm install` command with `--set driver.enabled=false` to prevent the NVIDIA GPU Operator from deploying drivers.
           
           helm install --wait --generate-name \
               -n gpu-operator --create-namespace \
               nvidia/gpu-operator \
               --set cdi.enabled=true \
               --set cdi.default=true \**    --set driver.enabled=false**
           

For common deployment scenarios and sample commands, see [Common Deployment Scenarios](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#common-deployment-scenarios) in the NVIDIA documentation.

  5. Verify GPU resource exporting:

After the NVIDIA GPU Operator is installed with a GPU driver and device plugin running properly, you should see that the GPU count is configured correctly in the `Allocatable` field for the node resource.
         
         kubectl describe node GPU_NODE_NAME | grep Allocatable -A7
         

Replace `GPU_NODE_NAME` with name of the node machine with the GPU you are testing.

The output is similar to the following:
         
         Allocatable:
           cpu:                127130m
           ephemeral-storage:  858356868519
           hugepages-1Gi:      0
           hugepages-2Mi:      0
           memory:             509648288Ki**nvidia.com/gpu:     1**
           pods:               250
         

  6. To verify that the GPUs are working, run the following sample GPU job, which runs the `nvidia-smi` command:
         
         export NODE_NAME=GPU_NODE_NAME
         
         cat <<EOF | kubectl create --kubeconfig=CLUSTER_KUBECONFIG -f -
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: test-job-gpu
         spec:
           template:
             spec:
               runtimeClassName: nvidia
               containers:
               - name: nvidia-test
                 image: nvidia/cuda:12.0.0-base-ubuntu22.04**        command: ["nvidia-smi"]**
                 resources:
                   limits:
                     nvidia.com/gpu: 1
               nodeSelector:
                 kubernetes.io/hostname: ${NODE_NAME}
               restartPolicy: Never
         EOF
         

Replace `CLUSTER_KUBECONFIG` with the path of the cluster kubeconfig file.

  7. Check the logs for the sample job output:
         
         kubectl logs job/test-job-gpu --kubeconfig=CLUSTER_KUBECONFIG
         

The output is similar to the following:
         
         +---------------------------------------------------------------------------------------+
         | NVIDIA-SMI 535.183.01             Driver Version: 535.183.1    CUDA Veersion 12.2     |
         |-----------------------------------------+----------------------+----------------------|
         | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
         |                                         |                      |               MIG M. |
         |=========================================+======================+======================|
         |   0  NVIDIA A100 80GB PCIe          Off | 00000000:25:00.0 Off |                    0 |
         | N/A   30C    P0              44W / 300W |      0MiB / 81920MiB |      0%      Default |
         |                                         |                      |             Disabled |
         +-----------------------------------------+----------------------+----------------------+
         
         +---------------------------------------------------------------------------------------+
         | Processes:                                                                            |
         |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
         |        ID   ID                                                             Usage      |
         |=======================================================================================|
         |  No running processes found                                                           |
         +---------------------------------------------------------------------------------------+
         




## Limitations

The following limitations apply when you use NVIDIA GPU Operator with clusters created with Google Distributed Cloud:

  * If you install a recent version of NVIDIA GPU Operator, containerd configurations applied by the operator might be overwritten during cluster or node pool updates or upgrades.

  * Use the Container Device Interface (CDI) for GPU workloads. For earlier versions of Google Distributed Cloud that use containerd 1.6, some CDI capabilities might not be available.

  * Load balancer node pools automatically run an update job every 7 days. This job overwrites containerd configurations, including those added by the NVIDIA GPU Operator.




## Best practices

To minimize conflicts and problems with your NVIDIA configurations, we recommend that you use the following precautions:

  * Back up the containerd config file, `/etc/containerd/config.toml`, before you upgrade or update the cluster or node pools. This file contains the `nvidia` runtime configuration. Restore the `config.toml` file after the upgrade or update completes successfully and restart containerd for any configuration changes to take effect.

  * To prevent potential conflicts or issues with the containerd configuration, don't use GPU nodes as load balancer nodes (`loadBalancer.nodePoolSpec`).




## Get Support

If you need additional assistance related to using GPUs with Google Distributed Cloud, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support).

For issues related to setting up or using GPU hardware on your operating system, refer to your hardware vendor or, if applicable, to [NVIDIA Support](https://www.nvidia.com/en-us/support/) directly.

Your feedback is appreciated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
