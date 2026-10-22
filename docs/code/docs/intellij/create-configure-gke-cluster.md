---
url: https://docs.cloud.google.com/code/docs/intellij/create-configure-gke-cluster/
title: Configure a GKE cluster in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:09.109595+00:00
---

# Configure a GKE cluster in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/create-configure-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Configure a GKE cluster in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code, you can create a Kubernetes cluster with Google Kubernetes Engine (GKE).

**Note:** For developing and testing an app, create and run on a non-production cluster. For changes that will be rolled out to production, use an [automated CI/CD workflow](https://docs.cloud.google.com/docs/ci-cd).

## Create a GKE cluster and add it to your KubeConfig

Cloud Code opens the Google Cloud console so that you can quickly create a cluster:

  1. To open the Kubernetes Explorer, click ![Kubernetes explorer button in IntelliJ](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-explorer-button.png)**Kubernetes Explorer** or navigate to **Tools** > **Cloud Code** > **Kubernetes** > **View Cluster Explorer**.

  2. In the header of the Kubernetes Explorer pane, click **\+ Connect to a GKE Cluster**.

  3. Choose **Create a new GKE Cluster** or **Create a new GKE Autopilot cluster**. For more information on which mode to choose, see [Comparing Autopilot and Standard modes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#comparison).

  4. If prompted, click **Open** to permit Cloud Code to open the Google Cloud console.

  5. In Google Cloud console, choose any configuration options that you want to customize and then click **Create**.

  6. After the cluster is created, in Cloud Code, in the Kubernetes explorer, click the **Refresh** icon.

  7. After the name of your new cluster appears in the list, click the cluster name. Your new cluster is added to the configuration and set as the default context.




## Work with an existing GKE cluster

If you have an existing Standard or Autopilot GKE cluster, you can set it as your active cluster and work with it using Cloud Code.

  1. In the header of the Kubernetes Explorer pane, click **\+ Add GKE Cluster**.
  2. Click **Google Kubernetes Engine**.
  3. Click your cluster name. Your cluster is added to the KubeConfig.



## Set a cluster as the default context

The active cluster is the cluster that your application is deployed to by default.

In the Kubernetes Explorer, right-click a cluster and then click **Set as Current Context**.

## Run an application on GKE

To run or debug an application on GKE, you'll need to define the container image repository for your project.

To learn more, read about [storing your container images](https://docs.cloud.google.com/code/docs/intellij/configuring-container-image-settings). 

## Remove a cluster from your KubeConfig

After you remove a cluster from your KubeConfig, the cluster is not available to deploy to.

In the Kubernetes Explorer, right-click a cluster and then click **Remove From KubeConfig**.

## Create and add a cluster from another cloud provider

If you're using an on-premises cluster or a cluster from another provider such as Azure or AWS, use the provider's tools to create the cluster and add it to your KubeConfig.

## What's next

  * [Organize your cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).
  * Learn how to add, delete or switch between your [kubeconfig files in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/kubeconfigs).
  * [Develop and debug parts of a microservice application](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#develop-microservices).
  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/debug).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
