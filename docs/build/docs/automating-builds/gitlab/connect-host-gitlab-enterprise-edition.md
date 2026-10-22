---
url: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition/
title: Connect to a GitLab Enterprise Edition host \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:59.763832+00:00
---

# Connect to a GitLab Enterprise Edition host  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitLab Enterprise Edition host Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect to [GitLab Enterprise Edition](https://about.gitlab.com/enterprise/) host to Cloud Build.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition)




### Host requirements

  * If you have not installed a GitLab Enterprise Edition Server instance, see [the installation guide from GitLab Enterprise Edition](https://about.gitlab.com/install/) for instructions.

When following the instructions to install a GitLab Enterprise Edition Server instance, keep note of the following:

    * You **must** configure your host to handle `HTTPS` protocol. Hosts configured with `HTTP` protocol are not supported.

    * You **must** configure your host with the same URL that is used to reach your host from Google Cloud. To learn more, see the GitLab documentation for [configuring the external URL](https://docs.gitlab.com/omnibus/settings/configuration.html#configure-the-external-url-for-gitlab).




## Required IAM permissions

To connect your GitLab Enterprise Edition host, grant the Cloud Build Connection Admin (`roles/cloudbuild.connectionAdmin`) role to your user account.

To add the required roles to your user account, see [Configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources). To learn more about IAM roles associated with Cloud Build, see [IAM roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).

**If your GitLab Enterprise Edition instance is hosted in a private network, see[Build repositories from GitLab Enterprise Edition in a private network](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab-enterprise-edition-private-network) to learn about additional IAM roles required prior to host connection.**

## Connect to a GitLab Enterprise Edition host

Before creating a host connection for your GitLab Enterprise Edition instance, you must create personal access tokens in GitLab Enterprise Edition by completing the following steps:

  1. Log into your GitLab Enterprise Edition instance.

  2. On the GitLab Enterprise Edition page for your instance, click your avatar in the upper-right corner.

  3. Click **Edit profile**.

  4. On the left sidebar, select **Access tokens**.

You see the [Personal Access Tokens](https://gitlab.com/-/profile/personal_access_tokens) page.

  5. Create an access token with the `api` scope to use for connecting and disconnecting repositories.

  6. Create an access token with the `read_api` scope to ensure Cloud Build repositories can access source code in repositories.

**Note:** In addition to [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), you can also use [project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html). If your GitLab version is 14.2 or later, you can also use [group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html). If you use project or group access tokens, select the `Maintainer` role to ensure a successful connection.



###  Console 

To connect your GitLab Enterprise Edition host to Cloud Build:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You see the **Repositories** page.

  2. At the top of the page, select the **2nd gen** tab.

  3. In the project selector in the top bar, select your Google Cloud project.

  4. Click **Create host connection** to connect a new host to Cloud Build.

  5. On the left panel, select **GitLab** as your source provider.

  6. In the **Configure Connection** section, enter the following information:

     * **Region** : Select a region for your connection.

**Note:** You must specify a region. Your connection cannot exist globally.
     * **Name** : Enter a name for your connection.

  7. In the **Host details** section, select or enter the following information:

     * **GitLab host** : Select **Self-managed GitLab Enterprise Edition**.

     * **Host URL** : Enter the host URL for your connection. For example, `https://my-gle-server.net`.

  8. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your GitLab Enterprise Edition repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

  9. In the **Networking** section, under **Connection type** , select one of the following options:

     * **Public internet** : Select this option if your instance is accessible using the public internet.

     * **Private network** : Select this option if your instance is hosted on a private network. Then, configure the following:

       1. **CA Certificate** : Click Browse to upload your self-signed certificate.

**Note:** Your certificate must not exceed 10 KB in size and should be in PEM format (`.pem`, `.cer`, or `.crt`). If this section is left blank, a [default set of certificates](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/#5-certificates) will be used in place.
       2. Under **Service Directory service** , selection the location for your service:

          * **In project CURRENT_PROJECT**
          * **In another project**
          * **Enter manually**
       3. Enter the following information:

          * **Project** : If you selected **In another project** or **Enter manually** , then enter or select your Google Cloud project ID from the drop-down menu.

          * **Region** : This field pre-selects the region of your connection. The region specified for your service must match the region associated with your connection.

          * **Namespace** : Select the namespace of your service.

          * **Service** : Select the service name in your namespace.

  10. In the **Personal access tokens** section, enter the following information:

     * **API access token** : Enter the token with the `api` scope access. This token is used for connecting and disconnecting repositories.

     * **Read API access token** : Enter the token with the `read_api` scope access. Cloud Build triggers use this token to access source code in repositories.

  11. Click **Connect**.

After clicking the **Connect** button, your personal access tokens are securely stored in Secret Manager. Following host connection, Cloud Build also creates a webhook secret on your behalf. You can view and manage secrets on the Secret Manager page. You can view and manage your secrets on the [Secret Manager](https://console.cloud.google.com/security/secret-manager) page.




###  gcloud 

Prior to connecting your GitLab Enterprise Edition host to Cloud Build, complete the following steps to store your credentials:

  1. [Store your token in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

  2. [Create a webhook secret in Secret Manager](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events) by running the following command:
         
         cat /proc/sys/kernel/random/uuid | tr -d '\n' | gcloud secrets create my-gle-webhook-secret --data-file=-
         

  3. If you store your secrets in a different Google Cloud project than the one you plan to use to create a host connection, enter the following command to grant your project access to the Cloud Build service agent:
         
         PN=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         CLOUD_BUILD_SERVICE_AGENT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:${CLOUD_BUILD_SERVICE_AGENT} \
           --role="roles/secretmanager.admin"
         

Where:

     * PROJECT_ID is your Google Cloud project ID.



You can now proceed to connect your GitLab Enterprise Edition host to Cloud Build.

Complete the following steps:

  1. Enter the following command to create a GitLab Enterprise Edition connection:
         
         gcloud builds connections create gitlab CONNECTION_NAME \
           --host-uri=HOST_URI \
           --project=PROJECT_ID \
           --region=REGION \
           --authorizer-token-secret-version=projects/PROJECT_ID/secrets/API_TOKEN/versions/SECRET_VERSION \
           --read-authorizer-token-secret-version=projects/PROJECT_ID/secrets/READ_TOKEN/versions/SECRET_VERSION \
           --webhook-secret-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET/versions/SECRET_VERSION
         

Where:

     * CONNECTION_NAME is a name for your connection in Cloud Build.
     * HOST_URI is the URI of your GitLab Enterprise Edition instance. For example, `https://my-gle-server.net`.
     * PROJECT_ID is your Google Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
     * API_TOKEN is the name of your token with `api`scope.
     * READ_TOKEN is the name of your token with `read_api`scope.
     * SECRET_VERSION is the version of your secret.
     * WEBHOOK_SECRET is your webhook secret.



You have now successfully created a GitLab Enterprise Edition connection.

###  Terraform 

You can connect your GitLab Enterprise Edition host to Cloud Build using Terraform. Learn more about [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform).

In the following example, the code snippet does the following:

  * Configures [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs) resources
  * Creates a secret to store your GitLab Enterprise Edition personal access token
  * Grants necessary permissions to the Cloud Build service agent to access secrets
  * Creates a GitLab Enterprise Edition connection
        
        // Configure the Terraform Google provider
        terraform {
          required_providers {
            google = {}
          }
        }
        
        // Create secrets and grant permissions to the Cloud Build service agent
        resource "google_secret_manager_secret" "api-pat-secret" {
            project = "PROJECT_ID"
            secret_id = "GITLAB_PAT_API"
        
            replication {
                auto {}
             }
         }
        
         resource "google_secret_manager_secret_version" "api-pat-secret-version" {
             secret = google_secret_manager_secret.api-pat-secret.id
             secret_data = "GITLAB_API_TOKEN"
         }
        
         resource "google_secret_manager_secret" "read-pat-secret" {
             project = "PROJECT_ID"
             secret_id = "GITLAB_PAT_READ"
        
             replication {
                 auto {}
             }
        }
        
        resource "google_secret_manager_secret_version" "read-pat-secret-version" {
            secret = google_secret_manager_secret.read-pat-secret.id
            secret_data = "GITLAB_API_TOKEN"
        }
        
        resource "google_secret_manager_secret" "webhook-secret-secret" {
            project = "PROJECT_ID"
            secret_id = "WEBHOOK_SECRET"
        
            replication {
                auto {}
            }
        }
        
        resource "google_secret_manager_secret_version" "webhook-secret-secret-version" {
            secret = google_secret_manager_secret.webhook-secret-secret.id
            secret_data = "WEBHOOK_SECRET_VALUE"
        }
        
        data "google_iam_policy" "serviceagent-secretAccessor" {
            binding {
                role = "roles/secretmanager.secretAccessor"
                members = ["serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"]
            }
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-pak" {
          project = google_secret_manager_secret.api-pat-secret.project
          secret_id = google_secret_manager_secret.api-pat-secret.secret_id
          policy_data = data.google_iam_policy.serviceagent-secretAccessor.policy_data
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-rpak" {
          project = google_secret_manager_secret.read-pat-secret.project
          secret_id = google_secret_manager_secret.read-pat-secret.secret_id
          policy_data = data.google_iam_policy.serviceagent-secretAccessor.policy_data
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-whs" {
          project = google_secret_manager_secret.webhook-secret-secret.project
          secret_id = google_secret_manager_secret.webhook-secret-secret.secret_id
          policy_data = data.google_iam_policy.serviceagent-secretAccessor.policy_data
        }
        
        // Create the connection and add the repository resource
        resource "google_cloudbuildv2_connection" "my-connection" {
            project = "PROJECT_ID"
            location = "REGION"
            name = "CONNECTION_NAME"
        
            gitlab_config {
                host_uri = "URI"
                authorizer_credential {
                    user_token_secret_version = google_secret_manager_secret_version.api-pat-secret-version.id
                }
                read_authorizer_credential {
                     user_token_secret_version = google_secret_manager_secret_version.read-pat-secret-version.id
                }
                webhook_secret_secret_version = google_secret_manager_secret_version.webhook-secret-secret-version.id
            }
        
            depends_on = [
                google_secret_manager_secret_iam_policy.policy-pak,
                google_secret_manager_secret_iam_policy.policy-rpak,
                google_secret_manager_secret_iam_policy.policy-whs
            ]
        }
        




Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `GITLAB_PAT_API`: your personal access token with `api` access.
  * `GITLAB_API_TOKEN`: your personal access token.
  * `GITLAB_PAT_READ`: your personal access token with `read_api` access.
  * `WEBHOOK_SECRET`: the secret name containing your webhook secret value.
  * `WEBHOOK_SECRET_VALUE`: the value of your webhook secret.
  * `PROJECT_NUMBER`: your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
        
        gcloud projects describe PROJECT_ID --format='value(projectNumber)'
        

  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.

  * `CONNECTION_NAME`: a name for your GitLab Enterprise Edition host connection in Cloud Build.

  * `URI`: the URI of your connection—for example, `https://my-gitlab-enterprise-server.net`.




You have now successfully created a GitLab Enterprise Edition connection.

## Rotate old or expired GitLab Enterprise Edition access tokens

Rotate your access tokens so that your Cloud Build host connection can maintain its connection to your GitLab Enterprise Edition repository. If your GitLab Enterprise Edition access token expires, then your Cloud Build host connection is disconnected from its GitLab Enterprise Edition repository. When this happens, you can't disable the connection or link a repository until you rotate the expired token. In addition, you will see errors in the following circumstances:

  * The **Connections detail** page for your connection shows an error message stating `Connection is disconnected due to an invalid or expired access token`.

  * If you try to link a repository to a connection that has an expired token, you see an **Invalid access token** message. Clicking **View connection** takes you to the **Connection details** page for the connection with the expired token.




Cloud Build lets you rotate access tokens by entering new token values and saving them in Secret Manager in the latest secret version for those tokens. To rotate your access tokens, do the following:

  1. Rotate each access token in GitLab Enterprise Edition:

     1. Go to the GitLab Enterprise Edition repository connected to your Cloud Build host connection.

     2. Follow the instructions in the GitLab documentation to [rotate an access token](https://docs.gitlab.com/user/profile/personal_access_tokens/#rotate-a-personal-access-token). When you rotate a token, GitLab Enterprise Edition creates a new token with new credentials and invalidates the previous version of that token. Your rotated token has the same permissions and scope as the original token.

     3. Copy the IDs of your rotated tokens.

  2. Update your access token in Cloud Build:

     1. Go to the **Connection details** page for your connection.

     2. Select **Update access tokens**.

     3. In the **Token rotation** menu, enter your new tokens in the **API access token** and **Read access token** fields.

     4. (Optional): If you want your connection to always use the latest version of the secret for your tokens, select **Update connection to always use latest version**. Leaving this option unselected may be helpful if your connection uses a specific secret version number.

     5. Select **Update** to save your changes.

Cloud Build saves the new access tokens as the latest version of your secret in Secret Manager.


For more information, see [Access token expiration](https://docs.gitlab.com/user/profile/personal_access_tokens/#access-token-expiration) in the GitLab Enterprise Edition documentation. 

## What's next

  * Learn how to [connect a GitLab Enterprise Edition repository](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab-enterprise-edition).
  * Learn how to build and deploy your workloads to Google Cloud using Google-managed CI/CD components in your GitLab pipeline. See [GitLab on Google Cloud](https://docs.cloud.google.com/docs/gitlab).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
