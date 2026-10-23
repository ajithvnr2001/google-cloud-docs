---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-emr/
title: Collect AWS Elastic MapReduce logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:34.258462+00:00
---

# Collect AWS Elastic MapReduce logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-emr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Elastic MapReduce logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Elastic MapReduce (EMR) logs to Google Security Operations. AWS EMR is a cloud-native big data platform that processes large amounts of data quickly. Integrating EMR logs into Google SecOps lets you analyze cluster activity and detect potential security threats.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



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



## How to configure AWS EMR to forward Logs

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type **EMR** and select **Amazon EMR** from the services list.
  3. Click **Clusters**.
  4. Find and select the **EMR cluster** for which you want to enable logging.
  5. Click **Edit** on the **Cluster details** page.
  6. In the **Edit Cluster** screen, go to the **Logging** section.
  7. Select **Enable** logging.
  8. Specify the **S3 bucket** where logs will be stored.
  9. Specify the **S3 URI** in the format `s3://your-bucket-name/` (this will store all EMR logs in the root of the bucket).
  10. Select the following log types: 
     * `Step logs`
     * `Application logs`
     * `YARN logs`
     * `System logs`
     * `HDFS Logs` (if you are using Hadoop)
  11. Click **Save**. 



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS EMR feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS EMR** log type.
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
`app_id` | `additional.fields[].key` | The value "APP" is assigned via parser  
`app_id` | `additional.fields[].value.string_value` | Directly mapped from the `APP` field in the raw log.  
`app_name` | `additional.fields[].key` | The value "APPNAME" is assigned via parser  
`app_name` | `additional.fields[].value.string_value` | Directly mapped from the `APPNAME` field in the raw log.  
`blockid` | `additional.fields[].key` | The value "blockid" is assigned via parser  
`blockid` | `additional.fields[].value.string_value` | Directly mapped from the `blockid` field in the raw log.  
`bytes` | `network.received_bytes` | Directly mapped from the `bytes` field in the raw log, converted to an unsigned integer.  
`cliID` | `additional.fields[].key` | The value "cliID" is assigned via parser  
`cliID` | `additional.fields[].value.string_value` | Directly mapped from the `cliID` field in the raw log.  
`cmd` | `target.process.command_line` | Directly mapped from the `cmd` field in the raw log.  
`comp_name` | `additional.fields[].key` | The value "COMP" is assigned via parser  
`comp_name` | `additional.fields[].value.string_value` | Directly mapped from the `COMP` field in the raw log.  
`configuration_version` | `additional.fields[].key` | The value "configuration_version" is assigned via parser  
`configuration_version` | `additional.fields[].value.string_value` | Directly mapped from the `configuration_version` field in the raw log, converted to a string.  
`containerID` | `additional.fields[].key` | The value "containerID" is assigned via parser  
`containerID` | `additional.fields[].value.string_value` | Directly mapped from the `CONTAINERID` field in the raw log.  
`description` | `security_result.description` | Directly mapped from the `description` field in the raw log.  
`dfs.FSNamesystem.*` | `additional.fields[].key` | Key is generated by concatenating "dfs.FSNamesystem." with the key from the JSON data.  
`dfs.FSNamesystem.*` | `additional.fields[].value.string_value` | Value is directly mapped from the corresponding value in the `dfs.FSNamesystem` JSON object, converted to a string.  
`duration` | `additional.fields[].key` | The value "duration" is assigned via parser  
`duration` | `additional.fields[].value.string_value` | Directly mapped from the `duration` field in the raw log.  
`duration` | `network.session_duration.seconds` | Directly mapped from the `duration` field in the raw log, converted to an integer.  
`environment` | `additional.fields[].key` | The value "environment" is assigned via parser  
`environment` | `additional.fields[].value.string_value` | Directly mapped from the `environment` field in the raw log. Extracted from the `ip_port` field using grok and string manipulation. Extracted from the `ip_port` field using grok and string manipulation, converted to an integer.  
`event_type` | `metadata.event_type` | Determined by parser logic based on the presence of `principal` and `target` information. Can be `NETWORK_CONNECTION`, `USER_RESOURCE_ACCESS`, `STATUS_UPDATE`, or `GENERIC_EVENT`.  
`file_path` | `target.file.full_path` | Directly mapped from the `file_path` field in the raw log.  
`host` | `principal.hostname` | Directly mapped from the `host` field in the raw log.  
`host` | `target.hostname` | Directly mapped from the `host` field in the raw log.  
`host_ip` | `principal.ip` | Directly mapped from the `host_ip` field in the raw log.  
`host_port` | `principal.port` | Directly mapped from the `host_port` field in the raw log, converted to an integer.  
`http_url` | `target.url` | Directly mapped from the `http_url` field in the raw log.  
`index` | `additional.fields[].key` | The value "index" is assigned via parser  
`index` | `additional.fields[].value.string_value` | Directly mapped from the `index` field in the raw log.  
`kind` | `metadata.product_event_type` | Directly mapped from the `kind` field in the raw log. The value "AWS_EMR" is assigned via parser The value "AWS EMR" is assigned via parser The value "AMAZON" is assigned via parser  
`offset` | `additional.fields[].key` | The value "offset" is assigned via parser  
`offset` | `additional.fields[].value.string_value` | Directly mapped from the `offset` field in the raw log.  
`op` | `metadata.product_event_type` | Directly mapped from the `op` or `OPERATION` field in the raw log.  
`proto` | `network.application_protocol` | Extracted from the `http_url` field using grok, converted to uppercase.  
`puppet_version` | `additional.fields[].key` | The value "puppet_version" is assigned via parser  
`puppet_version` | `additional.fields[].value.string_value` | Directly mapped from the `puppet_version` field in the raw log.  
`queue_name` | `additional.fields[].key` | The value "queue_name" is assigned via parser  
`queue_name` | `additional.fields[].value.string_value` | Directly mapped from the `queue_name` field in the raw log.  
`report_format` | `additional.fields[].key` | The value "report_format" is assigned via parser  
`report_format` | `additional.fields[].value.string_value` | Directly mapped from the `report_format` field in the raw log, converted to a string.  
`resource` | `additional.fields[].key` | The value "resource" is assigned via parser  
`resource` | `additional.fields[].value.string_value` | Directly mapped from the `resource` field in the raw log.  
`result` | `security_result.action_details` | Directly mapped from the `RESULT` field in the raw log.  
`security_id` | `additional.fields[].key` | The value "security_id" is assigned via parser  
`security_id` | `additional.fields[].value.string_value` | Directly mapped from the `security_id` field in the raw log.  
`severity` | `security_result.severity` | Mapped from the `severity` field in the raw log. `INFO` is mapped to `INFORMATIONAL`, `WARN` is mapped to `MEDIUM`.  
`srvID` | `additional.fields[].key` | The value "srvID" is assigned via parser  
`srvID` | `additional.fields[].value.string_value` | Directly mapped from the `srvID` field in the raw log.  
`status` | `additional.fields[].key` | The value "status" is assigned via parser  
`status` | `additional.fields[].value.string_value` | Directly mapped from the `status` field in the raw log.  
`summary` | `security_result.summary` | Directly mapped from the `summary` field in the raw log.  
`target_app` | `target.application` | Directly mapped from the `TARGET` field in the raw log.  
`target_ip` | `target.ip` | Directly mapped from the `target_ip` or `IP` field in the raw log.  
`target_port` | `target.port` | Directly mapped from the `target_port` field in the raw log, converted to an integer.  
`timestamp` | `metadata.event_timestamp` | Directly mapped from the `timestamp` field in the raw log, parsed as an ISO8601 timestamp.  
`timestamp` | `event.timestamp` | Directly mapped from the `timestamp` field in the raw log, parsed as an ISO8601 timestamp.  
`trade_date` | `additional.fields[].key` | The value "trade_date" is assigned via parser  
`trade_date` | `additional.fields[].value.string_value` | Directly mapped from the `trade_date` field in the raw log.  
`transaction_uuid` | `additional.fields[].key` | The value "transaction_uuid" is assigned via parser  
`transaction_uuid` | `additional.fields[].value.string_value` | Directly mapped from the `transaction_uuid` field in the raw log.  
`type` | `additional.fields[].key` | The value "type" is assigned via parser  
`type` | `additional.fields[].value.string_value` | Directly mapped from the `type` field in the raw log.  
`user` | `target.user.userid` | Directly mapped from the `USER` or `ugi` field in the raw log.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-emr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
