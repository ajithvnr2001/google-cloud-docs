---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/covid-ctc-ioc/
title: Collect COVID-19 Cyber Threat Coalition IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:09.881842+00:00
---

# Collect COVID-19 Cyber Threat Coalition IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/covid-ctc-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect COVID-19 Cyber Threat Coalition IOC logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest COVID-19 Cyber Threat Coalition IOC logs to Google Security Operations using Google Cloud Storage V2.

**Note:** The COVID-19 Cyber Threat Coalition (CTC) ceased coordinated operations around September 2020. The CTC blocklist is no longer actively maintained, and the primary data feeds have been discontinued. Some historical IOC data may still be available through [AlienVault OTX](https://otx.alienvault.com/). This guide is preserved for organizations that have previously downloaded CTC IOC files and wish to ingest historical data into Google SecOps.

The COVID-19 Cyber Threat Coalition (CTC) was a community-driven threat intelligence initiative that aggregated indicators of compromise (IOCs) related to COVID-19 themed cyber threats, including phishing domains, malicious URLs, and suspicious IP addresses. The CTC distributed IOC feeds as downloadable files. To ingest these files, you must upload them to a Google Cloud Storage (GCS) bucket and then configure a Google SecOps feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Access to previously downloaded COVID-19 Cyber Threat Coalition IOC feed files or historical data from AlienVault OTX



## Create Google Cloud Storage bucket

  1. Go to the [the Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `covid-ctc-ioc-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Upload IOC files to GCS

**Note:** The CTC blocklist and primary IOC feeds are no longer maintained. This section describes how to upload previously downloaded historical IOC files to GCS.

### Obtain IOC data (historical)

The CTC originally distributed IOC data through the following channels:

  * **CTC Blocklist** : A curated list of COVID-19 themed malicious domains and URLs, previously available at `cyberthreatcoalition.org/blocklist` (now discontinued).
  * **AlienVault OTX** : The CTC community contributed IOC data to AlienVault Open Threat Exchange (OTX). Some historical IOC data may still be accessible through the [AlienVault OTX platform](https://otx.alienvault.com/).
  * **Direct file downloads** : IOC files were distributed in CSV and text formats through the CTC website and community channels.



### Upload historical IOC files using the Google Cloud console

Since the CTC IOC data is no longer actively produced, a one-time or infrequent upload is the most appropriate approach.

  1. Go to the [the Google Cloud console](https://console.cloud.google.com/).
  2. In the navigation menu, go to **Cloud Storage > Buckets**.
  3. Click on your bucket name (for example, `covid-ctc-ioc-logs`).
  4. Click **Create folder**.
  5. Enter `ioc-data` as the folder name.
  6. Click **Create**.
  7. Navigate into the `ioc-data` folder.
  8. Click **Upload files**.
  9. Select the CTC IOC files from your local machine and upload them.



### Alternative: Storage Transfer Service (for bulk uploads)

If you have a large number of historical IOC files stored on an on-premise file system, use Storage Transfer Service with a Transfer Agent.

  1. In the **GCP Console** , go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **POSIX filesystem** as the source.
  4. Follow the instructions to install the [Storage Transfer Agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) on the machine with the IOC files.
  5. Configure the transfer job:

Setting | Value  
---|---  
**Source directory** | Path to the directory containing CTC IOC files  
**Destination bucket** | `covid-ctc-ioc-logs`  
**Destination path** | `ioc-data/`  
**Schedule** | Run once (or as needed)  
  6. Click **Create**.




## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `COVID CTC IOC Feed`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **COVID-19 Cyber Threat Coalition** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://covid-ctc-ioc-logs/ioc-data/
           

       * Replace: 
         * `covid-ctc-ioc-logs`: Your GCS bucket name.
         * `ioc-data`: Optional prefix/folder path where IOC files are stored.
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
`domain` | `domain_and_ports.domain` | Directly mapped  
`ip_address` | `ip_and_ports.ip_address` | Directly mapped  
N/A | `categorization` | Constant: `Suspicious COVID-19 Related Activity`  
N/A | `confidence_score` | Constant: `Low`  
N/A | `description` | Constant: `Suspected to be associated with a COVID-19 related attack...`  
N/A | `feed_name` | Constant: `COVID-19 Cyber Threat Coalition`  
N/A | `raw_severity` | Constant: `Low`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
