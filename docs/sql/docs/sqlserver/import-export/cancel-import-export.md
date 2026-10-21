---
url: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export/
title: Cancel the import and export of data \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:47.848596+00:00
---

# Cancel the import and export of data  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Cancel the import and export of data Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/import-export/cancel-import-export "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to cancel the import and export of data into Cloud SQL instances. This data is contained in either [SQL dump files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql) or [BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak).

## Before you begin

To cancel the import and export of data, you need the ID of the import or export operation. You need to specify this ID in the `gcloud` or REST API command so that Cloud SQL knows which operation to cancel.

The operation ID is returned in the `name` field of the response. To obtain this ID, see [Export and import using SQL dump files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql).

You can also find the operation ID by making an [`operations.list`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/list) call on the Cloud SQL instance.

## Cancel the import or export operation

You can use `gcloud` or REST API commands to cancel an import or export operation.

### gcloud

Use the `gcloud sql operations cancel` command to cancel the operation. 
    
    
    gcloud sql operations cancel operation-ID

Replace the operation-ID variable with the ID of the operation. For more information, see Before you begin. 

### REST v1

Before using any of the request data, make the following replacements: 

  * project-ID: The project ID.
  * operation-ID: The ID of the import or export operation. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export#before-you-begin).



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID/cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {}
    

This REST API call doesn't return any response. For more information about checking the cancellation status of the import or export operation, see Check the cancelled status. 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-ID: The project ID.
  * operation-ID: The ID of the import or export operation. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export#before-you-begin).



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID/cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID/cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID/cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {}
    

This REST API call doesn't return any response. For more information about checking the cancellation status of the import or export operation, see Check the cancelled status. 

## Check the cancelled status

You can use `gcloud` or REST API commands to check the status of a cancelled import or export operation.

### gcloud

Use the `[ gcloud sql operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/operations/describe)` command to check the status of the cancelled operation. 
    
    
    gcloud sql operations describe operation-ID

Replace the operation-ID variable with the ID of the cancelled operation. For more information, see Before you begin. 

### REST v1

Before using any of the request data, make the following replacements: 

  * project-ID: The project ID.
  * operation-ID: The ID of the import or export operation. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export#before-you-begin).



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
    "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2022-11-08T22:12:58.199Z",
      "startTime": "2022-11-08T22:13:04.798Z",
      "endTime": "2022-11-08T22:13:45.862Z",
      "error": {
        "kind": "sql#operationErrors",
        "errors": [
          {
            "kind": "sql#operationError",
            "code": "CANCEL_SUCCESSFUL",
            "message": "Operation successfully cancelled"
          }
        ]
      },
      "operationType": "EXPORT",
      "exportContext": {
        "uri": "gs://replica-bucket/source-database.sql",
        "kind": "sql#exportContext",
        "sqlExportOptions": {
          "schemaOnly": false,
          "mysqlExportOptions": {
            "masterData": 0
          }
        },
        "fileType": "SQL"
      },
      "name": "operation-ID",
      "targetId": "cloud-sql-instance-display-name",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-ID/operations/operation-ID",
      "targetProject": "project-ID",
      "instanceUid": "cloud-sql-instance-ID"
    }
    
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * project-ID: The project ID.
  * operation-ID: The ID of the import or export operation. For more information, see [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/cancel-import-export#before-you-begin).



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
    "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/project-ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2022-11-08T22:12:58.199Z",
      "startTime": "2022-11-08T22:13:04.798Z",
      "endTime": "2022-11-08T22:13:45.862Z",
      "error": {
        "kind": "sql#operationErrors",
        "errors": [
          {
            "kind": "sql#operationError",
            "code": "CANCEL_SUCCESSFUL",
            "message": "Operation successfully cancelled"
          }
        ]
      },
      "operationType": "EXPORT",
      "exportContext": {
        "uri": "gs://replica-bucket/source-database.sql",
        "kind": "sql#exportContext",
        "sqlExportOptions": {
          "schemaOnly": false,
          "mysqlExportOptions": {
            "masterData": 0
          }
        },
        "fileType": "SQL"
      },
      "name": "operation-ID",
      "targetId": "cloud-sql-instance-display-name",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/project-ID/operations/operation-ID",
      "targetProject": "project-ID",
      "instanceUid": "cloud-sql-instance-ID"
    }
    
    

## Troubleshoot

Issue | Troubleshooting | Error message: `You can't cancel operation [operation-ID] because this operation isn't in progress.` |  You're trying to cancel an import or export operation that's completed, failed, or cancelled. If the operation is running, you can cancel it.  
---|---  
Error message: `You can't cancel operation [operation-ID] because Cloud SQL doesn't support the cancellation of an [operation-type] operation.` | Cloud SQL doesn't support the cancellation of the operation because it has an [operation type](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#sqloperationtype) other than `IMPORT` or `EXPORT`.  
Error message: `The [operation-type] operation isn't cancelled. Wait and retry in a few seconds.` |  Cloud SQL can't cancel the import or export operation at this time. Try again in a few seconds. If the problem persists, contact [Google Cloud Support](https://docs.cloud.google.com/support).  
  
## What's next

  * Learn more about [best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).
  * Learn how to [export and import data into Cloud SQL instances using SQL dump files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql).
  * Learn how to [check the status of import and export operations](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/checking-status-import-export).
  * [Known issues for imports and exports](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues#import-export).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
