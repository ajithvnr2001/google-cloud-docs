---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/update-stateful-workloads/
title: Update stateful workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:51.672744+00:00
---

# Update stateful workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/update-stateful-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Update stateful workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to update existing stateful workloads running in a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. As your application evolves based on resource usage and configuration optimizations, you must update your underlying pod specification in the Kubernetes cluster to reflect those workload changes. For more information on planning updates for stateful workloads, see the Kubernetes documentation for [Update strategies](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#update-strategies).

This page is for developers within the application operator group, who are responsible for updating application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view stateful workloads in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Update a `StatefulSet` resource

To update the `StatefulSet`, apply a new or updated manifest file. This is useful for making various changes to your `StatefulSet` when scaling or for specifying a new version of your application.

To update a `StatefulSet` object, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        apply -f STATEFULSET_FILE
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the stateful workloads.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_FILE`: the name of the updated `StatefulSet` manifest file.




The `kubectl apply` command applies a manifest file to a resource. If the specified resource does not exist, it is created by the command.

## Inspect a `StatefulSet` resource update rollout

You can view detailed information regarding the update rollout status and history of a `StatefulSet` object. You can also undo a rollout of a `StatefulSet` object.

### Inspect the rollout

To inspect the rollout of the `StatefulSet` resource, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout status statefulset STATEFULSET_NAME
    

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the stateful workloads.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the updated `StatefulSet` object.




### Get the rollout history

To see the `StatefulSet` resource's rollout history, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout history statefulset STATEFULSET_NAME
    

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the stateful workloads.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the updated `StatefulSet` object.




### Undo a rollout

To undo a rollout, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        rollout undo statefulset STATEFULSET_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the stateful workloads.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
