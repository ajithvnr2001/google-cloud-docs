---
url: https://docs.cloud.google.com/sql/docs/postgres/flags/
title: Configure database flags \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:25.736525+00:00
---

# Configure database flags  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/flags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure database flags Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/flags "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/flags "View this page for the SQL Server database engine")

This page describes how to configure database flags for Cloud SQL, and lists the flags that you can set for your instance. You use database flags for many operations, including adjusting PostgreSQL parameters, adjusting options, and configuring and tuning an instance.

In some cases, setting one flag may require that you set another flag to fully enable the functionality you want to use.

When you set, remove, or modify a flag for a database instance, the database might be restarted. The flag value is then persisted for the instance until you remove it. If the instance is the source of a replica, and the instance is restarted, the replica is also restarted to align with the current configuration of the instance.

## Configure database flags

The following sections cover common flag management tasks.

### Set a database flag

### Console

  1. In the [Google Cloud console](https://console.cloud.google.com/project/_/sql/instances), select the project that contains the Cloud SQL instance for which you want to set a database flag.
  2. Open the instance and click **Edit**.
  3. Go to the **Flags** section.
  4. To set a flag that has not been set on the instance before, click **Add item** , choose the flag from the drop-down menu, and set its value. 
  5. Click **Save** to save your changes.
  6. Confirm your changes under **Flags** on the Overview page.



### gcloud

Edit the instance:
    
    
    gcloud sql instances patch INSTANCE_NAME --database-flags=FLAG1=VALUE1,FLAG2=VALUE2

This command will overwrite all database flags previously set. To keep those and add new ones, include the values for all flags you want set on the instance; any flag not specifically included is set to its default value. For flags that don't take a value, specify the flag name followed by an equals sign ("=").

For example, to set the `log_connections` and `log_min_error_statement` flags, you can use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags=log_connections=on,log_min_error_statement=error

### Terraform

To add database flags, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "instance" {
      name             = "postgres-instance"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        database_flags {
          name  = "log_connections"
          value = "on"
        }
        database_flags {
          name  = "log_min_error_statement"
          value = "error"
        }
        tier = "db-custom-2-7680"
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
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

To set a flag for an existing database:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "flag_name",
            "value": "flag_value"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If there are existing flags configured for the database, modify the previous command to include them. The `PATCH` command overwrites the existing flags with the ones specified in the request. 

### REST v1beta4

To set a flag for an existing database:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags":
        [
          {
            "name": "flag_name",
            "value": "flag_value"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If there are existing flags configured for the database, modify the previous command to include them. The `PATCH` command overwrites the existing flags with the ones specified in the request. 

### Clear all flags to their default values

### Console

  1. In the [Google Cloud console](https://console.cloud.google.com/project/_/sql/instances), select the project that contains the Cloud SQL instance for which you want to clear all flags.
  2. Open the instance and click **Edit**.
  3. Open the **Database flags** section.
  4. Click the **X** next to all of the flags shown.
  5. Click **Save** to save your changes.



### gcloud

Clear all flags to their default values on an instance:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --clear-database-flags

You are prompted to confirm that the instance will be restarted.

### REST v1

To clear all flags for an existing instance:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags": []
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To clear all flags for an existing instance:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "databaseFlags": []
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### View current values of database flags

To view all current values of the PostgreSQL settings, log into your instance with the `psql` client and enter the following statement: 
    
    
     SELECT name, setting FROM pg_settings;
    

Note that you can change the value only for supported flags (as listed below). 

### Determine which database flags have been set for an instance

To see which flags have been set for a Cloud SQL instance:

### Console

  1. In the [Google Cloud console](https://console.cloud.google.com/project/_/sql/instances), select the project that contains the Cloud SQL instance for which you want to see the database flags that have been set.
  2. Select the instance to open its **Instance Overview** page. 

The database flags that have been set are listed under the **Database flags** section.




### gcloud

Get the instance state:
    
    
    gcloud sql instances describe INSTANCE_NAME

In the output, database flags are listed under the `settings` as the collection `databaseFlags`. For more information about the representation of the flags in the output, see [Instances Resource Representation](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances). 

### REST v1

To list flags configured for an instance:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": false
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "databaseFlags": [
          {
            "name": "general_log",
            "value": "on"
          }
        ],
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

In the output, look for the `databaseFlags` field.

### REST v1beta4

To list flags configured for an instance:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": false
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "databaseFlags": [
          {
            "name": "general_log",
            "value": "on"
          }
        ],
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

In the output, look for the `databaseFlags` field.

## Supported flags

Flags not mentioned in the following table are not supported.

For a given flag, Cloud SQL might support a different value or range from the corresponding PostgreSQL parameter or option.

A | C | D | E | F | G | H | I | J | L | M | O | P | R | S | T | V | W

Cloud SQL Flag | Type  
Acceptable Values and Notes  | Restart  
Required?   
---|---|---  
[ anon.algorithm](https://postgresql-anonymizer.readthedocs.io/en/stable/configure/) | `String`   
The default is **sha256**. | No  
[ anon.maskschema](https://postgresql-anonymizer.readthedocs.io/en/stable/configure/) | `String`   
The default is **mask**. | No  
[ anon.restrict_to_trusted_schemas](https://postgresql-anonymizer.readthedocs.io/en/stable/configure/) | `boolean`   
`on` | `off`   
The default is **off**.  | No  
[ anon.salt](https://postgresql-anonymizer.readthedocs.io/en/stable/configure/) | `String`   
There's no default value. | No  
[ anon.sourceschema](https://postgresql-anonymizer.readthedocs.io/en/stable/configure/) | `String`   
The default is **public**. | No  
[ auto_explain.log_analyze](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ auto_explain.log_buffers](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ auto_explain.log_min_duration](https://www.postgresql.org/docs/current/static/auto-explain.html) | `Integer`   
`-1 ... 2147483647`   
The default is **-1**.  | No   
[ auto_explain.log_format](https://www.postgresql.org/docs/current/static/auto-explain.html) | `String`   
`text|xml|json|yaml`  
The default is **text**.  | No   
[ auto_explain.log_level](https://www.postgresql.org/docs/current/static/auto-explain.html) | `String`   
`debug5|debug4|debug3|debug2|debug1|debug|`  
`info|notice|warning|log`   
The default is **log**.   
Supported in PostgreSQL 12 and later.  | No   
[ auto_explain.log_nested_statements](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ auto_explain.log_settings](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.   
Supported in PostgreSQL 12 and later.  | No   
[ auto_explain.log_timing](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **on**.  | No   
[ auto_explain.log_triggers](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ auto_explain.log_wal](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.   
Supported in PostgreSQL 13 and later.  | No   
[ auto_explain.log_verbose](https://www.postgresql.org/docs/current/static/auto-explain.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ auto_explain.sample_rate](https://www.postgresql.org/docs/current/static/auto-explain.html) | `Float`   
`0 ... 1`   
The default is **1**.  | No   
[autovacuum](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM) | `boolean`  
`on` | `off`   
The default is **on**.   
For usage information that might affect the SLA, see the [Operational guidelines for Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines#database_flag_values).  | No  
[autovacuum_analyze_scale_factor](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-ANALYZE-SCALE-FACTOR) | `float`  
`0` ... `100`   
The default is **0.1**.  | No  
[autovacuum_analyze_threshold](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-ANALYZE-THRESHOLD) | `integer`  
`0` ... `2147483647`   
The default is **50**. | No  
[autovacuum_freeze_max_age](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE) | `integer`  
`100000` ... `2000000000`   
The default is **200000000**.   
For usage information that might affect the SLA, see the [Operational guidelines for Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines#database_flag_values).  | Yes  
[autovacuum_max_workers](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MAX-WORKERS) | `integer`  
`1` ... `varies (see note)`   
The default is **3**. **Note:** To determine the maximum value that you can set for this flag, you must first calculate the number of backend connections that are already in use. This calculation is the sum of the values for max_connections (maximum number of client connections), autovacuum_max_workers (maximum number of autovacuum processes), and [max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES). The sum cannot exceed `262142`.  | Yes  
[autovacuum_multixact_freeze_max_age](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MULTIXACT-FREEZE-MAX-AGE) | `integer`  
`10000` ... `2000000000`   
The default is **400000000**.   
For usage information that might affect the SLA, see the [Operational guidelines for Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines#database_flag_values).  | Yes  
[autovacuum_naptime](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-NAPTIME) | `integer`  
`1` ... `2147483`s   
The default is **60** s. | No  
[autovacuum_vacuum_cost_delay](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY) | `integer`  
`0` ... `100` ms, or `-1` to use the `vacuum_cost_delay` value  
For PostgreSQL 9.6, 10, and 11, the default value is 2 ms. | No  
[autovacuum_vacuum_cost_limit](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT) | `integer`  
`0` ... ` 10000`, or `-1` to use the `vacuum_cost_limit` value   
The default is **-1**. | No  
[autovacuum_vacuum_insert_scale_factor](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-INSERT-SCALE-FACTOR) | `float`  
`0` ... `100`   
The default is **0.2**. | No  
[autovacuum_vacuum_insert_threshold](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-INSERT-THRESHOLD) | `integer`  
`-1` ... `2147483647`   
The default is **1000**. | No  
[autovacuum_vacuum_max_threshold](https://www.postgresql.org/docs/18/static/runtime-config-vacuum.html#GUC-AUTOVACUUM-VACUUM-MAX-THRESHOLD) | `integer`  
`-1` ... `2147483647`   
The default is **100000000**.   
Supported in PostgreSQL 18 and later. | No  
[autovacuum_vacuum_scale_factor](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-SCALE-FACTOR) | `float`  
`0` ... `100`   
The default is **0.2**. | No  
[autovacuum_vacuum_threshold](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-THRESHOLD) | `integer`  
`0` ... `2147483647`   
The default is **50**. | No  
[autovacuum_work_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-AUTOVACUUM-WORK-MEM) | `integer`  
`0` ... `2147483647` KB, or `-1` to use the `maintenance_work_mem` value   
The default is **-1**. | No  
[autovacuum_worker_slots](https://www.postgresql.org/docs/18/static/runtime-config-vacuum.html#GUC-AUTOVACUUM-WORKER-SLOTS) | `integer`  
`1` ... `262143`   
The default is **16**.   
Supported in PostgreSQL 18 and later. | Yes  
[backend_flush_after](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-BACKEND-FLUSH-AFTER) | `integer`  
`0` ... `256`   
The unit is `8` KB.   
The default is **0**. | No  
[bgwriter_delay](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-BGWRITER-DELAY) | `integer`  
`10` ... `10000` ms   
The default is **200**. | No  
[bgwriter_flush_after](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-BGWRITER-FLUSH-AFTER) | `integer`  
`0` ... `256`   
The unit is `8` KB.   
The default is **64**. | No  
[bgwriter_lru_maxpages](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-BGWRITER-LRU-MAXPAGES) | `integer`  
`0` ... `1073741823`   
The default is **100**. | No  
[bgwriter_lru_multiplier](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-BGWRITER-LRU-MULTIPLIER) | `Float`  
`0` ... `10`   
The default is **2**. | No  
[checkpoint_completion_target](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-CHECKPOINT-COMPLETION-TARGET) | `float`  
`0.0` ... `1.0`   
The default is **0.9**. | No  
[checkpoint_flush_after](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-CHECKPOINT-FLUSH-AFTER) | `integer`  
`0` ... `256`   
Unit is `8` KB.   
The default is **32**. | No  
[checkpoint_timeout](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-CHECKPOINT-TIMEOUT) | `integer`  
`30` ... `86,400`s   
The default is **300** s.   
For usage information that might affect the SLA, see the [Operational guidelines for Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines#database_flag_values).  | No  
[checkpoint_warning](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-CHECKPOINT-WARNING) | `integer`  
`0` ... `2147483647`s   
The default is **30** s. | No  
[client_connection_check_interval](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-CLIENT-CONNECTION-CHECK-INTERVAL) | `integer`  
`0` ... `2147483647`   
The default is **0**. | No  
[ cloudsql.allow_passwordless_local_connections](https://docs.cloud.google.com/sql/docs/postgres/extensions#use_dblink_to_connect_without_a_password) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. Also, Cloud SQL doesn't support the flag for [Identity and Access Management (IAM) users](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users).  | No  
[ cloudsql.enable_anon](https://docs.cloud.google.com/sql/docs/postgres/extensions#postgresql_anonymizer) | `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | No  
[ cloudsql.enable_auto_explain](https://docs.cloud.google.com/sql/docs/postgres/extensions#auto_explain) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_index_advisor](https://docs.cloud.google.com/sql/docs/postgres/index-advisor-overview) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_maintenance_mode](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#flag_cloudsql_enable_maintenance_mode) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Overcome transaction ID (TXID) wraparound](https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound#flag_cloudsql_enable_maintenance_mode).  | Yes  
[ cloudsql.enable_parameterized_secure_views](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Parameterized secure views in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views).  | Yes  
[ cloudsql.enable_pgaudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit#enable-auditing-flag) | `boolean`  
`on` | `off`   
The default is **off**. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Auditing for PostgreSQL using pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit#enable-auditing-flag).  | Yes  
[ cloudsql.enable_pg_bigm](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_bigm) |  `boolean`  
`on` | `off`   
default: `off` **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ pg_bigm](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_bigm).  | Yes  
[ cloudsql.enable_pg_cron](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) |  `boolean`  
`on` | `off`   
The default is `off`.   
Supported in PostgreSQL 10 and later. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_pg_hint_plan](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_hint_plan) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_pglogical](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | Yes  
[ cloudsql.enable_pg_squeeze](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_squeeze) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_pg_textsearch](https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_pg_wait_sampling](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions) | `boolean`  
`on` | `off` **Note:** This flag is specific to Cloud SQL.  | Yes  
[ cloudsql.enable_vector_assist](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Vector assist overview](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview).  | Yes  
[ cloudsql.iam_authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances#configure-iam-db-instance) | `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL.  | No  
[ cloudsql.logical_decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) | `boolean`  
`on` | `off`   
The default is `off`. **Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | Yes  
[ cloudsql.max_failed_attempts_user](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication#user_password_policies) | `integer`  
`0` ... `10000`   
The default is **10**.   
**Note:** This flag is specific to Cloud SQL. It determines the number of users that can set the **Lock after failed attempts** restriction for a user password policy. This restriction specifies the number of times that a user can try a password incorrectly before their account is locked.  | Yes  
[ cloudsql.pgaudit_mask_literals](https://docs.cloud.google.com/sql/docs/postgres/pg-audit#mask-sensitive-data-in-audit-logs) | `boolean`  
`on` | `off`   
The default is `off`.   
**Note:** This flag is specific to Cloud SQL.  | No  
[cloudsql.pg_authid_select_role](https://docs.cloud.google.com/sql/docs/postgres/users#pg_shadow) | `string`  
**Note:** This flag is specific to Cloud SQL. For more information about this flag, see [ Access to the `pg_shadow` view and the `pg_authid` table](https://docs.cloud.google.com/sql/docs/postgres/users#pg_shadow).  | No  
[commit_delay](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-COMMIT-DELAY) | `integer`  
`0` ... `100000`   
The default is **0**. | No  
[commit_siblings](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-COMMIT-SIBLINGS) | `integer`  
`0` ... `1000`   
The default is **5**. | No  
[constraint_exclusion](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-CONSTRAINT-EXCLUSION) | `enumeration`  
`partition` | `on` | `off`   
The default is **partition**. | No  
[cpu_index_tuple_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-CONSTANTS) | `float`  
`0.0` ... `inf`   
The default is **0.005**. | No  
[cpu_operator_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-CPU-OPERATOR-COST) | `float`  
`0.0` ... `inf`   
The default is **0.0025**. | No  
[cpu_tuple_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-CPU-TUPLE-COST) | `float`  
`0.0` ... `inf`   
The default is **0.01**. | No  
[ cron.database_name](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c) | `String`.   
Supported in PostgreSQL 10 and later.  | Yes   
[ cron.log_statement](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c) | `boolean`   
`on` | `off`   
The default is **on**.   
Supported in PostgreSQL 10 and later.  | Yes   
[ cron.log_run](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c) | `boolean`   
`on` | `off`   
The default is **on**.   
Supported in PostgreSQL 10 and later.  | Yes   
[ cron.max_running_jobs](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c) | `Integer`   
`0 ... varies`   
The default is **5**.   
Supported in PostgreSQL 10 and later.  | Yes   
[ cron.log_min_messages](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c) | `String`   
`debug5|debug4|debug3|debug2|debug1|debug|`  
`info|notice|warning|error|log|fatal|panic`   
The default is **warning**.   
Supported in PostgreSQL 10 and later.  | No   
[cursor_tuple_fraction](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-OTHER) | `float`  
`0.0` ... `1.0`   
The default is **0.1**. | No  
[deadlock_timeout](https://www.postgresql.org/docs/current/static/runtime-config-locks.html) | `integer`  
`1` ... `2147483647` ms   
The default is **1000** ms. | No  
[default_statistics_target](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-DEFAULT-STATISTICS-TARGET) | `integer`  
`1` ... `10000`   
The default is **100**. | No  
[default_tablespace](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TABLESPACE) | `string` | No  
[default_toast_compression](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TOAST-COMPRESSION) | `string`   
The default is `pglz`. | No  
[default_transaction_deferrable](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-DEFERRABLE) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[default_transaction_isolation](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-ISOLATION) | `enumeration`  
`serializable` | `'repeatable read'` | `'read committed'` | `'read uncommitted'`   
The default is **'read committed'**. | No  
[effective_cache_size](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-EFFECTIVE-CACHE-SIZE) | `integer`  
The size range is from 10% - 70% of the instance's memory.   
Unit is `8` KB.   
The default is 40% of VM memory. For example, for a 45GB instance memory, the default value is `18537160` KB. | No  
[effective_io_concurrency](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-EFFECTIVE-IO-CONCURRENCY) | `integer`  
`0` ... `1000`   
The default is **1**. | No  
[enable_async_append](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-ASYNC-APPEND) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_bitmapscan](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_distinct_reordering](https://www.postgresql.org/docs/18/static/runtime-config-query.html#GUC-ENABLE-DISTINCT-REORDERING) | `boolean`  
`on` | `off`   
The default is **on**.   
Supported in PostgreSQL 18 and later. | No  
[enable_gathermerge](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-GATHERMERGE) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_incremental_sort](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-INCREMENTAL-SORT) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_memoize](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-MEMOIZE) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_parallel_append](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-PARALLEL-APPEND) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_parallel_hash](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-PARALLEL-HASH) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_partition_pruning](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-PARTITION-PRUNING) | `boolean`  
`on` | `off`   
The default is **on**.  | No  
[enable_partitionwise_aggregate](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-PARTITIONWISE-AGGREGATE) | `boolean`  
`on` | `off`   
The default is **off**.  | No  
[enable_partitionwise_join](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-ENABLE-PARTITIONWISE-JOIN) | `boolean`  
`on` | `off`   
The default is **off**.  | No  
[enable_hashagg](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_hashjoin](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_indexonlyscan](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_indexscan](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_material](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on** | No  
[enable_mergejoin](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_nestloop](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_self_join_elimination](https://www.postgresql.org/docs/18/static/runtime-config-query.html#GUC-ENABLE-SELF-JOIN-ELIMINATION) | `boolean`  
`on` | `off`   
The default is **on**.   
Supported in PostgreSQL 18 and later. | No  
[enable_seqscan](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_sort](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[enable_tidscan](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-ENABLE) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[force_parallel_mode](https://postgresqlco.nf/doc/en/param/force_parallel_mode/) | `enumeration`  
`off` | `on` | `regress`   
The default is **off**.   
**Note:** For PostgreSQL 16 and later, this flag is renamed to [`debug_parallel_query`](https://postgresqlco.nf/doc/en/param/debug_parallel_query/). | No  
[from_collapse_limit](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-FROM-COLLAPSE-LIMIT) | `integer`  
`1` ... `2147483647`   
The default is **8**. | No  
[geqo](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[geqo_effort](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `integer`  
`1` ... `10`   
The default is **5**. | No  
[geqo_generations](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `integer`  
`0` ... `2147483647`   
The default is **0**. | No  
[geqo_pool_size](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `integer`  
`0` ... `2147483647`   
The default is **0**. | No  
[geqo_seed](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `float`  
`0.0` ... `1.0`   
The default is **0**. | No  
[geqo_selection_bias](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `float`  
`1.5` ... `2.0`   
The default is **2**. | No  
[geqo_threshold](https://www.postgresql.org/docs/current/static/runtime-config-query.html#RUNTIME-CONFIG-QUERY-GEQO) | `integer`  
`2` ... `2147483647`   
The default is **12**. | No  
[gin_fuzzy_search_limit](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-GIN-FUZZY-SEARCH-LIMIT) | `integer`  
`0` ... `2147483647`   
The default is **0**. | No  
[gin_pending_list_limit](https://www.postgresql.org/docs/current/static/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT) | `integer`  
`64` ... `2147483647`KB   
The default is **4096** KB. | No  
[hash_mem_multiplier](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-HASH-MEM-MULTIPLIER) | `float`  
`1` ... `1000`   
The default is **2**. | No  
[hot_standby_feedback](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#RUNTIME-CONFIG-REPLICATION-STANDBY) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[huge_pages](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-HUGE-PAGES) | `enumeration`  
`try` | `off`   
The default is **try**. | Yes  
[idle_in_transaction_session_timeout](https://www.postgresql.org/docs/current/static/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT) | `integer`  
`0` ... `2147483647` ms   
The default is **0**. | No  
[io_max_concurrency](https://www.postgresql.org/docs/18/static/runtime-config-resource.html#GUC-IO-MAX-CONCURRENCY) | `integer`  
`-1` ... `1024`   
The default is **-1**.   
Supported in PostgreSQL 18 and later. | Yes  
[io_method](https://www.postgresql.org/docs/18/static/runtime-config-resource.html#GUC-IO-METHOD) | `string`  
`sync`, `worker`   
The default is **worker**.   
Supported in PostgreSQL 18 and later. | Yes  
[io_workers](https://www.postgresql.org/docs/18/static/runtime-config-resource.html#GUC-IO-WORKERS) | `integer`  
`-1` ... `32`   
The default is **3**.   
Supported in PostgreSQL 18 and later. | No  
[ ivfflat.probes](https://github.com/pgvector/pgvector#query-options) | `integer`   
`1` ... `varies`   
The default is **1**.   
Supported in PostgreSQL 11 and later.  | No   
[join_collapse_limit](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-JOIN-COLLAPSE-LIMIT) | `integer`  
`1` ... `2147483647`   
The default is **8**. | No  
[local_preload_libraries](https://www.postgresql.org/docs/current/static/local_preload_libraries) | `String`   
This flag lets you specify one or more shared libraries that are preloaded at the start of a database connection, in a comma-separated list. | No  
[lock_timeout](https://www.postgresql.org/docs/current/static/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT) | `integer`  
`0` ... `2147483647` ms   
The default is **0**. | No  
[log_autovacuum_min_duration](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-LOG-AUTOVACUUM-MIN-DURATION) | `integer`  
`0` ... `2147483647` ms, or `-1` to disable   
The default is **0**. | No  
[log_checkpoints](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_connections](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_disconnections](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_duration](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_error_verbosity](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHAT) | `enumeration`  
`terse` | `default` | `verbose`   
The default is **default**. | No  
[log_executor_stats](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-MONITOR) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_hostname](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-HOSTNAME) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_line_prefix](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-LINE-PREFIX) | `String`  
A printf-style string that's generated at the beginning of each line of a log file.   
The default is `%m [%p]: [%l-1] db=%d,user=%u`, which logs timestamp, process ID, database, and username.  
| No  
[log_lock_failures](https://www.postgresql.org/docs/18/static/runtime-config-logging.html#GUC-LOG-LOCK-FAILURES) | `boolean`  
`on` | `off`   
The default is **off**.   
Supported in PostgreSQL 18 and later. | No  
[log_lock_waits](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-LOCK-WAITS) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_min_duration_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-MIN-DURATION-STATEMENT) | `integer`  
`-1` ... `2147483647` ms   
The default is **-1**. | No  
[log_min_error_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN) | `enumeration`  
`debug5` | `debug4` | `debug3` | `debug2` | `debug1` | `info` | `notice` | `warning` | `error` | `log` | `fatal` | `panic`   
The default is **error**. | No  
[log_min_messages](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#RUNTIME-CONFIG-LOGGING-WHEN) | `enumeration`  
`debug5` | `debug4` | `debug3` | `debug2` | `debug1` | `info` | `notice` | `warning` | `error` | `log` | `fatal` | `panic`   
The default is **warning**. | No  
[log_parameter_max_length](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-PARAMETER-MAX-LENGTH) | `integer`  
`-1` ... `1073741823`   
The default is **-1**.   
Supported in PostgreSQL 13 and later. | No  
[log_parameter_max_length_on_error](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-PARAMETER-MAX-LENGTH-ON-ERROR) | `integer`  
`-1` ... `1073741823`   
The default is **0**.   
Supported in PostgreSQL 13 and later. | No  
[log_parser_stats](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-MONITOR) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_planner_stats](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-MONITOR) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_recovery_conflict_waits](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-RECOVERY-CONFLICT-WAITS) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_replication_commands](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-REPLICATION-COMMANDS) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[log_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-STATEMENT) | `enumeration`  
`none` | `ddl` | `mod` | `all`   
Set to `mod` to log all Data definition language (DDL) statements, plus data-modifying statements such as `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`   
The default is **none**. When not set to `none`, PostgreSQL can log statements that contain passwords. It's recommended to use [pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit) instead of [log_statement](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-STATEMENT). | No  
[log_statement_stats](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-MONITOR) | `boolean`  
`on` | `off`   
May not be enabled together with `log_parser_stats`, `log_planner_stats`, or `log_executor_stats`.   
The default is **off**. | No  
[log_temp_files](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-TEMP-FILES) | `integer`  
`0` ... `2147483647` KB, or `-1` to disable   
The default is **0**. | No  
[log_timezone](https://www.postgresql.org/docs/current/static/runtime-config-logging.html#GUC-LOG-TIMEZONE) | `string`  
This flag provides Cloud SQL for PostgreSQL users with a way to set the time zone used for timestamps that are written in the server log. You specify time zones by name. For example, `Europe/London` is the timezone name for London. You must update this flag manually, on the primary instance and on all read replicas, to account for it. Timezone names are case insensitive. You can supply the timezone name in any case. We support `UTC+X` as a valid format for this flag, where `X` is `+/-HH:MM`. At this time, we don't support POSIX time zone specifications. | Yes  
[logical_decoding_work_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM) | `integer`  
`64` ... `2147483647`   
The default is **65536**. | No  
[maintenance_io_concurrency](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE-IO-CONCURRENCY) | `integer`  
`0` ... `1000`   
The default is **10**. | No  
[maintenance_work_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) | `integer`  
`1024` ... `2147483647` KB   
The default is **64** MB. | No  
[max_active_replication_origins](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-ACTIVE-REPLICATION-ORIGINS) | `integer`  
`0` ... `262143`   
The default is **10** This flag must be set when using [read pools](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools).   
Supported in PostgreSQL 18 and later. | Yes  
[max_connections](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-MAX-CONNECTIONS) | `integer`  
`14` ... `varies (see note)`   
The default value depends on the amount of memory of the largest instance in the chain of primaries (this instance; and, if it's a read replica, its primary, its primary's primary, etc. all the way up to the root of the replication tree). | Memory (GB) on largest instance| Default value  
---|---  
tiny (~0.5)| 25  
small (~1.7)| 50  
from 3.75 to < 6| 100  
from 6 to < 7.5| 200  
from 7.5 to < 15| 400  
from 15 to < 30| 500  
from 30 to < 60| 600  
from 60 to < 120| 800  
>=120| 1,000  
  
**Note:** To determine the maximum value that you can set for this flag, you must first calculate the number of backend connections that are already in use. This calculation is the sum of the values for max_connections (maximum number of client connections), autovacuum_max_workers (maximum number of autovacuum processes), and [max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES). The sum cannot exceed `262142`. 

The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that is lower than the new value on the primary, or that have not been changed from the default value. Such changes on the primary cause the replica to restart. 

Yes  
[max_locks_per_transaction](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION) | `integer`  
`10` ... `2,147,483,647`   
The default is **64**. The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that is lower than the new value on the primary, or that have not been changed from the default value. Such changes on the primary cause the replica to restart.  | Yes  
[max_logical_replication_workers](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-LOGICAL-REPLICATION-WORKERS) | `integer`  
`4` ... `8192`   
The default is **4**.   
Supported in PostgreSQL 10 and later. | Yes  
[max_parallel_maintenance_workers](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS) | `integer`  
`0` ... `varies` **Note:** Limits based on the RAM in the instance, in the way described for `max_worker_processes`.  
The default is **2**.   
Supported in PostgreSQL 11 and later. The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that's lower than the new value on the primary, or that haven't been changed from the default value.  If the value on the primary is `default`, then the value for the replicas can't be changed. To change the value for the replicas, first, set the value on the primary to an integer. | No  
[max_parallel_workers](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS) | `integer`  
`0` ... `varies` **Note:** Limits based on the RAM in the instance, in the way described for `max_worker_processes`.  
The default is **8**.   
Supported in PostgreSQL 10 and later. The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that's lower than the new value on the primary, or that haven't been changed from the default value.  If the value on the primary is `default`, then the value for the replicas can't be changed. To change the value for the replicas, first, set the value on the primary to an integer. | No  
[max_parallel_workers_per_gather](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER) | `integer`  
`0` ... `varies` **Note:** Limits based on the RAM in the instance, in the way described for `max_worker_processes`.  
The default is **2**. The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that's lower than the new value on the primary, or that haven't been changed from the default value.  If the value on the primary is `default`, then the value for the replicas can't be changed. To change the value for the replicas, first, set the value on the primary to an integer. | No  
[max_pred_locks_per_page](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-PAGE) | `integer`  
`0` ... `2147483647`   
The default is **2**.   
Supported in PostgreSQL 10 and later. | No  
[max_pred_locks_per_relation](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-RELATION) | `integer`  
`-2147483648` ... `2147483647`   
The default is **-2**.   
Supported in PostgreSQL 10 and later. | No  
[max_pred_locks_per_transaction](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-TRANSACTION) | `integer`  
`64` ... `1048576` **Note:** The maximum value of this setting scales linearly with the memory available on your instance. | Memory size (GB)| Maximum value  
---|---  
0 - 1| 512  
1 - 2| 1024  
2 - 4| 2048  
4 - 8| 4096  
8 - 16| 8192  
16 - 32| 16384  
32 - 64| 32768  
64 - 128| 65536  
128 - 256| 131072  
256 - 512| 262144  
512 - 1024| 524288  
> 1024| 1048576  
Yes  
[max_prepared_transactions](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PREPARED-TRANSACTIONS) | `integer`  
`0` ... `varies`  
| Memory size (MB)| Max value  
---|---  
0 - 3,840| 30,000  
3,840 - 7,680| 85,000  
7,680 - 15,360| 200,000  
15,360 and later| 262,000  
  
The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that is lower than the new value on the primary, or that have not been changed from the default value. Such changes on the primary cause the replica to restart. 

Yes  
[ max_replication_slots](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) | `integer`  
`10` ... `varies` **Note:** The maximum value of this setting scales linearly with the memory available on your instance. | Memory size (GB)| Max value  
---|---  
0 - 4| 10  
4 - 16| 32  
16 - 32| 128  
32 - 64| 256  
64 -128| 512  
128 - 256| 1024  
256 - 512| 2048  
> 512| 4096  
  
For more information about this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).   
The default is **10**.  Yes  
[max_slot_wal_keep_size](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE) | `integer`  
`102400` ... `10485760`   
Unit is `MB` | No  
[max_stack_depth](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-STACK-DEPTH) | `integer`  
`100` ... `7680`   
Unit is `KB`. | No  
[max_standby_archive_delay](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-STANDBY-ARCHIVE-DELAY) | `integer`  
`0` ... `2147483647` ms, or `-1` to wait forever  | No  
[max_standby_streaming_delay](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-STANDBY-STREAMING-DELAY) | `integer`  
`0` ... `2147483647 `ms, or `-1` to wait forever | No  
[max_sync_workers_per_subscription](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-MAX-SYNC-WORKERS-PER-SUBSCRIPTION) | `integer`  
`2` ... `64`   
Cannot be greater than `max_logical_replication_workers`.  | No  
[ max_wal_senders](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) | `integer`  
`10` ... `varies`   
The default is **10**. **Note:** The maximum value of this setting scales linearly with the memory available on your instance. This value must be set to a value greater than or equal to the value of `max_replication_slots`. | Memory size (GB)| Max value  
---|---  
0 - 4| 10  
4 - 16| 32  
16 - 32| 128  
32 - 64| 256  
64 -128| 512  
128 - 256| 1024  
256 - 512| 2048  
> 512| 4096  
  
For more information about this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication). 

The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that is lower than the new value on the primary, or that have not been changed from the default value. Such changes on the primary cause the replica to restart. 

Yes  
[max_wal_size](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-MAX-WAL-SIZE) | `integer`  
`2` ... `2147483647` The unit is 16 MB (the WAL file size) for version 9.6 and 1 MB for PostgreSQL 10 and later. The default value is `1504` MB if instance memory more than or equal to `3.75` GB. The default value is `1` GB if instance memory is less than `3.75` GB.  For usage information that might affect the SLA, see the [Operational guidelines for Cloud SQL for PostgreSQL instances](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines#database_flag_values).  | No  
[max_worker_processes](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) | `integer`  
`8` ... `varies` **Note:** The maximum value of this setting scales linearly with the memory available on your instance. | Memory size (GB)| Max value  
---|---  
from 0 to < 8| 10  
from 8 to < 16| 16  
from 16 to < 32| 32  
from 32 to < 64| 64  
from 64 to < 128| 128  
from 128 to < 256| 256  
from 256 to < 512| 512  
> 512| 1024  
  
For more information about this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).

The value on replicas must be greater than or equal to the value on the primary. Changes on the primary propagate to replicas that have a value that is lower than the new value on the primary, or that have not been changed from the default value. Such changes on the primary cause the replica to restart. 

Yes  
[min_parallel_index_scan_size](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-MIN-PARALLEL-INDEX-SCAN-SIZE) | `integer`  
`0` ... `715827882`   
Unit is `8` KB | No  
[min_parallel_table_scan_size](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-MIN-PARALLEL-TABLE-SCAN-SIZE) | `integer`  
`0` ... `715827882`   
Unit is `8` KB | No  
[min_parallel_relation_size](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-MIN-PARALLEL-RELATION-SIZE) | `integer`  
`0` ... `715827882`   
Unit is `8` KB   
Supported only in PostgreSQL 9.6. | No  
[min_wal_size](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-MIN-WAL-SIZE) | `integer`  
`32` ... `2147483647` The unit is 16 MB (the WAL file size) for version 9.6 and 1 MB for PostgreSQL 10 and later.  | No  
[old_snapshot_threshold](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-OLD-SNAPSHOT-THRESHOLD) | `integer`  
`0` ... `86400` min, or `-1` to disable   
The default is **-1**. **Note:** For PostgreSQL 17, this flag is deprecated. | Yes  
[parallel_setup_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-PARALLEL-SETUP-COST) | `float`  
`0.0` ... `inf`   
The default is **1000**. | No  
[parallel_tuple_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-PARALLEL-TUPLE-COST) | `float`  
`0.0` ... `inf`   
The default is **0.1**. | No  
[ password_encryption](https://www.postgresql.org/docs/current/static/runtime-config-connection.html) | `enumeration`  
`md5` | `scram-sha-256` The default depends on the PostgreSQL version. For PostgreSQL versions 10 to 13, the default is `md5`. For PostgreSQL 14 and higher, the default is `scram-sha-256`. | No  
[ pg_bigm.enable_recheck](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html#parametares) | `boolean`   
`on` | `off` | No  
[ pg_bigm.gin_key_limit](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html#parametares) | `integer`  
`0` ... `2147483647` | No  
[ pg_bigm.similarity_limit](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html#parametares) | `float`  
`0.0` ... `1.0` | No  
[ pg_hint_plan.enable_hint](https://pghintplan.osdn.jp/pg_hint_plan.html) | `boolean`   
`on` | `off`   
The default is **on**.  | No   
[ pg_hint_plan.debug_print](https://pghintplan.osdn.jp/pg_hint_plan.html) | `String`   
`off|on|detailed|verbose|0|1||2|3|no|yes|false|true`   
The default is **off**.  | No   
[ pg_hint_plan.parse_messages](https://pghintplan.osdn.jp/pg_hint_plan.html) | `String`   
`debug5|debug4|debug3|debug2|debug1|debug|`  
`info|notice|warning|error|log`   
The default is **info**.  | No   
[ pg_hint_plan.message_level](https://pghintplan.osdn.jp/pg_hint_plan.html) | `String`   
`debug5|debug4|debug3|debug2|debug1|debug|`  
`info|notice|warning|error|log`   
The default is **log**.  | No   
[ pg_hint_plan.enable_hint_table](https://pghintplan.osdn.jp/pg_hint_plan.html) | `boolean`   
`on` | `off`   
The default is **off**.  | No   
[ pglogical.batch_inserts](https://github.com/2ndQuadrant/pglogical#configuration-options) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | Yes  
[ pglogical.conflict_log_level](https://github.com/2ndQuadrant/pglogical#configuration-options) |  `String`  
The default is `LOG`.  
This flag accepts the same values as `log_min_messages`. **Note:** For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | No  
[ pglogical.conflict_resolution](https://github.com/2ndQuadrant/pglogical#configuration-options) |  `String`  
`error|apply_remote|keep_local|last_update_wins|first_update_wins ` The default is `apply_remote`. **Note:** The values `keep_local`, `last_update_wins` and `first_update_wins` requires `track_commit_timestamps` to be enabled on both nodes. For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | No  
[ pglogical.extra_connection_options](https://github.com/2ndQuadrant/pglogical#subscription-management) |  `String`   
Accepts PostgreSQL [ keyword/value connection strings](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING).   
The default is the empty string. **Note:** For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | No  
[ pglogical.synchronous_commit](https://github.com/2ndQuadrant/pglogical#synchronous-replication) |  `boolean`  
`on` | `off`   
The default is `on`. **Note:** For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | Yes  
[ pglogical.use_spi](https://github.com/2ndQuadrant/pglogical#configuration-options) |  `boolean`  
`on` | `off`   
The default is `off`. **Note:** For information about the feature that uses this flag, see [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  | Yes  
[pg_stat_statements.max](https://www.postgresql.org/docs/current/static/pgstatstatements.html#id-1.11.7.38.8) | `integer`  
`100` ... `2147483647`   
The default is **5000**. | Yes  
[pg_stat_statements.save](https://www.postgresql.org/docs/current/static/pgstatstatements.html#id-1.11.7.38.8) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[pg_stat_statements.track](https://www.postgresql.org/docs/current/static/pgstatstatements.html#id-1.11.7.38.8) | `enumeration`  
`none` | `top` | `all`   
The default is **top**. | No  
[pg_stat_statements.track_planning](https://www.postgresql.org/docs/current/static/pgstatstatements.html#id-1.11.7.38.8) | `boolean`  
`on` | `off`   
The default is **off**.   
Supported in PostgreSQL 13 and later. | No  
[pg_stat_statements.track_utility](https://www.postgresql.org/docs/current/static/pgstatstatements.html#id-1.11.7.38.8) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[pg_textsearch.bulk_load_threshold](https://github.com/timescale/pg_textsearch) | `integer`  
The number of terms per transaction before auto-spill. Set to 0 to disable.   
The default is 100,000.   
Supported in PostgreSQL 17 and later. | No  
[pg_textsearch.compress_segments](https://github.com/timescale/pg_textsearch) | `boolean`  
`on` | `off`  
Compress posting blocks in new segments.   
The default is **on**.   
Supported in PostgreSQL 17 and later. | No  
[pg_textsearch.default_limit](https://github.com/timescale/pg_textsearch) | `integer`  
The maximum number of documents scored when no `LIMIT` clause is present.   
The default is 1,000.   
Supported in PostgreSQL 17 and later. | No  
[pg_textsearch.memtable_pages_threshold](https://github.com/timescale/pg_textsearch) | `integer`  
The number of pages to chain before auto-spill. Set it to 0 to disable.   
The default is 64.   
Supported in PostgreSQL 17 and later.  | No  
[pg_textsearch.segments_per_level](https://github.com/timescale/pg_textsearch) | `integer`  
The number of segments per level before automatic compaction occurs.   
The range is 0-64, and the default is 8.   
Supported in PostgreSQL 17 and later. | No  
[ pgaudit.log](https://github.com/pgaudit/pgaudit#pgauditlog) | `enumeration`  
`read` | `write` | `function` | `role` | `ddl` | `misc` | `misc_set` | `all|none` You can provide multiple classes using a comma-separated list, and subtract a class by prefacing the class with a `-` sign. The default is `none`.  | No  
[ pgaudit.log_catalog](https://github.com/pgaudit/pgaudit#pgauditlog_catalog) | `boolean`  
`on` | `off`   
The default is `on`.  | No  
[ pgaudit.log_client](https://github.com/pgaudit/pgaudit#pgauditlog_client) | `boolean`  
`on` | `off`   
The default is `off`.  | No  
[ pgaudit.log_level](https://github.com/pgaudit/pgaudit#pgauditlog_level) | `enumeration`  
`debug5` | `debug4` | `debug3` | `debug2` | `debug1` | `info` | `notice` | `warning` | `error` | `log`   
The default is `log`. Additionally, `pgaudit.log_level` is enabled only when `pgaudit.log_client` is on.  | No  
[ pgaudit.log_parameter](https://github.com/pgaudit/pgaudit#pgauditlog_parameter) | `boolean`  
`on` | `off`   
The default is `off`.  | No  
[ pgaudit.log_relation](https://github.com/pgaudit/pgaudit#pgauditlog_relation) | `boolean`  
`on` | `off`   
The default is `off`.  | No  
[ pgaudit.log_statement_once](https://github.com/pgaudit/pgaudit#pgauditlog_statement_once) | `boolean`  
`on` | `off`   
The default is `off`.  | No  
[ pgaudit.role](https://github.com/pgaudit/pgaudit#pgauditrole) | `string`   
There is no default.  | No  
[ pgaudit.log_rows](https://github.com/pgaudit/pgaudit#pgauditlog_rows) | `boolean`   
The default is off.  | No  
[pgtt.enabled](https://github.com/darold/pgtt#configuration) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[pg_wait_sampling.history_period](https://github.com/postgrespro/pg_wait_sampling) | `integer`  
`1` ... `2147483647` | No  
[pg_wait_sampling.history_size](https://github.com/postgrespro/pg_wait_sampling) | `integer`  
`1` ... `2147483647` | No  
[pg_wait_sampling.profile_period](https://github.com/postgrespro/pg_wait_sampling) | `integer`  
`1` ... `2147483647` | No  
[pg_wait_sampling.profile_pid](https://github.com/postgrespro/pg_wait_sampling) | `boolean`  
`on` | `off` | No  
[pg_wait_sampling.profile_queries](https://github.com/postgrespro/pg_wait_sampling) | `boolean`  
`on` | `off` | No  
[random_page_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-RANDOM-PAGE-COST) | `float`  
`0.0` ... `inf`   
The default is **4**. | No  
[ plan_cache_mode](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-PLAN-CACHE-MODE) | `String`   
`auto|force_generic_plan|force_custom_plan`   
The default is **auto**.  | No   
[rdkit.agent_FP_bit_ratio](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `float`  
`0` ... `3` | No  
[rdkit.avalon_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.dice_threshold](https://www.rdkit.org/docs/Cartridge.html#parameters) | `float`  
`0` ... `1` | No  
[rdkit.difference_FP_weight_agents](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`-10` ... `10` | No  
[rdkit.difference_FP_weight_nonagents](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`1` ... `20` | No  
[rdkit.do_chiral_sss](https://www.rdkit.org/docs/Cartridge.html#parameters) | `boolean`  
`on` | `off` | No  
[rdkit.do_enhanced_stereo_sss](https://www.rdkit.org/docs/Cartridge.html#parameters) | `boolean`  
`on` | `off` | No  
[rdkit.featmorgan_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.hashed_atompair_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.hashed_torsion_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.ignore_reaction_agents](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `boolean`  
`on` | `off` | No  
[rdkit.init_reaction](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `boolean`  
`on` | `off` | No  
[rdkit.layered_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.morgan_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.move_unmmapped_reactants_to_agents](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `boolean`  
`on` | `off` | No  
[rdkit.rdkit_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `9192` | No  
[rdkit.reaction_difference_fp_size](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`64` ... `9192` | No  
[rdkit.reaction_difference_fp_type](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`1` ... `3` | No  
[rdkit.reaction_sss_fp_size](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`64` ... `9192` | No  
[rdkit.reaction_sss_fp_type](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `integer`  
`1` ... `5` | No  
[rdkit.sss_fp_size](https://www.rdkit.org/docs/Cartridge.html#parameters) | `integer`  
`64` ... `4096` | No  
[rdkit.tanimoto_threshold](https://www.rdkit.org/docs/Cartridge.html#parameters) | `float`  
`0` ... `1` | No  
[rdkit.threshold_unmapped_reactant_atoms](https://github.com/rdkit/rdkit/blob/master/Code/PgSQL/rdkit/guc.c) | `float`  
`0` ... `1` | No  
[recovery_prefetch](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-RECOVERY-PREFETCH) | `string`  
`on` | `off` | `try`   
The default is **try**.   
Supported in PostgreSQL 15 and later. | No  
[replacement_sort_tuples](https://www.postgresql.org/docs/10/runtime-config-resource.html#GUC-REPLACEMENT-SORT-TUPLES) | `integer`  
`0` ... `2147483647` **Warning:** This flag is supported only until PostgreSQL 9.6 for Cloud SQL. | No  
[reserved_connections](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-RESERVED-CONNECTIONS) | `integer`  
`0` ... `262143`   
Supported in PostgreSQL 16 and later. | Yes  
  
[session_replication_role](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-SESSION-REPLICATION-ROLE) | `enumeration`  
`origin` | `replica` | `local`   
[Can be set only in current session](https://docs.cloud.google.com/sql/docs/postgres/flags#flag_session_replication_role) | -  
[seq_page_cost](https://www.postgresql.org/docs/current/static/runtime-config-query.html#GUC-SEQ-PAGE-COST) | `float`  
`0.0` ... `inf`   
The default is **1.0**.  | No  
[shared_buffers](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-SHARED-BUFFERS) | `integer`  
The size range is from 10% - 60% of the instance's memory.   
Unit is `8` KB.   
The default is one-third of the instance's total VM memory (in MB). For example, for `45` GB of instance memory, the default value is `15085`MB.  | Yes  
[squeeze.max_xlock_time](https://github.com/cybertec-postgresql/pg_squeeze?tab=readme-ov-file#control-the-impact-on-other-backends) | `integer`  
`1` ... `2147483647` | No  
[squeeze.worker_autostart](https://github.com/cybertec-postgresql/pg_squeeze?tab=readme-ov-file#enable--disable-table-processing) | `string`  
| Yes  
[squeeze.worker_role](https://github.com/cybertec-postgresql/pg_squeeze?tab=readme-ov-file#enable--disable-table-processing) | `string`  
| Yes  
[ssl_max_protocol_version](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-SSL-MAX-PROTOCOL-VERSION) | `enumeration`  
Postgres 14: Sets the maximum SSL/TLS protocol version to use. Valid values are as for `ssl_min_protocol_version`, with the addition of an empty string, which allows any protocol version to be specified.   
Supported in PostgreSQL 12 and later. | No  
[ssl_min_protocol_version](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-SSL-MIN-PROTOCOL-VERSION) | `enumeration`  
Postgres 14: Sets the minimum SSL/TLS protocol version to use. Valid values are currently: `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`.   
The default is `TLSv1`.   
Supported in PostgreSQL 12 and later. | No  
  
[standard_conforming_strings](https://www.postgresql.org/docs/current/static/runtime-config-compatible.html#GUC-STANDARD-CONFORMING-STRINGS) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[synchronize_seqscans](https://www.postgresql.org/docs/current/static/runtime-config-compatible.html#RUNTIME-CONFIG-COMPATIBLE-VERSION) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[tcp_keepalives_count](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-TCP-KEEPALIVES-COUNT) | `integer`  
`0` ... `2147483647`   
The default is **5**. | No  
[tcp_keepalives_idle](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-TCP-KEEPALIVES-IDLE) | `integer`  
`0` ... `2147483647`   
The default is **60**. | No  
[tcp_keepalives_interval](https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-TCP-KEEPALIVES-INTERVAL) | `integer`  
`0` ... `2147483647`   
The default is **60**. | No  
[temp_buffers](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) | `integer`  
`100` ... `1,073,741,823`   
Unit is `8` KB | No  
[temp_file_limit](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-DISK) | `integer`  
`1048576` ... `2147483647` KB   
The default is 10% of the initial disk size. For example, for a 100-GB disk, the default value is `10262623`KB. | No  
[TimeZone](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-TIMEZONE) | `string`  
This flag provides Cloud SQL for PostgreSQL users with a way to set the time zone for displaying and analyzing timestamps. You specify time zones by name. For example, `Europe/London` is the timezone name for London. You must update this flag manually, on the primary instance and on all read replicas, to account for it. Timezone names are case insensitive. You can supply the timezone name in any case. We support `UTC+X` as a valid format for this flag, where `X` is `+/-HH`. At this time, we don't support POSIX time zone specifications. | Yes  
[trace_notify](https://www.postgresql.org/docs/current/static/runtime-config-developer.html) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[trace_recovery_messages](https://www.postgresql.org/docs/current/static/runtime-config-developer.html) | `enumeration`  
`debug5` | `debug4` | `debug3` | `debug2` | `debug1` | `log` | `notice` | `warning` | `error`   
The default is **log**. **Note:** For PostgreSQL 17, this flag is deprecated. | No  
[trace_sort](https://www.postgresql.org/docs/current/static/runtime-config-developer.html) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[track_activities](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-COLLECTOR) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[track_activity_query_size](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#RUNTIME-CONFIG-STATISTICS-COLLECTOR) | `integer`  
`100` ... `102400`   
The default is **1** KB. | Yes  
[track_commit_timestamp](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#RUNTIME-CONFIG-REPLICATION-SENDER) | `boolean`  
`on` | `off`   
The default is **off**. | Yes  
[track_cost_delay_timing](https://www.postgresql.org/docs/18/static/runtime-config-statistics.html#GUC-TRACK-COST-DELAY-TIMING) | `boolean`  
`on` | `off`   
The default is **off**.   
Supported in PostgreSQL 18 and later. | No  
[track_counts](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#GUC-TRACK-COUNTS) | `boolean`  
`on` | `off`   
The default is **on**. | No  
[track_functions](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#GUC-TRACK-FUNCTIONS) | `enumeration`  
`none` | `pl` | `all`   
The default is **none**. | No  
[track_io_timing](https://www.postgresql.org/docs/current/static/runtime-config-statistics.html#GUC-TRACK-IO-TIMING) | `boolean`  
`on` | `off`   
The default is **off**. | No  
[vacuum_cost_delay](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-VACUUM-COST) | `integer`  
`0` ... `100` ms   
The default is **0**. | No  
[vacuum_cost_limit](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-VACUUM-COST-LIMIT) | `integer`  
`1` ... `10000`   
The default is **200**. | No  
[vacuum_cost_page_dirty](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-VACUUM-COST-PAGE-DIRTY) | `integer`  
`0` ... `10000`   
The default is **20**. | No  
[vacuum_cost_page_hit](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-VACUUM-COST-PAGE-HIT) | `integer`  
`0` ... `10000`   
The default is **1**. | No  
[vacuum_cost_page_miss](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-VACUUM-COST-PAGE-MISS) | `integer`  
`0` ... `10000`   
The default is **10**. | No  
[vacuum_failsafe_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-FAILSAFE-AGE) | `integer`  
`0` ... `2100000000`   
The default is **1600000000**. | No  
[vacuum_freeze_min_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-FREEZE-MIN-AGE) | `integer`  
`0` ... `1000000000`   
The default is **50000000**. | No  
[vacuum_freeze_table_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-FREEZE-TABLE-AGE) | `integer`  
`0` ... `2000000000`   
The default is **150000000**.  | No  
[vacuum_max_eager_freeze_failure_rate](https://www.postgresql.org/docs/18/static/runtime-config-vacuum.html#GUC-VACUUM-MAX-EAGER-FREEZE-FAILURE-RATE) | `float`  
`0` ... `1`   
The default is **0.03**.   
Supported in PostgreSQL 18 and later.  | No  
[vacuum_multixact_failsafe_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-MULTIXACT-FAILSAFE-AGE) | `integer`  
`0` ... `2100000000`   
The default is **1600000000**. | No  
[vacuum_multixact_freeze_min_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-MULTIXACT-FREEZE-MIN-AGE) | `integer`  
`0` ... `1000000000`   
The default is **5000000**.  | No  
[vacuum_multixact_freeze_table_age](https://www.postgresql.org/docs/current/static/runtime-config-client.html#GUC-VACUUM-MULTIXACT-FREEZE-TABLE-AGE) | `integer`  
`0` ... `2000000000`   
The default is **150000000**. | No  
[vacuum_truncate](https://www.postgresql.org/docs/18/static/runtime-config-vacuum.html#GUC-VACUUM-TRUNCATE) | `boolean`  
`on` | `off`   
The default is **on**.   
Supported in PostgreSQL 18 and later. | No  
[wal_buffers](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-WAL-BUFFERS) | `integer`  
The size range is from -1 - 5% of the instance's memory.   
Unit is `8` KB.   
The default is **16** MB.  | Yes  
[ wal_compression](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-WAL-COMPRESSION) | `enumeration`  
`off` | `on` | `pglz` | `lz4` | `zstd`   
The default is **off**.   
**Note:** The `pglz`, `lz4`, and `zstd` values are supported only for PostgreSQL versions 15 and later. | No  
[wal_decode_buffer_size](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-WAL-DECODE-BUFFER-SIZE) | `integer`  
`65536` ... `1073741823`   
Unit is `B`.   
Supported in PostgreSQL 15 and later. | Yes  
[ wal_receiver_timeout](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-WAL-RECEIVER-TIMEOUT) | `integer`  
`0` ... `2147483647`   
The default is 60 seconds. This flag affects the WAL sender and receiver. If not appropriately set, this flag affects logical and physical replication. This flag also affects replication performance and latency. A value of zero disables the timeout mechanism. The unit is milliseconds.  | No  
[ wal_sender_timeout](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) | `integer`  
`0` ... `2147483647`   
The default is 60 seconds. This flag affects the WAL sender and receiver. If not appropriately set, this flag affects logical and physical replication. This flag also affects replication performance and latency. A value of zero disables the timeout mechanism. The unit is milliseconds.  | No  
[wal_writer_delay](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-WAL-WRITER-DELAY) | `integer`  
`1` ... `10000`   
The default is **200**. | No  
[wal_writer_flush_after](https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-WAL-WRITER-FLUSH-AFTER) | `integer`  
`0` ... `2147483647`   
The default is **128**. | No  
  
[work_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-WORK-MEM) | `integer`  
`64` ... `2147483647` KB   
The default is **4** MB. | No  
  
## Special flags

### `bgwriter`

PostgreSQL has a background writer (`bgwriter`) flag. This flag issues writes of new or modified shared buffers. These shared buffers are known as dirty buffers. When the number of clean shared buffers is insufficient, the background writer writes dirty buffers to the file system and marks them as clean.

Two flags associated with the `bgwriter` flag are `bgwriter_delay` and `bgwriter_lru_maxpages`. `bgwriter_delay` specifies the delay between activity rounds for the background writer in milliseconds (ms), and `bgwriter_lru_maxpages` specifies how many buffers will be written by the background writer.

The default value for the `bgwriter` flag is `200 ms`. However, if you select a solid state drive (SSD) that's greater than 500 GB, then the value of the `bgwriter_delay` flag is set to `50`, and the value of the `bgwriter_lru_maxpages` flag is set to `200`.

For more information about the [background writer](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-BACKGROUND-WRITER), see the PostgreSQL documentation.

### `cloudsql_session_read_only`

You can use the `cloudsql_session_read_only` flag to create a [read-only session](https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions).

This flag can be set to `on`, `off`, or `locked`. Its default value is `off`.

**Note:** This flag is specific to Cloud SQL. It is not a PostgreSQL flag.

### `session_replication_role`

PostgreSQL has the `session_replication_role` flag, which is designed to be used for logical replication and lets you disable constraint triggers in individual sessions.

Sometimes this flag can also be used for some maintenance operations to circumvent constraint (most often Foreign Key) checks.

This flag can be set in a session by any user which has the `REPLICATION` property set. The `REPLICATION` property for any user can be set by `cloudsqlsuperuser` when one of flags [ cloudsql.enable_pglogical](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) or [ cloudsql.logical_decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication) is set for the instance.

This flag can not be set for the whole instance.

## Troubleshooting

Issue | Troubleshooting | You set the time zone for a session, but it expires when you log off. |  Connect to the database and set the database time zone to the one you want, either per user or per database. In Cloud SQL for PostgreSQL, you can specify the following. These settings remain after a session is closed, mimicking a `.conf` configuration:
    
    
    ALTER DATABASE dbname SET TIMEZONE TO 'timezone';
    ALTER USER username SET TIMEZONE TO 'timezone';

These settings apply only to new connections to the database. To see the change to the time zone, disconnect from the instance and then reconnect to it.  
---|---  
  
## What's next

  * Learn more about [PostgreSQL server configuration](https://www.postgresql.org/docs/current/static/runtime-config.html).
  * Learn more about [Operational Guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
