---
url: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring/
title: Restore an instance using a backup \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:31.404229+00:00
---

# Restore an instance using a backup  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Restore an instance using a backup Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restoring "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restoring "View this page for the SQL Server database engine")

You can restore your instance from a backup and recover it to a specific period of time to a new or an existing instance. You can restore a live or a deleted instance. To learn more about how restoring works, see [Restore overview](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).

To restore an instance using a backup, you must do the following:

  1. Find the backup you want to restore
  2. Use the backup to restore your instance



The location of your backup depends on your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options).

## Restore a live instance

You can restore a backup in the following ways:

  * Restore to the same instance where the backup is taken
  * Restore to a new or existing instance in the same project
  * Restore to a new or existing instance in a different project or region



### Restore to the same instance

When you restore data from a backup to the same instance, you return the data on that instance to the state of when you took the backup.

**Warning:** The restore process overwrites all of the current data on the instance, including previous point-in-time recovery (PITR) logs. Previous on-demand and automatic backups on the instance are retained.

To restore your instance using a backup to the same instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. On the **Backups** page, click **Standard tier** or **Enhanced tier** , depending on your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options).

  3. If your instance is using standard backups, then select the instance you want to view backups for.




If your instance is using enhanced backups, then select **Enhanced tier** , then select the **Backup vault** that contains the backup you want to use. All backups available in the backup vault for your selected instance are displayed.

  1. Find the name of the backup you want to restore and then click **Restore**.

**Note:** All replicas for your target instance must be deleted prior to restoring.

  1. In **Choose restore destination** , select **Overwrite the source instance**.

  2. In the **Destination instance ID** field, enter the name of the instance to be overwritten to confirm your selection.

  3. Click **Restore**.




Cloud SQL restores the backup to same instance. To check the status of the restore operation, go to the **Operations** page for the instance.

You can create any replicas once the restore operation completes.

###  gcloud 

  1. All replicas must be deleted from your instance prior to restoring.

Determine if your instance has any read replicas using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance contains replicas, then delete the replicas using the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
    
    gcloud sql instances delete REPLICA_NAME
    

Replace the following:

     * `REPLICA_NAME`: the name of the replica.
  2. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  3. To restore the instance from the specified backup, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=INSTANCE_NAME
         

Replace the following:

     * `BACKUP_ID`: the backup you want to restore's ID.
     * `INSTANCE_NAME`: the name of the instance.
  4. After the restore operation completes, recreate any replicas that you deleted in this procedure.




###  REST v1 

  1. To determine if the instance has any read replicas and to get their IDs, list all the replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the backup you want to use.

     * If your instance is using standard backups, run the following:

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
    
    

     * If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).
  4. Restore the instance from the backup:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BACKUP_ID the backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": "BACKUP_ID",
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  5. After the restore operation completes, recreate any replicas that you deleted in this procedure.




###  REST v1beta4 

  1. To determine if the instance has any read replicas and to get their IDs, list all the replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the backup you want to use.

     * If your instance is using standard backups, run the following:

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
    
    

     * If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).
  4. Restore the instance from the backup:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID
     * BACKUP_RUN_ID: a date-and-time stamp of when Cloud SQL restores the instance from the backup

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": "BACKUP_RUN_ID",
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  5. After the restore operation completes, recreate any replicas that you deleted in this procedure.




### Restore to a new or existing instance

When you restore data from a backup to a different instance, you update the data on the target instance to the state of the source instance when you took the backup.

If you need a list of backups for the project and can't view them on the instance overview page due to an outage, you can use the [backupRuns.list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list) API with a wildcard (-). The wildcard option retrieves a list of all backups across all instances in the project. For more information, see [Viewing backups during an outage](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#backuplist).

To restore your instance to a new or existing instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. On the **Backups** page, click **Standard tier** or **Enhanced tier** , depending on your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options).

  3. If your instance is using standard backups, then select the instance you want to view backups for.




If your instance is using enhanced backups, then select **Enhanced tier** , then select the **Backup vault** that contains the backup you want to use. All backups available in the backup vault for your selected instance are displayed.

  1. Find the name of the backup you want to restore and then click **Restore**.

  2. In **Choose restore destination** :

     * If you want to restore your instance to a new instance, then select **Restore to a new instance** and update the following:

     * Under **Region** , confirm the region. The region should match the new instance's region.

     * In the **Instance ID** box, give your new instance a name. This name is permanent and cannot be changed.

     * If you want to restore your instance to an existing instance, then select **Overwrite an existing instance** and do the following:

**Note:** All replicas for your target instance must be deleted prior to restoring.
     * From the **Instance to be overwritten** menu, select the instance you want to use for the restore. The instance you select and all its data will be overwritten.

     * In the **Destination instance ID** field, enter the name of the instance to be overwritten to confirm your selection.

  3. Click **Restore**.

Cloud SQL restores the backup to the new or existing instance, depending on your selection. To check the status of the restore operation, go to the **Operations** page for the instance.

You can create any replicas once the restore operation completes.




###  gcloud 

  1. If you're restoring to an existing instance, then all replicas must be deleted from your target instance prior to restoring.

Determine if your instance has any read replicas using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe TARGET_INSTANCE_NAME
         

Replace the following:

     * `TARGET_INSTANCE_NAME`: the name of the instance.

If your instance contains replicas, then delete the replicas using the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
    
    gcloud sql instances delete REPLICA_NAME
    

Replace the following:

     * `REPLICA_NAME`: the name of the replica.
  2. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  3. To restore the instance from the specified backup, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=TARGET_INSTANCE_NAME \
         --backup-instance=SOURCE_INSTANCE_NAME
         

Replace the following:

     * `BACKUP_ID`: the backup you want to restore's ID.
     * `TARGET_INSTANCE_NAME`: the name of the target new or existing instance.
     * `SOURCE_INSTANCE_NAME`: the name of the source instance.
  4. If you're restoring to an existing instance, then after the restore operation completes, recreate any replicas that you deleted in this procedure.




###  REST v1 

  1. If you're using an existing instance, all replicas must be deleted prior to restoring. Determine if the instance has any read replicas and to get their IDs, list all the replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the backup you want to use.

     * If your instance is using standard backups, run the following:

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
    
    

     * If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).
  4. Restore the instance from the backup:

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * target-instance-id: The target instance ID
     * source-instance-id: The source instance ID
     * backup-id The backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": backup-id,
        "instanceId": "source-instance-id"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/target-instance-id/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  5. After the restore operation completes, recreate any replicas that you deleted in this procedure.




###  REST v1beta4 

  1. To determine if the instance has any read replicas and to get their IDs, list all the replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all replicas for the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the backup you want to use.

     * If your instance is using standard backups, run the following:

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
    
    

     * If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).
  4. Restore the instance from the backup:

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * target-instance-id: The target instance ID
     * source-instance-id: The source instance ID
     * backup-id The backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": backup-id,
        "instanceId": "source-instance-id"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/target-instance-id/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  5. After the restore operation completes, recreate any replicas that you deleted in this procedure.




### Restore to an instance in another project

You can use the `project` parameter to restore data to an instance in a different project. When you restore from a backup to an instance in a different project, you update the data on the target instance to the state of the source instance when you took the backup.

The user restoring to a different project must have the following permissions to restore the instance: * [`cloudsql.instances.restoreBackup`](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions) permission for the target project * [`cloudsql.backupRuns.get`](https://docs.cloud.google.com/sql/docs/mysql/iam-permissions) permission for the source project.

These permissions are included the `Cloud SQL Admin` role.

**Warning:** The restore process overwrites all of the current data on the instance, including previous point-in-time recovery (PITR) logs. Previous on-demand and automatic backups on the instance are retained.

To restore your instance using a backup to an instance in a different project or region, do the following:

###  gcloud 

  1. If restoring to an existing instance, determine if the target instance has any read replicas using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe TARGET_INSTANCE_NAME
         

Replace the following:

     * `TARGET_INSTANCE_NAME`: the name of the target instance you want to restore your backup to.

Delete all replicas for your target instance using the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
    
    gcloud sql instances delete REPLICA_NAME
    

Replace the following:

     * `REPLICA_NAME`: the name of the replica of the target instance.

All replicas must be deleted before you can restore to an existing instance.

  2. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  3. To restore to a new or existing instance in a new project, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=TARGET_INSTANCE_NAME \
         --backup-instance=SOURCE_INSTANCE_NAME \
         --backup-project=SOURCE_INSTANCE_PROJECT
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup from the backup vault. You'll need to include the full path of the backup in this field.

     * `TARGET_INSTANCE_NAME`: the instance in the destination project which you're restoring data.

     * `SOURCE_INSTANCE_NAME`: the instance name in the source project where the data is.

     * `SOURCE_INSTANCE_PROJECT`: the project that contains the source instance.




###  REST v1 

  1. To obtain the `backupId`, run the following:

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
    
    

  2. Restore the backup to an instance in a different project:

Before using any of the request data, make the following replacements: 

     * source-project-id: The source project ID
     * target-project-id: The target project ID
     * target-instance-id: The target instance ID
     * source-instance-id: The source instance ID
     * backup-id The backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/target-project-id/instances/target-instance-id/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": backup-id,
        "project": "source-project-id",
        "instanceId": "source-instance-id"
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
         "https://sqladmin.googleapis.com/v1/projects/target-project-id/instances/target-instance-id/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/target-project-id/instances/target-instance-id/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/target-project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_VOLUME",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/target-project-id/operations/operation-id",
      "targetProject": "target-project-id"
    }
    




###  REST v1beta4 

  1. To obtain the `backupId`, run the following:

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
    
    

  2. Restore the backup to an instance in a different project:

Before using any of the request data, make the following replacements: 

     * source-project-id: The source project ID
     * target-project-id: The target project ID
     * target-instance-id: The target instance ID
     * source-instance-id: The source instance ID
     * backup-id The backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/target-project-id/instances/target-instance-id/restoreBackup

Request JSON body: 
    
    {
      "restoreBackupContext":
      {
        "backupRunId": backup-id,
        "project": "source-project-id",
        "instanceId": "source-instance-id"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/target-project-id/instances/target-instance-id/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/target-project-id/instances/target-instance-id/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/target-project-id/instances/target-instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_VOLUME",
      "name": "operation-id",
      "targetId": "target-instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/target-project-id/operations/operation-id",
      "targetProject": "target-project-id"
    }
    




## Restore a deleted instance

You can use a [final backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup) or a [retained backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups) to restore a deleted instance for the following scenarios:

  * Restore to an existing instance in the same project
  * Restore to a new instance in the same project
  * Restore to a new or existing instance in a different project



### Restore to an existing instance

When you restore data from a final or retained backup to an existing instance, you update the data on the target instance to the state of the source instance when you took the backup. For more information about restoring an instance, see [General tips about performing a restore](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-restore).

**Warning:** The restore process overwrites all of the current data on the instance, including previous point-in-time recovery (PITR) logs. Previous on-demand and automatic backups on the instance are retained.

To restore a deleted instance using a backup to an existing instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. If the target instance has any read replicas, then use the more actions menu ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png) to delete them. All replicas must be deleted before you can restore a retained or final backup to the existing instance.

  3. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  4. On the **Backups** page, click **Standard tier** or **Enhanced tier** , depending on your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options).

  5. If your instance is using standard backups, then click the name of the deleted instance that contains the backup you want to restore.




If your instance is using enhanced backups, select **Enhanced tier** , then select the **Backup vault** that contains the backup you want to use. All backups available in the backup vault for your selected instance are displayed.

  1. Find the name of the backup you want to restore and then click **Restore**.

  2. On the **Restore an instance from a backup** page, confirm that you selected the correct backup in **Review backup details**.

  3. In the **Choose restore destination** section, select **Overwrite an existing instance**.

  4. From the **Instance to be overwritten** menu, select the instance that you want to restore the backup to. The instance you select and all its data will be overwritten.

  5. To confirm your selection, in the **Destination instance ID** field, enter the name of the instance to be overwritten.

  6. Click **Restore**.




Cloud SQL will restore the backup to the existing instance. To check the status of the restore operation, go to the **Operations** page for the instance.

You can create any replicas once the restore operation completes.

###  gcloud 

  1. When restoring to an existing instance, all replicas must be deleted from your target instance prior to restoring.

Determine if your instance has any read replicas using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe TARGET_INSTANCE_NAME
         

Replace the following:

     * `TARGET_INSTANCE_NAME`: the name of the instance.

If your instance contains replicas, then delete the replicas using the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
    
    gcloud sql instances delete REPLICA_NAME
    

Replace the following:

     * `REPLICA_NAME`: the name of the replica.
  2. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  3. To restore the instance from the specified backup, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=TARGET_INSTANCE_NAME
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup you want to restore.
     * `TARGET_INSTANCE_NAME`: the name of the new or existing target instance.
  4. After the restore operation completes, recreate any replicas that you deleted in this procedure.




###  REST v1 

  1. When restoring to an existing instance, all replicas must be deleted from your target instance prior to restoring. To determine if the instance has any read replicas, run the following:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all the read replicas of the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the final or retained backup you want to use:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "state": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
           }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "This is a final backup.",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
    }
    

  4. Restore the target instance from the retained or final backup.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * TARGET_INSTANCE_ID: the target instance ID
     * BACKUP_ID: the backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




###  REST v1beta4 

  1. When restoring to an existing instance, all replicas must be deleted from your target instance prior to restoring. To determine if the instance has any read replicas, run the following:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID?fields=replicaNames" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "replicaNames": [
        "REPLICA_NAME"
      ]
    }
    

  2. Delete all the read replicas of the instance:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * REPLICA_ID: the replica ID

HTTP method and URL: 
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/REPLICA_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "REPLICA_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Get the ID of the final or retained backup you want to use:

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "state": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
           }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "This is a final backup.",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
    }
    

  4. Restore the target instance from the retained or final backup.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * TARGET_INSTANCE_ID: the target instance ID
     * BACKUP_ID: the backup ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




### Restore to a new instance

When you create an instance from a final or retained backup, Cloud SQL uses the configuration settings of the instance from where the backup is taken. After the instance is created, Cloud SQL restores the data to the state of when the backup is taken.

To restore data from a final or retained backup to a new instance, you must have the following permissions:

  * `cloudsql.instances.create` permission for the target project
  * `cloudsql.instances.restoreBackup` permission for the target project
  * `cloudsql.backupRuns.get permission` for the source backup.



These permissions are included in the Cloud SQL Admin role.

**Note:** The instance that you create from the final backup has a different IP address from the instance where the final backup is taken. For more information about restoring an instance, see [General tips about performing a restore](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-restore).

To restore a deleted instance using a backup to a new instance, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. On the **Backups** page, click **Standard tier** or **Enhanced tier** , depending on your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options).

  3. If your instance is using standard backups, then click the name of the deleted instance that contains the backup you want to restore.

If your instance is using enhanced backups, then select **Enhanced tier** , then select the **Backup vault** that contains the backup you want to use. All backups available in the backup vault for your selected instance are displayed.

  4. Find the name of the backup you want to restore and click **Restore**.

  5. On the **Restore an instance from a backup** page, confirm that you selected the correct backup in **Review backup details**.

  6. In the **Choose restore destination** section, select **Restore to a new instance**.

  7. From the **Region** menu, select the region for the new instance.

  8. In the **Instance ID** field, enter an ID for the new instance. This ID cannot be changed once created.

  9. Click **Restore**.




Cloud SQL will restore the backup to the existing instance. To check the status of the restore operation, go to the **Operations** page for the instance.

###  gcloud 

  1. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  2. To restore the instance from the specified backup, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=TARGET_INSTANCE_NAME
         

Replace the following:

     * `BACKUP_ID`: The ID of th backup you want to restore.
     * `TARGET_INSTANCE_NAME`: the name of the new or existing target instance.



###  REST v1 

**Restore a new instance from the specified retained or final backup**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * TARGET_INSTANCE_ID: the target instance ID
  * BACKUP_ID: the backup ID

**Note:** The `restore_instance_settings: {}` line of code lets Cloud SQL restore data from the backup to the new instance.

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
      restore_instance_settings: {}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

**Restore a new instance from the specified retained or final backup**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * TARGET_INSTANCE_ID: the target instance ID
  * BACKUP_ID: the backup ID

**Note:** The `restore_instance_settings: {}` line of code lets Cloud SQL restore data from the backup to the new instance.

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
      restore_instance_settings: {}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Restore to a new or existing instance in a different project

You can use the `project` parameter to restore data to an instance in a different project. When you restore a deleted instance from a backup to an instance in a different project, the target instance is updated to the state of the source instance when you took the backup.

The user restoring to a different project must have the following permissions to restore the instance:

  * `cloudsql.instances.create` permission for the target project
  * `cloudsql.instances.restoreBackup` permission for the target project
  * `cloudsql.backupRuns.get permission` for the source backup.



These permissions are included the `Cloud SQL Admin` role.

**Warning:** The restore process overwrites all of the current data on the instance, including previous point-in-time recovery (PITR) logs. Previous on-demand and automatic backups on the instance are retained.

To restore your instance using a backup to an instance in a different project or region, do the following:

###  gcloud 

  1. If restoring to an existing instance, determine if the target instance has any read replicas using the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe TARGET_INSTANCE_NAME
         

Replace the following:

     * `TARGET_INSTANCE_NAME`: the name of the target instance you want to restore your backup to.

Delete all replicas for your target instance using the [`gcloud sql instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command:
           
           gcloud sql instances delete REPLICA_NAME
             ```
           
           Replace the following:
           

       * `REPLICA_NAME`: the name of the replica of the target instance.

All replicas must be deleted before you can restore to an existing instance.

  2. Find the backup you want to use.

If your instance is using standard backups, use the [`gcloud sql backups list`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command to find a backup and record its `ID` value:
         
         gcloud sql backups list --instance=INSTANCE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

If your instance is using enhanced backups, see [List all backups in a backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#list-backups).

  3. To restore to a new or existing instance in a new project, use the [`gcloud sql backups restore`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/restore) command:
         
         gcloud sql backups restore BACKUP_ID \
         --restore-instance=TARGET_INSTANCE_NAME \
         --backup-instance=SOURCE_INSTANCE_NAME \
         --backup-project=SOURCE_INSTANCE_PROJECT
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup from the backup vault. You'll need to include the full path of the backup in this field.

     * `TARGET_INSTANCE_NAME`: the instance in the destination project which you're restoring data.

     * `SOURCE_INSTANCE_NAME`: the instance name in the source project where the data is.

     * `SOURCE_INSTANCE_PROJECT`: the project that contains the source instance.




###  REST v1 

To get the `backupID` for the retained or final backup, run the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "state": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
           }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "This is a final backup.",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
    }
    

**Restore to a different project**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * TARGET_INSTANCE_ID: the target instance ID
  * BACKUP_ID: the backup ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

To get the `backupID` for the retained or final backup, run the following:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "state": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
           }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "This is a final backup.",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
    }
    

**Restore to a different project**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * TARGET_INSTANCE_ID: the target instance ID
  * BACKUP_ID: the backup ID



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup

Request JSON body: 
    
    
    {
      backup: projects/PROJECT_ID/backups/BACKUP_ID
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID/restoreBackup" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/TARGET_INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "RESTORE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "TARGET_INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## What's next

  * [See how to recreate a read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica). 

  * [Learn more about backing up your data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).

  * [See how to backup your data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up). 

  * See the [MySQL documentation about point-in-time recovery](https://dev.mysql.com/doc/refman/8.4/en/point-in-time-recovery.html).

  * See the [MySQL documentation about the mysqlbinlog tool](https://dev.mysql.com/doc/refman/8.4/en/mysqlbinlog.html). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
