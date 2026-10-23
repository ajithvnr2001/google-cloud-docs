---
url: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/configure-pitr/
title: Configure point-in-time recovery (PITR) \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:44.456136+00:00
---

# Configure point-in-time recovery (PITR)  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/configure-pitr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure point-in-time recovery (PITR) Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/configure-pitr "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr "View this page for the SQL Server database engine")

**Note:**

To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations.

[Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#tips-pitr) lets you restore a Cloud SQL instance to a specific point in time. This helps you recover lost data and revert unintended changes or corruption.

PITR requires [automated backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#automated-backups). You can configure PITR on an existing instance by enabling or disabling the feature, adjusting transaction log retention, and switching transaction log storage to Cloud Storage.

## Before you begin

Before you begin, review the following:

  * If you enable PITR on an existing instance, then the instance restarts.
  * PITR is enabled by default when you create a [Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) instance in the Google Cloud console. If you are using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API and you want to enable the feature, then you must do so manually.
  * PITR is enabled by default when you create a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) instance, regardless of the method used. If you want to [disable the feature](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/configure-pitr#disabling-pitr), then you must do so manually.
  * [Automated backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#automated-backups) are enabled by default when you create an instance in the Google Cloud console. If you are using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API and you want to enable the feature, then you must do so manually.



## Enable PITR

The following procedure enables PITR on an _existing_ primary instance.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the instance you want to enable PITR on and click **Edit**.
  3. Under **Customize your instance** , expand the **Data Protection** section.
  4. Select the **Enable point-in-time recovery** checkbox.
  5. In the **Days of logs** field, enter the number of days to retain logs, from 1-35 for Cloud SQL Enterprise Plus edition, or 1-7 for Cloud SQL Enterprise edition.
  6. Click **Save**.



### gcloud

  1. Display the instance overview: 
         
         gcloud sql instances describe INSTANCE_NAME

  2. If you see `enabled: false` in the `backupConfiguration` section, enable scheduled backups: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --backup-start-time=HH:MM

Specify the `backup-start-time` parameter using 24-hour time in UTC±00 time zone.

  3. Enable PITR: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --enable-point-in-time-recovery

If you're enabling PITR on a primary instance, you can also configure the number of days for which you want to retain transaction logs by adding the following parameter:
         
         --retained-transaction-log-days=RETAINED_TRANSACTION_LOG_DAYS

  4. Confirm your change: 
         
         gcloud sql instances describe INSTANCE_NAME

In the `backupConfiguration` section, you see `pointInTimeRecoveryEnabled: true` if the change was successful.




### Terraform

To enable PITR, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "postgres_instance_pitr" {
      name             = ""
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        backup_configuration {
          enabled                        = true
          point_in_time_recovery_enabled = true
          start_time                     = "20:55"
          transaction_log_retention_days = "3"
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
    

## Disable PITR

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the instance you want to deactivate and select **Edit**.
  3. Under **Customize your instance** , expand the **Data Protection** section.
  4. Clear **Enable point-in-time recovery**.
  5. Click **Save**.



### gcloud

  1. Deactivate point-in-time recovery: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --no-enable-point-in-time-recovery

  2. Confirm your change: 
         
         gcloud sql instances describe INSTANCE_NAME

In the `backupConfiguration` section, you see `pointInTimeRecoveryEnabled: false` if the change was successful.




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
    

## Set transaction log retention

To set the number of days to retain write-ahead logs: 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Open the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) for the instance you want to set the transaction log on and select **Edit**.
  3. Under **Customize your instance** , expand the **Data Protection** section.
  4. In the **Enable point-in-time recovery** section, expand **Advanced options**.
  5. Enter the number of days to retain logs, from 1-35 for Cloud SQL Enterprise Plus edition or 1-7 for Cloud SQL Enterprise edition.
  6. Click **Save**.



### gcloud

Edit the instance to set the number of days to retain write-ahead logs.

Replace the following:

  * INSTANCE_NAME: The name of the instance you want to set the transaction log on.
  * DAYS_TO_RETAIN: The number of days of transaction logs to keep. For Cloud SQL Enterprise Plus edition, the valid range is between 1 and 35 days, with a default of 14 days. For Cloud SQL Enterprise edition, the valid range is between 1 and 7 days, with a default of 7 days.

If you don't specify a value, then Cloud SQL uses the default value. This is valid only when PITR is enabled. Keeping more days of transaction logs requires a bigger storage size.



    
    
      gcloud sql instances patch INSTANCE_NAME   
        --retained-transaction-log-days=DAYS_TO_RETAIN
      

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DAYS_TO_RETAIN: the number of days to retain transaction logs. For Cloud SQL Enterprise Plus edition, the valid range is between 1 and 35 days, with a default of 14 days. For Cloud SQL Enterprise edition, the valid range is between 1 and 7 days, with a default of 7 days.

If no value is specified, then the default value is used. This is valid only when PITR is enabled. Keeping more days of transaction logs requires a bigger storage size.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "transactionLogRetentionDays": "DAYS_TO_RETAIN"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID.
  * DAYS_TO_RETAIN: the number of days to retain transaction logs. For Cloud SQL Enterprise Plus edition, the valid range is between 1 and 35 days, with a default of 14 days. For Cloud SQL Enterprise edition, the valid range is between 1 and 7 days, with a default of 7 days.

If no value is specified, then the default value is used. This is valid only when PITR is enabled. Keeping more days of transaction logs requires a bigger storage size.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":
      {
        "backupConfiguration":
        {
          "transactionLogRetentionDays": "DAYS_TO_RETAIN"
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

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Check the storage location of transaction logs used for PITR

You can check where your Cloud SQL instance is storing the transaction logs used for PITR.

### gcloud

To determine whether your instance stores logs for PITR on disk or Cloud Storage, use the following command:
    
    
       gcloud sql instances describe INSTANCE_NAME
       

Replace INSTANCE_NAME with the name of the instance.

For multiple instances in the same project, you can also check the storage location of the transaction logs. To determine the location for multiple instances, use the following command:
    
    
       gcloud sql instances list --show-transactional-log-storage-state
       

Example response:
    
    
    NAME  DATABASE_VERSION LOCATION         TRANSACTIONAL_LOG_STORAGE_STATE
    my_01 POSTGRES_12      us-central-1     DISK
    my_02 POSTGRES_12      us-central-1     CLOUD_STORAGE
    ...
       

In the output of the command, the `transactionalLogStorageState` field or the `TRANSACTIONAL_LOG_STORAGE_STATE` column provides information about where the transaction logs for PITR are stored for the instance. The possible transaction log storage states are the following:

  * `DISK`: the instance stores the transaction logs used for PITR on disk. If you upgrade a Cloud SQL Enterprise edition instance to Cloud SQL Enterprise Plus edition, then the upgrade process switches the log storage location to Cloud Storage automatically. For more information, see [Upgrade an instance to Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place). You can also choose to switch the storage location by using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Cloud SQL Admin API without upgrading the edition of your instance and without incurring any downtime. For more information, see Switch transaction log storage to Cloud Storage. 
  * `SWITCHING_TO_CLOUD_STORAGE`: the instance is switching the storage location for the PITR transaction logs to Cloud Storage.
  * `SWITCHED_TO_CLOUD_STORAGE`: the instance has completed the switching the storage location for PITR transaction logs from disk to Cloud Storage.
  * `CLOUD_STORAGE`: the instance stores the transaction logs used for PITR in Cloud Storage.



## Switch transaction log storage to Cloud Storage

If your instance stores its transaction logs used for PITR on disk, then you can switch the storage location to Cloud Storage without incurring any downtime. The overall process of switching the storage location takes approximately the duration of the transaction log retention period (days) to complete. As soon as you start the switch, transaction logs start accruing in Cloud Storage. During the operation, you can check the status of the overall process by using the command in Check the storage location of transaction logs used for PITR.

After the overall process of switching to Cloud Storage is complete, Cloud SQL uses transaction logs from Cloud Storage for PITR.

### gcloud

To switch the storage location to Cloud Storage, use the following command:
    
    
       gcloud sql instances patch INSTANCE_NAME \
          --switch-transaction-logs-to-cloud-storage
       

Replace INSTANCE_NAME with the name of the instance. The instance must be a primary instance and not a replica instance. The response is similar to the following:
    
    
    The following message is used for the patch API method.
    {"name": "INSTANCE_NAME", "project": "PROJECT_NAME", "switchTransactionalLogsToCloudStorageEnabled": "true"}
    
    Patching Cloud SQL instance...done.
    Updated
    [https://sqladmin.prod.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME].
       

If the command returns an error, then see Troubleshoot the switch to Cloud Storage for possible next steps.

### REST v1

**Important** : You can't make additional updates to the instance in the same request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID. The instance must be a primary instance and not a replica instance.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
       "switchTransactionLogsToCloudStorageEnabled": true
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If the request returns an error, then see Troubleshoot the switch to Cloud Storage for possible next steps.

### REST v1beta4

**Important** : You can't make additional updates to the instance in the same request.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * INSTANCE_ID: the instance ID. The instance must be a primary instance and not a replica instance.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
       "switchTransactionLogsToCloudStorageEnabled": true
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

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If the request returns an error, then see Troubleshoot the switch to Cloud Storage for possible next steps.

### Troubleshoot the switch to Cloud Storage

The following table lists possible errors that might return with the `INVALID REQUEST` code when you switch the storage location of the transaction logs from disk to Cloud Storage.

Issue | Troubleshooting |  `Switching the storage location of the transaction logs used for PITR is not supported for instances with database type %s.` | Make sure that you're running the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) command or making the API request on a Cloud SQL for MySQL or Cloud SQL for PostgreSQL instance. Switching the storage location for transaction logs by using gcloud CLI or the Cloud SQL Admin API is not supported for Cloud SQL for SQL Server.   
---|---  
`PostgreSQL transactional logging is not enabled on this instance.` |  PostgreSQL uses write-ahead logging as the transaction logs for point-in-time recovery (PITR). To support PITR, PostgreSQL requires that you enable write-ahead logging on the instance. For more information about how to enable write-ahead logging, see [Enable PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#enablingpitr).   
`This instance is already storing transaction logs used for PITR in Cloud Storage` |  To verify the storage location of the transaction logs, run the command in [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).   
`The instance is already switching transaction logs used for PITR from disk to Cloud Storage.` |  Wait for the switch operation to complete. To verify the status of the operation and the storage location of the transaction logs, run the command in [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).  
  
## What's next

  * [Configure flags](https://docs.cloud.google.com/sql/docs/postgres/flags) on your clone



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
