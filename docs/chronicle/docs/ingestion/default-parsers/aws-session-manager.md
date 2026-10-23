---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-session-manager/
title: Collect AWS Session Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:40.156280+00:00
---

# Collect AWS Session Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-session-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS Session Manager logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AWS Session Manager logs to Google Security Operations. AWS Session Manager provides secure and auditable access to Amazon EC2 instances and on-premises servers. By integrating its logs into Google SecOps, you can enhance your security posture and track remote access events.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to AWS



## Configure AWS IAM and S3

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



## How to configure AWS Session Manager to Save Logs in S3

  1. Go to the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/).
  2. In the navigation pane, select **Session Manager**.
  3. Click the **Preferences** tab.
  4. Click **Edit**.
  5. Under S3 logging, select the **Enable** checkbox.
  6. Deselect the **Allow only encrypted S3 buckets** checkbox.
  7. Select an Amazon S3 bucket that has already been created in your account to store session log data.
  8. Enter the name of an Amazon S3 bucket that has already been created in your account to store session log data.
  9. Click **Save**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the AWS Session Manager feed

  1. Click the **Amazon Cloud Platform** pack.
  2. Locate the **AWS Session Manager** log type.
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
`--cid` | metadata.description | Part of the description field when present in the log  
`--collector.filesystem.ignored-mount-points` | metadata.description | Part of the description field when present in the log  
`--collector.vmstat.fields` | metadata.description | Part of the description field when present in the log  
`--message-log` | metadata.description | Part of the description field when present in the log  
`--name` | metadata.description | Part of the description field when present in the log  
`--net` | metadata.description | Part of the description field when present in the log  
`--path.procfs` | metadata.description | Part of the description field when present in the log  
`--path.rootfs` | metadata.description | Part of the description field when present in the log  
`--path.sysfs` | metadata.description | Part of the description field when present in the log  
`-v /:/rootfs:ro` | metadata.description | Part of the description field when present in the log  
`-v /proc:/host/proc` | metadata.description | Part of the description field when present in the log  
`-v /sys:/host/sys` | metadata.description | Part of the description field when present in the log  
`CID` | metadata.description | Part of the description field when present in the log  
`ERROR` | security_result.severity | Extracted from the log message using grok pattern matching.  
`falconctl` | metadata.description | Part of the description field when present in the log  
`ip-1-2-4-2` | principal.ip | Extracted from the log message using grok pattern matching and converted to a standard IP address format.  
`ip-1-2-8-6` | principal.ip | Extracted from the log message using grok pattern matching and converted to a standard IP address format.  
`java` | target.process.command_line | Extracted from the log message using grok pattern matching.  
`Jun13` | metadata.event_timestamp.seconds | Part of the timestamp field when present in the log, combined with month_date and time_stamp fields.  
`[kworker/u16:8-kverityd]` | target.process.command_line | Extracted from the log message using grok pattern matching.  
`root` | principal.user.userid | Extracted from the log message using grok pattern matching.  
| metadata.event_type | Determined based on the presence and values of other fields:   
\- "STATUS_UPDATE" if src_ip is present.   
\- "NETWORK_CONNECTION" if both src_ip and dest_ip are present.   
\- "USER_UNCATEGORIZED" if user_id is present.   
\- "GENERIC_EVENT" otherwise.  
| metadata.log_type | Set to "AWS_SESSION_MANAGER".  
| metadata.product_name | Set to "AWS Session Manager".  
| metadata.vendor_name | Set to "Amazon".  
| target.process.pid | Extracted from the log message using grok pattern matching.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-session-manager-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
