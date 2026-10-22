---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/scale-stateless-workloads/
title: Scale stateless workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:59.564022+00:00
---

# Scale stateless workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/scale-stateless-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Scale stateless workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document describes how to scale existing stateless workloads running in a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster. You must scale the pods running in your stateless workloads as your container workload requirements evolve.

This document is for developers within the application operator group who are responsible for managing application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to scale stateless workloads. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

To create, delete, edit, or view workloads in a shared cluster, ask your Project IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

#### Standard cluster roles

To create, delete, edit, or view workloads in a standard cluster, ask your Project IAM Admin to grant you the **Cluster Developer** (`cluster-developer`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.




## Scale a deployment

Use the scaling functionality of Kubernetes to appropriately scale the amount of pods running in your deployment.

### Autoscale the pods of a deployment

Kubernetes offers autoscaling to remove the need of manually updating your deployment when demand evolves. Complete the following steps to autoscale the pods of your deployment:

  1. To ensure the horizontal pod autoscaler can appropriately measure the CPU percentage, set the [CPU resource request](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#support-for-resource-metrics) on your deployment.

  2. Set the horizontal pod autoscaler in your deployment:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG \
             -n NAMESPACE \
             autoscale deployment DEPLOYMENT_NAME \
             --cpu-percent=CPU_PERCENT \
             --min=MIN_NUMBER_REPLICAS \
             --max=MAX_NUMBER_REPLICAS
         

Replace the following:

     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

     * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

     * `DEPLOYMENT_NAME`: the name of the deployment to autoscale.

     * `CPU_PERCENT`: the target average CPU utilization to request, represented as a percentage, over all the pods.

     * `MIN_NUMBER_REPLICAS`: the lower limit for the number of pods the autoscaler can provision.

     * `MAX_NUMBER_REPLICAS`: the upper limit for the number of pods the autoscaler can provision.

  3. Check the current status of the horizontal pod autoscaler:
         
         kubectl get hpa
         

The output is similar to the following:
         
         NAME              REFERENCE                          TARGET    MINPODS   MAXPODS   REPLICAS   AGE
         DEPLOYMENT_NAME   Deployment/DEPLOYMENT_NAME/scale   0% / 50%  1         10        1          18s
         




### Manually scale the pods of a deployment

If you prefer to manually scale a deployment, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG \
        -n NAMESPACE \
        scale deployment DEPLOYMENT_NAME \
        --replicas NUMBER_OF_REPLICAS
    

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `DEPLOYMENT_NAME`: the name of the deployment in which to autoscale.

  * `DEPLOYMENT_NAME`: the number of replicated `Pod` objects in the deployment.




## What's next

  * [Inspect stateless workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/inspect-stateless-workloads)
  * [Update stateless workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/update-stateless-workloads)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
