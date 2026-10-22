---
url: https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster/
title: Create and configure a GKE cluster in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:35.768113+00:00
---

# Create and configure a GKE cluster in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Create and configure a GKE cluster in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code, you can create a Kubernetes cluster with Google Kubernetes Engine (GKE).

**Note:** For developing and testing an app, create and run on a non-production cluster. For changes that will be rolled out to production, use an [automated CI/CD workflow](https://docs.cloud.google.com/docs/ci-cd).

## Create a GKE cluster and add it to your KubeConfig

To create a cluster:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Click add **Add a Cluster to the KubeConfig**.
  3. Select **Google Kubernetes Engine** and then select **Yes** to enable the Google Kubernetes Engine API in your project.
  4. Choose **Standard** or **Autopilot**. For more information, see [Comparing Autopilot and Standard modes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#comparison).
  5. If prompted, click **Open** to permit Cloud Code to open the Google Cloud console.
  6. In Google Cloud console, choose any configuration options that you want to customize and then click **Create**.
  7. After the cluster is created, in Cloud Code, click the **Refresh** icon.
  8. After the name of your new cluster appears in the list, click the cluster name. Your new cluster is added to your kubeconfig and set as the default context.



**Tip:** To create a Kubernetes cluster using the command palette, launch the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Cloud Code: Create GKE cluster** command.

## Work with an existing GKE cluster

If you have an existing Standard or Autopilot GKE cluster, you can set it as your active cluster and work with it using Cloud Code.

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Click add **Add a Cluster to the KubeConfig**.
  3. Click **Google Kubernetes Engine**.
  4. Click your cluster name. Your cluster is added to the KubeConfig.



## Set a cluster as the default context

The active cluster is the cluster that your application is deployed to by default.

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Right-click a cluster and then click **Set as Active Cluster**.



## Run an application on GKE

To run or debug an application on GKE, you'll need to define the container image repository for your project.

When attempting to debug, you may be prompted to [authenticate your credentials to run and debug an application locally](https://docs.cloud.google.com/code/docs/vscode/install#authenticate_credentials_for_debugging_applications_locally).

To learn more, see [get started with Cloud Code for Kubernetes](https://docs.cloud.google.com/code/docs/vscode/get-started-k8s#run_your_application)

## Remove a cluster from your KubeConfig

After you remove a cluster from your KubeConfig, the cluster is not available to deploy to.

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Right-click a cluster and then click **Remove Context Under Cluster**.



## Open an interactive terminal to a container

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Expand your minikube cluster, expand **Pods** , and then expand **Containers**.
  3. Right-click a container and then click **Get Terminal**.



## Open an external IP address

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Expand your minikube cluster and then expand **Services**.
  3. Expand **External IPs** , right-click an IP address, and then click **Open Address**.
  4. Click **Open**.



## Create and add a cluster from another cloud provider

If you're using an on-premises cluster or a cluster from another provider such as Azure or AWS, use the provider's tools to create the cluster and add it to your KubeConfig.

## What's next

  * [Organize your cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).
  * Learn how to add, delete or switch between your [kubeconfig files in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/kubeconfigs).
  * [Develop and debug parts of a microservice application](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#develop-microservices).
  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/debug).



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
