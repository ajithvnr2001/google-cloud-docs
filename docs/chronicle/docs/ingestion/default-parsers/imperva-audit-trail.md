---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail/
title: Collect Imperva Audit Trail logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:14.964061+00:00
---

# Collect Imperva Audit Trail logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-audit-trail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Imperva Audit Trail logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Imperva Audit Trail logs to Google Security Operations using Amazon S3. Imperva Audit Trail provides comprehensive logging of all administrative actions performed in your Imperva account, including user logins, configuration changes, policy modifications, and system events. This integration lets you send these audit logs to Google SecOps for compliance monitoring and security analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to AWS
  * Privileged access to Imperva Console



## Collect Imperva Audit Trail prerequisites (API credentials)

  1. Sign in to the **Imperva Console** at `my.imperva.com`.
  2. Go to **Account > Account Management**.
  3. On the sidebar, click **SIEM Logs > Log Configuration**.
  4. Click **Add connection**.
  5. Select **Amazon S3** as the delivery method.
  6. Configure the connection for Amazon S3: 
     * **Connection name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **Access key** : Your S3 access key.
     * **Secret key** : Your S3 secret key.
     * **Path** : The bucket path in format `<bucket-name>/<folder>` (for example, `imperva-audit-trail-logs/chronicle`).



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save bucket **Name** and **Region** for future reference (for example, `imperva-audit-trail-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add a description tag.
  10. Click **Create access key**.
  11. Click **Download CSV file** to save the **Access Key** and **Secret Access Key** for future reference.
  12. Click **Done**.
  13. Select **Permissions** tab.
  14. Click **Add permissions** in section **Permissions policies**.
  15. Select **Add permissions**.
  16. Select **Attach policies directly**.
  17. Search for **AmazonS3FullAccess** policy.
  18. Select the policy.
  19. Click **Next**.
  20. Click **Add permissions**.



## Configure the IAM policy and role for S3 uploads

  1. In the AWS console, go to **IAM > Policies**.
  2. Click **Create policy > JSON tab**.
  3. Enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowPutObjects",
               "Effect": "Allow",
               "Action": "s3:PutObject",
               "Resource": "arn:aws:s3:::imperva-audit-trail-logs/*"
             },
             {
               "Sid": "AllowGetObjects",
               "Effect": "Allow", 
               "Action": "s3:GetObject",
               "Resource": "arn:aws:s3:::imperva-audit-trail-logs/*"
             },
             {
               "Sid": "AllowListBucket",
               "Effect": "Allow",
               "Action": "s3:ListBucket", 
               "Resource": "arn:aws:s3:::imperva-audit-trail-logs"
             }
           ]
         }
         

     * Replace `imperva-audit-trail-logs` if you entered a different bucket name.
  4. Click **Next > Create policy**.

  5. Go to **IAM > Roles > Create role > AWS service > Lambda**.

  6. Attach the newly created policy.

  7. Name the role `imperva-audit-trail-s3-role` and click **Create role**.




## Configure Imperva Audit Trail S3 connection

  1. Return to the **Imperva Console** SIEM Logs configuration.
  2. Update the Amazon S3 connection with the AWS credentials: 
     * **Access key** : The User access key with access to the S3 bucket.
     * **Secret key** : The User secret key with access to the S3 bucket.
     * **Path** : Enter the path in format `imperva-audit-trail-logs/chronicle`.
  3. Click **Test connection** to verify connectivity.
  4. Ensure the connection status shows **Available**.



## Configure Audit Trail log export

  1. In the **Connections table** , expand your Amazon S3 connection.
  2. Click **Add log type**.
  3. Provide the following configuration details: 
     * **Configuration name** : Enter a descriptive name (for example, `Audit Trail Logs to Chronicle`).
     * **Select service** : Choose **Audit Trail**.
     * **Select log types** : Select **AUDIT_TRAIL** log type.
     * **Format** : JSON (structured format for audit trail logs).
     * **State** : Set to **Enabled**.
  4. Click **Add log type** to save the configuration.



## Optional: Create read-only IAM user & keys for Google SecOps

  1. Go to **AWS Console > IAM > Users**.
  2. Click **Add users**.
  3. Provide the following configuration details: 
     * **User** : Enter `secops-reader`.
     * **Access type** : Select **Access key – Programmatic access**.
  4. Click **Create user**.
  5. Attach minimal read policy (custom): **Users > secops-reader > Permissions > Add permissions > Attach policies directly > Create policy**.
  6. In the JSON editor, enter the following policy:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::imperva-audit-trail-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::imperva-audit-trail-logs"
             }
           ]
         }
         

  7. Set the name to `secops-reader-policy`.

  8. Go to **Create policy > search/select > Next > Add permissions**.

  9. Go to **Security credentials > Access keys > Create access key**.

  10. Download the **CSV** (these values are entered into the feed).




## Configure a feed in Google SecOps to ingest Imperva Audit Trail logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Imperva Audit Trail logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Imperva Audit Trail** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://imperva-audit-trail-logs/chronicle/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-audit-trail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
