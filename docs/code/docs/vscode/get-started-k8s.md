---
url: https://docs.cloud.google.com/code/docs/vscode/get-started-k8s/
title: Get started with Cloud Code for VS Code for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:13.294838+00:00
---

# Get started with Cloud Code for VS Code for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/get-started-k8s/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Get started with Cloud Code for VS Code for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code lets you create a Kubernetes application based on a sample or from an existing project.

## Create an application from a template

Cloud Code comes with a collection of [code sample](https://github.com/GoogleCloudPlatform/cloud-code-samples#readme) templates to get you started quickly. To create a Kubernetes application using an existing sample, follow these steps:

  1. Launch the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: New Application**.
  2. Select **Kubernetes application** for the type of sample.
  3. Select a sample based on the language you'd like to use from the available options: NodeJS, Go, Python, Java.
  4. Choose a preferred application location on your local machine and then click **Create new application** to save.

Cloud Code clones the sample you chose and opens your new project for use.




### Sample application structure

All language sample applications have nearly the same structure. This is not the only supported structure but is recommended when starting.

For example, the Node.js Guestbook application structure looks like:
    
    
    .
    |---- .vscode
    |      └---- launch.json
    |---- kubernetes-manifests
    |     |---- guestbook-backend.deployment.yaml
    |     |---- guestbook-backend.service.yaml
    |     |---- guestbook-frontend.deployment.yaml
    |     |---- guestbook-frontend.service.yaml
    |     |---- mongo.deployment.yaml
    |     └---- mongo.service.yaml
    |---- src
    |     |---- backend
    |     |     |---- Dockerfile
    |     |     |---- index.js
    |     |     |---- app.js
    |     |     └---- package.json
    |     |---- frontend
    |           |---- Dockerfile
    |           |---- index.js
    |     |     |---- app.js
    |           └---- package.json
    └---- skaffold.yaml
    

Taking a closer look at this Kubernetes Guestbook Node.js sample app, here are some key files and their uses:

  * .vscode 
    * `extensions.json`: prompt requesting download of related extensions when opening this project
    * `launch.json`: launch configuration (of type `cloudcode.kubernetes`) to run or debug the Kubernetes application
    * `tasks.json`: configuration information for [Visual Studio Code Tasks](https://code.visualstudio.com/docs/editor/tasks)
  * kubernetes-manifests 
    * `guestbook-backend.deployment.yaml`: Pod specification for the backend nodes
    * `guestbook-frontend.deployment.yaml`: Pod specification for the frontend nodes
    * `mongo.deployment.yaml`: Pod specification for the database
  * src 
    * `(backend|frontend)/app.js`: Node.js code with the web server logic
    * `(backend|frontend)/Dockerfile`: used to build the container image for our program
  * `skaffold.yaml`: A [config file](https://skaffold.dev/docs/), which Cloud Code uses to build, deploy and debug Kubernetes applications



## Use your own application

For steps to use an existing project, see [use Cloud Code with an existing Kubernetes application](https://docs.cloud.google.com/code/docs/vscode/use-existing-app).

**Note:** For developing and testing an app, create and run the application on a non-production cluster.   
For changes that will be rolled out to production, use an [automated CI/CD workflow](https://docs.cloud.google.com/docs/ci-cd). 

## Set your Kubernetes context

Before running your application, ensure you're set up to deploy your app to your preferred Kubernetes context. You can specify this in your configuration.

## Configuration

When using the **Cloud Code: Develop on Kubernetes** run configuration, you can customize your deployment by configuring available settings.

To add or edit configurations, go to **Run** > **Open Configurations** and then edit or add configurations. 

## Build settings

Cloud Code supports Docker, Jib, and Buildpacks artifact types. Refer to the [Configuring container image build preferences guide](https://docs.cloud.google.com/code/docs/vscode/image-build-settings) to learn about how to set your preferred builder and its relevant settings.

## Customize your launch configuration

To configure how your application is run, you can customize your [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml) file.

You can also configure your launch by editing the `cloudcode.kubernetes` configuration in your `.vscode/launch.json` file.

For more information on customizing your launch configuration, see the [Kubernetes in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/k8s-overview#customize_your_launch_configuration).

**Note:** Cloud Code is built to work with [Cloud Build](https://docs.cloud.google.com/build/docs). To build an existing application using Google Cloud infrastructure, see the [Skaffold docs for Cloud Build](https://skaffold.dev/docs/pipeline-stages/builders/docker/#dockerfile-remotely-with-google-cloud-build).

## Run your application

Once you have an application set up, you can run it on a Kubernetes cluster and view it live, by leveraging [`skaffold dev`](https://skaffold.dev/docs/workflows/dev). You can run your application on a local cluster (like minikube or Docker Desktop), Google Kubernetes Engine, or any other Cloud provider.

**Note:** If you're working with a private Autopilot cluster, you might run into an image pull error when pulling an image outside of the image registry for your project, such as by using Docker Hub. To resolve this issue, you can either host the image on [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) or provide [outbound internet access for your private nodes](https://docs.cloud.google.com/nat/docs/gke-example#create-nat).

  1. Open the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P`) and then run the **Cloud Code: Run on Kubernetes** command.
  2. Confirm whether to use the current [Kubernetes context](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#context) to run the app in (or switch to a preferred one). For more information about setting up a Kubernetes context, see [setting up configuration](https://docs.cloud.google.com/code/docs/vscode/use-existing-app#setting_up_configuration).
  3. If you chose a remote cluster as the context, when prompted, choose an image registry to push the images to. If your project has [Artifact Registry API enabled](https://docs.cloud.google.com/artifact-registry/docs/enable-service) and at least one [Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/manage-repos), you can browse to and select an existing Artifact Registry repository.

The following samples demonstrate how to specify where container images are stored for some common registries: 

Artifact Registry  | `REGION`-docker.pkg.dev/`PROJECT_ID`/`REPO_NAME`  
---|---  
Docker Hub  | docker.io/`ACCOUNT`   
Make sure that you're [properly authenticated](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry) if you're using a private Docker Hub repository.   
  
AWS Container Repository (ECR)  | `AWS_ACCOUNT_ID`.dkr.ecr.`REGION`.amazonaws.com/`APP`  
Azure Container Registry (ACR)  | `ACR_NAME`.azurecr.io/`APP`  
  
Cloud Code concatenates this image registry with the image name specified in the Kubernetes manifests to generate the final image repository name.

For more information, see the [image registry handling guide](https://skaffold.dev/docs/environment/image-registries).

This choice is stored in your `cloudcode.kubernetes` launch configuration (found in .vscode/launch.json).

Cloud Code builds your containers, pushes them to the registry, applies Kubernetes configurations to the cluster, and waits for the rollout. 




## View logs

In addition to seeing logs from running pods as a live stream in the terminal output as you're developing and running your application, you can view logs from a specific pod by navigating to the Kubernetes section.

To view logs from a specific pod, follow these steps:

  1. In the Kubernetes section, expand **Deployments**
  2. Right-click the pod you'd like to see logs from, and then click **View Logs**.

The **Logs viewer** opens. 




## Make changes, rebuild, and clean up

If you've set watch mode to `false` in your launch configuration and you want to make changes to your application and then rebuild and redeploy the application: 

  1. Make and Save your changes.

  2. In the Debug Toolbar, click **Pause** (`F6`) and then click **Restart** (`Ctrl/Cmd + Shift + F5`) to rebuild and redeploy the application.

  3. To stop running the application, in the Debug Toolbar, click **Stop**.




After you stop the application, all deployed Kubernetes resources are deleted from the cluster. You can change this behavior using the `cleanUp` flag in your launch configuration.

## Store secrets

If your code includes potentially sensitive data like API keys, passwords, and certificates, it is recommended you store them as secrets. With Cloud Code, you can securely store these secrets in Secret Manager and programmatically fetch them when you need them.

For a detailed look at how you can create and manage secrets with Cloud Code, see the [Secret Manager guide](https://docs.cloud.google.com/code/docs/vscode/secret-manager).

## View resource details

The Kubernetes section displays clusters, namespaces, nodes, workloads (such as deployments, replicasets, pods and containers), services and ingresses, configurations (such as secrets and config maps) and storage (such as volumes). Using the Kubernetes section, you can perform unique actions on some of these resources.

See the [Kubernetes overview](https://docs.cloud.google.com/code/docs/vscode/k8s-overview#resource-specific_actions) for more information on viewing resource details.

## What's next

  * [Explore your build options with buildpacks, Jib, or Docker](https://docs.cloud.google.com/code/docs/vscode/image-build-settings).
  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * Learn more about Cloud Code's [YAML editing](https://docs.cloud.google.com/code/docs/vscode/yaml-editing) assistance.



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
