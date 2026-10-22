---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/gpu/
title: Deploy GPU container workloads \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:10.002902+00:00
---

# Deploy GPU container workloads  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Deploy GPU container workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy GPU container workloads on the Google Distributed Cloud (GDC) Sandbox AI Optimized SKU.

## Deploy GPU container workloads

The GDC Sandbox AI Optimized SKU includes four NVIDIA H100 80GB HBM3 GPUs within the org-infra cluster. These GPUs are accessible using the resource name `nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3`. This section describes how to update a container configuration to use these GPUS.

The GPUs in GDC Sandbox AI Optimized SKU are associated with a pre-configured project, "**sandbox-gpu-project** " (present only in GDC Sandbox AI Optimized SKU instances). You must deploy your container using this project inside the `org-1-infra` cluster to make use of the GPUs.

**Note:** For GPU workloads, there is no direct access to HaaS (Harbor as a Service). You must be able to fetch images from the Google Cloud Artifact Registry or internet.

### Before you begin

  * To run commands against the org infrastructure cluster, make sure that you have the kubeconfig of the `org-1-infra` cluster, as described in [Work with clusters](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters#org-infra-cluster):

    * Configure and authenticate with the `gdcloud` command line, and
    * generate the kubeconfig file for the org infrastructure cluster, and assign its path to the environment variable `KUBECONFIG`.
  * To run the workloads, you must have the `sandbox-gpu-admin` role assigned. By default, the role is assigned to the `platform-admin` user. You can assign the role to other users by signing in as the `platform-admin` and running the following command:
        
        kubectl --kubeconfig ${KUBECONFIG} create rolebinding ${NAME} --role=sandbox-gpu-admin \
        --user=${USER} --namespace=sandbox-gpu-project
        

  * To allow network traffic to your container, you must have a project network policy. For more information, see [Create a network policy](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/container-workloads#create_a_network_policy).


**Warning:** The GPU hosts maintain architectural isolation from the rest of the ecosystem. Data plane services (such as DBS and Object Storage) and general-purpose VMs are explicitly excluded from accessing the resources where the GPU workloads run.

### Configure a container to use GPU resources

  1. Add the `.containers.resources.requests` and `.containers.resources.limits` fields to your container specification to request GPUs for the workload. All containers within the sandbox-gpu-project can request up to a total of 4 GPUs across the entire project. The following example requests one GPU as part of the container specification.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-deployment
           namespace: sandbox-gpu-project
           labels:
             app: nginx
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: nginx
           template:
             metadata:
               labels:
                 app: nginx
             spec:
               containers:
               - name: nginx
                 image: nginx:latest
                 resources:
                   requests:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1
                   limits:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1
         


**Note:** If you are using GDC Sandbox AI Optimized with A100 GPUs, the GPUs are accessible using the resource name `nvidia.com/gpu-pod-NVIDIA_A100_SXM4_80GB`. Substitute this resource name for `nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3` in the configuration file.

  1. Containers also require additional permissions to access GPUs. For each container that requests GPUs, add a `.containers.securityContext` granting `securityContext.seLinuxOptions` of type `unconfined_t` to the container.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-deployment
           namespace: sandbox-gpu-project
           labels:
             app: nginx
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: nginx
           template:
             metadata:
               labels:
                 app: nginx
             spec:
               containers:
               - name: nginx
                 image: nginx:latest
                 resources:
                   requests:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1
                   limits:
                     nvidia.com/gpu-pod-NVIDIA_H100_80GB_HBM3: 1
                 securityContext:
                   seLinuxOptions:
                     type: unconfined_t
         

  2. Apply your container manifest file:
         
         kubectl apply -f ${CONTAINER_MANIFEST_FILE_PATH} \
             -n sandbox-gpu-project \
             --kubeconfig ${KUBECONFIG}
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
