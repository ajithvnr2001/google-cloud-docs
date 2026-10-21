---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/deploy-gpu-container-workloads/
title: Manage GPU container workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:34:29.043936+00:00
---

# Manage GPU container workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/deploy-gpu-container-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage GPU container workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

You can enable and manage graphics processing unit (GPU) resources on your containers. For example, you might prefer running artificial intelligence (AI) and machine learning (ML) notebooks in a GPU environment. To run GPU container workloads, you must have a Kubernetes cluster that supports GPU devices. GPU support is enabled by default for Kubernetes clusters that have GPU machines provisioned for them.

This document is for application developers within the application operator group who are responsible for creating application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to deploy GPUs to your containers. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

To verify GPU-supported node pools and deploy GPU workloads in a shared cluster, request the following roles based on the task to perform:

  * **User Cluster Admin** (`user-cluster-admin`): create, delete, edit, or view the resources of a shared cluster hosted on the management API server. This role lets you check GPUs in the shared cluster, and isn't bound to your project namespace.
  * **Namespace Admin** (`namespace-admin`): create, delete, edit, or view the resources of a shared cluster hosted in the project. This role lets you deploy GPU workloads to a standard cluster, and is bound to your project namespace.



#### Standard cluster roles

To verify GPU-supported node pools and deploy GPU workloads to a standard cluster, ask your Project IAM Admin to grant you the following roles:

  * **Standard Cluster Admin** (`standard-cluster-admin`): create, delete, edit, or view the resources of a standard cluster hosted on the management API server. This role lets you check GPUs in the shared cluster, and is bound to your project namespace.
  * **Cluster Developer** (`cluster-developer`): create, delete, edit, or view a standard cluster. This role lets you deploy GPU workloads to a standard cluster by providing access to the data plane APIs hosted within the standard cluster. This role is bound to your project namespace.



### Prepare your environment

To configure a container to use GPU resources, make sure you have the following resources:

  * A Kubernetes cluster with a GPU machine class. For more information, see the [supported GPU cards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster#supported-gpu-cards) section.

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the zonal management API server that hosts your Kubernetes cluster. Use this path to replace `MANAGEMENT_API_SERVER` in these instructions.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in) the kubeconfig file for the org infrastructure cluster in the zone intended to host your GPUs.




## Configure a container to use GPU resources

To use these GPUs in a container, complete the following steps:

  1. Verify your Kubernetes cluster has node pools that support GPUs:
         
         kubectl describe clusters.cluster.gdc.goog/KUBERNETES_CLUSTER_NAME \
             -n KUBERNETES_CLUSTER_NAMESPACE \
             --kubeconfig MANAGEMENT_API_SERVER
         

Replace the following:

     * `KUBERNETES_CLUSTER_NAME`: the name of the cluster.
     * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path where the Kubernetes cluster is hosted. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

The relevant output is similar to the following snippet:
    
    # Several lines of code are omitted here.
    spec:
      nodePools:
      - machineTypeName: a2-ultragpu-1g-gdc
        nodeCount: 2
    # Several lines of code are omitted here.
    

For a full list of supported GPU machine types and Multi-Instance GPU (MIG) profiles, see [Cluster node machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines).

  2. Add the `.containers.resources.requests` and `.containers.resources.limits` fields to your container spec. Each resource name is different depending on your machine class. Check your GPU resource allocation to find your GPU resource names.

For example, the following container spec requests three partitions of a GPU from an `a2-ultragpu-1g-gdc` node:
         
         # Several lines of code are omitted here.
          containers:
          - name: my-container
            image: "my-image"
            resources:
              requests:
                nvidia.com/mig-1g.10gb-NVIDIA_A100_80GB_PCIE: 3
              limits:
                nvidia.com/mig-1g.10gb-NVIDIA_A100_80GB_PCIE: 3
          # Several lines of code are omitted here.
         

**Note:** You can request a maximum of seven GPU partitions per pod.
  3. Containers also require additional permissions to access GPUs. For each container that requests GPUs, add the following permissions to your container spec:
         
         # Several lines of code are omitted here.
         securityContext:
          seLinuxOptions:
            type: unconfined_t
         # Several lines of code are omitted here.
         

  4. Apply your container manifest file:
         
         kubectl apply -f CONTAINER_MANIFEST_FILE \
             -n KUBERNETES_CLUSTER_NAMESPACE \
             --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
         

Replace the following:

     * `CONTAINER_MANIFEST_FILE`: the YAML manifest file for your container workload.
     * `KUBERNETES_CLUSTER_NAMESPACE`: the namespace of the cluster. For shared clusters, use the `platform` namespace. For standard clusters, use the project namespace of the cluster.
     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path of the cluster.



## Check GPU resource allocation

  * To check your GPU resource allocation, use the following command:
        
        kubectl describe nodes NODE_NAME --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
        

Replace the following:

    * `NODE_NAME`: the node managing the GPUs you want to inspect.
    * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path of the cluster.

The relevant output is similar to the following snippet:
    
    # Several lines of code are omitted here.
    Capacity:
      nvidia.com/mig-1g.10gb-NVIDIA_A100_80GB_PCIE: 7
    Allocatable:
      nvidia.com/mig-1g.10gb-NVIDIA_A100_80GB_PCIE: 7
    # Several lines of code are omitted here.
    




Note the resource names for your GPUs; you must specify them when configuring a container to use GPU resources.

## What's next

  * [Kubernetes clusters in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters)
  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
