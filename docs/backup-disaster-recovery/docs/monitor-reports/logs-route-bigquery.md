---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery/
title: Set up prebuilt reports in BigQuery in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:46.266801+00:00
---

# Set up prebuilt reports in BigQuery in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Set up prebuilt reports in BigQuery in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up and view prebuilt reports in BigQuery in the appliance management console. These reports are created using logs from Cloud Logging. To set up reports, you need to do a one-time activity of creating a log [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) to stream logging data into BigQuery and then execute the prebuilt script.

## Required IAM role

The following IAM permissions are required to view prebuilt reports in BigQuery. Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

**Role** | **When to grant the role**  
---|---  
Logs Configuration Writer (`roles/logging.configWriter`)   
or   
Logging Admin (`roles/logging.admin`) and BigQuery Data Editor (`roles/bigquery.dataEditor`) | To create a sink and BigQuery dataset from the Google Cloud console.  
Owner (`roles/owner`) | To create a sink and BigQuery dataset from the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).  
BigQuery Admin (`bigquery.admin`) | To write custom queries or download queries.  
  
## Create a sink and route logs to BigQuery

BigQuery stores only the logs that are generated after a log sink is created. The logs that are generated before creating a log sink are not visible in BigQuery. You can create the log sink from the Google Cloud console or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To create sink and route logs in BigQuery, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to Log Router page](https://console.cloud.google.com/logs/router)

  2. Select an existing Google Cloud project.
  3. Click **Create sink**.
  4. In the **Sink details** panel, enter the following fields: 
     1. **Sink name** : enter the sink name as `BackupandDR_reports_sink`. You must use the sink name `BackupandDR_reports_sink` for the identification of Backup and DR reports from other sinks. 
     2. **Sink description** : Describe the purpose or use case for the sink.
  5. In the **Sink destination** panel, do the following:

     1. In the **Select sink service** menu, select the **BigQuery dataset** sink service.
     2. In the **Select BigQuery dataset** , select **Create new BigQuery dataset**.
     3. On the **Create dataset** page, do the following: 
        1. For **Dataset ID** , enter the dataset name as `BackupandDR_reports` to identify from other datasets. Don't change the dataset name from `BackupandDR_reports`.
        2. For **Location type** , choose a geographic [location](https://docs.cloud.google.com/bigquery/docs/locations) for the dataset. After a dataset is created, the location can't be changed.
        3. Optional: If you want tables in this dataset to expire, select **Enable table expiration** , then specify the **Default maximum table age** in days.
        4. Click **Create dataset**.
  6. In the **Choose logs to include in sink** panel, do the following:

     1. In the **Build inclusion filter** field, enter the following filter expression that matches the log entries you want to include.
            
            logName=~"projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_*"
            

     2. To verify you entered the correct filter, select **Preview logs**. This opens the **Logs Explorer** in a new tab with the filter prepopulated.

  7. Optional: In the **Choose logs to filter out of sink** panel, do the following:

     1. In the **Exclusion filter name** field, enter a name.
     2. In the **Build an exclusion filter** field, enter a [filter expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries you want to exclude. You can also use the [sample function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude.

**Note:** If you want your exclusion filter to be disabled when the sink is created, then select **Disable** after you enter your filter expression. You can update the sink later to enable the exclusion filter.
  8. Select **Create sink**.

You can see the dataset in the **BigQuery Studio**.




###  gcloud 

  1. Go to **Activate cloud shell** and click **Open editor**.
  2. Click the menuicon, select **File** , and then select **New text file**.
  3. Copy and paste the following script.
         
         #!/bin/bash
           echo "This script will set up a log sink for BackupDR reports to be available in BigQuery"
         
           # Get the default project ID
           DEFAULT_PROJECT_ID=$(gcloud config get-value project)
           read -p "Enter Project ID (default: $DEFAULT_PROJECT_ID, press Enter to continue):" PROJECT_ID
         
           # Use default if no input is provided
           if [ -z "$PROJECT_ID" ]; then
             PROJECT_ID=$DEFAULT_PROJECT_ID
           fi
             # Set the project ID
           result=$(gcloud config set project $PROJECT_ID)
           if [ $? -ne 0 ]; then
             echo "Error setting the project to $PROJECT_ID"
             exit 1
           fi
             # --- Check if BigQuery API is already enabled, enable if not ---
           echo "Checking if BigQuery API is enabled..."
           if gcloud services list | grep "bigquery.googleapis.com" >/dev/null; then
             echo "BigQuery API is already enabled for $PROJECT_ID"
           else
             echo "For logs to be available in BigQuery, we need to enable BigQuery service in the project if not done already. This might mean additional costs incurred. Please check the pricing at https://cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview#pricing before proceeding."
             read -p "Do you want to continue(Y/N)?" continue
             if [ "$continue" = "y" ] || [ "$continue" = "Y" ]; then
               echo "Enabling BigQuery API..."
               result=$(gcloud services enable bigquery.googleapis.com --project $PROJECT_ID)
               if [ $? -eq 0 ]; then
                 echo "Successfully enabled BigQuery api for $PROJECT_ID"
               else
                 echo "Error in setting up the BigQuery api for the project. $result"
                 exit 1
               fi
             else
               exit 0
             fi
           fi
             # --- Check if BigQuery data set already exists, create if not ---
           echo "Checking if BigQuery data set exists..."
           if bq ls | grep "BackupandDR_reports" >/dev/null; then
             echo "Dataset BackupandDR_reports already exists for $PROJECT_ID"
           else
             echo "Creating bigQuery dataset BackupandDR_reports..."
             # --- Get dataset location from user (default: US) ---
             read -p "Enter dataset location (default: US, press Enter to use): " DATASET_LOCATION
             if [ -z "$DATASET_LOCATION" ]; then
               DATASET_LOCATION="US"
             fi
             # --- Get table expiration in days from user (default: no expiration) ---
             read -p "Enter default table expiration in days (default: no expiration, press Enter to skip): " TABLE_EXPIRATION_DAYS
         
             # Calculate table expiration in seconds if provided
             if [ -n "$TABLE_EXPIRATION_DAYS" ]; then
               TABLE_EXPIRATION_SECONDS=$((TABLE_EXPIRATION_DAYS * 24 * 60 * 60))
               EXPIRATION_FLAG="--default_table_expiration $TABLE_EXPIRATION_SECONDS"
             else
               EXPIRATION_FLAG=""
             fi
             result=$(bq --location=$DATASET_LOCATION mk $EXPIRATION_FLAG BackupandDR_reports)
             if [ $? -eq 0 ]; then
               echo "Created a BigQuery dataset BackupandDR_reports successfully."
             else
               echo ""
               echo "ERROR : Failed to create the BigQuery dataset."
               echo $result
               exit 1
             fi
           fi
             # --- Check if Log Sink already exists, create if not ---
           echo "Checking if Log Sink exists..."
           if gcloud logging sinks list | grep "BackupandDR_reports_sink" >/dev/null; then
             echo "Log Sink BackupandDR_reports_sink already exists for $PROJECT_ID"
           else
             log_filter="projects/$PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_*"
             echo "Creating log sink BackupandDR_reports_sink..."
             result=$(gcloud logging sinks create BackupandDR_reports_sink bigquery.googleapis.com/projects/$PROJECT_ID/datasets/BackupandDR_reports --log-filter="logName=~\"$log_filter\"")
             if [ $? -eq 0 ]; then
               echo "Created a logsink BackupandDR_reports_sink successfully."
             else
               echo ""
               echo "ERROR : Failed to create logsink."
               exit 1
             fi
           fi
         
           # --- Add IAM Policy binding for Cloud logging service account to write logs to BigQuery ---
           result=$(gcloud projects add-iam-policy-binding $(gcloud projects describe $PROJECT_ID --format="value(projectNumber)") --member=serviceAccount:service-$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")@gcp-sa-logging.iam.gserviceaccount.com --role=roles/bigquery.dataEditor --condition=None)
           if [ $? -eq 0 ]; then
             echo "Added permission for cloud logging to write to BigQuery datasets"
           else
             echo ""
             echo "ERROR : Failed to add permissions for cloud logging to write to BigQuery datasets. Please make sure that you have correct access rights in order to be able to proceed."
             exit 1
           fi
         
           echo "Setup complete. The logs for the project $PROJECT_ID will now start flowing to bigquery."
           exit 0
         

  4. Save the file with a name with a Bash file extension, for example, `script.sh`.

  5. Run the command bash using the file you just created. For example, `bash script.sh`.

You can see the created dataset in the **BigQuery Studio**.




**Note:** Typically, log entries are visible in BigQuery within one minute. However, when a sink is created, it might take up to sixty minutes before the log data is available in BigQuery.

## Set up prebuilt reports

You can set up prebuilt reports by executing the following script within the dataset where the logs are being routed through the log sink.

The script adds the following prebuilt reports:

  * [Backup and Recovery job reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-recovery-reports)
  * [Daily Schedule Compliance reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery)
  * [Protected Resource reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-reports)
  * [Storage Resource Utilization reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-reports-bigquery)
  * [Mounted Image reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-reports-bigquery)
  * [Unprotected Resource reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-reports)
  * [Connector Version reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-reports-bigquery)
  * [Backup Policy Detail reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-logs)

**Note:** Depending on the log category, logs are generated at a frequency of zero to eight hours. To ensure successful execution of the script, it is recommended that you run the script at least eight hours after creating the sink.

To set up prebuilt reports in BigQuery, do the following:

###  gcloud 

  1. Go to **Activate cloud shell** and click **Open editor**.
  2. Create a new text file.
  3. Copy and paste the following prebuilt reports script into the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).
         
         backup_job_summary_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_recovery_jobs_*`
           WHERE DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) >= DATE_SUB(CURRENT_DATE(), INTERVAL 29 DAY) AND
           DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) < CURRENT_DATE() + 1
           GROUP BY insertId
           )
           SELECT
           DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) as Date,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.job_type as Job_Type,
           COUNT(CASE WHEN jsonPayload.job_status = "succeeded" THEN 1 END)/COUNT(*) * 100 as Success_Percent,
           COUNT(*) as Total_Jobs,
           COUNT(CASE WHEN jsonPayload.job_status = "succeeded" THEN 1 END) as Succeeded,
           COUNT(CASE WHEN jsonPayload.job_status = "failed" THEN 1 END) as Failed,
           COUNT(CASE WHEN jsonPayload.job_status = "canceled" THEN 1 END) as Cancelled,
           COUNT(CASE WHEN jsonPayload.job_status = "notrun" THEN 1 END) as Not_Run,
           FROM filtered_data
           WHERE jsonPayload.job_category = "Backup Job" AND
           jsonPayload.job_status != "retry"
           GROUP BY Date, jsonPayload.job_type, jsonPayload.resource_id, jsonPayload.resource_name, jsonPayload.resource_type
           ORDER BY  Date, Resource_Name;'
         
           recovery_job_summary_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_recovery_jobs_*`
           WHERE DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) >= DATE_SUB(CURRENT_DATE(), INTERVAL 29 DAY) AND
           DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) < CURRENT_DATE() + 1
           GROUP BY insertId
           )
           SELECT
           DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) as Date,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.job_type as Job_Type,
           COUNT(CASE WHEN jsonPayload.job_status = "succeeded" THEN 1 END)/COUNT(*) * 100 as Success_Percent,
           COUNT(*) as Total_Jobs,
           COUNT(CASE WHEN jsonPayload.job_status = "succeeded" THEN 1 END) as Succeeded,
           COUNT(CASE WHEN jsonPayload.job_status = "failed" THEN 1 END) as Failed,
           COUNT(CASE WHEN jsonPayload.job_status = "canceled" THEN 1 END) as Cancelled,
           COUNT(CASE WHEN jsonPayload.job_status = "notrun" THEN 1 END) as Not_Run,
           FROM filtered_data
           WHERE jsonPayload.job_category = "Recovery Job" AND
           jsonPayload.job_status != "retry"
           GROUP BY Date, jsonPayload.job_type, jsonPayload.resource_id, jsonPayload.resource_name, jsonPayload.resource_type
           ORDER BY Date, Resource_Name;'
         
           failed_job_query='WITH filtered_data AS (
           SELECT insertId, ANY_VALUE(jsonPayload) as jsonPayload
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_recovery_jobs_*`
           GROUP BY insertId
           )
           SELECT
           jsonPayload.job_name as Job_Name,
           jsonPayload.job_category as Job_Category,
           jsonPayload.job_type as Job_Type,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.error_code as Error_Code,
           jsonPayload.error_message as Error_Message,
           jsonPayload.hostname as Host_Name,
           jsonPayload.backup_rule_policy_name as Backup_Rule_Policy_Name,
           jsonPayload.backup_plan_policy_template as Backup_Plan_Policy_Template,
           jsonPayload.appliance_name as Appliance_Name,
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(jsonPayload.job_start_time)) as Job_Start_Time,
           DATE(jsonPayload.job_start_time) as Job_Date,
           jsonPayload.backup_type as Backup_Type
           FROM filtered_data
           WHERE
           jsonPayload.job_status = "failed"
           ORDER BY Job_Start_Time DESC, Resource_Name'
         
           job_details_query='WITH filtered_data AS (
           SELECT insertId, ANY_VALUE(jsonPayload) as jsonPayload
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_recovery_jobs_*`
           GROUP BY insertId
           )
           SELECT
           jsonPayload.job_name as Job_Name,
           jsonPayload.job_category as Job_Category,
           jsonPayload.job_type as Job_Type,
           jsonPayload.log_backup as Log_Backup,
           jsonPayload.job_status as Job_Status,
           DATE(CASE WHEN jsonPayload.job_start_time = "" THEN jsonPayload.job_queued_time ELSE jsonPayload.job_start_time END) as Job_Date,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.error_code as Error_Code,
           jsonPayload.error_message as Error_Message,
           jsonPayload.job_initiation_failure_reason as Job_Initiation_Failure_Reason,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.hostname as Host_Name,
           jsonPayload.target_appliance_name as Target_Appliance_Name,
           jsonPayload.target_pool_name as Target_Pool_Name,
           jsonPayload.target_host_name as Target_Host_Name,
           jsonPayload.backup_plan_policy_template as Backup_Plan_Policy_Template,
           jsonPayload.backup_rule_policy_name as Backup_Rule_Policy_Name,
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(CASE WHEN jsonPayload.job_queued_time !="" THEN jsonPayload.job_queued_time ELSE NULL END))  as Job_Queue_Time,
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(CASE WHEN jsonPayload.job_start_time!="" THEN jsonPayload.job_start_time ELSE NULL END))  as Job_Start_Time,
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(CASE WHEN jsonPayload.job_end_time!="" THEN jsonPayload.job_end_time ELSE NULL END))  as Job_End_Time,
           jsonPayload.job_duration_in_hours as Job_Duration_In_Hours,
           jsonPayload.backup_consistency as Backup_Consistency,
           jsonPayload.resource_data_size_in_gib as Resource_Data_Size_In_GiB,
           jsonPayload.snapshot_disk_size_in_gib as Snapshot_Disk_Size_in_GiB,
           jsonPayload.pre_compress_in_gib as Pre_Compress_In_GiB,
           jsonPayload.compression_ratio as Compression_Ratio,
           jsonPayload.data_sent_in_gib as Streamsnap_Data_Sent_In_GiB,
           jsonPayload.data_written_in_gib as Streamsnap_Data_Written_In_GiB,
           jsonPayload.data_copied_in_gib as Data_Copied_In_GiB,
           jsonPayload.data_change_rate as Data_Change_Rate_Percent,
           jsonPayload.backup_type as Backup_Type,
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(CASE WHEN jsonPayload.recovery_point!="" THEN jsonPayload.recovery_point ELSE NULL END))  as Recovery_Point,
           jsonPayload.onvault_pool_storage_consumed_in_gib as OnVault_Pool_Storage_Consumed_In_GiB,
           FROM filtered_data
           ORDER BY Job_Start_Time DESC, Resource_Name'
         
           unresolved_failures_query='WITH job_data AS (
           SELECT insertId, ANY_VALUE(jsonPayload) as jsonPayload
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_recovery_jobs_*`
           WHERE
           jsonPayload.job_status in ("succeeded", "failed")
           GROUP BY insertId
           ),
           -- Select resources which have their latest status as failed
           unresolved_failed_resources AS (
           SELECT
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.job_type as Job_Type,
           jsonPayload.job_status as Job_Status,
           jsonPayload.job_start_time as Job_Start_Time,
           jsonPayload.hostname as Hostname,
           jsonPayload.error_code as Error_Code,
           jsonPayload.error_message as Error_Message
           FROM job_data j1
           WHERE jsonPayload.job_start_time = (SELECT MAX(jsonPayload.job_start_time) FROM job_data j2 WHERE j1.jsonPayload.appliance_name = j2.jsonPayload.appliance_name AND j1.jsonPayload.resource_name = j2.jsonPayload.resource_name AND j1.jsonPayload.resource_type = j2.jsonPayload.resource_type AND j1.jsonPayload.job_type = j2.jsonPayload.job_type) AND
           jsonPayload.job_status = "failed"
           ),
           -- Select all jobs for all the resources that have unresolved failures
           all_jobs_of_unresolved_failure_resources AS (
           SELECT
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.job_type as Job_Type,
           jsonPayload.job_category as Job_Category,
           jsonPayload.job_name as Job_Name,
           jsonPayload.recovery_point as Recovery_Point,
           jsonPayload.job_status as Job_Status,
           jsonPayload.job_start_time as Job_Start_Time,
           jsonPayload.hostname as Hostname,
           jsonPayload.error_code as Error_Code
           FROM job_data j1
           JOIN unresolved_failed_resources fr
           ON
           j1.jsonPayload.appliance_name = fr.Appliance_Name AND
           j1.jsonPayload.resource_name = fr.Resource_Name AND
           j1.jsonPayload.resource_type = fr.Resource_Type AND
           j1.jsonPayload.job_type = fr.Job_Type
           ),
           -- Select the latest successful jobs for the resources with unresolved failures
           latest_success AS (
           SELECT *
           FROM all_jobs_of_unresolved_failure_resources all_jobs
           WHERE
           all_jobs.Job_Status = "succeeded" AND
           all_jobs.Job_Start_Time = (
             SELECT MAX(Job_Start_Time) FROM
             all_jobs_of_unresolved_failure_resources all_jobs_2
             WHERE all_jobs_2.Appliance_Name = all_jobs.Appliance_Name AND
             all_jobs_2.Resource_Name = all_jobs.Resource_Name AND
             all_jobs_2.Resource_Type = all_jobs.Resource_Type AND
             all_jobs_2.Job_Type = all_jobs.Job_Type AND
             all_jobs_2.job_status = "succeeded"
             )
           ),
           -- Select all failed jobs after the last success for the resources with unresolved failures
           failed_jobs_to_report AS (
           SELECT
           all_jobs.Appliance_Name as Appliance_Name,
           all_jobs.Resource_Name as Resource_Name,
           all_jobs.Resource_Type as Resource_Type,
           all_jobs.Job_Type as Job_Type,
           all_jobs.Job_Name as Job_Name,
           all_jobs.Recovery_Point as Recovery_Point,
           all_jobs.Job_Status as Job_Status,
           all_jobs.Job_Start_Time as Job_Start_Time,
           all_jobs.Hostname as Hostname,
           all_jobs.Error_Code as Error_Code,
           all_jobs.Job_Category as Job_Category,
           FROM all_jobs_of_unresolved_failure_resources all_jobs
           LEFT JOIN latest_success success
           ON success.Appliance_Name = all_jobs.Appliance_Name AND
             success.Resource_Name = all_jobs.Resource_Name AND
             success.Resource_Type = all_jobs.Resource_Type AND
             success.Job_Type = all_jobs.Job_Type
           WHERE all_jobs.Job_Status = "failed" AND
           TIMESTAMP(all_jobs.Job_Start_Time) > COALESCE(TIMESTAMP(success.Job_Start_Time), TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY)))
           )
           SELECT
           failed_jobs.Resource_Name,
           failed_jobs.Resource_Type,
           failed_jobs.Job_Type,
           failed_jobs.Job_Category,
           COUNT(*) as Error_Count,
           failed_jobs.Error_Code,
           ANY_VALUE(ufr.Error_Message) as Error_Message,
           FORMAT_TIMESTAMP("%F %R %Z", MIN(TIMESTAMP(failed_jobs.Job_Start_Time))) as First_Failure,
           FORMAT_TIMESTAMP("%F %R %Z", MAX(TIMESTAMP(failed_jobs.Job_Start_Time))) as Last_Failure,
           TIMESTAMP_DIFF(CURRENT_TIMESTAMP,TIMESTAMP(MAX(failed_jobs.Job_Start_Time)), HOUR) as Hours_Since_Last_Failure,
           failed_jobs.Appliance_Name
           FROM failed_jobs_to_report failed_jobs
           LEFT JOIN unresolved_failed_resources ufr
           ON failed_jobs.Appliance_Name = ufr.Appliance_Name AND
             failed_jobs.Resource_Name = ufr.Resource_Name AND
             failed_jobs.Resource_Type = ufr.Resource_Type AND
             failed_jobs.Job_Type = ufr.Job_Type AND
             failed_jobs.Error_Code = ufr.Error_Code
           GROUP BY Appliance_Name, Resource_Name, Resource_Type, Job_Type, Job_Category, Error_Code
           ORDER BY Last_Failure DESC
           '
           daily_schedule_compliance_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_daily_schedule_compliance_*`
           WHERE DATE(jsonPayload.date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY) AND
           DATE(jsonPayload.date) < CURRENT_DATE() + 1
           GROUP BY insertId
           )
           SELECT
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.backup_rule_policy_name as Backup_Rule_Policy_Name,
           jsonPayload.backup_plan_policy_template as Backup_Plan_Policy_Template,
           DATE(jsonPayload.date) as Date,
           jsonPayload.backup_window_start_time as Backup_Window_Start_Time,
           jsonPayload.job_type as Job_Type,
           jsonPayload.status as Status,
           jsonPayload.comment as Comment,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.host_name as Host_Name
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Resource_Name, Date;
           '
           protected_data_resource_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_protected_resource_*`
           GROUP BY insertId
           )
           SELECT
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.host_name as Host_Name,
           jsonPayload.backup_plan_policy_template as Backup_Plan_Policy_Template,
           jsonPayload.protected_on as Protected_On,
           jsonPayload.recovery_point as Recovery_Point,
           jsonPayload.protected_data_in_gib as Protected_Data_in_Gib,
           jsonPayload.onvault_in_gib as OnVault_Data_in_Gib,
           jsonPayload.backup_plan_restrictions as Backup_Plan_Restrictions,
           jsonPayload.backup_inclusion_or_exclusion as Backup_Inclusion_or_Exclusion,
           jsonPayload.policy_overrides as Policy_Overrides,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.remote_appliance as Remote_Appliance,
           jsonPayload.source_appliance as Source_Appliance,
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Resource_Name;'
         
           storage_utilization_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_storage_utilization_*`
           GROUP BY insertId
           )
           SELECT
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.pool_name as Pool_Name,
           jsonPayload.storage_type as Storage_Type,
           jsonPayload.total_capacity_in_gib as Total_Capacity_In_GiB,
           jsonPayload.used_capacity_in_gib as Used_Capacity_In_GiB,
           jsonPayload.utilization_percentage as Utilization_percentage,
           jsonPayload.appliance_id as Appliance_id,
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Appliance_Name;'
         
           mounted_image_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_mounted_images_*`
           GROUP BY insertId
           )
           SELECT
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
           jsonPayload.source_resource_name as Source_Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.mounted_image_name as Mounted_Image_Name,
           jsonPayload.source_image_name as Source_Image_Name,
           jsonPayload.source_image_type as Source_Image_Type,
           jsonPayload.recovery_point_date as Recovery_Point_Date,
           jsonPayload.last_mount_date as Last_Mount_Date,
           jsonPayload.source_host_name as Source_Host_Name,
           jsonPayload.mounted_host_name as Mounted_Host_Name,
           jsonPayload.mounted_resource_name as Mounted_Resource_Name,
           jsonPayload.resource_virtual_size_in_gib as Resource_Virtual_Size_In_Gib,
           jsonPayload.storage_consumed_in_gib as Storage_Consumed_In_Gib,
           jsonPayload.mounted_resource_label as Mounted_Resource_Label,
           jsonPayload.restorable_object as Restorable_Object,
           jsonPayload.mounted_image_age_in_days as Mounted_Image_Age_In_Days,
           jsonPayload.user_name as User_Name,
           jsonPayload.read_mode as Read_Mode,
           jsonPayload.resource_size_in_gib as Resource_Size_In_Gib,
           jsonPayload.source_image_expiration_date as Source_Image_Expiration_Date,
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Mounted_Resource_Name;'
         
           unprotected_resource_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_unprotected_resource_*`
           GROUP BY insertId
           )
           SELECT
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
           jsonPayload.resource_name as Resource_Name,
           jsonPayload.resource_type as Resource_Type,
           jsonPayload.host_name as Host_Name,
           jsonPayload.instance_name as Instance_Name,
           jsonPayload.discovered_on as Discovered_On,
           jsonPayload.discovered_by as Discovery_Appliance,
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Resource_Name;'
         
           connector_version_query='WITH filtered_data AS (
           SELECT
           insertId,
           ANY_VALUE(jsonPayload) as jsonPayload,
           ANY_VALUE(timestamp) as Report_Timestamp
           FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_connector_version_*`
           GROUP BY insertId
           )
           SELECT
           FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
           jsonPayload.appliance_name as Appliance_Name,
           jsonPayload.host_name as Host_Name,
           jsonPayload.host_os_type as Host_OS_Type,
           jsonPayload.host_ip_address as Host_IP_Address,
           jsonPayload.db_authentication as DB_Authentication,
           jsonPayload.installed_version as Installed_Version,
           jsonPayload.available_version as Available_Version,
           jsonPayload.version_check as Version_Check,
           jsonPayload.disk_preference as Disk_Preference,
           jsonPayload.transport as Transport,
           FROM filtered_data f1
           WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id)
           ORDER BY Host_Name;'
         
           backup_policy_details_query='WITH filtered_data AS (
             SELECT
             insertId,
             ANY_VALUE(jsonPayload) as jsonPayload,
             ANY_VALUE(timestamp) as Report_Timestamp
             FROM `PROJECT_ID.DATASET_NAME.backupdr_googleapis_com_gcb_backup_rule_policy_details_*`
             GROUP BY insertId
             )
             SELECT
             FORMAT_TIMESTAMP("%F %R %Z", TIMESTAMP(Report_Timestamp)) as Last_updated_on,
             jsonPayload.backup_plan_policy_template as Backup_Template,
             jsonPayload.backup_rule_policy_name as Backup_Policy_Name,
             jsonPayload.backup_rule_policy_type as Backup_Policy_Type,
             jsonPayload.backup_schedule_type as Backup_Schedule_Type,
             jsonPayload.backup_window_start_time as Backup_Window_Start_Time,
             jsonPayload.backup_window_end_time as Backup_Window_End_Time,
             jsonPayload.backup_frequency_in_days as Backup_Frequency_In_Days,
             CASE WHEN jsonPayload.backup_consistency = "Crash Consistency Backup" THEN "Crash Consistent Backup"
             WHEN jsonPayload.backup_consistency = "Application Consistency Backup" THEN "Application Consistent Backup"
             ELSE jsonPayload.backup_consistency
             END as Backup_Consistency,
             jsonPayload.log_backup_frequency_in_minutes as Log_Backup_Frequency_In_Minutes,
             jsonPayload.backup_retention_period_in_days as Backup_Retention_Period_In_Days,
             jsonPayload.protected_resources_count as Protected_Resources_Count,
             jsonPayload.schedule_disabled_resources_count as Schedule_Disabled_Resources_Count,
             jsonPayload.appliance_name as Appliance_Name,
             FROM filtered_data f1
             WHERE Report_Timestamp = (SELECT MAX(Report_Timestamp) FROM filtered_data f2 WHERE f2.jsonPayload.appliance_id = f1.jsonPayload.appliance_id);' 
         
           table_not_exists_error_flag=false
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_backup_recovery_jobs%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$backup_job_summary_query" DATASET_NAME.'Backup Jobs Summary')
         
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$backup_job_summary_query" DATASET_NAME.'Backup Jobs Summary'
           else
           echo $result
           fi
         
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$recovery_job_summary_query" DATASET_NAME.'Recovery Jobs Summary')
         
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$recovery_job_summary_query" DATASET_NAME.'Recovery Jobs Summary'
           else
           echo $result
           fi
         
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$failed_job_query" DATASET_NAME.'Failed Jobs')
         
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$failed_job_query" DATASET_NAME.'Failed Jobs'
           else
           echo $result
           fi
         
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$job_details_query" DATASET_NAME.'Job Details')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$job_details_query" DATASET_NAME.'Job Details'
           else
           echo $result
           fi
         
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$unresolved_failures_query" DATASET_NAME.'Unresolved Failures')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$unresolved_failures_query" DATASET_NAME.'Unresolved Failures'
           else
           echo $result
           fi
         
           else
           echo "The table backupdr_googleapis_com_gcb_backup_recovery_jobs does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_daily_schedule_compliance%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$daily_schedule_compliance_query" DATASET_NAME.'Daily Schedule Compliance')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$daily_schedule_compliance_query" DATASET_NAME.'Daily Schedule Compliance'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_daily_schedule_compliance does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_protected_resource%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$protected_data_resource_query" DATASET_NAME.'Protected Data Resource')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$protected_data_resource_query" DATASET_NAME.'Protected Data Resource'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_protected_resource does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_backup_storage_utilization%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$storage_utilization_query" DATASET_NAME.'Storage Resource Utilization')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$storage_utilization_query" DATASET_NAME.'Storage Resource Utilization'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_backup_storage_utilization does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_unprotected_resource%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$unprotected_resource_query" DATASET_NAME.'Unprotected Resource')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$unprotected_resource_query" DATASET_NAME.'Unprotected Resource'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_unprotected_resource does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_mounted_images%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$mounted_image_query" DATASET_NAME.'Mounted Image Details')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$mounted_image_query" DATASET_NAME.'Mounted Image Details'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_mounted_images does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           check_table=$(bq query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.TABLES WHERE table_name like '%backupdr_googleapis_com_gcb_connector_version%'" | tail -n +2 | tr -d ' ')
           if [ "$check_table" == 'true' ]; then
           result=$(bq update --use_legacy_sql=false --expiration 0 --view "$connector_version_query" DATASET_NAME.'Connector Version Details')
           if [ $? -ne 0 ]; then
           bq mk --use_legacy_sql=false --expiration 0 --view "$connector_version_query" DATASET_NAME.'Connector Version Details'
           else
           echo $result
           fi
           else
           echo "The table backupdr_googleapis_com_gcb_connector_version does not exist in the dataset DATASET_NAME."
           table_not_exists_error_flag=true
           fi
         
           if [ $table_not_exists_error_flag == true ]; then
           echo -e "\e[1m\e[33mAll the prebuilt reports could not be created successfully in BigQuery as one or more report logs are missing in the dataset DATASET_NAME."
           echo -e "Please ensure that you have waited for at least 8 hours after creating the sink, before running the script to create pre built reports. Try re-running the script again after some time to fix the issue."
           echo -e "Reach out to Google Cloud Support in case you are still facing this issue.\e[0m"
           fi
         
           # Check if view exists
           check_view=$(bq --project_id PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from DATASET_NAME.INFORMATION_SCHEMA.VIEWS WHERE table_name='Storage Resource Utilization'" | tail -n +2 | tr -d ' ')
           if [ "$check_view" == 'true' ]; then
             # Check if view is working correctly
             fetch_result=$(bq query --format=csv --use_legacy_sql=false "SELECT COUNT(*) FROM \`DATASET_NAME.Storage Resource Utilization\`" 2>&1)
             if [[ $? -eq 0 ]]; then
                 echo -e "\e[1m\e[33mTo fix a schema related error in the Backup Storage Utilization view, we updated the software on June 3rd, 2024. As part of the fix, storage utilization data before June 3rd 2024, will be no longer available in the report.\e[0m"
                 echo -e "Deleting the data before June 3rd 2024..."
                 start_date="20240301"
                 end_date="20240603"
                 current_date="$start_date"
                 while [ "$current_date" -le "$end_date" ]; do
                     table_name="DATASET_NAME.backupdr_googleapis_com_gcb_backup_storage_utilization_${current_date}"
                     bq rm -f -t "$table_name"
                     current_date=$(date -d "$(date -d "$current_date" +%Y-%m-%d) + 1 day" +%Y%m%d)
                 done
                 echo -e "Completed successfully."
             fi
           fi
         
         

Replace the following:

     * `PROJECT_ID`: the name of your project.
     * `DATASET_NAME`: the name of your BigQuery dataset. We recommend that you set the BigQuery dataset name for Backup and DR reports to the default dataset name, which is `BackupandDR_reports`. If you have set a different name than the default dataset name while creating the sink, change the dataset name to match your BigQuery dataset.
  4. Save the file with a name with a Bash file extension, for example, `backupdrreports.sh`.

  5. Run the command bash using the file you just created. For example, `bash backupdrreports.sh`.

You can see the prebuilt reports under the dataset in the **BigQuery Studio**.




After you [set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script), if you have access to Google Workspace, you can [view the results in Google connected sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets). If you don't have access to Google Workspace, you can [view the reports in Data Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio) or [download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download) in a CSV file.

## Pricing

You may be charged for viewing prebuilt reports in BigQuery. These charges are based on the volume of reporting data, that is streamed, stored, and queried in BigQuery. For the details, see [Pricing](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview#pricing).

## What's next

  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Google connected sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
