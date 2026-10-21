---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudwatch/
title: Collect AWS CloudWatch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:37:02.640877+00:00
---

# Collect AWS CloudWatch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-cloudwatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS CloudWatch logs

**Parser Version:** 18.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS CloudWatch logs to Google Security Operations using Amazon S3.

AWS CloudWatch is a monitoring and observability service that collects operational data in the form of logs, metrics, and events from AWS resources and applications. This integration uses Amazon Data Firehose to stream CloudWatch log data to an S3 bucket, which Google SecOps then ingests using an Amazon S3 V2 feed.

## Before you begin

  * A Google SecOps instance
  * Privileged access to the **AWS Management Console** with permissions to manage: 
    * **Amazon CloudWatch Logs** (log groups, subscription filters)
    * **Amazon Data Firehose** (delivery streams)
    * **Amazon S3** (buckets)
    * **AWS IAM** (roles, policies, users)



## Configure AWS S3 bucket

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for future reference (for example, `cwlogs-to-secops`).



## Configure the IAM role for Amazon Data Firehose

Amazon Data Firehose requires an IAM role to write logs to your S3 bucket.

### Create the IAM policy

  1. In the **AWS Console** , go to **IAM > Policies > Create policy**.
  2. Select the **JSON** tab.
  3. Paste the following policy (replace `cwlogs-to-secops` with your actual bucket name):
         
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
                         "arn:aws:s3:::cwlogs-to-secops",
                         "arn:aws:s3:::cwlogs-to-secops/*"
                     ]
                 },
                 {
                     "Sid": "CloudWatchLogging",
                     "Effect": "Allow",
                     "Action": [
                         "logs:PutLogEvents"
                     ],
                     "Resource": "arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/cwlogs-to-secops:log-stream:*"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `FirehoseS3DeliveryPolicy`.

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

  5. Search for and select **FirehoseS3DeliveryPolicy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `FirehoseToS3Role`.

  8. Click **Create role**.




## Create the Amazon Data Firehose stream

  1. Open the **Kinesis console** at <https://console.aws.amazon.com/kinesis>.
  2. In the navigation pane, select **Amazon Data Firehose**.
  3. Click **Create Firehose stream**.
  4. Under **Choose source and destination** , provide the following configuration: 
     * **Source** : Select **Direct PUT**.
     * **Destination** : Select **Amazon S3**.
  5. In the **Firehose stream name** field, enter `cwlogs-to-secops`.
  6. Under **Transform records** , in the **Decompress source records from Amazon CloudWatch Logs** section:

     1. Select **Turn on decompression**.
     2. Do **not** select **Turn on message extraction**.
**Note:** Keeping message extraction disabled preserves CloudWatch metadata (logGroup, logStream, subscriptionFilters) in the delivered logs. The AWS_CLOUDWATCH parser supports the full CloudWatch Logs envelope format including the `logEvents` structure.
  7. Under **Destination settings** :

     * **S3 bucket** : Select the S3 bucket `cwlogs-to-secops`.
     * **S3 bucket prefix** (optional): Enter `cloudwatch-logs/`.
     * **S3 bucket error output prefix** (optional): Enter `firehose-errors/`.
  8. Under **Buffer hints** :

     * **Buffer size** : `5` MiB (default).
     * **Buffer interval** : `300` seconds (default).
  9. Under **Advanced settings** :

     * **Server-side encryption** : Optional. Enable if encryption is required.
     * **Error logging** : Select **Enabled** (recommended).
     * **Permissions** : Select **Choose existing IAM role** , then select `FirehoseToS3Role`.
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
                     "Resource": "arn:aws:firehose:<region>:<account-id>:deliverystream/cwlogs-to-secops"
                 }
             ]
         }
         

  4. Click **Next**.

  5. In the **Policy name** field, enter `CWLtoFirehoseWritePolicy`.

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

  5. Search for and select **CWLtoFirehoseWritePolicy**.

  6. Click **Next**.

  7. In the **Role name** field, enter `CWLtoFirehoseRole`.

  8. Click **Create role**.




## Create CloudWatch Logs subscription filter

  1. In the **AWS Console** , go to **CloudWatch > Logs > Log groups**.
  2. Select the target log group that you want to stream to Google SecOps.
  3. Select the **Subscription filters** tab.
  4. Click **Create > Create Amazon Data Firehose subscription filter**.
  5. Provide the following configuration details: 
     * **Destination** : Select the Firehose stream `cwlogs-to-secops`.
     * **Grant permission** : Select the role `CWLtoFirehoseRole`.
     * **Subscription filter name** : Enter a descriptive name (for example, `secops-all-events`).
     * **Log format** : Select **Other**.
     * **Subscription filter pattern** : Leave empty to send all events, or enter a filter pattern to send only specific events.
  6. Click **Start streaming**.

**Note:** Repeat steps 1-6 for each additional log group you want to stream to Google SecOps. All subscription filters can use the same Firehose stream and IAM roles.



## Configure IAM user for Google SecOps

Google SecOps needs an IAM user with access to the S3 bucket to ingest the delivered logs.

  1. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  2. Select the created **User**.
  3. Select **Security credentials** tab.
  4. Click **Create Access Key** in section **Access Keys**.
  5. Select **Third-party service** as **Use case**.
  6. Click **Next**.
  7. Optional: Add description tag.
  8. Click **Create access key**.
  9. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  10. Click **Done**.
  11. Select **Permissions** tab.
  12. Click **Add permissions** in section **Permissions policies**.
  13. Select **Add permissions**.
  14. Select **Attach policies directly**.
  15. Search for **AmazonS3FullAccess** policy.
  16. Select the policy.
  17. Click **Next**.
  18. Click **Add permissions**.



## Configure a feed in Google SecOps to ingest AWS CloudWatch logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **AWS CloudWatch** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields: 
     * **S3 URI** : `s3://cwlogs-to-secops/cloudwatch-logs/`
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next** and then click **Submit**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`account` | `principal.user.userid` | The value of `account` from the raw log is mapped to the `principal.user.userid` field.  
`account_id` | `principal.user.userid` | The value of `account_id` from the raw log is mapped to the `principal.user.userid` field.  
`AlertId` | `metadata.product_log_id` | The value of `AlertId` from the raw log is mapped to the `metadata.product_log_id` field.  
`arrivalTimestamp` | `metadata.event_timestamp` | The value of `arrivalTimestamp` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp` field.  
`attemptsMade` | `additional.fields` | The value of `attemptsMade` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "Attempts Made".  
`awsAccountId` | `principal.asset_id` | The value of `awsAccountId` from the raw log is prepended with "AWS Account id: " and mapped to the `principal.asset_id` field.  
`billed_duration` | `additional.fields` | The value of `billed_duration` from the raw log is added as a key-value pair to the `additional.fields` with the key "billed_duration".  
`BytesIn` | `network.received_bytes` | The value of `BytesIn` from the raw log is converted to an unsigned integer and mapped to the `network.received_bytes` field.  
`cipher` | `network.tls.cipher` | The value of `cipher` from the raw log is mapped to the `network.tls.cipher` field.  
`Ciphers` | `network.tls.client.supported_ciphers` | The value of `Ciphers` from the raw log is split by commas and each value is added to the `network.tls.client.supported_ciphers` array.  
`cloudwatchLog` | `security_result.description` | The value of `cloudwatchLog` from the raw log is mapped to the `security_result.description` field.  
`CloudAccountId` | `metadata.product_deployment_id` | The value of `CloudAccountId` from the raw log is mapped to the `metadata.product_deployment_id` field.  
`CloudType` | `target.resource.attribute.cloud.environment` | The value of `CloudType` from the raw log determines the value of `target.resource.attribute.cloud.environment`. If `CloudType` is "gcp", the value is "GOOGLE_CLOUD_PLATFORM". If `CloudType` is "aws", the value is "AMAZON_WEB_SERVICES". If `CloudType` is "azure", the value is "MICROSOFT_AZURE".  
`Context.Execution.Id` | `target.resource.attribute.labels` | The value of `Context.Execution.Id` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Context Id".  
`Context.Execution.Name` | `target.resource.attribute.labels` | The value of `Context.Execution.Name` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Context Name".  
`Context.Execution.RoleArn` | `target.resource.product_object_id` | The value of `Context.Execution.RoleArn` from the raw log is mapped to the `target.resource.product_object_id` field.  
`descr` | `metadata.description` | The value of `descr` from the raw log, after removing extra whitespace, is mapped to the `metadata.description` field unless it is "-". If `descr` is empty, the value of `log` is used instead.  
`destination.name` | `target.location.country_or_region` | The value of `destination.name` from the raw log is mapped to the `target.location.country_or_region` field.  
`destination.properties.prefix` | `target.resource.attribute.labels` | The value of `destination.properties.prefix` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Destination properties prefix".  
`detail.additionalEventData.configRuleArn` | `security_result.rule_id` | The value of `detail.additionalEventData.configRuleArn` from the raw log is mapped to the `security_result.rule_id` field.  
`detail.additionalEventData.configRuleName` | `security_result.rule_name` | The value of `detail.additionalEventData.configRuleName` from the raw log is mapped to the `security_result.rule_name` field.  
`detail.additionalEventData.managedRuleIdentifier` | `additional.fields` | The value of `detail.additionalEventData.managedRuleIdentifier` from the raw log is added as a key-value pair to the `additional.fields` with the key "managedRuleIdentifier".  
`detail.additionalEventData.notificationJobType` | `additional.fields` | The value of `detail.additionalEventData.notificationJobType` from the raw log is added as a key-value pair to the `additional.fields` with the key "notificationJobType".  
`detail.awsAccountId` | `principal.asset_id` | The value of `detail.awsAccountId` from the raw log is prepended with "AWS Account id: " and mapped to the `principal.asset_id` field.  
`detail.awsRegion` | `principal.location.name` | The value of `detail.awsRegion` from the raw log is mapped to the `principal.location.name` field.  
`detail.configRuleArn` | `security_result.rule_id` | The value of `detail.configRuleArn` from the raw log is mapped to the `security_result.rule_id` field.  
`detail.configRuleName` | `security_result.rule_name` | The value of `detail.configRuleName` from the raw log is mapped to the `security_result.rule_name` field.  
`detail.configurationItem.awsAccountId` | `principal.user.userid` | The value of `detail.configurationItem.awsAccountId` from the raw log is mapped to the `principal.user.userid` field.  
`detail.configurationItem.awsRegion` | `target.location.country_or_region` | The value of `detail.configurationItem.awsRegion` from the raw log is mapped to the `target.location.country_or_region` field.  
`detail.configurationItem.configuration.complianceType` | `security_result.summary` | The value of `detail.configurationItem.configuration.complianceType` from the raw log is mapped to the `security_result.summary` field.  
`detail.configurationItem.configuration.targetResourceId` | `target.resource.attribute.labels` | The value of `detail.configurationItem.configuration.targetResourceId` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "configurationItem configuration targetResourceId".  
`detail.configurationItem.configuration.targetResourceType` | `target.resource.attribute.labels` | The value of `detail.configurationItem.configuration.targetResourceType` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "configurationItem configuration targetResourceType".  
`detail.configurationItem.configurationItemCaptureTime` | `_target.asset.attribute.creation_time` | The value of `detail.configurationItem.configurationItemCaptureTime` from the raw log is converted to a timestamp and mapped to the `_target.asset.attribute.creation_time` field.  
`detail.configurationItem.configurationItemStatus` | `target.resource.attribute.labels` | The value of `detail.configurationItem.configurationItemStatus` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "configurationItem configurationItemStatus".  
`detail.configurationItem.configurationStateId` | `target.resource.attribute.labels` | The value of `detail.configurationItem.configurationStateId` from the raw log is converted to a string and added as a key-value pair to the `target.resource.attribute.labels` with the key "configurationItem configurationStateId".  
`detail.configurationItem.resourceId` | `target.resource.id` | The value of `detail.configurationItem.resourceId` from the raw log is mapped to the `target.resource.id` field.  
`detail.configurationItem.resourceType` | `target.resource.resource_subtype` | The value of `detail.configurationItem.resourceType` from the raw log is mapped to the `target.resource.resource_subtype` field.  
`detail.configurationItemDiff.changedProperties.Configuration.configRuleList.1.updatedValue.configRuleArn` | `security_result.rule_id` | The value of `detail.configurationItemDiff.changedProperties.Configuration.configRuleList.1.updatedValue.configRuleArn` from the raw log is mapped to the `security_result.rule_id` field.  
`detail.eventCategory` | `security_result.category_details` | The value of `detail.eventCategory` from the raw log is mapped to the `security_result.category_details` field.  
`detail.eventID` | `metadata.product_log_id` | The value of `detail.eventID` from the raw log is mapped to the `metadata.product_log_id` field.  
`detail.eventName` | `additional.fields` | The value of `detail.eventName` from the raw log is added as a key-value pair to the `additional.fields` with the key "Event Name".  
`detail.eventSource` | `target.application` | The value of `detail.eventSource` from the raw log is mapped to the `target.application` field.  
`detail.eventType` | `additional.fields` | The value of `detail.eventType` from the raw log is added as a key-value pair to the `additional.fields` with the key "Event Type".  
`detail.eventVersion` | `metadata.product_version` | The value of `detail.eventVersion` from the raw log is mapped to the `metadata.product_version` field.  
`detail.managementEvent` | `additional.fields` | The value of `detail.managementEvent` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "detail managementEvent".  
`detail.messageType` | `target.resource.attribute.labels` | The value of `detail.messageType` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Message Type".  
`detail.newEvaluationResult.complianceType` | `security_result.summary` | The value of `detail.newEvaluationResult.complianceType` from the raw log is mapped to the `security_result.summary` field.  
`detail.newEvaluationResult.configRuleInvokedTime` | `additional.fields` | The value of `detail.newEvaluationResult.configRuleInvokedTime` from the raw log is added as a key-value pair to the `additional.fields` with the key "newEvaluationResult_configRuleInvokedTime".  
`detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName` | `additional.fields` | The value of `detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName` from the raw log is added as a key-value pair to the `additional.fields` with the key "newEvaluationResult_configRuleName".  
`detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId` | `additional.fields` | The value of `detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId` from the raw log is added as a key-value pair to the `additional.fields` with the key "newEvaluationResult_resourceId".  
`detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType` | `additional.fields` | The value of `detail.newEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType` from the raw log is added as a key-value pair to the `additional.fields` with the key "newEvaluationResult_resourceType".  
`detail.newEvaluationResult.resultRecordedTime` | `additional.fields` | The value of `detail.newEvaluationResult.resultRecordedTime` from the raw log is added as a key-value pair to the `additional.fields` with the key "newEvaluationResult_resultRecordedTime".  
`detail.oldEvaluationResult.configRuleInvokedTime` | `additional.fields` | The value of `detail.oldEvaluationResult.configRuleInvokedTime` from the raw log is added as a key-value pair to the `additional.fields` with the key "oldEvaluationResult_configRuleInvokedTime".  
`detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName` | `additional.fields` | The value of `detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.configRuleName` from the raw log is added as a key-value pair to the `additional.fields` with the key "oldEvaluationResult_configRuleName".  
`detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId` | `additional.fields` | The value of `detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceId` from the raw log is added as a key-value pair to the `additional.fields` with the key "oldEvaluationResult_resourceId".  
`detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType` | `additional.fields` | The value of `detail.oldEvaluationResult.evaluationResultIdentifier.evaluationResultQualifier.resourceType` from the raw log is added as a key-value pair to the `additional.fields` with the key "oldEvaluationResult_resourceType".  
`detail.oldEvaluationResult.resultRecordedTime` | `additional.fields` | The value of `detail.oldEvaluationResult.resultRecordedTime` from the raw log is added as a key-value pair to the `additional.fields` with the key "oldEvaluationResult_resultRecordedTime".  
`detail.readOnly` | `additional.fields` | The value of `detail.readOnly` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "detail readOnly".  
`detail.recipientAccountId` | `target.resource.attribute.labels` | The value of `detail.recipientAccountId` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Recipient Account Id".  
`detail.recordVersion` | `metadata.product_version` | The value of `detail.recordVersion` from the raw log is mapped to the `metadata.product_version` field.  
`detail.requestID` | `target.resource.attribute.labels` | The value of `detail.requestID` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Detail Request ID".  
`detail.resourceType` | `target.resource.resource_subtype` | The value of `detail.resourceType` from the raw log is mapped to the `target.resource.resource_subtype` field.  
`detail.s3Bucket` | `about.resource.name` | The value of `detail.s3Bucket` from the raw log is mapped to the `about.resource.name` field.  
`detail.s3ObjectKey` | `target.resource.attribute.labels` | The value of `detail.s3ObjectKey` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "s3ObjectKey".  
`detail.userAgent` | `network.http.user_agent` | The value of `detail.userAgent` from the raw log is mapped to the `network.http.user_agent` field.  
`detail.userIdentity.accessKeyId` | `target.user.userid` | The value of `detail.userIdentity.accessKeyId` from the raw log is mapped to the `target.user.userid` field.  
`detail.userIdentity.accountId` | `metadata.product_deployment_id` | The value of `detail.userIdentity.accountId` from the raw log is mapped to the `metadata.product_deployment_id` field.  
`detail.userIdentity.arn` | `target.user.userid` | The value of `detail.userIdentity.arn` from the raw log is mapped to the `target.user.userid` field.  
`detail.userIdentity.principalId` | `principal.user.product_object_id` | The value of `detail.userIdentity.principalId` from the raw log is mapped to the `principal.user.product_object_id` field.  
`detail.userIdentity.sessionContext.attributes.mfaAuthenticated` | `principal.user.attribute.labels` | The value of `detail.userIdentity.sessionContext.attributes.mfaAuthenticated` from the raw log is added as a key-value pair to the `principal.user.attribute.labels` with the key "mfaAuthenticated".  
`detail.userIdentity.sessionContext.sessionIssuer.userName` | `target.user.user_display_name` | The value of `detail.userIdentity.sessionContext.sessionIssuer.userName` from the raw log is mapped to the `target.user.user_display_name` field.  
`detail.userIdentity.type` | `principal.resource.type` | The value of `detail.userIdentity.type` from the raw log is mapped to the `principal.resource.type` field.  
`detail-type` | `metadata.product_event_type` | The value of `detail-type` from the raw log is mapped to the `metadata.product_event_type` field.  
`device` | `principal.asset.product_object_id` | The value of `device` from the raw log is mapped to the `principal.asset.product_object_id` field.  
`digestPublicKeyFingerprint` | `target.file.sha1` | The value of `digestPublicKeyFingerprint` from the raw log is mapped to the `target.file.sha1` field.  
`digestS3Bucket` | `principal.resource.name` | The value of `digestS3Bucket` from the raw log is mapped to the `principal.resource.name` field.  
`digestS3Object` | `principal.asset.asset_id` | The value of `digestS3Object` from the raw log is prepended with "S3 Object: " and mapped to the `principal.asset.asset_id` field.  
`digestSignatureAlgorithm` | `network.tls.cipher` | The value of `digestSignatureAlgorithm` from the raw log is mapped to the `network.tls.cipher` field.  
`digestStartTime` | `metadata.event_timestamp` | The value of `digestStartTime` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp` field.  
`dimensions.VolumeId` | `additional.fields` | The value of `dimensions.VolumeId` from the raw log is added as a key-value pair to the `additional.fields` with the key "VolumeId".  
`duration` | `additional.fields` | The value of `duration` from the raw log is added as a key-value pair to the `additional.fields` with the key "duration".  
`errorCode` | `security_result.rule_name` | The value of `errorCode` from the raw log is mapped to the `security_result.rule_name` field.  
`errorMessage` | `security_result.summary` | The value of `errorMessage` from the raw log is mapped to the `security_result.summary` field.  
`executionId` | `principal.process.pid` | The value of `executionId` from the raw log is mapped to the `principal.process.pid` field.  
`host` | `principal.hostname`, `principal.ip` | The value of `host` from the raw log, with hyphens replaced by dots, is parsed as an IP address and mapped to the `principal.ip` field if successful. Otherwise, it is mapped to the `principal.hostname` field.  
`http_verb` | `network.http.method` | The value of `http_verb` from the raw log is converted to uppercase and mapped to the `network.http.method` field.  
`kubernetes.container_hash` | `additional.fields` | The value of `kubernetes.container_hash` from the raw log is added as a key-value pair to the `additional.fields` with the key "container_hash".  
`kubernetes.container_image` | `additional.fields` | The value of `kubernetes.container_image` from the raw log is added as a key-value pair to the `additional.fields` with the key "container_image".  
`kubernetes.container_name` | `additional.fields` | The value of `kubernetes.container_name` from the raw log is added as a key-value pair to the `additional.fields` with the key "container_name".  
`kubernetes.docker_id` | `principal.asset_id` | The value of `kubernetes.docker_id` from the raw log is prepended with "id: " and mapped to the `principal.asset_id` field.  
`kubernetes.host` | `principal.hostname`, `principal.ip` | The value of `kubernetes.host` from the raw log, with hyphens replaced by dots, is parsed as an IP address and mapped to the `principal.ip` field if successful. Otherwise, it is mapped to the `principal.hostname` field.  
`kubernetes.namespace` | `principal.namespace` | The value of `kubernetes.namespace` from the raw log is mapped to the `principal.namespace` field.  
`kubernetes.namespace_name` | `principal.namespace` | The value of `kubernetes.namespace_name` from the raw log is mapped to the `principal.namespace` field.  
`kubernetes.pod_id` | `principal.asset.asset_id` | The value of `kubernetes.pod_id` from the raw log is prepended with "pod_id: " and mapped to the `principal.asset.asset_id` field.  
`kubernetes.pod_name` | `additional.fields` | The value of `kubernetes.pod_name` from the raw log is added as a key-value pair to the `additional.fields` with the key "pod name".  
`lambdaArn` | `principal.hostname` | The value of `lambdaArn` from the raw log is mapped to the `principal.hostname` field.  
`level` | `security_result.severity` | The value of `level` from the raw log determines the value of `security_result.severity`. If `level` is "Info", the value is "INFORMATIONAL". If `level` is "Error", the value is "ERROR". If `level` is "Warning", the value is "MEDIUM".  
`log` | `metadata.description` | The value of `log` from the raw log is mapped to the `metadata.description` field if `descr` is empty.  
`logFiles` | `about` | For each element in the `logFiles` array from the raw log, an `about` object is created with `file.full_path` set to `s3Object`, `asset.hostname` set to `s3Bucket`, and `file.sha256` set to `hashValue`.  
`log_processed.cause` | `security_result.summary` | The value of `log_processed.cause` from the raw log is mapped to the `security_result.summary` field.  
`log_processed.ids` | `intermediary.hostname` | For each element in the `log_processed.ids` array from the raw log, an `intermediary` object is created with `hostname` set to the element's value.  
`log_processed.level` | `security_result.severity` | The value of `log_processed.level` from the raw log is mapped to the `security_result.severity` field.  
`log_processed.msg` | `metadata.description` | The value of `log_processed.msg` from the raw log is mapped to the `metadata.description` field.  
`log_processed.ts` | `metadata.event_timestamp` | The value of `log_processed.ts` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp` field.  
`log_type` | `metadata.log_type` | The value of `log_type` from the raw log is mapped to the `metadata.log_type` field. This is a custom field added for context.  
`logevent.message` | `security_result.description` | The value of `logevent.message` from the raw log is mapped to the `security_result.description` field. It is also parsed using grok to extract additional fields.  
`logGroup` | `security_result.about.resource.name` | The value of `logGroup` from the raw log is mapped to the `security_result.about.resource.name` field.  
`logStream` | `security_result.about.resource.attribute.labels` | The value of `logStream` from the raw log is added as a key-value pair to the `security_result.about.resource.attribute.labels` with the key "logStream".  
`memory_used` | `additional.fields` | The value of `memory_used` from the raw log is added as a key-value pair to the `additional.fields` with the key "memory_used".  
`metric_name` | `additional.fields` | The value of `metric_name` from the raw log is added as a key-value pair to the `additional.fields` with the key "metric_name".  
`metric_stream_name` | `additional.fields` | The value of `metric_stream_name` from the raw log is added as a key-value pair to the `additional.fields` with the key "metric_stream_name".  
`namespace` | `principal.namespace` | The value of `namespace` from the raw log is mapped to the `principal.namespace` field.  
`owner` | `principal.user.userid` | The value of `owner` from the raw log is mapped to the `principal.user.userid` field.  
`parameters` | `additional.fields` | The value of `parameters` from the raw log is added as a key-value pair to the `additional.fields` with the key "Parameters".  
`Path` | `principal.process.file.full_path` | The value of `Path` from the raw log is mapped to the `principal.process.file.full_path` field.  
`pid` | `principal.process.pid` | The value of `pid` from the raw log is mapped to the `principal.process.pid` field.  
`PolicyName` | `security_result.rule_name` | The value of `PolicyName` from the raw log is mapped to the `security_result.rule_name` field.  
`prin_host` | `principal.hostname` | The value of `prin_host` from the raw log is mapped to the `principal.hostname` field.  
`principal_hostname` | `principal.hostname` | The value of `principal_hostname` from the raw log is mapped to the `principal.hostname` field.  
`process` | `principal.application` | The value of `process` from the raw log is mapped to the `principal.application` field.  
`rawData` | `additional.fields` | The value of `rawData` from the raw log is added as a key-value pair to the `additional.fields` with the key "Raw Data".  
`Recommendation` | `security_result.detection_fields` | The value of `Recommendation` from the raw log is added as a key-value pair to the `security_result.detection_fields` with the key "Recommendation".  
`referral_url` | `network.http.referral_url` | The value of `referral_url` from the raw log is mapped to the `network.http.referral_url` field.  
`region` | `principal.location.name` | The value of `region` from the raw log is mapped to the `principal.location.name` field.  
`resp_code` | `network.http.response_code` | The value of `resp_code` from the raw log is converted to an integer and mapped to the `network.http.response_code` field.  
`resource_url` | `network.http.referral_url` | The value of `resource_url` from the raw log is mapped to the `network.http.referral_url` field.  
`ResourceType` | `target.resource.resource_subtype` | The value of `ResourceType` from the raw log is mapped to the `target.resource.resource_subtype` field.  
`response_body` | `additional.fields` | The value of `response_body` from the raw log is added as a key-value pair to the `additional.fields` with the key "Response body".  
`Role` | `target.resource.product_object_id` | The value of `Role` from the raw log is mapped to the `target.resource.product_object_id` field.  
`s3_bucket_path` | `target.file.full_path` | The value of `s3_bucket_path` from the raw log is mapped to the `target.file.full_path` field.  
`sec_result.category` | `security_result.category` | The value of `sec_result.category` is derived from the parser logic. If `descr` contains "authentication is required", the value is "AUTH_VIOLATION".  
`sec_result.description` | `security_result.description` | The value of `sec_result.description` is derived from the parser logic. It is set to the value of `cloudwatchLog` if present.  
`sec_result.severity` | `security_result.severity` | The value of `sec_result.severity` is derived from the parser logic. It is set based on the value of `severity` or `level`.  
`sec_result.summary` | `security_result.summary` | The value of `sec_result.summary` is derived from the parser logic. It is set to the value of `log_processed.cause` or `errorMessage` if present.  
`security_result` | `security_result` | The `security_result` object is constructed from various fields and parser logic.  
`serverId` | `additional.fields` | The value of `serverId` from the raw log is added as a key-value pair to the `additional.fields` with the key "server_id".  
`severity` | `security_result.severity` | The value of `severity` from the raw log, converted to uppercase and normalized, is mapped to the `security_result.severity` field.  
`Source` | `principal.hostname` | The value of `Source` from the raw log is mapped to the `principal.hostname` field.  
`source` | `principal.hostname` | The value of `source` from the raw log is mapped to the `principal.hostname` field.  
`SourceIP` | `principal.ip` | The value of `SourceIP` from the raw log is mapped to the `principal.ip` field.  
`src_port` | `principal.port` | If `src_port` is "80", it is converted to an integer and mapped to the `principal.port` field, and `network.application_protocol` is set to "HTTP".  
`stream` | `additional.fields` | The value of `stream` from the raw log is added as a key-value pair to the `additional.fields` with the key "stream".  
`subscriptionFilters` | `security_result.about.resource.attribute.labels` | For each element in the `subscriptionFilters` array from the raw log, a key-value pair is added to the `security_result.about.resource.attribute.labels` with the key "subscriptionFilter" and the value from the array.  
`support_contact` | `target.resource.attribute.labels` | The value of `support_contact` from the raw log is added as a key-value pair to the `target.resource.attribute.labels` with the key "Support Contact".  
`t_ip` | `target.ip` | The value of `t_ip` from the raw log, after removing hyphens, is parsed as an IP address and mapped to the `target.ip` field if successful.  
`time` | `metadata.event_timestamp` | The value of `time` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp` field.  
`timestamp` | `metadata.event_timestamp` | The value of `timestamp` from the raw log is converted to a timestamp using various formats and mapped to the `metadata.event_timestamp` field.  
`tls` | `network.tls.version` | The value of `tls` from the raw log is mapped to the `network.tls.version` field.  
`transferDetails.serverId` | `additional.fields` | The value of `transferDetails.serverId` from the raw log is added as a key-value pair to the `additional.fields` with the key "server_id".  
`transferDetails.sessionId` | `network.session_id` | The value of `transferDetails.sessionId` from the raw log is mapped to the `network.session_id` field.  
`transferDetails.username` | `principal.user.user_display_name` | The value of `transferDetails.username` from the raw log is mapped to the `principal.user.user_display_name` field.  
`ts` | `metadata.event_timestamp` | The value of `ts` from the raw log, combined with the timezone if available, is converted to a timestamp and mapped to the `metadata.event_timestamp` field.  
`type` | `metadata.product_event_type` | The value of `type` from the raw log is mapped to the `metadata.product_event_type` field.  
`unit` | `additional.fields` | The value of `unit` from the raw log is added as a key-value pair to the `additional.fields` with the key "unit".  
`url` | `target.url` | The value of `url` from the raw log is mapped to the `target.url` field.  
`url_back_to_product` | `metadata.url_back_to_product` | The value of `url_back_to_product` from the raw log is mapped to the `metadata.url_back_to_product` field.  
`User` | `principal.user.userid` | The value of `User` from the raw log is mapped to the `principal.user.userid` field.  
`user` | `target.user.userid`, `metadata.event_type`, `extensions.auth.mechanism` | If `user` is present, `metadata.event_type` is set to "USER_LOGIN", `extensions.auth.mechanism` is set to "NETWORK", and the value of `user` is mapped to `target.user.userid`.  
`value.count` | `additional.fields` | The value of `value.count` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "count".  
`value.max` | `additional.fields` | The value of `value.max` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "max".  
`value.min` | `additional.fields` | The value of `value.min` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "min".  
`value.sum` | `additional.fields` | The value of `value.sum` from the raw log is converted to a string and added as a key-value pair to the `additional.fields` with the key "sum".  
`workflowId` | `additional.fields` | The value of `workflowId` from the raw log is added as a key-value pair to the `additional.fields` with the key "workflowId".  
`aws_account` | `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`phoneNumber_country` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`aws_log_stream` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`aws_message_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`lambda_request_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phoneNumber_countryCallingCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phoneNumber_countryCallingCodeSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`max_memory_used` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gridInquiryId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`phoneCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dateOfBirth` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gender` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`countryOfBirth` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nationality` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nationalities` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`postalCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`street` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`block` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`building` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`floor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unit` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`addressLine` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`expirationDate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`annualIncome_max` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`annualIncome_min` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`savings_max` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`savings_min` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customerAgreement` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`orderHandling` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`privacyPolicy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`riskDisclosure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`employmentStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`typeOfBusiness` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`updatedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`industryLabel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`industryCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occupationCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`occupationLabel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`primary` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`expiredAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`signedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`selectedTaxResidency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`diplomaOrHigher` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`qualifiedFinancePro` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`workedPast10Years` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`workedPast3Years` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`none` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dataConfirmed` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isDeactivated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kycStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pepCheckStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cfd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Billed_Duration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`countryCode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`additional` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timestamp_iso` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`log_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`lambda_level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`source_region` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`awsRegion` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`functionName` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`functionVersion` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`environment` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`authProvider` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`dataProvider` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`igApplicationId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`igClientId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`ibkrUserId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`sourceOfFunds` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`phoneNumber_nationalNumber` | `event.idm.read_only_udm.target.user.phone_numbers` | Mapped from changelog  
`phoneNumber_number` | `event.idm.read_only_udm.principal.user.phone_numbers` | Mapped from changelog  
`phoneNumber` | `event.idm.read_only_udm.principal.user.phone_numbers` | Mapped from changelog  
`externalUserId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`report_request_id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`memory_size` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`http_verb` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`referral_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`resp_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`userId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`source_account` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`lastName` | `event.idm.read_only_udm.principal.user.last_name` | Mapped from changelog  
`firstName` | `event.idm.read_only_udm.principal.user.first_name` | Mapped from changelog  
`city` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`nric` | `event.idm.read_only_udm.principal.user.employee_id` | Mapped from changelog  
`principalName` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`Protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`Cat` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`Hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`IP` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`LocalIp` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`Hash` | `event.idm.read_only_udm.principal.process.file.md5` | Mapped from changelog  
`Pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`LocalPort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`ValidSig` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Company` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ImageType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`MWName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`DriveType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Times` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SocketOpFlags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ALProtocolExpected` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ALProtocolDetected` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CipherType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ConnectionState` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProxyConnection` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ContentEncoding` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Broken` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ExeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Prevalence` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PrevLastDay` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.firewall_name` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`logevent.message.firewall_name` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`logevent.message.availability_zone` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`logevent.message.event.src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`logevent.message.event.src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`logevent.message.event.src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`logevent.message.event.dest_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`logevent.message.event.dest_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`logevent.message.event.dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`logevent.message.event.alert.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logevent.message.event.verdict.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logevent.message.event.alert.signature` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.icmp_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.icmp_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.app_proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.alert.signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.alert.rev` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.alert.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`logevent.message.event.flow_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`logevent.message.event.direction` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`logevent.message.event.alert.signature (key: Signature)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.icmp_type (key: Icmp_Type)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.icmp_code (key: Icmp_Code)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.app_proto (key: App_Proto)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.alert.signature_id (key: Signature_ID)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.alert.rev (key: Rev)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.pkt_src (key: Pkt_Src)` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event.timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`origin-role` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`action_detail` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`service` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`url-requested` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`active-role` | `event.idm.read_only_udm.target.user.attribute.roles` | Mapped from changelog  
`client_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`http-request-origin-ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`realmId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`realmName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`clientId` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`userId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`sessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`redirect_uri` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`ipAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ipAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`time_value_log` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`auth_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Authentication_Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Thread_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Response_Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`consent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Consent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`code_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Code_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Response_Mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authSessionParentId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Auth_Session_Parent_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`authSessionTabId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Auth_Session_Tab_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_p` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`raw_p_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`key_event` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Key_Event` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`auth_method` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Auth_Method` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`finding.AwsAccountId` | `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`finding.UpdatedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.Title` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.FirstObservedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Remediation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Release` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.PackageManager` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.FixedInVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Epoch` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerabilityvalue.Architecture` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.SchemaVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerability.RelatedVulnerabilities` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerability.ReferenceUrls` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vulnerability.EpssScore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.AwsAccountName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.CompanyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.GeneratorId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.ProductName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.RecordState` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Details.AwsEc2Instance.ImageId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Details.AwsEc2Instance.SubnetId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Details.AwsEc2Instance.Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.ProductFields.aws/inspector/FindingStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.ProductFields.aws/inspector/inspectorScore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.ProductFields.aws/inspector/instanceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.ProductFields.aws/inspector/resources/1/resourceDetails/awsEc2InstanceDetails/platform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.Application` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.BuildBy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.Environment` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.FacultyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.Lifecycle` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.Support` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.Tags.ams:rt:ams-managed` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`finding.CreatedAt` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`finding.Description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`finding.FindingProviderFields.Severity.Label` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`finding.FindingProviderFields.Severity.Normalized` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`finding.FindingProviderFields.Types` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`vulnerability.LastKnownExploitAt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability.ExploitAvailable` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability.FixAvailable` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`finding.LastObservedAt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`finding.ProcessedAt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`finding.ProductArn` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`finding.Region` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`finding.Remediation.Recommendation.Text` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`resource.Details.AwsEc2Instance.IpV4Addresses` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`resource.Details.AwsEc2Instance.LaunchedAt` | `event.idm.read_only_udm.target.asset.attribute.creation_time` | Mapped from changelog  
`resource.Details.AwsEc2Instance.VpcId` | `event.idm.read_only_udm.target.asset.attribute.cloud.vpc.id` | Mapped from changelog  
`finding.ProductFields.aws/inspector/ProductVersion` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`vulnerability.Cvss` | `event.idm.read_only_udm.security_result.about.asset.vulnerabilities` | Mapped from changelog  
`logevent.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`logevent.timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`record.owner` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`msgs.availability_zone` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`logevent.message.event_data.dest_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`msgs.event.dest_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`logevent.message.event_data.dest_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`logevent.message.event_data.dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`msgs.event.dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`logevent.message.event_data.src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`logevent.message.event_data.src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`msgs.firewall_name` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`logevent.message.event_data.alert.rev` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event_data.alert.signature` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event_data.alert.signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logevent.message.event_data.pkt_src` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msgs.event.alert.rev` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msgs.event.alert.signature` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msgs.event.alert.signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msgs.event.pkt_src` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.messageType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`record.logGroup` | `event.idm.read_only_udm.security_result.about.resource.name` | Mapped from changelog  
`record.logStream` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`record.subscriptionFilters` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`logevent.message.event_data.alert.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logevent.message.event_data.verdict.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`msgs.event.alert.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`msgs.event.verdict.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`logevent.message.event_data.alert.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`msgs.event.alert.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`logevent.message.event_data.direction` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`msgs.event.direction` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`logevent.message.event_data.proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`msgs.event.proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`accountID` | `event.idm.read_only_udm.target.user.product_object_id` | Mapped from changelog  
`file` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`func` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pointsToLaunchpadArn` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`result` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.Arn` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.DataProtectionStatus` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.InheritedProperties` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.KmsKeyId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.LogGroupClass` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.MetricFilterCount` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.RetentionInDays` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`logGroup.StoredBytes` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`logGroupArn` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`logGroupName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`requestID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`owner` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`logGroup` | `event.idm.read_only_udm.security_result.about.resource.name` | Mapped from changelog  
`logStream` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`logevent.message` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`act_det` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`tar_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`tar_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`tar_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`rec_bytes` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`meth` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`subscriptionFilter` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`log_processed_control_data_sampling_interval", "log_processed_cpus_per_sock_avg", "log_processed_cpus_per_sock_max", "log_processed_cpus_per_sock_min", "flow_aggregation_result" fields, "flows_after", "flows_before", "level", "message", "sock_add_result" fields, "sock_cache_len", "sock_delta_result" fields, "sock_eviction_result" fields, "sock_nat_result" fields, "container_hash", "container_image` | `additional.fields` | Mapped from changelog  
`kubernetes_host_details` | `principal.hostname` | Mapped from changelog  
`prin_ip` | `principal.ip` | Mapped from changelog  
`kubernetes_pod_id` | `principal.product_object_id` | Mapped from changelog  
`kubernetes_pod_name` | `principal.namespace` | Mapped from changelog  
`log_processed_level` | `sec_result.severity` | Mapped from changelog  
`connectionTesterClassName` | `principal.hostname` | Mapped from changelog  
`identityToken` | `principal.user.userid` | Mapped from changelog  
`jdbcUrl` | `target.url` | Mapped from changelog  
`driverClass` | `target.application` | Mapped from changelog  
`uid` | `metadata.product_log_id` | Mapped from changelog  
`ResourceRegion` | `target.location.country_or_region` | Mapped from changelog  
`PolicyName","detail.additionalEventData.configRuleName` | `security_result.rule_name` | Mapped from changelog  
`region","detail.awsRegion` | `principal.location.name` | Mapped from changelog  
`detail.user.arn` | `target.user.userid` | Mapped from changelog  
`detail.user.sessionContext.sessionIssuer.userName` | `target.user.user_display_name` | Mapped from changelog  
`detail.user.mfaAuthenticated` | `principal.user.attribute.labels` | Mapped from changelog  
`detail.managementEvent", "detail.eventType", "detail.readOnly", "detail.eventName", "detail.additionalEventData.notificationJobType", "detail.additionalEventData.managedRuleIdentifier", "duration", "billed_duration", "memory_used` | `additional.fields` | Mapped from changelog  
`request_id` | `target.resource.attribute.labels` | Mapped from changelog  
`package` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`network_dir` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`digestPublicKeyFingerprint" from "additional.fields` | `event.idm.read_only_udm.target.file.sha1` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudwatch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
