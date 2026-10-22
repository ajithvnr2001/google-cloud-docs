---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/deploy-gpu-container-workloads/
title: Manage GPU container workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:44.412893+00:00
---

# Manage GPU container workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/deploy-gpu-container-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage GPU container workloads Stay organized with collections  Save and categorize content based on your preferences. 

You can enable and manage graphics processing unit (GPU) resources on your containers. For example, you might prefer running artificial intelligence (AI) and machine learning (ML) notebooks in a GPU environment. GPU support is enabled by default in Google Distributed Cloud (GDC) air-gapped appliance.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view the resources in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role in your project namespace. This role lets you deploy GPU workloads in your project namespace.

### Prepare your environment

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/pa-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the bare metal Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Configure a container to use GPU resources

To use GPUs in a container, complete the following steps:

  1. Confirm your Kubernetes cluster nodes support your GPU resource allocation:
         
         kubectl describe nodes NODE_NAME
         

Replace `NODE_NAME` with the node managing the GPUs you want to inspect.

The relevant output is similar to the following snippet:
         
         Capacity:
           nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
         Allocatable:
           nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
         

  2. Add the `.containers.resources.requests` and `.containers.resources.limits` fields to your container spec. Since your Kubernetes cluster is preconfigured with GPU machines, the configuration is the same for all workloads:
         
         ...
          containers:
          - name: CONTAINER_NAME
            image: CONTAINER_IMAGE
            resources:
              requests:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
              limits:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
          ...
         

Replace the following:

     * `CONTAINER_NAME`: the name of the container.
     * `CONTAINER_IMAGE`: the container image to access the GPU machines. You must include the container registry path and version of the image, such as `REGISTRY_PATH/hello-app:1.0`.
  3. Containers also require additional permissions to access GPUs. For each container that requests GPUs, add the following permissions to your container spec:
         
         ...
         securityContext:
          seLinuxOptions:
            type: unconfined_t
         ...
         

  4. Apply your container manifest file:
         
         kubectl apply -f CONTAINER_MANIFEST_FILE \
             -n NAMESPACE \
             --kubeconfig CLUSTER_KUBECONFIG
         

Replace the following:

     * `CONTAINER_MANIFEST_FILE`: the YAML file for your container workload custom resource.
     * `NAMESPACE`: the project namespace in which to deploy the container workloads.
     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the bare metal Kubernetes cluster to which you're deploying container workloads.
  5. Verify that your pods are running and are using the GPUs:
         
         kubectl get pods -A | grep CONTAINER_NAME \
             -n NAMESPACE \
             --kubeconfig CLUSTER_KUBECONFIG
         

The relevant output is similar to the following snippet:
         
         Port:           80/TCP
         Host Port:      0/TCP
         State:          Running
         Ready:          True
         Restart Count:  0
         Limits:
           nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE:  1
         Requests:
           nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE:  1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
