---
url: https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases/
title: Create and manage databases \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:35.945668+00:00
---

# Create and manage databases  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create and manage databases Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases "View this page for the SQL Server database engine")

This page contains information about creating, listing, and deleting MySQL databases on a Cloud SQL instance.

A newly-created instance has four system databases: 

  * [`information_schema`](https://dev.mysql.com/doc/refman/8.4/en/information-schema.html): Provides access to database metadata, information about the MySQL server.
  * [`mysql`](https://dev.mysql.com/doc/refman/8.4/en/system-schema.html): The system schema. It contains tables that store information required by the MySQL server as it runs.
  * [`performance_schema`](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html): A feature for monitoring MySQL Server execution at a low level.
  * [`sys`](https://dev.mysql.com/doc/refman/8.4/en/sys-schema.html): Contains a set of objects that helps DBAs and developers interpret data collected by the performance schema.

For more information about MySQL databases, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/database-use.html). 

## Before you begin

Before completing the tasks on this page, you must have:

  * Created a Cloud SQL instance. For more information, see [Creating instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).



If you plan to use the mysql client to create or manage your databases, you must have:

  * Configured access and connected to the instance with a `mysql` client. For more information about connection options, see [Connection Options for External Applications](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods). 



## Create a database on the Cloud SQL instance

**Note:** The maximum length of the database name is 64 characters. For more information on other criteria for this name, see [Schema Object Names](https://dev.mysql.com/doc/refman/8.4/en/identifiers.html).

If you don't specify a custom character set and collation when you create your database, then the database has the following default values:

  * **MySQL 5.6, 5.7** : (created with Google Cloud console, Cloud SQL Admin API, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or mysql client)
    * Character set: `utf8`
    * Collation: `utf8_general_ci`
  * **MySQL 8.0.x and later** (created with the Google Cloud console)
    * Character set: `utf8`
    * Collation: `utf8_general_ci`
  * **MySQL 8.0.x and later** (created with the Cloud SQL Admin API, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or mysql client)
    * Character set: `utf8mb4`
    * Collation: `utf8mb4_0900_ai_ci`



If you need to modify the character set or collation configuration of your database after creation, then see [Update the character set and collation for a database](https://docs.cloud.google.com/sql/docs/mysql/charset-collation).

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Databases** from the SQL navigation menu.
  4. Click **Create database**.
  5. In the **Create a database** dialog, specify the name of the database, and optionally the character set and collation. 

For more information about character sets and collations, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/8.4/en/charset.html). 

  6. Click **Create**.



### gcloud

For reference information, see [`gcloud sql databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/create).

For more information about character sets and collations, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/8.4/en/charset.html). 
    
    
    gcloud sql databases create DATABASE_NAME \
    --instance=INSTANCE_NAME \
    [--charset=CHARSET] \
    [--collation=COLLATION]

### Terraform

To create a database, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database).
    
    
    resource "google_sql_database" "database" {
      name     = "my-database"
      instance = google_sql_database_instance.instance.name
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

The following request uses the [databases:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/insert) method to create a new database on the specified instance.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * database-name: The name of a database inside the Cloud SQL instance



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases

Request JSON body: 
    
    
    {
      "project": "project-id",
      "instance": "instance-id",
      "name": "database-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_DATABASE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

The following request uses the [databases:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/insert) method to create a new database on the specified instance.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * database-name: The name of a database inside the Cloud SQL instance



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases

Request JSON body: 
    
    
    {
      "project": "project-id",
      "instance": "instance-id",
      "name": "database-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE_DATABASE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### mysql Client

For reference information, see [CREATE DATABASE](https://dev.mysql.com/doc/refman/8.4/en/create-database.html) in the MySQL documentation.

For more information about character sets and collations, see [Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/8.4/en/charset.html). 
    
    
    CREATE DATABASE database_name
      [[CHARACTER SET charset_name][COLLATE collation_name]];

## List your databases

To list all databases on an instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Databases** from the left side menu. The **Databases** page lists databases along with their collation type, character set, and database type.



### gcloud

For reference information, see [`gcloud sql databases list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/list).
    
    
    gcloud sql databases list \
    --instance=INSTANCE_NAME

### REST v1

The following request uses the [databases:list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/list) method to list the databases for an instance.

When you list the databases using the API, you see additional template databases and a system database that are not displayed by the console. You cannot delete or manage the system database.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#database",
      "charset": "utf8",
      "collation": "utf8_general_ci",
      "etag": "etag",
      "name": "sys",
      "instance": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases/sys",
      "project": "project-id"
    }
    

**Note** : The [`databases.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/list) API supports only response payloads that include up to 4 MB of text.

If you run a database list request on a large instance, then you might receive an error. If this occurs, then to get the list of databases, we recommend that you run the request directly from the instance.

### REST v1beta4

The following request uses the [databases:list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/list) method to list the databases for an instance.

When you list the databases using the API, you see additional template databases and a system database that are not displayed by the console. You cannot delete or manage the system database.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#database",
      "charset": "utf8",
      "collation": "utf8_general_ci",
      "etag": "etag",
      "name": "sys",
      "instance": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases/sys",
      "project": "project-id"
    }
    

**Note** : The [`databases.list`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/list) API supports only response payloads that include up to 4 MB of text.

If you run a database list request on a large instance, then you might receive an error. If this occurs, then to get the list of databases, we recommend that you run the request directly from the instance.

### mysql Client

For reference information, see [SHOW DATABASES](https://dev.mysql.com/doc/refman/8.4/en/show-databases.html) in the MySQL documentation.
    
    
    SHOW DATABASES;

## Delete a database

To delete a database on the Cloud SQL instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Databases** from the left side menu.
  4. In the database list, find the database you want to delete and click the trash can icon.
  5. In the **Delete database** dialog, enter the name of the database and then click **Delete**.

**Note:** Deleting a database removes all files in the database's directory, including any files not directly used by the database. Examples of such files are `#sql-*` files created from interrupted ALTER TABLE operations in MySQL 5.6 and MySQL 5.7. 

### gcloud

For reference information, see [`gcloud sql databases delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/databases/delete).
    
    
    gcloud sql databases delete DATABASE_NAME \
    --instance=INSTANCE_NAME

**Note:** Deleting a database removes all files in the database's directory, including any files not directly used by the database. Examples of such files are `#sql-*` files created from interrupted ALTER TABLE operations in MySQL 5.6 and MySQL 5.7. 

### REST v1

The following request uses the [databases:delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/delete) method to delete the specified database.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * database-name: The name of a database inside the Cloud SQL instance



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases/database-name

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases/database-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/databases/database-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_DATABASE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

The following request uses the [databases:delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/delete) method to delete the specified database.

**Note:** Deleting a database removes all files in the database's directory, including any files not directly used by the database. Examples of such files are `#sql-*` files created from interrupted ALTER TABLE operations in MySQL 5.6 and MySQL 5.7. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * database-name: The name of a database inside the Cloud SQL instance



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases/database-name

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases/database-name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/databases/database-name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_DATABASE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### mysql Client

For reference information, see [DROP DATABASE](https://dev.mysql.com/doc/refman/8.4/en/show-databases.html) in the MySQL documentation.
    
    
    DROP DATABASE [database_name];

**Note:** If the database's directory contains any files not directly used by the database, the `DROP DATABASE` command will generate errors indicating that the database directory couldn't be deleted, such as: 

  * Error dropping database (can't rmdir './_database_name_ ', errno: 39)
  * Error dropping database (can't rmdir './_database_name_ ', errno: 17)

Examples of such files are `#sql-*` files created from interrupted ALTER TABLE operations in MySQL 5.6 and MySQL 5.7. To delete these files and complete the DROP DATABASE operation, repeat the operation using one of the other methods: the console, the `gcloud` command, or the REST API call. 

## What's next

  * [Manage users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) for your instance.
  * [Import data](https://docs.cloud.google.com/sql/docs/mysql/import-export) into your instance. 
  * Learn about [options for connecting to your instance using the mysql client](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods).
  * [Create a database table](https://dev.mysql.com/doc/refman/8.4/en/create-table.html).
  * [Cloud SQL for MySQL stored procedures](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud SQL free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
