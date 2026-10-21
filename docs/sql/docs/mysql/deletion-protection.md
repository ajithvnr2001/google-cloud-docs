---
url: https://docs.cloud.google.com/sql/docs/mysql/deletion-protection/
title: Prevent deletion of an instance \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:39.704279+00:00
---

# Prevent deletion of an instance  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/deletion-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Prevent deletion of an instance Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/deletion-protection "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/deletion-protection "View this page for the SQL Server database engine")

This page describes how to protect Cloud SQL instances from accidental deletion.

## Overview

Instance deletion protection lets you to prevent the accidental removal of existing and new instances. Using instance deletion protection, you can safeguard instances that are important to your applications and services.

You can enable the deletion protection option when you create an instance. Additionally, you can enable this option on an existing instance. In both cases, deletion is prevented at the instance level. By default, the deletion protection option is disabled unless you use the Google Cloud console or Terraform to create an instance.

When you clone an instance, the new instance receives the deletion protection option (enabled or disabled) from the source instance.

## Plan for deletion protection

If you are planning to create an instance, decide whether you want to protect the new instance from accidental deletion. For example, a critical instance should be protected in this way.

Also consider whether there are existing instances you want to protect from accidental deletion. If you have multiple instances to protect, enable the option on each instance.

### Consider deletion protection for read replicas

When you create a read replica, that read replica doesn't get a deletion protection setting from the primary instance; this setting remains independent. However, you can enable deletion protection on a new or existing read replica.

For Cloud SQL read replicas, the deletion protection option works the same way as it does for Cloud SQL instances.

### Confirm the necessary permissions or roles

To enable the deletion protection option, the service account associated with the Cloud SQL instance must have certain [permissions or IAM roles](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions).

#### Permissions or roles for creating an instance

As in the case of related operations, the deletion protection option requires the `cloudsql.instances.create` permission or the `cloudsql.admin` role. Thus, when you create an instance, no extra permissions are needed to enable deletion protection.

#### Permissions or roles for editing an instance

As in the case of related operations, deletion protection changes require the `cloudsql.instances.update` permission or the `cloudsql.editor` role. Thus, when you edit an instance for deletion protection, no extra permissions are needed.

### Plan instance deletion

If you are planning to delete an instance, first do the following:

  * Confirm that it is safe to delete the instance
  * Confirm that deletion protection is disabled; if necessary, edit the instance to disable deletion protection



### Limitations of deletion protection

Deletion protection on an instance does not prevent:

  * Stopping the instance
  * Restarting the instance
  * Editing the instance
  * Deleting a backup
  * Suspending the instance due to billing issues
  * Deleting the suspended instance due to billing issues
  * Deleting the instance due to a project deletion



## Enable deletion protection on a new instance

The following are ways to enable the deletion protection option. By default, the deletion protection option is disabled unless you use the Google Cloud console or Terraform to create an instance.

If deletion protection is enabled, an attempt to delete the instance fails.

### Console

  1. Follow the steps to begin [ creating an Instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen).
  2. In the **Customize your instance** section, expand **Show configuration options**.
  3. Expand **Data Protection**.
  4. In the **Data Protection** section, confirm that the **Prevent instance deletion** checkbox is selected.
  5. As needed for your instance, select other [configuration options](https://docs.cloud.google.com/sql/docs/mysql/instance-settings). 
  6. Click **Create instance**.



### gcloud

To enable deletion protection during instance creation, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create#--\[no-\]deletion-protection) command, similar to the following:
    
    
    gcloud sql instances create INSTANCE_NAME \
        --deletion-protection

### REST v1

To enable deletion protection during instance creation, specify `true` in the `deletionProtection` field.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: Desired instance ID
  * database-version: The database version
  * region: desired region
  * machine-type: desired machine type



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances

Request JSON body: 
    
    
    {
      "name": "instance-id",
      "region": "region",
      "databaseVersion": "database-version",
      "settings": {
        "tier": "machine-type",
        "deletionProtectionEnabled": true
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-05-24T15:34:10.929Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To enable deletion protection during instance creation, specify `true` in the `deletionProtection` field.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: Desired instance ID
  * database-version: The database version
  * region: desired region
  * machine-type: desired machine type



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances

Request JSON body: 
    
    
    {
      "name": "instance-id",
      "region": "region",
      "databaseVersion": "database-version",
      "settings": {
        "tier": "machine-type",
        "deletionProtectionEnabled": true
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
         "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-05-26T15:37:10.929Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) is constructed for this task, see the [APIs Explorer on the instances:insert page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert). 

## Enable or disable deletion protection on an existing instance

The following are the ways to edit an instance for deletion protection. If you enable the option, a subsequent attempt to delete the instance fails.

### Console

  1. Follow the steps to begin [ editing an Instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#edit_an_instance).
  2. After you click **Edit** , find the **Customize your instance** section and expand **Show configuration options**.
  3. Expand **Data Protection**.
  4. In the **Data Protection** section, select or clear the **Prevent instance deletion** checkbox.
  5. As needed for your instance, edit other [configuration options](https://docs.cloud.google.com/sql/docs/mysql/instance-settings). 
  6. Click **Save**.



### gcloud

To enable deletion protection when you update an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--\[no-\]deletion-protection) command, similar to the following:
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --deletion-protection

To disable deletion protection when you update an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch#--\[no-\]deletion-protection) command, similar to the following:
    
    
    gcloud sql instances patch INSTANCE_NAME \
        --no-deletion-protection

### REST v1

To enable deletion protection when you update an instance, specify `true` in the `deletionProtection` field. To remove deletion protection, specify `false` in that field.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: Desired instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings": {
        "deletionProtectionEnabled": true
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-06-1T03:42:12.281Z",
      "operationType": "CREATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

To enable deletion protection when you update an instance, specify `true` in the `deletionProtection` field. To remove deletion protection, specify `false` in that field.

Before using any of the request data, make the following replacements: 

  * project-id: Your project ID
  * instance-id: Desired instance ID



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings": {
        "deletionProtectionEnabled": true
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
         "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2022-06-1T03:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
