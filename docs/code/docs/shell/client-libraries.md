---
url: https://docs.cloud.google.com/code/docs/shell/client-libraries/
title: Manage Cloud APIs and Cloud Client Libraries in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:09.570506+00:00
---

# Manage Cloud APIs and Cloud Client Libraries in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Manage Cloud APIs and Cloud Client Libraries in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

To access Google Cloud products and services programmatically, you use [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview). These APIs expose a simple JSON REST interface. The recommended way to access the Cloud APIs is to use the Cloud Client Libraries.

Cloud Code makes it easy to add the Cloud Client Libraries for the Cloud APIs and language you're using to your project. In the same view, you can search for samples for each API and easily incorporate samples into your application.

## Browsing Cloud APIs

To explore all available Google Cloud APIs:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Cloud APIs** section.

The Cloud APIs view groups Cloud APIs by category.

  2. To view details of an API, click the API name. Details such as the service name, status, installation instructions for client libraries, documentation, and code samples are displayed.




## Enabling Cloud APIs

To enable Cloud APIs for a project using the API details page, follow these steps: 

  1. On the Cloud API details page, choose the project to enable the Cloud API for.

  2. Click **Enable API**. After the API is enabled, a message is displayed to confirm the change. 



## Adding client libraries to your project

In addition to exploring and enabling Cloud APIs using Cloud Code, you can add a language-specific client library to your project.

To install a client library, follow the instructions on the API details page for your language.

## Using API samples

You can search for and use code samples for each API in the API browser.

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Cloud APIs** section.

  2. To open the detail view, click the name of an API.

  3. To view code samples for the API, click **Code Samples**.

  4. To filter the list of samples, type text to search for or choose a programming language from the **Language** list.

  5. To view a sample, click the name of the sample. There are also options to copy the sample to your clipboard or view the sample in GitHub.




## Setting up authentication

After you've enabled the required APIs and added the necessary client libraries, you need to configure your application for it to be successfully authenticated. Your configuration depends on your type of development and the platform you're running on.

After you complete the authentication steps, your application can authenticate and is ready to be deployed.

### Local development

The Cloud Shell VM instance uses the Compute Engine default service account (the service account Google Kubernetes Engine uses by default) as its default service account. This means that when developing with Cloud Code on Cloud Shell, you don't need to set up any additional configuration when working with client libraries. Your application is authenticated and ready to run locally.

### Local development with APIs that require a service account

Some APIs, such as the Cloud Translation API, require a service account with appropriate permissions to authenticate your requests. For more information, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-gcloud). 

  1. To open a terminal, click **Terminal** > **New Terminal**.

  2. Create a service account to authenticate your API requests:
         
         gcloud iam service-accounts create \
         SERVICE_ACCOUNT_ID \
         --project PROJECT_ID

Replace the following values:

     * `SERVICE_ACCOUNT_ID`: the service account ID
     * `PROJECT_ID`: the project ID

To find these IDs, in Google Cloud, click the **Navigation menu** at the top-left of the screen, hold your pointer over **IAM & Admin** and click **Service Accounts**.

The **Email** column shows the unique `SERVICE_ACCOUNT_ID` and `PROJECT_ID` for each of your service accounts in the following format:

`SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com`

For example: A service account email address of `my-service-account@my-project.iam.gserviceaccount.com` has the following values:

     * `SERVICE_ACCOUNT_ID`: `my-service-account`
     * `PROJECT_ID`: `my-project`
  3. Grant your service account the appropriate role. The following sample command grants the Cloud Translation API User role. To determine the role to grant, see the documentation for the Cloud API you're using.
         
         gcloud projects \
         add-iam-policy-binding \
         PROJECT_ID \
         --member='serviceAccount:SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com' \
         --role='roles/cloudtranslate.user'

  4. Create a service account key:
         
         gcloud iam service-accounts keys \
         create key.json --iam-account \
         SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com

  5. Set the key as your default credentials:
         
         export \
          GOOGLE_APPLICATION_CREDENTIALS=key.json
         

  6. Optional: To permit users to [impersonate the service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts), run the `gcloud iam service-accounts add-iam-policy-binding` command to grant a user the Service Account User role (`roles/iam.serviceAccountUser`) on the service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
             SERVICE_ACCOUNT_ID@PROJECT_ID.iam.gserviceaccount.com \
             --member="user:USER_EMAIL" \
             --role="roles/iam.serviceAccountUser"

Replace the following values:

     * `USER_EMAIL`: the email address for the user



### Remote development

### GKE

Depending on the scope of your project, you can choose how you authenticate Google Cloud services on GKE: 

  * **(Development only)** **Note:** GKE cluster service account and access scope settings are permanent; after your cluster is created, these settings can't be changed. Specify the settings as recommended below. 
    1. [Create a GKE cluster](https://console.cloud.google.com/kubernetes/add) with the following settings: 
       * Make sure that you're using the service account GKE uses by default, the Compute Engine default service account, and that **Access scopes** is set at **Allow full access to all Cloud APIs** (both settings are accessible in the **Node Pools** > **Security** section). Since the Compute Engine service account is shared by all workloads deployed on your node, this method overprovisions permissions and should only be used for development.
       * Make sure that Workload Identity isn't enabled on your cluster (in the **Cluster** > **Security** section).
    2. Assign the necessary roles to your service account: 
       * If you're using the Compute Engine default service account, the correct IAM roles might already be applied.
       * For a list of IAM role types and predefined roles that you can grant to identities, see the [Understanding roles guide](https://docs.cloud.google.com/iam/docs/understanding-roles). For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * **(Recommended for production)**
    1. [Configure your GKE cluster and application with Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account.
    2. Configure your Kubernetes Deployment to reference the Kubernetes service account by setting the `.spec.serviceAccountName` field in your Kubernetes Deployment YAML file. If you're working on an app created from a Cloud Code sample application, this file is located under the kubernetes-manifests folder. 
    3. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app: 
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://docs.cloud.google.com/iam/docs/understanding-roles). For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



### Cloud Run

  1. To create a new unique service account for deploying your Cloud Run application, navigate to the Service Accounts page and then select the project that your secret is stored in. 

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Create service account**. 
  3. In the **Create service account** dialog, enter a descriptive name for the service account. 
  4. Change the **Service account ID** to a unique, recognizable value and then click **Create**. 
  5. If the Google Cloud service you're trying to access requires additional roles, grant the roles, click **Continue** , and then click **Done**. 
  6. To add your service account to your deploy configuration: 
     1. Using the Cloud Code status bar, choose the **Cloud Run: Deploy** command. 
     2. In the Cloud Run Deployment UI, under **Revision Settings** , in the **Service Account** field, specify your service account. 
![Advanced revision settings section expanded in Cloud Run: Deploy and Service Account field filled in with service account name of the format service-account-name@project-name.iam.gserviceaccount.com](https://docs.cloud.google.com/static/code/docs/vscode/images/service-account-cloud-run.png)



### Cloud Run

Depending on the scope of your project, you can choose how you authenticate Google Cloud services on GKE: 

  * **(Development only)** **Note:** GKE cluster service account and access scope settings are permanent; after your cluster is created, these settings can't be changed. Specify the settings as recommended below. 
    1. [Create a GKE cluster](https://console.cloud.google.com/kubernetes/add) with the following settings: 
       * Make sure that you're using the service account that GKE uses by default, the Compute Engine default service account, and that **Access scopes** is set at **Allow full access to all Cloud APIs** (both settings accessible in the **Node Pools** > **Security** section). Since the Compute Engine service account is shared by all workloads deployed on your node, this method overprovisions permissions and should only be used for development.
       * Make sure that Workload Identity isn't enabled on your cluster (in the **Cluster** > **Security** section).
    2. Assign the necessary roles to your service account: 
       * If you're using the Compute Engine default service account, the correct IAM roles might already be applied.
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://docs.cloud.google.com/iam/docs/understanding-roles). For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * **(Recommended for production)**
    1. [Configure your GKE cluster and application with Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate Google Cloud services on GKE. This associates your Kubernetes service account with your Google service account.
    2. To add your service account to your deploy configuration: 
       1. Using the Cloud Code status bar, choose the **Cloud Run: Deploy** command. 
       2. In the Cloud Run Deployment UI, under **Revision Settings** , in the **Service Account** field, specify your service account. 
![Advanced revision settings section expanded in Cloud Run: Deploy and Service Account field filled in with Kubernetes service account name of the format service-account-name@project-name.iam.gserviceaccount.com](https://docs.cloud.google.com/static/code/docs/vscode/images/k8s-service-account-cloud-run.png)
    3. If the Google Cloud service you're trying to access requires additional roles, grant them for the Google service account you're using to develop your app: 
       * For a list of IAM role types and predefined roles you can grant to identities, see the [Understanding roles guide](https://docs.cloud.google.com/iam/docs/understanding-roles). For steps to grant the roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



### Remote development with Secret Manager permissions enabled

If you're developing remotely, using a service account for authentication, and your application uses [secrets](https://docs.cloud.google.com/code/docs/shell/secret-manager), you need to complete a few more steps in addition to the remote development instructions. These steps assign your Google service account the [role required](https://docs.cloud.google.com/secret-manager/docs/access-control) to access a particular Secret Manager secret:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Secret Manager** section.

![Secret Manager in Cloud Code open with two secrets listed](https://docs.cloud.google.com/static/code/docs/vscode/images/secret-manager-ui.png)

  2. Right-click the secret and select **Edit Permissions in Cloud console**. This launches the Secret Manager configuration page for that secret in your web browser.

![Right-clicked secret in Secret Manager panel](https://docs.cloud.google.com/static/code/docs/vscode/images/secret-manager-permissions.png)

  3. In Google Cloud console, click **Permissions** and then click **Add**.

  4. In the **New principals** field, enter the name of your service account.

  5. In the **Select a role** field, choose the **Secret Manager Secret Accessor** role.

  6. Click **Save**.

Your service account now has permission to access this particular secret.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
