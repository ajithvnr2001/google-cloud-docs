---
url: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-backups-deleted-instance/
title: Manage backups for deleted instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:30.319420+00:00
---

# Manage backups for deleted instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-backups-deleted-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage backups for deleted instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-backups-deleted-instance "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-backups-deleted-instance "View this page for the SQL Server database engine")

You can manage backups after an instance is deleted if you elected to [retain backups after instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups), or [took a final backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup) prior to deleting your instance. Retained backups include automated and on-demand backups that were taken when the instance was live. When you delete your instance, these backups become independent of your instance and are stored at the project level. For more information about how backups work and which backups are retained, see [Cloud SQL backups overview](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).

You can use these backups to [restore an instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore) after your instance is deleted.

## Before you begin

To manage retained backups in a Google Cloud project, you need the following permissions:

###  Console 

Task | Required permissions  
---|---  
List backups | `cloudsql.backupRuns.list`  
Describe a backup | `cloudsql.backupRuns.get`  
Update a backup | `cloudsql.backupRuns.update`  
Delete a backup | `cloudsql.backupRuns.delete`  
  
###  gcloud 

Action | Command | Required permissions  
---|---|---  
List backups | `gcloud sql backups list` | `cloudsql.backupRuns.list`  
Describe a backup | `gcloud sql backups describe` | `cloudsql.backupRuns.get`  
Update a backup | `gcloud sql backups patch` | `cloudsql.backupRuns.update`  
Delete a backup | `gcloud sql backups delete` | `cloudsql.backupRuns.delete`  
  
###  REST 

Action | Method | Required permissions  
---|---|---  
List backups | `backups.listBackup` | `cloudsql.backupRuns.list`  
Describe a backup | `backups.getBackup` | `cloudsql.backupRuns.get`  
Update a backup | `backups.updateBackup` | `cloudsql.backupRuns.update`  
Delete a backup | `backups.deleteBackup` | `cloudsql.backupRuns.delete`  
  
## List all backups for a deleted instance

You can see a list of all retained and final backups for a deleted instance for your Google Cloud console project. Backups include details such as the name of the backup, the instance it belonged to, the type of backup, and the time the instance was deleted. Since the name of a deleted instance can be reused after its been deleted, we recommend using the `instance deletion time` field to differentiate which instance a particular backup belongs to. For a live instance, this field is blank.

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. Select your instance's [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options): **standard tier** or **enhanced tier**.

  3. Click **Filter** , then **Instance status** , and select **Deleted instance**.

This page lists all deleted instances in your Google Cloud console project.

  4. Click the name of the deleted instance you want to view backups for.

This page lists all retained automed and on-demand backups, and the final backup, if available, for your deleted instance.




###  gcloud 

  1. To get a list of all backups that are associated with a Google Cloud project, use the [gcloud sql backups list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command:
         
         gcloud sql backups list
         --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
  2. To view details about a specific retained backup, use the [gcloud sql backups describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe) command:
         
         gcloud sql backups describe BACKUP_NAME
         --project=PROJECT_ID
         

Replace the following:

     * `BACKUP_NAME`: the name of your retained backup.
     * `PROJECT_ID`: the ID of your Google Cloud project.



###  REST v1 

**Get a list of all backups**

Use this example to get a list of all retained and final backups associated with a Google Cloud project. For a complete list of parameters for this call, see the [`Backups.ListBackups`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/ListBackups) page.

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
    

**View details for a backup**

Use this example to view the details of a retained or final backup. For a complete list of parameters for this call, see the [`backup.getBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1//backups/getBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "status": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
             }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "final backup",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
        }
    

###  REST v1beta4 

**Get a list of all retained backs**

Use this example to get a list of all retained and final backups associated Google Cloud project. For a complete list of parameters for this call, see the [`backups.listBackups`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/listBackups) page.

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
    

**View details for a retained backup**

Use this example to view the details of a retained or final backup. For a complete list of parameters for this call, see the [`backups.getBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/getBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "name": "projects/PROJECT_ID/backups/BACKUP_ID",
          "kind": "sql#backup",
          "status": "SUCCESSFUL",
          "backupInterval": {
                "startTime": "2020-01-21T11:25:33.858Z",
                "endTime": "2020-01-21T11:26:18.663Z",
             }
          "type": "FINAL",
          "instance": "INSTANCE_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "location": "us"
          "description": "final backup",
          "backupKind": "SNAPSHOT",
          "dataDiskSizeGB": "10",
          "expiryTime": "2020-01-30T11:26:18.663Z",
          "backup_run": "projects/PROJECT_ID/instances/INSTANCE_ID/backupRuns/BACKUP_RUN_ID",
          "satisfies_pzs": false,
          "satisfies_pzi": false
        }
    

## Update a retained or final backup after instance deletion

After you delete an instance, you can update the settings for any retained or final backups associated with that instance that are stored at the project level. Depending on the type of backup, the details you can update might be different.

You can update the description and the retention settings of a final backup taken prior to deleting your instance. However, for on-demand or automated backups that are retained after instance deletion, you can only update the description of for these backups. For retained backups, the retention settings are set based on the retention settings of the backups when the instance was live. For more information, see [Retain backups after instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#recovery-backups).

### Update a final backup

You can update the retention settings and the description of a final backup taken before an instance is deleted. To update the backup, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. Click the name of the deleted instance you want to view backups for.

You will see a list of all retained and final backups, and their details for the deleted instance.

  3. For the final backup you want to update, click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png), and then do the following:

     * If you want to edit the description of the final backup, click **Edit description**.

Enter the description in the **Describe this backup** field, then click **Update**.

     * If you want to edit the retention period for the final backup, click **Edit retention period**.

Select the date in the **Retain backup until** field. The retention period can range from 1 to 365 days after instance deletion. Once you select the date to retain the backup until, click **Update**.




###  gcloud 

You'll need the `backup-name` of the final backup you want to update. To get the `backup-name`, see List backups for a deleted instance.

To update the retention period or the description of a final backup, use the [gcloud sql backups patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/patch) command and specify either the `expiry-time` or the `ttl-days` for the backup:
    
    
    gcloud sql backups patch BACKUP_NAME
    --description=BACKUP_DESCRIPTION
    --expiry-time=EXPIRY_TIME | --ttl-days=TTL_DAYS
    

Replace the following:

  * `BACKUP_NAME`: the name of the final backup.
  * `BACKUP_DESCRIPTION`: the new description you want to add to final backup.
  * One of the following:

    * `EXPIRY_TIME`: the new date and time for when you want the final backup to be deleted. The maximum time is 365 days from instance deletion.
    * `TTL_DAYS`: the number of days you want to retain your final backup. This can range from 1 to 365 days, where the default is 30 days.



###  REST v1 

You'll need the `backup-name` of the final backup you want to update. To get the `backup-name`, see List backups for a deleted instance.

You can update the description and the retention settings for the final backup. The retention setting can be updated using one of the following methods:

  * Update the retention days for the final backup
  * Update the expiration time for the final backup



**Update the retention period using retention days**

Use this example to update the retention setting of the final backup using the retention days parameter:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * TTL_DAYS: the retention period of the final backup (from 1 to 365 days). This is known as _time to live (TTL)_. The retention period starts from the current date and time, and the maximum retention period that Cloud SQL allows is 1 year (or 365 days).



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days

Request JSON body: 
    
    
    {
            "backup": {
                expiration: {
                "ttl_days": TTL_DAYS,
                }
             },
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

**Update the retention period using expiration time**

Use this example to update the retention setting of the final backup using the expiration time parameter:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DATE_AND_TIME_STAMP: a date-and-time stamp of when Cloud SQL deletes the final backup automatically.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time

Request JSON body: 
    
    
    {
            "backup": {
                expiration: {
                "expiry_time": DATE_AND_TIME_STAMP,
                }
             },
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

**Update the description**

Use this example to update the description of the final backup. For a complete list of parameters for this call, see the [`Backups.UpdateBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/UpdateBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DESCRIPTION: the updated description for the final backup.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description

Request JSON body: 
    
    
    {
            "backup": {
                "description": DESCRIPTION,
             },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

You'll need the `backup-name` of the final backup you want to update. To get the `backup-name`, see List backups for a deleted instance.

You can update the description and the retention settings for the final backup. The retention setting can be updated using one of the following methods:

  * Update the retention days for the final backup
  * Update the expiration time for the final backup



**Update the retention period using retention days**

Use this example to update the retention setting of the final backup using the retention days parameter:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * TTL_DAYS: the retention period of the final backup (from 1 to 365 days). This is known as _time to live (TTL)_. The retention period starts from the current date and time, and the maximum retention period that Cloud SQL allows is 1 year (or 365 days).



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days

Request JSON body: 
    
    
    {
            "backup": {
                expiration: {
                "ttl_days": TTL_DAYS,
                }
             },
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=ttl_days" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

**Update the retention period using expiration time**

Use this example to update the retention setting of the final backup using the expiration time parameter:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DATE_AND_TIME_STAMP: a date-and-time stamp of when Cloud SQL deletes the final backup automatically.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time

Request JSON body: 
    
    
    {
            "backup": {
                expiration: {
                "expiry_time": DATE_AND_TIME_STAMP,
                }
             },
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=expiry_time" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

**Update the description**

Use this example to update the description of the final backup. For a complete list of parameters for this call, see the [`backups.updateBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/updateBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DESCRIPTION: the updated description for the final backup.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description

Request JSON body: 
    
    
    {
            "backup": {
                "description": DESCRIPTION,
             },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

### Update a retained backup

You can update the description of retained on-demand and automated backups. To update the backup, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. Click the name of the deleted instance you want to view backups for.

You will see a list of all retained and final backups, and their details for the deleted instance.

  3. For the retained backup you want to update, click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png), and then select **Edit description**.

  4. In the **Edit Backup Description** window, update the description for your backup.

  5. Click **Update**.




###  gcloud 

To update the description of your retained backup, use the [gcloud sql backups patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/patch) command:
    
    
    gcloud sql backups patch BACKUP_NAME
    --description=BACKUP_DESCRIPTION
    

Replace the following:

  * `BACKUP_NAME`: the name of your retained backup.
  * `BACKUP_DESCRIPTION`: the new description you want to add to your retained backup.



###  REST v1 

**Get a list of all retained backs**

Use this example to get a list of all retained backups associated with a Google Cloud project. For a complete list of parameters for this call, see the [`Backups.ListBackups`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/ListBackups) page.

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
    

**Update the description**

Use this example to update the description of the retained backup. For a complete list of parameters for this call, see the [`Backups.UpdateBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/UpdateBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DESCRIPTION: the updated description for the final backup.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description

Request JSON body: 
    
    
    {
            "backup": {
                "description": DESCRIPTION,
             },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

**Get a list of all retained backs**

Use this example to get a list of all retained backups associated with a Google Cloud project. For a complete list of parameters for this call, see the [`backups.listBackups`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/listBackups) page.

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
    

**Update the description**

Use this example to update the description of the retained backup. For a complete list of parameters for this call, see the [`backups.updateBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/updateBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.
  * DESCRIPTION: the updated description for the final backup.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description

Request JSON body: 
    
    
    {
            "backup": {
                "description": DESCRIPTION,
             },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID?update_mask=description" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
          "kind": "sql#operation",
          "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
          "status": "DONE",
          "user": "user@example.com",
          "insertTime": "2024-02-15T00:10:22.078Z",
          "operationType": "UPDATE_BACKUP",
          "name": "OPERATION_ID",
          "targetId": "BACKUP_ID",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
          "targetProject": "PROJECT_ID"
    }
    

## Delete a backup associated with a deleted instance

You can delete a final or retained on-demand and automated backup for a deleted instance at any time.

**Note:** Once you manually delete a retained or final backup, it can't be recovered.

###  Console 

  1. In the Google Cloud console, go to the **Cloud SQL Backups** page.

[Go to Cloud SQL Backups](https://console.cloud.google.com/sql/backups)

  2. Click the name of the deleted instance you want to view backups for.

You will see a list of all retained and final backups, and their details for the deleted instance.

  3. For the backup you want to delete, click more actions ![More actions icon.](https://docs.cloud.google.com/static/sql/images/more-actions.png), and then select **Delete**.

  4. In the **Delete backup** window, enter the name of deleted instance, and then click **Delete**.




###  gcloud 

To delete a retained backup, use the [`gcloud sql backups delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/list) command:
    
    
    gcloud sql backups delete BACKUP_NAME
    

Replace the following:

  * `BACKUP_NAME`: the name of your retained backup.



###  REST v1 

Use this example to delete a final or retained backup. For a complete list of parameters for this call, see the [`Backups.DeleteBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/DeleteBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/backups/BACKUP_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "BACKUP_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

###  REST v1beta4 

Use this example to delete a final or retained backup. For a complete list of parameters for this call, see the [`backups.deleteBackup`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta/backups/deleteBackup) page.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * BACKUP_ID: the backup ID. You obtain this ID from the output of running the previous call.



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/backups/BACKUP_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "DELETE_BACKUP",
      "name": "OPERATION_ID",
      "targetId": "BACKUP_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## What's next

  * [Learn more about backing up your data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).
  * [Learn more about restoring data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).
  * [See how to restore your data from a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
