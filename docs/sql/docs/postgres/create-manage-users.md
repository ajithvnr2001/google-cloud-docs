---
url: https://docs.cloud.google.com/sql/docs/postgres/create-manage-users/
title: Create and manage users \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:29.067583+00:00
---

# Create and manage users  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/create-manage-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Create and manage users Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users "View this page for the SQL Server database engine")

This page describes how to enable and use Cloud SQL built-in authentication.

For an overview, see [Cloud SQL built-in database authentication](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication). 

## Before creating users

  1. Create a Cloud SQL instance. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance). 
  2. Enable password policies for the instance. For more information, see [Instance password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies).
  3. If you plan to use your database's administrative client to manage users, then do the following:

     1. Connect the client to your instance. See [Connection options for external applications](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods).

     2. Configure the default user on the instance by setting the password. See Set the password for the default user account. 




## Set the password for the default user account

When you create a new Cloud SQL instance, you must set a password for the default user account before you can connect to the instance.

For Cloud SQL for PostgreSQL, the default user is `postgres`. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Find the `postgres` user and select **Change password** from the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png). 
  5. Provide a strong password that you can remember and click **OK**.



### gcloud

Use the [ `gcloud sql users set-password`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password) command as follows to set the password for the default user.

Replace INSTANCE_NAME with the name of the instance before running the command.
    
    
    gcloud sql users set-password postgres \
    --instance=INSTANCE_NAME \
    --prompt-for-password

### REST v1

To update the password for the default user account, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID
  * user-id: The ID of the user
  * password: The password for the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id

Request JSON body: 
    
    
    {
      "name": "user-id",
      "password": "password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To update the password for the default user account, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID
  * user-id: The ID of the user
  * password: The password for the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id

Request JSON body: 
    
    
    {
      "name": "user-id",
      "password": "password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Create a user

After setting up the default user account, you can create other users.

When you create a built-in user, you can assign the user with one or more database roles.

To assign a custom database role to a user, you must create the role in the PostgreSQL database first. To create a role in PostgreSQL, see [Database roles](https://www.postgresql.org/docs/current/static/database-roles.html). 

### Console

**Note** : You can't assign database roles to PostgreSQL users by using the Google Cloud console. To assign a database role or roles to a PostgreSQL user, use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API instead.

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. 

In the **Add a user account to instance _instance_name_** page, you can choose whether the user authenticates with the built-in database method (username and password) or as an [IAM user](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users). 

  5. Select **Built-in authentication** (the default) and add the following information: 
     * A **User name**.
     * Optional. A **Password**. Provide a strong password that you can remember.
  6. Click **Add**.



If you create a PostgreSQL user that uses built-in authentication, then the user is granted the `cloudsqlsuperuser` role automatically. The user is provided with the following privileges associated with this role: `CREATEROLE`, `CREATEDB`, and `LOGIN`.

If you want to change the privileges for the user, then you can create and assign one or more custom PostgreSQL database roles when you create the user in Cloud SQL. If you assign one or more custom database roles when you create the user in Cloud SQL, then the user isn't granted the `cloudsqlsuperuser` role.

If you need to change the attributes for these users, then use the [ALTER ROLE](https://www.postgresql.org/docs/current/static/sql-alterrole.html) command in the `psql` client. Not all attributes can be modified with `ALTER ROLE`. Exceptions include the `NOSUPERUSER` and `NOREPLICATION` roles. 

For more information about these user accounts and privileges, see [ Other PostgreSQL user accounts](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users). 

### gcloud

To create a user, use the [ `gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command.

Replace the following:

  * USER_NAME: the user name.
  * INSTANCE_NAME: the name of the instance.
  * PASSWORD: the password for the user.
  * ROLE_1, ROLE_2 ..., ROLE__N_ : optional. The database role or roles to assign to the user.


    
    
    gcloud sql users create USER_NAME \
    --instance=INSTANCE_NAME \
    --password=PASSWORD \
    --database-roles=ROLE_1, ROLE_2, ..., ROLE__N_

If you create a PostgreSQL user that uses built-in authentication, then the user is granted the `cloudsqlsuperuser` role automatically. The user is provided with the following privileges associated with this role: `CREATEROLE`, `CREATEDB`, and `LOGIN`.

If you want to change the privileges for the user, then you can create and assign one or more custom PostgreSQL database roles when you create the user in Cloud SQL. If you assign one or more custom database roles when you create the user in Cloud SQL, then the user isn't granted the `cloudsqlsuperuser` role.

If you need to change the attributes for these users, then use the [ALTER ROLE](https://www.postgresql.org/docs/current/static/sql-alterrole.html) command in the `psql` client. Not all attributes can be modified with `ALTER ROLE`. Exceptions include the `NOSUPERUSER` and `NOREPLICATION` roles. 

For more information about these user accounts and privileges, see [ Other PostgreSQL user accounts](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users). 

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

When you create a user, you can add user password policy parameters.

### Terraform

To create a user, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "random_password" "pwd" {
      length  = 16
      special = false
    }
    
    resource "google_sql_user" "user" {
      name     = "user"
      instance = google_sql_database_instance.default.name
      password = random_password.pwd.result
    }

You can also create a user and assign database roles.
    
    
    resource "google_sql_user" "builtin_user" {
      name     = "test-user1"
      password = "password"
      instance = google_sql_database_instance.default.name
      # Specify the list of database roles to be granted to the user
      # The database roles must exist in the database.
      database_roles = ["cloudsqlsuperuser"]
    }

#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### REST v1

To create a user, use a POST request with the [ users:insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/insert) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password for the user
  * ROLE_1, ROLE_2 ..., ROLE__N_ : optional. The database role or roles to assign to the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ]
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If you create a PostgreSQL user that uses built-in authentication, then the user is granted the `cloudsqlsuperuser` role automatically. The user is provided with the following privileges associated with this role: `CREATEROLE`, `CREATEDB`, and `LOGIN`.

If you want to change the privileges for the user, then you can create and assign one or more custom PostgreSQL database roles when you create the user in Cloud SQL. If you assign one or more custom database roles when you create the user in Cloud SQL, then the user isn't granted the `cloudsqlsuperuser` role.

If you need to change the attributes for these users, then use the [ALTER ROLE](https://www.postgresql.org/docs/current/static/sql-alterrole.html) command in the `psql` client. Not all attributes can be modified with `ALTER ROLE`. Exceptions include the `NOSUPERUSER` and `NOREPLICATION` roles. 

For more information about these user accounts and privileges, see [ Other PostgreSQL user accounts](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users). 

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

When you create a user, you can add user password policy parameters.

### REST v1beta4

To create a user, use a POST request with the [ users:insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/insert) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password for the user
  * ROLE_1, ROLE_2 ..., ROLE__N_ : optional. The database role or roles to assign to the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ]
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If you create a PostgreSQL user that uses built-in authentication, then the user is granted the `cloudsqlsuperuser` role automatically. The user is provided with the following privileges associated with this role: `CREATEROLE`, `CREATEDB`, and `LOGIN`.

If you want to change the privileges for the user, then you can create and assign one or more custom PostgreSQL database roles when you create the user in Cloud SQL. If you assign one or more custom database roles when you create the user in Cloud SQL, then the user isn't granted the `cloudsqlsuperuser` role.

If you need to change the attributes for these users, then use the [ALTER ROLE](https://www.postgresql.org/docs/current/static/sql-alterrole.html) command in the `psql` client. Not all attributes can be modified with `ALTER ROLE`. Exceptions include the `NOSUPERUSER` and `NOREPLICATION` roles. 

For more information about these user accounts and privileges, see [ Other PostgreSQL user accounts](https://docs.cloud.google.com/sql/docs/postgres/users#other_postgresql_users). 

Username length limits are the same for Cloud SQL as for on-premises PostgreSQL. 

When you create a user, you can add user password policy parameters.

### psql Client

  1. At the `psql` prompt, create the user: 
         
         CREATE USER USER_NAME
               WITH PASSWORD PASSWORD
               ATTRIBUTE1
               ATTRIBUTE2...;
           

Enter the password when prompted.

For more information about role attributes, see the [ PostgreSQL documentation](https://www.postgresql.org/docs/current/static/role-attributes.html).

**NOTE:** When using EXTENSION [ `pg_stat_statements`](https://www.postgresql.org/docs/9.6/pgstatstatements.html), SQL statements from all users are visible to users with the `cloudsqlsuperuser` ROLE (in PostgreSQL version 10 and higher). Don't use plain text passwords in queries. 
  2. You can confirm the user creation by displaying the user table: 
         
         SELECT * FROM pg_roles;
           




## Set a user password policy

You can set a password policy with the built-in authentication type.

**Note:** Password policies don't apply to encrypted passwords. If you set user password policies, and you want to deactivate the [password policy for the instance](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#instance_password_policies), then you must first remove all user password policies.

### gcloud

To set the user password policy, use the [ `gcloud sql users set-password-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy) command.

Replace the following:

  * USER_NAME: The user name. 
  * INSTANCE_NAME: The name of the instance.
  * HOST: The user's host name as a specific IP address, address range, or any host (`%`).
  * PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS: Optional: The number of times that a user can try the password incorrectly before the account is locked. Use `--password-policy-enable-failed-attempts-check` to enable and `--no-password-policy-enable-failed-attempts-check` to disable the check.
  * PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION: Optional: Specifies the number of days after which the password expires and the user needs to create a new one.


    
    
    gcloud sql users set-password-policy USER_NAME \
    --instance=INSTANCE_NAME \
    --host=HOST \
    --password-policy-enable-failed-attempts-check \
    --password-policy-allowed-failed-attempts=PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS \
    --password-policy-password-expiration-duration=PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION

To remove a user password policy, use the `--clear-password-policy` parameter. 
    
    
    gcloud sql users set-password-policy USER_NAME \
    --instance=INSTANCE_NAME \
    --host=HOST \
    --clear-password-policy

To view the user password policy, see  List users.

### REST v1

To set a user password policy, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password of the user
  * FAILED_ATTEMPTS_CHECK: set to `true` to enable a check for the number of failed attempts to log in after which the account is locked
  * NUMBER_OF_ATTEMPTS: the number of failed attempts to log in after which the account is locked
  * PASSWORD_EXPIRATION_DURATION: the number of days after which the password expires and the user needs to create a new one



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "data":
      {
        "passwordValidationUserPolicy" : {
          {
            "enableFailedAttemptsCheck" : "FAILED_ATTEMPTS_CHECK",
            "allowedFailedAttempts" : "NUMBER_OF_ATTEMPTS",
            "passwordExpirationDuration" : "PASSWORD_EXPIRATION_DURATION"
          }
        },
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2021-11-02T19:12:08.132Z",
      "startTime": "2021-11-02T19:12:08.132Z",
      "endTime": "2021-11-02T19:12:09.125Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To view the user password policy, see  List users.

### REST v1beta4

To set a user password policy, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password of the user
  * FAILED_ATTEMPTS_CHECK: set to `true` to enable a check for the number of failed attempts to log in after which the account is locked
  * NUMBER_OF_ATTEMPTS: the number of failed attempts to log in after which the account is locked
  * PASSWORD_EXPIRATION_DURATION: the number of days after which the password expires and the user needs to create a new one



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "data":
      {
        "passwordValidationUserPolicy" : {
          {
            "enableFailedAttemptsCheck" : "FAILED_ATTEMPTS_CHECK",
            "allowedFailedAttempts" : "NUMBER_OF_ATTEMPTS",
            "passwordExpirationDuration" : "PASSWORD_EXPIRATION_DURATION"
          }
        },
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2021-11-02T19:12:08.132Z",
      "startTime": "2021-11-02T19:12:08.132Z",
      "endTime": "2021-11-02T19:12:09.125Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To view the user password policy, see  List users.

## List users

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu. 



### gcloud

Use the [ gcloud sql users list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/list) command to list the users for this instance:
    
    
    gcloud sql users list \
    --instance=INSTANCE_NAME

The command returns the `Name`, `Host`, and authentication `Type` for each user.

Additionally, for the built-in authentication type, the password policy settings and status are returned. For example:
    
    
        NAME    HOST    TYPE        PASSWORD_POLICY
        user1           BUILT_IN    {'allowedFailedAttempts': 2,
                                     'enableFailedAttemptsCheck': True,
                                     'passwordExpirationDuration': '7d',
                                     'status': {
                                       'locked': True,
                                       'passwordExpirationTime': '2022-07-01T19:53:45.822742904Z'
                                     }
                                    }
       

### REST v1

To list the users defined for an instance, use a GET request with the [ users:list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/list) method.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#usersList",
      "items": [
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "sqlserver",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "user-id-1",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "user-id-2",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          ...
        },
        {
          ...
        }
      ]
    }
    

If a user password policy was set, the `items` section of the response includes a `passwordPolicy` section. The following code sample shows the `passwordPolicy` section. 
    
    
      {
      ...
      "passwordValidationUserPolicy" : {
        {
          "enableFailedAttemptsCheck" : true,
          "allowedFailedAttempts" : 8,
          "passwordExpirationDuration" : "7d"
        }
      },
      ...
    }
      

**Note** : The [`users.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/list) API supports only response payloads that include up to 4 MB of text or roughly 16,000 users.

If your database has a large number of users that exceeds these limits, then a request to list users might result in an error. If this occurs, then to get the list of users, we recommend that you run the request directly from the database.

### REST v1beta4

To list the users defined for an instance, use a GET request with the [ users:list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/list) method.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#usersList",
      "items": [
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "sqlserver",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "user-id-1",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "user-id-2",
          "host": "",
          "instance": "instance-id",
          "project": "project-id",
          "sqlserverUserDetails": {
            "serverRoles": [
              "CustomerDbRootRole"
            ]
          }
        },
        {
          ...
        },
        {
          ...
        }
      ]
    }
    

If a user password policy was set, the `items` section of the response includes a `passwordPolicy` section. The following code sample shows the `passwordPolicy` section. 
    
    
      {
      ...
      "passwordValidationUserPolicy" : {
        {
          "enableFailedAttemptsCheck" : true,
          "allowedFailedAttempts" : 8,
          "passwordExpirationDuration" : "7d"
        }
      },
      ...
    }
      

**Note** : The [`users.list`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/list) API supports only response payloads that include up to 4 MB of text or roughly 16,000 users.

If your database has a large number of users that exceeds these limits, then a request to list users might result in an error. If this occurs, then to get the list of users, we recommend that you run the request directly from the database.

### psql Client

At the `psql` prompt, list the PostgreSQL users:
    
    
    SELECT * FROM pg_roles;

Note: You can't use the Google Cloud console or `gcloud` to display system users.

## Add database roles to an existing user

After you create a built-in user, you can assign additional roles to the user. These roles are added to their existing roles and don't replace the existing set of roles assigned to user account.

Before you can assign a role to a user in Cloud SQL for PostgreSQL, the role must already exist. If you're using a custom role, then you must create the role in the PostgreSQL database first. 

To create a role in PostgreSQL, see [Database roles](https://www.postgresql.org/docs/current/static/database-roles.html).

You can't assign any of the predefined system roles listed in [Cloud SQL system roles and users](https://docs.cloud.google.com/sql/docs/postgres/users#system-roles-users) to existing PostgreSQL users, except for the `cloudsqlsuperuser`. 

### gcloud

To assign roles to a user, use the [ `gcloud sql users assign-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles) command.
    
    
    gcloud sql users assign-roles USER_NAME \
    --instance=INSTANCE_NAME \
    --type=BUILT_IN \
    --database-roles=ROLE_1, ROLE_2, ..., ROLE__N_

Replace the following:

  * USER_NAME: the username.
  * INSTANCE_NAME: the name of the instance.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the user.

For the `type` field, specify `BUILT_IN` to represent the [Cloud SQL user type](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles#--type). This field determines the method used for authentication. 

### REST v1

To update a user, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

When you assign database roles, you can update user password policy parameters.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the desired instance ID
  * USER_ID: the ID of the user
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the database role or roles to assign to the user

For the `type` field, specify `BUILT_IN` to represent the [Cloud SQL user type](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles#--type). This field determines the method used for authentication. 

HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "type": "BUILT_IN",
      "databaseRoles": [
       "ROLE_1",
       "ROLE_2"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
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
        -Method PUT `  
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To update a user, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

When you assign database roles, you can update user password policy parameters.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the desired instance ID
  * USER_ID: the ID of the user
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the user

For the `type` field, specify `BUILT_IN` to represent the [Cloud SQL user type](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles#--type). This field determines the method used for authentication. 

HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "type": "BUILT_IN",
      "databaseRoles": [
       "ROLE_1",
       "ROLE_2"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
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
        -Method PUT `  
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Replace database roles for an existing user

If you want to replace or remove database roles from the user, you must revoke all of their existing roles while specifying new database roles, if any.

By default, when you create a built-in PostgreSQL user, the user is granted the `cloudsqlsuperuser` role automatically. If you don't want a user to keep the `cloudsqlsuperuser` role, then revoke the existing roles of the user.

### gcloud

To replace the database roles for a user, you revoke the existing roles for the user and assign new roles. To replace database roles for a user, use the following [ `gcloud sql users assign-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles) command.
    
    
    gcloud sql users assign-roles USER_NAME \
    --type=BUILT_IN \
    --instance=INSTANCE_NAME \
    --database-roles=ROLE_1,ROLE_2 \
    --revoke-existing-roles

Replace the following:

  * USER_NAME: the username. 
  * HOST: the user's host name as a specific IP address, address range, or any host (`%`).
  * INSTANCE_NAME: the name of the instance.
  * ROLE_1, ROLE_2: the new database role or roles to assign to the user.

For the `type` field, specify `BUILT_IN` to represent the [Cloud SQL user type](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/assign-roles#--type). This field determines the method used for authentication. 

You can also revoke the existing roles for a user and assign zero roles. For example:
    
    
    gcloud sql users assign-roles USER_NAME \
    --type=BUILT_IN \
    --instance=INSTANCE_NAME \
    --database-roles= \
    --revoke-existing-roles

### REST v1

To update a user, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

When you replace a user's database roles, you can update user password policy parameters in the same API request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the desired instance ID
  * USER_ID: the ID of the user
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the new database role or roles to assign to the user. You can also specify an empty list.



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "type": "BUILT-IN",
      "databaseRoles": [
       "ROLE_1",
       "ROLE_2"
      ],
      "revokeExistingRoles": true
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
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
        -Method PUT `  
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To update a user, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

When you replace a user's database roles, you can update user password policy parameters in the same API request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the desired instance ID
  * USER_ID: the ID of the user
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the new database role or roles to assign to the user. You can also specify an empty list.



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "type": "BUILT-IN",
      "databaseRoles": [
       "ROLE_1",
       "ROLE_2"
      ],
      "revokeExistingRoles": true
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
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
        -Method PUT `  
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
      "insertTime": "2025-10-20T22:44:16.656Z",
      "startTime": "2025-10-20T22:44:16.686Z",
      "endTime": "2025-10-20T22:44:20.437Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Change a user password

User passwords can be changed in one of the following ways.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the user you want to update.
  5. Select **Change password**.
  6. Specify a new password. 
  7. Click **OK**. 



### gcloud

Use the [ `gcloud sql users set-password`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password) command to change a password.

Replace the following:

  * USER_NAME: The user name.
  * INSTANCE_NAME: The name of the instance.


    
    
    gcloud sql users set-password USER_NAME \
    --instance=INSTANCE_NAME \
    --prompt-for-password

### REST v1

To change a user password, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

The following request updates the password for the user account `user_name`. 

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID
  * user-id: The ID of the user
  * password: The new password for the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id

Request JSON body: 
    
    
    {
      "name": "user-id",
      "password": "password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=user-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To change a user password, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

The following request updates the password for the user account `user_name`. 

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: The desired instance ID
  * user-id: The ID of the user
  * password: The new password for the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id

Request JSON body: 
    
    
    {
      "name": "user-id",
      "password": "password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=user-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### psql Client

At the `psql` prompt, run the [ALTER USER](https://www.postgresql.org/docs/current/static/sql-alteruser.html) command. 

  1. Unlock the user. 
         
         ALTER USER USER_NAME WITH LOGIN;

  2. Change the password and enter the password when prompted. 
         
         ALTER USER USER_NAME WITH PASSWORD PASSWORD;

**NOTE:** When using EXTENSION [ `pg_stat_statements`](https://www.postgresql.org/docs/9.6/pgstatstatements.html), SQL statements from all users are visible to users with the `cloudsqlsuperuser` ROLE (in PostgreSQL version 10 and higher). Don't use plain text passwords in queries. 



If a user is locked out due to password policy settings, change the password to unlock them. Ensure that passwords, when changed, adhere to the password policy.

## Remove a user password policy

You can remove a password policy from a user that has the built-in authentication type.

### gcloud

To remove the user password policy, use the [ `gcloud sql users set-password-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy) command and the `--clear-password-policy` parameter.

Replace the following:

  * USER_NAME: the user name
  * INSTANCE_NAME: the name of the instance
  * HOST: the user's host name as a specific IP address, address range, or any host (`%`)


    
    
    gcloud sql users set-password-policy USER_NAME \
    --instance=INSTANCE_NAME \
    --host=HOST \
    --clear-password-policy

### REST v1

To remove a user password policy, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/update) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password of the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "data":
      {
        "passwordValidationUserPolicy" : {}
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2021-11-02T19:12:08.132Z",
      "startTime": "2021-11-02T19:12:08.132Z",
      "endTime": "2021-11-02T19:12:09.125Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To remove a user password policy, use a PUT request with the [ users:update](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/update) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: the instance ID
  * USER_ID: the ID of the user
  * PASSWORD: the password of the user



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID

Request JSON body: 
    
    
    {
      "name": "USER_ID",
      "password": "PASSWORD",
      "data":
      {
        "passwordValidationUserPolicy" : {}
      }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?name=USER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2021-11-02T19:12:08.132Z",
      "startTime": "2021-11-02T19:12:08.132Z",
      "endTime": "2021-11-02T19:12:09.125Z",
      "operationType": "UPDATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Remove a user

The default user can remove users.

Before removing a user, you must drop all the objects it owns or reassign their ownership, and revoke any privileges the role has been granted on other objects.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the user you want to remove.
  5. Select **Remove** and then select **Remove** again.



### gcloud

Use the [ `gcloud sql users delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/delete) command to remove a user.

Replace the following:

  * USER_NAME: The user name.
  * INSTANCE_NAME: The name of the instance.


    
    
    gcloud sql users delete USER_NAME \
    --instance=INSTANCE_NAME

### REST v1

The request below uses the [ users:delete](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/users/delete) method to delete the specified user account.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * INSTANCE_ID: The desired instance ID
  * USERNAME: The email address for the user or service account



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "DELETE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

The request below uses the [ users:delete](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/users/delete) method to delete the specified user account.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * INSTANCE_ID: The desired instance ID
  * USERNAME: The email address for the user or service account



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "DELETE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### psql Client

  1. At the `psql` prompt, delete the user: 
         
         DROP ROLE USER_NAME;

For more information about the `DROP ROLE` statement, see [ the PostgreSQL documentation](https://www.postgresql.org/docs/current/static/sql-droprole.html). 




## Update user properties

To update user properties such as attributes, you must use the `psql` client. For more information, see [Database Roles](https://www.postgresql.org/docs/current/static/user-manag.html) in the PostgreSQL documentation. **NOTE:** When using EXTENSION [ `pg_stat_statements`](https://www.postgresql.org/docs/9.6/pgstatstatements.html), SQL statements from all users are visible to users with the `cloudsqlsuperuser` ROLE (in PostgreSQL version 10 and higher). Don't use plain text passwords in queries. 

## What's next

  * Learn more about [how Cloud SQL works with users](https://docs.cloud.google.com/sql/docs/postgres/users). 
  * Read the [PostgreSQL documentation about role creation](https://www.postgresql.org/docs/current/static/sql-createrole.html).
  * Learn about [connecting to instances](https://docs.cloud.google.com/sql/docs/postgres/external-connection-methods). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
