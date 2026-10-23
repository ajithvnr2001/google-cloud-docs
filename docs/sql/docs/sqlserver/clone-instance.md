---
url: https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance/
title: Clone instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:19.899386+00:00
---

# Clone instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Clone instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/clone-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/clone-instance "View this page for the PostgreSQL database engine") | SQL Server

This page explains cloning, and describes how to clone an instance.

## Overview

Cloning a Cloud SQL instance creates a new instance that is a copy of the source instance. The new instance is completely independent from the source instance.

**Note:** If there are many changes done recently on your instance, then cloning the instance might start a long-running operation.

## Standard clone

Standard clone creates a full backup of the source instance. The instance then uses that backup to provision a new, separate instance. The new instance is a functionally independent copy of the source at the time the operation began. The duration of a standard cloning operation is proportional to the database size.

## Frequently asked questions

Question | Answer | Does cloning impact performance? | No. Cloning has no performance impact on the source instance.  
---|---  
Are backups copied to the new instance? | No. The new instance creates new automated backups. Manual backups are not copied over from the source instance.  
Does the new instance have the same IP address or addresses? | No. The new instance has a new IP address or addresses.  
Does the new instance have the same configuration settings? | Yes. The new instance has the same settings such as database flags, connectivity options, machine type, and storage and memory settings.  
Are replicas copied to the new instance? | No. You need to create new replicas for the new instance.  
Can you clone a replica? | No. You can't clone a replica.  
Can you make a clone from an earlier point in time? | Yes. [ Point-in-time recovery](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#perform-pitr) uses cloning to restore an instance from an earlier point in time. This helps you recover your database from a destructive event.  
Are the [maintenance settings](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#management) of the source instance automatically copied to the clone instance? | No. You need to configure the maintenance settings for the clone instance.  
Can you clone an instance that was once a clone? | Yes. You can clone an instance that was cloned from another instance.  
Are database users copied to the new instance? | Yes, but database user passwords are not copied, and need to be recreated.  
  
## Clone an instance

You can clone a Cloud SQL instance by using the Google Cloud console, [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the API.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Find the row of the instance to clone.
  3. In the **Actions** column, click the more_vert **More Actions** menu. 
  4. Click **Create clone**.
  5. On the **Create a clone** page, update the instance ID if needed, and click **Create clone** , leaving **Clone current state of instance** selected. 

You are returned to the instance listing page while the clone initializes. 




### gcloud

To clone an instance, use the [`gcloud sql instances clone`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/clone) command:
    
    
    gcloud sql instances clone SOURCE_INSTANCE_NAME DESTINATION_INSTANCE_NAME \
    --project PROJECT_ID \
    --preferred-zone ZONE_NAME \
    --preferred-secondary-zone SECONDARY_ZONE_NAME

Make the following replacements:

  * SOURCE_INSTANCE_NAME: the name of the Cloud SQL instance to clone.
  * DESTINATION_INSTANCE_NAME: the name of the cloned instance.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the source and destination instances.
  * ZONE_NAME: Optional. The name of the primary zone for the destination instance. Use this if you want the destination instance to be in a different primary zone than the Cloud SQL instance that you're cloning. For a regional instance, this zone replaces the primary zone, but the secondary zone remains the same as the source instance.
  * SECONDARY_ZONE_NAME: Optional. The name of the secondary zone for the destination instance. Use this to specify a different secondary zone for the regional Cloud SQL instance that you want to clone.



If you're using the `--preferred-zone` and `--preferred-secondary-zone` parameters, then the following conditions apply:

  * Both the primary and secondary zones must be valid zones.
  * Both zones must belong to the same region as the source instance.
  * The primary and secondary zones must be different.
  * For zonal instances, you can't use the `--preferred-secondary-zone` parameter. If you do, then the process to clone the instance fails.
  * If you don't specify values for either the `--preferred-zone` or `--preferred-secondary-zone` parameters, then the cloned instance has the same primary and secondary zones as the source instance.



To run the `gcloud sql instances clone` command, you must have the `[cloudsql.instances.clone](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#permissions-roles)` permission. For more information about required permissions to run [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

**Note:** If you want to clone an instance that has [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled for it, then you don't need to specify the `enable-private-service-connect`, `allowed-psc-projects`, and `no-assign-ip` flags. The cloned instance inherits these flags from the source instance.

### Terraform

To clone the instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)
    
    
    resource "google_sql_database_instance" "clone" {
      name             = "sqlserver-instance-clone-name"
      region           = "us-central1"
      database_version = "SQLSERVER_2017_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      clone {
        source_instance_name = google_sql_database_instance.source.id
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

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the source and destination instances.
  * SOURCE_INSTANCE_NAME: the name of the Cloud SQL instance to clone.
  * DESTINATION_INSTANCE_NAME: the name of the cloned instance.
  * ZONE_NAME: Optional. The name of the primary zone for the destination instance. Use this if you want the destination instance to be in a different primary zone than the Cloud SQL instance that you're cloning. For a regional instance, this zone replaces the primary zone, but the secondary zone remains the same as the source instance.
  * SECONDARY_ZONE_NAME: Optional. The name of the secondary zone for the destination instance. Use this to specify a different secondary zone for the regional Cloud SQL instance that you want to clone.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "destinationInstanceName": "DESTINATION_INSTANCE_NAME",
        "preferredZone": "ZONE_NAME",
        "preferredSecondaryZone": "SECONDARY_ZONE_NAME"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "OPERATION_ID",
      "targetId": "DESTINATION_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If you're using the `preferredZone` and `preferredSecondaryZone` parameters, then the following conditions apply:

  * Both the primary and secondary zones must be valid zones.
  * Both zones must belong to the same region as the source instance.
  * The primary and secondary zones must be different.
  * For zonal instances, you can't use the `preferredSecondaryZone` parameter. If you do, then the process to clone the instance fails.
  * If you don't specify values for either the `preferredZone` or `preferredSecondaryZone` parameters, then the cloned instance has the same primary and secondary zones as the source instance.



To use the [`instances.clone`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/clone) API method, you must have the `[cloudsql.instances.clone](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#permissions-roles)` permission. For more information about required permissions to use API methods, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

**Note:** If you want to clone an instance that has [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled for it, then you don't need to specify the `allowedConsumerProjects` and `pscEnabled` flags. The cloned instance inherits these flags from the source instance.

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the source and destination instances.
  * SOURCE_INSTANCE_NAME: the name of the Cloud SQL instance to clone.
  * DESTINATION_INSTANCE_NAME: the name of the cloned instance.
  * ZONE_NAME: Optional. The name of the primary zone for the destination instance. Use this if you want the destination instance to be in a different primary zone than the Cloud SQL instance that you're cloning. For a regional instance, this zone replaces the primary zone, but the secondary zone remains the same as the source instance.
  * SECONDARY_ZONE_NAME: Optional. The name of the secondary zone for the destination instance. Use this to specify a different secondary zone for the regional Cloud SQL instance that you want to clone.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "destinationInstanceName": "DESTINATION_INSTANCE_NAME",
        "preferredZone": "ZONE_NAME",
        "preferredSecondaryZone": "SECONDARY_ZONE_NAME"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/SOURCE_INSTANCE_NAME/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "OPERATION_ID",
      "targetId": "DESTINATION_INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If you're using the `preferredZone` and `preferredSecondaryZone` parameters, then the following conditions apply:

  * Both the primary and secondary zones must be valid zones.
  * Both zones must belong to the same region as the source instance.
  * The primary and secondary zones must be different.
  * For zonal instances, you can't use the `preferredSecondaryZone` parameter. If you do, then the process to clone the instance fails.
  * If you don't specify values for either the `preferredZone` or `preferredSecondaryZone` parameters, then the cloned instance has the same primary and secondary zones as the source instance.



To use the [`instances.clone`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone) API method, you must have the `[cloudsql.instances.clone](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#permissions-roles)` permission. For more information about required permissions to use API methods, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

**Note:** If you want to clone an instance that has [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled for it, then you don't need to specify the `allowedConsumerProjects` and `pscEnabled` flags. The cloned instance inherits these flags from the source instance.

## Clone an instance that uses an internal IP address

If your Cloud SQL instance uses an internal IP address, you can optionally specify an [allocated IP range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing_allocated_ip_address_ranges) for the clone's new IP address. For example, `google-managed-services-default`.

### gcloud

Clone the instance, optionally specifying the allocated IP range you want to use:
    
    
    gcloud sql instances clone SOURCE_INSTANCE_NAME TARGET_INSTANCE_NAME \
    --allocated-ip-range-name ALLOCATED_IP_RANGE_NAME

The user or service account that's running the `gcloud sql instances clone` command must have the `cloudsql.instances.clone` permission. For more information about required permissions to run [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

### REST v1

Clone the instance, optionally specifying the allocated IP range you want to use:

Before using any of the request data, make the following replacements: 

  * project-id: the project ID
  * source-instance-id: the source instance ID
  * target-instance-id: the target instance ID
  * allocated-ip-range-name: the name of an allocated IP range



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "destinationInstanceName": "target-instance-id",
        "allocatedIpRange": "allocated-ip-range-name"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

The user or service account that's using the [`instances.clone`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone) API method must have the `cloudsql.instances.clone` permission. For more information about required permissions to use API methods, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

### REST v1beta4

Clone the instance, optionally specifying the allocated IP range you want to use:

Before using any of the request data, make the following replacements: 

  * project-id: the project ID
  * source-instance-id: the source instance ID
  * target-instance-id: the target instance ID
  * allocated-ip-range-name: the name of an allocated IP range



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone

Request JSON body: 
    
    
    {
      "cloneContext":
      {
        "destinationInstanceName": "target-instance-id",
        "allocatedIpRange": "allocated-ip-range-name"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/source-instance-id/clone" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CLONE",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

The user or service account that's using the [`instances.clone`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/clone) API method must have the `cloudsql.instances.clone` permission. For more information about required permissions to use API methods, see [Cloud SQL permissions](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions).

If you don't specify an allocated IP range, the following behavior is applied:

  * If the source instance was created with a specified range, the cloned instance is created in the same range.
  * If the source instance was not created with a specified range, the cloned instance is created in a random range.



## Troubleshoot

Issue | Troubleshooting | Cloning fails with `constraints/sql.restrictAuthorizedNetworks` error. | The cloning operation is blocked by the `Authorized Networks` configuration. `Authorized Networks` are configured for public IP addresses in the Connectivity section of the Google Cloud console, and cloning is not permitted due to [security considerations](https://docs.cloud.google.com/sql/docs/sqlserver/connection-org-policy). Remove all `Authorized Networks` entries from the Cloud SQL instance if you can. Otherwise, [create a replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica) without any `Authorized Networks` entries.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider. Help Token: [help-token-id].` |  You're trying to use the Google Cloud console to clone an instance with a private IP address, but you didn't specify the allocated IP range that you want to use and the source instance isn't created with the specified range. As a result, the cloned instance is created in a random range. Use `gcloud` to clone the instance and provide a value for the   
`--allocated-ip-range-name` parameter. For more information, see [Cloning an instance with a private IP](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance#gcloud_1).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
