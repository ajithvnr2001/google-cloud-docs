---
url: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-standard-backups/
title: Manage standard backups \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:27.308993+00:00
---

# Manage standard backups  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-standard-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Manage standard backups Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-standard-backups "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-standard-backups "View this page for the SQL Server database engine")

**Warning:** All data on an instance, including backups, is permanently lost when that instance is deleted. To preserve your data, you can either take a [final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) of your instance at time of deletion, enable [retained backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retained-backups) for your instance before you delete it, or [export your data to Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/import-export) before you delete it.

Cloud SQL [standard backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options#standard-backups) let you schedule automated backups, create on-demand backups, and view existing backups for your database instance. Regular backups help you protect your data against accidental loss or corruption and support disaster recovery. If your instance uses enhanced backups, then see [Manage enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups).

Instances created before the [availability of the enhanced backups option](https://docs.cloud.google.com/sql/docs/postgres/release-notes#July_31_2025) use standard backups by default. To upgrade your instance to use enhanced backups, see [Enable enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups#enable). For more information about how backups work and the available backup options, see [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups) and [Choose your backup option](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options).

## Create an on-demand backup

To create an on-demand backup:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. Click **Create backup**.
  5. On the **Create backup** page, add a description, if needed, and click **Create**. 



### gcloud

Create the backup:
    
    
    gcloud sql backups create \
    --async \
    --instance=INSTANCE_NAME

You can provide a description of the backup using the `--description` parameter. 

To create a backup in a custom location:
    
    
    gcloud sql backups create \
    --async \
    --instance=INSTANCE_NAME \
    --location=BACKUP_LOCATION

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "BACKUP_VOLUME",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "BACKUP_VOLUME",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Configure automated backups

Automated backups are taken on a schedule cadence while your instance is running. You can also set the retention period for your automated backups. For more information about how automated backups work, see [Automated backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#automated-backups).

### Schedule automated backups

To schedule automated backups for an instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. Click **Edit** , next to **Settings**.
  5. Choose a window of time for your data to be automatically backed up.
  6. Click **Save**.



### gcloud

  1. Edit the instance to specify a backup start time: 
         
         gcloud sql instances patch INSTANCE_NAME --backup-start-time=HH:MM

The `backup-start-time` parameter is specified in a 24-hour time format, in the UTC±00 time zone, and specifies the start of a 4-hour backup window. Backups can start any time during the backup window. 
  2. Confirm your changes: 
         
         gcloud sql instances describe INSTANCE_NAME

In the `backupConfiguration` section, confirm that you see `enabled: true` and the time that you specified. 



### Terraform

To create a backup for a database, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "instance" {
      name             = "postgres-instance-backup"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        backup_configuration {
          enabled    = true
          start_time = "20:55"
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
    

### REST v1beta4

You can enable pointInTimeRecovery at the same time by setting `pointInTimeRecoveryEnabled` to `true` within the `backupConfiguration` object. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the primary or read replica instance that you're configuring for high availability
  * START_TIME: the time (in hours and minutes)



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "startTime": "START_TIME",
          "enabled": true,
          "pointInTimeRecoveryEnabled": true
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

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Note:** If an on-demand backup is ongoing when an automatic backup is scheduled to begin, the automatic backup is rescheduled for a later time.

### Set automated backup retention

To set the number of automated backups to retain:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. Click **Edit**.
  5. In the **Automate backups** section, expand **Advanced options**.
  6. Enter the **Number of backups** to store at a time. 
  7. Click **Save**.



### gcloud

Edit the instance to set the number of automated backups to retain. The number can't be less than the default (seven). 
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --retained-backups-count=NUM_TO_RETAIN

### Terraform

To specify the number of automated backups to retain for a database instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "default" {
      name             = "postgres-instance-backup-retention"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        backup_configuration {
          enabled = true
          backup_retention_settings {
            retained_backups = 365
            retention_unit   = "COUNT"
          }
        }
      }
    }

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * unit: Optional: The retention unit can either be an integer or a string. The currently supported (and default) values are 1 or "COUNT".
  * num-to-retain: The number of automated backups to retain, from 1 to 365.
  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "backupRetentionSettings":
          {
            "retentionUnit": unit,
            "retainedBackups": "num-to-retain"
          }
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
    

### Disable automated backups

To disable automated backups for an instance:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. Click **Manage automated backups**
  5. Clear **Automate backups**.
  6. Click **Save**.



### gcloud

Edit the instance to disable backups:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --no-backup

### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "enabled": false
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

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "enabled": false,
          "pointInTimeRecoveryEnabled": false
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
    

## Delete a backup

You can delete automated and on-demand backups.

Deleting a backup might not free up as much space as the size of the backup. This is because backups are incremental, so deleting an older backup might transfer some of its contents to a more recent backup to preserve the integrity of the newer backup. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. Click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the backup you want to delete. 
  5. Select **Delete**.
  6. In the Delete backup window, type `Delete` into the field and click **Delete**. 



### gcloud

Delete a backup of a Cloud SQL instance:
    
    
    gcloud beta sql backups delete BACKUP_ID \
    --instance INSTANCE_NAME
          

For a complete list of parameters, see the [gcloud beta sql backups delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/backups/delete) command reference page. 

### REST v1

  1. List the backups to obtain the ID for the backup you want to delete: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "backup-id",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id",
          "location": "us"
        }
    
    

  2. Delete the backup: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * backup-id: The backup ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




### REST v1beta4

  1. List the backups to obtain the ID for the backup you want to delete: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "backup-id",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id",
          "location": "us"
        }
    
    

  2. Delete the backup: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * backup-id: The backup ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




## Set a custom location for backups

Only use a custom backup location if required by regulation. If not required, use the default multi-region backup location.

You can use a custom location for on-demand and automatic backups. For a complete list of valid location values, see the [Instance locations](https://docs.cloud.google.com/sql/docs/postgres/instance-locations).

**Note:** If you change the location where backups are stored, existing backups remain in their original location.

**Note:** Backups fail if they are in a region the organization policy does not allow. Backups taken in the same region as the instance always succeed, regardless of the organization policy or other constraints. 

To update an instance with a custom location:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. From the SQL navigation menu, select **Backups**.
  4. Next to **Settings** , click **Edit**.
  5. In the **Automated Backups** section, expand **Advanced Options**.
  6. Click **Multi-region (default)** or **Region**.
  7. Select the location from the **Location** drop-down menu. 
  8. Click **Save**.



### gcloud

For reference information, see [gcloud sql instances patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch). 
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --backup-location=BACKUP_LOCATION
      

### Terraform

To specify a custom location for a database instance backup, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "default" {
      name             = "postgres-instance-with-backup-location"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        backup_configuration {
          enabled  = true
          location = "us-central1"
        }
      }
    }

### REST v1

Use the instance's [ `settings.backupConfiguration.location`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances) parameter for the backup location. 

Before using any of the request data, make the following replacements: 

  * region: The project region
  * backup-region: The backup region
  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "region": "region"
      "settings":
      {
        "backupConfiguration":
        {
          "location": "backup-region",
          "enabled": true,
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

Use the instance's [ `settings.backupConfiguration.location`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances) parameter for the backup location. 

Before using any of the request data, make the following replacements: 

  * region: The project region
  * backup-region: The backup region
  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "region": "region"
      "settings":
      {
        "backupConfiguration":
        {
          "location": "backup-region",
          "enabled": true,
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
    

## View a list of backups

To view a list of backups and details about a backup, use the following options. 

The Google Cloud console does not show skipped or failed backups in the backup history. To see skipped backups, use `gcloud` or the API. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu to view recent backups, along with creation time and type of backup. 



### gcloud

  * List the backups of the instance: 
        
        gcloud sql backups list \
        --instance INSTANCE_NAME

You can filter and control the results using the standard list parameters. For a complete list, see the [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command reference page. 

  * View the details of a backup by specifying the backup `ID` from the output of the `backups list` command. 
        
        gcloud sql backups describe BACKUP_ID \
        --instance INSTANCE_NAME
            




### REST v1

You can also use the [ APIs Explorer on the BackupRuns:list page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/backupRuns/list) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "backup-id",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id",
          "location": "us"
        }
    
    

### REST v1beta4

You can also use the [ APIs Explorer on the BackupRuns:list page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/backupRuns/list) to send the REST API request. 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "backup-id",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id",
          "location": "us"
        }
    
    

## View a list of backups during an outage

When an instance is in a region that is having an outage, you can only view backups for that instance using a wildcard (`-`) with the `backupRuns.list` API. The wildcard returns all backups in the project. See [Restoring to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance).

When there's an outage in a region where an instance has customer-managed encryption keys (CMEK) enabled, you can't restore the backups for that instance to a different region. The reason is because Cloud SQL uses [regional Cloud KMS keys](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#key) for encryption when CMEK is enabled on the instance. To restore backups for a CMEK instance, Cloud SQL must have access to the CMEK key. In a regional outage, there's no access to the Cloud KMS keys in that region.

### gcloud

  1. List the backups for every instance in a project: 
         
         gcloud sql backups list --instance -

The command returns information similar to the following:
         
         {
               "kind": "sql#backupRun",
               "status": "SUCCESSFUL",
               "enqueuedTime": "2020-01-21T11:25:33.818Z",
               "id": "backup-id",
               "startTime": "2020-01-21T11:25:33.858Z",
               "endTime": "2020-01-21T11:26:18.663Z",
               "type": "AUTOMATED",
               "windowStartTime": "2020-01-21T10:00:00.479Z",
               "instance": "instance-id",
               "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns/backup-id",
               "location": "us"
               "backupKind": "SNAPSHOT"
             }

  2. Find the backup for the instance you need. To restore this backup, see [Restoring to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance). 



### REST v1

  1. List all the backups in a project: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID, or `-` for a list of all backups in the project

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/-/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/-/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/-/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "BACKUP_ID",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_ID",
          "location": "us"
          "backupKind": "SNAPSHOT"
        }
    
    

  2. Find the backup for the instance you need. To restore this backup, see [Restoring to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance). 



### REST v1beta4

  1. List all the backups in a project: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID, or `-` for a list of all backups in the project

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/-/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/-/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/-/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "kind": "sql#backupRun",
          "status": "SUCCESSFUL",
          "enqueuedTime": "2020-01-21T11:25:33.818Z",
          "id": "backup-id",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "windowStartTime": "2020-01-21T10:00:00.479Z",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/instance-id/backupRuns/backup-id",
          "location": "us"
          "backupKind": "SNAPSHOT"
        }
    
    

  2. Find the backup for the instance you need. To restore this backup, see [Restoring to a different instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups-another-instance). 



## View backup locations

To see the locations of the backups taken for an instance, use `backupRuns`:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Backups** from the SQL navigation menu.
  4. In the backups list, the **Location** column lists the type of location (multi-region or region) and the specific multi-region or region for each backup. 



### gcloud

For reference information, see [gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe). 

  1. List the backups of the instance: 
         
         gcloud sql backups list \
         --instance INSTANCE_NAME

You can filter and control the results using the standard list parameters. For a complete list, see the [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command reference page. 

  2. To list the details of one backup, use the `ID` from the output of the `backups list` command. 
         
         gcloud sql backups describe BACKUP_ID \
         --instance INSTANCE_NAME




### REST v1

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    
    

**In the previous examples:**

  * `REGION` is the region for the original instance. 
  * `BACKUP_LOCATION` is the location where you want Cloud SQL to store the backup. 



### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    
    

**In the previous examples:**

  * `REGION` is the region for the original instance. 
  * `BACKUP_LOCATION` is the location where you want Cloud SQL to store the backup. 



## View backup size

You can view the size of a backup for a Cloud SQL instance by using [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API.

### gcloud

  1. To get a list of all backups that are associated with a Google Cloud project, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command:
         
         gcloud sql backups list

**Note** : By using this command, you can retrieve information about the backups, including their IDs. You need a backup ID to view the size of a backup.

Also, you can filter and control the results of running this command by using standard list parameters. For a complete list, see the [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command reference page.

  2. To view the size of a backup, use the [`gcloud sql backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe) command:
         
         gcloud sql backups describe BACKUP_ID \
         --instance=INSTANCE_NAME \
         --project=PROJECT_ID

Make the following replacements:

     * BACKUP_ID: the ID of the backup. You obtain this ID from the output of running the `gcloud sql backups list` command.
     * INSTANCE_NAME: the name of the instance.
     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.

In the output, the `maxChargeableBytes` parameter displays the size of the backup (in bytes).




### REST

#### Get a list of backups

Use this example to get a list of all backups that are associated with a Google Cloud project. For a complete list of parameters for this call, see the [backupRuns.list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/list) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * INSTANCE_NAME: the name of the instance



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns",
          "kind": "sql#backupRun",
          "enqueuedTime": "2024-04-24T22:16:02.208Z",
          "id": "INSTANCE_ID",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/instances/INSTANCE_NAME/backupRuns",
          "location": "us",
          "description": "get a list of backups",
          "instance": "INSTANCE_NAME"
    }
    

#### View details about a backup

Use this example to view the details about a backup, including the backup size. For a complete list of parameters for this call, see the [backupRuns.get](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/get) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
  * INSTANCE_NAME: the name of the instance.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns/BACKUP_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns/BACKUP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns/BACKUP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/instances/INSTANCE_NAME/backupRuns/BACKUP_ID",
          "kind": "sql#backupRun",
          "enqueuedTime": "2024-04-24T22:16:02.208Z",
          "id": "INSTANCE_ID",
          "startTime": "2020-01-21T11:25:33.858Z",
          "endTime": "2020-01-21T11:26:18.663Z",
          "type": "AUTOMATED",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/instances/INSTANCE_NAME/backupRuns/BACKUP_ID",
          "location": "us",
          "description": "view details about a backup",
          "maxChargeableBytes": "BYTE_NUMBER",
          "instance": "INSTANCE_NAME"
    }
    

## Configure final backups

You can set your instance to automatically take a backup by enabling the [final backup instance setting](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#final-backup) and setting the [final backup retention period](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#final-backup-retention-days). If you don't enable final backup for your instance prior to deletion, you can also take a final backup when you [delete your instance](https://docs.cloud.google.com/sql/docs/postgres/delete-instance). For more information about how final backups work, see [Final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backup).

To manage a final backup after your instance is deleted, see [Manage backups for deleted instances](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-backups-deleted-instance).

### Enable final backup

To enable final backups for an instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to enable final backup for. To open the instance's **Overview** page, click the instance's name.

  3. Click **Edit**.

  4. Under **Customize your instance** , expand **Data Protection**.

  5. To enable final backup, check the box for **Final backup on instance deletion** under **Instance deletion protection**.

The default retention period is 30 days. To change this, enter a number between 1 to 365 in the **Days of retention** box.

  6. Click **Save**.

**Note:** This will cause your instance to restart.



###  gcloud 

Use the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command to enable final backup.
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --final-backup \
      --final-backup-retention-days=RETENTION_DAYS
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance.
  * `RETENTION_DAYS`: the number of days to retain the final backup. This can range from 1 to 365 days, and the default is 30 days.



###  REST v1 

To enable final backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * RETENTION_DAYS: the number of days to retain final backups



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "enabled": true,
          "retentionDays: RETENTION_DAYS
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
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta 

To enable final backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * RETENTION_DAYS: the number of days to retain final backups



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "enabled": true,
          "retentionDays: RETENTION_DAYS
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Set final backup retention

To set the final backup retention period for an instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to enable final backup for. To open the instance's **Overview** page, click the instance's name.

  3. Click **Edit**.

  4. Under **Customize your instance** , expand **Data Protection**.

  5. To change the final backup retention period, enter a number between 1 and 365 in the **Days of retention** box under the **Final backup after instance deletion** setting.

The default retention period is 30 days.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command to update the final backup retention days setting.
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --final-backup-retention-days=RETENTION_DAYS
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance.
  * `RETENTION_DAYS`: the number of days to retain the final backup. This can range from 1 to 365 days, and the default is 30 days.



###  REST v1 

To update the final backup retention days setting, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * RETENTION_DAYS: the number of days to retain final backups



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "retentionDays: RETENTION_DAYS
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
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta 

To update the final backup retention days setting, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * RETENTION_DAYS: the number of days to retain final backups



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "retentionDays: RETENTION_DAYS
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Disable final backup

To disable final backups for an instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to enable final backup for. To open the instance's **Overview** page, click the instance's name.

  3. Click **Edit**.

  4. Under **Customize your instance** , expand **Data Protection**.

  5. To disable final backup, uncheck the box for **Final backup on instance deletion** under **Instance deletion protection**.

  6. Click **Save**.

**Note:** This will cause your instance to restart.



###  gcloud 

Use the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command to disable final backup.
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --no-final-backup
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance.



###  REST v1 

To disable final backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "enabled": false
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
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta 

To disable final backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "FinalBackupConfig": {
          "enabled": false
        }
      }s
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Configure retained backups

You can set your instance to automatically retain all automated and on-demand backups when you delete your instance. These backups are retained based on the retention period of the backup at time of deletion. For more information about how final backups work, see [Final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backup).

To manage retained backups after your instance is deleted, see [Manage backups for deleted instances](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-backups-deleted-instance).

### Enable retained backups

To enable retained backups for an instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to enable retained backups for. To open the instance's **Overview** page, click the instance's name.

  3. Click **Edit**.

  4. Under **Customize your instance** , expand **Data Protection**.

  5. To enable retained backups, check the box for **Retain backups after instance deletion** under **Instance deletion protection**.

  6. Click **Save**.

**Note:** This will cause your instance to restart.



###  gcloud 

Use the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command to enable retained backups.
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --retain-backups-on-delete
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance.



###  REST v1 

To enable retained backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "retainBackupsOnDelete": true
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
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta 

To enable retained backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "retainBackupsOnDelete": true
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Disable retained backups

To disable retained backups for an instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the instance you want to enable retained backups for. To open the instance's **Overview** page, click the instance's name.

  3. Click **Edit**.

  4. Under **Customize your instance** , expand **Data Protection**.

  5. To disable retained backups, uncheck the box for **Retain backups after instance deletion** under **Instance deletion protection**.

  6. Click **Save**.

**Note:** This will cause your instance to restart.



###  gcloud 

Use the [`gcloud sql instances`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command to disable retained backups.
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --no-retain-backups-on-delete
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance.



###  REST v1 

To disable retained backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "retainBackupsOnDelete": false
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
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta 

To disable retained backups, do the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "retainBackupsOnDelete": true
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## What's next

  * [Learn more about backing up your data](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups). 
  * [Learn more about restoring data](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore). 
  * [See how to restore your data from a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring#restorebackups). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
