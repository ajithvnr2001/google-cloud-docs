---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-aurora/
title: Collect AWS Aurora logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:30:49.464135+00:00
---

# Collect AWS Aurora logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-aurora/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Aurora logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Aurora logs to Google Security Operations. AWS Aurora is a managed relational database service that offers high performance, scalability, and availability. In this integration, you will configure AWS Aurora to forward logs to Google SecOps for analysis, monitoring, and threat detection.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS
  * AWS Aurora database cluster set up and running



## Configure Amazon S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save the bucket **Name** and **Region** for later use.
  3. Create a user following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**. 
  5. Select the **Security credentials** tab.
  6. Click **Create Access Key** in the **Access Keys** section.
  7. Select **Third-party service** as the **Use case**.
  8. Click **Next**.
  9. Optional: add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for later use. 
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions** in the **Permissions policies** section.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for and select **AmazonS3FullAccess** and **CloudWatchLogsFullAccess** policies.
  18. Click **Next**.
  19. Click **Add permissions**.



## Configure Enhanced Monitoring

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type **RDS** and select **RDS** from the services list.
  3. In the **RDS Dashboard** , select **Databases** from the navigation pane.
  4. Select the **Aurora cluster** you want to monitor.
  5. Under the **Logs & monitoring** section, click **Modify**.
  6. Go to the **Monitoring** section and enable **Enhanced Monitoring**.
  7. Set the **Monitoring role** to the appropriate IAM role that has permissions to publish to **CloudWatch Logs** or **S3**.
  8. Save the changes and apply them to your Aurora cluster.



## How to configure AWS Aurora audit logs

  1. In the **RDS Dashboard** , select **Databases** and click your **Aurora cluster**.
  2. Under the **Logs & Monitoring** section, click **Modify**.
  3. In the **Database Options** section, make sure that **Enable Audit Logs** is selected.
  4. Under **Destination** , choose **S3** and specify the **S3 bucket** where logs will be stored.
  5. Click **Save changes** to apply the settings.



## Optional: AWS Aurora Logs Configuration using CloudWatch

For additional monitoring capabilities, you can configure **CloudWatch Logs** to capture Aurora logs.

  1. In the **RDS Dashboard** , select your **Aurora cluster**.
  2. Under the **Logs & Monitoring** section, make sure that **CloudWatch Logs** integration is enabled.
  3. Go to **CloudWatch Logs** and create a new **Log Group** to store the Aurora logs.
  4. On the **Log Groups** screen, choose the name of your new **Log Group**.
  5. Select **Actions > Export data to Amazon S3**.
  6. On the **Export data to Amazon S3** screen, under **Define data export** , set the time range for the data to export using **From** and **To**.

**Note:** If your log group has multiple log streams, you can provide a log stream prefix to limit the log group data to a specific stream.  
Choose **Advanced** , and then for **Stream prefix** , enter the log stream prefix.
  7. **Choose S3 bucket** , select the account associated with the Amazon S3 bucket.

  8. **S3 bucket name** , select an Amazon S3 bucket.

  9. **S3 Bucket prefix** , enter the randomly generated string that you specified in the bucket policy.

  10. Choose **Export** to export your log data to Amazon S3.

  11. To view the status of the log data that you exported to Amazon S3, select **Actions > View all exports to Amazon S3**.




## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Aurora feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Aurora** log type.
  3. Specify the values in the following fields.

     * **Source Type** : Amazon SQS V2
     * **Queue Name** : The SQS queue name to read from
     * **S3 URI** : The bucket URI. 
       * `s3://your-log-bucket-name/`
         * Replace `your-log-bucket-name` with the actual name of your S3 bucket.
     * **Source deletion options** : Select the deletion option according to your ingestion preferences.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **SQS Queue Access Key ID** : An account access key that is a 20-character alphanumeric string.

     * **SQS Queue Secret Access Key** : An account access key that is a 40-character alphanumeric string.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`account` | `principal.group.product_object_id` | Directly mapped from the `account` field in the raw log.  
`column1` | `timestamp_epoch` | Directly mapped from the `column1` field in the raw log. Used to derive `metadata.event_timestamp`.  
`column10` | Varies | Can be `principal.process.command_line`, `object` or `number` depending on the log format.  
`column11` | `ddl` or `response` or `command_line2` | Can be `principal.resource.resource_subtype` (ddl), `security_result.outcomes.value` (response) or part of `principal.process.command_line` (command_line2) depending on the log format.  
`column12` | `operation` or `response` or `command_line3` | Can be `sr.summary` (operation), `security_result.outcomes.value` (response) or part of `principal.process.command_line` (command_line3) depending on the log format.  
`column13` | `database` or `response` | Can be `target.resource.name` (database) or `security_result.outcomes.value` (response) depending on the log format.  
`column14` | `object` | Directly mapped to `principal.resource.product_object_id` or `target_data.resource.name` depending on the log format.  
`column15` | `command_line` | Directly mapped to `principal.process.command_line`.  
`column16` | `response` | Directly mapped to `security_result.outcomes.value`.  
`column2` | `timestamp` or `timestamp_ms` | Directly mapped from the `column2` field in the raw log.  
`column3` | `ip` or `hostname` | Can be `principal.ip` or `principal.resource.name` depending on the log format.  
`column4` | `port` or `userid` | Can be `principal.port` or `principal.user.userid` depending on the log format.  
`column5` | `userid` or `ip` | Can be `principal.user.userid` or `principal.ip` depending on the log format.  
`column6` | `hostname` or `connection_id` | Can be `principal.resource.name` or `network.session_id` depending on the log format.  
`column7` | `connection_id` or `query_id` | Can be `network.session_id` or `principal.process.pid` depending on the log format.  
`column8` | `operation` | Directly mapped to `sr.summary` or `metadata.product_event_type`.  
`column9` | `query_id` or `database` | Can be `principal.process.pid` or `target_data.resource.name` depending on the log format.  
`command_line` | `principal.process.command_line` | Directly mapped from the extracted `command_line` field.  
`connection_id` | `network.session_id` | Directly mapped from the extracted `connection_id` field.  
`database` | `target.resource.name` | Directly mapped from the extracted `database` field. Derived from several fields like `operation`, `command_line`, `has_principal_user`, and `has_principal_machine` through conditional logic in the parser. Can be `RESOURCE_DELETION`, `RESOURCE_CREATION`, `RESOURCE_READ`, `RESOURCE_WRITTEN`, `USER_RESOURCE_ACCESS`, `USER_UNCATEGORIZED`, or `GENERIC_EVENT`. Hardcoded to "AWS_AURORA". Mapped from `column8` or derived from parser logic. Hardcoded to "AURORA". Hardcoded to "AMAZON".  
`has_principal_machine` | `has_principal_machine` | Set to "true" if `principal.ip` is present, otherwise initialized to "false".  
`has_principal_user` | `has_principal_user` | Set to "true" if `principal.user.userid` is present, otherwise initialized to "false".  
`hostname` | `principal.resource.name` | Directly mapped from the extracted `hostname` field.  
`ip` | `principal.ip` | Directly mapped from the extracted `ip` field.  
`logevent.id` | `security_result.detection_fields.value` | Nested within `target.logEvents.logEvents`, mapped with key "id".  
`logevent.message` | `security_result.detection_fields.value` | Nested within `target.logEvents.logEvents`, mapped with key "message". Used to extract `principal.ip`, `time_unix`, `operation`, and `user`.  
`logevent.timestamp` | `security_result.detection_fields.value` | Nested within `target.logEvents.logEvents`, mapped with key "timestamp".  
`object` | `target_data.resource.name` or `principal.resource.product_object_id` | Directly mapped from the extracted `object` field.  
`operation` | `sr.summary` | Directly mapped from the extracted `operation` field.  
`port` | `principal.port` | Directly mapped from the extracted `port` field.  
`query_id` | `principal.process.pid` | Directly mapped from the extracted `query_id` field.  
`response` | `security_result.outcomes.value` | Directly mapped from the extracted `response` field.  
`service` | `principal.application` | Directly mapped from the `service` field in the raw log.  
`src_ip` | `principal.ip` | Extracted from `logevent.message` within the nested `target.logEvents.logEvents` structure.  
`target.logEvents.logGroup` | `target.resource.attribute.labels.value` | Mapped with key "logGroup".  
`target.logEvents.logStream` | `target.resource.attribute.labels.value` | Mapped with key "logStream".  
`target.logEvents.messageType` | `target.resource.attribute.labels.value` | Mapped with key "messageType".  
`target.logEvents.owner` | `target.resource.attribute.labels.value` | Mapped with key "owner".  
`timestamp_epoch` | `metadata.event_timestamp` | Converted to `metadata.event_timestamp` using the `date` filter.  
`user` | `principal.user.userid` | Extracted from `logevent.message` within the nested `target.logEvents.logEvents` structure.  
`userid` | `principal.user.userid` | Directly mapped from the extracted `userid` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-aurora-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
