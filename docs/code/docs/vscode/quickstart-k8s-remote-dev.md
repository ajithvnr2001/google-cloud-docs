---
url: https://docs.cloud.google.com/code/docs/vscode/quickstart-k8s-remote-dev/
title: Quickstart: Deploy a Kubernetes app by using remote development in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:48.378097+00:00
---

# Quickstart: Deploy a Kubernetes app by using remote development in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/quickstart-k8s-remote-dev/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Kubernetes app by using remote development

This page shows you how to get started quickly with Cloud Code for VS Code using a remote development environment in Cloud Shell.

In this quickstart, you'll skip setup and clone a project into your remote development workspace with the click of a button, create a cluster, run a Kubernetes app on this cluster, debug your running code, view logs from your live application, and connect a terminal to your running container.

**Note:** For steps to set up remote debugging on Chrome OS, see [Build a dev workflow with Cloud Code on a Pixelbook](https://cloud.google.com/blog/products/application-development/build-a-dev-workflow-with-cloud-code-on-a-pixelbook).

## Before you begin

To set up supporting resources and access Cloud Shell, the remote development environment on Google Cloud that you use in this quickstart, inside VS Code, complete the following steps:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Install [Visual Studio Code](https://code.visualstudio.com/) on your machine, if you haven't already.
  7. Install the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) Visual Studio Code extension.
  8. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is required for copying samples to your machine.
  9. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/vscode/install#installing) if you haven't already.



## Launching Cloud Code

When you open Visual Studio Code connected to a remote development environment in Cloud Shell, the environment has all the tools you need to develop Kubernetes applications.

  1. To start work in your remote development workplace, choose your preferred language for the cloned project and then click the **Open with Cloud Code** button:

### Node.js

[Open with Cloud Code](vscode://googlecloudtools.cloudcode/shell?repo=https://github.com/GoogleCloudPlatform/cloud-code-samples.git&subpath=/nodejs/nodejs-guestbook)

### Java

[Open with Cloud Code](vscode://googlecloudtools.cloudcode/shell?repo=https://github.com/GoogleCloudPlatform/cloud-code-samples.git&subpath=/java/java-guestbook)

### Python

[Open with Cloud Code](vscode://googlecloudtools.cloudcode/shell?repo=https://github.com/GoogleCloudPlatform/cloud-code-samples.git&subpath=/python/python-guestbook)

### Go

[Open with Cloud Code](vscode://googlecloudtools.cloudcode/shell?repo=https://github.com/GoogleCloudPlatform/cloud-code-samples.git&subpath=/golang/go-guestbook)

VS Code launches and clones a project into your remote development workspace.

  2. If you don't already have the prerequisites set up, you're prompted to install them.




## Create a GKE cluster

To create a Standard Google Kubernetes Engine (GKE) cluster, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and expand the **Kubernetes** section.

  2. Click add **Add a cluster to the KubeConfig** and then click **Google Kubernetes Engine** in the **Quick pick** menu.

  3. When prompted to enable the container API, select **Yes**.

  4. Click **\+ Create a New GKE Cluster**.

  5. Choose **Standard** as the cluster type.

  6. Click **Open** to permit Cloud Code to open the Google Cloud console.

  7. In the Google Cloud console, ensure the project selected is the one you created or chose earlier.

  8. Set the cluster name to `my-first-cluster`.

  9. Select **Zonal** as the location type, and set the zone to `us-central1-a`.

  10. Click **Create**. Cluster creation takes a few minutes.

  11. After the cluster is created, click **Add a cluster to the KubeConfig** again, and select from the list the cluster you just created.

  12. Your new cluster is added to the configuration and configured to be the active context.




## Run and view your app

Now that you're all set up, you can run your application and view it live. Cloud Code watches your file system for changes so that you can edit and rerun your app in near real time.

To run your application, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Run on Kubernetes**. When prompted again, select **Run on Kubernetes**.

  3. Confirm whether to use the current cluster context or switch to a different one.

  4. If prompted, choose an image registry to push the images to. If you're creating a new image registry using `gcr.io/PROJECT_ID`, ensure that the image registry is in the same project as your cluster.

  5. After your application is running on Kubernetes, click the **Status** entry of the **Run on Kubernetes** task in the **Development sessions** section. A window will open with an **Output** tab that includes the URL of your application. To open this URL, press `Control` (or `Command` on macOS) and click the address.

You can also find your application in the [Workloads overview](https://console.cloud.google.com/kubernetes/workload/overview) in the Google Cloud console. For more information about your running application, including its external IP address and port number, click its name in the list.




### Troubleshooting tips

If you're using a pre-existing cluster, to set your cluster as active and get cluster credentials, follow these steps:

  1. In VS Code, click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and expand the **Kubernetes** section.

  2. Right-click your cluster name and then click **Set as Active Cluster**.




## Debug your app

To debug your application, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Debug on Kubernetes**.

  3. If prompted, [authenticate your credentials to run and debug an application locally](https://docs.cloud.google.com/code/docs/vscode/install#authenticate_credentials_for_debugging_applications_locally).

  4. If prompted, confirm whether to use the current cluster context or switch to a preferred one.

Cloud Code uses the `cloudcode.kubernetes` configurations in your `.vscode/launch.json` file to run your application and attach a debugger session to it.

Cloud Code builds your containers, pushes them to the registry, applies Kubernetes configurations to the cluster, and returns the IP address that you can use to browse your live application.

  5. Before your debugger session is attached, you're prompted to confirm or enter the directory in the remote container where the program to debug is found or press ESC to skip debugging the container.

  6. To add a breakpoint to line #9, open `src/app.js` and then click in the editor margin.

Red filled circles signify active breakpoints, while gray hollow circles signify disabled breakpoints. For finer breakpoint control, you can use the Breakpoints section in VS Code's Debug view.

![Breakpoints section in the left hand panel of Debug View that allows adding, removing, and disabling breakpoints](https://docs.cloud.google.com/static/code/docs/vscode/images/breakpoint-section.png)

When you send a new request to your application, the debugger pauses at the first active breakpoint.

In the following sample, under **Local** in the **Variables** section, note that the value of `res._contentLength;` for `Hello, world!` is 13.

![App paused at breakpoint and variables and call stack sections populated with values in scope](https://docs.cloud.google.com/static/code/docs/vscode/images/quickstart-debug-breakpoints.png)

  7. Edit the string being sent inline #8 to `Hello, goodbye!` and then restart the **Debug on Kubernetes** action.

After the app is rebuilt and redeployed, note the updated value of `res._contentLength`.

![App paused at breakpoint with updated values](https://docs.cloud.google.com/static/code/docs/vscode/images/quickstart-debug-breakpoints-2.png)




After your debugging session starts, the **Development sessions** pane displays the structured logging view. As a task begins, the task appears with a spinning semi-circle progress_activity.

If a task succeeds, a check mark check_circle appears next to the step.

To see details of a step, click the step in the **Development session** pane. The Output pane displays the step in the logging output.

## Open a terminal in your container

To open a terminal in your container, follow these instructions:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and expand the **Kubernetes** section.

  2. Expand the following sections:

     * Your preferred cluster's section
     * The **Namespaces** section and then your preferred namespace's section
     * The **Pods** section and then your preferred pod's section
     * The **Containers** section

![Cloud Code pods](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-pods.png)

  3. Right-click the container in which you'd like to open a terminal and then click **Get Terminal**.

This launches a terminal. You now have access to a shell inside the running container.




## Clean up

After you stop your application, all Kubernetes resources deployed during the run are deleted automatically.

To avoid incurring charges to your account for other resources used in this quickstart, be sure to delete the project or delete the cluster you created if you want to reuse the project.

To delete the cluster:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** explorer.
  2. Hold the pointer over your cluster name and then click open_in_new **Open in Google Cloud console**.
  3. Click **Delete** and then click **Delete**.



To delete your project (and associated resources, including any clusters):

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Consider [importing an existing application](https://docs.cloud.google.com/code/docs/vscode/use-existing-app) into VS Code and getting set up with Cloud Code.
  * Tackle more advanced Google Cloud and Kubernetes configuration with Cloud Code's [YAML editing support](https://docs.cloud.google.com/code/docs/vscode/yaml-editing).
  * Discover the language-specific [debugging support](https://docs.cloud.google.com/code/docs/vscode/debug) that Cloud Code provides.
  * Speed up your development with [file sync and hot reloading](https://docs.cloud.google.com/code/docs/vscode/speed-up-k8s-development#enable-file-sync-and-hot-reloading).
  * [Create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster)
  * [Configure private clusters](https://docs.cloud.google.com/code/docs/vscode/configure-private-cluster)
  * Customize your Cloud Code experience by configuring [relevant settings](https://docs.cloud.google.com/code/docs/vscode/configuring-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
