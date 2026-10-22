---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud/
title: Connect to a Bitbucket Cloud host \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:09.957152+00:00
---

# Connect to a Bitbucket Cloud host  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a Bitbucket Cloud host Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect a [Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/) host to Cloud Build.

## Before you begin

  * Enable the Cloud Build, Secret Manager, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,compute.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center)



  * Ensure that the source code is in a Bitbucket Cloud repository.
  * Ensure that the Bitbucket Cloud source repository has either a `Dockerfile` or a [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config).
  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) to use `gcloud` commands.



## Required IAM permissions

To ensure that has the necessary permissions to connect, ask your administrator to grant the Cloud Build Connection Admin (`cloudbuild.connectionAdmin`) IAM role to on your user account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create Bitbucket Cloud access tokens

Create the following two access tokens in Bitbucket Cloud:

  * Admin access token - for connecting and disconnecting repositories.
  * Read access token - to allow Cloud Build to access your source code.



To create these tokens, follow these steps:

  1. Sign in to [Bitbucket Cloud](https://bitbucket.org).

  2. Follow the Bitbucket Cloud instructions to create access tokens linked to your [repository](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/), [project](https://support.atlassian.com/bitbucket-cloud/docs/project-access-tokens/), or [workspace](https://support.atlassian.com/bitbucket-cloud/docs/workspace-access-tokens/).

Grant the following permissions:

     * Admin access token:

       * Repositories: **Read** and **Admin**
       * Pull Requests: **Read**
       * Webhooks: **Read** and **Write**
     * Read access token:

       * Repositories: **Read**
**Note:** some token types are only available in Bitbucket Premium. Learn more about [tokens in Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/).
  3. Copy your tokens for use in the following procedures.




## Connect to a Bitbucket Cloud host

###  Console 

Connect Cloud Build to your Bitbucket Cloud host by completing the following steps:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You will see the **Repositories** page.

  2. In the project selector, select your Google Cloud project.

  3. At the top of the page, select the **2nd gen** tab.

  4. Click **Create host connection** to connect a new host to Cloud Build.

  5. On the left panel, select **Bitbucket** as your source provider.

  6. In the **Configure Connection** section, enter the following information:

     * **Region** : Select a region for your connection.

**Note:** You must specify a region. Your connection cannot exist globally.
     * **Name** : Enter a name for your connection.

  7. In the **Host details** section, enter the following information:

     * Select **Bitbucket Cloud** as your host type.

     * **Workspace** : Enter the [workspace ID](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/) for your Bitbucket Cloud repository.

  8. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your Bitbucket Cloud repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

  9. In the **Access tokens** section, enter the following:

     * **Admin access token** : Enter your admin access token [created previously](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#tokens).

     * **Read access token** : Enter your read access token [created previously](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#tokens).

  10. Click **Connect**.

The new connection appears in the **Repositories** page.




###  gcloud 

  1. Complete the following steps to store your credentials:

     1. Store your access tokens in Secret Manager in your Google Cloud project by running the following commands:
            
            echo -n ADMIN_TOKEN | gcloud secrets create ADMIN_SECRET_NAME --data-file=-
            
            echo -n READ_TOKEN | gcloud secrets create READ_SECRET_NAME --data-file=-
            

Where:

        * ADMIN_TOKEN is your admin access token.
        * ADMIN_SECRET_NAME is the name you want to give to your admin access token secret in Secret Manager.
        * READ_TOKEN is your read access token.
        * READ_SECRET_NAME is the name you want to give to your read access token secret in Secret Manager.
     2. [Create a webhook secret in Secret Manager](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events) by running the following command, where WEBHOOK_SECRET_NAME is the name you want to give to your webhook secret:
            
            echo -n ${ex.(random-uuid)} | gcloud secrets create WEBHOOK_SECRET_NAME --data-file=-
            

     3. If your secrets aren't all in the same project, grant access to your Cloud Build service agent by running the following:
            
            PN=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
            CLOUD_BUILD_SERVICE_ACCOUNT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
            gcloud secrets add-iam-policy-binding ADMIN_SECRET_NAME \
                --member="serviceAccount:${CLOUD_BUILD_SERVICE_ACCOUNT}" \
                --role="roles/secretmanager.secretAccessor"
            
            gcloud secrets add-iam-policy-binding READ_SECRET_NAME \
                --member="serviceAccount:${CLOUD_BUILD_SERVICE_ACCOUNT}" \
                --role="roles/secretmanager.secretAccessor"
            
            gcloud secrets add-iam-policy-binding WEBHOOK_SECRET_NAME \
                --member="serviceAccount:${CLOUD_BUILD_SERVICE_ACCOUNT}" \
                --role="roles/secretmanager.secretAccessor"
            

Where:

        * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project). 
        * ADMIN_SECRET_NAME is the name of your admin token secret. 
        * READ_SECRET_NAME is the name of your read token secret.
        * WEBHOOK_SECRET_NAME is the name of your webhook secret.
  2. Connect Cloud Build to your Bitbucket Cloud host by using the following command:
         
         gcloud builds connections create bitbucket-cloud CONNECTION_NAME \
             --workspace=WORKSPACE_ID \
             --project=PROJECT_ID \
             --region=REGION \
             --authorizer-token-secret-version=projects/PROJECT_ID/secrets/ADMIN_SECRET_NAME/versions/latest \
             --read-authorizer-token-secret-version=projects/PROJECT_ID/secrets/READ_SECRET_NAME/versions/latest \
             --webhook-secret-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET_NAME/versions/1
         

Where:

     * CONNECTION_NAME is the name you want to give to the connection to your Bitbucket Cloud host.
     * WORKSPACE_ID is the Workspace ID for your Bitbucket Cloud repository.
     * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your host connection. 
     * ADMIN_SECRET_NAME is the name of your admin token secret. 
     * READ_SECRET_NAME is the name of your read access token secret.
     * WEBHOOK_SECRET_NAME is the name of your webhook secret.



###  Terraform 

You can connect your Bitbucket Cloud host to Cloud Build using Terraform.

In the following example, the code snippet does the following:

  * Configures the Terraform Google provider.
  * Creates a Secret Manager secret to store the Bitbucket tokens.
  * Grants necessary permissions to the Cloud Build service agent to access secrets.
  * Creates a Bitbucket Cloud connection.
        
        // Configure the Terraform Google provider
        terraform {
          required_providers {
            google = {}
          }
        }
        
        provider "google" {
          project = "PROJECT_ID"
          region = "REGION"
        }
        
        // Create secrets and grant permissions to the Cloud Build service agent
        resource "google_secret_manager_secret" "admin-token-secret" {
            project = "PROJECT_ID"
            secret_id = "ADMIN_TOKEN_NAME"
        
            replication {
                auto {}
            }
        }
        
        resource "google_secret_manager_secret_version" "admin-token-secret-version" {
            secret = google_secret_manager_secret.admin-token-secret.id
            secret_data = "ADMIN_TOKEN_VALUE"
        }
        
        resource "google_secret_manager_secret" "read-token-secret" {
            project = "PROJECT_ID"
            secret_id = "READ_TOKEN_NAME"
        
            replication {
                auto {}
            }
        }
        
        resource "google_secret_manager_secret_version" "read-token-secret-version" {
            secret = google_secret_manager_secret.read-token-secret.id
            secret_data = "READ_TOKEN_VALUE"
        }
        
        resource "google_secret_manager_secret" "webhook-secret-secret" {
            project = "PROJECT_ID"
            secret_id = "WEBHOOK_SECRET_NAME"
        
            replication {
                auto {}
            }
        }
        
        resource "google_secret_manager_secret_version" "webhook-secret-secret-version" {
            secret = google_secret_manager_secret.webhook-secret-secret.id
            secret_data = "WEBHOOK_SECRET_VALUE"
        }
        
        data "google_iam_policy" "p4sa-secretAccessor" {
            binding {
                role = "roles/secretmanager.secretAccessor"
                members = ["serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"]
            }
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-pak" {
          project = google_secret_manager_secret.admin-token-secret.project
          secret_id = google_secret_manager_secret.admin-token-secret.secret_id
          policy_data = data.google_iam_policy.p4sa-secretAccessor.policy_data
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-rpak" {
          project = google_secret_manager_secret.read-token-secret.project
          secret_id = google_secret_manager_secret.read-token-secret.secret_id
          policy_data = data.google_iam_policy.p4sa-secretAccessor.policy_data
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-whs" {
          project = google_secret_manager_secret.webhook-secret-secret.project
          secret_id = google_secret_manager_secret.webhook-secret-secret.secret_id
          policy_data = data.google_iam_policy.p4sa-secretAccessor.policy_data
        }
        
        // Create the connection and add the repository resource
        resource "google_cloudbuildv2_connection" "my-connection" {
            project = "PROJECT_ID"
            location = "REGION"
            name = "CONNECTION_NAME"
        
            bitbucket_cloud_config {
                workspace = "WORKSPACE_ID"
                authorizer_credential {
                    user_token_secret_version = google_secret_manager_secret_version.admin-token-secret-version.id
                }
                read_authorizer_credential {
                    user_token_secret_version = google_secret_manager_secret_version.read-token-secret-version.id
                }
                webhook_secret_secret_version = google_secret_manager_secret_version.webhook-secret-secret-version.id
            }
        
            depends_on = [
                google_secret_manager_secret_iam_policy.policy-pak,
                google_secret_manager_secret_iam_policy.policy-rpak,
                google_secret_manager_secret_iam_policy.policy-whs
            ]
        }
        




Where:

  * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
  * PROJECT_NUMBER is your Google Cloud project number.
  * ADMIN_TOKEN_NAME is the name of your token with `webhook`, `repository`, `repository:admin`, and `pullrequest` scope access.
  * ADMIN_TOKEN_VALUE is the value of your ADMIN_TOKEN_NAME.
  * READ_TOKEN_NAME is the name of your token with `repository:read` scope.
  * READ_TOKEN_VALUE is the value of your READ_TOKEN_NAME.
  * WEBHOOK_SECRET_NAME is the name of your webhook secret.
  * WEBHOOK_SECRET_VALUE is the value of your WEBHOOK_SECRET_NAME.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * CONNECTION_NAME is the name of your connection.
  * WORKSPACE_ID is the Workspace ID for your Bitbucket Cloud repository.



## Rotate old or expired Bitbucket Cloud access tokens

Rotate your access tokens so that your Cloud Build host connection can maintain its connection to your Bitbucket Cloud repository. If your Bitbucket Cloud access token expires, then your Cloud Build host connection is disconnected from its Bitbucket Cloud repository. When this happens, you can't disable the connection or link a repository until you rotate the expired token. In addition, you will see errors in the following circumstances:

  * The **Connections detail** page for your connection shows an error message stating `Connection is disconnected due to an invalid or expired access token`.

  * If you try to link a repository to a connection that has an expired token, you see an **Invalid access token** message. Clicking **View connection** takes you to the **Connection details** page for the connection with the expired token.




Cloud Build lets you rotate access tokens by entering new token values and saving them in Secret Manager in the latest secret version for those tokens. To rotate your access tokens, do the following:

  1. Rotate each access token in Bitbucket Cloud:

     1. Go to the Bitbucket Cloud repository connected to your Cloud Build host connection.

     2. Follow the instructions in the Bitbucket documentation to [rotate an access token](https://support.atlassian.com/bitbucket-cloud/docs/rotate-an-access-token-for-a-repository/). When you rotate a token, Bitbucket Cloud creates a new token with new credentials and invalidates the previous version of that token. Your rotated token has the same permissions and scope as the original token.

     3. Copy the IDs of your rotated tokens.

  2. Update your access token in Cloud Build:

     1. Go to the **Connection details** page for your connection.

     2. Select **Update access tokens**.

     3. In the **Token rotation** menu, enter your new tokens in the **API access token** and **Read access token** fields.

     4. (Optional): If you want your connection to always use the latest version of the secret for your tokens, select **Update connection to always use latest version**. Leaving this option unselected may be helpful if your connection uses a specific secret version number.

     5. Select **Update** to save your changes.

Cloud Build saves the new access tokens as the latest version of your secret in Secret Manager.


For more information, see [Access tokens](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) and [Enhancing security in Bitbucket: Introducing expiry for access tokens](https://www.atlassian.com/blog/bitbucket/enhancing-security-in-bitbucket-introducing-expiry-for-access-tokens) in the Bitbucket Cloud documentation. 

## What's next

  * Learn how to [connect to a Bitbucket Cloud repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-cloud).
  * Learn how to [view build results](https://docs.cloud.google.com/build/docs/view-build-results).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
