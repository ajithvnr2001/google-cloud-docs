---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateless-workloads/
title: Create stateless workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:02.543369+00:00
---

# Create stateless workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateless-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create stateless workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create and manage stateless workloads within a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. Stateless workloads let you scale your application deployment based on workload demands, all without having to manage persistent storage in a Kubernetes cluster to store data or application state. This page helps you get started so you can efficiently optimize and adjust your application's availability.

This page is for developers within the application operator group, who are responsible for creating application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view stateless workloads in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Create a deployment

You create a deployment by writing a `Deployment` manifest and running `kubectl apply` to create the resource. This method also retains updates made to live resources without merging the changes back into the manifest files.

To create a `Deployment` from its manifest file, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: DEPLOYMENT_NAME
    spec:
      replicas: NUMBER_OF_REPLICAS
      selector:
        matchLabels:
          run: APP_NAME
      template:
        metadata:
          labels: # The labels given to each pod in the deployment, which are used
                  # to manage all pods in the deployment.
            run: APP_NAME
        spec: # The pod specification, which defines how each pod runs in the deployment.
          containers:
          - name: CONTAINER_NAME
            image: CONTAINER_IMAGE
            resources:
              requests:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
              limits:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
    EOF
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster to which you're deploying container workloads.

  * `NAMESPACE`: the project namespace in which to deploy the container workloads.

  * `DEPLOYMENT_NAME`: the name of the `Deployment` object.

  * `APP_NAME`: the name of the application to run within the deployment.

  * `NUMBER_OF_REPLICAS`: the number of replicated `Pod` objects that the deployment manages.

  * `CONTAINER_NAME`: the name of the container.

  * `CONTAINER_IMAGE`: the name of the container image. You must include the container registry path and version of the image, such as `REGISTRY_PATH/hello-app:1.0`. For more information about setting the container registry path, see the [Managed Harbor Service overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/mhs-overview).


**Note:** You can also use `kubectl apply -f DIRECTORY` to create new objects defined by manifest files stored in a directory.

For example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          run: my-app
      template:
        metadata:
          labels:
            run: my-app
        spec:
          containers:
          - name: hello-app
            image: REGISTRY_PATH/hello-app:1.0
            resources:
              requests:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
              limits:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
    

If you're deploying GPU workloads to your containers, see [Manage GPU container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/deploy-gpu-container-workloads) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
