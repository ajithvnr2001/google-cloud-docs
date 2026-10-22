---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake/
title: Collect Snowflake logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:36.974692+00:00
---

# Collect Snowflake logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snowflake/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Snowflake logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Snowflake logs to Google Security Operations. You can configure ingestion using two methods: Cloud Storage V2 (recommended) or Amazon S3 V2. Both methods use the same mechanism on the Snowflake side: a scheduled task unloads account usage data to an external stage, and Google SecOps reads the exported files with a feed.

Snowflake is a cloud data platform that stores account activity in the `SNOWFLAKE.ACCOUNT_USAGE` schema. The `LOGIN_HISTORY` view records authentication attempts, including the client IP address, the authentication factor, and the failure reason. The `QUERY_HISTORY` view records every statement executed in the account, including the user, the role, the warehouse, and the objects touched.

**Note:** An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `SNOWFLAKE` ingestion label.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Access to Snowflake with a role that can create storage integrations (only `ACCOUNTADMIN` has this privilege by default), databases, warehouses, stages, and tasks
  * For Cloud Storage V2: a Google Cloud project with the Cloud Storage API enabled, and permissions to create buckets, create Identity and Access Management (IAM) roles, and manage bucket IAM policies
  * For Amazon S3 V2: privileged access to AWS to create S3 buckets, IAM policies, IAM roles, and IAM users



## Grant access to Snowflake account usage data

The `SNOWFLAKE.ACCOUNT_USAGE` views are readable by `ACCOUNTADMIN` only until access is granted explicitly. Create a dedicated role for the export and grant it the two database roles that cover the views this document exports.

  1. Sign in to Snowflake and open a worksheet.
  2. Create the export role and grant it read access to the account usage views as follows:
         
         USE ROLE ACCOUNTADMIN;
         
         CREATE ROLE IF NOT EXISTS SECOPS_EXPORTER;
         
         GRANT DATABASE ROLE SNOWFLAKE.SECURITY_VIEWER TO ROLE SECOPS_EXPORTER;
         GRANT DATABASE ROLE SNOWFLAKE.GOVERNANCE_VIEWER TO ROLE SECOPS_EXPORTER;
         

**Note:** `SNOWFLAKE.SECURITY_VIEWER` covers `LOGIN_HISTORY` and `SNOWFLAKE.GOVERNANCE_VIEWER` covers `QUERY_HISTORY`. Granting `IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE` also works, but it exposes the whole schema, including organization level data, so prefer the two database roles.
  3. Create the database, schema, and warehouse that the export uses, and grant them to the role as follows:
         
         CREATE DATABASE IF NOT EXISTS SECOPS_EXPORT;
         CREATE SCHEMA IF NOT EXISTS SECOPS_EXPORT.ACTIVITY;
         
         CREATE WAREHOUSE IF NOT EXISTS SECOPS_EXPORT_WH
             WITH WAREHOUSE_SIZE = 'XSMALL'
             AUTO_SUSPEND = 60
             AUTO_RESUME = TRUE
             INITIALLY_SUSPENDED = TRUE;
         
         GRANT USAGE ON DATABASE SECOPS_EXPORT TO ROLE SECOPS_EXPORTER;
         GRANT USAGE, CREATE STAGE, CREATE TABLE, CREATE PROCEDURE, CREATE TASK, CREATE FILE FORMAT
             ON SCHEMA SECOPS_EXPORT.ACTIVITY TO ROLE SECOPS_EXPORTER;
         GRANT USAGE, OPERATE ON WAREHOUSE SECOPS_EXPORT_WH TO ROLE SECOPS_EXPORTER;
         GRANT EXECUTE TASK ON ACCOUNT TO ROLE SECOPS_EXPORTER;
         GRANT ROLE SECOPS_EXPORTER TO USER <YOUR_USER>;
         

     * Replace `<YOUR_USER>` with the Snowflake user that owns the export.



## Method 1: Cloud Storage V2 (recommended)

### Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `snowflake-activity-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create a custom Cloud Storage role for Snowflake

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.
  2. Click **Create role**.
  3. Provide the following configuration details: 
     * **Title** : Enter `Snowflake Unload`
     * **ID** : Enter `snowflake_unload`
     * **Role launch stage** : Select **General Availability**
  4. Click **Add permissions** and add the following permissions: 
     * `storage.buckets.get`
     * `storage.objects.create`
     * `storage.objects.delete`
     * `storage.objects.list`
  5. Click **Create**.

**Note:** This is the permission set that Snowflake documents for unloading data. Loading data into Snowflake additionally requires `storage.objects.get`, which this integration does not need.



### Create the Snowflake storage integration for Cloud Storage

  1. In a Snowflake worksheet, create the storage integration as follows:
         
         USE ROLE ACCOUNTADMIN;
         
         CREATE STORAGE INTEGRATION SECOPS_GCS_INT
             TYPE = EXTERNAL_STAGE
             STORAGE_PROVIDER = 'GCS'
             ENABLED = TRUE
             STORAGE_ALLOWED_LOCATIONS = ('gcs://snowflake-activity-logs/snowflake/');
         
         GRANT USAGE ON INTEGRATION SECOPS_GCS_INT TO ROLE SECOPS_EXPORTER;
         

     * Replace `snowflake-activity-logs` with your bucket name.
  2. Retrieve the service account that Snowflake created for the integration as follows:
         
         DESC STORAGE INTEGRATION SECOPS_GCS_INT;
         

  3. Copy the value of the `STORAGE_GCP_SERVICE_ACCOUNT` property. The value has the following format:
         
         service-account-id@project1-123456.iam.gserviceaccount.com
         

**Note:** Snowflake creates one service account for the whole Snowflake account, so each Cloud Storage storage integration in the account uses the same value.



### Grant the Snowflake service account access to the bucket

  1. In the Google Cloud console, go to **Cloud Storage > Buckets**.
  2. Click the bucket you created (for example, `snowflake-activity-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the `STORAGE_GCP_SERVICE_ACCOUNT` value
     * **Assign roles** : Select **Snowflake Unload**
  6. Click **Save**.



### Create the file format and external stage

  1. In a Snowflake worksheet, create the file format and the stage that writes to the bucket as follows:
         
         USE ROLE SECOPS_EXPORTER;
         USE SCHEMA SECOPS_EXPORT.ACTIVITY;
         
         CREATE OR REPLACE FILE FORMAT SECOPS_JSON_FORMAT
             TYPE = JSON;
         
         CREATE OR REPLACE STAGE SECOPS_EXPORT_STAGE
             URL = 'gcs://snowflake-activity-logs/snowflake/'
             STORAGE_INTEGRATION = SECOPS_GCS_INT
             FILE_FORMAT = SECOPS_JSON_FORMAT;
         

**Note:** Snowflake compresses unloaded files with gzip by default, so the bucket receives `.json.gz` objects. The feed decompresses them during ingestion.



### Create the export state table

The export tracks how far it has read in each view. Without that watermark, every run would re-export the whole view and the same events would be ingested again.

  1. Create the state table and seed it as follows:
         
         CREATE TABLE IF NOT EXISTS SECOPS_EXPORT_STATE (
             VIEW_NAME STRING NOT NULL,
             LAST_EXPORTED TIMESTAMP_LTZ NOT NULL,
             WINDOW_END TIMESTAMP_LTZ
         );
         
         INSERT INTO SECOPS_EXPORT_STATE (VIEW_NAME, LAST_EXPORTED)
             SELECT 'LOGIN_HISTORY', DATEADD('day', -7, CURRENT_TIMESTAMP())
             UNION ALL
             SELECT 'QUERY_HISTORY', DATEADD('day', -7, CURRENT_TIMESTAMP());
         

**Note:** The seed values decide how much history the first run exports. Account usage views keep 365 days of data, so a larger backfill is possible, at the cost of a large first export. Run the `INSERT` statement once. Running it again adds duplicate rows and the export stops advancing correctly.



### Create the export procedure

  1. Create the procedure that unloads both views and advances the watermark as follows:
         
         CREATE OR REPLACE PROCEDURE SECOPS_EXPORT_ACTIVITY()
         RETURNS STRING
         LANGUAGE SQL
         AS
         $$
         BEGIN
             UPDATE SECOPS_EXPORT_STATE
                 SET WINDOW_END = DATEADD('hour', -3, CURRENT_TIMESTAMP());
         
             COPY INTO @SECOPS_EXPORT_STAGE/login_history/
                 FROM (
                     SELECT OBJECT_CONSTRUCT(
                         'application', 'snowflake',
                         'log_type', 'login_history',
                         'EVENT_TIMESTAMP', EVENT_TIMESTAMP,
                         'EVENT_TYPE', EVENT_TYPE,
                         'USER_NAME', USER_NAME,
                         'CLIENT_IP', CLIENT_IP,
                         'REPORTED_CLIENT_TYPE', REPORTED_CLIENT_TYPE,
                         'REPORTED_CLIENT_VERSION', REPORTED_CLIENT_VERSION,
                         'FIRST_AUTHENTICATION_FACTOR', FIRST_AUTHENTICATION_FACTOR,
                         'SECOND_AUTHENTICATION_FACTOR', SECOND_AUTHENTICATION_FACTOR,
                         'IS_SUCCESS', IS_SUCCESS,
                         'ERROR_CODE', ERROR_CODE,
                         'ERROR_MESSAGE', ERROR_MESSAGE)
                     FROM SNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORY
                     WHERE EVENT_TIMESTAMP > (SELECT LAST_EXPORTED FROM SECOPS_EXPORT_STATE WHERE VIEW_NAME = 'LOGIN_HISTORY')
                         AND EVENT_TIMESTAMP <= (SELECT WINDOW_END FROM SECOPS_EXPORT_STATE WHERE VIEW_NAME = 'LOGIN_HISTORY')
                 )
                 FILE_FORMAT = (TYPE = JSON)
                 INCLUDE_QUERY_ID = TRUE;
         
             UPDATE SECOPS_EXPORT_STATE
                 SET LAST_EXPORTED = WINDOW_END
                 WHERE VIEW_NAME = 'LOGIN_HISTORY';
         
             COPY INTO @SECOPS_EXPORT_STAGE/query_history/
                 FROM (
                     SELECT OBJECT_CONSTRUCT(
                         'application', 'snowflake',
                         'log_type', 'query_history',
                         'START_TIME', START_TIME,
                         'END_TIME', END_TIME,
                         'QUERY_ID', QUERY_ID,
                         'QUERY_TYPE', QUERY_TYPE,
                         'EXECUTION_STATUS', EXECUTION_STATUS,
                         'ERROR_MESSAGE', ERROR_MESSAGE,
                         'USER_NAME', USER_NAME,
                         'ROLE_NAME', ROLE_NAME,
                         'WAREHOUSE_NAME', WAREHOUSE_NAME,
                         'WAREHOUSE_SIZE', WAREHOUSE_SIZE,
                         'DATABASE_NAME', DATABASE_NAME,
                         'SCHEMA_NAME', SCHEMA_NAME,
                         'SESSION_ID', SESSION_ID,
                         'BYTES_SCANNED', BYTES_SCANNED,
                         'ROWS_PRODUCED', ROWS_PRODUCED,
                         'TOTAL_ELAPSED_TIME', TOTAL_ELAPSED_TIME)
                     FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
                     WHERE START_TIME > (SELECT LAST_EXPORTED FROM SECOPS_EXPORT_STATE WHERE VIEW_NAME = 'QUERY_HISTORY')
                         AND START_TIME <= (SELECT WINDOW_END FROM SECOPS_EXPORT_STATE WHERE VIEW_NAME = 'QUERY_HISTORY')
                 )
                 FILE_FORMAT = (TYPE = JSON)
                 INCLUDE_QUERY_ID = TRUE;
         
             UPDATE SECOPS_EXPORT_STATE
                 SET LAST_EXPORTED = WINDOW_END
                 WHERE VIEW_NAME = 'QUERY_HISTORY';
         
             RETURN 'Export completed';
         END;
         $$;
         




Each element of the procedure exists for a reason:

  * The window closes three hours behind the current time. Snowflake populates `LOGIN_HISTORY` with up to two hours of latency and `QUERY_HISTORY` with up to 45 minutes, so a window that ends now would skip rows that the view has not materialized yet. Events therefore reach Google SecOps about three hours after they happen. Shortening the lag trades completeness for freshness.
  * `WINDOW_END` is written to the table before the unload, so the value used by the `COPY INTO` statement and the value written back to `LAST_EXPORTED` are identical. Recomputing the current time in the second statement would skip everything that happened in between.
  * Each `LAST_EXPORTED` update runs after its own `COPY INTO` statement. If an unload fails, the procedure stops, the watermark stays where it was, and the next run repeats that window instead of skipping it.
  * `INCLUDE_QUERY_ID = TRUE` adds a UUID to every filename. Without it, unloaded files are named `data_0_0_0` and repeated exports to the same path collide, which Snowflake documents as a source of duplicated data in the stage.



### Schedule the export task

  1. Create and start the task as follows:
         
         CREATE OR REPLACE TASK SECOPS_EXPORT_TASK
             WAREHOUSE = SECOPS_EXPORT_WH
             SCHEDULE = 'USING CRON 0 * * * * UTC'
             AS CALL SECOPS_EXPORT_ACTIVITY();
         
         ALTER TASK SECOPS_EXPORT_TASK RESUME;
         

**Note:** Snowflake creates tasks in a suspended state. The task does not run until `ALTER TASK ... RESUME` is executed.
  2. Run the task once to verify the setup without waiting for the schedule as follows:
         
         EXECUTE TASK SECOPS_EXPORT_TASK;
         

  3. Check the result of the run and the files that reached the stage as follows:
         
         SELECT NAME, STATE, ERROR_MESSAGE, SCHEDULED_TIME
         FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(TASK_NAME => 'SECOPS_EXPORT_TASK'))
         ORDER BY SCHEDULED_TIME DESC
         LIMIT 5;
         
         LIST @SECOPS_EXPORT_STAGE;
         




### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snowflake activity logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snowflake** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://snowflake-activity-logs/snowflake/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: `Storage Object Viewer` to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. `Storage Object Viewer` does not grant the bucket-level permission the feed needs, and the `Storage Legacy Bucket` roles do not grant permission to read object contents.

## Method 2: Amazon S3 V2

Use this method when the logs must land in Amazon S3. The Snowflake side is identical apart from the storage integration and the stage, so the export procedure and task from Method 1 are reused unchanged.

### Configure an Amazon S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference. For example, `snowflake-activity-logs`.



### Configure the Snowflake AWS IAM policy

  1. Sign in to the AWS Management Console.
  2. Search for and select **IAM**.
  3. Select **Account settings**.
  4. Under **Security Token Service (STS)** in the **Endpoints** list, find the Snowflake region where your account is located.
  5. If the STS status is inactive, move the toggle to **Active**.
  6. Select **Policies**.
  7. Select **Create Policy**.
  8. In **Policy editor** , select **JSON**.
  9. Copy and paste the following policy, which grants Snowflake the permissions it needs to unload data into one bucket and folder path:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": [
                         "s3:PutObject",
                         "s3:GetObject",
                         "s3:GetObjectVersion",
                         "s3:DeleteObject",
                         "s3:DeleteObjectVersion"
                     ],
                     "Resource": "arn:aws:s3:::snowflake-activity-logs/snowflake/*"
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "s3:ListBucket",
                         "s3:GetBucketLocation"
                     ],
                     "Resource": "arn:aws:s3:::snowflake-activity-logs",
                     "Condition": {
                         "StringLike": {
                             "s3:prefix": [
                                 "snowflake/*"
                             ]
                         }
                     }
                 }
             ]
         }
         

  10. Click **Next**.

  11. Enter a **Policy name** (for example, `snowflake_access`) and an optional description.

  12. Click **Create policy**.




### Configure the Snowflake AWS IAM role

  1. In **IAM** , select **Roles**.
  2. Click **Create role**.
  3. Select **AWS account** as the trusted entity type.
  4. Select **Another AWS account**.
  5. In the **Account ID** field, enter your own AWS account ID temporarily. You modify the trust relationship later and grant access to Snowflake.
  6. Select the **Require external ID** option.
  7. Enter a placeholder ID such as `0000`. You replace it with the external ID of the storage integration later.
  8. Click **Next**.
  9. Select the IAM policy you created earlier.
  10. Click **Next**.
  11. Enter a name and description for the role.
  12. Click **Create role**.
  13. On the role summary page, copy and save the **Role ARN** value.



### Create the Snowflake storage integration for Amazon S3

  1. In a Snowflake worksheet, create the storage integration as follows:
         
         USE ROLE ACCOUNTADMIN;
         
         CREATE STORAGE INTEGRATION SECOPS_S3_INT
             TYPE = EXTERNAL_STAGE
             STORAGE_PROVIDER = 'S3'
             ENABLED = TRUE
             STORAGE_AWS_ROLE_ARN = '<IAM_ROLE_ARN>'
             STORAGE_ALLOWED_LOCATIONS = ('s3://snowflake-activity-logs/snowflake/');
         
         GRANT USAGE ON INTEGRATION SECOPS_S3_INT TO ROLE SECOPS_EXPORTER;
         

     * Replace `<IAM_ROLE_ARN>` with the Role ARN you saved.
  2. Retrieve the AWS identity that Snowflake created for the integration as follows:
         
         DESC INTEGRATION SECOPS_S3_INT;
         

  3. Copy and save the values of the following properties as follows:

     * **STORAGE_AWS_IAM_USER_ARN**
     * **STORAGE_AWS_EXTERNAL_ID**



### Grant the Snowflake IAM user access to the bucket

  1. Go to the AWS Management Console.
  2. Select **IAM > Roles**.
  3. Select the role you created earlier.
  4. Select the **Trust relationships** tab.
  5. Click **Edit trust policy**.
  6. Update the policy document with the `DESC INTEGRATION` output values as follows:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "",
                     "Effect": "Allow",
                     "Principal": {
                         "AWS": "<STORAGE_AWS_IAM_USER_ARN>"
                     },
                     "Action": "sts:AssumeRole",
                     "Condition": {
                         "StringEquals": {
                             "sts:ExternalId": "<STORAGE_AWS_EXTERNAL_ID>"
                         }
                     }
                 }
             ]
         }
         

  7. Click **Update policy**.




### Create the file format, stage, and export objects

  1. In a Snowflake worksheet, create the file format and the stage that writes to the bucket as follows:
         
         USE ROLE SECOPS_EXPORTER;
         USE SCHEMA SECOPS_EXPORT.ACTIVITY;
         
         CREATE OR REPLACE FILE FORMAT SECOPS_JSON_FORMAT
             TYPE = JSON;
         
         CREATE OR REPLACE STAGE SECOPS_EXPORT_STAGE
             URL = 's3://snowflake-activity-logs/snowflake/'
             STORAGE_INTEGRATION = SECOPS_S3_INT
             FILE_FORMAT = SECOPS_JSON_FORMAT;
         

  2. Create the state table, the procedure, and the task exactly as described in Method 1, in the sections **Create the export state table** , **Create the export procedure** , and **Schedule the export task**. The statements reference the stage by name, so they need no change.




### Configure AWS IAM for Google SecOps

  1. Sign in to the AWS Management Console.
  2. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  3. Select the created **User**.
  4. Select the **Security credentials** tab.
  5. Click **Create Access Key** in the **Access Keys** section.
  6. Select **Third-party service** as the **Use case**.
  7. Click **Next**.
  8. Optional: Add a description tag.
  9. Click **Create access key**.
  10. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  11. Click **Done**.
  12. Select the **Permissions** tab.
  13. Click **Add permissions** in the **Permissions policies** section.
  14. Select **Add permissions**.
  15. Select **Attach policies directly**.
  16. Search for and select the **AmazonS3FullAccess** policy.
  17. Click **Next**.
  18. Click **Add permissions**.



### Configure a feed in Google SecOps to ingest Snowflake logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snowflake activity logs`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Snowflake** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters as follows:

     * **S3 URI** : `s3://snowflake-activity-logs/snowflake/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`column4_label` | `additional.fields` | Merged  
`column7_label` | `additional.fields` | Merged  
`first_authentication_factor_label` | `additional.fields` | Merged  
`host_list` | `additional.fields` | Merged  
`query_text_label` | `additional.fields` | Merged  
`query_type_label` | `additional.fields` | Merged  
`roleIds_list` | `additional.fields` | Merged  
`roleNames_list` | `additional.fields` | Merged  
`rolecount_label` | `additional.fields` | Merged  
`user_count_label` | `additional.fields` | Merged  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`START_TIME` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS Z`  
`column2` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS Z`  
`column20` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS Z`  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`, `true` → `USER_LOGIN`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`column10` | `metadata.product_event_type` | Directly mapped  
`QUERY_ID` | `metadata.product_log_id` | Directly mapped  
`column1` | `metadata.product_log_id` | Directly mapped  
`column6` | `metadata.product_version` | Directly mapped  
`SESSION_ID` | `network.http.session_id` | Directly mapped  
`RECEIVED_BYTES` | `network.received_bytes` | Renamed/mapped  
`BYTES_SENT_OVER_THE_NETWORK` | `network.sent_bytes` | Renamed/mapped  
`SENT_BYTES` | `network.sent_bytes` | Renamed/mapped  
`APPLICATION` | `principal.application` | Directly mapped  
`data.user_name` | `principal.asset.hostname` | Directly mapped  
`CLIENT_IP` | `principal.asset.ip` | Merged  
`IP` | `principal.asset.ip` | Merged  
`column5` | `principal.asset.ip` | Merged  
`SOURCE_REGION` | `principal.cloud.availability_zone` | Directly mapped  
`SOURCE_CLOUD` | `principal.cloud.environment` | Mapped: `(?i)azure` → `MICROSOFT_AZURE`, `(?i)amazon` → `AMAZON_WEB_SERVICES`, `(?i)google` ...  
`data.user_name` | `principal.hostname` | Directly mapped  
`CLIENT_IP` | `principal.ip` | Merged  
`IP` | `principal.ip` | Merged  
`column5` | `principal.ip` | Merged  
`OS` | `principal.platform` | Mapped: `(?i)Linux` → `LINUX`, `(?i)windows` → `WINDOWS`, `(?i)mac/ios` → `MAC`  
`OS_VERSION` | `principal.platform_version` | Directly mapped  
`SOURCE_CLOUD_label` | `principal.resource.attribute.labels` | Merged  
`roles` | `principal.user.attribute.roles` | Merged  
`data.role_name` | `principal.user.role_name` | Directly mapped  
`column9` | `principal.user.user_display_name` | Directly mapped  
`USER_NAME` | `principal.user.userid` | Directly mapped  
`column10` | `principal.user.userid` | Directly mapped  
`column3` | `principal.user.userid` | Directly mapped  
`EXECUTION_STATUS` | `security_result.action` | Mapped: `(?i)success` → `action`, `(?i)fail` → `security_result_action_block`  
`STATUS` | `security_result.action` | Mapped: `(?i)success` → `action`, `(?i)fail` → `action`  
`action` | `security_result.action` | Merged  
`security_result_action_block` | `security_result.action` | Merged  
`OCSP_MODE` | `security_result.action_details` | Directly mapped  
`column11` | `security_result.action_details` | Directly mapped  
`column3` | `security_result.action_details` | Directly mapped  
`BYTES_DELETED_label` | `security_result.detection_fields` | Merged  
`BYTES_READ_FROM_RESULT_label` | `security_result.detection_fields` | Merged  
`BYTES_SCANNED_label` | `security_result.detection_fields` | Merged  
`BYTES_SPILLED_TO_LOCAL_STORAGE_label` | `security_result.detection_fields` | Merged  
`BYTES_SPILLED_TO_REMOTE_STORAGE_label` | `security_result.detection_fields` | Merged  
`BYTES_WRITTEN_TO_RESULT_label` | `security_result.detection_fields` | Merged  
`BYTES_WRITTEN_label` | `security_result.detection_fields` | Merged  
`CHILD_QUERIES_WAIT_TIME_label` | `security_result.detection_fields` | Merged  
`CLUSTER_NUMBER_label` | `security_result.detection_fields` | Merged  
`COMPILATION_TIME_label` | `security_result.detection_fields` | Merged  
`CREDITS_USED_CLOUD_SERVICES_label` | `security_result.detection_fields` | Merged  
`DATABASE_ID_label` | `security_result.detection_fields` | Merged  
`DATABASE_NAME_label` | `security_result.detection_fields` | Merged  
`END_TIME_label` | `security_result.detection_fields` | Merged  
`ERROR_MESSAGE_label` | `security_result.detection_fields` | Merged  
`EXECUTION_TIME_label` | `security_result.detection_fields` | Merged  
`EXTERNAL_FUNCTION_TOTAL_INVOCATIONS_label` | `security_result.detection_fields` | Merged  
`EXTERNAL_FUNCTION_TOTAL_RECEIVED_BYTES_label` | `security_result.detection_fields` | Merged  
`EXTERNAL_FUNCTION_TOTAL_RECEIVED_ROWS_label` | `security_result.detection_fields` | Merged  
`EXTERNAL_FUNCTION_TOTAL_SENT_BYTES_label` | `security_result.detection_fields` | Merged  
`EXTERNAL_FUNCTION_TOTAL_SENT_ROWS_label` | `security_result.detection_fields` | Merged  
`INBOUND_DATA_TRANSFER_BYTES_label` | `security_result.detection_fields` | Merged  
`IS_CLIENT_GENERATED_STATEMENT_label` | `security_result.detection_fields` | Merged  
`LIST_EXTERNAL_FILES_TIME_label` | `security_result.detection_fields` | Merged  
`OUTBOUND_DATA_TRANSFER_BYTES_label` | `security_result.detection_fields` | Merged  
`PARTITIONS_SCANNED_label` | `security_result.detection_fields` | Merged  
`PARTITIONS_TOTAL_label` | `security_result.detection_fields` | Merged  
`PERCENTAGE_SCANNED_FROM_CACHE_label` | `security_result.detection_fields` | Merged  
`QUERY_ACCELERATION_BYTES_SCANNED_label` | `security_result.detection_fields` | Merged  
`QUERY_ACCELERATION_PARTITIONS_SCANNED_label` | `security_result.detection_fields` | Merged  
`QUERY_ACCELERATION_UPPER_LIMIT_SCALE_FACTOR_label` | `security_result.detection_fields` | Merged  
`QUERY_HASH_VERSION_label` | `security_result.detection_fields` | Merged  
`QUERY_HASH_label` | `security_result.detection_fields` | Merged  
`QUERY_LOAD_PERCENT_label` | `security_result.detection_fields` | Merged  
`QUERY_PARAMETERIZED_HASH_VERSION_label` | `security_result.detection_fields` | Merged  
`QUERY_TAG_label` | `security_result.detection_fields` | Merged  
`QUERY_TYPE_label` | `security_result.detection_fields` | Merged  
`QUEUED_OVERLOAD_TIME_label` | `security_result.detection_fields` | Merged  
`QUEUED_PROVISIONING_TIME_label` | `security_result.detection_fields` | Merged  
`QUEUED_REPAIR_TIME_label` | `security_result.detection_fields` | Merged  
`RELEASE_VERSION_label` | `security_result.detection_fields` | Merged  
`ROLE_TYPE_label` | `security_result.detection_fields` | Merged  
`ROWS_DELETED_label` | `security_result.detection_fields` | Merged  
`ROWS_INSERTED_label` | `security_result.detection_fields` | Merged  
`ROWS_PRODUCED_label` | `security_result.detection_fields` | Merged  
`ROWS_UNLOADED_label` | `security_result.detection_fields` | Merged  
`ROWS_UPDATED_label` | `security_result.detection_fields` | Merged  
`ROWS_WRITTEN_TO_RESULT_label` | `security_result.detection_fields` | Merged  
`SCHEMA_ID_label` | `security_result.detection_fields` | Merged  
`SCHEMA_NAME_label` | `security_result.detection_fields` | Merged  
`TOTAL_ELAPSED_TIME_label` | `security_result.detection_fields` | Merged  
`TRANSACTION_BLOCKED_TIME_label` | `security_result.detection_fields` | Merged  
`TRANSACTION_ID_label` | `security_result.detection_fields` | Merged  
`WAREHOUSE_ID_label` | `security_result.detection_fields` | Merged  
`WAREHOUSE_NAME_label` | `security_result.detection_fields` | Merged  
`WAREHOUSE_SIZE_label` | `security_result.detection_fields` | Merged  
`WAREHOUSE_TYPE_label` | `security_result.detection_fields` | Merged  
`authentication_factor_label` | `security_result.detection_fields` | Merged  
`column4_label` | `security_result.detection_fields` | Merged  
`column6_label` | `security_result.detection_fields` | Merged  
`column7_label` | `security_result.detection_fields` | Merged  
`column8_label` | `security_result.detection_fields` | Merged  
`event_id_label` | `security_result.detection_fields` | Merged  
`event_type_label` | `security_result.detection_fields` | Merged  
`is_success_label` | `security_result.detection_fields` | Merged  
`python_compiler_label` | `security_result.detection_fields` | Merged  
`python_runtime_label` | `security_result.detection_fields` | Merged  
`python_version_label` | `security_result.detection_fields` | Merged  
`reported_client_type_label` | `security_result.detection_fields` | Merged  
`reported_client_version_label` | `security_result.detection_fields` | Merged  
`tracing_label` | `security_result.detection_fields` | Merged  
`EXECUTION_STATUS` | `security_result.summary` | Directly mapped  
`STATUS` | `security_result.summary` | Directly mapped  
`column17` | `security_result.summary` | Directly mapped  
`TARGET_REGION` | `target.cloud.availability_zone` | Directly mapped  
`TARGET_CLOUD` | `target.cloud.environment` | Mapped: `(?i)azure` → `MICROSOFT_AZURE`, `(?i)amazon` → `AMAZON_WEB_SERVICES`, `(?i)google` ...  
`TARGET_CLOUD_label` | `target.resource.attribute.labels` | Merged  
`column2_label` | `target.resource.attribute.labels` | Merged  
`column7_label` | `target.resource.attribute.labels` | Merged  
`USER_NAME` | `target.user.userid` | Directly mapped  
`column4` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `SNOWFLAKE`  
N/A | `metadata.vendor_name` | Constant: `SNOWFLAKE`  
N/A | `principal.cloud.environment` | Constant: `MICROSOFT_AZURE`  
N/A | `principal.platform` | Constant: `LINUX`  
N/A | `target.cloud.environment` | Constant: `MICROSOFT_AZURE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snowflake-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
