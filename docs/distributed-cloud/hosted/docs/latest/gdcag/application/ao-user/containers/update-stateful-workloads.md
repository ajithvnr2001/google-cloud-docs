---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/update-stateful-workloads/
title: Update stateful workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:23:57.374761+00:00
---

# Update stateful workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/update-stateful-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Update stateful workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to update existing stateful workloads running in a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster. As your application evolves based on resource usage and configuration optimizations, you must update your underlying pod specification in the Kubernetes cluster to reflect those workload changes. For more information on planning updates for stateful workloads, see the Kubernetes documentation for [Update strategies](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#update-strategies).

This document is for developers within the application operator group, who are responsible for updating application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to update stateful workloads. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

To create, delete, edit, or view workloads in a shared cluster, ask your Project IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

#### Standard cluster roles

To create, delete, edit, or view workloads in a standard cluster, ask your Project IAM Admin to grant you the **Cluster Developer** (`cluster-developer`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.




## Update a `StatefulSet` resource

To update the `StatefulSet`, apply a new or updated manifest file. This is useful for making various changes to your `StatefulSet` when scaling or for specifying a new version of your application.

To update a `StatefulSet` object, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        apply -f STATEFULSET_FILE
    

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the stateful workloads.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `STATEFULSET_FILE`: the name of the updated `StatefulSet` manifest file.




The `kubectl apply` command applies a manifest file to a resource. If the specified resource does not exist, it is created by the command.

## Inspect a `StatefulSet` resource update rollout

You can view detailed information regarding the update rollout status and history of a `StatefulSet` object. You can also undo a rollout of a `StatefulSet` object.

### Inspect the rollout

To inspect the rollout of the `StatefulSet` resource, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout status statefulset STATEFULSET_NAME
    

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the stateful workloads.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `STATEFULSET_NAME`: the name of the updated `StatefulSet` object.




### Get the rollout history

To see the `StatefulSet` resource's rollout history, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout history statefulset STATEFULSET_NAME
    

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the stateful workloads.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `STATEFULSET_NAME`: the name of the updated `StatefulSet` object.




### Undo a rollout

To undo a rollout, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout undo statefulset STATEFULSET_NAME
    

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the stateful workloads.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object.




## What's next

  * [Upgrade a cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/upgrade-cluster)
  * [Isolate container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/isolate-container-workloads)
  * [Maintain Kubernetes clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
