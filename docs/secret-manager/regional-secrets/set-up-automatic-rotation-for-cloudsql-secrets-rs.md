---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/set-up-automatic-rotation-for-cloudsql-secrets-rs/
title: Configure automatic rotation for Cloud SQL secrets \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:53.409543+00:00
---

# Configure automatic rotation for Cloud SQL secrets  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/set-up-automatic-rotation-for-cloudsql-secrets-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Configure automatic rotation for Cloud SQL secrets Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure automatic rotation for your Cloud SQL database credentials in Secret Manager. 

## Before you begin

  * Ensure that your Cloud SQL instance uses a supported database engine flavor, such as [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/introduction) or [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/introduction). 
  * Ensure that you are using a regional secret. Automatic rotation for Cloud SQL credentials is available only for regional secrets in Secret Manager. Global secrets don't support this feature. 
  * Ensure that you have an existing Cloud SQL instance and a database user. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance) and [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users). 
  * Ensure that you have permissions to manage the IAM policies on your Cloud SQL instance. For more information, see [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions). 



**Note:** Automatic rotation can cause temporary application downtime. During the short window between the database update and the secret alias update, applications that use the old password might experience connection failures. Ensure that your applications implement robust error handling (retries) to fetch the latest version upon authentication failure.

## Required roles

To get the permissions that you need to enable automatic rotation, ask your administrator to grant you a role that contains the following permissions: 

  * `cloudsql.users.list`
  * `cloudsql.users.update`



You can get these permissions either with [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). To see which roles are associated with which permissions, refer to [IAM roles for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a Cloud SQL database credential secret

To enable automatic rotation, you must create a secret of the type `Cloud SQL DB credentials`.

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab, and then click add **Create regional secret**.

  3. On the **Create regional secret** page, enter a name for the secret in the **Name** field.

  4. Select the **Set secret type** checkbox and choose `Cloud SQL DB credentials` as the secret type.

**Note** : You can't manually add secret versions to secrets with the `Cloud SQL DB credentials` secret type. Secret Manager automatically creates and updates secret versions during the rotation process.
  5. Choose the location where you want your regional secret to be stored from the **Region** list.

  6. (Optional) In the **Rotation** section, configure the rotation schedule for your secret. If you don't configure a rotation schedule, you must rotate the secret manually.

     1. Select the **Set rotation period** checkbox.

     2. In the **Rotation period** list, select from the default options or select **Custom** to configure your own rotation schedule.

     3. In the **Starting on** field, enter the rotation period start date and time.

  7. Click **Create secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID \
        --location=LOCATION \
        --secret-type=CLOUD_SQL_DB_CREDENTIALS

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID `
        --location=LOCATION `
        --secret-type=CLOUD_SQL_DB_CREDENTIALS

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID ^
        --location=LOCATION ^
        --secret-type=CLOUD_SQL_DB_CREDENTIALS

You should receive a response similar to the following:
    
    
    Created secret [projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID].
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {
      "secretType": "CLOUD_SQL_DB_CREDENTIALS"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID"

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
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2026-07-28T05:00:00Z",
      "secretType": "CLOUD_SQL_DB_CREDENTIALS",
      "etag": "\"1a2b3c4d\"",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID"
      }
    }
    

## Grant permissions to the built-in secret identity

Each secret has a unique identifier that distinguishes it from all other resources in your Google Cloud project. You must grant the built-in identity the required permissions that are needed to update credentials on your Cloud SQL instance. For more information, see [Granting roles to resources with built-in identities](https://docs.cloud.google.com/iam/docs/built-in-resource-identities).

### Console

  1. On the secret details page, go to the **Overview** tab.

  2. Note the **IAM principal identifier** of the secret.

The identifier has the following format: `principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID`.

  3. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click **Grant access**.

The **Grant access** panel appears.

  5. In the **New principals** field, enter the IAM principal identifier of the secret.

  6. From the **Select a role** list, select a role that grants the necessary permissions.

For more information, see [Required roles](https://docs.cloud.google.com/secret-manager/regional-secrets/set-up-automatic-rotation-for-cloudsql-secrets-rs#required-roles).

  7. Click **Save**.




### gcloud

#### Get the secret identity

Before you grant IAM permissions, describe the secret to get the `iamPolicyUidPrincipal` built-in identity. You specify this identity string in the `--member` flag when adding the IAM policy binding.

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID \
        --location=LOCATION \
        --format="value(policyMember.iamPolicyUidPrincipal)"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID `
        --location=LOCATION `
        --format="value(policyMember.iamPolicyUidPrincipal)"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID ^
        --location=LOCATION ^
        --format="value(policyMember.iamPolicyUidPrincipal)"

You should receive a response similar to the following:
    
    
    principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID
    

#### Grant IAM role to the secret identity

Grant an IAM role that contains the required Cloud SQL permissions (such as `cloudsql.users.update` and `cloudsql.users.list`, or the predefined `roles/cloudsql.admin` role) to the secret identity principal retrieved in the previous step:

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PROJECT_NUMBER: the numerical Google Cloud project number
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * SECRET_UID: the system-generated unique identifier of the secret resource
  * ROLE: the IAM role granted to the secret identity



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID" \
        --role="ROLE"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID `
        --member="principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID" `
        --role="ROLE"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID ^
        --member="principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID" ^
        --role="ROLE"

### REST

#### Get the secret identity

Before you grant IAM permissions, retrieve the secret details to get the `iamPolicyUidPrincipal` built-in identity. You specify this identity string in your request JSON when setting the IAM policy.

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    GET https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2026-07-28T05:00:00Z",
      "secretType": "CLOUD_SQL_DB_CREDENTIALS",
      "etag": "\"1a2b3c4d\"",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID"
      }
    }
    

#### Grant IAM role to the secret identity

Grant an IAM role that contains the required Cloud SQL permissions (such as `cloudsql.users.update` and `cloudsql.users.list`, or the predefined `roles/cloudsql.admin` role) to the secret identity principal retrieved in the previous step:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * ROLE: the IAM role granted to the secret identity
  * PROJECT_NUMBER: the numerical Google Cloud project number
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * SECRET_UID: the system-generated unique identifier of the secret resource



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy"

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
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwWWv0I7vBw=",
      "bindings": [
        {
          "role": "roles/cloudsql.admin",
          "members": [
            "principal://secretmanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/LOCATION/secrets/SECRET_UID"
          ]
        }
      ]
    }
    

## Rotate your secret

The rotation status of the newly created Cloud SQL secrets are `Disabled` until the first successful rotation. You must manually rotate your secret to verify permissions and start the automatic rotation schedule.

**Note:** You can manually rotate your secret at any time to respond to a security incident or to test your rotation logic. Manual rotations don't affect the existing automatic schedule.

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. Click the secret name to go to the secret details page.

  4. Click timer **Rotate**.

The **Rotate secret** panel appears.

  5. Specify the instance ID and the username of the Cloud SQL instance that you want to update.

  6. (Optional) Expand the **Additional settings** section to enter a specific password. If left blank, Secret Manager automatically generates a strong, random password.

  7. Click **Rotate**.




### gcloud

#### Enable managed rotation

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * INSTANCE_ID: the Cloud SQL [instance ID](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#instance-id-naming-2ndgen)
  * USERNAME: the Cloud SQL [database user account name](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users)



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets enable-managed-rotation SECRET_ID \
        --location=LOCATION \
        --instance-id=INSTANCE_ID \
        --username=USERNAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets enable-managed-rotation SECRET_ID `
        --location=LOCATION `
        --instance-id=INSTANCE_ID `
        --username=USERNAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets enable-managed-rotation SECRET_ID ^
        --location=LOCATION ^
        --instance-id=INSTANCE_ID ^
        --username=USERNAME

#### Manually rotate your secret

Trigger an immediate manual rotation to generate the initial secret version and verify connectivity.

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets rotate-secret SECRET_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets rotate-secret SECRET_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets rotate-secret SECRET_ID ^
        --location=LOCATION

You should receive a response similar to the following:
    
    
    Name: projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET_ID/versions/1
    State: ENABLED
    

### REST

#### Enable managed rotation

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * INSTANCE_ID: the Cloud SQL [instance ID](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#instance-id-naming-2ndgen)
  * USERNAME: the Cloud SQL [database user account name](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users)



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:enableManagedRotation

Request JSON body: 
    
    
    {
      "cloudSqlSingleUserCredentials": {
        "instanceId": "INSTANCE_ID",
        "username": "USERNAME"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:enableManagedRotation"

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
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:enableManagedRotation" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET_ID/versions/1",
      "createTime": "2026-07-28T05:00:00Z",
      "state": "ENABLED"
    }
    

#### Manually rotate your secret

Trigger an immediate manual rotation to generate the initial secret version and verify connectivity.

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:rotateSecret

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:rotateSecret"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:rotateSecret" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/secrets/SECRET_ID/versions/1",
      "createTime": "2026-07-28T05:00:00Z",
      "state": "ENABLED"
    }
    

Secret Manager attempts to update the credentials in your Cloud SQL instance. If successful, the **Rotation status** changes to `Enabled`, and the scheduled automatic rotation timer begins.

## What's next

  * Learn how to [set up rotation schedules for secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
