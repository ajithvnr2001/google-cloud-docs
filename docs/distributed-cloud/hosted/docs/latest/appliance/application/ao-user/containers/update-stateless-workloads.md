---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/update-stateless-workloads/
title: Update stateless workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:43.025034+00:00
---

# Update stateless workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/update-stateless-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Update stateless workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to update existing stateless workloads running in a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. As your application evolves based on resource usage and configuration optimizations, you must update your underlying pod specification in the Kubernetes cluster to reflect those workload changes.

This page is for developers within the application operator group, who are responsible for updating application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view stateless workloads in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Update the deployment

To update a `Deployment` object, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        apply -f DEPLOYMENT_FILE
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the deployment.

  * `NAMESPACE`: the project namespace.

  * `DEPLOYMENT_FILE`: the name of the `Deployment` manifest file to update.




The `kubectl apply` command applies a manifest file to a resource. If the specified resource does not exist, it is created by the command.

There are also several other ways to update resources within your deployment.

### Update a container image

To change the image of a `Deployment` object, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        set image deployment DEPLOYMENT_NAME \
        IMAGE=IMAGE:TAG
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the deployment.

  * `NAMESPACE`: the project namespace.

  * `DEPLOYMENT_NAME`: the name of the `Deployment` object containing the image.

  * `IMAGE`: the name of the container image.

  * `TAG`: the tag to update for the container image.




Updating the image of a deployment is useful to change selector fields or resources, such as requests or limits.

For example, to update a `Deployment` object named `nginx` to use version `1.9.1`, run:
    
    
    kubectl --kubeconfig /tmp/kubeconfig.yaml -n my-namespace \
        set image deployment nginx nginx=nginx:1.9.1
    

### Roll back an update

If you want to roll back an update, such as when your deployment becomes unstable, use the `kubectl` CLI. A `Deployment` object's rollout history is preserved in the system so you can roll back at any time.

To roll back an in-progress or completed update to its previous revision, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        -n NAMESPACE \
        rollout undo deployment DEPLOYMENT_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the deployment.

  * `NAMESPACE`: the project namespace.

  * `DEPLOYMENT_NAME`: the name of the `Deployment` object to roll back.




To roll back to a specific revision, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG \
        -n NAMESPACE \
        rollout undo deployment DEPLOYMENT_NAME \
        --to-revision=REVISION_NUMBER
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the deployment.

  * `NAMESPACE`: the project namespace.

  * `DEPLOYMENT_NAME`: the name of the `Deployment` object to roll back.

  * `REVISION_NUMBER`: the integer that defines the revision to roll back to, such as `3`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
