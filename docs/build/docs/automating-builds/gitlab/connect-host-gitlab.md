---
url: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab/
title: Connect to a GitLab host \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:00.047040+00:00
---

# Connect to a GitLab host  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitLab host Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect a [GitLab](https://about.gitlab.com/) host to Cloud Build.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab)




## Connect to a GitLab host

Before creating a host connection for your GitLab instance, you must create personal access tokens in GitLab by completing the following steps:

  1. Log into your GitLab instance.

  2. On the GitLab page for your instance, click your avatar in the upper-right corner.

  3. Click **Edit profile**.

  4. On the left sidebar, select **Access tokens**.

You see the [Personal Access Tokens](https://gitlab.com/-/user_settings/personal_access_tokens) page.

  5. Create an access token with the `api` scope to use for connecting and disconnecting repositories.

  6. Create an access token with the `read_api` scope to ensure Cloud Build repositories can access source code in repositories.

**Note:** In addition to [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), you can also use [project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html). If your GitLab version is 14.2 or higher, you can also use [group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html). If you use project or group access tokens, select the `Maintainer` role to ensure a successful connection.



###  Console 

To connect your GitLab host to Cloud Build:

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

  7. In the **Host details** section, go to **GitLab host** and select **GitLab.com**.

  8. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your GitLab repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

  9. In the **Personal access tokens** section, enter the following information:

     * **API access token** : Enter the token with the `api` scope access. This token is used for connecting and disconnecting repositories.

     * **Read API access token** : Enter the token with the `read_api` scope access. Cloud Build triggers use this token to access source code in repositories.

  10. Click **Connect**.

After clicking the **Connect** button, your personal access tokens are securely stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview). Following host connection, Cloud Build also creates a webhook secret on your behalf. You can view and manage your secrets on the [Secret Manager page](https://console.cloud.google.com/security/secret-manager).




You have now successfully created a GitLab connection.

###  gcloud 

Prior to connecting your GitLab host to Cloud Build, complete the following steps to store your credentials:

  1. [Store your token in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

  2. [Create a webhook secret in Secret Manager](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events) by running the following command:
         
         cat /proc/sys/kernel/random/uuid | tr -d '\n' | gcloud secrets create my-gle-webhook-secret --data-file=-
         

  3. If you store your secrets in a different Google Cloud project than the one you plan to use to create a host connection, enter the following command to grant your project access to the Cloud Build service agent:
         
         PN=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         CLOUD_BUILD_SERVICE_AGENT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:${CLOUD_BUILD_SERVICE_AGENT}" \
           --role="roles/secretmanager.admin"
         

Where:

     * PROJECT_ID is your Google Cloud project ID.



You can now proceed to connect your GitLab host to Cloud Build.

Complete the following steps:

To connect your GitLab host to Cloud Build:

  1. Enter the following command to create a GitLab connection:
         
         gcloud builds connections create gitlab CONNECTION_NAME \
           --host-uri=HOST_URI \
           --project=PROJECT_ID \
           --region=REGION \
           --authorizer-token-secret-version=projects/PROJECT_ID/secrets/API_TOKEN/versions/SECRET_VERSION \
           --read-authorizer-token-secret-version=projects/PROJECT_ID/secrets/READ_TOKEN/versions/SECRET_VERSION \
           --webhook-secret-secret-version=projects/PROJECT_ID/secrets/WEBHOOK_SECRET/versions/SECRET_VERSION
         

Where:

     * CONNECTION_NAME is a name for your GitLab host connection in Cloud Build.
     * HOST_URI is the URI of your GitLab instance. For example, `https://my-gle-server.net`.
     * PROJECT_ID is your Google Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
     * API_TOKEN is the name of your token with `api`scope.
     * READ_TOKEN is the name of your token with `read_api`scope.
     * SECRET_VERSION is the version of your secret.
     * WEBHOOK_SECRET is your webhook secret.



You have now successfully created a GitLab connection.

## Rotate old or expired GitLab access tokens

Rotate your access tokens so that your Cloud Build host connection can maintain its connection to your GitLab repository. If your GitLab access token expires, then your Cloud Build host connection is disconnected from its GitLab repository. When this happens, you can't disable the connection or link a repository until you rotate the expired token. In addition, you will see errors in the following circumstances:

  * The **Connections detail** page for your connection shows an error message stating `Connection is disconnected due to an invalid or expired access token`.

  * If you try to link a repository to a connection that has an expired token, you see an **Invalid access token** message. Clicking **View connection** takes you to the **Connection details** page for the connection with the expired token.




Cloud Build lets you rotate access tokens by entering new token values and saving them in Secret Manager in the latest secret version for those tokens. To rotate your access tokens, do the following:

  1. Rotate each access token in GitLab:

     1. Go to the GitLab repository connected to your Cloud Build host connection.

     2. Follow the instructions in the GitLab documentation to [rotate an access token](https://docs.gitlab.com/user/profile/personal_access_tokens/#rotate-a-personal-access-token). When you rotate a token, GitLab creates a new token with new credentials and invalidates the previous version of that token. Your rotated token has the same permissions and scope as the original token.

     3. Copy the IDs of your rotated tokens.

  2. Update your access token in Cloud Build:

     1. Go to the **Connection details** page for your connection.

     2. Select **Update access tokens**.

     3. In the **Token rotation** menu, enter your new tokens in the **API access token** and **Read access token** fields.

     4. (Optional): If you want your connection to always use the latest version of the secret for your tokens, select **Update connection to always use latest version**. Leaving this option unselected may be helpful if your connection uses a specific secret version number.

     5. Select **Update** to save your changes.

Cloud Build saves the new access tokens as the latest version of your secret in Secret Manager.


For more information, see [Access token expiration](https://docs.gitlab.com/user/profile/personal_access_tokens/#access-token-expiration) in the GitLab documentation. 

## What's next

  * Learn how to [connect a GitLab repository](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab).
  * Learn how to build and deploy your workloads to Google Cloud using Google-managed CI/CD components in your GitLab pipeline. See [GitLab on Google Cloud](https://docs.cloud.google.com/docs/gitlab).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
