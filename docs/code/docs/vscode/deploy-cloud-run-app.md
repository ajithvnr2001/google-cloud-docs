---
url: https://docs.cloud.google.com/code/docs/vscode/deploy-cloud-run-app/
title: Quickstart: Deploy a Cloud Run service with Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:12.462611+00:00
---

# Quickstart: Deploy a Cloud Run service with Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/deploy-cloud-run-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Cloud Run service with Cloud Code for VS Code

This document shows you how to get started with Cloud Code.

You'll create a service from a sample "Hello, world" application, deploy your service publicly with Cloud Code, and view the status of your live service's resources.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  10. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is required to copy samples to your machine.
  11. Install [Docker](https://docs.docker.com/get-docker/). Docker is required to build the sample code. Ensure your local user account is able to build containers.
  12. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/vscode/install#installing) if you haven't already.



### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on the project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Cloud Run Builder ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a service

To create a sample service application, follow these steps:

  1. In the Cloud Code status bar, click the active project name.

![Active project name in status bar](https://docs.cloud.google.com/static/code/docs/vscode/images/cloudcode-status-bar.png)

  2. In the Quick Pick menu that appears, select **New Application**.

  3. Select **Cloud Run application** as the application type.

  4. From the list of sample applications, select one for your preferred language.

For example, choosing **Node.js: Cloud Run** creates a "Hello, world" service application in Node.js.

  5. Confirm the file system location of your service's source code (or modify it, if necessary) and click **Create New Application**.

A preview of the `README.md` file for your selected service opens in VS Code.




## Deploy to Cloud Run

To deploy your service to Cloud Run, follow these steps:

  1. Open the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run the **Deploy to Cloud Run** command.

  2. In the **Deploy to Cloud Run** pane, set your Google Cloud project.

  3. Accept the remaining default settings and then click **Deploy**.

Cloud Code builds your image, pushes it to the registry, and deploys your service to Cloud Run.

  4. To view your running service, open the URL displayed at the top of the **Deploy to Cloud Run** dialog.




## View resource status

You can view the status of your Cloud Run services using the Cloud Run service browser:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** in the VS Code Activity bar.
  2. Expand the **Cloud Run** section to view your Cloud Run service.
  3. Click the service to view its properties.



## View logs

You can also view logs from your deployed service with the Log Viewer that comes with Cloud Code.

To view logs, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** in the VS Code Activity bar.
  2. Expand the **Cloud Run** section to view your Cloud Run service.
  3. Right-click your Cloud Run service and then click **View logs**.



## Clean up

To delete your project:

  1. Go to the Projects page in the Google Cloud console:

[Go to the Projects page](https://console.cloud.google.com/project)

  2. Select the project you created for this quickstart and then click **Delete**.

  3. Type the project ID to confirm and then click **Shut down**.

This shuts down the project and schedules it for deletion.




If you're using a pre-existing project and would like to delete resources you created for this quickstart:

  * **Container image:** While Cloud Run doesn't charge when the service isn't in use, you might be [charged for storing the container image in Artifact Registry](https://cloud.google.com/artifact-registry/pricing). For steps to delete your image, see [Deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images).

  * **Cloud Run service:** To delete a Cloud Run service, navigate to Cloud Run in the Google Cloud console using the navigation menu. Select the service you want to delete and then click **Delete**. 




## What's next

  * Discover the language-specific [debugging support](https://docs.cloud.google.com/code/docs/vscode/debug) that Cloud Code provides.
  * Customize your Cloud Code experience by configuring [relevant settings](https://docs.cloud.google.com/code/docs/vscode/configuring-settings).
  * Try creating and [running a Kubernetes application with Cloud Code](https://docs.cloud.google.com/code/docs/vscode/quickstart-local-dev). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
