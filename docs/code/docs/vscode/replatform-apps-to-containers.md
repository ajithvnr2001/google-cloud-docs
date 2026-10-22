---
url: https://docs.cloud.google.com/code/docs/vscode/replatform-apps-to-containers/
title: Replatform Linux applications to containers \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:36.703424+00:00
---

# Replatform Linux applications to containers  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/replatform-apps-to-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Replatform Linux applications to containers Stay organized with collections  Save and categorize content based on your preferences. 

The [Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs/getting-started) integration with [Cloud Code](https://docs.cloud.google.com/code/docs/vscode/overview) gives you the ability to modernize Linux application components that run on virtual machines (VMs), and generate artifacts that can be deployed to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run), directly in your IDE, using a Linux machine. 

In this guide, you learn how to replatform an existing application to a GKE container using the Cloud Code extension in your IDE on a Linux machine.

This guide is intended for developers on a Linux machine that have working knowledge of VS Code, are familiar with Google Cloud, and have a VM running their application component.

**Note:** To perform the steps in this guide, you must use a Linux machine. Cloud Code doesn't support replatforming applications to containers using Windows or macOS.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Google Kubernetes Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  8. Install the [Cloud Code extension](https://docs.cloud.google.com/code/docs/vscode/install#installing) if you haven't already.
  9. [Create and configure a GKE cluster](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster).
  10. Make sure you know what type of migration you want to perform. For more information on supported workloads, see [Review compatible OS, workloads, and Kubernetes versions](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/compatible-components#supported_workloads).
  11. [Prepare your source and local machines for modernization](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/prepare-for-migration). Cloud Code only supports Linux for modernization.



## Add a replatform source

In this section, you install the Migration Center discovery client CLI (`mcdc`) and other Migrate to Containers tools on your local machine, if you haven't already, and add a replatform source by following these steps:

  1. In the activity bar of your IDE, click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** , and then expand the **Replatform Apps** explorer.

  2. If this is your first time using Migrate to Containers in Cloud Code, you'll need to install the `mcdc` CLI and other Migrate to Containers tools on your local machine by clicking **Install tools**. Otherwise, proceed to the next step.

  3. Click **Edit Sources**. This opens an empty `mcdc-sources.json` file. Add your sources in the following format:
         
         [
           {
             "title": "SOURCE_NAME",
             "host": "HOSTNAME",
             "user": "USER",
             "identityFile":"IDENTITY-FILE-PATH"
           }
         ]
         

**Note:** You can use the same `host`, `user`, and `identityFile` variables in an SSH command.
  4. To see the sources appear in the **Replatform Apps** explorer, hold your pointer over the **Replatform Apps** explorer and click the cached **Reload sources** button that appears.




### Optional: Generate a Fit Assessment

Before attempting to replatform your application to a container, we recommend that you generate a [Fit Assessment](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment) of your source, which notifies you if your source is capable of replatforming a container.

To generate a Fit Assessment of your source, right-click your source and select **Assess source**. This opens the terminal in your IDE and displays the logs of your source's assessment.

When the assessment is complete, `mcdc` generates a Fit Assessment Report in your IDE.

If your sources are reported to be a _Good Fit_ , then you're ready to replatform your application.

## Replatform your application

Cloud Code creates a dedicated workspace for each replatform and lets you run the **Copy** , **Analyze** , and **Generate** tasks in the workspace to automate the replatform steps. If you run the **Generate** task without running the **Copy** and **Analyze** tasks first, it automatically runs them before generating artifacts.

The following sections guide you through performing each of these tasks and replatforming your application to a container using Cloud Code.

To learn more about the lifecycle of a migration, see [Migrate to Containers CLI architecture](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/architecture).

### Create a new replatform workspace

Before you create a new replatform workspace, you'll need to know which migration parameters to select for your migration type. For more information about the parameters for each migration type, see [Create a migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan).

To create a new replatform workspace with artifacts in your IDE, follow these steps:

  1. In the **Replatform Apps** explorer, right-click the source you want to replatform and then click **Replatform**.

  2. From the list of options that appear in the menu, select a replatform journey.

  3. Select a new workspace directory to replatform your application in, click **OK** , and then click **Create replatform workspace**.

  4. Select the migration parameters for your migration type.

  5. Optional: If you selected the WebSphere migration type and want to use a [binary scanner](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan#optional_set_up_the_binaryappscannerjar), select the `binaryAppScanner.jar` file.

The workspace generation takes a few seconds. This opens your new workspace directory in a new window of your IDE.




### Copy files from your VM to your workspace

To copy the files from your VM to your workspace in your IDE, perform the following steps:

  1. Optional: The `mcdc` CLI applies filters to reduce the size of the copy, but you can modify the `filters.txt` file to further reduce the size of the copy. To learn how to reduce the size of the copy, see [Reduce the size of the copied file system](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/copy-file-system#reduce_the_size_of_the_copied_file_system).

  2. Open the command palette by pressing `Ctrl+Shift+P`.

  3. Search for and select **Tasks: Run Task** , and then select **m2c: Copy**. Copying files may take a few minutes.




### Analyze VM file system and generate a migration plan

To analyze the VM file system and generate a migration plan, perform the following steps:

  1. Open the command palette by pressing `Ctrl+Shift+P`.

  2. Search for and select **Tasks: Run Task** , and then select **m2c: Analyze**.

If the analyze task fails, you need to modify your migration parameters through the `analyze-args.ini` file. This file has one line per parameter with accompanying documentation about the parameter.

When the analysis succeeds, Cloud Code creates a directory called `migration-plan` which contains the results of the analysis in the form of a `config.yaml` file. You can edit this file to change the way your artifacts are generated.

The structure of your `config.yaml` file differs based on your migration type. For more information about the supported migration types, see the following pages:

     * [Linux VMs](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/linux/customizing-a-migration-plan)
     * [Tomcat servers](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/tomcat/tomcat-customizing-a-migration-plan)
     * [WebSphere workloads](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere/websphere-customizing-a-migration)
     * [JBoss servers](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/jboss/jboss-customizing-a-migration-plan)
     * [Apache servers](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/apache/apache-customizing-a-migration-plan)
     * [WordPress sites](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/wordpress/wordpress-customizing-a-migration-plan)



### Generate artifacts

To generate artifacts, you need to run the **Generate** task in your IDE. If you didn't already run the **Copy** and **Analyze** tasks in the previous sections, the **Generate** task automatically runs them both before generating artifacts.

To generate the artifacts, perform the following steps:

  1. Open the command palette by pressing `Ctrl+Shift+P`.

  2. Search for and select **Tasks: Run Task** , and then select **m2c: Generate**. This generates the artifacts in the `src` directory, which contains a `skaffold.yaml` file that is used to build and deploy a container image. Each migration type generates different artifacts, but all migration types usually create one or more dockerfiles and a GKE deployment spec that `skaffold.yaml` references.

When artifact generation is complete, you're finished replatforming your application!

  3. Optional: If you want to modify the migration plan, edit your `config.yaml` file and re-run the **m2c: Generate** task.

Otherwise, if you're satisfied with your replatform results, you can proceed to run your application in a GKE container.




## Run your application in a GKE container

In this section, you run your replatformed application in a GKE container, view your running application's logs, and clean up resources.

If you haven't already created and configured a GKE cluster, follow the instructions in [Create and configure a GKE cluster in Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster). 

To learn more about debugging GKE applications, see [Debug Kubernetes applications with Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/debug).

### Run and view your application

Now that you're all set up, you can run your application and view it live. Cloud Code watches your file system for changes so that you can edit and rerun your app in real time.

To run your application, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **Run on Kubernetes**.

  3. Confirm whether to use the current cluster context or switch to a different one.

  4. If prompted, choose an image registry to push the images to. If you're creating a new image registry using `gcr.io/PROJECT_ID`, ensure that the image registry is in the same project as your cluster.

An output window appears where you can track the progress of your running application. You'll also see a livestream of the logs from the running pods in the terminal output.

  5. After your application is running on Kubernetes, the output window displays an IP address. To use this linked IP address to access your application, press `Ctrl` and click the address.




After your debugging session starts, the **Development sessions** pane displays the structured logging view. As a task begins, the task appears with a spinning semi-circle progress_activity.

If a task succeeds, a check mark check_circle appears next to the step.

To see details of a step, click the step in the **Development session** pane. The Output pane displays the step in the logging output.

### Clean up

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



To delete all local files that were created during the replatform process:

  1. Open the command palette (`Ctrl+Shift+P`).
  2. Search for and select **Tasks: Run Task** , and then select **m2c: Cleanup**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
