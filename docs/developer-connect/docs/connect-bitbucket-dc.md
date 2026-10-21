---
url: https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-dc/
title: Connect to Bitbucket Data Center \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:27:11.674388+00:00
---

# Connect to Bitbucket Data Center  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-dc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

#  Connect to Bitbucket Data Center Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create connections to Bitbucket Data Center and create links to Bitbucket Data Center repositories. You can complete these tasks using the Google Cloud console, or the Google Cloud CLI. 

These instructions are for application developers, platform administrators, and security managers who want to use Bitbucket Data Center source code repositories with Google. Specifically, you can use Bitbucket Data Center repositories with [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).

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

  8. Ensure that you have access to an account on [Bitbucket Data Center.](https://bitbucket.org/)

To help keep your team's work secure, we recommend that you complete the tasks in this guide using a bot account or an account shared by your team, not a personal account.

  9. Ensure that you own a Bitbucket Data Center repository, or have admin-level permissions on a shared repository. 
  10. Optional: Create a [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/create-key) (CMEK) for encrypting the authentication secrets that Developer Connect creates.
  11. Optional: To use the command-line instructions in this guide, complete the following steps: 
     1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
     2. Create a [Developer Connect service account](https://docs.cloud.google.com/developer-connect/docs/access-control#sa) by running the following command, where PROJECT_ID is your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects): 
            
            gcloud beta services identity create \
                        --service=developerconnect.googleapis.com \
                        --project=PROJECT_ID
                    




### Required roles

To get the permissions that you need to create connections and links, ask your administrator to grant you the following IAM roles: 

  * If you aren't the project owner: [Developer Connect Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.admin) (`roles/developerconnect.admin`) on your user account. 
  * If you plan to use a CMEK to encrypt the secrets that Developer Connect creates: [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the Secret Manager Service Account. 
  * If you plan to use the gcloud CLI to complete the steps in this guide: [Secret Manager Admin role ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the Developer Connect Service Account. 
  * If you plan to use the Google Cloud console to complete the steps in this guide: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on your user account. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** When you have the Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role, the Google Cloud console can automatically grant necessary permissions on your behalf. If your administrator won't allow you to have the Project IAM Admin role, then ask your administrator to grant Secret Manager Admin (`roles/secretmanager.admin`) on the Developer Connect Service Account (`service-{projectNumber}@gcp-sa-devconnect.iam.gserviceaccount.com`). 

## Create access tokens

Create personal access tokens in Bitbucket Data Center by completing the following steps:

  1. [Sign in to Bitbucket Data Center](https://bitbucket.org/).

  2. Follow the instructions in the Bitbucket Data Center documentation to [create two HTTP access tokens](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html) and grant the following scopes.

Developer Connect supports user, project, and repository access tokens.

     * Create one token with the `repository admin` scope. In Developer Connect, this token is called the _admin access token_.
     * Create one token with the `repository read` scope. In Developer Connect, this token is called the _read access token_.

You are responsible for managing Bitbucket Data Center token lifetimes in Bitbucket Data Center. To help protect your source code, you can set an expiry date during token creation. If you don't set an expiry date, then the token remains valid until you revoke it in Bitbucket Data Center.

  3. Copy the access tokens for use in the following procedures.




## Create a connection

This section describes how to create a connection between Developer Connect and Bitbucket Data Center. If you're using the Google Cloud console, then you can also start adding links to repositories as you finish setting up your connection.

To create a new Bitbucket Data Center connection, select one of the following options:

###  Console 

Initiate a connection by completing the following steps:

  1. In the Google Cloud console, open **Developer Connect**.

[Go to Developer Connect](https://console.cloud.google.com/developer-connect/connections)

Developer Connect displays the **Git repositories** page.

     * **If you see a list of source code management providers:** Start configuring your first connection by selecting a source code management provider. Click **Connect** on the Bitbucket Data Center card.
     * **If you see a table listing existing connections** : Set the source code management provider by clicking **Create connection** > **Bitbucket Data Center**.

The **Create Connection** page opens.

  2. For **Region** , choose a [region](https://docs.cloud.google.com/developer-connect/docs/locations) for your connection resources.

     1. For **Name** , enter a name for your new connection.
  3. For **Host URL** , enter the URL for the Bitbucket Data Center host you want to connect to.

  4. In the **Access Tokens** section, enter your Bitbucket Data Center access tokens:

     * **Admin access token** : Enter the token with the repository admin scope access.

     * **Read access token** : Enter the token with the repository read scope access.

  5. Click **Show more** to see optional configuration settings.

     1. Optional: By default, Developer Connect can act as a proxy for Git calls to Bitbucket Data Center. To disable this option, clear the **Enable Developer Connect proxy** checkbox.

     2. Optional: In the **Encryption** section, select a [CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Developer Connect creates.

  6. Click the **Continue** button. Developer Connect creates your connection. This process can take a few seconds.




Once the connection is created, the **Link repositories** page appears.

Complete the following steps to link repositories to your connection:

  1. In the list of available repositories, select the repositories you want to use.

  2. Click **OK**.

  3. Click **Link**.




Your connection is added to the **Connections** page and your repository links are added to the **Repositories** page in the Google Cloud console. You can add more links to existing connections at any time.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

###  gcloud 

  1. Create a webhook secret in Secret Manager by running the following command, where WEBHOOK_SECRET_NAME is a name for your webhook secret:
         
         cat /proc/sys/kernel/random/uuid | tr -d '\n' | gcloud secrets create WEBHOOK_SECRET_NAME
         

  2. Store your access tokens in Secret Manager by running the following commands:
         
         gcloud secrets create ADMIN_SECRET_NAME
         
         echo -n ADMIN_SECRET_DATA | gcloud secrets versions add ADMIN_SECRET_NAME --data-file=-
         
         gcloud secrets create READ_SECRET_NAME
         
         echo -n READ_SECRET_DATA | gcloud secrets versions add READ_SECRET_NAME --data-file=-
         

Replace the following:

     * ADMIN_SECRET_NAME: a name for the secret that stores your admin access token.
     * ADMIN_SECRET_DATA: your admin access token.
     * READ_SECRET_NAME: a name for the secret that stores your read access token.
     * READ_SECRET_DATA: your read access token.
  3. Run the [`gcloud developer-connect connections create`](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create) command to create a connection to Bitbucket Data Center:
         
         gcloud developer-connect connections create CONNECTION_NAME \
             --location=REGION \
             --bitbucket-data-center-config-host-uri=HOST_URI \
             --bitbucket-data-center-config-authorizer-credential-user-token-secret-version=projects/PROJECT_ID/secrets/ADMIN_SECRET_NAME/versions/VERSION \
             --bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version=projects/PROJECT_ID/secrets/READ_SECRET_NAME/versions/VERSION \
             --bitbucket-data-center-config-webhook-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET_NAME/versions/VERSION \
             --git-proxy-config-enabled
         

Replace the following:

     * CONNECTION_NAME: a name for your connection.
     * REGION: the [region](https://docs.cloud.google.com/developer-connect/docs/locations) to use for your connection.
     * HOST_URI: the [URI of your Bitbucket Data Center host](https://confluence.atlassian.com/bitbucketserver/specify-the-bitbucket-base-url-776640392.html) including the `https://` prefix.
     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
     * ADMIN_SECRET_NAME: the name of the Secret Manager secret that contains your admin access token.
     * READ_SECRET_NAME: the name of the Secret Manager secret that contains your read access token.
     * WEBHOOK_SECRET_NAME: the name of the Secret Manager secret that contains your webhook secret.
     * VERSION: the version number of each secret. This can be `latest` to use the most recent version number.
     * `--git-proxy-config-enabled`: an optional flag that enables Developer Connect to act as a proxy for Git calls to Bitbucket Data Center. This capability is in [Preview](https://cloud.google.com/products/#product-launch-stages).

Developer Connect completes the connection to Bitbucket Data Center. Next, link to repositories.




## Link to repositories using an existing connection

Once you have established a connection to Bitbucket Data Center, you can link to repositories. You can repeat these steps later to link additional repositories as needed.

To create repository links on an existing Bitbucket Data Center connection, select one of the following options:

###  Console 

Create links to repositories by completing the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the **Repositories** page](https://console.cloud.google.com/developer-connect/git-repository-links)

  2. Click **Link repository**.

The **Link Git repositories** pane opens.

  3. In the connections list, choose a connection.

  4. Click **Continue**.

  5. In the repositories list, select the repositories you want to link to.

Developer Connect displays suggested names for your repository resources.

  6. Select a repository resource naming option:

     * **Generated** : Use the generated repository resource names.
     * **Manual** : Input names of your own.
  7. Click **Create**.

Developer Connect creates the repository links and displays them in the Google Cloud console.




###  gcloud 

Create a link to your Bitbucket Data Center repository by running the following command:
    
    
    gcloud developer-connect connections git-repository-links create REPO_NAME \
        --clone-uri=REPO_URI \
        --connection=CONNECTION_NAME \
        --location=REGION
    

Replace the following:

  * REPO_NAME: a name for the new link between Developer Connect and your Bitbucket Data Center repository.
  * REPO_URI: the URL of your repository in Bitbucket Data Center, including the `https://` prefix and the `.git` suffix.
  * CONNECTION_NAME: the name of your connection to Bitbucket Data Center.
  * REGION: the region of your connection.



Developer Connect creates the repository links.

To list linked repositories, run the [`developer-connect connections git-repository-linkslist`](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect/connections/git-repository-links/list) command.

If you're setting up Gemini Code Assist, continue the process by following the steps in [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

## What's next

  * [Finish setting up Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).
  * [Learn how Gemini Code Assist helps you accelerate software development](https://docs.cloud.google.com/gemini/docs/codeassist/overview).
  * [Explore other integrations available through Developer Connect.](https://docs.cloud.google.com/developer-connect/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
