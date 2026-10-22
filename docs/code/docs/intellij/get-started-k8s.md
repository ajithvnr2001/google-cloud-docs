---
url: https://docs.cloud.google.com/code/docs/intellij/get-started-k8s/
title: Get started with Cloud Code for IntelliJ for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:46.718217+00:00
---

# Get started with Cloud Code for IntelliJ for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/get-started-k8s/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Get started with Cloud Code for IntelliJ for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code lets you create a Kubernetes application based on a sample or from an existing project.

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

## Container image storage options

If you chose a remote cluster as the context, choose an image registry to push the images to. Go to **Run** > **Edit configurations** to set the image registry in your **Run/Debug Configurations**.

Refer to the [guide on storing your container image](https://docs.cloud.google.com/code/docs/intellij/configuring-container-image-settings) for more details.

## Build settings

Cloud Code supports Docker, Jib, and Buildpacks artifact types. Refer to the [Configuring container image build preferences guide](https://docs.cloud.google.com/code/docs/intellij/image-build-settings) to learn about how to set your preferred builder and its relevant settings.

## Customize your launch configuration

To configure how your application is run, you can customize your [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml) file.

You can also configure your launch in your **Run/Debug configurations**. To edit your configurations, go to **Run** > **Edit configurations**.

For more information on customizing your launch configuration, see the [Kubernetes in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/k8s-overview#customize_your_launch_configuration).

**Note:** Cloud Code is built to work with [Cloud Build](https://docs.cloud.google.com/build/docs). To build an existing application using Google Cloud infrastructure, see the [Skaffold docs for Cloud Build](https://skaffold.dev/docs/pipeline-stages/builders/docker/#dockerfile-remotely-with-google-cloud-build).

## Run your application

Once you have an application set up, you can run it on a Kubernetes cluster and view it live, by leveraging [`skaffold dev`](https://skaffold.dev/docs/workflows/dev). You can run your application on a local cluster (like minikube or Docker Desktop), Google Kubernetes Engine, or any other Cloud provider.

**Note:** If you're working with a private Autopilot cluster, you might run into an image pull error when pulling an image outside of the image registry for your project, such as by using Docker Hub. To resolve this issue, you can either host the image on [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) or provide [outbound internet access for your private nodes](https://docs.cloud.google.com/nat/docs/gke-example#create-nat).

  1. Click the Run icon on your preferred run action. You can then view incoming application logs in the **output window** under the **Logs** tab.

When the deployment starts, you'll see the list of forwarded ports for your deployed application.

  2. After the deployment is successful, you're notified that new service URLs are available. Click the **Service URLs** tab to view the URL(s), then click the URL link to open your browser with your running application. 

Alternatively, you can open the **Event Log** and then click the link to open your browser with your running application.

The **Deployed Resources** pane shows what you deployed during the development session.




## View logs

In addition to seeing logs from running pods as a live stream in the terminal output as you're developing and running your application, you can view logs from a specific pod by navigating to the Kubernetes Explorer.

To view logs from a specific pod, follow these steps:

  1. Navigate to the Kubernetes Explorer. It can be accessed either from the side panel on the right or using **Tools** > **Cloud Code** > **Kubernetes** > **View Cluster Explorer**. 

  2. Select the pod you'd like to see logs from.

  3. Right-click the pod and then click **Stream Logs**. Alternatively, you can stream logs for individual containers running in pods.

The Kubernetes Explorer Console displays the logs.




## Make changes, rebuild, and clean up

If watch mode is set to **On demand** in your launch configuration and you want to make changes to your application and then rebuild and redeploy the application: 

  1. Make and save your changes.

  2. Click the **Trigger Build and Deploy** icon or press `Option + Ctrl/Cmd + Comma` to rebuild and redeploy the application.

  3. To stop running the application, click the **Stop** icon or press `Ctrl/Cmd + F2`.




After you stop the application, all deployed Kubernetes resources are deleted from the cluster. You can change this behavior using the `cleanUp` flag in your launch configuration.

## Store secrets

If your code includes potentially sensitive data like API keys, passwords, and certificates, it is recommended you store them as secrets. With Cloud Code, you can securely store these secrets in Secret Manager and programmatically fetch them when you need them.

For a detailed look at how you can create and manage secrets with Cloud Code, see the [Secret Manager guide](https://docs.cloud.google.com/code/docs/intellij/secret-manager).

## View resource details

The Kubernetes Explorer displays clusters, namespaces, nodes, workloads (such as deployments, replicasets, pods and containers), services and ingresses, configurations (such as secrets and config maps) and storage (such as volumes). Using the Kubernetes Explorer, you can perform unique actions on some of these resources.

See the [Kubernetes overview](https://docs.cloud.google.com/code/docs/intellij/k8s-overview#resource-specific_actions) for more information on viewing resource details.

## What's next

  * [Explore your build options with buildpacks, Jib, or Docker](https://docs.cloud.google.com/code/docs/intellij/image-build-settings).
  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Learn more about Cloud Code's [YAML editing](https://docs.cloud.google.com/code/docs/intellij/yaml-editing) assistance.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
