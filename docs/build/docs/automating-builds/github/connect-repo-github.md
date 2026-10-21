---
url: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github/
title: Connect to a GitHub repository \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:05.434102+00:00
---

# Connect to a GitHub repository  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitHub repository Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to connect a [GitHub](https://docs.github.com/) repository to Cloud Build. To learn more about Cloud Build repositories, see [Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/github/connect-repo-github)



  * Have your source code ready in a GitHub repository.
  * Have either a `Dockerfile` or a [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config) in your GitHub source repository.
  * If you're initially connecting your repository to Cloud Build, make sure you have admin-level permissions on your repository. To learn more about GitHub repository permissions, see [Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization).
  * To use `gcloud` commands on this page, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.



## Connect to a GitHub host

###  Console 

To connect your GitHub repository to Cloud Build:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You see the **Repositories** page.

  2. In the project selector in the top bar, select your Google Cloud project.

  3. At the top of the page, select the **2nd gen** tab.

  4. Click **Create host connection** to connect a new host to Cloud Build.

  5. On the left panel, select **GitHub** as your source provider.

  6. In the **Configure Connection** section, enter the following information:

     * **Region** : Select a region for your connection.

**Note:** You must specify a region. Your connection cannot exist globally.
     * **Name** : Enter a name for your connection.

  7. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your GitHub repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

  8. Click **Connect**.

After you click the **Connect** button, you are asked to authorize the Cloud Build GitHub App to access your GitHub account. You may revoke access to the app by uninstalling or deleting the App from your host at any time.

Cloud Build requests authorization of your GitHub user account and stores the resulting authorization token as a secret in Secret Manager in your project. The authorization token is used to validate access of your user account for the installation of the Cloud Build GitHub App and to the repositories linked. The Cloud Build Service Agent account (`service-{projectNumber}@gcp-sa-cloudbuild.iam.gserviceaccount.com`) is used to access your secret. To view your secret, see [List secrets and view secret details](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

**Note:** This authentication can be used to create additional connections in the same project. We recommend using a robot account, or an account shared by your team, instead of a personal GitHub account to keep your connections secure.

After authorizing the Cloud Build GitHub App, you are redirected to the Cloud Build [**Repositories**](https://console.cloud.google.com/cloud-build/repositories) page.




###  gcloud 

To connect your GitHub host using `gcloud`, complete the following steps:

**Note:** The installation steps require actions in your web browser.

  1. Enter the following command to initiate a connection to your GitHub repository:
         
         gcloud builds connections create github CONNECTION_NAME --region=REGION
         

Where:

     * CONNECTION_NAME is a name for your connection as it will appear in Cloud Build.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

**Note:** You must specify a region. Your connection cannot exist globally.

After running the `gcloud builds connections` command, you see a link to authorize the Cloud Build GitHub App.

  2. Log into your `github.com` account.

**Note:** This authentication can be used to create additional connections in the same project. We recommend using a robot account, or an account shared by your team, instead of a personal GitHub account to keep your connections secure.
  3. Follow the link to authorize the Cloud Build GitHub App.

After authorizing the app, Cloud Build stores an authentication token as a secret in Secret Manager in your Google Cloud project. You can view your secrets on the **[Secret Manager](https://console.cloud.google.com/security/secret-manager)** page.

  4. Install the Cloud Build GitHub App in your account or in an organization you own.

Permit the installation using your GitHub account and select repository permissions when prompted.

  5. Verify the installation of your GitHub connection by running the following command:
         
         gcloud builds connections describe CONNECTION_NAME --region=REGION
         

Where:

     * CONNECTION_NAME is the name of your GitHub host connection in Cloud Build.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.

If the `installationState` field is set to `COMPLETE`, you have successfully installed the connection. Otherwise, the `installationState` field provides a link for additional steps required.




## Connect to a GitHub host programmatically

To connect to a GitHub host programmatically, you must first configure the authentication token for the connection, and then create the GitHub connection in Cloud Build.

### Configure an authentication token

To connect to a GitHub host programmatically, you must create a Cloud Build GitHub connection, including a secret for an authentication token. You can acquire an authentication token in two ways:

  * Create a personal access token in GitHub.

**Note:** Cloud Build doesn't support the use of GitHub fine-grained access tokens.
  * Use a token from an existing Cloud Build GitHub connection. This method is helpful if your GitHub account has restrictions preventing the creation of Personal Access Tokens. In addition, if you reference this token when creating a connection from a script, you don't need to manually authenticate the connection using a web browser.




###  Personal access token 

  1. Follow the steps to [create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) in the GitHub documentation.

  2. Select the following [OAuth scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) when prompted in GitHub:

     * `repo` to grant full access to public and private repositories.
     * `read:user` to grant access to read a user's profile data.
     * `read:org` for read-only access to organization membership and projects (if your app is installed in an organization).
**Note:** When your token expires, you'll need to delete the expired token and create a new one.
  3. Save the value of your personal access token. You'll use it in a later step.




###  Existing connection 

  1. Run the following the command in gcloud CLI:
         
         gcloud builds connections describe CONNECTION_NAME --region=REGION
         

Where:

     * CONNECTION_NAME is the name of your GitHub host connection.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger.
  2. In the command output, the value of the `authorizerTokenSecretVersion` is the ID of the secret containing the connection's authentication token. Copy this value and save it in a secure place. You'll use the generated token in the following steps.

**Note:** If you don't yet have a GitHub connection in Cloud Build but want to use a Cloud Build connection's authentication token, run `gcloud builds connections create github CONNECTION_NAME --region=REGION` to create one. You can then run `gcloud build connections describe` to retrieve that connection's secret and use it when creating a connection to GitHub in the following steps.



### Create the GitHub connection

Create a GitHub connection by using Terraform or the gcloud CLI.

###  Terraform 

You can connect your GitHub host to Cloud Build using the Google Terraform provider by completing the following steps:

  1. [Install the Cloud Build GitHub App](https://github.com/apps/google-cloud-build) on your GitHub account or in an organization you own.

  2. Configure your GitHub connection in Terraform. The following Terraform code sample shows shows a configuration that does the following:

     * Configures the Terraform Google provider

     * Creates a secret to store GitHub personal access tokens

     * Grants permissions to the Cloud Build Service Agent to access the secret

     * Creates a GitHub connection
    
    // Configure the terraform google provider
    terraform {
      required_providers {
        google = {}
        }
    }
    
    // Create a secret containing the personal access token and grant permissions to the Service Agent
    resource "google_secret_manager_secret" "github_token_secret" {
        project = PROJECT_ID
        secret_id = SECRET_ID
    
        replication {
            auto {}
        }
    }
    
    resource "google_secret_manager_secret_version" "github_token_secret_version" {
        secret = google_secret_manager_secret.github_token_secret.id
        secret_data = GITHUB_PAT
    }
    
    data "google_iam_policy" "serviceagent_secretAccessor" {
        binding {
            role = "roles/secretmanager.secretAccessor"
            members = ["serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"]
        }
    }
    
    resource "google_secret_manager_secret_iam_policy" "policy" {
      project = google_secret_manager_secret.github_token_secret.project
      secret_id = google_secret_manager_secret.github_token_secret.secret_id
      policy_data = data.google_iam_policy.serviceagent_secretAccessor.policy_data
    }
    
    // Create the GitHub connection
    resource "google_cloudbuildv2_connection" "my_connection" {
        project = PROJECT_ID
        location = REGION
        name = CONNECTION_NAME
    
        github_config {
            app_installation_id = INSTALLATION_ID
            authorizer_credential {
                oauth_token_secret_version = google_secret_manager_secret_version.github_token_secret_version.id
            }
        }
        depends_on = [google_secret_manager_secret_iam_policy.policy]
    }
    




Where:

  * PROJECT_NUMBER is your Google Cloud project number.
  * SECRET_ID is the ID of your GitHub personal access token or secret in Secret Manager.
  * GITHUB_PAT is the access token of the personal access token in GitHub.
  * PROJECT_ID is your Google Cloud project ID.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * CONNECTION_NAME is a name for your connection as it will appear in Cloud Build.
  * INSTALLATION_ID is the installation ID of your Cloud Build GitHub app. Your installation ID can be found in the URL of your Cloud Build GitHub App. In the following URL, `https://github.com/settings/installations/1234567`, the installation ID is the numerical value `1234567`.



###  gcloud 

To connect your GitHub host to Cloud Build, do the following:

  1. [Install the Cloud Build GitHub App](https://github.com/apps/google-cloud-build) on your GitHub account or in an organization you own.

  2. Optional. If you're using a GitHub personal access token for authentication, run the following command to store the token in Secret Manager in your Google Cloud project:
         
         echo -n 'TOKEN' | gcloud secrets create SECRET_NAME --data-file=-
         

  3. Grant access to the Cloud Build Service Agent on the secret, where SECRET_NAME is the name of your secret as stored in Secret Manager:
         
         PROJECT_ID=$(gcloud config list --format="value(core.project)")
         PN=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
         CLOUD_BUILD_SERVICE_AGENT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud secrets add-iam-policy-binding SECRET_NAME \
           --member="serviceAccount:${CLOUD_BUILD_SERVICE_AGENT}" \
           --role="roles/secretmanager.secretAccessor"
         

  4. Create your GitHub connection:
         
         gcloud builds connections create github CONNECTION_NAME \
           --authorizer-token-secret-version=projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION  \
           --app-installation-id=INSTALLATION_ID --region=REGION
         

Where:

     * CONNECTION_NAME is a name of your GitHub host connection in Cloud Build.
     * PROJECT_ID is your Google Cloud project ID.
     * SECRET_NAME is the name of your secret as stored in Secret Manager.
     * VERSION is the version of your secret.
     * INSTALLATION_ID is the installation ID of your GitHub app. Your installation ID can be found in the URL of your Cloud Build GitHub App. In the following URL, `https://github.com/settings/installations/1234567`, the installation ID is the numerical value `1234567`.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for of your connection.



## Connect a GitHub repository

###  Console 

To connect a GitHub repository to a host connection, complete the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You see the **Repositories** page.

  2. At the top of the page, select the **2nd gen** tab.

  3. Click **Link Repositories** to link repositories from your connection.

You see the **Connect Repositories** panel.

  4. In the **Connect Repositories** panel, enter the following information:

     1. **Connection** : Select a connection from the drop-down menu.
     2. **Repository** : Select a repository to link to your connection.

     3. **Repository Name** : Enter a name for your repository.

        1. **Generated** : Select this option for Cloud Build to automatically generated repository names on your behalf for selected repositories.
        2. **Manual** : Select this option to manually specify names for your selected repositories.

If you select **Manual** , you can modify the names for your selected repositories in the **Repository names** section.

  5. Click **Link** to link your repository to your connection.




###  gcloud 

To add a GitHub repository to your connection, enter the following command:
    
    
       gcloud builds repositories create REPO_NAME \
         --remote-uri=REPO_URI \
         --connection=CONNECTION_NAME --region=REGION
    

Where:

  * REPO_NAME is the name of your repository.
  * REPO_URI is the link to your GitHub repository. For example, `https://github.com/cloud-build/test-repo.git`.
  * CONNECTION_NAME is the name given to the GitHub Enterprise host connection created in Cloud Build from [Connect to a GitHub host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github#connecting_a_github_host).
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.



###  Terraform 

To add a GitHub repository to your connection, add the following code snippet to your Terraform configuration:
    
    
        resource "google_cloudbuildv2_repository" "my_repository" {
          project = "PROJECT_ID"
          location = "REGION"
          name = "REPO_NAME"
          parent_connection = google_cloudbuildv2_connection.my_connection.name
          remote_uri = "URI"
      }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * REPO_NAME is the name of your GitHub repository.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * URI is the host URI of your repository. For example, `https://github.com/myuser/myrepo.git`.



## What's next

  * Learn how to [build repositories from GitHub](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).
  * Learn how to [specify additional repositories](https://docs.cloud.google.com/build/docs/building/manage-dependencies) as dependencies to your build.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
