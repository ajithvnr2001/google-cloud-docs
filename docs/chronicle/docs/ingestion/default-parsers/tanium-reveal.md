---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal/
title: Collect Tanium Reveal logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:59.927171+00:00
---

# Collect Tanium Reveal logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-reveal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Reveal logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Reveal logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Reveal produces sensitive data discovery alerts, compliance findings, and data classification results in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser processes the JSON logs, transforming them into the UDM format. It parses the JSON message, extracts fields like Computer ID, Computer Name, and Rule Name, maps them to UDM fields, and handles specific Reveal events like "Endpoints with Confirmed Sensitive Data" to populate security result details.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * **Tanium Core Platform** 7.0 or later
  * **Tanium Reveal** module installed and configured
  * **Tanium Connect** module installed with valid license
  * **Tanium Trends** 3.6.343 or later for reporting integration
  * Privileged access to **Tanium Console** with administrative rights
  * Privileged access to **AWS** (S3, IAM)



## Configure Tanium Reveal service account

  1. Sign in to the **Tanium Console**.
  2. Go to **Modules > Reveal**.
  3. Click **Settings** at the top right.
  4. In the **Service Account** section, configure the following: 
     * **Service Account User** : Select a user with appropriate Reveal permissions.
     * **Verify** the account has Connect User role privilege.
     * **Confirm** access to Reveal data sources and rules.
  5. Click **Save** to apply the service account configuration.



## Collect Tanium Reveal prerequisites

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Administration > Permissions > Users**.
  3. Create or identify a service account user with the following roles: 
     * **Reveal Administrator** or **Reveal Read Only User** role.
     * **Connect User** role privilege.
     * Access to monitored computer groups (recommended: **All Computers** group).
     * **Read Saved Question** permission for Reveal content sets.

**Note:** The service account credentials are used internally by Tanium Connect to authenticate and retrieve Reveal sensitive data findings. These credentials are configured during the Tanium Connect source setup within the Tanium Console interface.

## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-reveal-logs`).
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
     * **Name** : Enter a descriptive name (for example, `Reveal Findings to S3 for SecOps`).
     * **Description** : Optional description (for example, `Export sensitive data findings and compliance alerts to AWS S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection to run on schedule.
  5. Click **Next**.



### Configure the connection source

  1. In the **Source** section, provide the following configuration details: 
     * **Source Type** : Select **Saved Question**.
     * **Saved Question** : Select one of the following Reveal-related saved questions: 
       * **Reveal - Endpoints with Confirmed Sensitive Data** for confirmed findings.
       * **Reveal - Rule Matches** for detailed rule match results.
       * **Reveal - Data Classification Results** for data type classification.
       * **Reveal - Compliance Findings** for regulatory compliance status.
     * **Computer Group** : Select **All Computers** or specific computer groups to monitor.
     * **Refresh Interval** : Set appropriate interval for data collection (for example, **15 minutes** for sensitive data alerts).
  2. Click **Next**.



### Configure AWS S3 destination

  1. In the **Destination** section, provide the following configuration details: 
     * **Destination Type** : Select **AWS S3**.
     * **Destination Name** : Enter a unique name (for example, `Google SecOps Reveal S3 Destination`).
     * **AWS Access Key** : Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
     * **AWS Secret Access Key** : Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
     * **Bucket Name** : Enter your S3 bucket name (for example, `tanium-reveal-logs`).
     * **Region** : Select the AWS region where your S3 bucket is located.
     * **Key Prefix** : Enter a prefix for the S3 objects (for example, `tanium/reveal/`).
  2. Click **Next**.



### Configure filters

  1. In the **Filters** section, configure data filtering options: 
     * **Send new items only** : Select this option to send only new sensitive data findings since the last export.
     * **Column filters** : Add filters based on specific finding attributes if needed (for example, filter by rule severity, data type, or compliance framework).
  2. Click **Next**.



### Format data for AWS S3

  1. In the **Format** section, configure the data format: 
     * **Format** : Select **JSON**.
     * **Options** : 
       * **Include headers** : Deselect to avoid headers in JSON output.
       * **Include empty cells** : Select based on your preference.
     * **Advanced Options** : 
       * **File naming** : Use default timestamp-based naming.
       * **Compression** : Select **Gzip** to reduce storage costs and transfer time.
  2. Click **Next**.



### Schedule the connection

  1. In the **Schedule** section, configure the export schedule: 
     * **Enable schedule** : Select to enable automatic scheduled exports.
     * **Schedule type** : Select **Recurring**.
     * **Frequency** : Select **Every 15 minutes** for timely sensitive data alerts.
     * **Start time** : Set appropriate start time for the first export.
  2. Click **Next**.



### Save and verify connection

  1. Review the connection configuration in the summary screen.
  2. Click **Save** to create the connection.
  3. Click **Test Connection** to verify the configuration.
  4. If the test is successful, click **Run Now** to perform an initial export.
  5. Monitor the connection status in the **Connect Overview** page.



## Configure a feed in Google SecOps to ingest Tanium Reveal logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Reveal logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Reveal** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-reveal-logs/tanium/reveal/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`Time` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`Computer-Name` | `principal.hostname` | Directly mapped  
`sec_result` | `security_result` | Merged  
`sec_result1` | `security_result` | Merged  
`Computer-ID` | `target.resource.id` | Directly mapped  
N/A | `metadata.event_type` | Constant: `SCAN_HOST`  
N/A | `metadata.product_name` | Constant: `Reveal`  
N/A | `metadata.vendor_name` | Constant: `Tanium`  
N/A | `target.asset.type` | Constant: `SERVER`  
N/A | `target.resource.resource_type` | Constant: `DEVICE`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
