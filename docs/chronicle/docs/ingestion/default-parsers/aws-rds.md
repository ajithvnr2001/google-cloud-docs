---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-rds/
title: Collect AWS RDS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:17.083298+00:00
---

# Collect AWS RDS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-rds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS RDS logs

**Parser Version:** 11.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect AWS RDS logs by setting up a Google SecOps feed.

For more information, see [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser that normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `AWS_RDS` ingestion label.

## Before you begin

Ensure you have the following prerequisites:

  * An AWS account that you can sign in to

  * A global administrator or RDS administrator




## How to configure AWS RDS

  1. Use an existing database or create a new database: 
     * To use an existing database, select the database, click **Modify** , and then select **Log exports**.
     * To use a new database, when you create the database, select **Additional configuration**.
  2. To publish to Amazon CloudWatch, select the following log types: 
     * **Audit log**
     * **Error log**
     * **General log**
     * **Slow query log**
  3. To specify log export for AWS Aurora PostgreSQL and PostgreSQL, select **PostgreSQL log**.
  4. To specify log export for AWS Microsoft SQL server, select the following log types: 
     * **Agent log**
     * **Error log**
  5. Save the log configuration.
  6. Select **CloudWatch > Logs** to view the collected logs. The log groups are automatically created after the logs are available through the instance.



To publish the logs to CloudWatch, configure IAM user and KMS key policies. For more information, see [IAM user and KMS key policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

Based on the service and region, identify the endpoints for connectivity by referring to the following AWS documentation:

  * For information about any logging sources, see [AWS Identity and Access Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iam-service.html).

  * For information about CloudWatch logging sources, see [CloudWatch logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html).




For engine-specific information, see the following documentation:

  * [Publishing MariaDB logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MariaDB.html#USER_LogAccess.MariaDB.PublishtoCloudWatchLogs).

  * [Publishing MySQL logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQLDB.PublishtoCloudWatchLogs.html).

  * [Publishing Oracle logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.Oracle.html#USER_LogAccess.Oracle.PublishtoCloudWatchLogs).

  * [Publishing PostgreSQL logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs).

  * [Publishing SQL Server logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.SQLServer.html#USER_LogAccess.SQLServer.PublishtoCloudWatchLogs).




## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS RDS feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS RDS** log type.
  3. Google SecOps supports log collection using an access key ID and secret method. To create the access key ID and secret, see [Configure tool authentication with AWS](https://docs.aws.amazon.com/powershell/latest/userguide/creds-idc.html).
  4. Specify the values in the following fields.

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
  5. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Field mapping reference

This parser extracts fields from AWS RDS syslog messages, primarily focusing on timestamp, description, and client IP. It uses grok patterns to identify these fields and populates corresponding UDM fields, classifying events as either `GENERIC_EVENT` or `STATUS_UPDATE` based on the presence of a client IP.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`client_ip` | `principal.ip` | Extracted from the raw log message using the regular expression `\\[CLIENT: %{IP:client_ip}\\]`.  
`create_time.nanos` | N/A | Not mapped to the IDM object.  
`create_time.seconds` | N/A | Not mapped to the IDM object.  
| `metadata.description` | The descriptive message from the log, extracted using grok patterns. Copied from `create_time.nanos`. Copied from `create_time.seconds`. Set to "GENERIC_EVENT" by default. Changed to "STATUS_UPDATE" if `client_ip` is present. Static value "AWS_RDS", set by the parser. Static value "AWS_RDS", set by the parser.  
`pid` | `principal.process.pid` | Extracted from the `descrip` field using the regular expression `process ID of %{INT:pid}`.  
`prin_namespace` | `event.idm.read_only_udm.principal.namespace` | Mapped from changelog  
`connection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`clientApplication` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`serverHost` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`commandText` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`objectType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`objectName` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`rowCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`errorMessage` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`command` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`rawData` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attemptsMade` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attemptEndingTimestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`errorCode` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`errorMessage` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`lambdaARN` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`arrivalTimestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`exitCode` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`prod_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`arn` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`PROTOCOL` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`address_data.HOST` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`address_data.HOST` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`SID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`USER` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`connect_data.HOST` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`connect_data.HOST` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`PROGRAM` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`action_details` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`src_port` | `principal.port` | Mapped from changelog  
`user_name` | `principal.user.user_display_name` | Mapped from changelog  
`database_name` | `target.resource.name` | Mapped from changelog  
`owner` | `principal.user.userid` | Mapped from changelog  
`logGroup` | `security_result.about.resource.name` | Mapped from changelog  
`logStream` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`logevent.id` | `metadata.product_log_id` | Mapped from changelog  
`logevent.message` | `security_result.description` | Mapped from changelog  
`resource_name` | `target.resource.name` | Mapped from changelog  
`src_ip` | `principal.ip` | Mapped from changelog  
`tar_ip` | `target.ip` | Mapped from changelog  
`tar_host` | `target.hostname` | Mapped from changelog  
`subscriptionFilters` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`type` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-rds-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
