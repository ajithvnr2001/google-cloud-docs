---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr/
title: Collect CrowdStrike Falcon logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:49.098267+00:00
---

# Collect CrowdStrike Falcon logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CrowdStrike Falcon logs

**Parser Version:** 33.0

This document describes how to ingest CrowdStrike Falcon logs into Google Security Operations. You can ingest several types of CrowdStrike Falcon logs, and this document outlines the specific configuration for each.

For a high-level overview of data ingestion in Google Security Operations, see [Data ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

## Supported CrowdStrike Falcon log types

Google Security Operations supports the following CrowdStrike Falcon log types through the parsers with the following ingestion labels:

  * **Endpoint Detection and Response (EDR)** : `CS_EDR`. This parser parses near real-time telemetry data from CrowdStrike Falcon Data Replicator (FDR), such as file access and registry modifications. Data is typically ingested from an S3 or Cloud Storage bucket.
  * **Detections** : `CS_DETECTS`. This parser parses Detection Summary events from CrowdStrike using the Detect API. While related to endpoint activity, `CS_DETECTS` provides higher-level detection summaries compared to the raw telemetry parsed using `CS_EDR`.

**Note:** CrowdStrike has deprecated the 'Detects' endpoint. We recommend using `CS_ALERTS` instead to ingest detection logs.
  * **Alerts** : `CS_ALERTS`. This parser parses alerts from CrowdStrike using the Alerts API. The CrowdStrike Alerts parser supports the following product types:

    * `epp`
    * `idp`
    * `overwatch`
    * `xdr`
    * `mobile`
    * `cwpp`
    * `ngsiem`
  * **Indicators of Compromise (IoC)** : `CS_IOC`. This parser parses IoCs and Indicators of Attack (IOAs) from CrowdStrike Threat Intelligence using the CrowdStrike Chronicle Intel Bridge. The CrowdStrike Indicator of Compromise (IoC) parser supports the following indicator types:

    * `domain`
    * `email_address`
    * `file_name`
    * `file_path`
    * `hash_md5`
    * `hash_sha1`
    * `hash_sha256`
    * `ip_address`
    * `mutex_name`
    * `url`



Google SecOps recommends using feeds for `CS_EDR`, `CS_DETECTS`, and `CS_IOC` for comprehensive data ingestion from CrowdStrike.

## Before you begin

Ensure that you have the following prerequisites:

  * Administrator rights on the CrowdStrike instance to install the [CrowdStrike Falcon Host sensor](https://falcon.us-2.crowdstrike.com/login?next=%2Fhost-management%2Fsensor-downloads%2Fall)
  * All systems in the deployment architecture are configured in the UTC time zone.
  * Target device runs on a supported operating system 
    * Must be a 64-bit server
    * Microsoft Windows Server 2008 R2 SP1 is supported for CrowdStrike Falcon Host sensor version 6.51 or later.
    * Legacy OS versions must support SHA-2 code signing.
  * Google SecOps service account file and your customer ID from the [Google SecOps support team](https://docs.cloud.google.com/chronicle/docs/getting-support)



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform:

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Ingest CrowdStrike Falcon logs

This section describes how to configure ingestion for the different types of CrowdStrike Falcon logs.

### Ingest EDR logs (`CS_EDR`)

You can ingest CrowdStrike Falcon EDR logs using one of the following methods, depending on where you want to send the logs from CrowdStrike:

  * **Amazon SQS** : Using a Falcon Data Replicator feed.
  * **Amazon S3** : Using a Google Security Operations feed configured for an S3 bucket.
  * **Google Cloud Storage** : By having CrowdStrike push logs to a Cloud Storage bucket.



Choose one of the following procedures.

#### Option 1: Ingest EDR logs from Amazon SQS

This method uses the CrowdStrike Falcon Data Replicator to send EDR logs to an Amazon SQS queue, which Google Security Operations then polls.

  1. Click the **CrowdStrike** pack.
  2. In the **CrowdStrike Falcon** log type, specify values for the following fields:

     * **Source** : Amazon SQS
     * **Region** : The S3 region associated with URI.
     * **Queue Name** : Name of the SQS queue from which to read log data.
     * **S3 URI** : The S3 bucket source URI.
     * **Account Number** : The SQS account number.
     * **Queue Access Key ID** : 20-character account access key ID. For example, `AKIAOSFOODNN7EXAMPLE`.
     * **Queue Secret Access Key** : 40-character secret access key. For example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.
     * **Source deletion option** : Option to delete files and directories after transferring the data.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : [Namespace associated with the feed](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion Labels** – Labels applied to all events from this feed.
  3. Click **Create Feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

#### Option 2: Ingest EDR logs from an Amazon S3 bucket

This method involves setting up a Google Security Operations feed to pull EDR logs directly from an Amazon S3 bucket.

To set up an ingestion feed using an S3 bucket, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Crowdstrike Falcon Logs**.
  5. In **Source type** , select **Amazon S3**.
  6. In **Log type** , select **CrowdStrike Falcon**.
  7. Based on the service account and the Amazon S3 bucket configuration that you created, specify values for the following fields: Field | Description  
---|---  
`region` | S3 region URI.  
`S3 uri` | S3 bucket source URI.  
`uri is a` | Type of object that the URI points to (for example, file or folder).  
`source deletion option` | Option to delete files and directories after transferring the data.  
`access key id` | Access key (20-character alphanumeric string). For example, `AKIAOSFOODNN7EXAMPLE`.  
`secret access key` | Secret access key (40-character alphanumeric string). For example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`.  
`oauth client id` | Public OAuth client ID.  
`oauth client secret` | OAuth 2.0 client secret.  
`oauth secret refresh uri` | OAuth 2.0 client secret refresh URI.  
`asset namespace` | Namespace associated with the feed.  
  8. Click **Next** and then **Submit**.



#### Option 3: Ingest EDR logs from Cloud Storage

You can configure CrowdStrike to send EDR logs to a Cloud Storage bucket, and then ingest these logs into Google Security Operations using a feed. This process requires coordination with CrowdStrike Support.

  1. **Contact CrowdStrike Support:** Open a support ticket with CrowdStrike to enable and configure pushing EDR logs to your Cloud Storage bucket. They will provide guidance on the required configurations.

  2. **Create and permission the Cloud Storage bucket:**

     1. In the Google Cloud console, create a new Cloud Storage bucket. Note the bucket name (for example, `gs://my-crowdstrike-edr-logs/`).
     2. Grant write permissions to the service account provided by CrowdStrike. Follow the instructions from CrowdStrike Support.
  3. **Configure the Google SecOps feed:**

     1. In your Google SecOps instance, go to **Settings > Feeds** and click **Add New**.
     2. Enter a descriptive **Feed name** (for example, `CS-EDR-GCS`).
     3. For **Source type** , select **Google Cloud Storage V2**.

**Note:** You can use the **Google Cloud Storage Event Driven V2** as **Source type** to minimize latency.**Note:** For Cloud Storage Event Driven feed types, set up a Pub/Sub subscription for Cloud Storage, as described in [Configure Pub/Sub](https://docs.cloud.google.com/storage-transfer/docs/event-driven-google#configure_pub_sub).
     4. For **Log type** , select **CrowdStrike Falcon**.

     5. In the service account section, click **Get Service Account**. Copy the unique service account email address displayed.

     6. In the Google Cloud console, navigate to your Cloud Storage bucket and grant the `Storage Object Viewer` IAM role to the service account email address you copied. This allows the feed to read the log files.

     7. Return to the Google SecOps feed configuration page.

     8. Enter the **Storage Bucket URL** (for example, `gs://my-crowdstrike-edr-logs/`). This URL must end with a trailing forward slash (`/`).

     9. For **Event Driven** feed types, provide the **Pub/Sub Subscription Name** (for example, `projects/myproject/subscriptions/crowdstrike-edr-sub`).

     10. Select a **Source Deletion Option**. **Never delete files** is recommended.

     11. Click **Next** , review the settings, and then click **Submit**.

  4. **Verify log ingestion:** After CrowdStrike confirms that logs are being pushed, check for incoming logs in Google SecOps with the Log Type `CS_EDR`.




### Ingest Alerts logs (`CS_ALERTS`)

To ingest CrowdStrike Falcon alerts, you configure a feed that uses the CrowdStrike API.

  1. **In the CrowdStrike Falcon Console:**

     1. Sign in to the CrowdStrike Falcon Console.
     2. Go to **Support and resources** > **Resources and tools** > **API Clients and Keys** , and click **Create API client**.
     3. Enter a **Client Name** and **Description**.
     4. For **API Scopes** , select the **Read** box for **Alerts**.
     5. Click **Create**. Note the generated **Client ID** , **Client Secret** , and **Base URL**.
  2. **In Google Security Operations:**

     1. Go to **Settings > Feeds** and click **Add New**.
     2. Select **Third Party API** for **Source type**.
     3. Select **CrowdStrike Alerts API** for **Log type**.
     4. Click **Next** and populate the following fields using the values from the CrowdStrike API client:

        * **OAuth token endpoint** : For example, `https://api.us-2.crowdstrike.com/oauth2/token`.
        * **OAuth client ID**
        * **OAuth client secret**
        * **Base URL** : For example, `api.us-2.crowdstrike.com`.
        * **Ingestion Type** : Select one of the following: 
          * **Bring all alerts** : Ingests both new and existing alerts that have been updated.
          * **Bring only new alerts** : Ingests new alerts only.
**Note:** Your token endpoint may not include "us-2" in your URL. This depends on your CrowdStrike region. Use the correct base URL from the CrowdStrike console.
     5. Click **Next** and then **Submit**.




### Ingest Detections logs (`CS_DETECTS`)

**Note:** CrowdStrike has deprecated the 'Detects' endpoint. We recommend using `CS_ALERTS` instead to ingest detection logs.

To ingest CrowdStrike Falcon detection logs, you also use the CrowdStrike API.

  1. **In the CrowdStrike Falcon Console:**

     1. Sign in to the CrowdStrike Falcon Console.
     2. Go to **Support Apps** > **API Clients and Keys**.
     3. Create a new API client key pair. This key pair must have `READ` permissions for `Detections`.
  2. **In Google Security Operations:**

     1. Go to **Settings > Feeds** and click **Add New**.
     2. Select **Third Party API** for **Source type**.
     3. Select **CrowdStrike Detection Monitoring** for **Log type**.
     4. Click **Next** and then **Submit**. You will be prompted for the API credentials you created.



### Ingest IoC logs (`CS_IOC`)

To ingest Indicator of Compromise (IoC) logs from CrowdStrike, you use the Google SecOps Intel Bridge.

  1. In the CrowdStrike Falcon Console, create a new API client key pair. This key pair must have `READ` permission for `Indicators (Falcon Intelligence)`.
  2. Set up the Google SecOps Intel Bridge by following the instructions at [CrowdStrike to Google SecOps Intel Bridge](https://github.com/CrowdStrike/chronicle-intel-bridge).
  3. Run the following Docker commands to send the logs from CrowdStrike to Google SecOps. `sa.json` is your Google SecOps service account file.
         
         docker build . -t ccib:latest
         docker run -it --rm \
               -e FALCON_CLIENT_ID="$FALCON_CLIENT_ID"  \
               -e FALCON_CLIENT_SECRET="$FALCON_CLIENT_SECRET"  \
               -e FALCON_CLOUD_REGION="$FALCON_CLOUD"  \
               -e CHRONICLE_CUSTOMER_ID="$CHRONICLE_CUSTOMER_ID"  \
               -e GOOGLE_APPLICATION_CREDENTIALS=/ccib/sa.json  \
               -v  ~/my/path/to/service/account/filer/sa.json:/ccib/sa.json  \
               ccib:latest
         

  4. After the container is running, IoC logs will begin streaming into Google SecOps.




If you encounter issues with any of these configurations, contact the [Google SecOps support team](https://docs.cloud.google.com/chronicle/docs/getting-support).

## Supported CrowdStrike log formats

The CrowdStrike parser supports logs in JSON format.

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
