---
url: https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise/
title: Connect to GitHub Enterprise \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:54.111096+00:00
---

# Connect to GitHub Enterprise  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Connect to GitHub Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create connections to GitHub Enterprise and create links to GitHub Enterprise repositories. You can complete these tasks using the Google Cloud console, or the Google Cloud CLI. 

These instructions are for application developers, platform administrators, and security managers who want to use GitHub Enterprise source code repositories with Google. Specifically, you can use GitHub Enterprise repositories with [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).

To learn more about Developer Connect, see [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Developer Connect, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Developer Connect, Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com,secretmanager.googleapis.com)

  8. Ensure that you have access to an account on [GitHub Enterprise.](https://github.com)

To help keep your team's work secure, we recommend that you complete the tasks in this guide using a bot account or an account shared by your team, not a personal account.

  9. Ensure that you own a GitHub Enterprise repository, or have admin-level permissions on a shared repository. 
  10. When using a repository in a GitHub Enterprise organization, ensure that you have [GitHub App Manager](https://docs.github.com/en/enterprise-server@3.14/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#github-app-managers) permissions.

  11. Optional: Create a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/create-key) (CMEK) for encrypting the authentication secrets that Developer Connect creates.
  12. Optional: To use the command-line instructions in this guide, complete the following steps: 
     1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
     2. Create a [Developer Connect service account](https://docs.cloud.google.com/developer-connect/docs/access-control#sa) by running the following command, where PROJECT_ID is your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects): 
            
            gcloud beta services identity create \
                        --service=developerconnect.googleapis.com \
                        --project=PROJECT_ID
                    




## Grant the required IAM permissions

To get the permissions that you need to create connections and links, ask your administrator to grant you the following IAM roles: 

  * If you aren't the project owner: [Developer Connect Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin) (`roles/developerconnect.admin`) on your user account. 
  * If you plan to use a CMEK to encrypt the secrets that Developer Connect creates: [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the Secret Manager Service Account. 
  * If you plan to use the gcloud CLI to complete the steps in this guide: [Secret Manager Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the Developer Connect Service Account. 
  * If you plan to use the Google Cloud console to complete the steps in this guide: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on your user account. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** When you have the Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role, the Google Cloud console can automatically grant necessary permissions on your behalf. If your administrator won't allow you to have the Project IAM Admin role, then ask your administrator to grant Secret Manager Admin (`roles/secretmanager.admin`) on the Developer Connect Service Account (`service-{projectNumber}@gcp-sa-devconnect.iam.gserviceaccount.com`). 

## Create a connection

This section describes how to create a connection between Developer Connect and GitHub Enterprise. If you're using the Google Cloud console, then you can also start adding links to repositories as you finish setting up your connection.

To create a new GitHub Enterprise connection, select one of the following options:

###  Console 

Initiate a connection by completing the following steps:

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

Developer Connect displays the **Git repositories** page.

     * **If you see a list of source code management providers:** Start configuring your first connection by selecting a source code management provider. Click **Connect** on the GitHub Enterprise card.
     * **If you see a table listing existing connections** : Set the source code management provider by clicking **Create connection** > **GitHub Enterprise**.

The **Create Connection** page opens.

  2. For **Region** , choose a [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection resources.

     1. For **Name** , enter a name for your new connection.
  3. Activate the **Enable a data residency compliant connection** checkbox to make this connection compliant with [data residency requirements](https://docs.cloud.google.com/developer-connect/docs/data-residency).

GitHub connections created using the Google Cloud console are data-residency compliant if you activate this checkbox when you create the connection. When you do this, Developer Connect [creates a GitHub app](https://docs.cloud.google.com/developer-connect/docs/data-residency)

When you create a GitHub connections using Google Cloud CLI, those connections are not data-residency compliant. All other connection types are data-residency compliant.

     1. For **Host URL** , enter the URL of the host you want to connect to.
  4. Click **Show more** to see optional configuration settings.

     1. Optional: By default, Developer Connect can act as a proxy for Git calls to GitHub Enterprise. To disable this option, clear the **Enable Developer Connect proxy** checkbox.

     2. For **Network type** , select **Public internet**.

If you want to use a private network, see [Connect to GitHub Enterprise repositories hosted in a private network](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise-private).

     3. Optional: In the **Encryption** section, select a [CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Developer Connect creates.

  5. Click **Continue**.

A GitHub dialog appears, inviting you to create a GitHub app.

  6. Following the prompts in GitHub, complete these tasks:

     1. Input a name for your app.

     2. Choose the organization where you want to install the app.

     3. Select the repositories you want to grant access to.

The dialog closes.

Developer Connect fetches your private key from GitHub and stores it in your Google Cloud project as a Secret Manager secret. To view your secrets, [list secrets in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).




Once the connection is created, the **Link repositories** page appears.

Complete the following steps to link repositories to your connection:

  1. In the list of available repositories, select the repositories you want to use.

  2. Click **OK**.

  3. Click **Link**.




Your connection is added to the **Connections** page and your repository links are added to the **Repositories** page in the Google Cloud console. You can add more links to existing connections at any time.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

###  gcloud 

The following tasks require some actions in your web browser.

Initiate a connection by completing the following steps:

  1. Run the [`gcloud developer-connect connections create`](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create) command to create a connection to GitHub Enterprise:
         
         gcloud developer-connect connections create CONNECTION_NAME \
             --location=REGION \
             --github-enterprise-config-host-uri=HOST_URI \
             --git-proxy-config-enabled
         

Replace the following:

     * CONNECTION_NAME: the name for your connection.
     * REGION: the [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection.
     * HOST_URI: the URI for the host you want to connect to.
     * `--git-proxy-config-enabled`: an optional flag that enables Developer Connect to act as a proxy for Git calls to GitHub Enterprise. This capability is in [Preview](https://cloud.google.com/products/#product-launch-stages).
  2. You must create a GitHub app to manage connections with GitHub. Run the following command to get URI for app setup:
         
         gcloud developer-connect connections describe CONNECTION_NAME \
             --location=REGION
         

Replace the following:

     * CONNECTION_NAME: the name for your connection.
     * REGION: the [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection.

Developer Connect returns a link to complete the next steps in a browser window. Copy this link.

  3. Open the link in a web browser.

  4. Sign in to your GitHub account if prompted to do so.

  5. Following the prompts in GitHub, complete these tasks:

     1. Input a name for your app.

     2. Choose the organization where you want to install the app.

     3. Select the repositories you want to grant access to.

The dialog closes.

Developer Connect fetches your private key from GitHub and stores it in your Google Cloud project as a Secret Manager secret. To view your secrets, [list secrets in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).




### Verify the connection

Verify the creation of your GitHub connection by running the following command:
    
    
    gcloud developer-connect connections describe CONNECTION_NAME \
        --location=REGION
    

Where:

  * CONNECTION_NAME: the name of your connection.
  * REGION: the region for your connection.



Developer Connect returns a status in the `installationState` field. If the value of this field is `COMPLETE`, your app installation is done. Otherwise, Developer Connect returns a URI to return you to configuration in the browser.

Once your connection is completed, choose which repositories to link by following the instructions in [Link to repositories](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#gcloud_1).

## Add repository links to existing connections

Once you have established a connection to GitHub Enterprise, you can link to repositories. You can repeat these steps later to link additional repositories as needed.

To create repository links on an existing GitHub Enterprise connection, select one of the following options:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the **Repositories** page](https://console.cloud.google.com/developer-connect/git-repository-links)

  2. Click **Link repository**.

The **Link Git repositories** pane opens.

  3. In the connections list, choose a connection.

  4. Click **Continue**.

  5. In the repositories list, select the repositories you want to link to.

  6. Click **Create**.




Developer Connect creates the repository links and displays them in the Google Cloud console.

###  gcloud 

Run the following command:
    
    
    gcloud developer-connect connections git-repository-links create REPO_NAME \
        --clone-uri=REPO_URI \
        --connection=CONNECTION_NAME \
        --location=REGION
    

Replace the following:

  * REPO_NAME: a name for your repository link.
  * REPO_URI: the link to your repository. For example, `https://github.com/cloud-build/test-repo.git`.
  * CONNECTION_NAME: the name of your connection.
  * REGION: the [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection.



Developer Connect creates the repository links.

To list linked repositories, run the [`developer-connect connections git-repository-links list`](https://docs.cloud.google.com/gcloud/reference/developer-connect/connections/git-repository-links/list) command.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

## Data sharing

Content from Google Cloud resources linked to this connection might be transferred to GitHub. This statement applies to all existing and future resources utilizing this connection. To stop sharing information with GitHub, delete Developer Connect connections in the Google Cloud console or gcloud CLI, and [revoke access in GitHub](https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps).

## What's next

  * [Finish setting up Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).
  * [Learn how Gemini Code Assist helps you accelerate software development](https://docs.cloud.google.com/gemini/docs/codeassist/overview).
  * [Explore other integrations available through Developer Connect.](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
