---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery/
title: Set up prebuilt backup plan based reports \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:00.949264+00:00
---

# Set up prebuilt backup plan based reports  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Set up prebuilt backup plan based reports Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to set up and view prebuilt reports in BigQuery for resources that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

To set up reports, you need to do a one-time activity of creating a log [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) to stream logging data into BigQuery and then execute the prebuilt script. If you want to set up and view prebuilt reports in BigQuery for the resources that are protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Set up prebuilt reports in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery).

## Required IAM role

The following IAM permissions are required to view prebuilt reports in BigQuery for vaulted backups. Learn how to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

**Role** | **When to grant the role**  
---|---  
Logs Configuration Writer (`roles/logging.configWriter`) or |   
  
Logging Admin (`roles/logging.admin`) and BigQuery Data Editor (`roles/bigquery.dataEditor`) | To create a sink and BigQuery dataset from the Google Cloud console. | | Owner (`roles/owner`) | To create a sink and BigQuery dataset from the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). | | BigQuery Admin (`bigquery.admin`) | To write custom queries or download queries. |

## Create a sink and route logs to BigQuery for vaulted backups

BigQuery stores only the logs that are generated after a log sink is created. The logs that are generated before creating a log sink are not visible in BigQuery. You can create the log sink from the Google Cloud console or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Before you begin

When configuring the BigQuery dataset sink service, ensure that the **Use partitioned tables** option in the log sink is unchecked.

**Caution:** The prebuilt reporting script requires logs to be routed into [date-sharded tables](https://docs.cloud.google.com/logging/docs/export/bigquery#partition-tables). Enabling partitioned tables will cause the reporting script to fail with an `8-hour wait` error.

To create sink and route logs in BigQuery for vaulted backups, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Log Router** page: 

[Go to Log Router page](https://console.cloud.google.com/logs/router)

  2. Select an existing Google Cloud project.
  3. Click **Create sink**.
  4. In the **Sink details** panel, enter the following fields: 
     1. **Sink name** : enter the sink name as `bdr_report_sink`. You must use the sink name `bdr_report_sink` for the identification of Backup and DR reports from other sinks.
     2. **Sink description** : Describe the purpose or use case for the sink.
  5. In the **Sink destination** panel, do the following:

     1. In the **Select sink service** menu, select the **BigQuery dataset** sink service.
     2. In the **Select BigQuery dataset** , select **Create new BigQuery dataset**.
     3. On the **Create dataset** page, do the following: 
        1. For **Dataset ID** , enter the dataset name as `bdr_reports` to identify from other datasets. Don't change the dataset name from `bdr_reports`.
        2. For **Location type** , choose a geographic [location](https://docs.cloud.google.com/bigquery/docs/locations) for the dataset. After a dataset is created, the location can't be changed.
        3. Optional: If you want tables in this dataset to expire, select **Enable table expiration** , then specify the **Default maximum table age** in days.
        4. Click **Create dataset**.
  6. In the **Choose logs to include in sink** panel, do the following:

     1. In the **Build inclusion filter** field, enter the following filter expression that matches the log entries you want to include.
            
            logName=~"projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fbdr_*" 
             Replace `PROJECT_ID` with the project name.
            

     2. To verify you entered the correct filter, select **Preview logs**. This opens the **Logs Explorer** in a new tab with the filter prepopulated.

  7. Optional: In the **Choose logs to filter out of sink** panel, do the following:

     1. In the **Exclusion filter name** field, enter a name.
     2. In the **Build an exclusion filter** field, enter a [filter expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language) that matches the log entries you want to exclude. You can also use the [sample function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions) to select a portion of the log entries to exclude.

**Note:** If you want your exclusion filter to be disabled when the sink is created, then select **Disable** after you enter your filter expression. You can update the sink later to enable the exclusion filter.
  8. Select **Create sink**.

You can see the dataset in the **BigQuery Studio**.




###  gcloud 

  1. Go to **Activate cloud shell** and click **Open editor**.
  2. Click the menu icon, select **File** , and then select **New text file**.
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
               echo "For logs to be available in BigQuery, we need to enable BigQuery service in the project if not done already. This might mean additional costs incurred. Please check the associated costs before proceeding."
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
             if bq ls | grep "bdr_reports" >/dev/null; then
               echo "Dataset bdr_reports already exists for $PROJECT_ID"
             else
               echo "Creating bigQuery dataset bdr_reports..."
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
               result=$(bq --location=$DATASET_LOCATION mk $EXPIRATION_FLAG bdr_reports)
               if [ $? -eq 0 ]; then
                 echo "Created a BigQuery dataset bdr_reports successfully."
               else
                 echo ""
                 echo "ERROR : Failed to create the BigQuery dataset."
                 echo $result
                 exit 1
               fi
             fi
               # --- Check if Log Sink already exists, create if not ---
             echo "Checking if Log Sink exists..."
             if gcloud logging sinks list | grep "bdr_report_sink" >/dev/null; then
               echo "Log Sink bdr_reports_sink already exists for $PROJECT_ID"
             else
               log_filter="projects/$PROJECT_ID/logs/backupdr.googleapis.com%2Fbdr_*"
               echo "Creating log sink bdr_reports..."
               result=$(gcloud logging sinks create bdr_report_sink bigquery.googleapis.com/projects/$PROJECT_ID/datasets/bdr_reports --log-filter="logName=~\"$log_filter\"")
               if [ $? -eq 0 ]; then
                 echo "Created a logsink bdr_reports_sink successfully."
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
               echo "ERROR : Failed to add permissions for cloud logging to write to BigQuery datasets. Please make sure that you have Owner access rights in order to be able to proceed."
               exit 1
             fi
         
             echo "Setup complete. The logs for the project $PROJECT_ID will now start flowing to bigquery."
             exit 0
         
           exit 0
         

  4. Save the file with a name with a Bash file extension, for example, `script.sh`.

  5. Run the command bash using the file you just created. For example, `bash script.sh`.

You can see the created dataset in the **BigQuery Studio**.




**Note:** Typically, log entries are visible in BigQuery within one minute. However, when a sink is created, it might take up to sixty minutes before the log data is available in BigQuery.

## Set up prebuilt reports for vaulted backups

You can set up prebuilt reports by executing the following script within the dataset where the logs are being routed through the log sink.

The script adds the following prebuilt reports:

  * [Backup and restore job reports for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-restore-backupvault-report)
  * [Protected resource reports for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-vault-reports)
  * [Backup vault consumption reports for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-vault-consumption-report)
  * [Daily schedule compliance reports for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/daily-schedule-policy-vault-report)
  * [Backup plan report for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/daily-schedule-policy-vault-report)

**Note:** Depending on the log category, logs are generated at a frequency of zero to eight hours. To ensure successful execution of the script, it is recommended that you run the script at least eight hours after creating the sink.

To set up prebuilt reports in BigQuery for vaulted backups, do the following:

###  gcloud 

  1. Go to **Activate cloud shell** and click **Open editor**.
  2. Click the menuicon, select **File** , and then select **New text file**.
  3. Copy and paste the following prebuilt reports script into the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).
         
         #!/bin/bash
         
         # Default config values. Modify only if required.
         DATASET="bdr_reports"
         JOBS_TABLE_PREFIX="backupdr_googleapis_com_bdr_backup_restore_jobs_"
         PROTECTED_RESOURCE_TABLE_PREFIX="backupdr_googleapis_com_bdr_protected_resource_"
         BACKUP_VAULT_TABLE_PREFIX="backupdr_googleapis_com_bdr_backup_vault_details_"
         BACKUP_PLAN_TABLE_PREFIX="backupdr_googleapis_com_bdr_backup_plan_details_"
         VIEW_FROM_DATE_SUFFIX="20000101"  #Use an old enough date so that the views should contain all the data.
         ALLOWED_RESOURCE_TYPES='('"'"'Compute Engine'"'"', '"'"'Disk'"'"', '"'"'Cloud SQL'"'"', '"'"'Filestore'"'"')'
         
         # Function to check if a routine exists
         routine_exists() {
         local routine_name="$1"
         bq --project_id $PROJECT_ID ls --routines "$DATASET" | grep "$routine_name" >/dev/null
         }
         
         # Function to check if a view exists
         view_exists() {
         local view_name="$1"
         check_view=$(bq --project_id $PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from $DATASET.INFORMATION_SCHEMA.VIEWS WHERE table_name='$view_name'" | tail -n +2 | tr -d ' ')
         if [ $check_view == 'true' ]; then
           return 0
         fi
         return -1
         }
         
         # Function to create a routine
         create_routine() {
         local routine_name="$1"
         local routine_type="$2"
         local definition_body="$3"
         # Construct the routine body JSON
         local routine_body='
           {
           "definitionBody": "'"$definition_body"'",
           "routineType": "'"$routine_type"'",
           "routineReference": {
               "projectId": "'"$PROJECT_ID"'",
               "datasetId": "'"$DATASET"'",
               "routineId": "'"$routine_name"'"
           },
           "arguments": [
               {
               "name": "FROM_DATE",
               "dataType": {
                   "typeKind": "STRING"
               }
               },
               {
               "name": "TO_DATE",
               "dataType": {
                   "typeKind": "STRING"
               }
               }
           ]
           }
         '
         
         # Use POST for creating a new routine
         local http_method="POST"
         local routine_id=""
         # If routine exists use PUT to update the routine
         if routine_exists "$routine_name"; then
         echo "Routine $routine_name already exists. Updating the existing routine"
         http_method="PUT"
         routine_id="/$routine_name"
         fi
         
         # Construct the curl command with the routine body
         local curl_command=(
           curl -s --request $http_method \
             "https://bigquery.googleapis.com/bigquery/v2/projects/$PROJECT_ID/datasets/$DATASET/routines$routine_id" \
             --header "Authorization: Bearer $ACCESS_TOKEN" \
             --header 'Accept: application/json' \
             --header 'Content-Type: application/json' \
             --data "$routine_body" --compressed
         )
           # Execute the curl command and capture the result
         local result=$( "${curl_command[@]}" )
         
         # Check if creation was successful
         if echo "$result" | grep '"etag":' > /dev/null; then
           echo "Routine '$routine_name' created/updated successfully."
         else
           echo "$result"
           exit -1
         fi
         }
         
         # Function to create a view
         create_view() {
         local view_name="$1"
         local parent_routine_name="$1"
         local view_query='
           SELECT * FROM `'$PROJECT_ID'.'$DATASET'.'$parent_routine_name'`("'$VIEW_FROM_DATE_SUFFIX'", FORMAT_DATE("%Y%m%d", CURRENT_DATE()));
         '
         
         # Check if view exists.
         if routine_exists "$parent_routine_name"; then
           view_exists "$view_name"
           if [ $? -eq 0 ]; then
             echo "View $view_name already exists. Skipping."
             return 0
           fi
           # Create the view if it does not exist
           bq --project_id $PROJECT_ID mk --use_legacy_sql=false --expiration 0 --view "$view_query" $DATASET.$view_name
         else
           echo "Routine $parent_routine_name is not present. Skipping the creation of $view_name."
           return -1
         fi
         }
         
         # Create all jobs related routines and views
         create_jobs_routines_and_views() {
         # Backup Restore Jobs
         create_routine "backup_restore_jobs" "TABLE_VALUED_FUNCTION" \
         '
         WITH
           dat AS (
           SELECT
             *,
             LAG(insertId, 1, '"'"'placeholder_id'"'"') OVER (ORDER BY timestamp, insertId) = insertId AS `insert_id_is_same`,
             LAG(timestamp, 1, TIMESTAMP_SECONDS(1)) OVER (ORDER BY timestamp, insertId) = timestamp AS `timestamp_is_same`
           FROM
             `'$PROJECT_ID'.'$DATASET'.'$JOBS_TABLE_PREFIX'*`
           WHERE
             _TABLE_SUFFIX >= FROM_DATE
             AND _TABLE_SUFFIX <= TO_DATE
             AND jsonpayload_v1_bdrbackuprestorejoblog.resourceType IN '"${ALLOWED_RESOURCE_TYPES}"' ),
           deduped AS (
           SELECT
             * EXCEPT (insert_id_is_same,
               timestamp_is_same),
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).endtime) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).endtime), NULL) AS job_end_time,
         
           FROM
             dat
           WHERE
             NOT (insert_id_is_same
               AND timestamp_is_same) ),
           latest AS (
           SELECT
             jsonpayload_v1_bdrbackuprestorejoblog.jobId AS job_id,
             MAX(CASE jsonpayload_v1_bdrbackuprestorejoblog.jobStatus
                 WHEN '"'"'RUNNING'"'"' THEN 1
                 WHEN '"'"'SKIPPED'"'"' THEN 2
                 WHEN '"'"'SUCCESSFUL'"'"' THEN 3
                 WHEN '"'"'FAILED'"'"' THEN 4
             END
               ) AS final_status_code
           FROM
             deduped
           GROUP BY
             jsonpayload_v1_bdrbackuprestorejoblog.jobid),
           filled_latest AS (
           SELECT
             jsonpayload_v1_bdrbackuprestorejoblog.jobId AS job_id,
             jsonpayload_v1_bdrbackuprestorejoblog.jobStatus AS final_status,
             PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', jsonpayload_v1_bdrbackuprestorejoblog.startTime) AS parsed_start_time,
             PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', deduped.job_end_time) AS parsed_end_time,
             TIMESTAMP_DIFF(PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', deduped.job_end_time), PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', jsonpayload_v1_bdrbackuprestorejoblog.startTime), HOUR) AS duration_hours,
             MOD(TIMESTAMP_DIFF(PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', deduped.job_end_time), PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', jsonpayload_v1_bdrbackuprestorejoblog.startTime), MINUTE), 60) AS duration_minutes,
             MOD(TIMESTAMP_DIFF(PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', deduped.job_end_time), PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', jsonpayload_v1_bdrbackuprestorejoblog.startTime), SECOND), 60) AS duration_seconds,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).restoreresourcename) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).restoreresourcename), NULL) AS restore_resource_name,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errortype) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errortype), NULL) AS error_type,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errormessage) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errormessage), NULL) AS error_message,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupname) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupname), NULL) AS backup_name,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupplanname) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupplanname), NULL) AS backup_plan_name,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backuprule) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backuprule), NULL) AS backup_rule,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupconsistencytime) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).backupconsistencytime), NULL) AS backup_consistency_time,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).incrementalbackupsizegib) = '"'"'number'"'"', FLOAT64(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).incrementalbackupsizegib), NULL) AS incremental_backup_size_in_gib,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errorcode) = '"'"'number'"'"', FLOAT64(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).errorcode), NULL) AS error_code,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).recoverypointtime) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).recoverypointtime), NULL) AS recovery_point_time,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).datasourcename) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).datasourcename), NULL) AS data_source_name,
           IF
             (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).restoreresourcelocation) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackuprestorejoblog).restoreresourcelocation), NULL) AS restore_resource_location,
         
           FROM
             deduped
           JOIN
             latest
           ON
             latest.job_id = jsonpayload_v1_bdrbackuprestorejoblog.jobId
             AND jsonpayload_v1_bdrbackuprestorejoblog.jobStatus = (
               CASE final_status_code
                 WHEN 1 THEN '"'"'RUNNING'"'"'
                 WHEN 2 THEN '"'"'SKIPPED'"'"'
                 WHEN 3 THEN '"'"'SUCCESSFUL'"'"'
                 WHEN 4 THEN '"'"'FAILED'"'"'
             END
               ) )
         SELECT
           FORMAT_TIMESTAMP('"'"'%m%d'"'"', filled_latest.parsed_start_time, '"'"'UTC'"'"') || '"'"'-'"'"' || ARRAY_TO_STRING(REGEXP_EXTRACT_ALL(jsonpayload_v1_bdrbackuprestorejoblog.resourceType, '"'"'\\\\b[A-Z]'"'"'), '"'"''"'"') || '"'"'-'"'"' || (CASE jsonpayload_v1_bdrbackuprestorejoblog.jobCategory
               WHEN '"'"'ON_DEMAND_BACKUP'"'"' THEN '"'"'B'"'"'
               WHEN '"'"'SCHEDULED_BACKUP'"'"' THEN '"'"'B'"'"'
               WHEN '"'"'ON_DEMAND_OPERATIONAL_BACKUP'"'"' THEN '"'"'B'"'"'
               WHEN '"'"'RESTORE'"'"' THEN '"'"'R'"'"'
               WHEN '"'"'PITR'"'"' THEN '"'"'R'"'"'
               ELSE '"'"'U'"'"'
           END
             ) || '"'"'-'"'"' || REPLACE(FORMAT_TIMESTAMP('"'"'%H%M%E3S'"'"', filled_latest.parsed_start_time, '"'"'UTC'"'"'), '"'"'.'"'"', '"'"''"'"') AS `job_name`,
           REGEXP_EXTRACT(jsonpayload_v1_bdrbackuprestorejoblog.sourceResourceName, '"'"'([^/]+)$'"'"') AS `resource_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.sourceResourceName, '"'"'/'"'"')) < 2, NULL, SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.sourceResourceName,'"'"'/'"'"')[1]) AS `resource_project_name`,
           jsonpayload_v1_bdrbackuprestorejoblog.jobStatus AS `job_status`,
           jsonpayload_v1_bdrbackuprestorejoblog.jobCategory AS `job_category`,
           Filled_latest.error_type AS `error_type`,
           CAST(filled_latest.error_code AS INT64) AS `error_code`,
           filled_latest.error_message AS `error_message`,
           parsed_start_time AS `job_start_time`,
           parsed_end_time AS `job_end_time`,
         IF
           (duration_hours > 0, duration_hours || '"'"'h '"'"', '"'"''"'"') ||
         IF
           (duration_minutes > 0, duration_minutes || '"'"'m '"'"', '"'"''"'"') ||
         IF
           (duration_seconds > 0, duration_seconds || '"'"'s '"'"', '"'"''"'"') AS `duration`,
           ROUND(filled_latest.incremental_backup_size_in_gib, 2) AS `incremental_backup_size_in_gib`,
           PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', filled_latest.backup_consistency_time) AS `backup_consistency_time`,
           PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', filled_latest.recovery_point_time) AS `recovery_point_time`,
         IF
           (filled_latest.data_source_name IS NULL OR ARRAY_LENGTH(SPLIT(filled_latest.data_source_name, '"'"'/'"'"')) < 8, NULL, SPLIT(filled_latest.data_source_name, '"'"'/'"'"')[7]) AS `data_source_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName, '"'"'/'"'"')[3]) AS `backup_vault_location`,
         IF
           (ARRAY_LENGTH(SPLIT(filled_latest.backup_plan_name, '"'"'/'"'"')) < 6, NULL, SPLIT(filled_latest.backup_plan_name,'"'"'/'"'"')[5]) AS `backup_plan_name`,
           filled_latest.backup_rule AS `backup_rule`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName,'"'"'/'"'"')[5]) AS `backup_vault_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackuprestorejoblog.backupVaultName,'"'"'/'"'"')[1]) AS `backup_vault_project_name`,
         IF
           (ARRAY_LENGTH(SPLIT(filled_latest.backup_name, '"'"'/'"'"')) < 10, NULL, SPLIT(filled_latest.backup_name,'"'"'/'"'"')[9]) AS `backup_name`,
         IF
           (ARRAY_LENGTH(SPLIT(filled_latest.restore_resource_name, '"'"'/'"'"')) < 6, NULL, SPLIT(filled_latest.restore_resource_name,'"'"'/'"'"')[1]) AS `restore_project_name`,
         IF
           (ARRAY_LENGTH(SPLIT(filled_latest.restore_resource_name, '"'"'/'"'"')) < 6, NULL, SPLIT(filled_latest.restore_resource_name,'"'"'/'"'"')[5]) AS `restore_resource_name`,
           filled_latest.restore_resource_location AS `restore_resource_location`,
           jsonpayload_v1_bdrbackuprestorejoblog.sourceresourcelocation AS `resource_location`,
           jsonpayload_v1_bdrbackuprestorejoblog.resourceType AS `resource_type`,
           jsonpayload_v1_bdrbackuprestorejoblog.sourceResourceId AS `resource_id`,
           jsonpayload_v1_bdrbackuprestorejoblog.jobId AS `job_id`,
           timestamp AS `log_timestamp`
         FROM
           deduped
         JOIN
           filled_latest
         ON
           filled_latest.job_id = jsonpayload_v1_bdrbackuprestorejoblog.jobId
           AND jsonpayload_v1_bdrbackuprestorejoblog.jobStatus = filled_latest.final_status
         ORDER BY
           parsed_start_time DESC
         '
         
         # Backup Jobs Summary
         create_routine "backup_jobs_summary" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             DATE(log_timestamp) AS `date`,
             resource_project_name,
             job_category,
             ROUND((COUNTIF(job_status = '"'"'SUCCESSFUL'"'"')/COUNT(*)) * 100, 2) AS `success_percent`,
             COUNT(*) AS `total`,
             COUNTIF(job_status = '"'"'SUCCESSFUL'"'"') AS `successful`,
             COUNTIF(job_status = '"'"'FAILED'"'"') AS `failed`,
             COUNTIF(job_status = '"'"'SKIPPED'"'"') AS `skipped`,
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_restore_jobs`(FROM_DATE,
               TO_DATE)
           WHERE job_category IN ('"'"'ON_DEMAND_BACKUP'"'"', '"'"'SCHEDULED_BACKUP'"'"', '"'"'ON_DEMAND_OPERATIONAL_BACKUP'"'"') AND job_status IN ('"'"'SUCCESSFUL'"'"', '"'"'FAILED'"'"', '"'"'SKIPPED'"'"')
           GROUP BY
             `date`,
             resource_project_name,
             job_category
           ORDER BY
             `date` DESC
         '
         create_view "backup_jobs_summary"
         
         # Backup Jobs Details
         create_routine "backup_jobs_details" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             job_name,
             resource_name,
             resource_project_name,
             job_status,
             error_type,
             error_code,
             error_message,
             job_start_time,
             job_end_time,
             duration,
             incremental_backup_size_in_gib,
             backup_consistency_time,
             backup_plan_name,
             backup_rule,
             backup_vault_name,
             backup_vault_project_name,
             backup_vault_location,
             resource_location,
             resource_type,
             resource_id,
             job_category,
             job_id
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_restore_jobs`(FROM_DATE,
               TO_DATE)
           WHERE
             job_status IN ('"'"'SUCCESSFUL'"'"',
               '"'"'FAILED'"'"', '"'"'SKIPPED'"'"') AND job_category IN ('"'"'ON_DEMAND_BACKUP'"'"', '"'"'SCHEDULED_BACKUP'"'"', '"'"'ON_DEMAND_OPERATIONAL_BACKUP'"'"')
         '
         create_view "backup_jobs_details"
         
         # Successful Backup Jobs Details
         create_routine "successful_backup_jobs" "TABLE_VALUED_FUNCTION" \
         'SELECT
             job_name,
             resource_name,
             resource_project_name,
             job_start_time,
             job_end_time,
             duration,
             incremental_backup_size_in_gib,
             backup_consistency_time,
             backup_plan_name,
             backup_rule,
             backup_vault_name,
             backup_vault_project_name,
             backup_vault_location,
             resource_type,
             resource_id,
             job_category,
             job_id
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_jobs_details`(FROM_DATE,
               TO_DATE) WHERE job_status = '"'"'SUCCESSFUL'"'"'
         '
         create_view "successful_backup_jobs"
         
         # Failed Backup Job Details
         create_routine "failed_backup_jobs" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             job_name,
             resource_name,
             resource_project_name,
             error_type,
             error_code,
             error_message,
             job_start_time,
             job_end_time,
             duration,
             backup_plan_name,
             backup_rule,
             backup_vault_name,
             backup_vault_project_name,
             backup_vault_location,
             resource_type,
             resource_id,
             job_category,
             job_id
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_jobs_details`(FROM_DATE,
               TO_DATE) WHERE job_status = '"'"'FAILED'"'"'
         '
         create_view "failed_backup_jobs"
         
         # Skipped Backup Job Details
         create_routine "skipped_backup_jobs" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             job_name,
             resource_name,
             resource_project_name,
             backup_plan_name,
             backup_rule,
             backup_vault_name,
             job_start_time,
             backup_vault_project_name,
             backup_vault_location,
             resource_type,
             resource_id,
             job_category,
             job_id
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_jobs_details`(FROM_DATE,
               TO_DATE)
           WHERE
             job_status = '"'"'SKIPPED'"'"'
         '
         create_view "skipped_backup_jobs"
         
         # Restore Jobs Summary
         create_routine "restore_jobs_summary" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             DATE(log_timestamp) AS `date`,
             restore_project_name,
             backup_vault_project_name,
             job_category,
             ROUND((COUNTIF(job_status = '"'"'SUCCESSFUL'"'"')/COUNT(*)) * 100, 2) AS `success_percent`,
             COUNT(*) AS `total`,
             COUNTIF(job_status = '"'"'SUCCESSFUL'"'"') AS `successful`,
             COUNTIF(job_status = '"'"'FAILED'"'"') AS `failed`,
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_restore_jobs`(FROM_DATE,
               TO_DATE)
           WHERE
             job_category IN ('"'"'RESTORE'"'"', '"'"'PITR'"'"')
             AND job_status IN ('"'"'SUCCESSFUL'"'"',
               '"'"'FAILED'"'"')
           GROUP BY
             `date`,
             restore_project_name,
             backup_vault_project_name,
             job_category
           ORDER BY
             `date` DESC
         '
         create_view "restore_jobs_summary"
         
         # Restore Jobs Details
         create_routine "restore_jobs_details" "TABLE_VALUED_FUNCTION" \
         '
         SELECT
             job_name,
             resource_name,
             resource_project_name,
             job_status,
             error_type,
             error_code,
             error_message,
             job_start_time,
             job_end_time,
             duration,
             restore_resource_name,
             restore_project_name,
             restore_resource_location,
             recovery_point_time,
             data_source_name,
             backup_vault_location,
             backup_vault_name,
             backup_vault_project_name,
             resource_location,
             resource_type,
             resource_id,
             job_category,
             job_id
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_restore_jobs`(FROM_DATE,
               TO_DATE)
           WHERE
             job_category IN ('"'"'RESTORE'"'"', '"'"'PITR'"'"')
             AND job_status IN ('"'"'SUCCESSFUL'"'"',
               '"'"'FAILED'"'"')
         '
         create_view "restore_jobs_details"
         }
         
         # Protected Resource Details
         create_protected_resource_routines_and_views() {
         create_routine "protected_resource_details" "TABLE_VALUED_FUNCTION" \
         '
         WITH
           dat AS (
           SELECT
             *,
             LAG(insertId, 1, '"'"'placeholder_id'"'"') OVER (ORDER BY timestamp, insertId) = insertId AS `insert_id_is_same`,
             LAG(timestamp, 1, TIMESTAMP_SECONDS(1)) OVER (ORDER BY timestamp, insertId) = timestamp AS `timestamp_is_same`
         
           FROM
             `'$PROJECT_ID'.'$DATASET'.'$PROTECTED_RESOURCE_TABLE_PREFIX'*` WHERE _TABLE_SUFFIX >= FROM_DATE AND _TABLE_SUFFIX <= TO_DATE
             AND jsonpayload_v1_bdrprotectedresourcelog.resourceType IN '"${ALLOWED_RESOURCE_TYPES}"'
             ),
           deduped AS (
           SELECT
             * EXCEPT (`insert_id_is_same`,
               `timestamp_is_same`)
           FROM
             dat
           WHERE
             NOT (`insert_id_is_same`
               AND `timestamp_is_same`) ),
           latest_for_date AS (
           SELECT
             DATE(timestamp) AS `log_date`,
             jsonpayload_v1_bdrprotectedresourcelog.sourceresourcename AS `source_resource_name`,
             MAX(timestamp) AS `latest_timestamp`
           FROM
             deduped
           GROUP BY
             `log_date`,
             `source_resource_name` )
         SELECT
           DATE(timestamp) AS `date`,
           jsonpayload_v1_bdrprotectedresourcelog.resourcetype AS `resource_type`,
           REGEXP_EXTRACT(jsonpayload_v1_bdrprotectedresourcelog.sourceresourcename, '"'"'([^/]+)$'"'"') AS `resource_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrprotectedresourcelog.sourceresourcename, '"'"'/'"'"')) < 2, NULL, SPLIT(jsonpayload_v1_bdrprotectedresourcelog.sourceresourcename,'"'"'/'"'"')[1]) AS `resource_project_name`,
           jsonpayload_v1_bdrprotectedresourcelog.sourceresourcedatasizegib AS `resource_data_size_in_gib`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupvaultname, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupvaultname,'"'"'/'"'"')[5]) AS `backup_vault_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname,'"'"'/'"'"')[5]) AS `backup_plan_name`,
           (
           SELECT
             ARRAY_AGG(STRUCT(
                 array_entry.rulename AS `rule_name`,
                 array_entry.recurrence AS `recurrence`,
                 array_entry.recurrenceschedule AS `recurrence_schedule`,
                 array_entry.backupwindow AS `backup_window`,
                 IF(array_entry.backupwindowtimezone = '"'"'Etc/UTC'"'"', '"'"'UTC'"'"',array_entry.backupwindowtimezone)  AS `backup_window_time_zone`,
                 array_entry.retentiondays AS `retention_days`
               ))
           FROM
             UNNEST(jsonpayload_v1_bdrprotectedresourcelog.currentbackupruledetails) array_entry ) AS `backup_rules`,
         DATE(PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', jsonpayload_v1_bdrprotectedresourcelog.lastprotectedon)) AS `last_backup_plan_assoc_date`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname, '"'"'/'"'"')) < 2, NULL, SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname,'"'"'/'"'"')[1]) AS `backup_vault_project_name`,
         IF
           (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname, '"'"'/'"'"')) < 4, NULL, SPLIT(jsonpayload_v1_bdrprotectedresourcelog.currentbackupplanname,'"'"'/'"'"')[3]) AS `backup_vault_location`,
           jsonpayload_v1_bdrprotectedresourcelog.sourceresourcelocation AS `resource_location`,
           jsonpayload_v1_bdrprotectedresourcelog.sourceresourceid AS `resource_id`,
         FROM
           deduped
         INNER JOIN
           latest_for_date
         ON
           DATE(timestamp) = latest_for_date.log_date
           AND timestamp = latest_for_date.latest_timestamp
           AND latest_for_date.`source_resource_name` = jsonpayload_v1_bdrprotectedresourcelog.sourceresourcename
         ORDER BY
           `date` DESC,
           `resource_name` ASC
         '
         create_view "protected_resource_details"
         }
         
         # Backup Vault Consumption
         create_backup_vault_consumption_routines_and_views() {
         create_routine "backup_vault_consumption" "TABLE_VALUED_FUNCTION" \
         '
         WITH
             dat AS (
             SELECT
               *,
             LAG(insertId, 1, '"'"'placeholder_id'"'"') OVER (ORDER BY timestamp, insertId) = insertId AS `insert_id_is_same`,
             LAG(timestamp, 1, TIMESTAMP_SECONDS(1)) OVER (ORDER BY timestamp, insertId) = timestamp AS `timestamp_is_same`
             FROM
               `'$PROJECT_ID'.'$DATASET'.'$BACKUP_VAULT_TABLE_PREFIX'*`
             WHERE
               jsonpayload_v1_bdrbackupvaultdetailslog.resourceType IN '"${ALLOWED_RESOURCE_TYPES}"'
               AND _TABLE_SUFFIX >= FROM_DATE
               AND _TABLE_SUFFIX <= TO_DATE ),
             deduped AS (
             SELECT
               * EXCEPT (`insert_id_is_same`,
                 `timestamp_is_same`)
             FROM
               dat
             WHERE
               NOT (`insert_id_is_same`
                 AND `timestamp_is_same`) ),
             latest_for_date AS (
             SELECT
               DATE(timestamp) AS `log_date`,
               MAX(timestamp) AS `latest_timestamp`,
               jsonpayload_v1_bdrbackupvaultdetailslog.sourceresourcename AS `source_resource_name`,
             FROM
               deduped
             GROUP BY
               log_date,
               `source_resource_name`)
           SELECT
             DATE(timestamp) AS `date`,
             jsonpayload_v1_bdrbackupvaultdetailslog.resourcetype AS `resource_type`,
             REGEXP_EXTRACT(jsonpayload_v1_bdrbackupvaultdetailslog.sourceresourcename, '"'"'([^/]+)$'"'"') AS `resource_name`,
             SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.sourceresourcename, '"'"'/'"'"')[1] AS `resource_project_name`,
           IF
             (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname,'"'"'/'"'"')[5]) AS `backup_vault_name`,
             jsonpayload_v1_bdrbackupvaultdetailslog.storedbytesgib AS `backup_vault_stored_bytes_in_gib`,
         CAST(jsonpayload_v1_bdrbackupvaultdetailslog.minimumEnforcedRetentionDays AS INT64) AS `backup_vault_minimum_enforced_retention_days`,
           IF
         (ARRAY_LENGTH(SPLIT(IF
         (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).currentbackupplanname) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).currentbackupplanname), NULL), '"'"'/'"'"')) < 6, NULL, SPLIT(IF
         (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).currentbackupplanname) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).currentbackupplanname), NULL),'"'"'/'"'"')[5]) AS `backup_plan_name`,
         PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', IF
         (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).firstavailablerestorepoint) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).firstavailablerestorepoint), NULL)) AS `first_available_restore_point`,
         PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', IF
         (JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).lastavailablerestorepoint) = '"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).lastavailablerestorepoint), NULL)) AS `last_available_restore_point`,
         
           IF
             (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname,'"'"'/'"'"')[1]) AS `backup_vault_project_name`,
           IF
             (ARRAY_LENGTH(SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname, '"'"'/'"'"')) < 6, NULL, SPLIT(jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname,'"'"'/'"'"')[3]) AS `backup_vault_location`,
           jsonpayload_v1_bdrbackupvaultdetailslog.sourceresourcelocation AS `resource_location`,
           FROM
             deduped
           INNER JOIN
             latest_for_date
           ON
             DATE(timestamp) = latest_for_date.log_date
             AND timestamp = latest_for_date.latest_timestamp
             AND jsonpayload_v1_bdrbackupvaultdetailslog.sourceresourcename = latest_for_date.`source_resource_name`
           ORDER BY
             `date` DESC,
             `resource_name` ASC
         '
         create_view "backup_vault_consumption"
         }
         
         # Backup Plan Details
         create_backup_plan_details_routines_and_views() {
           create_routine "backup_plan_details" "TABLE_VALUED_FUNCTION" \
           '
           WITH
             backup_plan_dat AS (
               SELECT
                 *,
                 LAG(insertId, 1, '"'"'placeholder_id'"'"') OVER (ORDER BY timestamp, insertId) = insertId AS `insert_id_is_same`,
                 LAG(timestamp, 1, TIMESTAMP_SECONDS(1)) OVER (ORDER BY timestamp, insertId) = timestamp AS `timestamp_is_same`
               FROM
                 `'$PROJECT_ID'.'$DATASET'.'$BACKUP_PLAN_TABLE_PREFIX'*`
               WHERE
                 _TABLE_SUFFIX >= FROM_DATE
                 AND _TABLE_SUFFIX <= TO_DATE
             ),
             backup_plan_deduped AS (
               SELECT
                 * EXCEPT (`insert_id_is_same`, `timestamp_is_same`)
               FROM
                 backup_plan_dat
               WHERE
                 NOT (`insert_id_is_same` AND `timestamp_is_same`)
             ),
             backup_plan_latest_for_date AS (
               SELECT
                 DATE(timestamp) AS `log_date`,
                 MAX(timestamp) AS `latest_timestamp`,
                 jsonpayload_v1_bdrbackupplandetailslog.backupplanname AS `backupplanname`
               FROM
                 backup_plan_deduped
               GROUP BY
                 `log_date`,
                 `backupplanname`
             ),
             latest_backup_vault AS (
               SELECT
                 timestamp,
                 jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname as backupvaultname,
                 jsonpayload_v1_bdrbackupvaultdetailslog.minimumenforcedretentiondays as minimumenforcedretentiondays,
                 IF(JSON_TYPE(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).effectivedateforenforcedretentionlock)='"'"'string'"'"', STRING(TO_JSON(jsonpayload_v1_bdrbackupvaultdetailslog).effectivedateforenforcedretentionlock), NULL) as effectivedateforenforcedretentionlock
               FROM `'$PROJECT_ID'.'$DATASET'.'$BACKUP_VAULT_TABLE_PREFIX'*`
               QUALIFY ROW_NUMBER() OVER (PARTITION BY jsonpayload_v1_bdrbackupvaultdetailslog.backupvaultname ORDER BY timestamp DESC) = 1
             )
           SELECT
             DATE(bp_d.timestamp) AS `date`,
             IF(ARRAY_LENGTH(SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupplanname, '"'"'/'"'"')) < 6, NULL, SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupplanname,'"'"'/'"'"')[OFFSET(5)]) AS `backup_plan_name`,
             IF(ARRAY_LENGTH(SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupplanname, '"'"'/'"'"')) < 4, NULL, SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupplanname, '"'"'/'"'"')[OFFSET(3)]) AS `backup_plan_location`,
             (
               SELECT
                 ARRAY_AGG(STRUCT(
                     rule_details.rulename AS `rule_name`,
                     rule_details.recurrence AS `recurrence`,
                     rule_details.recurrenceschedule AS `recurrence_schedule`,
                     rule_details.backupwindow AS `backup_window`,
                     IF(rule_details.backupwindowtimezone = '"'"'Etc/UTC'"'"', '"'"'UTC'"'"',rule_details.backupwindowtimezone)  AS `backup_window_time_zone`,
                     rule_details.retentiondays AS `retention_days`
                   ))
               FROM
                 UNNEST(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupruledetails) rule_details
             ) AS `backup_rules`,
             IF(ARRAY_LENGTH(SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupvaultname, '"'"'/'"'"')) < 6, NULL, SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupvaultname,'"'"'/'"'"')[OFFSET(5)]) AS `backup_vault_name`,
             IF(ARRAY_LENGTH(SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupvaultname, '"'"'/'"'"')) < 4, NULL, SPLIT(bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupvaultname, '"'"'/'"'"')[OFFSET(3)]) AS `backup_vault_location`,
             bp_d.jsonpayload_v1_bdrbackupplandetailslog.resourcesprotectedcount AS `resources_protected_count`,
             bp_d.jsonpayload_v1_bdrbackupplandetailslog.protecteddatavolumegib AS `protected_data_volume_gib`,
             bv_d.minimumenforcedretentiondays AS `minimum_enforced_retention_days`,
             bv_d.effectivedateforenforcedretentionlock AS `effective_date_for_enforced_retention_lock`,
             CASE
               WHEN bv_d.effectivedateforenforcedretentionlock IS NULL THEN '"'"'unlocked'"'"'
               WHEN LENGTH(TRIM(bv_d.effectivedateforenforcedretentionlock)) = 0 THEN '"'"'unlocked'"'"'
               WHEN PARSE_TIMESTAMP('"'"'%FT%H:%M:%E*S%Ez'"'"', bv_d.effectivedateforenforcedretentionlock) <= CURRENT_TIMESTAMP() THEN '"'"'locked'"'"'
               ELSE '"'"'unlocked'"'"'
             END AS `lock_on_enforced_retention`
           FROM
             backup_plan_deduped AS bp_d
             INNER JOIN backup_plan_latest_for_date AS bp_lfd
               ON DATE(bp_d.timestamp) = bp_lfd.log_date
               AND bp_d.timestamp = bp_lfd.latest_timestamp
               AND bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupplanname = bp_lfd.backupplanname
             LEFT JOIN latest_backup_vault AS bv_d
               ON bp_d.jsonpayload_v1_bdrbackupplandetailslog.backupvaultname = bv_d.backupvaultname
           ORDER BY
             `date` DESC,
             `backup_plan_name` ASC
           '
           create_view "backup_plan_details"
         }
         
         # Daily Scheduled Compliance
         create_daily_scheduled_compliance_routine_and_view() {
         create_routine "daily_scheduled_compliance" "TABLE_VALUED_FUNCTION" \
         '
         WITH
           DailyComplianceWindows AS (
           SELECT
             * EXCEPT (backup_rules),
             PARSE_TIMESTAMP('"'"'%F %H:%M %Z'"'"', date || '"'"' '"'"' || REGEXP_EXTRACT_ALL(backup_window, '"'"'[0-9][0-9]:[0-9][0-9]'"'"')[0] || '"'"' '"'"' || backup_window_time_zone) AS expected_start_time,
             resource_project_name || '"'"'/'"'"' || resource_location || '"'"'/'"'"' || resource_id AS unique_resource_name,
           IF
             (REGEXP_EXTRACT_ALL(backup_window, '"'"'[0-9][0-9]:[0-9][0-9]'"'"')[1] = '"'"'24:00'"'"', TIMESTAMP_ADD(PARSE_TIMESTAMP('"'"'%F %H:%M %Z'"'"', date || '"'"' 23:59 '"'"' || backup_window_time_zone), INTERVAL 1 MINUTE), PARSE_TIMESTAMP('"'"'%F %H:%M %Z'"'"', date || '"'"' '"'"' || REGEXP_EXTRACT_ALL(backup_window, '"'"'[0-9][0-9]:[0-9][0-9]'"'"')[1] || '"'"' '"'"' || backup_window_time_zone)) AS expected_end_time
           FROM
             `'$PROJECT_ID'.'$DATASET'.protected_resource_details`(FROM_DATE, TO_DATE)
           CROSS JOIN
             UNNEST(backup_rules) AS rule
           ON
             rule.recurrence='"'"'Daily'"'"'),
           BackupJobs AS (
           SELECT
             *,
             resource_project_name || '"'"'/'"'"' || resource_location || '"'"'/'"'"' || resource_id AS unique_resource_name,
           FROM
             `'$PROJECT_ID'.'$DATASET'.backup_restore_jobs`(FROM_DATE, FORMAT_DATE('"'"'%Y%m%d'"'"', DATE_ADD(PARSE_DATE('"'"'%Y%m%d'"'"', TO_DATE), INTERVAL 10 DAY)))
           WHERE
             job_category IN ('"'"'ON_DEMAND_BACKUP'"'"',
               '"'"'SCHEDULED_BACKUP'"'"',
               '"'"'ON_DEMAND_OPERATIONAL_BACKUP'"'"') ),
           DailyCompliance AS (
           SELECT
             date,
             DailyComplianceWindows.resource_type,
             DailyComplianceWindows.resource_name,
             DailyComplianceWindows.resource_project_name as `resource_project_name`,
             DailyComplianceWindows.backup_plan_name,
             DailyComplianceWindows.rule_name,
             DailyComplianceWindows.backup_window,
             DailyComplianceWindows.backup_window_time_zone,
             (CASE BackupJobs.job_status
                 WHEN '"'"'SUCCESSFUL'"'"' THEN '"'"'Successful'"'"'
                 WHEN '"'"'RUNNING'"'"' THEN '"'"'Pending'"'"'
                 ELSE
             IF
               (CURRENT_TIMESTAMP() <= DailyComplianceWindows.expected_end_time, '"'"'Pending'"'"', '"'"'Failed'"'"')
             END
               ) AS backup_schedule_compliance_status,
             (CASE BackupJobs.job_status
                 WHEN '"'"'SUCCESSFUL'"'"' THEN '"'"'Job '"'"' || BackupJobs.job_name || '"'"' was successful.'"'"'
                 WHEN '"'"'RUNNING'"'"' THEN '"'"'Job '"'"' || BackupJobs.job_name || '"'"' is running.'"'"'
                 ELSE
             IF
               (CURRENT_TIMESTAMP() <= DailyComplianceWindows.expected_end_time, '"'"'Backup window for '"'"'|| date || '"'"' has not passed yet.'"'"', '"'"'No successful backup job detected within backup window.'"'"')
             END
               ) AS comment,
             DailyComplianceWindows.backup_vault_name,
             DailyComplianceWindows.backup_vault_project_name as `backup_vault_project_name`,
             DailyComplianceWindows.backup_vault_location as `backup_vault_location`,
             DailyComplianceWindows.resource_location,
             ROW_NUMBER() OVER (PARTITION BY BackupJobs.unique_resource_name, DailyComplianceWindows.date, DailyComplianceWindows.rule_name ORDER BY (CASE BackupJobs.job_status WHEN '"'"'SUCCESSFUL'"'"' THEN 4 WHEN '"'"'RUNNING'"'"' THEN 3 ELSE 1 END ) DESC,
               BackupJobs.job_start_time ASC) AS row_number,
           FROM
             DailyComplianceWindows
           LEFT JOIN
             BackupJobs
           ON
             (BackupJobs.unique_resource_name = DailyComplianceWindows.unique_resource_name
               AND BackupJobs.backup_rule = DailyComplianceWindows.rule_name
               AND BackupJobs.job_status = '"'"'SUCCESSFUL'"'"'
               AND BackupJobs.backup_consistency_time >= DailyComplianceWindows.expected_start_time
               AND BackupJobs.backup_consistency_time <= DailyComplianceWindows.expected_end_time)
             OR (BackupJobs.unique_resource_name = DailyComplianceWindows.unique_resource_name
               AND BackupJobs.backup_rule = DailyComplianceWindows.rule_name
               AND BackupJobs.job_status = '"'"'RUNNING'"'"'
               AND BackupJobs.job_start_time >= DailyComplianceWindows.expected_start_time
               AND BackupJobs.job_start_time <= DailyComplianceWindows.expected_end_time)
           ORDER BY
             date DESC,
             BackupJobs.resource_name ASC)
         SELECT
           * EXCEPT(row_number)
         FROM
           DailyCompliance
         WHERE
           row_number = 1
         '
         create_view "daily_scheduled_compliance"
         }
         
         # --- Main script ---
         
         # Get the default project ID
         DEFAULT_PROJECT_ID=$(gcloud config get-value project)
         read -p "Enter Project ID (default: $DEFAULT_PROJECT_ID, press Enter to continue):" PROJECT_ID
         
         # Use default if no input is provided
         if [ -z "$PROJECT_ID" ]; then
           PROJECT_ID=$DEFAULT_PROJECT_ID
         fi
         
         ## Generate Access Token
         echo "Generating access token..."
         ACCESS_TOKEN=$(gcloud auth print-access-token --quiet)
         if [ -z "$ACCESS_TOKEN" ]; then
           echo "Failed to retrieve access token" >&2
           exit 1
         fi
         echo "Access token generated successfully..."
         
         ## Check if the dataset exists
         echo "Check if Reporting Dataset exists..."
         if bq --project_id $PROJECT_ID ls | grep "$DATASET" >/dev/null; then
           echo "Dataset $DATASET exists for $PROJECT_ID. Continuing."
         else
           echo "Dataset $DATASET does not exist for $PROJECT_ID. Exiting."
           exit 0
         fi
         
         ## Check if the tables exist
         echo "Determining which tables are available in BigQuery..."
         check_jobs_table=$(bq --project_id $PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from "$DATASET".INFORMATION_SCHEMA.TABLES WHERE table_name like '%"$JOBS_TABLE_PREFIX"%'" | tail -n +2 | tr -d ' ')
         check_protected_resource_table=$(bq --project_id $PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from "$DATASET".INFORMATION_SCHEMA.TABLES WHERE table_name like '%"$PROTECTED_RESOURCE_TABLE_PREFIX"%'" | tail -n +2 | tr -d ' ')
         check_backup_vault_consumption_table=$(bq --project_id $PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from "$DATASET".INFORMATION_SCHEMA.TABLES WHERE table_name like '%"$BACKUP_VAULT_TABLE_PREFIX"%'" | tail -n +2 | tr -d ' ')
         check_backup_plan_details_table=$(bq --project_id $PROJECT_ID query --format=csv --use_legacy_sql=false "Select COUNT(*)>0 from "$DATASET".INFORMATION_SCHEMA.TABLES WHERE table_name like '%"$BACKUP_PLAN_TABLE_PREFIX"%'" | tail -n +2 | tr -d ' ')
         
         echo "Creating routines and views based on available tables.."
         if [ "$check_jobs_table" == 'true' ]; then
         create_jobs_routines_and_views
         fi
         
         if [ "$check_protected_resource_table" == 'true' ]; then
         create_protected_resource_routines_and_views
         fi
         
         if [ "$check_backup_vault_consumption_table" == 'true' ]; then
         create_backup_vault_consumption_routines_and_views
         fi
         
         if [ "$check_backup_plan_details_table" == 'true' ]; then
         create_backup_plan_details_routines_and_views
         fi
         
         if [ "$check_jobs_table" == 'true' ] && [ "$check_protected_resource_table" == 'true' ]; then
         create_daily_scheduled_compliance_routine_and_view
         fi
         
         if [ $check_jobs_table == 'false' ] || [ $check_protected_resource_table == 'false' ] || [ $check_backup_vault_consumption_table == 'false' ] || [ $check_backup_plan_details_table == 'false' ]; then
         echo -e "\e[1m\e[33mAll the prebuilt reports could not be created successfully in BigQuery as one or more report logs are missing in the dataset $DATASET."
         echo -e "Please ensure that you have waited for at least 8 hours after creating the sink, and before running the script to create pre built reports. Try re-running the script again after some time to fix the issue."
         echo -e "Reach out to Google Cloud Support in case you are still facing this issue.\e[0m"
         else
         echo "Set up completed..."
         fi
         

  4. Save the file with a name with a Bash file extension, for example, `backupdrreports.sh`.

  5. Run the command bash using the file you just created. For example, `bash backupdrreports.sh`.

You can see the prebuilt reports under the dataset in the **BigQuery Studio**.




After you [set up prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#script), you can [view the reports in Data Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-vault-lookerstudio).

## What's next

  * Learn how to [View prebuilt reports in Looker for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-vault-lookerstudio)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
