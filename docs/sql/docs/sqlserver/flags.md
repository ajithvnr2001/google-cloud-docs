---
url: https://docs.cloud.google.com/sql/docs/sqlserver/flags/
title: Configure database flags \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:12.291151+00:00
---

# Configure database flags  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/flags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Configure database flags Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/flags "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/flags "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to configure database flags for Cloud SQL, and lists the flags that you can set for your instance. You use database flags for many operations, including adjusting SQL Server parameters, adjusting options, and configuring and tuning an instance.

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

For example, to set the `1204`, `remote access`, and `remote query timeout (s)` flags, you can use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --database-flags="1204"=on,"remote access"=on,"remote query timeout (s)"=300

### Terraform

To add database flags, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "instance" {
      name             = "sqlserver-instance-flags"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        database_flags {
          name  = "1204"
          value = "on"
        }
        database_flags {
          name  = "remote access"
          value = "on"
        }
        database_flags {
          name  = "remote query timeout (s)"
          value = "300"
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
    

### Determine which database flags have been set for an instance

To see which flags have been set for a Cloud SQL instance:

### Console

  1. In the [Google Cloud console](https://console.cloud.google.com/project/_/sql/instances), select the project that contains the Cloud SQL instance for which you want to see the database flags that have been set.
  2. Select the instance to open its **Instance Overview** page. 

The database flags that have been set are listed under the **Database flags** section.




### gcloud

Get the instance state:
    
    
    gcloud sql instances describe INSTANCE_NAME

In the output, database flags are listed under the `settings` as the collection `databaseFlags`. For more information about the representation of the flags in the output, see [Instances Resource Representation](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances). 

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

Cloud SQL supports only those flags that are listed in this section.

**Note:** When you create an instance, you can set a permanent time zone for the instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone).Cloud SQL Flag | Type  
Acceptable Values and Notes | Restart  
Required?  
---|---|---  
[1204 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[1222 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[1224 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[2528 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[3205 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[3226 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[3625 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | Yes  
[4199 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[4616 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | No  
[7806 (trace flag)](https://docs.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver15#trace-flags) | `boolean`  
`on` | `off` | Yes  
[13702 (trace flag)](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-traceon-trace-flags-transact-sql?view=sql-server-ver17#tf13702) | `boolean`  
`on` | `off` | Yes  
[access check cache bucket count](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/access-check-cache-server-configuration-options?view=sql-server-ver15) | `integer`  
`0` ... `65536` | No  
[access check cache quota](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/access-check-cache-server-configuration-options?view=sql-server-ver15) | `integer`  
`0` ... `2147483647` | No  
[affinity mask](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-mask-server-configuration-option?view=sql-server-ver15) | `integer`  
`2147483648` ... `2147483647` | Yes  
[affinity I/O mask](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-input-output-mask-server-configuration-option?view=sql-server-ver15) | `integer`  
`2147483648` ... `2147483647` | Yes  
[agent xps](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/agent-xps-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[automatic soft-numa disabled](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/soft-numa-sql-server?view=sql-server-ver15) | `boolean`  
`on` | `off` | Yes  
[cloud sql xe bucket name](https://docs.cloud.google.com/sql/docs/sqlserver/extended-events#xevent_session_configuration_parameters) | `string`  
The bucket name must start with the `gs://` prefix. | No  
[cloud sql xe output total disk size (mb)](https://docs.cloud.google.com/sql/docs/sqlserver/extended-events#xevent_session_configuration_parameters) | `integer`  
`10` ... `512` | No  
[cloud sql xe file retention (mins)](https://docs.cloud.google.com/sql/docs/sqlserver/extended-events#xevent_session_configuration_parameters) | `integer`  
`0` ... `10080` | No  
[cloud sql xe upload interval (mins)](https://docs.cloud.google.com/sql/docs/sqlserver/extended-events#xevent_session_configuration_parameters) | `integer`  
`1` ... `60` | No  
[cloudsql enable linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers) | `boolean`  
`on` | `off` | No  
[cost threshold for parallelism](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-cost-threshold-for-parallelism-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[contained database authentication](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/contained-database-authentication-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[ cross db ownership chaining](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/cross-db-ownership-chaining-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` This flag is deprecated for all SQL Server versions. Going forward, you can't set its value to `on`. However, if you have this flag enabled, we strongly recommend that you either remove the flag from your database or set it to `off`. For cross-database access, use the [ Microsoft tutorial for signing stored procedures with a certificate.](https://learn.microsoft.com/en-us/sql/relational-databases/tutorial-signing-stored-procedures-with-a-certificate?view=sql-server-ver16) | No  
[cursor threshold](https://docs.microsoft.com/sql/database-engine/configure-windows/configure-the-cursor-threshold-server-configuration-option?view=sql-server-ver15) | `integer`  
`-1` ... `2147483647` | No  
[default full-text language](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-default-full-text-language-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `2147483647` | No  
[ default language](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-default-language-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32` | No  
[default trace enabled](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/default-trace-enabled-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[disallow results from triggers](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/disallow-results-from-triggers-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[external scripts enabled](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/external-scripts-enabled-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | Yes  
[ft crawl bandwidth (max)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ft-crawl-bandwidth-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[ft crawl bandwidth (min)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ft-crawl-bandwidth-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[ft notify bandwidth (max)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ft-notify-bandwidth-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[ft notify bandwidth (min)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ft-notify-bandwidth-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[fill factor (%)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-fill-factor-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `100` | Yes  
[index create memory (kb)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-index-create-memory-server-configuration-option?view=sql-server-ver15) | `integer`  
`704` ... `2147483647` | No  
[locks](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-locks-server-configuration-option?view=sql-server-ver15) | `integer`  
`5000` ... `2147483647` | Yes  
[max degree of parallelism (MAXDOP)](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver16) | `integer`  
`0` ... `32767` | No  
[max server memory (mb)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver15) | `integer`  
`1000` ... `2147483647`   
Cloud SQL may set a value for this flag on instances, based on [ Microsoft's recommended values](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver15#recommendations). For more information, see Special flags.  | No  
[max text repl size (b)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-text-repl-size-server-configuration-option?view=sql-server-ver15) | `integer`  
`-1` ... `2147483647` | No  
[max worker threads](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-worker-threads-server-configuration-option?view=sql-server-ver15) | `integer`  
`128` ... `65535` | No  
[nested triggers](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-nested-triggers-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[optimize for ad hoc workloads](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/optimize-for-ad-hoc-workloads-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[ph timeout (s)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/ph-timeout-server-configuration-option?view=sql-server-ver15) | `integer`  
`1` ... `3600` | No  
[cloud sql enable polybase](https://docs.cloud.google.com/sql/docs/sqlserver/enable-and-disable-polybase) | `boolean`  
`on` | `off` | Yes  
[cloud sql enable sp_help_revlogin](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) | `boolean`  
`on` | `off` | No  
[query governor cost limit](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-query-governor-cost-limit-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `2147483647` | No  
[query wait (s)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-query-wait-server-configuration-option?view=sql-server-ver15) | `integer`  
`-1` ... `2147483647` | No  
[recovery interval (min)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-recovery-interval-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
[remote access](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-access-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | Yes  
[remote login timeout (s)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-login-timeout-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `2147483647` | No  
[remote query timeout (s)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-query-timeout-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `2147483647` | No  
[transform noise words](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/transform-noise-words-server-configuration-option?view=sql-server-ver15) | `boolean`  
`on` | `off` | No  
[two digit year cutoff](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-two-digit-year-cutoff-server-configuration-option?view=sql-server-ver15) | `integer`  
`1753` ... `9999` | No  
[user connections](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-user-connections-server-configuration-option?view=sql-server-ver15) | `integer`  
`0`, `10` ... `32767` | Yes  
[user options](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-user-options-server-configuration-option?view=sql-server-ver15) | `integer`  
`0` ... `32767` | No  
  
## Special flags

This section contains additional information about Cloud SQL for SQL Server flags.

### `max degree of parallelism (MAXDOP)`

`Max degree of parallelism (MAXDOP)` is a Microsoft database flag available for use in Cloud SQL for SQL Server. This flag lets you limit the maximum number of threads used when running a single query in a parallel plan.

If left to the default value of `0`, then the database instance uses all available processors. However, this might not always be efficient or even practical if managing instances with hundreds of databases.

We recommend following Microsoft documentation recommendations when setting the flag's value, which can vary based on the number of numa nodes and the [number of available logical processors](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver16). 

You can check the numa node configuration using the [dynamic management view (DMV)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/system-dynamic-management-views?view=sql-server-ver17) from [sys.dm_os_sys_info](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-sys-info-transact-sql?view=sql-server-ver17). To check the numa node configuration, use a code snippet similar to the following:
    
    
          SELECT socket_count,cores_per_socket,numa_node_count   
    
          FROM sys.dm_os_sys_info
        

While you can use MAXDOP to limit the maximum number of processors you want to allow for parallel plan execution, you can also use the [cost threshold for parallelism](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-cost-threshold-for-parallelism-server-configuration-option?view=sql-server-ver17) feature to indicate the minimum cost you want to set for a single processor before expanding parallel operations to another processor. These features let you better control the efficiency and cost of parallel plan execution.

Recommended values for these features vary on a case-by-case basis, and will be influenced by your server and application workload needs.

For help determining the best MAXDOP and cost threshold for parallelism values for your servers, see the following resources:

  * [Server configuration: max degree of parallelism](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-degree-of-parallelism-server-configuration-option?view=sql-server-ver16)
  * [Best practices: Database settings to modify](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#sqlserver_settings_modify)



Changing the default value helps address the following potential issues: 

  * If the `max degree of parallelism (MAXDOP)` flag is set to `0`, then instances or client applications that require SharePoint downloads fail. The SharePoint download runs a pre-check that requires a numeric value for the flag and won't accept a value less than 1.
  * Leaving the MAXDOP flag to the default of `0`, effectively indicates that there is no limit and that all available processors can be used for parallel operations. While this value might be fine for servers routinely running small queries, it might pose a cost issue if you also need to periodically run very large queries.



Using the `max degree of parallelism (MAXDOP)` flag, you can control the number of threads at three levels:

  * Instance level, using database flags
  * Database scope, using TSQL
  * Query level, using query hints



Note that if the instance is resized, then the flag value remains unchanged.

### `max server memory (mb)`

The `max server memory (mb)` flag limits the amount of memory that Cloud SQL can allocate for its internal pools.

We recommend you not configure a value for this flag and that you let Cloud SQL manage the value for you. If you must manually manage this value, as a general recommendation, set the `max server memory (mb)` value to roughly 80% of available memory to help prevent SQL Server from consuming all memory.

Conversely, for instances with large amounts of memory, 80% of available memory might be too low of a value and might lead to wasted memory usage.

If you don't set a value for this flag, then Cloud SQL manages the value automatically, based on the size of the RAM for your instance. Also, if you resize your instance, then Cloud SQL adjusts the value of the flag automatically to meet our recommendations for the new instance size. This resize operation also removes any manually set value for this flag. This helps your database utilize resources more effectively by helping prevent overallocation, reducing the likelihood of a crash due to out-of-memory issues, and helping to avoid performance degradation for your instance.

For more information, see [Maximum server memory](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#sqlserver-settings-global) and [Optimize high memory usage](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage#memory-optimization-options).

### `cloud sql enable sp_help_revlogin`

The `cloud sql enable sp_help_revlogin` flag lets you enable or disable the `sp_help_revlogin` stored procedure in the `msdb` database.

When this flag is set to `on`, Cloud SQL installs the stored procedure in the `msdb` database and grants execution permissions to the `sqlserver` administrative user. This lets you export SQL Server logins, password hashes, and SIDs to help with login migration and synchronization between instances.

When this flag is set to `off`, Cloud SQL removes the stored procedure from the `msdb` database.

For more information, see [Export SQL Server logins](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins).

## Troubleshooting

Issue | Troubleshooting | You want to modify the time zone for a Cloud SQL instance. |  To see how to update an instance's time zone, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone). In Cloud SQL for SQL Server, you can use the `AT TIME ZONE` function for time conversions and more. For more information about this function, see [ AT TIME ZONE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/at-time-zone-transact-sql?view=sql-server-ver15).  
---|---  
  
## What's next

  * Learn more about [SQL Server configuration options](https://docs.microsoft.com/sql/database-engine/configure-windows/server-configuration-options-sql-server?view=sql-server-ver15).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
