---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-lambda-function/
title: Collect AWS Lambda Function logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:32.648490+00:00
---

# Collect AWS Lambda Function logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-lambda-function/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Lambda Function logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Lambda Function logs to Google Security Operations using Amazon S3.

AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources. Lambda automatically sends all function logs (platform logs, extension logs, and application output) to Amazon CloudWatch Logs, creating a log group per function. This integration uses Amazon Data Firehose to stream Lambda log events from CloudWatch Logs to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **AWS Management Console** with permissions to manage: 
    * **AWS Lambda** (functions, logging configuration)
    * **Amazon CloudWatch Logs** (log groups, subscription filters)
    * **Amazon Data Firehose** (delivery streams)
    * **Amazon S3** (buckets)
    * **AWS IAM** (roles, policies, users)



## Verify the CloudWatch Logs log group for your Lambda function

  * AWS Lambda automatically creates a CloudWatch Logs log group for each function when it is first invoked. The default log group naming convention is:
        
        /aws/lambda/<function-name>
        




To verify:

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Search for `/aws/lambda/`.
  3. Confirm that a log group exists for each Lambda function whose logs you want to ingest.

**Note:** If you configured a custom log group for your Lambda function, use that log group name instead. Custom log group names are configured in the Lambda function's **Logging configuration** settings.



## Configure an AWS S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference (for example, `lambda-logs-to-secops`).



## Configure an IAM role for Amazon Data Firehose

Amazon Data Firehose requires an IAM role to write logs to your S3 bucket.

### Create the IAM policy

  1. In the **AWS Console** , go to **IAM > Policies > Create policy**.
  2. Select the **JSON** tab.
  3. Paste the following policy (replace `lambda-logs-to-secops` with your actual bucket name):
         
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
                         "arn:aws:s3:::lambda-logs-to-secops",
                         "arn:aws:s3:::lambda-logs-to-secops/*"
                     ]
                 },
                 {
                     "Sid": "CloudWatchLogging",
                     "Effect": "Allow",
                     "Action": [
                         "logs:PutLogEvents"
                     ],
                     "Resource": "arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/lambda-logs-to-secops:log-stream:*"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `LambdaLogsFirehoseS3Policy`.

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

  5. Search for and select **LambdaLogsFirehoseS3Policy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `LambdaLogsFirehoseToS3Role`.

  8. Click **Create role**.




## Create the Amazon Data Firehose stream

  1. Open the **Kinesis console** at <https://console.aws.amazon.com/kinesis>.
  2. In the navigation pane, select **Amazon Data Firehose**.
  3. Click **Create Firehose stream**.
  4. Under **Choose source and destination** , provide the following configuration: 
     * **Source** : Select **Direct PUT**.
     * **Destination** : Select **Amazon S3**.
  5. In the **Firehose stream name** field, enter `lambda-logs-to-secops`.
  6. Under **Transform records** , in the **Decompress source records from Amazon CloudWatch Logs** section:

     1. Select **Turn on decompression**.
     2. Do **not** select **Turn on message extraction**.
**Note:** Keeping message extraction disabled preserves CloudWatch metadata (logGroup, logStream, subscriptionFilters) in the delivered logs. The AWS_LAMBDA_FUNCTION parser supports the full CloudWatch Logs envelope format including the `logEvents` structure.
  7. Under **Destination settings** :

     * **S3 bucket** : Select the S3 bucket `lambda-logs-to-secops`.
     * **S3 bucket prefix** (optional): Enter `lambda-logs/`.
     * **S3 bucket error output prefix** (optional): Enter `firehose-errors/`.
  8. Under **Buffer hints** :

     * **Buffer size** : `5` MiB (default).
     * **Buffer interval** : `300` seconds (default).
  9. Under **Advanced settings** :

     * **Server-side encryption** : Optional. Enable if encryption is required.
     * **Error logging** : Select **Enabled** (recommended).
     * **Permissions** : Select **Choose existing IAM role** , then select `LambdaLogsFirehoseToS3Role`.
  10. Click **Create Firehose stream**.

  11. Wait for the stream **Status** to show **Active**.




## Configure an IAM role for CloudWatch Logs

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
                     "Resource": "arn:aws:firehose:<region>:<account-id>:deliverystream/lambda-logs-to-secops"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `LambdaLogsCWLtoFirehosePolicy`.

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

  5. Search for and select **LambdaLogsCWLtoFirehosePolicy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `LambdaLogsCWLtoFirehoseRole`.

  8. Click **Create role**.




## Create a CloudWatch Logs subscription filter

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Select the log group `/aws/lambda/<function-name>`.
  3. Select the **Subscription filters** tab.
  4. Click **Create > Create Amazon Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select the Firehose stream `lambda-logs-to-secops`.
     * **Grant permission** : Select the role `LambdaLogsCWLtoFirehoseRole`.
     * **Subscription filter name** : Enter a descriptive name (for example, `lambda-logs-to-secops-filter`).
     * **Log format** : Select **Other**.
     * **Subscription filter pattern** : Leave empty to send all Lambda function log events.
  6. Click **Start streaming**.

**Note:** Repeat steps 1-6 for each additional Lambda function log group you want to stream to Google SecOps. Each Lambda function has a separate log group at `/aws/lambda/<function-name>`. All subscription filters can use the same Firehose stream and IAM roles.



## Configure an IAM user for Google SecOps

Google SecOps needs an IAM user with access to the S3 bucket to ingest the delivered logs.

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



## Configure a feed in Google SecOps to ingest AWS Lambda Function logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **AWS Lambda Function** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields: 
     * **S3 URI** : `s3://lambda-logs-to-secops/lambda-logs/`
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
`Activity_id_label` | `additional.fields` | Merged  
`Arrays_label` | `additional.fields` | Merged  
`Name_label` | `additional.fields` | Merged  
`Type_1_label` | `additional.fields` | Merged  
`Type_id_label` | `additional.fields` | Merged  
`Type_label` | `additional.fields` | Merged  
`Uid_label` | `additional.fields` | Merged  
`Uid_label_1` | `additional.fields` | Merged  
`Value_label` | `additional.fields` | Merged  
`__type_label` | `additional.fields` | Merged  
`attempts_label` | `additional.fields` | Merged  
`class_name_label` | `additional.fields` | Merged  
`contentType_label` | `additional.fields` | Merged  
`env_label` | `additional.fields` | Merged  
`extendedRequestId_label` | `additional.fields` | Merged  
`feature_name_label` | `additional.fields` | Merged  
`line_number_label` | `additional.fields` | Merged  
`logType_label` | `additional.fields` | Merged  
`product_name_label` | `additional.fields` | Merged  
`requestid_label` | `additional.fields` | Merged  
`sourceAccount_label` | `additional.fields` | Merged  
`stack_label` | `additional.fields` | Merged  
`totalRetryDelay_label` | `additional.fields` | Merged  
`vendor_name_label` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`description` | `metadata.description` | Directly mapped  
`file_desc` | `metadata.description` | Directly mapped  
`Time` | `metadata.event_timestamp` | Parsed as `UNIX`  
`time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZ`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`, `true...  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`  
`Api.Operation` | `metadata.product_event_type` | Directly mapped  
`name` | `metadata.product_event_type` | Directly mapped  
`Api.Request.Uid` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`meta_data.requestId` | `metadata.product_log_id` | Directly mapped  
`Metadata.Version` | `metadata.product_version` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`meta_data.httpStatusCode` | `network.http.response_code` | Directly mapped  
`Http_request.User_agent` | `network.http.user_agent` | Directly mapped  
`Actor.Invoked_by` | `principal.administrative_domain` | Directly mapped  
`Src_endpoint.Domain` | `principal.asset.hostname` | Directly mapped  
`Src_endpoint.Domain` | `principal.hostname` | Directly mapped  
`Cloud.Region` | `principal.resource.attribute.cloud.availability_zone` | Directly mapped  
`Actor.User.Name` | `principal.user.userid` | Directly mapped  
`Status` | `security_result.action_details` | Directly mapped  
`Category_name` | `security_result.category_details` | Merged  
`error` | `security_result.description` | Directly mapped  
`errorMessage` | `security_result.description` | Directly mapped  
`Metadata_uid_label` | `security_result.detection_fields` | Merged  
`category_uid_label` | `security_result.detection_fields` | Merged  
`class_uid_label` | `security_result.detection_fields` | Merged  
`errorType_label` | `security_result.detection_fields` | Merged  
`event_code_label` | `security_result.detection_fields` | Merged  
`fault_label` | `security_result.detection_fields` | Merged  
`functionName_label` | `security_result.detection_fields` | Merged  
`severity_id_label` | `security_result.detection_fields` | Merged  
`sourceArn_label` | `security_result.detection_fields` | Merged  
`type_name_label` | `security_result.detection_fields` | Merged  
`type_uid_label` | `security_result.detection_fields` | Merged  
`user_type_label` | `security_result.detection_fields` | Merged  
`Severity` | `security_result.severity` | Mapped: `Informational` → `INFORMATIONAL`  
`severity` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`  
`msg` | `security_result.summary` | Directly mapped  
`Api.Service.Name` | `target.application` | Directly mapped  
`service` | `target.application` | Directly mapped  
`size` | `target.file.size` | Directly mapped  
`filename` | `target.process.file.full_path` | Directly mapped  
`Activity_name` | `target.resource.name` | Directly mapped  
`targetVar` | `target.resource.name` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `AWS_Lambda_Function`  
N/A | `metadata.vendor_name` | Constant: `AWS_Lambda_Function`  
N/A | `principal.resource.attribute.cloud.environment` | Constant: `AMAZON_WEB_SERVICES`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-lambda-function-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
