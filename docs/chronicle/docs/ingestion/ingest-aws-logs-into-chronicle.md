---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle/
title: Collect AWS CloudTrail logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:50:30.986242+00:00
---

# Collect AWS CloudTrail logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS CloudTrail logs

**Parser Version:** 30.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to collect AWS CloudTrail logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of AWS CloudTrail and the Google SecOps feed configured to send logs to Google SecOps. Your deployment might be different from the typical deployment described in this document. The deployment contains the following components:

  * **AWS CloudTrail** : The platform that collects logs.

  * **AWS S3** : The platform that stores logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from AWS S3 and writes logs to Google SecOps.

  * **Google SecOps** : The platform that retains and analyzes the logs from AWS CloudTrail.




An ingestion label identifies the parser that normalizes raw log data to structured UDM format. The information into this document applies to the parser with the `AWS_CLOUDTRAIL` ingestion label.

## Before you begin

Make sure you have the following prerequisites:

  * [AWS Account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
  * prerequisites for using AWS CloudTrail are met. For more information, see [AWS CloudTrail setup](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html).
  * All systems in the deployment architecture use the UTC time zone



## Basic steps to ingest logs from S3 with SQS

This section describes the basic steps for ingesting AWS CloudTrail logs into your Google SecOps instance. The steps describe how to do this using Amazon S3 with Amazon SQS as the feed source type.

### Configure AWS CloudTrail and S3

In this procedure, you configure AWS CloudTrail logs to be written to an S3 bucket.

  1. In the AWS console, search for **CloudTrail**.
  2. Click **Create trail**.
  3. Provide a **Trail name**.
  4. Select **Create new S3 bucket**. You may also choose to use an existing S3 bucket.
  5. Provide a name for **AWS KMS alias** , or choose an existing **AWS KMS Key**.
  6. You can leave the other settings as default, and click **Next**.
  7. Choose **Event type** , add **Data events** as required, and click **Next**.
  8. Review the settings in **Review and create** , and click **Create trail**.
  9. In the AWS console, search for **Amazon S3 Buckets**.
  10. Click the newly created log bucket, and select the folder **AWSLogs**. Then click **Copy S3 URI** and save it for use in the following steps.



### Set up a Standard SQS Queue and SNS

If you use an SQS queue, it must be a _Standard_ queue, not a FIFO queue.

  1. Enable AWS CloudTrail and configure it to deliver logs to an S3 bucket using a new or existing trail.
  2. Open the AWS SNS console and create a new Standard topic. Name it, e.g., CloudTrail-Notification-Topic.
  3. Create a SQS queue using the AWS SQS console, e.g., CloudTrail-Notification-Queue, and update its access policy to allow the SNS topic ARN to send messages. For details about creating SQS queues, see [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

Example SQS policy snippet:
         
         {
            "Version": "2012-10-17",
            "Id": `PolicyForSNS`,
            "Statement": [
               {
                  "Sid": "AllowSNS",
                  "Effect": "Allow",
                  "Principal": { "Service": "sns.amazonaws.com" },
                  "Action": "SQS:SendMessage",
                  "Resource": "arn:aws:sqs:REGION:ACCOUNT_ID:CloudTrail-Notification-Queue",
                  "Condition": {
                  "ArnEquals": { "aws:SourceArn": "arn:aws:sns:REGION:ACCOUNT_ID:CloudTrail-Notification-Topic"}
                  }
               }
            ]
         }
         

  4. Go to the **SNS topic** → **Subscriptions** → **Create subscription** , set Protocol to SQS, and Endpoint to the ARN of the SQS queue.

**Important:** When creating the SNS subscription for the SQS queue, you must enable the **Raw message delivery** option. This setting is required for Google SecOps to receive the raw CloudTrail log payload, allowing the parser to correctly ingest the logs.
  5. CloudTrail doesn't natively push new logs to SNS. To enable notifications, you can use a **CloudTrail Event Selector for Management Events** , or use **CloudTrail integration with CloudWatch Logs** and then create a CloudWatch Event Rule that triggers notifications by setting an SNS topic as the target. For more details, see [set up notifications on your S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html).

Example event pattern:
         
         {
            "source": ["aws.s3"],
            "detail-type": ["AWS API Call via CloudTrail"],
            "detail": {
               "eventName": ["PutObject"],
               "requestParameters": {
                  "bucketName": [`CloudTrail-Notification-Topic`]
               }
            }
         }
         

  6. Make sure IAM roles or policies allow CloudWatch Events to publish to SNS, and make sure SNS is allowed to send messages to SQS.




### Configure AWS IAM user

Configure an AWS IAM user which Google SecOps will be used to access both the SQS queue (if used) and the S3 bucket.

  1. In the AWS console, search for **IAM**.
  2. Click **Users** , and then in the following screen, click **Create Users**.
  3. Provide a name for the user, for example, _chronicle-feed-user_ , and select **Provide user access to the AWS Management Console**.
  4. Select **Attach existing policies directly** and select **AmazonS3ReadOnlyAccess** or **AmazonS3FullAccess** , as required. **AmazonS3FullAccess** would be used if Google SecOps should clear the S3 buckets after reading logs, to optimize AWS S3 storage costs.
  5. As a recommended alternative to the previous step, you can further restrict access to only the specified S3 bucket by creating a custom policy. Click **Create policy** and follow the [AWS documentation](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html) to create a custom policy.
  6. When you apply a policy, make sure that you have included `sqs:DeleteMessage`. Google SecOps isn't able to delete messages if the `sqs:DeleteMessage` permission isn't attached to the SQS queue. All the messages are accumulated on the AWS side, which causes a delay as Google SecOps repeatedly attempts to transfer the same files.
  7. Click **Next:Tags**.
  8. Add any tags if required, and click **Next:Review**.
  9. Review the configuration and click **Create user**.
  10. Once the user is created, go to the **Security Credentials** tab, and click **Create Access Key**.
  11. Choose **CLI** and click **Next:Tags**.
  12. Add any tags if required, then click **Create Access Key: Review**.
  13. Copy the **Access Key ID** and **Secret Access Key** of the created user, for use in the next step.

**Note:** To configure the AWS IAM role trust policy for Google SecOps, you need the unique `SubjectID` of the Google-managed service account. This ID cannot be obtained using the `googleServiceAccounts.get` API.

To find the `SubjectID`, follow these steps:

     1. Begin the AWS CloudTrail feed configuration process within Google SecOps.
     2. Navigate to your designated Amazon S3 bucket and review your AWS CloudTrail logs for entries related to the feed setup attempt.
     3. Open the relevant log entry and look for the `userIdentity` section within the raw JSON data.
     4. Inside that section, locate the `principalId` or `userName` field. The numeric value listed here is your unique **SubjectID**.
     5. Copy this **SubjectID** and add it to your AWS IAM role's trust policy to grant the necessary access permissions.



## Configuring KMS key permissions

A KMS key is required to decrypt CloudTrail logs, which are encrypted server-side. AWS KMS provides enhanced encryption and security for sensitive data stored in Amazon S3.

  1. In the AWS console, search for **Key Management Service (KMS)**.
  2. Click **Create Key:Next**.
  3. Add an **Alias** for the key. Optionally, add a **Description** and **Tags** if required. Click **Next: Review**.
  4. After reviewing the configuration, click **Next**.
  5. Select the **Key Users** who should have access to this key, then click **Finish**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS CloudTrail feed

  1. Click the **Amazon Cloud Platform** pack.
  2. In the **AWS CloudTrail** log type, specify the following values:
  3. Specify values for the following fields:

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

## Supported AWS CloudTrail log types

The AWS CloudTrail parser supports the following services: 

  * apigateway.amazonaws.com
  * appconfig.amazonaws.com
  * autoscaling.amazonaws.com
  * cloud9.amazonaws.com
  * cloudsearch.amazonaws.com
  * cloudshell.amazonaws.com
  * cloudtrail.amazonaws.com
  * config.amazonaws.com
  * devicefarm.amazonaws.com
  * ds.amazonaws.com
  * dynamodb.amazonaws.com
  * ec2-instance-connect.amazonaws.com
  * ec2.amazonaws.com
  * ecr-public.amazonaws.com
  * ecr.amazonaws.com
  * ecs.amazonaws.com
  * eks.amazonaws.com
  * elasticache.amazonaws.com
  * elasticloadbalancing.amazonaws.com
  * firehose.amazonaws.com
  * guardduty.amazonaws.com
  * health.amazonaws.com
  * iam.amazonaws.com
  * imagebuilder.amazonaws.com
  * kinesis.amazonaws.com
  * kinesisanalytics.amazonaws.com
  * kinesisvideo.amazonaws.com
  * kms.amazonaws.com
  * lambda.amazonaws.com
  * logs.amazonaws.com
  * macie2.amazonaws.com
  * monitoring.amazonaws.com
  * network-firewall.amazonaws.com
  * organizations.amazonaws.com
  * quicksight.amazonaws.com
  * ram.amazonaws.com
  * rds.amazonaws.com
  * resource-explorer-2.amazonaws.com
  * resource-groups.amazonaws.com
  * route53-recovery-readiness.amazonaws.com
  * route53.amazonaws.com
  * route53domains.amazonaws.com
  * route53resolver.amazonaws.com
  * s3-outposts.amazonaws.com
  * s3.amazonaws.com
  * s3express.amazonaws.com
  * secretsmanager.amazonaws.com
  * securityhub.amazonaws.com
  * ses.amazonaws.com
  * signin.amazonaws.com
  * ssm.amazonaws.com
  * sts.amazonaws.com
  * waf-regional.amazonaws.com
  * waf.amazonaws.com
  * wafv2.amazonaws.com



## Supported AWS CloudTrail log formats

The AWS CloudTrail parser supports logs in JSON format.

## Supported AWS CloudTrail sample logs

  * JSON:
        
        {
          "Records": [{
              "eventVersion": "1.08",
              "userIdentity": {
                  "type": "AssumedRole",
                  "principalId": "AROAXELJRGZMPHEYTK4Q4:redlock",
                  "arn": "arn:aws:sts::111111111111:assumed-role/PrismaCloudReadOnlyRole/redlock",
                  "accountId": "111111111111",
                  "accessKeyId": "ASIAXELJRGZMNUCV3DC4",
                  "sessionContext": {
                      "sessionIssuer": {
                          "type": "Role",
                          "principalId": "AROAXELJRGZMPHEYTK4Q4",
                          "arn": "arn:aws:iam::111111111111:role/PrismaCloudReadOnlyRole",
                          "accountId": "111111111111",
                          "userName": "PrismaCloudReadOnlyRole"
                      },
                      "webIdFederationData": {},
                      "attributes": {
                          "creationDate": "2021-07-01T03:20:01Z",
                          "mfaAuthenticated": "false"
                      }
                  }
              },
              "eventTime": "2021-07-01T03:35:42Z",
              "eventSource": "kms.amazonaws.com",
              "eventName": "DescribeKey",
              "awsRegion": "eu-west-1",
              "sourceIPAddress": "198.51.100.0",
              "userAgent": "aws-sdk-java/1.11.1025Linux/4.14.232-176.381.amzn2.x86_64OpenJDK_64-Bit_Server_VM/11.0.10+9java/11.0.10groovy/2.5.12vendor/AdoptOpenJDKcfg/retry-mode/legacy",
              "requestParameters": {
                  "keyId": "11a011a1-1010-11a1-a0aa-c4e1a9367642"
              },
              "responseElements": null,
              "requestID": "11a011a1-1010-11a1-a0aa-604ac86fc50e",
              "eventID": "11a011a1-1010-11a1-a0aa-17ef2bdeb889",
              "readOnly": true,
              "resources": [{
                  "accountId": "111111111111",
                  "type": "AWS::KMS::Key",
                  "ARN": "arn:aws:kms:eu-west-1:111111111111:key/11a011a1-1010-11a1-a0aa-c4e1a9367642"
              }],
              "eventType": "AwsApiCall",
              "managementEvent": true,
              "recipientAccountId": "111111111111",
              "eventCategory": "Management"
          }]
        }
        




For more information on Field mapping and UDM mapping, refer to [AWS Cloudtrail field mapping](https://docs.cloud.google.com/chronicle/docs/reference/aws-cloudtrail-field-map)

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudtrail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
