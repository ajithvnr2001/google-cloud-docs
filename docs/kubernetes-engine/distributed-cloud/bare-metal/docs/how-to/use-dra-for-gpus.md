---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/use-dra-for-gpus/
title: Manage GPU devices with dynamic resource allocation \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:50.768354+00:00
---

# Manage GPU devices with dynamic resource allocation  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/use-dra-for-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Manage GPU devices with dynamic resource allocation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure your GPU workloads to use dynamic resource allocation in your Google Distributed Cloud bare metal clusters. Dynamic resource allocation is a Kubernetes API that lets you request and share generic resources, such as GPUs, among Pods and containers. Third-party drivers manage these resources. 

With dynamic resource allocation, Kubernetes schedules Pods based on the referenced device configuration. App operators don't need to select specific nodes in their workloads and don't need to ensure that each Pod requests exactly the number of devices that are attached to those nodes. This process is similar to allocating volumes for storage.

This capability helps you run AI workloads by dynamically and precisely allocating the GPU resources within your bare metal clusters, improving resource utilization and performance for demanding workloads.

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you configure your GPU workloads to use dynamic resource allocation, verify that the following prerequisites are met:

  * Your bare metal cluster is at version 1.33.0 or later.
  * Your operating system is either Ubuntu 22.04 or Red Hat Enterprise Linux (RHEL) 9.4.
  * You have updated your cluster to enable dynamic resource allocation as described in [Enable dynamic resource allocation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#enable-dra).
  * You have at least one node machine with a GPU attached and the NVIDIA GPU driver installed. For more information, see [Install or uninstall the bundled NVIDIA GPU Operator](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#gpu-oper).
  * If you are using the bundled NVIDIA GPU operator, version 1.33.0 or later enables Container Device Interface (CDI) by default. If you are using a manually installed GPU operator, ensure CDI is enabled in the `ClusterPolicy`.
  * You have followed the instructions in [NVIDIA DRA Driver for GPUs](https://github.com/NVIDIA/k8s-dra-driver-gpu?tab=readme-ov-file#nvidia-dra-driver-for-gpus) to install the NVIDIA DRA driver on all GPU-attached nodes.



## Create GPU workloads that use dynamic resource allocation

For your GPU workloads to take advantage of dynamic resource allocation to request GPUs, they must be in a shared namespace with a `ResourceClaim` that describes the request for GPU device allocation. Your workloads must reference the `ResourceClaim` for Kubernetes to assign GPU resources.

The following steps set up an environment in which your workloads use dynamic resource allocation to request GPU resources:

  1. To create resources related to dynamic resource allocation, create a new `Namespace` in your cluster:
         
         cat <<EOF | kubectl apply --kubeconfig=CLUSTER_KUBECONFIG -f -
         apiVersion: v1
         kind: Namespace
         metadata:
           name: NAMESPACE_NAME
         EOF
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the path of the user cluster kubeconfig file.

     * `NAMESPACE_NAME` with the name for your dynamic resource allocation namespace.

  2. Create a `ResourceClaim` to describe the request for GPU access:
         
         cat <<EOF | kubectl apply --kubeconfig=CLUSTER_KUBECONFIG -f -
         apiVersion: resource.k8s.io/v1beta1
         kind: ResourceClaim
         metadata:
           namespace: NAMESPACE_NAME
           name: RESOURCE_CLAIM_NAME
         spec:
             devices:
               requests:
               - name: gpu
                 deviceClassName: gpu.nvidia.com
         EOF
         

Replace `RESOURCE_CLAIM_NAME` with the name of your resource claim for GPU requests.

  3. Create workloads that reference the `ResourceClaim` created in the preceding step.

The following workload examples show how to reference a `ResourceClaim` named `gpu-claim` in the `dra-test` namespace. The containers in the `pod1` Pod are NVIDIA [compute unified device architecture (CUDA) samples](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/k8s/containers/cuda-sample) designed to run CUDA workloads on the GPUs. When the `pod1` Pod completes successfully, it indicates that the dynamic resource allocation capability is working properly and dynamic resource allocation is ready to manage GPU resources in your cluster.

###  Ubuntu 

     1. Use the following command to apply the manifest to your cluster:
            
            cat <<EOF | kubectl apply --kubeconfig=CLUSTER_KUBECONFIG -f -
            apiVersion: v1
            kind: Pod
            metadata:
              name: pod1
              namespace: dra-test
            spec:
              restartPolicy: OnFailure**  resourceClaims:
                - name: gpu
                  resourceClaimName: gpu-claim**
              containers:
                - name: ctr0
                  image: nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda12.5.0**      resources:
                    claims:
                      - name: gpu**
                - name: ctr1
                  image: nvcr.io/nvidia/k8s/cuda-sample:devicequery**      resources:
                    claims:
                      - name: gpu**
            EOF
            

###  RHEL 

     1. Use the following command to apply the manifest to your cluster:
            
            cat <<EOF | kubectl apply --kubeconfig=CLUSTER_KUBECONFIG -f -
            apiVersion: v1
            kind: Pod
            metadata:
              name: pod1
              namespace: dra-test
            spec:
              restartPolicy: OnFailure
            
              resourceClaims:
                - name: gpu
                  resourceClaimName: gpu-claim
              containers:
                - name: ctr0
                  image: nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda12.5.0**      resources:
                    claims:
                      - name: gpu**
                - name: ctr1
                  image: nvcr.io/nvidia/k8s/cuda-sample:devicequery**      resources:
                    claims:
                      - name: gpu**
            EOF
            




## Limitations

Consider the following limitations when you use dynamic resource allocation:

  * When you use RHEL OS with a supported version of the NVIDIA GPU operator, the Container Device Interface (CDI) handles device injection and SELinux labeling automatically. You aren't required to use manual SELinux policy configuration or set pod `securityContext`.

  * This feature uses the `resource.k8s.io/v1beta1` API group, which differs from the open source Kubernetes API group for this feature, `resource.k8s.io/v1`. The `v1` open source API group provides more features and better stability than the `v1beta1` API group.




## What's next

  * Refer to the Kubernetes documentation for more information about [dynamic resource allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/).
  * Learn how to [serve third-party LLMs on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/serve-3p-llms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
