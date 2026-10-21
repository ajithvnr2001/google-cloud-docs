---
url: https://docs.cloud.google.com/developer-connect/docs/connect-repo/
title: Quickstart: Connect a source code repository \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:27:09.863586+00:00
---

# Quickstart: Connect a source code repository  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/connect-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect a source code repository

Developer Connect lets you integrate with non-Google products and services so you can use them in supported Google products.

This quickstart shows you how to connect to [GitHub](https://docs.github.com/) using a [Git repository connection](https://docs.cloud.google.com/developer-connect/docs/git-repo-connections). This type of connection is required for when you want to use [Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).

For a list of all the integrations that Developer Connect supports, see [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Developer Connect Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Developer Connect and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Developer Connect Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  10. Make sure that you have a GitHub account and access to a repository hosted on GitHub.com. Or, follow the GitHub documentation to create new ones:
     * [Create a GitHub account](https://github.com/signup)
     * [Create a repository on GitHub.com](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)
  11. If you're using an existing repository and you aren't the owner, ask the owner to grant admin-level permissions to the repository. If the repository is in a GitHub organization, request admin-level permissions from the organization owner. To learn more about GitHub organizations, see [GitHub account types](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts).



## Initiate a connection

  1. Open the **Developer Connect** page in the Google Cloud console.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect)

The **Git Repositories** page opens, displaying a list of source code management providers.

  2. Select a source code management provider by clicking **Connect** on the card for that provider.

The **Create connection** page opens.

  3. Choose `us-central1` as the region.

  4. Enter `quickstart-connection` as the name.

  5. Click **Continue**.

The **Google Developer Connect** dialog appears requesting authorization to use your GitHub OAuth token.

If you don't see a dialog, turn off any pop-up blocking browser plug-ins and makes sure that your browser settings allow pop-ups. For example, in Chrome, follow the instructions to [allow pop-ups](https://support.google.com/chrome/answer/95472).

  6. Click **I understand and continue**.

  7. Complete the GitHub account sign-in steps if prompted to do so.

  8. Click **Authorize Developer Connect** if prompted to do so. If you don't see this prompt, authorization has already been granted on this account.




## Configure the connection

Grant permissions on your GitHub account and repositories using the following steps. The prompts depend on whether someone using the GitHub account has already installed the **Google Developer Connect** app in GitHub.

  * **If you see a list of GitHub accounts:** You don't have the app installed yet. Install and configure it by following these steps:

    1. Choose the GitHub account that has access to the repository you want to link.

    2. Specify GitHub repository permissions and install the app. For more information, see the GitHub instructions on [installing apps](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party#installing-a-github-app).

  * **If you see a prompt to re-use an existing installation:** Choose where to install and configure the app by following these steps:

    1. Click **GitHub Account** to see accounts that have the app installed. If you see the account you want to use, choose it.

       1. Click **Confirm**.
    2. If you don't see the account that you want to use, choose **Install the GitHub App on another GitHub account**.

       1. Click **Confirm**.

       2. Choose the GitHub account you want to use.

       3. Specify GitHub repository permissions and install the app. For more information, see the GitHub instructions on [installing apps](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party#installing-a-github-app).



  1. In **Repositories** , choose the repository you want to link.

  2. Click **Link**.




The connection is added to the connections list, and the linked repository is added to the repository list.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Developer Connect** page.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect)

  2. In the **Repositories** tab, in the row containing the name of the linked repository, click more_vert **More options**.

  3. Choose **Unlink**.

  4. Click **Confirm**.

  5. Click the **Connections** tab.

  6. In the row containing the name of your connection, click more_vert **More options**.

  7. Choose **Delete**.

  8. Enter the name of your connection.

  9. Click **Confirm**.




Deleting connections and links doesn't delete the repositories on GitHub.com. If you created a new GitHub repository for this quickstart and you want to delete the repository, follow the GitHub instructions to [delete a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository).

If you want to uninstall the Google Developer Connect app, follow the GitHub instructions on [modifying installed apps](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).

## What's next

  * [Learn about Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).
  * [Build apps in Firebase App Hosting using GitHub repositories](https://firebase.google.com/docs/app-hosting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
