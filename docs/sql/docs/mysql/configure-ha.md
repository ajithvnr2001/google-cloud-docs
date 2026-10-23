---
url: https://docs.cloud.google.com/sql/docs/mysql/configure-ha/
title: Enable and disable high availability \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:19.766338+00:00
---

# Enable and disable high availability  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/configure-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Enable and disable high availability Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-ha "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha "View this page for the SQL Server database engine")

This page describes how to configure an instance for high availability.

You can configure an instance for high availability when you create the instance, or you can enable high availability on an existing instance.

For more information about high availability, see [Overview of the high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

The [legacy configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha) for high availability used a `failover replica` instance. The new configuration does not use a `failover replica`. Instead, it uses Google's [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks#repds), which synchronously replicate data at the block level between two zones in a region. If you have an existing MySQL instance that uses the legacy high availability configuration, you can [update your configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy) to use the current version. For other procedures related to the legacy high availability configuration, see [Legacy configuration for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha). **Important:** As of January 13, 2025, the legacy configuration for high availability (HA) is deprecated for all instances. You can't create instances with legacy high availability configuration, and you can't enable legacy high availability configuration on any existing instances. In addition, after January 13, 2025, legacy high availability instances are no longer covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).   
  
We recommend that you update your remaining legacy high availability instances to the current high availability configuration. You can do so by following the instructions in [Update an instance from legacy to current high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy). Starting on May 1, 2025, Cloud SQL will begin updating any instances that use the legacy high availability configuration to use the current regional persistent disk-based high availability configuration automatically. 

## Create a new instance configured for high availability

When you create an instance and configure it for high availability, Cloud SQL creates it as a regional instance.

To create an instance configured for high availability:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select **Create instance**.
  3. Select the database engine.
  4. In the **Choose region and zonal availability** section, select **Multiple zones (Highly available)**.
  5. Expand **Specify zones**.
  6. Select the primary and secondary zones. The following conditions apply when the secondary zone is used during instance creation or edit: 
     * The zones default to `Any` for the primary zone and `Any (different from primary)` for the secondary zone.

If both the primary and secondary zones are specified, they must be different zones.

  7. Click **Save**. 

You are returned to the instance page for the primary instance while the instance is updated.




### gcloud

  1. Create the regional instance: 
         
         gcloud sql instances create REGIONAL_INSTANCE_NAME \
         --availability-type=REGIONAL \
         --database-version=DATABASE_VERSION \
         --tier=MACHINE_TYPE \
         --enable-bin-log

For a complete list of available parameters, see the [gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) reference page. 
  2. You can specify both the primary and secondary zones, using the `--zone` and `--secondary-zone` parameters. The following restrictions apply when the secondary zone is used during instance creation or edit: 
     * The zones must be valid zones.
     * If the secondary zone is specified, the primary must also be specified.
     * If the primary and secondary zones are specified, they must be different zones.
     * If the primary and secondary zones are specified, they must belong to the same region.
  3. Configure the root user: 
         
         gcloud sql users set-password root --host=% \
         --instance=PRIMARY_INSTANCE_NAME \
         --password=PASSWORD




### Terraform

To create an instance with high availability, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "mysql_instance_ha" {
      name             = "mysql-instance-ha"
      region           = "asia-northeast1"
      database_version = "MYSQL_8_0"
      settings {
        tier              = "db-f1-micro"
        availability_type = "REGIONAL"
        backup_configuration {
          enabled            = true
          binary_log_enabled = true
          start_time         = "20:55"
        }
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

For the complete list of parameters for the request, see the [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) page. 

Create the regional instance.

  1. Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-name: The instance name
     * database-version: The database version enum string
     * region The GCP region
     * machine-type The machine type

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances

Request JSON body: 
    
    {
      "name": "instance-name",
      "region": "region",
      "databaseVersion": "database-version",
       "settings": {
         "tier": "machine-type",
         "backupConfiguration": {
             "binaryLogEnabled": true,
             "enabled": true
          },
          "availabilityType": "REGIONAL"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  2. When the instance finishes initializing, update the root password on the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * password: The new root user password

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=root&host=%25'

Request JSON body: 
    
    {
       "name": "root",
       "host": "%",
       "password": "password"}
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=root&host=%25'"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?name=root&host=%25'" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




### REST v1beta4

For the complete list of parameters for the request, see the [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) page. 

Create the regional instance.

  1. Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-name: The instance name
     * database-version: The database version enum string
     * region The GCP region
     * machine-type The machine type

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances

Request JSON body: 
    
    {
      "name": "instance-name",
      "region": "region",
      "databaseVersion": "database-version",
       "settings": {
         "tier": "machine-type",
         "backupConfiguration": {
             "binaryLogEnabled": true,
             "enabled": true
          },
          "availabilityType": "REGIONAL"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-name",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  2. When the instance finishes initializing, update the root password on the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * password: The new root user password

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=root&host=%25'

Request JSON body: 
    
    {
       "name": "root",
       "host": "%",
       "password": "password"}
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=root&host=%25'"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?name=root&host=%25'" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




For more details about creating an instance, see [Creating Instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

## Configure an existing instance for high availability

You can configure a Cloud SQL instance for high availability by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API.

**Note:** After you start the high availability configuration for an instance, you can't stop it. Reconfiguring the instance restarts it. It typically takes only a few minutes for Cloud SQL to reconfigure the instance and restart it. However, if the instance has a large disk or load, then it might take up to an hour.

### Console

**Important:** You can't use the Google Cloud console to configure instances that have [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) enabled for high availability. To configure these instances, use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API.

To configure an instance for high availability:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Choose region and zonal availability** section, select **Multiple zones (Highly available)**.
  5. Expand **Specify zones**.
  6. Select the primary and secondary zones. The following conditions apply when you use the secondary zone while you're creating or editing an instance: 
     * The zones default to `Any` for the primary zone and `Any (different from primary)` for the secondary zone.

If you specify both the primary and secondary zones, then they must be different zones.

  7. Click **Save**.



### gcloud

To configure an instance to be a regional, high availability instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --availability-type REGIONAL \
    --enable-bin-log \
    --backup-start-time=HH:MM

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance that you're configuring for high availability
  * HH:MM: the time (in hours and minutes)



### REST v1

To configure an instance to be a regional, high availability instance:

  1. Check the instance to see if automatic backups and binary logs are enabled. These are required for high availability instances.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

The output contains a section similar to the following:
    
    "backupConfiguration": {
        "kind": "sql#backupConfiguration",
        "startTime": "12:00",
        "enabled": true,
        "binaryLogEnabled": true
        }
      

  2. If either `enabled` or `binaryLogEnabled` are `false`, then use the `[instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch)` method to enable them both. To enable backups, set `enabled` to `true` and `startTime` to a value which is the start of the backup window. To enable binary logging, set `binaryLogEnabled` to `true`. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the primary or read replica instance that you're configuring for high availability
     * START_TIME: the time (in hours and minutes)

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "startTime": "START_TIME",
          "enabled": true,
          "binaryLogEnabled": true
        }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Configure the instance to be a regional, high availability instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings": {"availabilityType": "REGIONAL" }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




### REST v1beta4

To configure an instance to be a regional, high availability instance:

  1. Check the instance to see if automatic backups and binary logs are enabled. These are required for high availability instances.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

The output contains a section similar to the following:
    
    "backupConfiguration": {
        "kind": "sql#backupConfiguration",
        "startTime": "12:00",
        "enabled": true,
        "binaryLogEnabled": true
        }
      

  2. If either `enabled` or `binaryLogEnabled` are `false`, then use the `[instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch)` method to enable them both. To enable backups, set `enabled` to `true` and `startTime` to a value which is the start of the backup window. To enable binary logging, set `binaryLogEnabled` to `true`. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the primary or read replica instance that you're configuring for high availability
     * START_TIME: the time (in hours and minutes)

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "startTime": "START_TIME",
          "enabled": true,
          "binaryLogEnabled": true
        }
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Configure the instance to be a regional, high availability instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings": {"availabilityType": "REGIONAL" }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




## Initiate failover

Testing failover is optional, but is recommended so that you can see how your application responds in the event of a failover.

This feature helps you test your application's response to an automatic failover. Make sure that your instance has completed any previous failover (so it's responding to connection requests) before you trigger another failover. Also, before you initiate failover for your instance, [configure the instance for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing).

To learn more about failovers, see the [Failover overview](https://docs.cloud.google.com/sql/docs/mysql/high-availability#failover-overview).

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Failover**.
  4. In the **Manually trigger a failover** dialog box, enter the ID of your instance in the text field, and then click **Trigger Failover**.



### gcloud

Initiate the failover:
    
    
    gcloud sql instances failover PRIMARY_INSTANCE_NAME

### REST v1

  1. Describe the primary instance to get the value of the `settingsVersion` field. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

  2. Initiate the failover: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-name: The instance name
     * settings-version: The settingsVersion from instanceInfo

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-name/failover

Request JSON body: 
    
    {
      "failoverContext":
         {
            "settingsVersion":"settings-version"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-name/failover"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-name/failover" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




### REST v1beta4

  1. Describe the primary instance to get the value of the `settingsVersion` field. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance that you're configuring for high availability

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

  2. Initiate the failover: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-name: The instance name
     * settings-version: The settingsVersion from instanceInfo

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-name/failover

Request JSON body: 
    
    {
      "failoverContext":
         {
            "settingsVersion":"settings-version"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-name/failover"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-name/failover" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-name",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-name",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




The instance fails over and it isn't available to serve data for a few minutes.

## Verify an instance's high availability configuration

To verify an instance has high availability and to view the zones in which it is running:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Confirm the following high availability settings are displayed in the **Configuration** section:
     * **Highly available (regional)**
     * **Located in** shows the current primary zone of the instance.

The new high availability does not use the [legacy](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha) failover replica. You will not see a failover replica in the instances list unless you are using the legacy configuration.

### gcloud
    
    
    gcloud sql instances describe INSTANCE_NAME

The output indicates `availabilityType` is `REGIONAL`. The `gceZone` and `secondaryGceZone` fields show the current primary and secondary zones of the instance. 

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance that you're configuring for high availability



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

The output indicates `availabilityType` is `REGIONAL`. The `gceZone` and `secondaryGceZone` fields show the current primary and secondary zones of the instance. 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance that you're configuring for high availability



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0"
    }
    

The output indicates `availabilityType` is `REGIONAL`. The `gceZone` and `secondaryGceZone` fields show the current primary and secondary zones of the instance. 

## Change the zones of a high availability instance

Changing one or both zones of an existing high availability instance causes a few minutes of downtime while the instance is reconfigured. To see the current primary and secondary zones that the high availability instance is running in, see [Verify an instance's high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#verify-ha).

**Note:** Once you start the zone change operation on an instance, you cannot stop it. This operation restarts the instance. It typically takes only a few minutes for the configuration and restart to complete. But if the instance has a large disk or load, it might take up to an hour. 

To change the zones of a high availability instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Choose region and zonal availability** section, expand **Specify zones** and select new zones. The zones default to `Any` for the primary zone and `Any (different from primary)` for the secondary zone. The following restrictions apply: 
     * You can specify the primary zone only, or both the primary and secondary zones.
     * If both the primary and secondary zones are specified, they must be different zones.
  5. Click **Save**. 

You are returned to the instance page for the primary instance while the instance is updated.




### gcloud

Change the zone in which the instance is running:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --zone=PRIMARY_ZONE --secondary-zone=SECONDARY_ZONE

The `--secondary-zone` parameter is optional. If you omit it, Cloud SQL will select an available zone that is different from the primary zone. 

The following restrictions apply: 

  * The zones must be valid zones belonging to the same region as the Cloud SQL instance.
  * If the secondary zone is specified, it must be different from the primary zone.



### REST v1

  1. Change the zones of the regional instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * INSTANCE_NAME: The instance name
     * PRIMARY_ZONE: The primary zone
     * SECONDARY_ZONE: The secondary zone

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
    "settings": {"locationPreference": {"zone": "PRIMARY_ZONE", "secondaryZone": "SECONDARY_ZONE"}}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

The `secondaryZone` parameter is optional. If you omit it, Cloud SQL will select an available zone that is different from the primary zone. 

The following restrictions apply: 

     * The zones must be valid zones.
     * Any zones that you choose must belong to the same region as the Cloud SQL instance.



### REST v1beta4

  1. Change the zones of the regional instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * INSTANCE_NAME: The instance name
     * PRIMARY_ZONE: The primary zone
     * SECONDARY_ZONE: The secondary zone

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
    "settings": {"locationPreference": {"zone": "PRIMARY_ZONE", "secondaryZone": "SECONDARY_ZONE"}}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

The `secondaryZone` parameter is optional. If you omit it, Cloud SQL will select an available zone that is different from the primary zone. 

The following restrictions apply: 

     * The zones must be valid zones.
     * Any zones that you choose must belong to the same region as the Cloud SQL instance.



## Deactivate high availability for an instance

You can deactivate high availability for a Cloud SQL instance by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or the API.

**Note:** Before you perform this procedure, make sure that no operations are running on the instance.

If you deactivate high availability for an instance, then in the event of a zonal outage, you need to recover the instance manually. For more information, see [Recovery options for standalone instances](https://docs.cloud.google.com/sql/docs/mysql/high-availability#recovery-options).

### Console

**Important:** You can't use the Google Cloud console to deactivate high availability for instances that have [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) enabled. To deactivate these instances, use [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API.

To deactivate high availability for an instance:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. Open **Auto backups**.
  5. In the **Availability** section, click **Single zone**.
  6. Click **Save**. This edit requires you to restart the instance.
  7. When the dialog appears, click **Save and restart**.



### gcloud

To deactivate high availability for an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --availability-type ZONAL

Replace INSTANCE_NAME with the name of the Cloud SQL instance for which you're deactivating high availability.

### REST v1

To change the availability type of the instance to `ZONAL`, use the `[instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch)` method. This method deactivates high availability for the instance.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance for which you're deactivating high availability



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings": {"availabilityType": "ZONAL" }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### REST v1beta4

To change the availability type of the instance to `ZONAL`, use the `[instances:patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch)` method. This method deactivates high availability for the instance.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance for which you're deactivating high availability



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings": {"availabilityType": "ZONAL" }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Troubleshoot

Issue | Troubleshooting | You can't find the metrics for a manual failover. | Only automatic failovers go into the metrics.  
---|---  
Cloud SQL instance resources (CPU and RAM) are near 100% usage, causing the high availability instance to go down. | The instance machine size is too small for the load. [ Edit the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#editing_an_instance) to upgrade to a larger machine size to get more CPUs and memory.   
  
## What's next

  * Learn more about [how the high availability configuration works](https://docs.cloud.google.com/sql/docs/mysql/high-availability).
  * Test how your application responds to lost connections by [restarting your instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance).
  * Learn more about [managing your database connections](https://docs.cloud.google.com/sql/faq#connections).
  * Learn more about [Google Cloud Observability](https://docs.cloud.google.com/monitoring/docs). 
  * Learn more about the [Legacy configuration for high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha). 
  * [Create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication) for your instance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
