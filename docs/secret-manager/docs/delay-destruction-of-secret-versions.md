---
url: https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions/
title: Delay destruction of secret versions \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:44.750394+00:00
---

# Delay destruction of secret versions  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/delay-destruction-of-secret-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Delay destruction of secret versions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up the delayed destruction of secret versions, update or remove the destruction delay duration, and restore secret versions that are scheduled for destruction.

By default, when a user chooses to destroy a secret version in Secret Manager, the secret material is destroyed immediately and permanently. However, users with the Secret Manager Admin role can set up delayed destruction of secret versions, which ensures that the secret version isn't destroyed immediately upon request and remains recoverable for a configurable duration.

When delayed destruction is enabled on the secret and you destroy a secret version, the following occurs:

  * The version is disabled, preventing its use.

  * The system schedules the version for permanent destruction at the end of the delay period.

  * After the delay period expires, the secret version is permanently and irrevocably destroyed.




## Benefits

This feature provides the following benefits:

  * An extra layer of protection against accidental or malicious destruction of critical secret material. Any user with the [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) role can [destroy a secret version](https://docs.cloud.google.com/secret-manager/docs/destroy-secret-version). This is an irreversible action. By setting up delayed destruction, you can prevent the immediate destruction of secret versions. You can grant users the minimum access required to manage the lifecycle of secret versions so that you can monitor and prevent any accidental destruction of sensitive data.

  * Destroying a secret version triggers a `SECRET_VERSION_DESTROY_SCHEDULED` [notification](https://docs.cloud.google.com/secret-manager/docs/event-notifications#events) to the Pub/Sub topics configured on the secret. Users with the Secret Manager Admin role can cancel the scheduled destruction and restore the secret version by either [enabling](https://docs.cloud.google.com/secret-manager/docs/enable-secret-version) or [disabling](https://docs.cloud.google.com/secret-manager/docs/disable-secret-version) the secret version.




## Before you begin

  1. Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

  2. Set up authentication.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles

To get the permissions that you need to set up delayed destruction of secret versions, ask your administrator to grant you the [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) IAM role on a secret. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up delayed destruction

You can enable the delayed destruction of a secret version when you create the secret or when you update the secret. To set up delayed destruction, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create secret**.

  3. On the **Create secret** page, enter a name for the secret in the **Name** field.

  4. Enter a value for the secret (for example, `abcd1234`). You can also upload a text file containing the secret value using the **Upload file** option. This action automatically creates the secret version.

  5. Go to the **Delay secret version destroy** section, and then select the **Set duration for delayed destruction** checkbox.

  6. In the **Destruction delay duration** field, enter the duration in days. The minimum value that you can enter is 1 day; the maximum value is 1000 days.

  7. Click **Create secret**.

To enable this feature on an existing secret, go to the [**Edit secret**](https://docs.cloud.google.com/secret-manager/docs/edit-secrets) page, and then configure the destruction delay duration.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret.
  * TTL_DURATION: the destruction delay duration for the secret versions. You can enter the duration in any format, for example, days, hours, or seconds. The minimum duration required is 1 day while maximum duration can be set to 1000 days.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --version-destroy-ttl=TTL_DURATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --version-destroy-ttl=TTL_DURATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --version-destroy-ttl=TTL_DURATION

The response contains the newly created secret. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * TTL_DURATION: the destruction delay duration for the secret versions. Enter duration in seconds. Note that the minimum duration required is 1 day while maximum duration can be set to 1000 days.



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {"replication": {"automatic": {}}, "version_destroy_ttl":"TTL_DURATION"}

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "name":"projects/PROJECT_ID/secrets/SECRET_ID",
    "replication":{
       "automatic":{
    
       }
    },
    "createTime":"2023-10-16T17:10:16.345401Z",
    "etag":"\"1607d90ee3d84c\"",
    "versionDestroyTtl":"TTL_DURATION"
    }
    

Delayed destruction doesn't apply in the following scenarios:

  * When a secret is [deleted](https://docs.cloud.google.com/secret-manager/docs/delete-secrets), all the secret material and related secret versions are deleted immediately.

  * When an expiration date is set on the secret and the secret expires, all the secret versions are destroyed immediately even if delayed destruction is enabled on the secret.




## Update destruction delay duration

To update the destruction delay duration, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. To edit a secret, use one of the following methods:

     * Click more_vert**Actions** for the secret that you want to edit, and then click **Edit**.

     * Click the secret name to go to the secret details page. On the secret details page, click edit**Edit secret**.

  3. On the **Edit secret** page, go to the **Delay secret version destroy** section. Update the delay duration as required, and then click **Update secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * TTL_DURATION: the destruction delay duration for the secret versions



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --version-destroy-ttl=TTL_DURATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --version-destroy-ttl=TTL_DURATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --version-destroy-ttl=TTL_DURATION

The response contains the newly created secret. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TTL_DURATION: the destruction delay duration for the secret versions



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl

Request JSON body: 
    
    
    {
      "version_destroy_ttl":"TTL_DURATION"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/PROJECT_ID/secrets/SECRET_ID",
      "replication":{
         "automatic":{
    
         }
      },
      "createTime":"2023-10-16T17:10:16.345401Z",
      "etag":"\"1607d90ee3d84c\"",
      "versionDestroyTtl":"TTL_DURATION"
    }
    

The secret versions that are affected by the destruction delay duration depends on the following:

  * When delayed destruction is set for the first time on the secret, the destruction delay duration affects all the active (enabled and disabled) versions of the secret.

  * When the destruction delay duration is updated or removed, the changes reflect only on new secret versions on which the destroy action is attempted. The secret versions that are already scheduled for destruction will continue to be destroyed at the scheduled destruction time.




## Disable delayed destruction

To disable delayed destruction of versions, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. To edit a secret, use one of the following methods:

     * Click more_vert**Actions** for the secret that you want to edit, and then click **Edit**.

     * Click the secret name to go to the secret details page. On the secret details page, click edit**Edit secret**.

  3. On the **Edit secret** page, go to the **Delay secret version destroy** section. Clear the **Set duration for delayed destruction** checkbox, and then click **Update secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --remove-version-destroy-ttl

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --remove-version-destroy-ttl

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --remove-version-destroy-ttl

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=version_destroy_ttl" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/PROJECT_ID/secrets/SECRET_ID",
      "replication":{
         "automatic":{
    
         }
      },
      "createTime":"2023-10-16T17:10:16.345401Z",
      "etag":"\"1607d90ee3d84c\""
    }
    

## Schedule secret versions for delayed destruction

To schedule a secret version for delayed destruction, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click a secret to access its versions. Delayed destruction of versions must be configured on this secret.

  3. On the secret details page, in the **Versions** tab, select the secret version that you want to destroy.

  4. Click more_vert**Actions** , and then click **Destroy**.

  5. In the confirmation dialog that appears, enter the secret ID to confirm, and then click **Schedule selected versions for destruction**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_VERSION_ID: the ID of the version or fully qualified identifier for the version
  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions destroy SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions destroy SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions destroy SECRET_VERSION_ID --secret=SECRET_ID

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * VERSION_ID: the ID of the version or fully qualified identifier for the version



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:destroy

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:destroy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:destroy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID",
      "createTime":"2023-10-16T17:21:55.920036Z",
      "state":"DISABLED",
      "replicationStatus":{
         "automatic":{
    
         }
      },
      "etag":"\"1607d8b2fc1cf4\"",
      "scheduledDestroyTime":"2023-10-16T17:26:57.459395960Z"
    }
    

The secret version is immediately disabled and scheduled for destruction after the destruction delay duration expires. You can see the exact date and time on which the version will be destroyed under the **Scheduled for destruction on** column in the **Versions** table.

## Restore secret versions

You can restore a secret version that is scheduled for destruction by enabling or disabling the secret version.

### Enable a secret version that is scheduled for destruction

To enable a secret version that is scheduled for destruction, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click a secret to access its versions.

  3. On the secret details page, in the **Versions** tab, select the secret version that is scheduled for destruction.

  4. Click more_vert**Actions** , and then click **Enable**.

  5. In the confirmation dialog that appears, click **Enable selected versions**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_VERSION_ID: the ID of the version or fully qualified identifier for the version
  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions enable SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions enable SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions enable SECRET_VERSION_ID --secret=SECRET_ID

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * VERSION_ID: the ID of the version or fully qualified identifier for the version



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:enable

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:enable"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:enable" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID",
      "createTime":"2023-10-16T17:21:55.920036Z",
      "state":"ENABLED",
      "replicationStatus":{
         "automatic":{
    
         }
      },
      "etag":"\"1607d8b3e8e1bc\""
    }
    

### Disable a secret version that is scheduled for destruction

To disable a secret version that is scheduled for destruction, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click a secret to access its versions.

  3. On the secret details page, in the **Versions** tab, select the secret version that is scheduled for destruction.

  4. Click more_vert**Actions** , and then click **Disable**.

  5. In the confirmation dialog that appears, click **Disable selected versions**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_VERSION_ID: the ID of the version or fully qualified identifier for the version
  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable SECRET_VERSION_ID --secret=SECRET_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable SECRET_VERSION_ID --secret=SECRET_ID

The response contains the disabled version of the secret. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * VERSION_ID: the ID of the version or fully qualified identifier for the version



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name":"projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID",
      "createTime":"2023-10-16T17:21:55.920036Z",
      "state":"DISABLED",
      "replicationStatus":{
         "automatic":{
    
         }
      },
      "etag":"\"1607d8b3e8e1bc\""
    }
    

## What's next

  * Learn how to [ensure data integrity](https://docs.cloud.google.com/secret-manager/docs/data-integrity).
  * Learn about [best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
