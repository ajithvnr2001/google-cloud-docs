---
url: https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager/
title: Enable the Secret Manager API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:33.334705+00:00
---

# Enable the Secret Manager API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Enable the Secret Manager API Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager exposes a REST API and a gRPC API for using and managing secrets directly or in your applications. This page describes how to enable the Secret Manager API and configure your Google Cloud project to use Secret Manager for the first time.

This step is a prerequisite for all tasks in Secret Manager, including the [quickstart](https://docs.cloud.google.com/secret-manager/docs/quickstart).

When you are becoming familiar with Secret Manager, we recommend using a separate Google Cloud project. Deleting the project also deletes all resources created during testing, including billable resources.

If you are developing an application in an IDE with [Cloud Code](https://cloud.google.com/code) installed, Secret Manager comes integrated into the extension. This means that you can create, view, update, and use secrets without having to leave your IDE. For more on using Secret Manager with Cloud Code, refer to the secret managing guide for your preferred IDE, [VS Code](https://docs.cloud.google.com/code/docs/vscode/secret-manager), [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/secret-manager), or [Cloud Shell Editor](https://docs.cloud.google.com/code/docs/shell/secret-manager).

## Before you begin

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.



## Enable the Secret Manager API

### Console

  1. In the Google Cloud console, go to the **Secret Manager API** page.

[Go to Secret Manager API](https://console.cloud.google.com/apis/library/secretmanager.googleapis.com)

  2. Verify that the name of your project appears in the project selector at the top of the page.

If you don't see the name of your project, click the project selector, and then select your project.

  3. Click **Enable**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To set your Google Cloud project in the gcloud session, run the [`gcloud config set project`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command. Replace PROJECT_ID with your Google Cloud project ID. 
         
         gcloud config set project PROJECT_ID

  3. To enable the Secret Manager API, run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command: 
         
         gcloud services enable secretmanager.googleapis.com

  4. To verify that the Secret Manager API is enabled, run the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command: 
         
         gcloud services list --enabled

Verify that the Secret Manager API is listed in the list of enabled APIs.




## Configure roles and permissions

To get the permissions that you need to set up Secret Manager, ask your administrator to grant you the [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about the access control for Secret Manager, see [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control).

## What's next

  * Learn more about [authentication and access](https://docs.cloud.google.com/secret-manager/docs/authentication) to the Secret Manager API.
  * Learn more about [creating secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).
  * Learn more about [adding a secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
