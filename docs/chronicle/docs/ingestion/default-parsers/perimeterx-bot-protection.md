---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/perimeterx-bot-protection/
title: Collect HUMAN Security (formerly PerimeterX Bot Protection) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:13:07.454083+00:00
---

# Collect HUMAN Security (formerly PerimeterX Bot Protection) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/perimeterx-bot-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HUMAN Security (formerly PerimeterX Bot Protection) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HUMAN Security (formerly known as PerimeterX Bot Protection) logs to Google Security Operations using Google Cloud Storage V2.

HUMAN Security is a bot detection and mitigation platform for web application protection. It analyzes client-side behavior, network fingerprints, and request patterns to identify and block automated threats. The HUMAN Portal provides a built-in Data Export feature that can stream bot detection activity logs to Amazon S3. To ingest these logs into Google SecOps, you export them to S3 and then use Google Cloud Storage Transfer Service to move the data to a GCS bucket.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Administrative access to the [HUMAN Portal](https://console.humansecurity.com)
  * An Amazon S3 bucket for receiving exported logs (if using S3 export)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `perimeterx-bot-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure PerimeterX Bot Defender data export

### Configure Data Export in the HUMAN Portal

  1. Sign in to the [HUMAN Portal](https://console.humansecurity.com).
  2. Go to **Bot Defender > Data Export**.
  3. Click **Add Integration** to create a new data export configuration.
  4. Provide a **custom descriptive name** for your integration.
  5. Select one or more **applications** from your account to associate with the export.
  6. Select the **Data Type** : 
     * **Logs** : Bot detection activity logs with request-level details.
     * **Metrics** : Aggregated bot traffic metrics.
  7. Select **S3** as the **Export Destination**.
  8. Provide your S3 bucket details: 
     * **S3 Bucket Name** : Enter the name of your Amazon S3 bucket.
     * **Region** : Select the AWS region of the S3 bucket.
     * **Access Key ID** : Enter the AWS access key with write permissions to the S3 bucket.
     * **Secret Access Key** : Enter the AWS secret access key.
  9. For the **Logs** data type, toggle the specific **activity types** and **fields** you want to export.
  10. Click **Save** to enable the data export.



### Transfer logs from S3 to GCS

  1. In the [Google Cloud Console](https://console.cloud.google.com/), go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **Amazon S3** as the source.
  4. Provide your S3 bucket name, access key ID, and secret access key.
  5. Select your GCS bucket (for example, `perimeterx-bot-logs`) as the destination.
  6. Set the **destination path prefix** (for example, `perimeterx-logs/`).
  7. Configure the schedule to run at regular intervals (for example, hourly or daily).
  8. Click **Create** to save the transfer job.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `PerimeterX Bot Protection Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **PerimeterX Bot Protection** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://perimeterx-bot-logs/perimeterx-logs/
           

       * Replace: 
         * `perimeterx-bot-logs`: Your GCS bucket name.
         * `perimeterx-logs`: Optional prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
true_ip_asn_name, event_type, custom_parameter1, custom_parameter2, custom_parameter3, custom_parameter4, custom_parameter5, custom_parameter6, custom_parameter7, custom_parameter8, custom_parameter9 | additional.fields | Additional fields not covered by the standard UDM schema  
| metadata.event_type | The type of the event  
user_agent | network.http.parsed_user_agent | Parsed user agent information  
referrer | network.http.referral_url | The referral URL  
user_agent | network.http.user_agent | The user agent string  
px_client_uuid | principal.asset.asset_id | Unique identifier for the asset  
domain | principal.asset.hostname | Hostname of the asset  
client_ip | principal.asset.ip | IP address of the asset  
domain | principal.hostname | Hostname of the principal  
client_ip | principal.ip | IP address of the principal  
city | principal.location.city | City of the principal  
country | principal.location.country_or_region | Country or region of the principal  
os_family | principal.platform | Platform of the principal  
os_version | principal.platform_version | Version of the platform  
px_app_id | principal.resource.attribute.labels | Labels for the principal's resource attributes  
px_vid | principal.user.userid | User ID of the principal  
browser_family, browser_version | security_result.detection_fields | Fields used in detection  
risk_score | security_result.risk_score | Risk score of the security result  
path | target.file.full_path | Full path of the target file  
full_url | target.url | URL of the target  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
`custom_parameter1", "custom_parameter2", "custom_parameter3", "custom_parameter4", "custom_parameter5", "custom_parameter6", "custom_parameter7` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/perimeterx-bot-protection-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
