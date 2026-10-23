---
url: https://docs.cloud.google.com/sql/docs/mysql/shrink-instance-storage-capacity/
title: Shrink instance storage capacity \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:54.366911+00:00
---

# Shrink instance storage capacity  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/shrink-instance-storage-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Shrink instance storage capacity Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/shrink-instance-storage-capacity "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/shrink-instance-storage-capacity "View this page for the SQL Server database engine")

This page shows you how to manage the storage capacity of a Cloud SQL instance using storage shrink capabilities.

## Before you begin

  1. Review the [feature's limitations](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink#limitations).

  2. If you're using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), make sure you are using the latest version of Google Cloud SDK and gcloud CLI.

     * [Install the latest gcloud CLI version](https://docs.cloud.google.com/sdk/docs/install#linux) (gcloud CLI version 563.0.0 or later).
     * To get the current gcloud CLI version, run `gcloud --version`.
     * To update the gcloud CLI version, run `gcloud components update`.
  3. Get the following IAM permissions:

     * `cloudsql.instances.getDiskShrinkConfig`
     * `cloudsql.instances.performDiskShrink`

These permissions are available in either of the following roles. When assigning your role, we recommend applying the principle of least privilege:

     * Cloud SQL Admin (`roles/cloudsql.admin`)
     * Cloud SQL Editor (`roles/cloudsql.editor`)

For more information, see the following resources:

     * [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles)
     * [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
     * [Granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



## Prepare the instance

Complete the following requirements before you begin.

These steps are the same for primary instances and read replicas.

If updating a read replica, make sure to shrink the capacity of the primary instance first, then shrink the size of the replica.

  1. [Get the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project containing the instance you want to manage.

  2. [Check the current state of the instance](https://docs.cloud.google.com/sql/docs/mysql/instance-info#info) to make sure it is running. One way to check is to use the [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe
         

Returns the following status:
         
         RUNNABLE
         

If not, [start the instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance#start).

  3. [Create a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#on-demand) of the current instance. This lets you [restore the instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups) later if you run into issues during configuration. 

  4. Disable all extensions or features that enable outbound connections (or require outbound data transfer). 




## Shrink the storage capacity of an instance

The following steps are the same for primary instances and read replicas.

  1. Check the target minimum storage capacity of the instance and the estimated operation time. This information can help you plan your storage shrink operation.

**Note:** This capability is unavailable for read replicas. Read replica storage capacity typically matches its associated primary instance.

### gcloud

Run the [`gcloud sql instances get-storage-shrink-config`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances) command:
         
         gcloud sql instances get-storage-shrink-config INSTANCE_NAME
         

Replace the following:

     * INSTANCE_NAME: the name of the primary instance.

The response includes a value for `minimalTargetSizeGb`. You can use this value to determine the value you want to use for the `--storage-size` parameter when you run a storage shrink operation.

The response also returns a message with an estimated operation time, similar to the following:
    
    ...
    "The estimated operation time is 20 minutes".
    

### REST v1

Use the [GET](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get) method to view the instance's target minimum storage capacity.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the name of the project where the primary instance resides.
     * INSTANCE_ID: the instance ID of the primary instance.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#instance",
      "min_target_size_gb": "1234"
      "message": "The size of your instance's storage impacts IOPS, and therefore shrinking your storage
        may have a negative impact on IOPS. Before shrinking your storage, please refer to our
        documentation on Cloud SQL limits to understand what impact shrinking your storage might have:
        https://docs.cloud.google.com/sql/docs/quotas#fixed-limits. Additionally, we recommend leaving an
        appropriate buffer for operational purposes, like reindexing, etc. We recommend a buffer of at
        least 100 GB or 20% more than current usage, whichever is larger. For more details, please refer
        to: https://docs.cloud.google.com/sql/docs/shared-responsibility. The estimated operation time is
        20 minutes."
    }
    
    

The response includes a value for `min_target_size_gb`. You can use this value to determine the value you want to use for the `--storage-size` parameter when you run a storage shrink operation.

The response also returns a message with an estimated operation time, similar to the following:
    
    ...
    "The estimated operation time is 20 minutes".
    

### REST v1beta4

Use the [GET](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get) method to view the instance's target minimum storage capacity.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the name of the project where the primary instance resides.
     * INSTANCE_ID: the instance ID of the primary instance.

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/getDiskShrinkConfig" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#instance",
      "min_target_size_gb": "1234"
      "message": "The size of your instance's storage impacts IOPS, and therefore shrinking your storage
        may have a negative impact on IOPS. Before shrinking your storage, please refer to our
        documentation on Cloud SQL limits to understand what impact shrinking your storage might have:
        https://docs.cloud.google.com/sql/docs/quotas#fixed-limits. Additionally, we recommend leaving an
        appropriate buffer for operational purposes, like reindexing, etc. We recommend a buffer of at
        least 100 GB or 20% more than current usage, whichever is larger. For more details, please refer
        to: https://docs.cloud.google.com/sql/docs/shared-responsibility. The estimated operation time is
        20 minutes."
    }
    
    

The response includes a value for `min_target_size_gb`. You can use this value to determine the value you want to use for the `--storage-size` parameter when you run a storage shrink operation.

The response also returns a message with an estimated operation time, similar to the following:
    
    ...
    "The estimated operation time is 20 minutes".
    

  2. Shrink storage capacity of the instance.

**Note:** The `--storage-size` flag is only supported for primary or standalone instances. You can't set a target storage size for a replica instance.

### gcloud

Run the following command to shrink storage on the instance:
         
         gcloud sql instances perform-storage-shrink INSTANCE_NAME \
           --storage-size=TARGET_STORAGE_SIZE
         

Replace the following:

     * INSTANCE_NAME: the name of the instance.
     * TARGET_STORAGE_SIZE: the target storage capacity in GB. For example, 100 GB.

### REST v1

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance resides.
     * INSTANCE_ID: the ID of the instance.
     * TARGET_STORAGE_SIZE: the target storage size in GB.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink

Request JSON body: 
    
    {
      "targetSizeGb": TARGET_STORAGE_SIZE
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/operation-id",
      "targetProject": "PROJECT_ID"
    }
    
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance resides.
     * INSTANCE_ID: the ID of the instance.
     * TARGET_STORAGE_SIZE: the target storage size of the instance.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink

Request JSON body: 
    
    {
      "targetSizeGb": TARGET_STORAGE_SIZE
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/performDiskShrink" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/operation-id",
      "targetProject": "PROJECT_ID"
    }
    
    

  3. To check the status of the storage shrink operation, see Check the status of an operation.




## Cancel storage shrink operation

**Note:** Cancel operations are only supported on primary or standalone instances.

  1. Get the storage shrink operation ID.

You can retrieve the operation ID by running the following [list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/list) command:
         
         gcloud sql operations list
         

  2. Send a cancellation request.

### gcloud

Run the following command to cancel the request:
         
         gcloud sql operations cancel OPERATION_ID
         

Replace the following:

OPERATION_ID: the ID of the storage shrink operation you want to cancel.

### REST v1

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance resides.
     * OPERATION_ID: the ID of the storage shrink operation you want to cancel.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID/cancel" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### REST v1beta4

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of the project where the instance resides.
     * OPERATION_ID: the ID of the storage shrink operation you want to cancel.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID/cancel" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




## Check the status of a cancellation request or other operation

To check the status of a request, run the following commands:

### gcloud

  1. Get the operation ID for the cancellation request:
         
         gcloud sql operations list
         

  2. Check the status of the operation:
         
         gcloud sql operations describe OPERATION_ID
         

Replace the following:

OPERATION_ID: the ID of the operation you want to check.




### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the instance resides.
  * OPERATION_ID: the ID of the storage shrink operation.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2023-12-18T22:43:09.849Z",
      "startTime": "2023-12-18T22:43:10.373Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "example_instance",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the instance resides.
  * OPERATION_ID: the ID of the storage shrink operation.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2023-12-18T22:43:09.849Z",
      "startTime": "2023-12-18T22:43:10.373Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "example_instance",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Troubleshooting

For information regarding troubleshooting, see [Issues updating storage capacity](https://docs.cloud.google.com/sql/docs/mysql/issues-updating-storage-capacity).

## What's next

  * [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink)
  * [Cloud SQL error messages](https://docs.cloud.google.com/sql/docs/mysql/error-messages)
  * [Cloud SQL storage options](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
