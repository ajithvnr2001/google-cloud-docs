---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-macie/
title: Collect AWS Macie logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:16.616090+00:00
---

# Collect AWS Macie logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-macie/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Macie logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Macie logs to Google Security Operations. AWS Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data. This integration will allow you to send Macie logs to Google SecOps for enhanced analysis and monitoring.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## Configure Amazon S3 and IAM

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
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Optional: Configuring AWS Macie

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type and select **Macie** from the services list.
  3. Click **Create job**.
  4. Create a new bucket or proceed with the existing one.
  5. Add **Schedule job**.
  6. Select all Managed Data Identifiers.
  7. Skip **Select Custom Data Identifiers** and click **Next**.
  8. Skip **Select Allow list** and click **Next**.
  9. Provide a meaningful name and description.
  10. Click **Next**.
  11. Review and click **Submit**.



## How to configure CloudTrail for AWS Macie

  1. Sign in to the **AWS Management Console**.
  2. In the search bar, type and select **CloudTrail** from the services list.

**Note:** If you already have a trail, you can modify and use it.
  3. If you want to proceed with a new trail, click **Create trail**.

  4. Provide a **Trail name** (for example, **Macie-Activity-Trail**).

  5. Select the **Enable for all accounts in my organization** checkbox.

  6. Type the S3 bucket URI created earlier (the format should be: `s3://your-log-bucket-name/`), or create a new S3 bucket.

  7. If SSE-KMS is enabled, provide a name for **AWS KMS alias** , or choose an **existing AWS KMS Key**.

  8. You can leave the other settings as default.

  9. Click **Next**.

  10. Select **Management events** and **Data events** under **Event Types**.

  11. Click **Next**.

  12. Review the settings in **Review and create**. 

  13. Click **Create trail**.

  14. Optional: if you created a new bucket, continue with the following process:

     1. Go to **S3**.
     2. Identify and select the newly created log bucket. 
     3. Select the folder **AWSLogs**.
     4. Click **Copy S3 URI** and save it.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Macie feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Macie** log type.
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
`accountId` | `principal.group.product_object_id` | Directly mapped from the `accountId` field.  
`category` | `security_result.category_details` | Directly mapped from the `category` field.  
`classificationDetails.jobArn` | `security_result.rule_name` | Directly mapped from the `classificationDetails.jobArn` field.  
`classificationDetails.jobId` | `security_result.rule_id` | Directly mapped from the `classificationDetails.jobId` field.  
`classificationDetails.originType` | `security_result.rule_type` | Directly mapped from the `classificationDetails.originType` field.  
`classificationDetails.result.mimeType` | `target.file.mime_type` | Directly mapped from the `classificationDetails.result.mimeType` field.  
`classificationDetails.result.sensitiveData.category` | `security_result.detection_fields.value` | Directly mapped from the `classificationDetails.result.sensitiveData.category` field. The parser iterates through the `sensitiveData` array and creates multiple `detection_fields` objects.  
`classificationDetails.result.sensitiveData.totalCount` | `security_result.detection_fields.value` | Directly mapped from the `classificationDetails.result.sensitiveData.totalCount` field. The parser iterates through the `sensitiveData` array and creates multiple `detection_fields` objects.  
`createdAt` | `metadata.event_timestamp` | Parsed and converted to UDM timestamp format from the `createdAt` field.  
`description` | `security_result.description` | Directly mapped from the `description` field.  
`id` | `metadata.product_log_id` | Directly mapped from the `id` field. Hardcoded to `SCAN_FILE` in the parser. Taken from the top-level `log_type` field in the raw log. Hardcoded to `AWS Macie` in the parser. Directly mapped from the `schemaVersion` field. Hardcoded to `AMAZON` in the parser. Concatenated from `resourcesAffected.s3Bucket.name`, `region`, and the string ".s3.amazonaws.com".  
`region` | `target.location.name` | Directly mapped from the `region` field.  
`resourcesAffected.s3Bucket.arn` | `target.resource_ancestors.product_object_id` | Directly mapped from the `resourcesAffected.s3Bucket.arn` field.  
`resourcesAffected.s3Bucket.createdAt` | `target.resource_ancestors.attribute.creation_time` | Parsed and converted to UDM timestamp format from the `resourcesAffected.s3Bucket.createdAt` field.  
`resourcesAffected.s3Bucket.name` | `target.resource_ancestors.name` | Directly mapped from the `resourcesAffected.s3Bucket.name` field.  
`resourcesAffected.s3Bucket.owner.displayName` | `target.user.user_display_name` | Directly mapped from the `resourcesAffected.s3Bucket.owner.displayName` field.  
`resourcesAffected.s3Bucket.owner.id` | `target.user.userid` | Directly mapped from the `resourcesAffected.s3Bucket.owner.id` field.  
`resourcesAffected.s3Object.eTag` | `target.file.md5` | Directly mapped from the `resourcesAffected.s3Object.eTag` field.  
`resourcesAffected.s3Object.key` | `target.file.names` | Directly mapped from the `resourcesAffected.s3Object.key` field.  
`resourcesAffected.s3Object.key` | `target.resource.name` | Directly mapped from the `resourcesAffected.s3Object.key` field.  
`resourcesAffected.s3Object.lastModified` | `target.resource.attribute.last_update_time` | Parsed and converted to UDM timestamp format from the `resourcesAffected.s3Object.lastModified` field.  
`resourcesAffected.s3Object.path` | `target.file.full_path` | Prefixed with "s3://" and mapped from the `resourcesAffected.s3Object.path` field.  
`resourcesAffected.s3Object.path` | `target.resource.product_object_id` | Directly mapped from the `resourcesAffected.s3Object.path` field.  
`resourcesAffected.s3Object.size` | `target.file.size` | Directly mapped from the `resourcesAffected.s3Object.size` field after converting to unsigned integer.  
`resourcesAffected.s3Object.storageClass` | `target.resource.attribute.labels.value` | Directly mapped from the `resourcesAffected.s3Object.storageClass` field. The key is hardcoded to "storageClass". Hardcoded to `DATA_AT_REST` in the parser.  
`security_result.detection_fields.key` | `category`, `totalCount` | Hardcoded keys for the detection fields.  
`severity.description` | `security_result.severity` | Mapped from the `severity.description` field. "Low" is mapped to `LOW`, "Medium" to `MEDIUM`, and "High" to `HIGH`. Hardcoded to `AMAZON_WEB_SERVICES` in the parser. Hardcoded to `STORAGE_OBJECT` in the parser. Hardcoded to `STORAGE_BUCKET` in the parser.  
`title` | `security_result.summary` | Directly mapped from the `title` field.  
`type` | `metadata.product_event_type` | Directly mapped from the `type` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-macie-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
