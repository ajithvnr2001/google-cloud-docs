---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ecs-metrics/
title: Collect AWS ECS Metrics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:31.355785+00:00
---

# Collect AWS ECS Metrics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ecs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS ECS Metrics logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS ECS Metrics logs to Google Security Operations using Amazon S3.

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you deploy, manage, and scale containerized applications. CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from ECS clusters, services, tasks, and containers, including CPU utilization, memory usage, network traffic, and storage I/O. This integration uses Amazon Data Firehose to stream Container Insights performance log events from CloudWatch Logs to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **AWS Management Console** with permissions to manage: 
    * **Amazon ECS** (clusters, account settings)
    * **Amazon CloudWatch Logs** (log groups, subscription filters)
    * **Amazon Data Firehose** (delivery streams)
    * **Amazon S3** (buckets)
    * **AWS IAM** (roles, policies, users)



## Enable Container Insights on Amazon ECS

Container Insights must be enabled to generate performance log events in CloudWatch Logs for your ECS clusters.

### Enable Container Insights at the account level

  1. Sign in to the **Amazon ECS console** at <https://console.aws.amazon.com/ecs/v2>.
  2. In the navigation pane, select **Account Settings**.
  3. Click **Update**.
  4. Select **Container Insights with enhanced observability**.
  5. Click **Save changes**.
  6. On the confirmation screen, click **Confirm**.

**Note:** After enabling the account setting, all new ECS clusters automatically use Container Insights with enhanced observability. Existing clusters require a separate update.



### Enable Container Insights on an existing cluster

  * To update an existing ECS cluster, run the following AWS CLI command (replace `your-cluster-name` with your cluster name):
        
        aws ecs update-cluster-settings --cluster your-cluster-name --settings name=containerInsights,value=enhanced
        

**Note:** Amazon ECS agent version 1.29 or later is required for EC2 launch type instances. Fargate launch type clusters do not require any agent updates.



### Verify the CloudWatch log group

  * After enabling Container Insights, Amazon ECS automatically creates a CloudWatch Logs log group with the following naming convention:
        
        /aws/ecs/containerinsights/your-cluster-name/performance
        




To verify:

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Search for `/aws/ecs/containerinsights/`.
  3. Confirm that a log group exists for each ECS cluster with Container Insights enabled.



## Configure an AWS S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference (for example, `ecs-metrics-to-secops`).



## Configure the IAM role for Amazon Data Firehose

Amazon Data Firehose requires an IAM role to write logs to your S3 bucket.

### Create the IAM policy

  1. In the **AWS Console** , go to **IAM > Policies > Create policy**.
  2. Select the **JSON** tab.
  3. Paste the following policy (replace `ecs-metrics-to-secops` with your actual bucket name):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Sid": "S3Delivery",
                     "Effect": "Allow",
                     "Action": [
                         "s3:AbortMultipartUpload",
                         "s3:GetBucketLocation",
                         "s3:GetObject",
                         "s3:ListBucket",
                         "s3:ListBucketMultipartUploads",
                         "s3:PutObject"
                     ],
                     "Resource": [
                         "arn:aws:s3:::ecs-metrics-to-secops",
                         "arn:aws:s3:::ecs-metrics-to-secops/*"
                     ]
                 },
                 {
                     "Sid": "CloudWatchLogging",
                     "Effect": "Allow",
                     "Action": [
                         "logs:PutLogEvents"
                     ],
                     "Resource": "arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/ecs-metrics-to-secops:log-stream:*"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `ECSMetricsFirehoseS3Policy`.

  6. Click **Create policy**.




### Create the IAM role

  1. Go to **IAM > Roles > Create role**.
  2. Select **Custom trust policy**.
  3. Paste the following trust policy:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "firehose.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  4. Click **Next**.

  5. Search for and select **ECSMetricsFirehoseS3Policy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `ECSMetricsFirehoseToS3Role`.

  8. Click **Create role**.




## Create the Amazon Data Firehose stream

  1. Open the **Kinesis console** at <https://console.aws.amazon.com/kinesis>.
  2. In the navigation pane, select **Amazon Data Firehose**.
  3. Click **Create Firehose stream**.
  4. Under **Choose source and destination** , provide the following configuration: 
     * **Source** : Select **Direct PUT**.
     * **Destination** : Select **Amazon S3**.
  5. In the **Firehose stream name** field, enter `ecs-metrics-to-secops`.
  6. Under **Transform records** , in the **Decompress source records from Amazon CloudWatch Logs** section:

     1. Select **Turn on decompression**.
     2. Do **not** select **Turn on message extraction**.
**Note:** Keeping message extraction disabled preserves CloudWatch metadata (logGroup, logStream, subscriptionFilters) in the delivered logs. The AWS_ECS_METRICS parser supports the full CloudWatch Logs envelope format including the `logEvents` structure.
  7. Under **Destination settings** :

     * **S3 bucket** : Select the S3 bucket `ecs-metrics-to-secops`.
     * **S3 bucket prefix** (optional): Enter `ecs-metrics/`.
     * **S3 bucket error output prefix** (optional): Enter `firehose-errors/`.
  8. Under **Buffer hints** :

     * **Buffer size** : `5` MiB (default).
     * **Buffer interval** : `300` seconds (default).
  9. Under **Advanced settings** :

     * **Server-side encryption** : Optional. Enable if encryption is required.
     * **Error logging** : Select **Enabled** (recommended).
     * **Permissions** : Select **Choose existing IAM role** , then select `ECSMetricsFirehoseToS3Role`.
  10. Click **Create Firehose stream**.

  11. Wait for the stream **Status** to show **Active**.




## Configure the IAM role for CloudWatch Logs

CloudWatch Logs requires an IAM role to send log data to the Firehose stream.

### Create the IAM policy

  1. Go to **IAM > Policies > Create policy**.
  2. Select the **JSON** tab.
  3. Paste the following policy (replace `<region>` and `<account-id>` with your AWS region and account ID):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": [
                         "firehose:PutRecord",
                         "firehose:PutRecordBatch"
                     ],
                     "Resource": "arn:aws:firehose:<region>:<account-id>:deliverystream/ecs-metrics-to-secops"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `ECSMetricsCWLtoFirehosePolicy`.

  6. Click **Create policy**.




### Create the IAM role

  1. Go to **IAM > Roles > Create role**.
  2. Select **Custom trust policy**.
  3. Paste the following trust policy (replace `<region>` with your AWS region):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Principal": {
                         "Service": "logs.<region>.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                 }
             ]
         }
         

  4. Click **Next**.

  5. Search for and select **ECSMetricsCWLtoFirehosePolicy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `ECSMetricsCWLtoFirehoseRole`.

  8. Click **Create role**.




## Create a CloudWatch Logs subscription filter

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Select the log group `/aws/ecs/containerinsights/your-cluster-name/performance`.
  3. Select the **Subscription filters** tab.
  4. Click **Create > Create Amazon Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select the Firehose stream `ecs-metrics-to-secops`.
     * **Grant permission** : Select the role `ECSMetricsCWLtoFirehoseRole`.
     * **Subscription filter name** : Enter a descriptive name (for example, `ecs-metrics-to-secops-filter`).
     * **Log format** : Select **Other**.
     * **Subscription filter pattern** : Leave empty to send all Container Insights performance events.
  6. Click **Start streaming**.

**Note:** Repeat steps 1-6 for each additional ECS cluster log group you want to stream to Google SecOps. Each cluster has a separate log group at `/aws/ecs/containerinsights/<cluster-name>/performance`. All subscription filters can use the same Firehose stream and IAM roles.



## Configure an IAM user for Google SecOps

Google SecOps needs an IAM user with access to the S3 bucket to ingest the delivered logs.

  1. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select **Security credentials** tab.
  4. Click **Create Access Key** in section **Access Keys**.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**. 
     * Optional: Add a description tag.
  7. Click **Create access key**.
  8. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  9. Click **Done**.
  10. Select **Permissions** tab.
  11. Click **Add permissions** in the **Permissions policies** section.
  12. Select **Add permissions**.
  13. Select **Attach policies directly**.
  14. Search for **AmazonS3FullAccess** policy.
  15. Select the policy.
  16. Click **Next**.
  17. Click **Add permissions**.



## Configure a feed in Google SecOps to ingest AWS ECS Metrics logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **AWS ECS Metrics** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields: 
     * **S3 URI** : `s3://ecs-metrics-to-secops/ecs-metrics/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next** and then click **Submit**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`cluster_rtt_ClusterId_label` | `additional.fields` | Merged  
`cluster_rtt_description_label` | `additional.fields` | Merged  
`compressed_label` | `additional.fields` | Merged  
`connectionID_localvalue_label` | `additional.fields` | Merged  
`connectionID_serverValue_label` | `additional.fields` | Merged  
`request_id_label` | `additional.fields` | Merged  
`source_label` | `additional.fields` | Merged  
`Time` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`, `true` → `NETWORK_CONNECTION`  
`connection` | `metadata.product_event_type` | Directly mapped  
`sent_bytes` | `network.sent_bytes` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`principal_ip` | `principal.asset.ip` | Merged  
`hostname` | `principal.hostname` | Directly mapped  
`principal_ip` | `principal.ip` | Merged  
`principal_port` | `principal.port` | Directly mapped  
`action` | `security_result.action` | Merged  
`severity` | `security_result.severity` | Mapped: `"ALERT", "EMERGENCY"` → `HIGH`, `"INFO", "NOTICE"` → `INFORMATIONAL`, `DEBUG` → `LO...  
`target_port` | `target.port` | Directly mapped  
`url` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-ecs-metrics-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
