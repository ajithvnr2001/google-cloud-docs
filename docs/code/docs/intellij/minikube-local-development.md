---
url: https://docs.cloud.google.com/code/docs/intellij/minikube-local-development/
title: Use minikube for local development in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:21:34.415677+00:00
---

# Use minikube for local development in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/minikube-local-development/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Use minikube for local development in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code automatically installs and manages minikube. If you opted out of dependency management, add the minikube binary to your `PATH`.

## Before you begin

  1. Install [Git](https://git-scm.com/downloads) so that Cloud Code can perform Git operations, like cloning a sample.
  2. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/intellij/install) if you haven't already.



## Create an application from a template

Cloud Code comes with a collection of [code sample](https://github.com/GoogleCloudPlatform/cloud-code-samples#readme) templates to get you started quickly. To create a Kubernetes application using an existing sample, follow these steps:

  1. Open **File** > **New Project**.
  2. Select **Cloud Code: Kubernetes**.
  3. Select a template from the list of starter applications. 
  4. Pick a name for your project.

Once you click **Finish** , Cloud Code will clone your chosen template and open your newly created project for use.

For **Java** templates, you'll be prompted to import Maven projects to sync your pom.xml. Click **Add as Maven project**. Additionally, import necessary Maven projects by clicking **Import Changes**.

  5. Kubernetes run and development IDE run targets for the project are automatically created and ready to run.

Optional: Alternatively, you can manually create run targets:

     1. Select the **Run Configuration** drop down, and click **Edit Configurations**.
     2. Click **\+ Add New Configuration** to add a new run configuration.
     3. Navigate to **Cloud Code: Kubernetes**
     4. Enter a name for your new configuration (default is "Unnamed").
     5. Click **OK** to create your run target.
**Note:** If you're logged into Google Cloud in your IDE and you have a default project defined, Cloud Code uses your default container image repository. To specify a different container image, follow [Configuring container image settings](https://docs.cloud.google.com/code/docs/intellij/configuring-container-image-settings#specifying_where_container_images_are_stored).



## Use your own application

For steps to use an existing project, see [use Cloud Code with an existing Kubernetes application](https://docs.cloud.google.com/code/docs/intellij/use-existing-app).

**Note:** For developing and testing an app, create and run the application on a non-production cluster.   
For changes that will be rolled out to production, use an [automated CI/CD workflow](https://docs.cloud.google.com/docs/ci-cd). 

## Set your Kubernetes context

Before running your application, ensure you're set up to deploy your app to your preferred Kubernetes context. You can specify this in your configuration.

If you'd like to switch your current context, you can do so with the [Kubernetes Explorer](https://docs.cloud.google.com/code/docs/intellij/use-kubernetes-explorer#clusters), accessible either from its sidebar panel on the right or using **Tools** > **Cloud Code** > **Kubernetes** > **View Cluster Explorer**.

To optimize your development loop by quickly picking up file changes of a certain type without having to perform an image rebuild, you can [enable file syncing and hot reloading](https://docs.cloud.google.com/code/docs/intellij/yaml-editing#enabling_skaffold_file_sync_and_hot_reloading). 

## Configuration

When using the **Cloud Code: Develop on Kubernetes** run configuration, you can customize your deployment by configuring available settings.

To add or edit configurations, go to **Run** > **Edit Configurations**. 

## Create and deploy to a minikube cluster

### Edit run configuration

  1. Click the configuration drop down in the top taskbar and then click **Edit Configurations**.

The **Develop on Kubernetes** configuration watches for changes, then rebuilds and reruns your app. You can customize your deployment by making changes to this run configuration or by creating a new Cloud Code: Kubernetes run configuration.

  2. In the **Run/Debug configurations dialog** for **Run** > **Deployment** , select **Deploy locally to a minikube cluster**.

  3. Click **OK** to save your configuration.




### Run on minikube

  1. Select **Develop on Kubernetes** from the configuration dropdown and click the **Run** icon.
  2. Cloud Code runs your app in a local minikube cluster.
  3. View the build process in the output window.

When the deployment is successful, you're notified that new service URLs are available

  4. Click the Service URLs tab to view the URLs, then click the URL link to open your browser with your running application

  5. To stop the application, click the stop icon next to the configuration dropdown.




## Create and add a cluster from another cloud provider

If you're using an on-premises cluster or a cluster from another provider such as Azure or AWS, use the provider's tools to create the cluster and add it to your KubeConfig.

## Work with other local clusters

In addition to [minikube](https://minikube.sigs.k8s.io/docs/start/), you can work with Cloud Code if you're using Docker Desktop (for [Mac](https://docs.docker.com/docker-for-mac/) or [Windows](https://docs.docker.com/docker-for-windows/)).

To get Cloud Code working with a local cluster, make sure that your default configuration (for example, `~/.kube/config`) contains your local cluster. This cluster must be set as the current context.

For example, if you were using a local cluster, `docker-for-desktop`, with Docker Desktop, set your preferred cluster by running the following command:
    
    
    kubectl config use-context docker-for-desktop
    

## What's next

  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/debug)



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
