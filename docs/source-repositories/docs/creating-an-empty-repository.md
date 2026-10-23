---
url: https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository/
title: Creating an empty repository \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:55.569212+00:00
---

# Creating an empty repository  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/creating-an-empty-repository/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Creating an empty repository Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Source Repositories to create a new, empty repository. Creating a repository is useful when you want to start a project or back up a Git repository using Cloud Source Repositories.

## Before you begin

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

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. [ Verify that you have the latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
  10. If you have not configured your user credentials in Git, follow the [ first time setup instructions.](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
  11. Enable the Cloud Source Repositories API.

[ Enable the Cloud Source Repositories API](https://console.cloud.google.com/apis/enableflow?apiid=sourcerepo.googleapis.com&redirect=https://cloud.google.com/source-repositories/docs/creating-an-empty-repository)




## Create a new repository

You can create a repository by using either the Google Cloud console or the `gcloud` command-line tool.

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories.

[ Open Cloud Source Repositories](https://source.cloud.google.com/repos)

  2. Click **Add repository**.

The **Add a repository** page opens.

  3. Select **Create new repository** and click **Continue**.

The **Create new repository** page opens.

  4. In the **Repository name** field, type a name for the new repository. Note that the names `All-Users` and `All-Projects` are restricted names and cannot be used.

  5. In the **Project** drop-down list, select the Google Cloud project the repository belongs to.

To create a new Google Cloud project, click **Create project**.

  6. Click **Create**.

Your repository is created, and the **Add code to your repository** page opens. This page provides instructions on how to [clone the repository to your local machine](https://docs.cloud.google.com/source-repositories/docs/cloning-repositories) or [push code from an existing repository](https://docs.cloud.google.com/source-repositories/docs/pushing-code-from-a-repository) based on your authentication type.




###  gcloud 

  1. From the command line, call:
         
         gcloud init
         gcloud source repos create [REPO_NAME]
         

Where `[REPO_NAME]` is the name for your repository. Note that the names `All-Users` and `All-Projects` are restricted names and cannot be used.




## Create a project

All repositories must belong to a Google Cloud project. If you don't have a Google Cloud project, you can create one by following these steps.

  1. On the **Create new repository** page, click **Create project**.

The **Create Cloud project** dialog opens.

  2. In the **Project name** field, type a name for the Google Cloud project.

  3. In the **Project ID** field, either accept the generated project ID or click **Edit Project ID** to enter a different one.

**Note:** Your Google Cloud project ID must be unique across Google Cloud.
  4. In the **Billing Account** drop-down list, select a billing account.

To create a billing account, click **Create billing account**.

  5. Click **Create**.




You can continue creating a new repository.

## What's next

Now that you have a repository in Cloud Source Repositories, you can now add your code, which might involve either of these processes:

  * [Cloning your new repository](https://docs.cloud.google.com/source-repositories/docs/cloning-repositories) to your local machine.
  * [Pushing code from an existing repository](https://docs.cloud.google.com/source-repositories/docs/pushing-code-from-a-repository) on your local machine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
