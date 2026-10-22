---
url: https://docs.cloud.google.com/code/docs/shell/minikube-local-development/
title: Use minikube for local development in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:21.736506+00:00
---

# Use minikube for local development in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/minikube-local-development/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Use minikube for local development in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code automatically installs and manages minikube. If you opted out of dependency management, add the minikube binary to your `PATH`.

## Before you begin

  * Install [Git](https://git-scm.com/downloads) so that Cloud Code can perform Git operations, like cloning a sample.



## Create an application from a template

Cloud Code comes with a collection of [code sample](https://github.com/GoogleCloudPlatform/cloud-code-samples#readme) templates to get you started quickly. To create a Kubernetes application using an existing sample, follow these steps:

  1. Launch the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: New Application**.
  2. Select **Kubernetes application** for the type of sample.
  3. Select a sample based on the language you'd like to use from the available options: NodeJS, Go, Python, Java.
  4. Choose a preferred application location on your local machine and then click **Create new application** to save.

Cloud Code clones the sample you chose and opens your new project for use.




## Use your own application

For steps to use an existing project, see [use Cloud Code with an existing Kubernetes application](https://docs.cloud.google.com/code/docs/shell/use-existing-app).

**Note:** For developing and testing an app, create and run the application on a non-production cluster.   
For changes that will be rolled out to production, use an [automated CI/CD workflow](https://docs.cloud.google.com/docs/ci-cd). 

## Set your Kubernetes context

Before running your application, ensure you're set up to deploy your app to your preferred Kubernetes context. You can specify this in your configuration.

## Configuration

When using the **Cloud Code: Develop on Kubernetes** run configuration, you can customize your deployment by configuring available settings.

To add or edit configurations, go to **Run** > **Open Configurations** and then edit or add configurations. 

## Create and deploy to a minikube cluster

### Start a minikube cluster

Cloud Code automatically installs and manages minikube. If you opted out of dependency management, add the minikube binary to your `PATH`.

  1. Launch the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Cloud Code: Control minikube** command.
  2. Click **minikube** for **Choose a Minikube cluster (profile) to control** and then click **Start**.



### Run on minikube

  1. Launch the Command Palette and run **Cloud Code: Run on Kubernetes**.
  2. Click **Yes** for **Use current context (minikube) to run the app?**
  3. Cloud Code runs your app in a your minikube cluster. If prompted, authorize Cloud Shell to use your credentials to make a Google Cloud API call.

View the deployment details in the **Development sessions** section of **Cloud Code**.

  4. View the URLs by clicking **Portfoward URLs** in the **Development sessions** section, then click the URL link to open your browser with your running application.




### Open an interactive terminal to a container

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Development Sessions** section.
  2. Expand **Deployed Resources** , then expand **Pods**.
  3. Right-click a container and then click **Get Terminal**.



### Pause or stop a minikube cluster

  1. Launch the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Cloud Code: Control minikube** command.
  2. After the **Choose a Minikube cluster (profile) to control** option populates, click **minikube** and then click **Stop** or **Pause**.



## Create and add a cluster from another cloud provider

If you're using an on-premises cluster or a cluster from another provider such as Azure or AWS, use the provider's tools to create the cluster and add it to your KubeConfig.

## Work with other local clusters

In addition to [minikube](https://minikube.sigs.k8s.io/docs/start/), you can work with Cloud Code if you're using Docker Desktop (for [Mac](https://docs.docker.com/docker-for-mac/) or [Windows](https://docs.docker.com/docker-for-windows/)).

To get Cloud Code working with a local cluster, make sure that your default configuration (for example, `~/.kube/config`) contains your local cluster. This cluster must be set as the current context.

For example, if you were using a local cluster, `docker-for-desktop`, with Docker Desktop, set your preferred cluster by running the following command:
    
    
    kubectl config use-context docker-for-desktop
    

## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/shell/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/shell/debug)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
