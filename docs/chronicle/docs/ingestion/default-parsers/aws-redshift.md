---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-redshift/
title: Collect AWS Redshift logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:43.647524+00:00
---

# Collect AWS Redshift logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-redshift/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Redshift logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Redshift logs to Google Security Operations using Amazon S3.

Amazon Redshift is a fully managed, petabyte-scale cloud data warehouse service from Amazon Web Services. It enables fast querying and analytics across large datasets using SQL-based tools and business intelligence applications. Amazon Redshift logs database activity including authentication attempts, connections, disconnections, user definition changes, and queries run against the database. This integration uses Amazon Redshift's native audit logging feature to deliver log files to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **AWS Management Console** with permissions to manage: 
    * **Amazon Redshift** (clusters, parameter groups)
    * **Amazon S3** (buckets, bucket policies)
    * **AWS IAM** (users, policies)



## Configure an S3 bucket for Amazon Redshift audit logging

Amazon Redshift uploads audit log files to an S3 bucket. You must configure the S3 bucket policy to allow the Amazon Redshift service to write log files.

### Create and configure the S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference (for example, `redshift-audit-logs-to-secops`).

**Note:** The S3 bucket must be in the same AWS Region as the Amazon Redshift cluster. The bucket must use Amazon S3-managed keys (SSE-S3) encryption (AES-256) and must not have S3 Object Lock enabled.
  3. Select the created bucket in the **Amazon S3 console** at <https://console.aws.amazon.com/s3>.

  4. Select the **Permissions** tab.

  5. In the **Bucket policy** section, click **Edit**.

  6. Add the following bucket policy (replace `redshift-audit-logs-to-secops` with your bucket name):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "Put bucket policy needed for audit logging",
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "redshift.amazonaws.com"
                     },
                     "Action": [
                         "s3:PutObject",
                         "s3:GetBucketAcl"
                     ],
                     "Resource": [
                         "arn:aws:s3:::redshift-audit-logs-to-secops",
                         "arn:aws:s3:::redshift-audit-logs-to-secops/*"
                     ]
                 }
             ]
         }
         

**Note:** For AWS Regions that are not enabled by default (opt-in Regions), use a Region-specific service principal name in the format `redshift.<region>.amazonaws.com` (for example, `redshift.ap-east-1.amazonaws.com`).
  7. Click **Save changes**.




## Enable the user activity log parameter

The connection log and user log are captured automatically when audit logging is enabled. To also capture the user activity log (which records each query before it runs on the database), you must enable the `enable_user_activity_logging` database parameter.

  1. Sign in to the **Amazon Redshift console** at <https://console.aws.amazon.com/redshiftv2/>.
  2. On the navigation menu, go to **Configurations > Workload management**.
  3. Select the parameter group associated with your cluster.
  4. Select the **Parameters** tab.
  5. Click **Edit parameters**.
  6. Set the **enable_user_activity_logging** parameter value to **true**.
  7. Click **Save**.

**Note:** If you modify the parameter group of an active cluster, reboot the cluster for the changes to take effect.



## Enable Amazon Redshift audit logging to S3

  1. Sign in to the **Amazon Redshift console** at <https://console.aws.amazon.com/redshiftv2/>.
  2. On the navigation menu, select **Clusters** , then select the cluster that you want to configure.
  3. Select the **Properties** tab.
  4. In the **Database configurations** panel, click **Edit** , then select **Edit audit logging**.
  5. On the **Edit audit logging** page, select **Turn on**.
  6. For **Log destination** , select **S3 bucket**.
  7. For **S3 bucket** , select the bucket you configured (for example, `redshift-audit-logs-to-secops`).
  8. Optional: Enter an **S3 key prefix** to organize the log files within the bucket (for example, `audit-logs/`).
  9. Select the logs to export: 
     * **Connection log** \- authentication attempts, connections, and disconnections
     * **User log** \- changes to database user definitions
     * **User activity log** \- each query before it runs on the database
  10. Click **Save changes**.



For more information, see [Database audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html) in the Amazon Redshift Management Guide.

## Configure an IAM user for Google SecOps

Google SecOps needs an IAM user with read access to the S3 bucket to ingest the exported audit logs.

  1. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select **Security credentials** tab.
  4. Click **Create Access Key** in section **Access Keys**.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**. 
     * Optional: Add description tag.
  7. Click **Create access key**.
  8. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  9. Click **Done**.
  10. Select **Permissions** tab.
  11. Click **Add permissions** in section **Permissions policies**.
  12. Select **Add permissions**.
  13. Select **Attach policies directly**.
  14. Search for **AmazonS3FullAccess** policy.
  15. Select the policy.
  16. Click **Next**.
  17. Click **Add permissions**.



## Configure a feed in Google SecOps to ingest AWS Redshift logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **AWS Redshift** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://redshift-audit-logs-to-secops/audit-logs/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`func_label` | `additional.fields` | Merged  
`lpclagg_label` | `additional.fields` | Merged  
`lpcltype_label` | `additional.fields` | Merged  
`msg` | `metadata.description` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_target_resource` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`column1` | `metadata.product_event_type` | Directly mapped  
`requestID` | `metadata.product_log_id` | Directly mapped  
`column20` | `network.application_protocol_version` | Directly mapped  
`column9` | `network.session_duration.seconds` | Renamed/mapped  
`column21` | `network.session_id` | Directly mapped  
`xid` | `network.session_id` | Directly mapped  
`column11` | `network.tls.cipher` | Directly mapped  
`column10` | `network.tls.version` | Directly mapped  
`column16` | `principal.application` | Directly mapped  
`column3` | `principal.asset.ip` | Merged  
`log_event.src_ip` | `principal.asset.ip` | Merged  
`column3` | `principal.hostname` | Directly mapped  
`column3` | `principal.ip` | Merged  
`log_event.src_ip` | `principal.ip` | Merged  
`region` | `principal.location.name` | Directly mapped  
`column17` | `principal.platform_version` | Directly mapped  
`column4` | `principal.port` | Directly mapped  
`column5` | `principal.process.pid` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`accountID` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`authmethod_label` | `security_result.detection_fields` | Merged  
`compression_label` | `security_result.detection_fields` | Merged  
`driver_version_label` | `security_result.detection_fields` | Merged  
`iamauthguid_label` | `security_result.detection_fields` | Merged  
`mtu_label` | `security_result.detection_fields` | Merged  
`plugin_name_label` | `security_result.detection_fields` | Merged  
`ssl_compression_label` | `security_result.detection_fields` | Merged  
`ssl_expansion_label` | `security_result.detection_fields` | Merged  
`level` | `security_result.severity` | Mapped: `(?i)Info` → `INFORMATIONAL`, `(?i)Error` → `ERROR`, `(?i)Warning` → `MEDIUM`  
`file` | `target.file.full_path` | Directly mapped  
`expected_bucket_label` | `target.resource.attribute.labels` | Merged  
`expected_s3_prefix_label` | `target.resource.attribute.labels` | Merged  
`sql_query_label` | `target.resource.attribute.labels` | Merged  
`time_zone_label` | `target.resource.attribute.labels` | Merged  
`ClusterIdentifier` | `target.resource.name` | Directly mapped  
`column6` | `target.resource.name` | Directly mapped  
`db` | `target.resource.name` | Directly mapped  
`column7` | `target.user.user_display_name` | Directly mapped  
`user` | `target.user.user_display_name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_RESOURCE_ACCESS`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.type` | Constant: `DATABASE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-redshift-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
