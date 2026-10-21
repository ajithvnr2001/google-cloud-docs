---
url: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/view-audit-logs-for-automated-backups/
title: View audit logs for automated backups \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:59.530315+00:00
---

# View audit logs for automated backups  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/view-audit-logs-for-automated-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  View audit logs for automated backups Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/view-audit-logs-for-automated-backups "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/view-audit-logs-for-automated-backups "View this page for the SQL Server database engine")

This page describes how to view an audit log for an automated backup of your Cloud SQL instance. 

You can use audit logs to do the following:

  * View an audit log to verify whether the backup is completed successfully.
  * Configure a log-based alert to notify you of the backup's status.



## View an audit log

You can use the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or API to view an audit log to verify whether a backup is completed successfully within a backup window.

### Console

  1. In the Google Cloud console, select **Logging** and then select **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. To filter for audit logs for automated backups of Cloud SQL instances, run the following query:
         
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.methodName="cloudsql.instances.automatedBackup"
         resource.type="cloudsql_database"

Replace PROJECT_ID with your Google Cloud project's ID.

The first expression filters for [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event). The second expression filters for audit logs for automated backups. The final expression filters for audit logs for Cloud SQL instances.

For more information about how to use the Google Cloud console to query for audit logs, see [View logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging#viewing_logs).

  3. View the status of a backup created during the backup window. This status is displayed in the `windowStatus` field. To view this field, complete the following steps:

     1. Click the audit log.
     2. Click the `metadata` field.



### gcloud

  1. To filter for audit logs for automated backups of Cloud SQL instances, run the following query:
         
         gcloud logging read \
         "logName=projects/PROJECT_NAME/logs/cloudaudit.googleapis.com%2Fsystem_event
         AND protoPayload.methodName=cloudsql.instances.automatedBackup AND
         resource.type=cloudsql_database" \ 
             --project=PROJECT_NAME

Replace PROJECT_NAME with your Google Cloud project's name.

The first expression filters for [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event). The second expression filters for audit logs for automated backups. The final expression filters for audit logs for Cloud SQL instances.

For more information about how to use `gcloud` to query for audit logs, see [View logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging#viewing_logs).

  2. View the status of a backup created during the backup window. This status is displayed in the `windowStatus` field.




### API

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The ID of your Google Cloud project.



For the request JSON body, the first expression filters for [ System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event). The second expression filters for audit logs for automated backups. The final expression filters for audit logs for Cloud SQL instances.

For more information about how to use the API to query for audit logs, see [View logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging#viewing_logs).

HTTP method and URL: 
    
    
    POST https://logging.googleapis.com/v2/entries:list

Request JSON body: 
    
    
    {
         "resourceNames": [
         "projects/PROJECT_ID"
          ],
         "pageSize": 5,
         "filter": "logName=projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event AND protoPayload.methodName = cloudsql.instances.automatedBackup AND resource.type=cloudsql_database",
         "orderBy": "timestamp desc"
    } 
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://logging.googleapis.com/v2/entries:list"

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
        -Uri "https://logging.googleapis.com/v2/entries:list" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "entries": [
        {
          "protoPayload": {
            "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
            "status": {
              "message": "OK"
            },
            "authenticationInfo": {},
            "requestMetadata": {
              "requestAttributes": {},
              "destinationAttributes": {}
            },
            "serviceName": "cloudsql.googleapis.com",
            "methodName": "cloudsql.instances.automatedBackup",
            "resourceName": "projects/PROJECT_ID/instances/INSTANCE_NAME",
            "metadata": {
              "windowStartTime": "2022-12-15T13:00:00Z",
              "message": "",
              **"windowStatus": "STATUS_SUCCEEDED",**
              "@type": "type.googleapis.com/speckle.AutomatedBackupEventLog",
              "windowEndTime": "2022-12-15T17:00:00Z",
              "backupCompletionTime": "2022-12-15T14:11:57.347Z",
              "backupStartTime": "2022-12-15T14:11:16.631Z"
            }
          },
          "insertId": "LOG_ENTRY_UNIQUE_IDENTIFIER",
          "resource": {
            "type": "cloudsql_database",
            "labels": {
              "region": "REGION_NAME",
              "project_id": "PROJECT_ID",
              "database_id": "DATABASE_ID"
            }
          },
          "timestamp": "2022-12-15T14:11:57.391565Z",
          "severity": "INFO",
          "logName": "projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event",
          "receiveTimestamp": "2022-12-15T14:11:57.785814800Z"
        },
     ],
    }
    

For more information about LOG_ENTRY_UNIQUE_IDENTIFIER for the `insertId` field, see [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

View the status of a backup created during the backup window. This status is displayed in the `windowStatus` field. 

### Automated backup statuses

  * `STATUS_SUCCEEDED`: The automated backup is completed successfully.
  * `STATUS_ATTEMPT_FAILED`: Cloud SQL tried to create the backup, but the backup either didn't start or it failed. Reasons for this status include:

    * Another backup is running on the instance.
    * The backup location is restricted by your organization policy.
    * The backup of the instance completed, but an error occurred.
    * The instance wasn't running when Cloud SQL tried to create the backup.
  * `STATUS_FAILED`: The automated backup of the instance either hasn't completed successfully or can't be completed within the backup window. 

For example, if you enabled automated backups and scheduled the backup window for between 1:00 am and 5:00 am, your backup might fail if you have many `EXPORT` operations during this time frame. Automated backups might also fail if there are too many conflicts with an `EXPORT` operation that runs for a long time. 

If Cloud SQL tries to create a backup multiple times during a backup window, but the backup can't be created for the reasons listed for `STATUS_ATTEMPT_FAILED`, Cloud SQL generates another audit log with the `windowStatus` field set to `STATUS_FAILED`.

  * `STATUS_SKIPPED`: The Cloud SQL instance [stopped running](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance) since the last successful backup. Therefore, a new automated backup wasn't created.




## Configure a log-based alert

You can [configure a log-based alert](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) to notify you of the backup's status. 

  * If a backup has a `STATUS_SUCCEEDED` status, you can be notified for tracking purposes.
  * If a backup has the `STATUS_FAILED` or `STATUS_ATTEMPT_FAILED` status, you can be notified to take corrective action, based on the message that appears in the log entry. You can also take an [on-demand backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up) before the next scheduled backup window.
  * If a backup has a `STATUS_SKIPPED` status, you can be notified to restart the Cloud SQL instance.



## What's next

  * [Learn more about backing up your data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups).
  * [Learn more about creating and managing backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up). 
  * [Learn more about restoring data](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).
  * [Learn more about point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr). 
  * [See how to restore your data from a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restoring#restorebackups).
  * [See how to perform a point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
