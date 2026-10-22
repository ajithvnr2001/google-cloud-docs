---
url: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise/
title: Connect to a GitHub Enterprise host \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:29.529502+00:00
---

# Connect to a GitHub Enterprise host  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Connect to a GitHub Enterprise host Stay organized with collections  Save and categorize content based on your preferences. 

1st gen 2nd gen

This page explains how to connect a [GitHub Enterprise](https://docs.github.com/en/enterprise-server) host to Cloud Build.

## Before you begin

  * Enable the Cloud Build and Secret Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise)



  * Ensure that you have the [latest version](https://docs.github.com/en/enterprise-server@2.22/admin/enterprise-management/upgrading-github-enterprise-server) of GitHub Enterprise.
  * Ensure you map a custom domain to your GitHub Enterprise host and have a valid SSL certificate for your host.

**Note:** If your GitHub Enterprise host is running on a Compute Engine instance, you can [create an External HTTP(s) Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https), and [use a Google-managed SSL](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) certificate for your instance.
  * If your GitHub Enterprise instance is hosted in a private network, see [Build repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network) prior to completing instructions on this page.




## Required IAM permissions

To connect your GitHub Enterprise host, grant the Cloud Build Connection Admin (`roles/cloudbuild.connectionAdmin`) role to your user account.

To add the required roles to your user account, see [Configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources). To learn more about IAM roles associated with Cloud Build, see [IAM roles and permissions](https://docs.cloud.google.com/build/docs/iam-roles-permissions).

To create connections using `gcloud` installation steps, grant the Secret Manager Admin role (`roles/secretmanager.admin`) to the Cloud Build Service Agent by running the following command in your Google Cloud project:
    
    
          PN=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
          CLOUD_BUILD_SERVICE_AGENT="service-${PN}@gcp-sa-cloudbuild.iam.gserviceaccount.com"
           gcloud projects add-iam-policy-binding ${PROJECT_ID} \
             --member="serviceAccount:${CLOUD_BUILD_SERVICE_AGENT}" \
             --role="roles/secretmanager.admin"
    

**Note:** You can revoke the Secret Manager Admin role (`roles/secretmanager.admin`) after your connection is in state `COMPLETE`. To learn more, see [Granting a role to the Cloud Build service agent](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#service-agent-permissions).

**If your GitHub Enterprise instance is hosted in a private network, see[Build repositories from GitHub Enterprise in a private network](https://docs.cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise-private-network?generation=2nd-gen) to learn about additional IAM roles required prior to host connection.**

## Connect to a GitHub Enterprise host

###  Console 

To connect your GitHub Enterprise host to Cloud Build:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

You will see the **Repositories** page.

  2. In the project selector in the top bar, select your Google Cloud project.

  3. At the top of the page, select the **2nd gen** tab.

  4. Click **Create host connection** to connect a new host to Cloud Build.

  5. On the left panel, select **GitHub Enterprise** as your source provider.

  6. In the **Configure Connection** section, enter the following information:

     * **Region** : Select a region for your connection.

**Note:** You must specify a region. Your connection cannot exist globally.
     * **Name** : Enter a name for your connection.

  7. In the **Host details** section, go to **Host URL** and enter the host URL for your connection. For example, `github.example.com`.

  8. Optional: If you want to manage the encryption keys used to encrypt the access tokens for your GitHub Enterprise repositories, then go to the **Encryption** section and choose a Cloud Key Management Service key. For more information, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).

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

  10. Click **Connect**.

After you click the **Connect** button, you'll be asked to create a GitHub App in your GitHub Enterprise host and install the app in a user account or organization. An authentication token from your GitHub Enterprise host is created and stored in this project as a Secret Manager secret. You can revoke access by uninstalling or deleting the GitHub app from your host at any time.

Cloud Build stores the authentication data of the created GitHub App as secrets in Secret Manager in your project. This data includes your private key and webhook secret. The private key is used as an authentication method to access the API of the Enterprise Server. The webhook secret is used to validate the events sent from the server to Cloud Build. The Cloud Build Service Agent account (`service-{projectNumber}@gcp-sa-cloudbuild.iam.gserviceaccount.com`) is used to access your secret. To view your secret, see [List secrets and view secret details](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).

After authorizing the Cloud Build GitHub App, you will be redirected to the Cloud Build [**Repositories**](https://console.cloud.google.com/cloud-build/repositories) page.




###  gcloud 

To connect your GitHub Enterprise host to Cloud Build using `gcloud` commands, complete the following steps:

  1. Enter the following command to create a GitHub Enterprise connection:
         
         gcloud builds connections create github-enterprise CONNECTION_NAME \
           --host-uri=HOST_URI --region=REGION
         

Where:

     * CONNECTION_NAME is a name for your GitHub Enterprise host connection in Cloud Build.
     * HOST_URI is the URI of your GitHub Enterprise instance. For example, `https://mmy-ghe-server.net`.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.

If your GitHub Enterprise instance is in a private network, specify your Service Directory resource. You can also specify your CA certificate.
    
    --service-directory-service=projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE/services/SERVICE_NAME \
    --ssl-ca-file=SSL_CA_FILEPATH
    

Where:

     * PROJECT_ID is your Google Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
     * NAMESPACE is the namespace for your service.
     * SERVICE_NAME is the name of your service in your namespace.
     * SSL_CA_FILEPATH is the path to your CA certificate.

After running the `gcloud builds connections...` command, you will receive a link to install the Cloud Build GitHub app.

  2. Follow the link returned in the previous step to create and install the Cloud Build GitHub App on your enterprise server.

  3. Enter the following command to verify your connection:
         
         gcloud builds connections describe CONNECTION_NAME --region=REGION
         

Where:

     * CONNECTION_NAME is the name of your GitHub Enterprise host connection in Cloud Build.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.

If the `installationState` field is set to `COMPLETE`, you have successfully installed the connection. Otherwise, the `installationState` field provides a link for additional steps required.




## Connect to a GitHub Enterprise host programmatically

To connect your GitHub Enterprise host programmatically to Cloud Build, you must install the GitHub app by completing the following steps:

  1. Register a new GitHub app. For example, you may register a new GitHub app at `https://my-ghe-server.net/settings/apps/new`.

  2. Complete the fields on the page:

     1. **GitHub App Name** : Enter a name for your app.
     2. **Homepage URL** : Enter a URL for your GitHub Enterprise Server.
     3. Clear the box for **Expire user authorization tokens**.
     4. In the **Webhook** section, complete the following steps: 
        * **Active** : Check the box to activate your webook.
        * **Webhook URL** : Enter your webhook URL. For example, `https://cloudbuild.googleapis.com/v2/projects/{PROJECT_NUMBER}/locations/{REGION}/connections:processWebhook`. The region in the webhook URL must match the region of your connection.
        * **Webhook secret** : Enter a randomly generated string and take note of it.
     5. In the **Permissions** section, specify the following permissions: 
        * **Repository permissions** : 
          * **Checks** : Read and write
          * **Contents** : Read and write
          * **Issues** : Read-only
          * **Metadata** Read-only
          * **Commit statuses** : Read-only
          * **Pull requests** : Read-only
     6. In the **Subscribe to events** section, check the following boxes: 
        * **Check run**
        * **Check suite**
        * **Commit comment**
        * **Issue comment**
        * **Pull request**
        * **Pull request review comment**
        * **Push**
        * **Repository**
     7. Check the box for **Any account** to allow your GitHub app to be installed by any user or organization.
  3. Click **Create GitHub app** to create your GitHub app.

One you click **Create GitHub app** , you will be redirected to your app page. Take note of your App ID and the App slug. The App slug can be found in the last segment of the URL of the page. For example, `https://my-ghe-server.net/settings/apps/{app-slug}`

  4. In the **Private keys** section, click **Generate a private key**.

Store the downloaded file in a secure place.

  5. In the left pane, select **Install App**.

Select the user or organization where you want to install the app. After the app is installed, take note of the installation ID. The installation ID can be found in the last segment of the URL of the page. For example, `https://my-ghe-server.net/settings/installations/{installation-id}`.




After you have installed your GitHub app, complete the following steps to connect your GitHub Enterprise host programmatically using Terraform or `gcloud`.

###  Terraform 

Once you have installed your GitHub app, you can connect your GitHub Enterprise host to Cloud Build using the Google Terraform provider.

In the following example, the code snippet does the following:

  * Configures the Terraform Google provider
  * Creates a secret to store the GitHub App's private key and webhook secret
  * Grants necessary permissions to the Cloud Build Service Agent to access secrets
  * Creates a GitHub Enterprise connection
        
        // Configure the terraform google provider
        terraform {
          required_providers {
            google = {}
          }
        }
        
        // create Secrets and grant permissions to the Service Agent
        resource "google_secret_manager_secret" "private-key-secret" {
            project = "PROJECT_ID"
            secret_id = "PRIVATE_KEY_SECRET"
        
            replication {
                auto {}
            }
        }
        
        resource "google_secret_manager_secret_version" "private-key-secret-version" {
            secret = google_secret_manager_secret.private-key-secret.id
            secret_data = file("private-key.pem")
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
        
        resource "google_secret_manager_secret_iam_policy" "policy-pk" {
          project = google_secret_manager_secret.private-key-secret.project
          secret_id = google_secret_manager_secret.private-key-secret.secret_id
          policy_data = data.google_iam_policy.serviceagent-secretAccessor.policy_data
        }
        
        resource "google_secret_manager_secret_iam_policy" "policy-whs" {
          project = google_secret_manager_secret.webhook-secret-secret.project
          secret_id = google_secret_manager_secret.webhook-secret-secret.secret_id
          policy_data = data.google_iam_policy.serviceagent-secretAccessor.policy_data
        }
        
        // create the connection and add the repository resource ---
        resource "google_cloudbuildv2_connection" "my-connection" {
            project = "PROJECT_ID"
            location = "REGION"
            name = "CONNECTION_NAME"
        
            github_enterprise_config {
                host_uri = "URI"
                private_key_secret_version = google_secret_manager_secret_version.private-key-secret-version.id
                webhook_secret_secret_version = google_secret_manager_secret_version.webhook-secret-secret-version.id
                app_id = "APP_ID"
                app_slug = "APP_SLUG"
                app_installation_id = INSTALLATION_ID
            }
        
            depends_on = [
                google_secret_manager_secret_iam_policy.policy-pk,
                google_secret_manager_secret_iam_policy.policy-whs
            ]
        }
        




Where:

  * PROJECT_ID is your Google Cloud project ID.
  * PRIVATE_KEY_SECRET is the secret containing your GitHub App's private key.
  * WEBHOOK_SECRET is the secret name containing your GitHub App's webhook secret value.
  * WEBHOOK_SECRET_VALUE is the value of your GitHub App's webhook secret.
  * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
  * CONNECTION_NAME is a name for your GitHub Enterprise host connection in Cloud Build.
  * URI is the URI of your connection. For example, `https://my-github-enterprise-server.net`.
  * APP_ID is the ID of your GitHub App.
  * APP_SLUG is the app slug. For example, `https://github.com/settings/apps/{app-slug}`.
  * INSTALLATION_ID is the installation ID of your GitHub app. Your installation ID can be found in the URL of your Cloud Build GitHub App, `https://github.com/settings/installations/{installation-id}`.



###  gcloud 

After you have installed your GitHub app, complete the following steps to connect your GitHub Enterprise host programmatically using `gcloud`:

  1. Store your secrets in Secret Manager:
         
         echo -n WEBHOOK_SECRET | gcloud secrets create mygheapp-webhook-secret --data-file=-
         # creating secret from the downloaded private key:
         gcloud secrets create mygheapp-private-key --data-file=PRIVATE_KEY_FILE
         

Where:

     * WEBHOOK_SECRET is the string you created for your webhook secret.
     * PRIVATE_KEY_FILE is the path to the private key you generated.
  2. Grant access to the Cloud Build Service Agent to access your secrets:
         
         PROJECT_NUMBER=$(gcloud projects describe PROJECT_ID --format="value(projectNumber)")
         CLOUD_BUILD_SERVICE_AGENT="service-$PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com"
         gcloud secrets add-iam-policy-binding mygheapp-webhook-secret \
           --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
           --role="roles/secretmanager.secretAccessor"
         gcloud secrets add-iam-policy-binding mygheapp-private-key \
           --member="serviceAccount:$CLOUD_BUILD_SERVICE_AGENT" \
           --role="roles/secretmanager.secretAccessor"
         

Where:

     * PROJECT_ID is your Google Cloud project ID.
     * CLOUD_BUILD_SERVICE_AGENT is your Per-Product Per-Project account.
  3. Create your GitHub Enterprise connection:
         
         gcloud builds connections create github-enterprise CONNECTION_NAME \
           --host-uri=HOST_URI \
           --app-id=APP_ID \
           --app-slug=APP_SLUG \
           --private-key-secret-version=projects/PROJECT_ID/secrets/mygheapp-private-key/versions/1 \
           --webhook-secret-secret-version=projects/PROJECT_ID/secrets/mygheapp-webhook-secret/versions/1 \
           --app-installation-id=INSTALLATION_ID \
           --region=REGION
         

Where:

     * CONNECTION_NAME is a name for your GitHub Enterprise host connection in Cloud Build.
     * HOST_URI is the URI of your GitHub Enterprise instance. For example, `https://mmy-ghe-server.net`.
     * APP_ID is the ID of your GitHub App.
     * APP_SLUG is the app slug. For example, `https://my-ghe-server.net/settings/apps/app-slug`.
     * PROJECT_ID is your Google Cloud project ID.
     * INSTALLATION_ID is the installation ID of your GitHub app. For example, `https://my-ghe-server.net/settings/installations/installation-id`
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.

If your GitHub Enterprise instance is in a private network, specify your Service Directory resource. You can also specify your CA certificate.
    
    --service-directory-service=projects/PROJECT_ID/locations/REGION/namespaces/NAMESPACE/services/SERVICE_NAME \
      --ssl-ca-file=SSL_CA_FILEPATH
    

Where:

     * PROJECT_ID is your Google Cloud project ID.
     * REGION is the [region](https://docs.cloud.google.com/build/docs/locations) for your connection.
     * NAMESPACE is the namespace of your service.
     * SERVICE_NAME is the name of your service in your namespace.
     * SSL_CA_FILEPATH is the path to your CA certificate.



## Rotate GitHub Enterprise access tokens

Rotate your access tokens so that your Cloud Build host connection can maintain its connection to your GitHub Enterprise repository. If your GitHub Enterprise access token expires, then your Cloud Build host connection is disconnected from its GitHub Enterprise repository. When this happens, you can't disable the connection or link a repository until you rotate the expired token. In addition, you will see errors in the following circumstances:

  * The **Connections details** page for your connection shows either a **Troubleshoot connection issues** error message or **GitHub App installation not found** error message. Both messages provide a **Manage installation** button.

  * If you try to link a repository to a connection that has an expired token, you see an **Invalid access token** message. Clicking **View connection** takes you to the **Connection details** page for the connection with the expired token.




Expired or invalid GitHub Enterprise access tokens can't be rotated in a Cloud Build connection, and that connection is no longer usable. To view information in GitHub Enterprise about the status of your repository and tokens, do the following:

  1. On the **Connection details** page, click **Troubleshoot**.

  2. On the **Troubleshoot connection issues** menu, click **Manage installation**.

Cloud Build opens the GitHub Enterprise page for your installations.




## Next steps

  * Learn how to [connect a repository to GitHub Enterprise](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise).
  * Learn how to [perform blue-green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
