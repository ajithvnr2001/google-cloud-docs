---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch/
title: Collect Tanium Patch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:11.494919+00:00
---

# Collect Tanium Patch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Patch logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Patch logs to Google Security Operations using Tanium Connect's native AWS S3 export functionality. Tanium Patch produces patch deployment, compliance, and vulnerability data in JSON format, which can be directly exported to S3 using Tanium Connect without requiring custom Lambda functions. The parser transforms the assessment JSON data into Google SecOps's Unified Data Model (UDM). It first normalizes key names, extracts data from the JSON structure, and then maps relevant fields to UDM attributes, including vulnerability details, security result information, and asset details like hostname and operating system. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * **Tanium Core Platform** 7.0 or later
  * **Tanium Patch** module installed and configured
  * **Tanium Connect** module installed with valid license
  * Privileged access to **Tanium Console** with administrative rights
  * Privileged access to **AWS** (S3, IAM)



## Configure Tanium Patch service account

  1. Sign in to the **Tanium Console**.
  2. Go to **Modules > Patch**.
  3. Click **Settings** at the top right.
  4. In the **Service Account** section, configure the following: 
     * **Service Account User** : Select a user with appropriate Patch permissions.
     * **Verify** the account has Connect User role privilege.
  5. Click **Save** to apply the service account configuration.



## Collect Tanium Patch prerequisites

  1. Sign in to the **Tanium Console** as an administrator.
  2. Go to **Administration > Permissions > Users**.
  3. Create or identify a service account user with the following roles:

     * **Patch Administrator** or **Patch Read Only User** role.
     * **Connect User** role privilege.
     * Access to monitored computer groups (recommended: **All Computers** group).
**Note:** The service account credentials are used internally by Tanium Connect to authenticate and retrieve Patch data. These credentials are configured during the Tanium Connect source setup within the Tanium Console interface.



## Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-patch-logs`).
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
     * **Name** : Enter a descriptive name (for example, `Patch Data to S3 for SecOps`).
     * **Description** : Optional description (for example, `Export Patch compliance and deployment data to AWS S3 for Google SecOps ingestion`).
     * **Enable** : Select to enable the connection to run on schedule.
  5. Click **Next**.



### Configure the connection source

  1. In the **Source** section, provide the following configuration details: 
     * **Source Type** : Select **Saved Question**.
     * **Saved Question** : Select one of the following Patch-related saved questions: 
       * **Patch - Deployment Results** for patch deployment status.
       * **Patch - Missing Patches** for vulnerability compliance data.
       * **Patch - Installed Patches** for installed patch inventory.
       * **Patch - Patch List** for comprehensive patch status.
     * **Computer Group** : Select **All Computers** or specific computer groups to monitor.
     * **Refresh Interval** : Set appropriate interval for data collection (for example, **1 hour**).
  2. Click **Next**.



### Configure AWS S3 destination

  1. In the **Destination** section, provide the following configuration details: 
     * **Destination Type** : Select **AWS S3**.
     * **Destination Name** : Enter a unique name (for example, `Google SecOps Patch S3 Destination`).
     * **AWS Access Key** : Enter the AWS access key from the CSV file downloaded in the AWS S3 configuration step.
     * **AWS Secret Access Key** : Enter the AWS secret access key from the CSV file downloaded in the AWS S3 configuration step.
     * **Bucket Name** : Enter your S3 bucket name (for example, `tanium-patch-logs`).
     * **Region** : Select the AWS region where your S3 bucket is located.
     * **Key Prefix** : Enter a prefix for the S3 objects (for example, `tanium/patch/`).
  2. Click **Next**.



### Configure filters

  1. In the **Filters** section, configure data filtering options: 
     * **Send new items only** : Select this option to send only new results since the last export.
     * **Column filters** : Add filters based on specific patch attributes if needed (for example, filter by patch severity, deployment status).
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
     * **Frequency** : Select **Hourly** for regular patch data export.
     * **Start time** : Set appropriate start time for the first export.
  2. Click **Next**.



### Save and verify connection

  1. Review the connection configuration in the summary screen.
  2. Click **Save** to create the connection.
  3. Click **Test Connection** to verify the configuration.
  4. If the test is successful, click **Run Now** to perform an initial export.
  5. Monitor the connection status in the **Connect Overview** page.



## Configure a feed in Google SecOps to ingest Tanium Patch logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Patch logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Patch** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-patch-logs/tanium/patch/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
Bulletins | `principal.asset.vulnerabilities.vendor_vulnerability_id` | The value is taken from the "Bulletins" field in the raw log, for the corresponding index of the "Title" field. If the value is "None", the field is not mapped.  
ComputerName | `principal.hostname` | The value is taken from the "ComputerName" field in the raw log.  
ComputerName | `principal.asset.hostname` | The value is taken from the "ComputerName" field in the raw log.  
CVEIDs | `principal.asset.vulnerabilities.cve_id` | The value is taken from the "CVEIDs" field in the raw log, for the corresponding index of the "Title" field. If the value is "None", the field is not mapped.  
KBArticles | `principal.asset.vulnerabilities.vendor_knowledge_base_article_id` | The value is taken from the "KBArticles" field in the raw log, for the corresponding index of the "Title" field. If the value is empty, the field is not mapped.  
KBArticles | `security_result.summary` | The value is taken from the "KBArticles" field in the raw log, for the corresponding index of the "Title" field. If the value is empty, the field is not mapped.  
OSType | `principal.asset.platform_software.platform` | If the value contains "Windows", the platform is set to "WINDOWS". If the value contains "Linux", the platform is set to "LINUX". If the value contains "Mac", the platform is set to "MAC".  
Severity | `principal.asset.vulnerabilities.severity` | The value is taken from the "Severity" field in the raw log, for the corresponding index of the "Title" field. If the value is "Critical", the severity is set to "HIGH". If the value is "Important", the severity is set to "MEDIUM". Otherwise, the severity is set to "UNKNOWN_SEVERITY".  
Severity | `principal.asset.vulnerabilities.severity_details` | The value is taken from the "Severity" field in the raw log, for the corresponding index of the "Title" field. If the value is "Critical" or "Important", the severity details are set to the raw log value.  
Title | `principal.asset.vulnerabilities.name` | The value is taken from the "Title" field in the raw log.  
Title | `security_result.description` | The value is taken from the "Title" field in the raw log, for the corresponding index of the "InstallStatus" field. If the "InstallStatus" value is not "Installed", the description is set to the raw log value.  
- | `metadata.event_timestamp` | The value is taken from the "create_time" field in the raw log.  
- | `metadata.event_type` | The value is set to "SCAN_HOST".  
- | `metadata.log_type` | The value is taken from the "log_type" field in the raw log.  
- | `metadata.product_name` | The value is set to "Patch".  
- | `metadata.vendor_name` | The value is set to "Tanium".  
- | `principal.asset.vulnerabilities.vendor` | The value is set to "Tanium".  
- | `security_result.category` | The value is set to "DATA_AT_REST".  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
