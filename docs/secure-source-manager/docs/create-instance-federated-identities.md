---
url: https://docs.cloud.google.com/secure-source-manager/docs/create-instance-federated-identities/
title: Create a Secure Source Manager instance to use with federated identities \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:04.997910+00:00
---

# Create a Secure Source Manager instance to use with federated identities  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/create-instance-federated-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Create a Secure Source Manager instance to use with federated identities Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to create a Secure Source Manager instance that uses Workforce Identity Federation with an external identity provider (IdP). 

For more information about Workforce Identity Federation, see [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

For information about limitations to Workforce Identity Federation in Secure Source Manager, see [Identity federation: products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#secure-source-manager).

Secure Source Manager is a single-tenant service. A single Secure Source Manager instance should only include users from one Google Cloud customer unless multiple companies who have a contractual relationship need to use a single instance for collaboration.

If you're working with multiple companies and want to collaborate with them on source code, we recommend you create a separate instance for each company.

**Note:** Secure Source Manager doesn't support domain-scoped projects.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Secure Source Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securesourcemanager.googleapis.com)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. Enable the Secure Source Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securesourcemanager.googleapis.com)

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Data encryption

By default, Google Cloud automatically [encrypts data at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using Google-owned and Google-managed encryption keys. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can create Secure Source Manager instances that are encrypted with [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/secure-source-manager/docs/cmek).

Don't store sensitive data in instance IDs or label key-value pairs because they are not encrypted with CMEK.

If you are creating your first Secure Source Manager instance in your project, you must manually create the Secure Source Manager service agent by running the following command:
    
    
    gcloud beta services identity create \
        --service=securesourcemanager.googleapis.com \
        --project=PROJECT_ID
    

Here, `PROJECT_ID` is the project ID of the project where you create your Secure Source Manager instance.

After you create the Secure Source Manager service agent, you must grant the Secure Source Manager Service Agent role (`roles/securesourcemanager.serviceAgent`) to the principal service-PROJECT-NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com or the instance creation will fail.

## Set up Workforce Identity Federation

Before you create an instance, you must set up a Workforce Identity Federation pool and provider.

  1. [Create a Workforce Identity Federation pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#create_a_pool).

**Note:** The **session duration** for your workforce identity pool defaults to one hour. We recommend increasing the duration to prevent users from reauthenticating repeatedly during their workday.
  2. [Configure your workforce identity pool provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#configure-provider) with the following [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings):

     * `google.subject`
     * `google.email`



## Create an instance

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * INSTANCE_ID: the name of the instance you want to create.
  * LOCATION: the region where you want to create the instance. For information on supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).
  * PROJECT_ID: the project ID of the project you want to create an instance in.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager instances create INSTANCE_ID --region=LOCATION --project=PROJECT_ID --enable-workforce-identity-federation

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager instances create INSTANCE_ID --region=LOCATION --project=PROJECT_ID --enable-workforce-identity-federation

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager instances create INSTANCE_ID --region=LOCATION --project=PROJECT_ID --enable-workforce-identity-federation

A long-running create instance operation starts. The output looks like the following:
    
    
      Create request issued for [my-instance].
      done: false
      metadata:
        '@type': type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata
        apiVersion: v1
        createTime: '2023-02-27T20:57:52.315609549Z'
        requestedCancellation: false
        target: projects/my-project/locations/us-central1/instances/my-instance
        verb: create
      name: projects/my-project/locations/us-central1/operations/operation-1234567894561-5ec69948c0f2b-60dd727f-a9b97a2e
    

Where `projects/my-project/locations/us-central1/operations/operation-1234567894561-5ec69948c0f2b-60dd727f-a9b97a2e` is the `OPERATION_NAME`. 

Record the `OPERATION_NAME` as you will need to use it to check the status of the operation.

It takes up to 60 minutes to create the instance.

###  API 

Before you run this command, replace the following values:

  * INSTANCE_ID: the name of the instance you want to create.
  * LOCATION: the region where you want to create the instance. For information about supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).
  * PROJECT_ID: the project ID of the project you want to create an instance in.



Run the following command:
    
    
    curl \
        -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=INSTANCE_ID \
        -H "Content-Type: application/json" \
        -d "{workforce_identity_federation_config: {enabled: true}}"
    
    

A long-running create instance operation starts. The output resembles the following:
    
    
    {
    "name": "OPERATION_NAME",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata",
      "createTime": "2022-11-01T14:31:32.420469714Z",
      "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
      "verb": "create",
      "requestedCancellation": false,
      "apiVersion": "v1"
    },
    "done": false
    }
    

This example output includes the following values:

  * `OPERATION_NAME`: the operation name—for example, `projects/my-project/locations/us-central1/operations/operation-1234567894561-5ec69948c0f2b-60dd727f-a9b97a2e`.
  * `PROJECT_ID`: the Google Cloud project.
  * `LOCATION`: the region where the instance is located.



Record the `OPERATION_NAME` because you need to use it to check the status of the operation.

It takes up to 60 minutes to create the instance.

###  Terraform 

The following example creates a Secure Source Manager instance with Workforce Identity Federation enabled:
    
    
    resource "google_secure_source_manager_instance" "instance" {
      instance_id = "INSTANCE_ID"
      location    = "LOCATION"
      project     = "PROJECT_ID"
      workforce_identity_federation_config {
        enabled = true
      }
    }
    

## Check operation status

###  gcloud

Before using any of the command data below, make the following replacements: 

  * OPERATION_NAME: the operation name from your create command response.
  * LOCATION: the instance region.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager operations describe OPERATION_NAME --region=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager operations describe OPERATION_NAME --region=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud source-manager operations describe OPERATION_NAME --region=LOCATION

Once the instance is ready, the response will look similar to the following:
    
    
      "name": "projects/my-project/locations/us-central1/operations/operation-123456789012-5ec69948c0f2b-60dd727f-a9b97a2e",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata",
        "createTime": "2022-11-01T14:31:32.420469714Z",
        "endTime": "2022-11-01T14:48:34.140378114Z",
        "target": "projects/my-project/locations/us-central1/instances/my-instance",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.Instance",
        "name": "projects/my-project/locations/us-central1/instances/my-instance",
        "createTime": "2022-11-01T14:31:32.416413630Z",
        "updateTime": "2022-11-01T14:31:32.416413630Z",
        "labels": {
          "ldap": "user",
          "source": "manual"
        },
        "state": "ACTIVE",
        "hostConfig": {
          "html": "my-instance-098765432109.us-central1.sourcemanager.dev",
          "api": "my-instance-098765432109-api.us-central1.sourcemanager.dev",
          "gitHttp": "my-instance-098765432109-git.us-central1.sourcemanager.dev"
        }
      }
    

Where the `my-instance-098765432109.us-central1.sourcemanager.dev` is the instance HTML URL.

it's possible for the status check to report completion before the instance is fully operational. If you encounter errors accessing the instance after creation, wait 60 minutes and try again before reaching out for assistance through Secure Source Manager Support at [secure-source-manager-support@google.com](mailto:secure-source-manager-support@google.com).

###  API 

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the operation name from your create command response.



HTTP method and URL: 
    
    
    GET https://securesourcemanager.googleapis.com/v1/OPERATION_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.googleapis.com/v1/OPERATION_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

Once the instance is ready, the response will look similar to the following:
    
    
      "name": "projects/my-project/locations/us-central1/operations/operation-123456789012-5ec69948c0f2b-60dd727f-a9b97a2e",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata",
        "createTime": "2024-10-28T15:37:39.009812863Z",
        "endTime": "2024-10-28T16:10:58.416640259Z",
        "target": "projects/my-project/locations/us-central1/instances/my-instance",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.securesourcemanager.v1.Instance",
        "name": "projects/my-project/locations/us-central1/instances/my-instance",
        "createTime": "2024-10-28T15:37:39.004550840Z",
        "updateTime": "2024-10-28T15:37:39.867857246Z",
        "state": "ACTIVE",
        "hostConfig": {
          "html": "my-instance-326202322590.us-central1.sourcemanager.dev",
          "api": "my-instance-326202322590-api.us-central1.sourcemanager.dev",
          "gitHttp": "my-instance-326202322590-git.us-central1.sourcemanager.dev",
          "gitSsh": "my-instance-326202322590-ssh.us-central1.sourcemanager.dev"
        },
        "workforceIdentityFederationConfig": {
          "enabled": true
        }
      }
    

Where the `my-instance-098765432109.us-central1.sourcemanager.dev` is the instance HTML URL.

it's possible for the status check to report completion before the instance is fully operational. If you encounter errors accessing the instance after creation, wait 60 minutes and try again before reaching out for assistance through Secure Source Manager Support at [secure-source-manager-support@google.com](mailto:secure-source-manager-support@google.com).

Copy the HTML URL from the successful check status response. You need this URL to access the instance through its web interface.

## Access the instance

After the instance is created, you can access it through its web interface using a browser.

**Note:** To [create repositories](https://docs.cloud.google.com/secure-source-manager/docs/create-repository) in the instance you need the Repo Creator role (`roles/securesourcemanager.repoCreator`) on the instance project and the Instance Repository Creator role (`roles/securesourcemanager.instanceRepositoryCreator`) on the Secure Source Manager instance.

  1. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

     * INSTANCE_ID with the instance name.
     * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION with the instance's region.

An OAuth screen appears requesting your provider name.

  2. Enter your workforce identity provider's name in the following format:
         
         locations/global/workforcePools/POOL_ID/providers/PROVIDER_ID
         

Replace the following:

     * `POOL_ID` with your Workforce Identity Federation pool ID.
     * `PROVIDER_ID` with your Workforce Identity Federation provider ID.

For more information about Workforce Identity Federation pools and providers, see [Manage Workforce Identity Federation identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers).

You are prompted to sign in using your provider credentials.

  3. Sign in using your provider credentials.

  4. The Secure Source Manager web interface opens. From here, you can create and view repositories, issues, and pull requests.

You must sign in again through the web interface after the **session duration** in your Workforce Identity Federation pool expires.




## Create your gcloud CLI login configuration

To authenticate with your workforce identity pool credentials to your Secure Source Manager instance using gcloud CLI commands or Git commands, you must create a login configuration with your workforce identity pool.

To create a workforce identity pool login configuration, follow the instructions in [Obtain short-lived tokens for Workforce Identity Federation](https://docs.cloud.google.com/sdk/docs/authenticate#federated-user-identities) to create a browser-based sign-in with the gcloud CLI.

After you have authenticated, you can use Git commands to interact with your Secure Source Manager instance. To get started with Git, see [Use Git source code management](https://docs.cloud.google.com/secure-source-manager/docs/use-git).

## What's next

  * [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).
  * [Grant users repository access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-repository-access).
  * [Control access with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
