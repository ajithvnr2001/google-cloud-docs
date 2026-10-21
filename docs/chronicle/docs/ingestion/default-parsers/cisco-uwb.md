---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-uwb/
title: Collect Cisco Umbrella Web Proxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:10:01.629114+00:00
---

# Collect Cisco Umbrella Web Proxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-uwb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Umbrella Web Proxy logs

**Parser Version:** 16.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Umbrella Web Proxy logs to Google Security Operations using Amazon S3. Cisco Umbrella Web Proxy provides full URL visibility and control for web traffic, acting as a cloud-based secure web gateway (SWG). Web Proxy logs capture HTTP and HTTPS traffic details including full URLs, user identities, content types, and security verdicts for requests proxied through the Umbrella intelligent proxy.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to the **Cisco Umbrella** dashboard with Full Admin or Read-Only Admin role.
  * Privileged access to **AWS** (S3, IAM).
  * Cisco Umbrella Secure Internet Gateway (SIG) or DNS Security Advantage license with intelligent proxy enabled.



## Configure Cisco Umbrella log export to Amazon S3

Cisco Umbrella natively supports exporting Web Proxy logs to an Amazon S3 bucket that you manage. If you have already configured S3 log export for Umbrella DNS logs, the same S3 bucket and IAM configuration can be reused. Umbrella stores proxy logs in a separate prefix.

  1. Sign in to the **Cisco Umbrella** dashboard at `https://dashboard.umbrella.com`.
  2. Go to **Admin > Log Management**.
  3. If S3 log export is not yet configured, click **Use your company-managed Amazon S3 bucket**.
  4. Provide the following configuration details: 
     * **Bucket Name** : Enter the name of the S3 bucket (for example, `umbrella-logs`).
     * **Region** : Select the AWS region where your bucket is located.
  5. Copy the **AWS Account ID** and **External ID** displayed by Umbrella if not already saved.
  6. Click **Save**.

**Note:** Umbrella automatically exports both DNS logs and proxy logs to the configured S3 bucket using separate prefixes (`dnslogs/` and `proxylogs/`).

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `umbrella-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**.
  9. Optional: Add description tag.
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



## Configure the IAM policy and role for Cisco Umbrella S3 access

Cisco Umbrella requires a cross-account IAM role to write logs to your S3 bucket.

  1. In the AWS console, go to **IAM > Policies > Create policy > JSON tab**.
  2. Copy and paste the following policy (replace `umbrella-logs` if you entered a different bucket name):
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Sid": "AllowUmbrellaPutObjects",
               "Effect": "Allow",
               "Action": [
                 "s3:PutObject",
                 "s3:GetBucketLocation"
               ],
               "Resource": [
                 "arn:aws:s3:::umbrella-logs",
                 "arn:aws:s3:::umbrella-logs/*"
               ]
             }
           ]
         }
         

  3. Click **Next > Create policy**. Name it `UmbrellaS3WritePolicy`.

  4. Go to **IAM > Roles > Create role > Custom trust policy**.

  5. Paste the tfollowing trust policy, replacing `UMBRELLA_AWS_ACCOUNT_ID` and `UMBRELLA_EXTERNAL_ID` with the values copied from the Umbrella dashboard:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Principal": {
                 "AWS": "arn:aws:iam::UMBRELLA_AWS_ACCOUNT_ID:root"
               },
               "Action": "sts:AssumeRole",
               "Condition": {
                 "StringEquals": {
                   "sts:ExternalId": "UMBRELLA_EXTERNAL_ID"
                 }
               }
             }
           ]
         }
         

  6. Click **Next**.

  7. Attach the `UmbrellaS3WritePolicy` policy.

  8. Name the role `UmbrellaS3Role` and click **Create role**.

  9. Copy the **Role ARN** for use in the Umbrella dashboard.




## Verify Cisco Umbrella log export

  1. Return to the **Cisco Umbrella** dashboard.
  2. Go to **Admin > Log Management**.
  3. Enter the **Role ARN** from the IAM role you created (if not already configured).
  4. Click **Verify** to confirm that Umbrella can write to the S3 bucket.
  5. After successful verification, Umbrella will begin exporting proxy logs to the S3 bucket.

**Note:** Umbrella exports Web Proxy logs in CSV format to the S3 bucket in the following path structure: `s3://umbrella-logs/proxylogs/<year>-<month>-<day>/`.

## Configure a feed in Google SecOps to ingest Cisco Umbrella Web Proxy logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Cisco Umbrella Web Proxy logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Cisco Umbrella Web Proxy** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters:

     * **S3 URI** : `s3://umbrella-logs/proxylogs/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.

  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`ampDisposition` | `security_result.detection_fields[].value` | The value of `ampDisposition` from the raw log.  
`ampMalware` | `security_result.detection_fields[].value` | The value of `ampMalware` from the raw log.  
`ampScore` | `security_result.detection_fields[].value` | The value of `ampScore` from the raw log.  
`avDetections` | `security_result.detection_fields[].value` | The value of `avDetections` from the raw log.  
`blockedCategories` | `security_result.threat_name` | The value of `blockedCategories` from the raw log.  
`certificateErrors` | `security_result.detection_fields[].value` | The value of `certificateErrors` from the raw log.  
`contentType` | `security_result.detection_fields[].value` | The value of `contentType` from the raw log.  
`destinationIp` | `target.ip` | The value of `destinationIp` from the raw log.  
`destinationListID` | `security_result.detection_fields[].value` | The value of `destinationListID` from the raw log.  
`dlpstatus` | `security_result.detection_fields[].value` | The value of `dlpstatus` from the raw log.  
`externalIp` | `principal.ip` | The value of `externalIp` from the raw log.  
`fileAction` | `security_result.detection_fields[].value` | The value of `fileAction` from the raw log.  
`fileName` | `target.file.names` | The value of `fileName` from the raw log.  
`identitiesV8` | `principal.hostname` | The value of `identitiesV8` from the raw log.  
`identity` | `principal.location.name` | The value of `identity` from the raw log.  
`internalIp` | `principal.ip` | The value of `internalIp` from the raw log.  
`isolateAction` | `security_result.detection_fields[].value` | The value of `isolateAction` from the raw log.  
`referer` | `network.http.referral_url` | The value of `referer` from the raw log.  
`requestMethod` | `network.http.method` | The value of `requestMethod` from the raw log.  
`requestSize` | `security_result.detection_fields[].value` | The value of `requestSize` from the raw log.  
`responseBodySize` | `security_result.detection_fields[].value` | The value of `responseBodySize` from the raw log.  
`responseSize` | `security_result.detection_fields[].value` | The value of `responseSize` from the raw log.  
`ruleID` | `security_result.rule_id` | The value of `ruleID` from the raw log.  
`rulesetID` | `security_result.detection_fields[].value` | The value of `rulesetID` from the raw log.  
`sha` | `security_result.about.file.sha256` | The value of `sha` from the raw log.  
`statusCode` | `network.http.response_code` | The value of `statusCode` from the raw log.  
`ts` | `timestamp` | The value of `ts` from the raw log, parsed into a timestamp.  
`url` | `target.url` | The value of `url` from the raw log.  
`userAgent` | `network.http.user_agent` | The value of `userAgent` from the raw log.  
`verdict` | `security_result.detection_fields[].value` | The value of `verdict` from the raw log.  
`warnstatus` | `security_result.detection_fields[].value` | The value of `warnstatus` from the raw log. The value of `collection_time` from the raw log. Hardcoded to `NETWORK_HTTP`. Hardcoded to `Cisco`. Hardcoded to `Umbrella`. Hardcoded to `UMBRELLA_WEBPROXY`. Derived from the scheme of the URL field (`http` or `https`). Parsed from the `userAgent` field using a user-agent parsing library. The value of `requestSize` from the raw log, converted to an integer. The value of `responseSize` from the raw log, converted to an integer. Derived from the `identity` field when `identityType` (or `identityTypeV8` with `identitiesV8`) indicates a user. Further parsed to extract user details like display name, first name, last name, and email address. Mapped from the `verdict` field: `allowed` or `allowed` -> `ALLOW`, other values -> `BLOCK`. If `categories` is not empty, set to `NETWORK_CATEGORIZED_CONTENT`. The value of `categories` from the raw log. Based on the `verdict` and potentially other fields. Usually `Traffic allowed` or `Traffic blocked`. If `verdict` is not `allowed` or `blocked` and `statusCode` is present, the summary is `Traffic %{statusCode}`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
