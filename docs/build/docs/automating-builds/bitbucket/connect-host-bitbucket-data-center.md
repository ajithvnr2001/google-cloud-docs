---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center/
title: Connect to a Bitbucket Data Center host \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:41.791578+00:00
---

# Connect to a Bitbucket Data Center host  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a Bitbucket Data Center host Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to connect a [Bitbucket Data Center](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html) host to Cloud Build. Connecting to a Bitbucket Data Center host integrates your Bitbucket Data Center repositories with Cloud Build. This way, you can configure build triggers to [build repositories from Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center) and [build repositories from Bitbucket Data Center in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network).

## Before you begin

  * Enable the Cloud Build, Secret Manager, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,compute.googleapis.com)



  * Have your source code ready in a Bitbucket Data Center repository.
  * Have either a `Dockerfile` or a [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config) in your Bitbucket Data Center source repository.
  * If you haven't installed a Bitbucket Data Center instance, then see [Bitbucket Data Center installation guide](https://confluence.atlassian.com/bitbucketserver/install-bitbucket-data-center-872139817.html) for instructions.



### Required IAM permissions

To get the permissions that you need to connect to your Bitbucket Data Center host, ask your administrator to grant you the [Cloud Build Connection Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.connectionAdmin) (`roles/cloudbuild.connectionAdmin`) IAM role on your user account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If your Bitbucket Data Center instance is hosted in a private network, see [Build repositories from Bitbucket Data Center in a private network](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-data-center-private-network) to learn about additional IAM roles required to configure a host connection.

### Create personal access tokens

Before you create a host connection for your Bitbucket Data Center instance, create personal access tokens in Bitbucket Data Center by doing the following:

  1. Sign in to your [Bitbucket Data Center](https://id.atlassian.com/login) instance.

  2. Follow the instructions to [create HTTP access tokens for your user account](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html).

     1. Create an access token with the **repository admin** scope to use for connecting and disconnecting repositories.

     2. Create an access token with the **repository read** scope to ensure Cloud Build repositories can access source code in repositories.

  3. Save your token values securely. You'll use them to [connect to your Bitbucket Data Center](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center) repository.


**Note:** In addition to access tokens for your user account, you can also use access tokens for projects or repositories. See [Create HTTP access tokens for projects or repositories](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html#HTTPaccesstokens-CreateHTTPaccesstokensforprojectsorrepositories).

## Connect to a Bitbucket Data Center host

###  Console 

To connect your Bitbucket Data Center host to Cloud Build:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

  2. At the top of the page, select the **2nd gen** tab.

  3. In the project selector in the top bar, select your Google Cloud project.

  4. Click **Create host connection** to connect a new host to Cloud Build.

  5. On the left panel, select **Bitbucket** as your source provider.

  6. In the **Configure Connection** section, enter the following information:

     * **Region** : Select a region for your connection. You must specify a region. Your connection cannot exist globally.

     * **Name** : Enter a name for your connection.

  7. In the **Host details** section, select or enter the following information:

     * **Bitbucket host** : Select Bitbucket Data Center as your host.

     * **Host URL** : Enter the [URL of your host](https://confluence.atlassian.com/bitbucketserver/specify-the-bitbucket-base-url-776640392.html).

  8. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your Bitbucket Data Center repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

  9. In the **Networking** section, select one of the following options:

     * **Public internet** : Select this option if your instance is accessible using the public internet.

     * **Private network** : Select this option if your instance is hosted on a private network. Then, configure the following:

       1. **CA Certificate** : Your self-signed certificate. Click **Browse** to open the certificate from your local machine.

Your certificate must not exceed 10 KB in size and should be in PEM format (`.pem`, `.cer`,or `.crt`). If you leave this field blank, Cloud Build uses a certificate from the [default set of certificates](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/#5-certificates).

       2. Under **Service Directory service** , selection the location for your service:

          * **In project CURRENT_PROJECT**
          * **In another project**
          * **Enter manually**
       3. Enter the following information:

          * **Project** : If you selected **In another project** or **Enter manually** , then enter or select your Google Cloud project ID from the drop-down menu.

          * **Region** : This field pre-selects the region of your connection. The region specified for your service must match the region associated with your connection.

          * **Namespace** : Select the namespace of your service.

          * **Service** : Select the service name in your namespace.

  10. In the **HTTP access tokens** section, enter the following information:

     * **Admin access token** : Enter the token with the **repository admin** scope access. This token is used for connecting and disconnecting repositories.

     * **Read access token** : Enter the token with the **repository read** scope access. Cloud Build triggers use this token to access source code in repositories.

  11. Click **Connect**.

After clicking the **Connect** button, your personal access tokens are securely stored in Secret Manager. After connecting to the Bitbucket Data Center host, Cloud Build creates a webhook secret on your behalf. You can view and manage your secrets on the [Secret Manager](https://console.cloud.google.com/security/secret-manager) page.




###  gcloud 

  1. [Store your tokens in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

  2. [Create a webhook secret in Secret Manager](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events) by running the following command, where WEBHOOK_SECRET is the name you want to give to your webhook secret:
         
         cat /proc/sys/kernel/random/uuid | tr -d '\n' | gcloud secrets create WEBHOOK_SECRET --data-file=-
         

  3. If you store your secrets in a different Google Cloud project than the one you plan to use to create a host connection, run the following command to grant your project access to the Cloud Build service agent:
         
         PN=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         CLOUD_BUILD_SERVICE_AGENT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:${CLOUD_BUILD_SERVICE_AGENT}" \
             --role="roles/secretmanager.admin"
         

Where:

     * PROJECT_ID is your Google Cloud project ID.



You can now proceed to connect your Bitbucket Data Center host to Cloud Build.

  1. Run the following command to create a Bitbucket Data Center connection:
         
         gcloud builds connections create bitbucket-data-center CONNECTION_NAME \
             --host-uri=HOST_URI \
             --project=PROJECT_ID \
             --region=REGION \
             --authorizer-token-secret-version=projects/PROJECT_ID/secrets/ADMIN_TOKEN/versions/SECRET_VERSION \
             --read-authorizer-token-secret-version=projects/PROJECT_ID/secrets/READ_TOKEN/versions/SECRET_VERSION \
             --webhook-secret-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET/versions/SECRET_VERSION
          ```
         
         Where:
         

     * CONNECTION_NAME is a name for your Bitbucket Data Center host connection in Cloud Build.
     * HOST_URI is the URI of your Bitbucket Data Center instance.
     * PROJECT_ID is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#get_an_existing_project).
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
     * ADMIN_TOKEN is the name of your token with **repository admin** scope.
     * READ_TOKEN is the name of your token with **repository read** scope.
     * SECRET_VERSION is the version of your secret.
     * WEBHOOK_SECRET is your webhook secret.



###  Terraform 

You can connect your Bitbucket Data Center host to Cloud Build using Terraform.

In the following example, the code snippet does the following:

  * Configures the Terraform Google provider.
  * Creates a Secret Manager secret to store the Bitbucket tokens.
  * Grants necessary permissions to the Cloud Build service agent to access secrets.
  * Creates a Bitbucket Data Center connection.
        
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
        
        // Create the connection resource
        resource "google_cloudbuildv2_connection" "my-connection" {
            project = "PROJECT_ID"
            location = "REGION"
            name = "CONNECTION_NAME"
        
            bitbucket_data_center_config {
                host_uri = "BITBUCKET_URI"
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
  * ADMIN_TOKEN_NAME is the name of your token with `repository:admin` scope.
  * ADMIN_TOKEN_VALUE is the value of your ADMIN_TOKEN_NAME.
  * READ_TOKEN_NAME is the name of your token with `repository:read` scope.
  * READ_TOKEN_VALUE is the value of your READ_TOKEN_NAME.
  * WEBHOOK_SECRET_NAME is the name of your webhook secret.
  * WEBHOOK_SECRET_VALUE is the value of your WEBHOOK_SECRET_NAME.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * CONNECTION_NAME is a name for your Bitbucket Data Center host connection in Cloud Build.
  * BITBUCKET_URI is the URI of your Bitbucket Data Center instance.



## Rotate old or expired Bitbucket Data Center access tokens

Rotate your access tokens so that your Cloud Build host connection can maintain its connection to your Bitbucket Data Center repository. If your Bitbucket Data Center access token expires, then your Cloud Build host connection is disconnected from its Bitbucket Data Center repository. When this happens, you can't disable the connection or link a repository until you rotate the expired token. In addition, you will see errors in the following circumstances:

  * The **Connections detail** page for your connection shows an error message stating `Connection is disconnected due to an invalid or expired access token`.

  * If you try to link a repository to a connection that has an expired token, you see an **Invalid access token** message. Clicking **View connection** takes you to the **Connection details** page for the connection with the expired token.




Cloud Build lets you rotate access tokens by entering new token values and saving them in Secret Manager in the latest secret version for those tokens. To rotate your access tokens, do the following:

  1. Rotate each access token in Bitbucket Data Center:

     1. Go to the Bitbucket Data Center repository connected to your Cloud Build host connection.

     2. Follow the instructions in the Bitbucket documentation to [rotate an access token](https://support.atlassian.com/bitbucket-cloud/docs/rotate-an-access-token-for-a-repository/). When you rotate a token, Bitbucket Data Center creates a new token with new credentials and invalidates the previous version of that token. Your rotated token has the same permissions and scope as the original token.

     3. Copy the IDs of your rotated tokens.

  2. Update your access token in Cloud Build:

     1. Go to the **Connection details** page for your connection.

     2. Select **Update access tokens**.

     3. In the **Token rotation** menu, enter your new tokens in the **API access token** and **Read access token** fields.

     4. (Optional): If you want your connection to always use the latest version of the secret for your tokens, select **Update connection to always use latest version**. Leaving this option unselected may be helpful if your connection uses a specific secret version number.

     5. Select **Update** to save your changes.

Cloud Build saves the new access tokens as the latest version of your secret in Secret Manager.


For more information, see [Access tokens](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) and [Enhancing security in Bitbucket: Introducing expiry for access tokens](https://www.atlassian.com/blog/bitbucket/enhancing-security-in-bitbucket-introducing-expiry-for-access-tokens) in the Bitbucket Data Center documentation. 

## What's next

  * Learn how to [connect a Bitbucket Data Center repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
