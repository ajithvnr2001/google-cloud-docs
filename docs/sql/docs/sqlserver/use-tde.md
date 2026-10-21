---
url: https://docs.cloud.google.com/sql/docs/sqlserver/use-tde/
title: Use transparent data encryption (TDE) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:09.293220+00:00
---

# Use transparent data encryption (TDE)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/use-tde/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use transparent data encryption (TDE) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page shows you how to use [transparent data encryption (TDE)](https://docs.cloud.google.com/sql/docs/sqlserver/about-tde).

The following sections show you how to manage TDE certificates.

## Before you begin

To import or export TDE certificates, you must have the `cloudsql.instances.manageEncryption` Identity and Access Management permission, available in the `cloudsql.admin` role. For more information, see the [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#roles).

**Note:** Only the `sqlserver` login has permissions to access certificates. This permission can be granted to other logins using the following command:
    
    
    GRANT VIEW ANY DEFINITION TO other_login AS CustomerDbRootRole

## Import an external TDE certificate

**Note:** You can't directly import external TDE certificates to replica instances.

### Console

You can't import a TDE certificate using Google Cloud console.

### gcloud

Use the following `[gcloud sql import](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import)` to import a certificate from a Cloud Storage bucket:
    
    
        gcloud sql import tde INSTANCE_NAME \
        --certificate CERTIFICATE_NAME \
        --cert-path=gs://BUCKET_NAME/CERTIFICATE_NAME \
        --pvk-path=gs://BUCKET_NAME/KEY_NAME \
        --prompt-for-pvk-password \
        --pvk-password CERTIFICATE_PASSWORD
        

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance to which you want to import the TDE certificate.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to import.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the TDE certificate you want to import is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



### REST v1

To import a TDE certificate, use the [`instances.import`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/import) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the encryption certificate is to be imported.
  * INSTANCE_NAME: the name of the Cloud SQL instance to which you want to import the encryption certificate.
  * TDE_CERTIFICATE_NAME: the name of the encryption certificate you want to use after it has been imported.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to import.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the encryption certificate you want to import is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import

Request JSON body: 
    
    
    
    {
      "importContext":
        {
            "fileType": "TDE",
            "tdeImportOptions":
              {
                "name": "TDE_CERTIFICATE_NAME",
                "certificatePath": "gs://BUCKET_NAME/CERTIFICATE_NAME",
                "privateKeyPath": "gs://BUCKET_NAME/KEY_NAME",
                "privateKeyPassword": "CERTIFICATE_PASSWORD"
              }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

### REST v1beta4

To import a TDE certificate, use the [`instances.import`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project where the encryption certificate is to be imported.
  * INSTANCE_NAME: the name of the Cloud SQL instance to which you want to import the encryption certificate.
  * TDE_CERTIFICATE_NAME: the name of the encryption certificate you want to use after it has been imported.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to import.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the encryption certificate you want to import is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import

Request JSON body: 
    
    
    
    {
      "importContext":
        {
            "fileType": "TDE",
            "tdeImportOptions":
              {
                "name": "TDE_CERTIFICATE_NAME",
                "certificatePath": "gs://BUCKET_NAME/CERTIFICATE_NAME",
                "privateKeyPath": "gs://BUCKET_NAME/KEY_NAME",
                "privateKeyPassword": "CERTIFICATE_PASSWORD"
              }
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/import" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

Each imported TDE certificate is assigned a unique name in the following format:
    
    
      gcloud_tde_user_CERTIFICATE_NAME_GENERATED_GUID

If [point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) is enabled on the instance, it may take several minutes before the imported TDE certificate is available.

## Rotate TDE certificates

  * You can rotate an imported TDE certificate with the `msdb.dbo.gcloudsql_rotate_tde_certificate` stored procedure. The procedure must be invoked by the `sqlserver` user, or by users to which the `sqlserver` user has given permission, using a call similar to the following:
        
        EXEC msdb.dbo.gcloudsql_rotate_tde_certificate TDE_CERTIFICATE_NAME
            




## Delete TDE certificates

  * You can import up to ten user TDE certificates. If you need to import more, delete any unnecessary TDE certificates using the `msdb.dbo.gcloudsql_drop_tde_user_certificate` stored procedure. The procedure must be invoked by the `sqlserver` user, or by users to which the `sqlserver` user has given permission, using a call similar to the following:
        
        EXEC gcloudsql_drop_tde_user_certificate TDE_CERTIFICATE_NAME
            

  * You can't delete a certificate managed by Cloud SQL.

  * You can't delete a certificate while it is in use.




## Export a TDE certificate

You must specify the full TDE certificate name—including the prefix and the suffix—to export. You can look up the full TDE encryption certificate name querying the name column from the `sys.certificates` view:
    
    
        SELECT name FROM sys.certificates
      

### Console

You can't export a TDE certificate using Google Cloud console.

### gcloud

Use the following `[gcloud sql export](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export)` to export a TDE certificate to a Cloud Storage bucket:
    
    
              gcloud sql export tde INSTANCE_NAME \
              --certificate CERTIFICATE_NAME \
              --cert-path=gs://BUCKET_NAME/CERTIFICATE_NAME \
              --pvk-path=gs://BUCKET_NAME/KEY_NAME \
              --prompt-for-pvk-password \
              --pvk-password CERTIFICATE_PASSWORD
            

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance from which you want to export the TDE certificate.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to export.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the TDE certificate you want to export is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



### REST v1

To export a TDE certificate, use the [`instances.export`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/export) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project from which the encryption certificate is to be exported.
  * INSTANCE_NAME: the name of the Cloud SQL instance from which you want to export the encryption certificate.
  * TDE_CERTIFICATE_NAME: the name of the encryption certificate you want to use after it has been exported.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to export.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the encryption certificate you want to export is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export

Request JSON body: 
    
    
    
    {
      "exportContext":
        {
          "fileType": "TDE",
          "tdeExportOptions":
            {
              "name": "TDE_CERTIFICATE_NAME",
              "certificatePath": "gs://BUCKET_NAME/CERTIFICATE_NAME",
              "privateKeyPath": "gs://BUCKET_NAME/KEY_NAME",
              "privateKeyPassword": "CERTIFICATE_PASSWORD"
            }
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/INSTANCE_NAME/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

### REST v1beta4

To export a TDE certificate, use the [`instances.export`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/import) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the name of the project from which the encryption certificate is to be exported.
  * INSTANCE_NAME: the name of the Cloud SQL instance from which you want to export the encryption certificate.
  * TDE_CERTIFICATE_NAME: the name of the encryption certificate you want to use after it has been exported.
  * CERTIFICATE_NAME: the name of the encryption certificate you want to export.
  * BUCKET_NAME: the name of the Cloud Storage bucket where the encryption certificate you want to export is located.
  * KEY_NAME: the name of the encryption key associated with the Cloud Storage bucket.
  * CERTIFICATE_PASSWORD: the certificate password.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export

Request JSON body: 
    
    
    
    {
      "exportContext":
        {
          "fileType": "TDE",
          "tdeExportOptions":
            {
              "name": "TDE_CERTIFICATE_NAME",
              "certificatePath": "gs://BUCKET_NAME/CERTIFICATE_NAME",
              "privateKeyPath": "gs://BUCKET_NAME/KEY_NAME",
              "privateKeyPassword": "CERTIFICATE_PASSWORD"
            }
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/INSTANCE_NAME/export" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/instances/DESTINATION_INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_NAME/operations/OPERATION_ID",
      "targetProject": "PROJECT_NAME"
    }
    

## Import a TDE-encrypted backup

When importing a TDE-encrypted backup, if the matching TDE certificate is already on the source instance, then you can import the encrypted backup directly and it won't be decrypted. You don't need to provide the certificate again.

If the certificate isn't on the instance, then use the `--keep-encrypted` flag when importing. The flag provides the following benefits:

  * Keeps the TDE certificate associated with the instance.
  * Prevents the backup from being decrypted during import.



If you don't use the `--keep-encrypted` flag, the imported backup will be decrypted, and the TDE certificate won't be saved on the server.

For more information, see the following resources:

  * [Export and import using BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak)
  * [Import data to a Cloud SQL instance from a BAK backup file ](https://docs.cloud.google.com/sdk/gcloud/reference/sql/import/bak)



## Export a TDE-encrypted backup

You can export a TDE-encrypted backup the same way you export an unencrypted one. The certificate used to encrypt the backup is not included in the export. You must export it separately.

For more information, see the following resources:

  * [Export and import using BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak)
  * [Export data to a Cloud SQL instance from a BAK backup file ](https://docs.cloud.google.com/sdk/gcloud/reference/sql/export/bak)



## Encrypt and decrypt a database

You can encrypt and decrypt your instance in much the same way you would using SQL Server.

Initially, only user `root` logins, such as `sqlserver` can access TDE certificates. To grant access to other users, use the following command or similar:
    
    
        GRANT VIEW ANY DEFINITION TO CERTIFICATE_NAME AS CustomerDbRootRole
      

Alternatively, you can grant access to a specific certificate and database user.

You can encrypt a database using the following command or similar:
    
    
        CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM = AES_256 ENCRYPTION BY SERVER CERTIFICATE CERTIFICATE_NAME
        ALTER DATABASE DATABASE_NAME SET ENCRYPTION ON
      

You can decrypt a database using the following command or similar:
    
    
        ALTER DATABASE DATABASE_NAME SET ENCRYPTION OFF
      

## What's next

  * [About TDE](https://docs.cloud.google.com/sql/docs/sqlserver/about-tde)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
