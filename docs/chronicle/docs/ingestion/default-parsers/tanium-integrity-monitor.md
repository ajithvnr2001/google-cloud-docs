---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-integrity-monitor/
title: Collect Tanium Integrity Monitor logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:26:56.837187+00:00
---

# Collect Tanium Integrity Monitor logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-integrity-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Integrity Monitor logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Integrity Monitor logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Integrity Monitor produces file and registry integrity monitoring events in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser first extracts fields like "computer_name", "process_path", and "change_type" from the "message" field of Tanium Integrity Monitor JSON logs using pattern matching. Then, it structures these extracted fields and some directly parsed JSON fields into the unified data model (UDM) format, handling both single-value and multi-value fields. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Tanium Console** with Integrity Monitor and Connect modules installed
  * Privileged access to **AWS** (S3, IAM)



## Collect Tanium Integrity Monitor prerequisites

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Administration > Permissions > Users**.
  3. Create or identify a service account user with the following roles: 
     * **Integrity Monitor Service Account** role.
     * **Connect User** role privilege.
     * Access to monitored computer groups (recommended: **All Computers** group).



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-integrity-monitor-logs`).
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
  16. Select **Attach policies directly**
  17. Search for and select the **AmazonS3FullAccess** policy.
  18. Click **Next**.
  19. Click **Add permissions**.



## Configure Tanium Connect AWS S3 destination

  1. Sign in to the **Tanium Console**.
  2. Go to **Modules > Connect**.
  3. Click **Create Connection**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Integrity Monitor to S3 for SecOps`).
     * **Description** : Optional description (for example, `Export IM events to AWS S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection to run on schedule.
  5. Click **Next**.



### Configure the connection source

  1. Select **Integrity Monitor Events** as the source type.
  2. Provide the following configuration details: 
     * **Source** : Select **Integrity Monitor - Monitor Events**.
     * **Service Account** : The connection will use the Tanium Connect service account configured in Integrity Monitor settings.
     * **Monitor** : Select **All Monitors** or choose specific monitors to export.
     * **Event types** : Select event types to include: 
       * **File events** : Include file creation, modification, deletion events.
       * **Registry events** : Include registry key changes (Windows only).
       * **Permission events** : Include file permission changes.
     * **Include labeled events** : Select to include events with labels.
     * **Include unlabeled events** : Select to include events without labels.
  3. Click **Next**.



### Configure AWS S3 destination

  1. Select **AWS S3** as the destination type.
  2. Provide the following configuration details: 
     * **Destination name** : Enter a unique name (for example, `Google SecOps S3 Destination`).
     * **AWS Access Key** : Enter the AWS access key from the previous step.
     * **AWS Secret Access Key** : Enter the AWS secret access key from the previous step.
     * **Bucket name** : Enter your S3 bucket name (for example, `tanium-integrity-monitor-logs`).
     * **Region** : Select the AWS region where your S3 bucket is located.
     * **Key prefix** : Enter a prefix for the S3 objects (for example, `tanium/integrity-monitor/`).
     * **Advanced Settings** : 
       * **File naming** : Select **Date and time-based naming**.
       * **File format** : Select **JSON Lines** for optimal Google SecOps ingestion.
       * **Compression** : Select **Gzip** to reduce storage costs.
  3. Click **Next**.



### Optional: Configure filters

  1. Configure data filters if needed: 
     * **New items only** : Select to send only new events since last export.
     * **Event filters** : Add filters based on event attributes if specific filtering is required.
     * **Computer group filters** : Select specific computer groups if needed.
  2. Click **Next**.



### Format data for AWS S3

  1. Configure the data format: 
     * **Format** : Select **JSON**.
     * **Include headers** : Deselect to avoid headers in JSON output.
     * **Field mappings** : Use default field mappings or customize as needed.
     * **Timestamp format** : Select **ISO 8601** format for consistent time representation.
  2. Click **Next**.



### Schedule the connection

  1. In the **Schedule** section, configure the export schedule: 
     * **Enable schedule** : Select to enable automatic scheduled exports.
     * **Schedule type** : Select **Recurring**.
     * **Frequency** : Select **Hourly** for regular data export.
     * **Start time** : Set appropriate start time for the first export.
  2. Click **Next**.



### Save and verify connection

  1. Review the connection configuration in the summary screen.
  2. Click **Save** to create the connection.
  3. Click **Test Connection** to verify the configuration.
  4. If the test is successful, click **Run Now** to perform an initial export.
  5. Monitor the connection status in the **Connect Overview** page.



## Configure a feed in Google SecOps to ingest Tanium Integrity Monitor logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Integrity Monitor logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Integrity Monitor** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-integrity-monitor-logs/tanium/integrity-monitor/`
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
Computer Name | principal.hostname | Directly mapped from the "Computer Name" field in the raw log.  
Count | additional.fields.value.string_value | Directly mapped from the "Count" field in the raw log.  
CreateNewFile | security_result.category_details | Directly mapped from the "Change Type" field in the raw log when its value is "CreateNewFile".  
Hash | target.file.sha256 | Directly mapped from the "Hash" field in the raw log.  
"No events matched the filters" | security_result.about.labels.value | Directly mapped from the "ID" field in the raw log when its value is "No events matched the filters".  
| additional.fields.key | Hardcoded to "Count" by the parser.  
| metadata.event_timestamp | Populated with the `create_time` field from the raw log.  
| metadata.event_type | Set to "STATUS_UPDATE" by the parser logic when the "principal_hostname" field is successfully extracted.  
| metadata.log_type | Hardcoded to "TANIUM_INTEGRITY_MONITOR" by the parser.  
| metadata.product_name | Hardcoded to "Tanium Integrity Monitor" by the parser.  
| metadata.vendor_name | Hardcoded to "Tanium Integrity Monitor" by the parser.  
| security_result.about.labels.key | Hardcoded to "ID" by the parser.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-integrity-monitor-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
