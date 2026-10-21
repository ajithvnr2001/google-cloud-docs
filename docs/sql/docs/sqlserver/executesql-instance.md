---
url: https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance/
title: Execute SQL statements using the Cloud SQL Data API \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:49.414423+00:00
---

# Execute SQL statements using the Cloud SQL Data API  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Execute SQL statements using the Cloud SQL Data API Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to execute SQL statements against databases on Cloud SQL instances using the Data API. With the Data API, you use the Cloud SQL Admin API and [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to run SQL statements on any instance where you've enabled Data API access. 

You can use the Data API with instances that use public IP addresses, private services access, or Private Service Connect. The Data API supports all types of SQL statements including data manipulation language (DML), data definition language (DDL), and data query language (DQL). The Data API is good for running small and quick administrative statements, such as creating database roles or users and making small schema updates. 

## Before you begin

Before you can execute SQL statements on an instance, take the following steps.

### Configure the database user

The Data API needs to authenticate as a database user to execute SQL statements. 

To authenticate as a built-in user using password, do the following: 

  1. [Create a user account with a non-empty password](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#creating). You can also use the default user `sqlserver`. 
  2. [Grant the account the required roles or privileges](https://docs.cloud.google.com/sql/docs/sqlserver/users#other-users) to execute SQL statements. If the user is not `sqlserver`, [grant the user the `db_owner` role](https://docs.cloud.google.com/sql/docs/sqlserver/users#troubleshooting).
  3. Use Secret Manager to [create a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret) to store the password. For security, the Data API asks for the secret's resource name instead of the password in the API request. The regional secret should be stored in the same region as your Cloud SQL instance. A secret created using Secret Manager's global endpoint are not supported even if it's stored in the same region.
  4. Grant Data API's caller `roles/secretmanager.secretAccessor`. As a best practice, define [IAM conditions](https://docs.cloud.google.com/secret-manager/regional-secrets/access-control-rs#iam-conditions) to allow a user to access a specific secret but not other secrets in the project.



### Required roles or permissions

The user or service accounts used to call the Data API must have the permission to execute SQL statements, `cloudsql.instances.executesql`. The permission is included in one of the following predefined roles:

  * `Cloud SQL Admin` (`roles/cloudsql.admin`)
  * `Cloud SQL Instance User` (`roles/cloudsql.instanceUser`)
  * `Cloud SQL Studio User` (`roles/cloudsql.studioUser`)



You can also define an [IAM custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) for the user or service account that includes the `cloudsql.instances.executesql` permission. This permission is [supported](https://docs.cloud.google.com/iam/docs/custom-roles-permissions-support) in IAM custom roles.

When using a Secret Manager secret to authenticate, the user or service account must also have the permission to access the secret, `secretmanager.versions.access`. The permission is included in one of the following predefined roles:

  * `Secret Manager Secret Accessor` (`roles/secretmanager.secretAccessor`)
  * `Secret Manager Admin` (`roles/secretmanager.admin`)



## Enable or disable the Data API

To use the Data API, you must enable it for each instance. You can disable the Data API at any time.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. From the SQL navigation menu, select **Connections**.
  4. Click the **Networking** tab.
  5. Select the **Allow Data API** checkbox.
  6. Click **Save**.



### gcloud

To enable Data API access on an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command with the `--data-api-access=ALLOW_DATA_API` flag:
    
    
    gcloud sql instances patch INSTANCE_NAME --data-api-access=ALLOW_DATA_API

To disable Data API access, use the `--data-api-access=DISALLOW_DATA_API` flag:
    
    
    gcloud sql instances patch INSTANCE_NAME --data-api-access=DISALLOW_DATA_API

Replace INSTANCE_NAME with the name of the instance on which to enable or disable the Data API.

### REST

To enable Data API access on an instance, send a `PATCH` request to the `instances.patch` endpoint:
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

The request body should contain the `dataApiAccess` field set to `ALLOW_DATA_API`:
    
    
    {
      "dataApiAccess": "ALLOW_DATA_API"
    }

To disable Data API access, set `dataApiAccess` to `DISALLOW_DATA_API`.

## Execute a SQL statement

You can execute SQL statements against databases on your Cloud SQL instance using either [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the REST API.

### Authenticate using password

You can execute SQL statements using built-in password authentication, when the password is stored as a regional secret with Secret Manager in the same region as the Cloud SQL instance.

### gcloud

To execute a SQL statement against a database on an instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), use the [`gcloud sql instances execute-sql`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/execute-sql) command.
    
    
    gcloud sql instances execute-sql INSTANCE_NAME \
    --database=DATABASE_NAME \
    --sql=SQL_STATEMENT \
    --user=USER \
    --password-secret-version=PASSWORD_SECRET_VERSION \
    --partial-result-mode=PARTIAL_RESULT_MODE

Make the following replacements:

  * INSTANCE_NAME: the name of the instance.
  * DATABASE_NAME: the name of the database within the instance.
  * SQL_STATEMENT: the SQL statement to execute. If the statement contains spaces or shell special characters, then it must be quoted.
  * USER: the database user to authenticate as. 
  * PASSWORD_SECRET_VERSION: the resource name of the Secret Manager secret holding the password for the database user. The secret should be [a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret) and stored in the same region as the Cloud SQL instance. The expected resource name format is `projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`. 
  * PARTIAL_RESULT_MODE: optional. Controls how to respond when result is incomplete. Can be `ALLOW_PARTIAL_RESULT`, `FAIL_PARTIAL_RESULT`, or `PARTIAL_RESULT_MODE_UNSPECIFIED`. See Modifying truncation behavior.



### Terraform

You can use Data API on Terraform to provision in-database resources such as databases, tables, extensions, users, and privilege grants, without manually connecting to the instance. To execute a SQL script on Terraform, use the [ `google_sql_provision_script`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_provision_script) Terraform resource.
    
    
    resource "google_sql_user" "built_in_user" {
      name     = "tf-user"
      host     = "%"  # Don't set this field for PostgreSQL and SQL Server.
      instance = google_sql_database_instance.instance.name
      password = "changeme"
      type     = "BUILT_IN"
    }
    
    # Create a regional secret. Global secrets are not supported even if
    # located in one region only.
    resource "google_secret_manager_regional_secret" "secret" {
      secret_id = "db-password"
    
      # Use the same region as the Cloud SQL instance.
      location = "us-central1"
    }
    
    resource "google_secret_manager_regional_secret_version" "secret_version" {
      secret = google_secret_manager_regional_secret.secret.id
      secret_data = "changeme"
    }
    
    resource "google_sql_provision_script" "script" {
      # You can inline the script or import from a file like script  = file("${path.module}/script.sql")
      # When modified, the whole script will be executed again. It's recommended to
      # make the script idempotent with patterns like create if not exists ... or
      # if not exists (select ...) then ... end if.
      script  = "CREATE TABLE IF NOT EXISTS table1 ( col VARCHAR(16) NOT NULL );"
    
      instance = google_sql_database_instance.instance.name
      database = google_sql_database.database.name
      description = "sql script to create tables"
      user = google_sql_user.built_in_user.name
    
      # The location should be the same as the Cloud SQL instance's location.
      password_secret_version = "projects/my-project/locations/us-central1/secrets/db-password/versions/latest"
    
      # The built-in database user and password secret version must be created
      # first. Cloud SQL will retrieve password from Secret Manager
      # and connect to this user account to execute your script.
      depends_on = [
        google_sql_user.built_in_user,
        google_secret_manager_regional_secret_version.secret_version
      ]
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

Deleting a `google_sql_provision_script` resource won't delete the in-database resources it created. To delete them, you can explicitly add statements in the script such as `drop ... if exists` and then apply the changes.

### REST

To execute a SQL statement against a database on an instance using the REST API, send a `POST` request to the `executeSql` endpoint:
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME/executeSql

The request body should contain the database name and the SQL statement:
    
    
    {
      "database": "DATABASE_NAME",
      "sqlStatement": "SQL_STATEMENT",
      "user": "USER",
      "passwordSecretVersion": "PASSWORD_SECRET_VERSION",
      "partialResultMode": "PARTIAL_RESULT_MODE"
    }

Make the following replacements:

  * PROJECT_ID: your project ID.
  * INSTANCE_NAME: the name of the instance.
  * DATABASE_NAME: the name of the database within the instance.
  * SQL_STATEMENT: the SQL statement to execute.
  * USER: the database user to authenticate as. 
  * PASSWORD_SECRET_VERSION: the resource name of the Secret Manager secret holding the password for the database user. The secret should be [a regional secret](https://docs.cloud.google.com/secret-manager/regional-secrets/create-regional-secret) and stored in the same region as the Cloud SQL instance. The expected resource name format is `projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`. 
  * PARTIAL_RESULT_MODE: optional. Controls how the API responds when the result exceeds 10 MB. Can be `FAIL_PARTIAL_RESULT`, `ALLOW_PARTIAL_RESULT`, or `PARTIAL_RESULT_MODE_UNSPECIFIED`. See Modifying truncation behavior.



### Modify truncation behavior

You can control how large results are handled when executing SQL, by including the `"partialResultMode"` field in the request. This field accepts the following values:

  * `FAIL_PARTIAL_RESULT`: Default. Throw an error if the result exceeds 10 MB or if only a partial result can be retrieved. Don't return the result.
  * `ALLOW_PARTIAL_RESULT`: Return a truncated result and set `partial_result` to true if the result exceeds 10 MB or if only a partial result can be retrieved due to error. Don't throw an error.
  * `PARTIAL_RESULT_MODE_UNSPECIFIED`: Unspecified mode, effectively the same as `FAIL_PARTIAL_RESULT`.



### Audit queries

You can track the application name by setting the `applicationName` field in the request. The database will track the application name in session statistics, for example, in the table `sys.dm_exec_sessions`. 

You can use [Query Insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights) to track more information about your queries and analyze performance problems. 

You can also use [SQL Server database auditing](https://docs.cloud.google.com/sql/docs/sqlserver/db-audit) to log queries for security or compliance purposes.

## Limitations

  * The size limit for a response is 10 MB. Results exceeding this size are truncated if `partialResultMode` is set to `ALLOW_PARTIAL_RESULT`, otherwise an error is thrown.
  * Requests are limited to 0.5 MB.
  * You can only run SQL statements for Cloud SQL for SQL Server instances that are running.
  * Cloud SQL doesn't support using the Data API with instances that are set up for external server replication.
  * Requests taking longer than 30 seconds are canceled. Setting a higher statement timeout using `SET LOCK_TIMEOUT` isn't supported. 
  * Cloud SQL limits the number of concurrent `executeSql` requests per instance to prevent overload. If the limit is reached, then subsequent requests fail and return one of the following errors:

    * `At most 'x' concurrent queries may be run on this instance. Try again later.`
    * `Maximum concurrent reads 'x' reached.`

The limit (`x`) is 5 queries for instances with less than 10 GB of [total memory](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview), and 10 queries for instances with at least 10 GB of total memory. 

  * Each response can contain a maximum of 10 database messages or warnings.

  * If there is a statement syntax or execution error, then no result is returned.

  * The Data API can't authenticate as built-in users with empty passwords. 

  * The Data API can be temporarily blocked for data integrity purposes when certain maintenance operations are ongoing on the instance. Retry later if it happens.



  * The `GO` command is not supported. This command is used in Microsoft SQL Server utilities to indicate that a batch of statements have ended and can be sent to SQL Server.
  * If a query includes a binary column, then the Data API can't show it. Convert binary values to a string instead.

For example, replace:
        
        SELECT my_binary_column from my_table2;
        

with:
        
        SELECT CONVERT(NVARCHAR(4000), my_binary_column, 1) from my_table2;
        

  * When running multiple queries and one of them fails, the first encountered error is returned. Some of the statements in the batch prior to the error might have executed successfully. You can wrap multiple queries in a `transaction` statement to prevent this issue:
        
        BEGIN TRANSACTION
            YOUR_SQL_STATEMENTS
        COMMIT;
        

Replace the following:

    * YOUR_SQL_STATEMENTS: the statements you want to run as part of this query


  * The SQL script and its execution response might transit through intermediate locations between your client and the location of the target instance. For this reason, requests will fail with the error "not supported for instances in certain Assured Workloads control packages folders" for certain Assured Workloads projects and for projects with `constraints/sql.restrictNoncompliantResourceCreation` manually enforced.



## Troubleshoot

This section contains information about issues associated with using the Data API, along with steps for troubleshooting the issues.

Issue | Troubleshooting |  `The instance doesn't allow using ExecuteSql to access this instance. You can allow it by patching the instance with {settings: { dataApiAccess: "ALLOW_DATA_API" }}` |  The Data API is disabled by default. [Enable the Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance#enable-disable-data-api) on the instance to resolve the issue.   
---|---  
`Secret cannot be provided when auto_iam_authn is true.` | When you set `auto_iam_authn` to `true`, you are authenticating to the database using IAM. This authentication method doesn't require a password or secret. See [ Authenticate using IAM](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance#authenticate-using-iam).   
`ExecuteSql API is not supported for instances in certain Assured Workloads control packages folders yet.` |  The SQL script and its execution response might transit through intermediate locations between your client and the location of the target instance. For this reason, requests will fail for instances in certain Assured Workloads projects. If your project is not enrolled in Assured Workloads but `constraints/sql.restrictNoncompliantResourceCreation` is manually enforced, then ask your organization's administrator to remove the constraint and the issue will be resolved on newly created instances.   
`The server principal USERNAME is not able to access the database DATABASE_NAME under the current security context.` |  The user is not a member of the database. Connect to the database as the `sqlserver` user and add the new user, then give the new user the `db_owner` role for the database. For example: 
    
    
      EXEC sp_adduser 'user';
      EXEC sp_addrolemember 'db_owner', 'user'
        
  
`The database is currently unavailable.` |  The instance might be restarting, undergoing maintenance, or in an unhealthy state. Check the instance's status and try again later.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
