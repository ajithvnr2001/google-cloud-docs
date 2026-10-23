---
url: https://docs.cloud.google.com/sql/docs/mysql/workforce-authentication/
title: Workforce Identity Federation authentication \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:21.844029+00:00
---

# Workforce Identity Federation authentication  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/workforce-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Workforce Identity Federation authentication Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/workforce-authentication "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to configure and use Workforce Identity Federation (also known as third-party IAM authentication) with Cloud SQL. Workforce Identity Federation lets you use your existing identity provider (IdP), such as Microsoft Active Directory or Okta, to access Cloud SQL instances without requiring a Google Account.

Key benefits of using Workforce Identity Federation include:

  * **Reduced overhead** : No need to verify domains or synchronize identities to Cloud Identity.
  * **Enhanced security** : Centralized management of database access through your existing enterprise IdP.
  * **Ease of scale** : Suitable for large organizations with complex identity management needs.



For a detailed description of Workforce Identity Federation, see the [Workforce Identity Federation overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

## How it works

Workforce Identity Federation lets users authenticate to Google Cloud by using an external identity. For Cloud SQL, this means that principals from a workforce pool can connect to Cloud SQL for MySQL instances.

Cloud SQL supports Workforce Identity Federation through the `CLOUD_IAM_WORKFORCE_IDENTITY` user type. To grant access, Cloud SQL validates your workforce credentials and project-level IAM permission during login.

## Before you begin

Before you configure Workforce Identity Federation database authentication, make sure that you meet the following prerequisites:

  * Install the latest [](https://docs.cloud.google.com/sdk/gcloud#download_and_install_the)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  * [Configure a Workforce Identity Federation pool](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation) and provider in your Google Cloud organization.
  * [Set up service account impersonation for your workload](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#impersonation).
  * Ensure that your Cloud SQL instance is running MySQL version 8.0 or later.



### Roles and permissions

To get the permissions that you need to configure and use Workforce Identity Federation authentication, ask your administrator to grant you the following IAM roles on the organization: 

  * Manage an instance: [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 
  * Connect to instance: [Cloud SQL Instance User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser) (`roles/cloudsql.instanceUser`) 
  * Connect to an instance using the Cloud SQL Auth Proxy: [Cloud SQL Client ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.client) (`roles/cloudsql.client`) 
  * Manage IAM policy: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure Workforce Identity Federation authentication

The following sections tell you how to configure your instance to use Workforce Identity Federation authentication.

### Enable IAM authentication on the instance

To enable IAM authentication, set the `cloudsql_iam_authentication` flag to `on`.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Expand the **Customize your instance** section.
  5. Expand the **Connections** section.
  6. Under **Security** , select the **Enable Cloud SQL IAM authentication** checkbox.
  7. Click **Save**.



### gcloud

Use the following command to enable IAM authentication:
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --database-flags=cloudsql_iam_authentication=on
      

Replace `INSTANCE_NAME` with the name of the instance.

### Terraform

Add the `database_flags` block to your `google_sql_database_instance` resource:
    
    
    resource "google_sql_database_instance" "instance" {
      name             = "INSTANCE_NAME"
      database_version = "MYSQL_8_0"
      region           = "REGION"
    
      settings {
        tier = "db-f1-micro"
        database_flags {
          name  = "cloudsql_iam_authentication"
          value = "on"
        }
      }
    }
      

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `REGION`: the region where the instance resides.



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region
  * DATABASE_VERSION: enum string of the database version. For example: `MYSQL_8_0`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        }
        "databaseFlags":
        [
          {
            "name": "cloudsql_iam_authentication",
            "value": "on"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region
  * DATABASE_VERSION: enum string of the database version. For example: `MYSQL_8_0`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        }
        "databaseFlags":
        [
          {
            "name": "cloudsql_iam_authentication",
            "value": "on"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Add the workforce identity user to the instance

Add the external principal to your instance by using the `CLOUD_IAM_WORKFORCE_IDENTITY` type.

Make sure that the user ID that you use matches the value provided by the [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) from your workforce identity provider. Typically, this is configured as an email address—for example, `cruz@example.com`.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. The **Add a user account to instance INSTANCE_NAME** pane opens.
  5. Select **Workforce Identity Federation**.
  6. In the **Workforce user** field, enter the user ID for the user that you want to add.
  7. Click **Add**.



### gcloud

Run the following command to create the user:
    
    
    gcloud sql users create USER_ID \
        --instance=INSTANCE_NAME \
        --type=CLOUD_IAM_WORKFORCE_IDENTITY
      

Replace the following:

  * `USER_ID`: the email address for the user that you want to add—for example, `cruz@example.com`.
  * `INSTANCE_NAME`: the name of the instance.



### Terraform

Use the `google_sql_user` resource to define the workforce identity user:
    
    
    resource "google_sql_user" "workforce_user" {
      name     = "USER_ID" # e.g., "cruz@example.com"
      instance = "INSTANCE_NAME"
      type     = "CLOUD_IAM_WORKFORCE_IDENTITY"
    }
      

Replace the following:

  * `USER_ID`: the user ID for the user that you want to add—for example, `cruz@example.com`.
  * `INSTANCE_NAME`: the name of the instance.



### REST v1

**Create a user account**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "CLOUD_IAM_WORKFORCE_IDENTITY"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:44:16.656Z",
      "startTime": "2020-02-07T22:44:16.686Z",
      "endTime": "2020-02-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

**Create a user account**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "CLOUD_IAM_WORKFORCE_IDENTITY"
      }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:44:16.656Z",
      "startTime": "2020-02-07T22:44:16.686Z",
      "endTime": "2020-02-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Grant instance user role

Grant the [`roles/cloudsql.instanceUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser) role to the workforce identity principal or the entire pool.

### Console

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant Access**.
  3. In the **New principals** field, do one of the following:

     * To grant access to an individual principal, enter the workforce identity as a `principal`:

`principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USER_ID`

     * To grant access to the entire pool, enter the workforce pool as a `principalSet`:

`principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`

  4. In the **Role** list, select **Cloud SQL** > **Cloud SQL Instance User**.
  5. Optional: If you want to connect using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors, click **Add another role** and then select **Cloud SQL** > **Cloud SQL Client**.
  6. Click **Save**.



### gcloud

To grant access to an individual user, use the `gcloud projects add-iam-policy-binding` command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USER_ID" \
        --role="roles/cloudsql.instanceUser"
      

Replace the following:

  * `USER_ID`: the user ID for the user that you want to add—for example, `cruz@example.com`.
  * `POOL_ID`: the ID of the workforce pool.
  * `PROJECT_ID`: the identifier of the project that contains the instance.



To grant access to the entire workforce pool, use the `gcloud projects add-iam-policy-binding` command with the `principalSet` member format:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*" \
        --role="roles/cloudsql.instanceUser"
      

### Terraform

Use the `google_project_iam_member` resource to grant the role to the workforce principal:
    
    
    resource "google_project_iam_member" "workforce_user_iam" {
      project = "PROJECT_ID"
      role    = "roles/cloudsql.instanceUser"
      member  = "principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USER_ID"
    }
      

Replace the following:

  * `USER_ID`: the user ID for the user that you want to add—for example, `cruz@example.com`.
  * `POOL_ID`: the ID of the workforce pool.
  * `PROJECT_ID`: the identifier of the project that contains the instance.



### REST

To grant IAM policies using the API, retrieve the project's IAM policy by using the `getIamPolicy` method. Then, append the new binding to the policy, and finally apply the updated policy by using the `setIamPolicy` method.

The following is an example of a binding payload to append to your IAM policy:
    
    
    {
      "bindings": [
        {
          "role": "roles/cloudsql.instanceUser",
          "members": [
            "principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USER_ID"
          ]
        }
      ]
    }
      

Replace the following:

  * `USER_ID`: the user ID for the user that you want to add—for example, `cruz@example.com`.
  * `POOL_ID`: the ID of the workforce pool.



### Grant database privileges

You can specify the database roles to be granted when creating the workforce identity user, or manually grant the database privileges inside the database.

For example, to grant privileges manually:
    
    
    GRANT SELECT ON TABLE_NAME TO "USER_ID";
    

Replace the following:

  * `TABLE_NAME`: the name of the database table.
  * `USER_ID` the user ID of the workforce identity database user—for example, `cruz@example.com`.



## Connect to the instance

You can now connect to your instance by using either [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Auth Proxy.

### Use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)

You must first authenticate with your workforce identity before you can generate a login token.

  1. To authenticate by using Workforce Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command with the `--cred-file` flag:
         
         gcloud auth login --cred-file=CONFIGURATION_FILE
         

Replace `CONFIGURATION_FILE` with the path to the configuration file generated for your workforce identity provider.

  2. To connect by using a generated token, run the following command:

`bash export MYSQL_PWD=$(gcloud sql generate-login-token) mysql --host=INSTANCE_IP --user=USER_ID \ --database=DB_NAME --ssl-mode=REQUIRED`

Replace the following:

  3. `INSTANCE_IP`: the IP address of your Cloud SQL instance.

  4. `USER_ID`: the user ID of the workforce user—for example, `cruz@example.com`.

  5. `DB_NAME`: the name of the database you want to connect to.




### Using the Cloud SQL Auth Proxy

Start the proxy with the [`--auto-iam-authn`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect#--auto-iam-authn) flag:
    
    
    ./cloud-sql-proxy INSTANCE_CONNECTION_NAME --auto-iam-authn
    

For more information about the proxy, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/%0Amysql/sql-proxy).

## Restrictions and limitations

  * **Duplicate user ID across pools** : Cloud SQL can't distinguish between subjects with the same user ID across different workforce pools or identity providers. If you use multiple workforce pools or providers, you must use IAM policies to ensure that you don't grant the `roles/cloudsql.instanceUser` login permission to duplicate subject names from different pools or providers. This prevents unauthorized access from another pool or provider with the same user ID.
  * **Login quota** : There is a quota of 12,000 logins per minute for each instance, which includes both successful and unsuccessful login attempts. When the quota is exceeded, logins are temporarily unavailable. We recommend that you avoid frequent logins and restrict logins using [authorized networks](https://docs.cloud.google.com/sql/docs/%20mysql/authorize-networks).



## What's next

  * Learn more about [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).
  * Learn how to [Configure instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/create-edit-iam-instances).
  * Learn how to [Manage users with IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users).
  * Learn how to [Log in using IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-logins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
