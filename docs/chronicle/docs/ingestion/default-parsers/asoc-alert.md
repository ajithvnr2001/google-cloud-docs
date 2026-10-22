---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert/
title: Collect AlphaSOC alert logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:27.536598+00:00
---

# Collect AlphaSOC alert logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asoc-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AlphaSOC alert logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest **AlphaSOC Alert** logs to Google Security Operations using **Amazon S3**. The parser extracts security alert data from ASOC alerts in JSON format, transforming it into the Unified Data Model (UDM). It parses fields related to observer, principal, target, and metadata, enriching the data with security results derived from threat information, severity levels, and associated categories, before finally structuring the output into the UDM format.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to the **AlphaSOC** platform.
  * Privileged access to **AWS** (S3, Identity and Access Management (IAM)).



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket-overview.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `alphasoc-alerts-logs`).
  3. Create an **IAM user** with minimal required permissions for S3 access following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select the **Security credentials** tab.
  6. In the **Access Keys** section, click **Create Access Key** .
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download .CSV file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select the **Permissions** tab.
  14. Click **Add permissions > Create policy > JSON**.
  15. Provide the following minimal policy for S3 access (replace `<BUCKET_NAME>` and `<OBJECT_PREFIX>` with your values):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "ListBucketPrefix",
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::<BUCKET_NAME>",
               "Condition": { 
                 "StringLike": { 
                   "s3:prefix": ["<OBJECT_PREFIX>/*"] 
                 } 
               }
             },
             {
               "Sid": "GetObjects",
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::<BUCKET_NAME>/<OBJECT_PREFIX>/*"
             }
           ]
         }
         

  16. Optional: If you plan to use the **Delete transferred files** option in the feed, add this additional statement to the policy:
         
         {
           "Sid": "DeleteObjectsIfEnabled",
           "Effect": "Allow",
           "Action": ["s3:DeleteObject"],
           "Resource": "arn:aws:s3:::<BUCKET_NAME>/<OBJECT_PREFIX>/*"
         }
         

  17. Click **Next > Create policy**.

  18. Return to the IAM user and click **Add permissions > Attach policies directly**.

  19. Search for and select the policy you just created.

  20. Click **Next > Add permissions**.




## Configure IAM role for AlphaSOC to export findings into your S3 bucket

  1. In the **AWS Console** , go to **IAM > Roles > Create role**.
  2. Select **Custom trust policy** and paste the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "AWS": "arn:aws:iam::610660487454:role/data-export"
               },
               "Action": "sts:AssumeRole"
             }
           ]
         }
         

  3. Click **Next**.

  4. Click **Create policy** to add an **inline policy** that allows writes to your chosen prefix (replace `<BUCKET_ARN>` and `<OBJECT_PREFIX>` such as `alphasoc/alerts`):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "InlinePolicy",
               "Effect": "Allow",
               "Action": ["s3:PutObject", "s3:PutObjectAcl"],
               "Resource": "<BUCKET_ARN>/<OBJECT_PREFIX>/*"
             }
           ]
         }
         

  5. If your bucket uses **KMS encryption** , add this statement to the same policy (replace `<AWS_REGION>`, `<AWS_ACCOUNT_ID>`, and `<AWS_KEY_ID>` with your values):
         
         {
           "Sid": "KMSkey",
           "Effect": "Allow",
           "Action": "kms:GenerateDataKey",
           "Resource": "arn:aws:kms:<AWS_REGION>:<AWS_ACCOUNT_ID>:key/<AWS_KEY_ID>"
         }
         

  6. Name the role (for example, `AlphaSOC-S3-Export`), click **Create role** , and copy its **Role ARN** for the next step.




## Provide S3 export configuration details to AlphaSOC

  1. Contact **AlphaSOC support** (`support@alphasoc.com`) or your AlphaSOC representative and provide the following configuration details to enable S3 export of findings: 
     * **S3 bucket name** (for example, `alphasoc-alerts-logs`)
     * **S3 bucket AWS region** (for example, `us-east-1`)
     * **S3 object prefix** (destination path for storing findings, for example, `alphasoc/alerts`)
     * **IAM role ARN** created in the previous section
     * Request to enable **S3 export** for findings or alerts from your workspace
  2. AlphaSOC will configure the S3 export integration on their side and provide confirmation once the setup is complete.



## Configure a feed in Google SecOps to ingest AlphaSOC Alerts

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `AlphaSOC Alerts`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **AlphaSOC** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://alphasoc-alerts-logs/alphasoc/alerts/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) (for example, `alphasoc.alerts`)
     * Optional: **Ingestion labels** : Add an ingestion label (for example, `vendor=alphasoc`, `type=alerts`).
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
