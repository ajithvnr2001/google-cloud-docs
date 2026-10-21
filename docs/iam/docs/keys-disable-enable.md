---
url: https://docs.cloud.google.com/iam/docs/keys-disable-enable/
title: Disable and enable service account keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:05.776301+00:00
---

# Disable and enable service account keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/keys-disable-enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Disable and enable service account keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to disable and enable service account keys using the Google Cloud console, the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), the [Identity and Access Management API](https://docs.cloud.google.com/iam/docs/reference/rest), or one of the [Google Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  * Understand [service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds).




### Required roles

To get the permissions that you need to disable and enable service account keys, ask your administrator to grant you the [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on the project, or the service account whose keys you want to manage. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

IAM basic roles also contain permissions to manage service account keys. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Disable a service account key

Disabling a service account key prevents you from using the key to authenticate with Google APIs. You can enable a disabled key at any time.

**Important:** Disabling a service account key does not revoke short-lived credentials that were issued based on the key. To revoke a compromised short-lived credential, you must [disable or delete the service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling) that the credential represents. If you do so, any workload that uses the service account will immediately lose access to your resources.

Before you [delete a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting), we recommend that you disable the key, then wait until you are sure that the key is no longer needed. You can then delete the key.

You can view disabled keys in the Google Cloud console, but you cannot use the Google Cloud console to disable a key. Use the gcloud CLI or the REST API instead.

### gcloud

Execute the [`gcloud iam service-accounts keys disable`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/disable) command to disable a service account key.

Replace the following values:

  * `KEY_ID`: The ID of the key to disable. To find the key's ID, [list all keys for the service account](https://docs.cloud.google.com/iam/docs/keys-list-get#list-keys), identify the key that you want to disable, and then copy its ID.
  * `SA_NAME`: The name of the service account that the key belongs to.
  * `PROJECT_ID`: Your Google Cloud project ID.


    
    
    gcloud iam service-accounts keys disable KEY_ID \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --project=PROJECT_ID

Output:
    
    
    Disabled key [KEY_ID] for service account
    [SA_NAME@PROJECT_ID.iam.gserviceaccount.com]
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import java.io.IOException;
    
    
    public class DisableServiceAccountKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "gcloud-project-id";
        String serviceAccountName = "service-account-name";
        String serviceAccountKeyName = "service-account-key-name";
    
        disableServiceAccountKey(projectId, serviceAccountName, serviceAccountKeyName);
      }
    
      // Disables a service account key.
      public static void disableServiceAccountKey(String projectId,
                                                  String accountName,
                                                  String key) throws IOException {
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the service account name in which
        // you want to disable the key.
        // See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys#disabling
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
        String name = String.format("projects/%s/serviceAccounts/%s/keys/%s", projectId, email, key);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          iamClient.[disableServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_disableServiceAccountKey__org_jspecify_annotations_Nullable_com_google_iam_admin_v1_KeyName_)(name);
    
          System.out.println("Disabled service account key: " + name);
        }
      }
    }

### REST

The `[projects.serviceAccounts.keys.disable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/disable)` method disables a service account key. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_NAME`: The name of the service account whose key you want to disable.
  * `KEY_ID`: The ID of the key that you want to disable. To find the key's ID, list all keys for the service account, identify the key that you want to disable, and then copy its ID from the end of the `name` field. The key's ID is everything after `keys/`. 



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:disable

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:disable"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:disable" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/disable). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
    }
    

## Enable a service account key

After you disable a service account key, you can enable the key at any time, then use the key to authenticate with Google APIs.

You cannot use the Google Cloud console to enable service account keys. Use the gcloud CLI or the REST API instead.

### gcloud

Execute the [`gcloud iam service-accounts keys enable`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/enable) command to enable a service account key.

Replace the following values:

  * `KEY_ID`: The ID of the key to enable. To find the key's ID, [list all keys for the service account](https://docs.cloud.google.com/iam/docs/keys-list-get#list-keys), identify the key that you want to enable, and then copy its ID.
  * `SA_NAME`: The name of the service account that the key belongs to.
  * `PROJECT_ID`: Your Google Cloud project ID.


    
    
    gcloud iam service-accounts keys enable KEY_ID \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com\
        --project=PROJECT_ID

Output:
    
    
    Enabled key [KEY_ID] for service account
    [SA_NAME@PROJECT_ID.iam.gserviceaccount.com]
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import java.io.IOException;
    
    
    public class EnableServiceAccountKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "gcloud-project-id";
        String serviceAccountName = "service-account-name";
        String serviceAccountKeyName = "service-account-key-name";
    
        enableServiceAccountKey(projectId, serviceAccountName, serviceAccountKeyName);
      }
    
      // Enables a service account key.
      public static void enableServiceAccountKey(String projectId,
                                                 String accountName,
                                                 String key) throws IOException {
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the service account name in which
        // you want to enable the key.
        // See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys#enabling
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
        String name = String.format("projects/%s/serviceAccounts/%s/keys/%s", projectId, email, key);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          iamClient.[enableServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_enableServiceAccountKey__org_jspecify_annotations_Nullable_com_google_iam_admin_v1_KeyName_)(name);
    
          System.out.println("Enabled service account key: " + name);
        }
      }
    }

### REST

The `[projects.serviceAccounts.keys.enable](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/enable)` method enables a service account key. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_NAME`: The name of the service account whose key you want to enable.
  * `KEY_ID`: The ID of the key that you want to enable. To find the key's ID, list all keys for the service account, identify the key that you want to enable, and then copy its ID from the end of the `name` field. The key's ID is everything after `keys/`. 



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:enable

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:enable"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID:enable" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/enable). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
    }
    

## What's next

  * Learn how to [delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting).
  * Learn how to [list and get service account keys](https://docs.cloud.google.com/iam/docs/keys-list-get).
  * Learn how to use service account keys to [authenticate as a service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).
  * Learn about [alternatives to service account keys for authentication](https://docs.cloud.google.com/docs/authentication#auth-decision-tree).
  * Understand the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
