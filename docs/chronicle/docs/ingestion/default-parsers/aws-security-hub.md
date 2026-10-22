---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-security-hub/
title: Collect AWS Security Hub logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:15.514748+00:00
---

# Collect AWS Security Hub logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-security-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Security Hub logs

**Parser Version:** 8.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Security Hub logs to Google Security Operations. AWS Security Hub provides a comprehensive view of security alerts and findings across AWS accounts. By sending these findings to Google SecOps, you can use Google SecOps capabilities to enhance monitoring and threat detection.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## Configure AWS IAM and S3

  1. Create an **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
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
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Create a Lambda function

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. Go to **Lambda**.
  3. Click **Create Function** and select **Author from Scratch**.
  4. Provide a name for your function; for example, `SecurityHubToS3`.
  5. Choose **Python 3.x** for the runtime.
  6. Enter the Lambda code that takes the findings from EventBridge and writes them to your S3 bucket:
         
         import json
         import boto3
         from datetime import datetime
         
         # Initialize the S3 client
         s3_client = boto3.client('s3')
         
         # S3 bucket where findings will be stored
         bucket_name = 'aws-security-hub-findings-stream'
         
         def lambda_handler(event, context):
            # Extract Security Hub findings from the event
            findings = event['detail']['findings']
         
            # Generate a timestamp for the file name to avoid overwriting
            timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
         
            # Generate the S3 object key (file name) based on the timestamp
            object_key = f"security_hub_findings_{timestamp}.json"
         
            # Convert findings to JSON format
            findings_json = json.dumps(findings)
         
            # Upload the findings to S3
            try:
               response = s3_client.put_object(
                     Bucket=bucket_name,
                     Key=object_key,
                     Body=findings_json,
                     ContentType='application/json'
               )
               print(f"Successfully uploaded findings to S3: {response}")
            except Exception as e:
               print(f"Error uploading findings to S3: {e}")
               raise e
         
            return {
               'statusCode': 200,
               'body': json.dumps('Successfully processed findings')
            }
         

**Note:** This code will store the findings as JSON files in your S3 bucket with timestamps.
  7. Set permissions for Lambda by adding an IAM role to the Lambda function with the following policy:
         
         {
            "Version": "2012-10-17",
            "Statement": [
               {
                     "Effect": "Allow",
                     "Action": [
                        "s3:PutObject"
                     ],
                     "Resource": "arn:aws:s3:::aws-security-hub-findings-stream/*"
               }
            ]
         }
         




## How to configure AWS Security Hub to forward findings with EventBridge

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type and select **Security Hub** from the services list.
  3. Click **Settings**.
  4. Under the **Integrations** section, find **EventBridge** and click **Enable**.
  5. In the search bar, type and select **EventBridge** from the services list.
  6. In the EventBridge console, click **Rules > Create rule**.
  7. Provide the following Rule configuration: 
     1. **Rule Name** : Provide a descriptive name for the rule; for example, **SendSecurityHubFindingsToS3**.
     2. **Event Source** : Select **AWS services**.
     3. **Service Name** : Choose **Security Hub**.
     4. **Event Type** : Select **Security Hub Findings**.
     5. **Set the Target** : Choose **Lambda function**.
     6. Select the Lambda function you just created (`SecurityHubToS3`).
  8. Click **Create**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Security Hub feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Security Hub** log type.
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
`account` | `principal.group.product_object_id` | The AWS account ID associated with the finding.  
`configurationItem.ARN` | `target.resource.id` | The Amazon Resource Name (ARN) of the configuration item.  
`configurationItem.awsAccountId` | `principal.user.userid` | The AWS account ID of the configuration item.  
`configurationItem.awsRegion` | `target.asset.location.country_or_region` | The AWS region of the configuration item.  
`configurationItem.configuration.complianceType` | `security_result.summary` | The compliance type of the configuration item.  
`configurationItem.configuration.configRuleList[].complianceType` | `security_result.summary` | Compliance status for each config rule.  
`configurationItem.configuration.configRuleList[].configRuleArn` | `security_result.rule_id` | The ARN of the AWS Config rule.  
`configurationItem.configuration.configRuleList[].configRuleId` | `security_result.about.labels.configRuleId` | The ID of the AWS Config rule.  
`configurationItem.configuration.configRuleList[].configRuleName` | `security_result.rule_name` | The name of the AWS Config rule.  
`configurationItem.configuration.privateIpAddress` | `target.ip` | The private IP address of the configuration item.  
`configurationItem.configuration.publicIpAddress` | `target.ip` | The public IP address of the configuration item.  
`configurationItem.configurationItemCaptureTime` | `target.asset.attribute.creation_time` | The capture time of the configuration item, converted to a timestamp.  
`configurationItem.configurationItemStatus` | `target.asset.attribute.labels.Configuration Item Status` | The status of the configuration item.  
`configurationItem.relationships[].resourceId` | `target.asset.attribute.cloud.vpc.id` | The resource ID of the related resource, used for VPC ID if it matches `vpc`.  
`configurationItem.resourceId` | `target.resource.id` | The resource ID of the configuration item.  
`configurationItem.resourceName` | `target.resource.name` | The name of the resource.  
`configurationItem.resourceType` | `target.resource.resource_subtype` | The resource type of the configuration item.  
`configurationItem.tags.Contact` | `principal.user.user_display_name` OR `principal.user.email_addresses` | Contact details extracted from tags, parsed for email and username.  
`configurationItem.tags.OS` / `configurationItem.tags.Os` | `target.asset.platform_software.platform` | The operating system from tags, mapped to platform if it's `Windows` or `Linux`.  
`configurationItemDiff.changeType` | `metadata.event_type` | The type of change, mapped to RESOURCE_WRITTEN or RESOURCE_CREATION.  
`detail.accountId` | `principal.group.product_object_id` | The AWS account ID associated with the finding.  
`detail.actionDescription` `detail.actionName` `detail.description` | `sec_result.description` | The description of the finding.  
`detail.findings[].AwsAccountId` | `principal.group.product_object_id` | The AWS account ID associated with the finding.  
`detail.findings[].CompanyName` `detail.findings[].CreatedAt` `detail.findings[].Description` | `sec_result.description` | The description of the finding.  
`detail.findings[].FindingProviderFields.Severity.Label` | `sec_result.severity` | The severity label of the finding, converted to uppercase.  
`detail.findings[].FindingProviderFields.Types[]` `detail.findings[].FirstObservedAt` `detail.findings[].GeneratorId` `detail.findings[].Id` `detail.findings[].LastObservedAt` `detail.findings[].ProductArn` `detail.findings[].ProductFields.` | See below | Various fields used for additional fields, principal, and target information.  
`detail.findings[].ProductName` `detail.findings[].RecordState` `detail.findings[].Region` | `target.location.name` | The AWS region of the finding.  
`detail.findings[].Resources[].Details.` | See below | Details about the resources involved in the finding.  
`detail.findings[].Resources[].Id` | `target.resource.product_object_id` | The ID of the resource.  
`detail.findings[].Resources[].Partition` `detail.findings[].Resources[].Region` | `target.location.name` | The AWS region of the resource.  
`detail.findings[].Resources[].Tags` `detail.findings[].Resources[].Type` | `target.resource.resource_type`, `target.resource.resource_subtype`, `metadata.event_type` | The type of resource, used for resource type, subtype, and event type mapping.  
`detail.findings[].Sample` `detail.findings[].SchemaVersion` `detail.findings[].Severity.Label` `detail.findings[].SourceUrl` `detail.findings[].Title` | `sec_result.summary` | The title of the finding.  
`detail.findings[].Types[]` `detail.findings[].UpdatedAt` `detail.findings[].Workflow.Status` `detail.findings[].WorkflowState` `detail-type` | `metadata.product_event_type` | The detail type of the event.  
`id` | `metadata.product_log_id` | The ID of the event.  
`region` | `target.location.name` | The AWS region of the event.  
`resources[]` `source` `time` `version` (Parser Logic) | `metadata.event_timestamp` | The create time from the original log entry, used as event timestamp.  
(Parser Logic) | `metadata.log_type` | Set to `AWS_SECURITY_HUB`.  
(Parser Logic) | `metadata.product_name` | Set to `AWS Security Hub`.  
(Parser Logic) | `metadata.vendor_name` | Set to `AMAZON`.  
(Parser Logic) | `target.asset.attribute.cloud.environment` | Set to `AMAZON_WEB_SERVICES`.  
(Parser Logic) | `metadata.event_type` | Set to `USER_RESOURCE_ACCESS` as a default if not mapped from `Resources[].Type` or `configurationItemDiff.changeType`. Set to `STATUS_UPDATE` if `configurationItems` is present and no other event type is set. Set to `RESOURCE_READ` if `configurationItem` or `configurationItems` is present and the status is `OK` or `ResourceDiscovered`. Set to `RESOURCE_DELETION` if `configurationItem` or `configurationItems` is present and the status is `ResourceDeleted`.  
(Parser Logic) | `metadata.description` | Set to `guardduty` if `detail.findings[].ProductFields.aws/guardduty/service/serviceName` is present.  
(Parser Logic) | `target.asset.attribute.cloud.vpc.resource_type` | Set to `VPC_NETWORK` if `configurationItems.relationships[].resourceId` matches `vpc`.  
(Parser Logic) | `target.resource.resource_type` | Set to `VIRTUAL_MACHINE` if `configurationItem` or `configurationItems` is present. Set to `UNSPECIFIED` if no other resource type is set.  
(Parser Logic) | `target.asset.platform_software.platform` | Set to `WINDOWS` or `LINUX` based on the presence of `Windows` or `(Linux|LINUX)` in the message for `configurationItem`. For `configurationItems`, it's set based on `configItem.tags.OS` or `configItem.tags.Os`.  
(Parser Logic) | `disambiguation_key` | Added when multiple events are generated from a single log entry.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-security-hub-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
