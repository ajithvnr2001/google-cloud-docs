---
url: https://docs.cloud.google.com/code/docs/intellij/quickstart-k8s/
title: Quickstart: Deploy a Kubernetes app with Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:47.824174+00:00
---

# Quickstart: Deploy a Kubernetes app with Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/quickstart-k8s/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Kubernetes app with Cloud Code for IntelliJ

Learn how to use Cloud Code for IntelliJ to deploy your first Kubernetes application.

In this quickstart, you'll set up a new Kubernetes application using a starter Hello World template, run your app on a cluster, configure continuous rebuilding to iteratively develop your app, debug your running code, and view streaming logs from your live application.

While we recommend using Google Cloud for this guide, you can instead use Cloud Code with a local cluster using tools such as [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube) and [Docker Desktop](https://www.docker.com/products/docker-desktop). However, features like live GKE cluster creation and integrated continuous delivery are best experienced with a Google Cloud project.

## Before you begin

Whether you choose to use a local or cloud-hosted cluster, to complete this quickstart, follow these steps:

  1. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is required to copy code samples to your machine.
  2. Install [Docker](https://docs.docker.com/get-docker/). Docker is required to build the sample code. Ensure your local user account is able to build containers.
  3. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/intellij/install#installing) if you haven't already.



To complete this quickstart using Google Cloud, follow these steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)




### Required roles

To get the permissions that you need to complete this quickstart using Google Cloud, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an application

Cloud Code comes with a collection of [code sample](https://github.com/GoogleCloudPlatform/cloud-code-samples#readme) templates to get you started. To create a new application using an existing sample:

  1. In your IDE, open **File** > **New Project** and select **Cloud Code: Kubernetes**.

  2. Select a **Hello World** template from the list of starter applications. ![List of templates available: Python, Go, NodeJS, Java hello world and guestbook applications](https://docs.cloud.google.com/static/code/docs/intellij/images/cloud-code-samples.png)

  3. Pick a name for your project.

After you click **Finish** , Cloud Code clones your chosen template and opens your newly created project for use.

For **Java** templates, you're prompted to import required Maven projects to sync your pom.xml. Click **Add as Maven project** and then click **Import Changes**.




## Choose a cluster

In order to develop your application, you'll need an associated Kubernetes cluster hosted either locally with minikube or using a cloud platform, like a Google Kubernetes Engine cluster.

### Local cluster

If you don't already have a cluster to use for this quickstart, you can choose to run your application with a Cloud Code-managed local minikube cluster. Cloud Code starts a minikube cluster to run your application and stops the cluster when deployment stops. If a minikube cluster is already running, Cloud Code reuses the existing minikube cluster for deployment.

You can choose to use this Cloud Code-managed minikube cluster in the next step, developing your application, by setting it as your deployment preference.

### Cloud platform-based cluster

If you already have a cluster configured to work with Kubernetes tools, such as kubectl, that you can use for this quickstart, Cloud Code deploys to it automatically. You can move on to developing your application where you can confirm your preferred cluster is set as your current context.

If you don't, you can create one using your cloud platform-specific instructions. For GKE, follow the [Creating a cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster) guide.

## Develop your application

To initiate development of your application on Kubernetes:

  1. If you're running on a cluster hosted on a cloud platform, ensure you have [defined where your container images are stored](https://docs.cloud.google.com/code/docs/intellij/configuring-container-image-settings#specifying_where_container_images_are_stored) for **Develop on Kubernetes**.

If you're logged into Google Cloud in your IDE and you have a default project defined, Cloud Code automatically uses your default container image repository (gcr.io/{project_id} where {project_id} references your default project).

  2. Ensure your preferred Kubernetes context is set. This can be specified in your Develop on Kubernetes configuration (accessible through **Run** > **Edit Configurations** > **Develop on Kubernetes**), on the Run tab and in the Deployment preferences section.

You can choose to deploy to a current context (default), locally to a minikube cluster, or to another available context.

By default, your Kubernetes application will run in [On-demand mode](https://docs.cloud.google.com/code/docs/intellij/watch-modes) with **On demand** selected. If preferred, you can select the **On file save** option instead.

  3. Choose the **Develop on Kubernetes** run target from the Run/Debug configuration selector in the Navigation bar.

![Kubernetes deployment run configurations](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-skaffold-develop-targets.png)

This ensures any code changes to be automatically built, pushed, and deployed to a new version of your application.

  4. To start the development cycle on your Kubernetes cluster, click the run action for **Develop on Kubernetes**.

  5. In the **output window** , on the **Logs** tab, view incoming application logs.

After the deployment has started, you'll see the list of forwarded ports for the deployed application.

  6. When the deployment is successful, you're notified that new service URLs are available. Click the **Service URLs** tab to view the URL(s), then click the URL link to open your browser with your running application.

![Viewing port-forwarded services in the Service URLs tab](https://docs.cloud.google.com/static/code/docs/intellij/images/port-forward-service-urls-hello-world.png)

Alternatively, you can open the **Event Log** and then click the link to open your browser with your running application.

The **Deployed Resources** pane shows what you deployed during the development session.




## Debug your application

**Note:** Debugging support is available for Java, Kotlin, Node.js, Go, and Python.

Cloud Code supports [applying changes while debugging](https://docs.cloud.google.com/code/docs/intellij/watch-modes#applying-changes-while-debugging).

To debug your application:

  1. Click the debug action ![Debug action icon](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-action.png) for **Develop on Kubernetes** to start the development cycle in debug mode on your Kubernetes cluster.

![Starting the Kubernetes cluster development cycle in debug mode](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-target.png)

**Note:** For Node.js apps, you will be prompted to help the debugger map your local sources to the remote sources in the container for each artifact you are debugging. This enables the Node debugger to correctly process your breakpoints. For more on how to configure this setting, refer to the [Debugging an app guide](https://docs.cloud.google.com/static/code/docs/intellij/debug#node.js).
  2. Cloud Code will attach a debug session. When successful, the Debug Tool window opens, confirming connection (on the Console tab).

You can now debug against your live Kubernetes cluster.

  3. Click the gutter at the executable line of the code where you want to add a breakpoint.

Red filled circles denote active breakpoints, while red-outlined hollow circles signify disabled breakpoints.

  4. When you send a new request to your application, it will pause at that desired line.

![Kubernetes debugger session](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debugger-session.png)

  5. To end the debugging session, click the stop icon on the `Develop on Kubernetes` run configuration.




## View logs

In addition to seeing a livestream of the logs from running pods in the terminal output as you're developing and running your application, you can view logs from a specific pod by navigating to the Kubernetes Explorer.

To view logs from a specific pod, follow these steps:

  1. Navigate to the Kubernetes Explorer. It can be accessed either from the side panel on the right or using **Tools** > **Cloud Code** > **Kubernetes** > **View Cluster Explorer**.

![Kubernetes Explorer panel open using the tab on the right side taskbar](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-explorer-panel-full-view.png)

  2. Select the pod you'd like to see logs from.

  3. Right-click the pod and then select **Stream Logs**. Alternatively, you can stream logs for individual containers running in pods.

This outputs logs to the Kubernetes Explorer Console.

![Streaming logs from a pod using its right-click menu to output logs into the Kubernetes Explorer Console](https://docs.cloud.google.com/static/code/docs/intellij/images/stream-logs-hello-world-pod.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

  2. Select the project you created for this Quickstart and click the trash can icon next to delete it.

This shuts down the project and schedules it for deletion.




## What's next

  * Consider importing an existing [Kubernetes](https://docs.cloud.google.com/code/docs/intellij/use-k8s-existing-app) application into your IDE and getting set up with Cloud Code.
  * Dive deeper into developing Kubernetes applications: 
    * Tackle more advanced Google Cloud and Kubernetes configuration with Cloud Code's [YAML editing support](https://docs.cloud.google.com/code/docs/intellij/yaml-editing).
    * For better insight into and management of your Kubernetes resources, use [the Kubernetes Explorer](https://docs.cloud.google.com/code/docs/intellij/use-kubernetes-explorer).
    * [Deploy your applications to ARM64, AMD64, or mixed-architecture GKE clusters](https://docs.cloud.google.com/code/docs/intellij/deploy-to-arm-amd-mixed-arch).
  * [Manage Cloud APIs and client libraries](https://docs.cloud.google.com/code/docs/intellij/client-libraries) from the comfort of your IDE.
  * [Explore your Cloud Storage content](https://docs.cloud.google.com/code/docs/intellij/gcs) within your IDE.
  * Add new projects to and check out existing ones from [Cloud Source Repositories with Cloud Code](https://docs.cloud.google.com/code/docs/intellij/vcs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
