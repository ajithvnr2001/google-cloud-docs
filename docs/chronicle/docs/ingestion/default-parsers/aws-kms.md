---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-kms/
title: Collect AWS Key Management Service logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:25.443127+00:00
---

# Collect AWS Key Management Service logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Key Management Service logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Key Management Service (KMS) logs to Google Security Operations. AWS KMS is a fully managed service that lets you to create and control encryption keys used to encrypt your data. This integration helps in monitoring and auditing the usage of encryption keys.

## Before you begin

Ensure you have the following prerequisites:

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



## How to configure CloudTrail for AWS KMS

  1. Sign in to the [AWS Management Console](https://aws.amazon.com/console/).
  2. In the search bar, type and select **CloudTrail** from the services list.
  3. Click **Create trail**.
  4. Provide a **Trail name** (for example, **KMS-Activity-Trail**).
  5. Select the **Enable for all accounts in my organization** checkbox.
  6. Type the S3 bucket URI created earlier (the format should be: `s3://your-log-bucket-name/`), or create a new S3 bucket.
  7. If SSE-KMS enabled, provide a name for **AWS KMS alias** , or choose an **existing AWS KMS Key**.
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



## How to set up the AWS Key Management Service feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Key Management Service** log type.
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
data.detail.awsRegion | principal.location.country_or_region | Directly mapped from the `data.detail.awsRegion` field in the raw log.  
data.detail.eventCategory | security_result.category_details | Directly mapped from the `data.detail.eventCategory` field in the raw log.  
data.detail.eventName | metadata.product_event_type | Directly mapped from the `data.detail.eventName` field in the raw log. This field determines the `metadata.event_type` value based on the logic: if eventName is "Decrypt" or "Encrypt", then event_type is "USER_RESOURCE_ACCESS", if eventName is "GenerateDataKey" then event_type is "USER_RESOURCE_CREATION", otherwise event_type is "GENERIC_EVENT".  
data.detail.requestID | additional.fields.key | Value is hardcoded to "requestID" in the parser code.  
data.detail.requestID | additional.fields.value.string_value | Directly mapped from the `data.detail.requestID` field in the raw log.  
data.detail.requestParameters.encryptionAlgorithm | security_result.detection_fields.key | Value is hardcoded to "encryptionAlgorithm" in the parser code.  
data.detail.requestParameters.encryptionAlgorithm | security_result.detection_fields.value | Directly mapped from the `data.detail.requestParameters.encryptionAlgorithm` field in the raw log.  
data.detail.resources.ARN | target.resource.id | Directly mapped from the `data.detail.resources.ARN` field in the raw log.  
data.detail.resources.type | target.resource.resource_subtype | Directly mapped from the `data.detail.resources.type` field in the raw log.  
data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated | principal.user.attribute.labels.key | Value is hardcoded to "mfaAuthenticated" in the parser code.  
data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated | principal.user.attribute.labels.value | Directly mapped from the `data.detail.userIdentity.sessionContext.attributes.mfaAuthenticated` field in the raw log.  
data.detail.userIdentity.sessionContext.sessionIssuer.principalId | principal.user.userid | Directly mapped from the `data.detail.userIdentity.sessionContext.sessionIssuer.principalId` field in the raw log.  
data.detail.userIdentity.sessionContext.sessionIssuer.userName | principal.user.user_display_name | Directly mapped from the `data.detail.userIdentity.sessionContext.sessionIssuer.userName` field in the raw log.  
data.detail.userIdentity.type | principal.user.attribute.roles.name | Directly mapped from the `data.detail.userIdentity.type` field in the raw log.  
data.id | metadata.product_log_id | Directly mapped from the `data.id` field in the raw log.  
data.time | metadata.event_timestamp.seconds | The seconds value of the timestamp parsed from the `data.time` field in the raw log.  
N/A | metadata.event_type | This field is derived by the parser logic based on the value of `data.detail.eventName`: if eventName is "Decrypt" or "Encrypt", then event_type is "USER_RESOURCE_ACCESS", if eventName is "GenerateDataKey" then event_type is "USER_RESOURCE_CREATION", otherwise event_type is "GENERIC_EVENT".  
N/A | metadata.log_type | Value is hardcoded to "AWS_KMS" in the parser code.  
N/A | metadata.product_name | Value is hardcoded to "AWS Key Management Service" in the parser code.  
N/A | metadata.vendor_name | Value is hardcoded to "AMAZON" in the parser code.  
N/A | principal.asset.attribute.cloud.environment | Value is hardcoded to "AMAZON_WEB_SERVICES" in the parser code.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-kms-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
