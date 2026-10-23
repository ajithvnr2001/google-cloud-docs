---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr/
title: Collect CrowdStrike Falcon logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:52.179423+00:00
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
    * `automated-lead`
    * `automated-lead-context`
    * `thirdparty`
    * `data-protection`
    * `fcs`
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

## CS_ALERTS UDM Mapping Delta

**Note:** In this delta, "Old UDM Mapping" refers to CrowdStrike Alerts (`CS_ALERTS`) parser releases before 27th Oct 2026. Versions released after 27th Oct 2026 include the following "New UDM Mapping".**Note:** The `metadata.event_type` value for an event can also change. Each UDM event type requires specific UDM fields to be populated. If the new UDM mapping no longer populates a required field of the event type that was previously assigned, the parser assigns a less specific event type, such as the corresponding `*_UNCATEGORIZED` event type or `GENERIC_EVENT`. Conversely, if the new UDM mapping populates all required fields of a more specific event type, the parser assigns that more specific event type. Review any rules, searches, and dashboards that filter on `metadata.event_type`.

The following table lists the delta between the old UDM mapping and the new UDM mapping of the CrowdStrike Alerts (`CS_ALERTS`) parser.

Log field | Old UDM Field Name | New UDM Field Name  
---|---|---  
`source_account_domain, device.machine_domain, logon_domain` | `principal.domain.name`  
If the `source_account_domain` log field value is _not_ empty, then The `source_account_domain` log field is mapped to the `principal.domain.name` UDM field.   
Otherwise if the `logon_domain` log field value is _not_ empty, then The `logon_domain` log field is mapped to the `principal.domain.name` UDM field.   
Otherwise if the `device.machine_domain` log field value is _not_ empty, then The `device.machine_domain` log field is mapped to the `principal.domain.name` UDM field. | `principal.domain.name`  
If the `source_account_domain` log field value is _not_ empty, then The `source_account_domain` log field is mapped to the `principal.domain.name` UDM field. If the `device.machine_domain` log field value is _not_ empty, then The `device.machine_domain` log field is mapped to the `principal.user.attribute.labels.device_machine_domain` UDM field. If the `logon_domain` log field value is _not_ empty, then The `logon_domain` log field is mapped to the `principal.user.attribute.labels.logon_domain` UDM field.   
Otherwise if the `device.machine_domain` log field value is _not_ empty, then The `device.machine_domain` log field is mapped to the `principal.domain.name` UDM field. If the `logon_domain` log field value is _not_ empty, then The `logon_domain` log field is mapped to the `principal.user.attribute.labels.logon_domain` UDM field.   
Otherwise if the `logon_domain` log field value is _not_ empty, then The `logon_domain` log field is mapped to the `principal.domain.name` UDM field.  
`source_endpoint_host_name, device.hostname, hostname, host_name, computer_name, threatgraph_indicators.hostname, host` | `principal.hostname`  
If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `principal.hostname` UDM field.   
Otherwise if the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.hostname` UDM field.   
Otherwise if the `host_name` log field value is _not_ empty, then The `host_name` log field is mapped to the `principal.hostname` UDM field.   
Otherwise if the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.hostname` UDM field.   
Otherwise if the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.hostname` UDM field.  | `principal.hostname`  
If the `hostname` log field value is _not_ empty, then The `hostname` log field is mapped to the `principal.hostname` UDM field. If the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.asset.attribute.labels.computer_name` UDM field. If the `host_name` log field value is _not_ empty, then The `host_name` log field is mapped to the `principal.asset.attribute.labels.host_name` UDM field. If the `host` log field value is _not_ empty, then The `host` log field is mapped to the `principal.asset.attribute.labels.host` UDM field. If the `device.hostname` log field value is _not_ empty, then The `device_hostname` log field is mapped to the `principal.asset.attribute.labels.device_hostname` UDM field. If the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.attribute.labels.source_endpoint_host_name` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_hostname` UDM field.  
Otherwise if the `host_name` log field value is _not_ empty, then The `host_name` log field is mapped to the `principal.hostname` UDM field. If the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.asset.attribute.labels.computer_name` UDM field. If the `host` log field value is _not_ empty, then The `host` log field is mapped to the `principal.asset.attribute.labels.host` UDM field. If the `device.hostname` log field value is _not_ empty, then The `device_hostname` log field is mapped to the `principal.asset.attribute.labels.device_hostname` UDM field. If the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.attribute.labels.source_endpoint_host_name` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields[threatgraph_indicator_hostname]` UDM field.   
Otherwise if the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.hostname` UDM field. If the `host` log field value is _not_ empty, then The `host` log field is mapped to the `principal.asset.attribute.labels.host` UDM field. If the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.asset.attribute.labels.device_hostname` UDM field. If the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.attribute.labels.source_endpoint_host_name` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_hostname` UDM field.   
Otherwise if the `host` log field value is _not_ empty, then The `host` log field is mapped to the `principal.hostname` UDM field. If the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.asset.attribute.labels.device_hostname` UDM field. If the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.attribute.labels.source_endpoint_host_name` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_hostname` UDM field.   
Otherwise if the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.hostname` UDM field. If the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.attribute.labels.source_endpoint_host_name` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_hostname` UDM field.   
Otherwise if the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.hostname` UDM field. If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_hostname` UDM field.   
Otherwise if the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `principal.hostname` UDM field.  
`source_endpoint_host_name, device.hostname, hostname, host_name, computer_name, threatgraph_indicators.hostname, host` | `principal.asset.hostname`  
If the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `host_name` log field value is _not_ empty, then The `host_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.asset.hostname` UDM field.  | `principal.asset.hostname`  
If the `hostname` log field value is _not_ empty, then The `hostname` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `host_name` log field value is _not_ empty, then The `host_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `computer_name` log field value is _not_ empty, then The `computer_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `host` log field value is _not_ empty, then The `host` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `device.hostname` log field value is _not_ empty, then The `device.hostname` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `source_endpoint_host_name` log field value is _not_ empty, then The `source_endpoint_host_name` log field is mapped to the `principal.asset.hostname` UDM field.   
Otherwise if the `threatgraph_indicators.0.hostname` log field value is _not_ empty, then The `threatgraph_indicators.0.hostname` log field is mapped to the `principal.asset.hostname` UDM field.  
`device.machine_domain` | `principal.asset.attribute.labels[device_machine_domain]` |   
`location_country_code, device_geo_location.country_name` | `principal.location.country_or_region`  
The `location_country_code` log field is mapped to the `principal.location.country_or_region` UDM field. | `principal.location.country_or_region`  
If the `device_geo_location.country_name` log field value is _not_ empty, then The `device_geo_location.country_name` log field is mapped to the `principal.location.country_or_region` UDM field. If the `location_country_code` log field value is _not_ empty, then The `location_country_code` log field is mapped to the `security_result.detection_fields.location_country_code` UDM field.   
Otherwise if the `location_country_code` log field value is _not_ empty, then The `location_country_code` log field is mapped to the `principal.location.country_or_region` UDM field.  
`source_account_upn` | `principal.user.attribute.labels[source_account_upn]` | `principal.user.email_addresses`  
`user_name` | `principal.user.attribute.labels[user_name]` |   
`user_name, source_account_name, encrypted_by_username, user_display_name` | `principal.user.user_display_name`  
If the `user_name` log field value is _not_ empty, then The `user_name` log field is mapped to the `principal.user.user_display_name` UDM field.   
Otherwise if the `source_account_name` log field value is _not_ empty, then The `source_account_name` log field is mapped to the `principal.user.user_display_name` UDM field. | `principal.user.user_display_name`  
If the `user_name` log field value is _not_ empty, then The `user_name` log field is mapped to the `principal.user.user_display_name` UDM field. If the `source_account_name` log field value is _not_ empty, then The `source_account_name` log field is mapped to the `principal.user.attribute.labels.source_account_name` UDM field. If the `encrypted_by_username` log field value is _not_ empty, then The `encrypted_by_username` log field is mapped to the `principal.user.attribute.labels.encrypted_by_username` UDM field. If the `user_display_name` log field value is _not_ empty, then The `user_display_name` log field is mapped to the `principal.user.attribute.labels.user_display_name` UDM field.   
Otherwise if the `source_account_name` log field value is _not_ empty, then The `source_account_name` log field is mapped to the `principal.user.user_display_name` UDM field. If the `encrypted_by_username` log field value is _not_ empty, then The `encrypted_by_username` log field is mapped to the `principal.user.attribute.labels.encrypted_by_username` UDM field. If the `user_display_name` log field value is _not_ empty, then The `user_display_name` log field is mapped to the `principal.user.attribute.labels.user_display_name` UDM field.   
Otherwise if the `encrypted_by_username` log field value is _not_ empty, then The `encrypted_by_username` log field is mapped to the `principal.user.user_display_name` UDM field. If the `user_display_name` log field value is _not_ empty, then The `user_display_name` log field is mapped to the `principal.user.attribute.labels.user_display_name` UDM field.   
Otherwise if the `user_display_name` log field value is _not_ empty, then The `user_display_name` log field is mapped to the `principal.user.user_display_name` UDM field.  
`source_account_object_sid, sid` | `principal.user.windows_sid` | `principal.user.windows_sid`  
If the `sid` log field value is _not_ empty, then The `sid` log field is mapped to the `principal.user.windows_sid` UDM field. If the `source_account_object_sid` log field value is _not_ empty, then The `source_account_object_sid` log field is mapped to the `principal.user.attribute.labels[source_account_object_sid]` UDM field.   
Otherwise if the `source_account_object_sid` log field value is _not_ empty, then The `source_account_object_sid` log field is mapped to the `principal.user.windows_sid` UDM field.  
`assigned_to_uuid` | `security_result.about.user.product_object_id` | `additional.fields[assigned_to_uuid]`  
`assigned_to_name` | `security_result.about.user.user_display_name` | `additional.fields[assigned_to_name]`  
`agent_id, threatgraph_indicators.host_id, host_id, mdm_device_id, device.device_id, source_asset.id` | `principal.asset_id`  
If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{threatgraph_indicators.0.host_id}`, where `%{threatgraph_indicators.0.host_id}` is replaced with the value of the `threatgraph_indicators.0.host_id` log field.   
Otherwise if the `host_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{host_id}`, where `%{host_id}` is replaced with the value of the `host_id` log field.   
Otherwise if the `agent_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the value of the `agent_id` log field.   
Otherwise if the `mdm_device_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{mdm_device_id}`, where `%{mdm_device_id}` is replaced with the value of the `mdm_device_id` log field.   
Otherwise if the `device.device_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{device.device_id}`, where `%{device.device_id}` is replaced with the value of the `device.device_id` log field. | `principal.asset_id, about.asset_id`  
If the `agent_id` log field value is _not_ empty, then the `agent_id` log field value is split into multiple values using the `|` separator. Iterate through the split `agent_id` values:  
if the `index` value is equal to `"0"`, then the `principal.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the split `agent_id` value.   
Otherwise, the `about.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the split `agent_id` value.  
If the `source_asset.id` log field value is _not_ empty, then The `source_asset.id` log field is mapped to the `principal.asset.attribute.labels.source_asset_id` UDM field. If the `host_id` log field value is _not_ empty, then The `host_id` log field is mapped to the `principal.asset.attribute.labels.host_id` UDM field. If the `device.device_id` log field value is _not_ empty, then The `device.device_id` log field is mapped to the `principal.asset.attribute.labels.device_id` UDM field. If the `mdm_device_id` log field value is _not_ empty, then The `mdm_device_id` log field is mapped to the `principal.asset.attribute.labels.mdm_device_id` UDM field. If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `threatgraph_indicators.0.host_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_host_id` UDM field.   
Otherwise if the `source_asset.id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{source_asset.id}`, where `%{source_asset.id}` is replaced with the value of the `source_asset.id` log field. If the `host_id` log field value is _not_ empty, then The `host_id` log field is mapped to the `principal.asset.attribute.labels.host_id` UDM field. If the `device.device_id` log field value is _not_ empty, then The `device.device_id` log field is mapped to the `principal.asset.attribute.labels.device_id` UDM field. If the `mdm_device_id` log field value is _not_ empty, then The `mdm_device_id` log field is mapped to the `principal.asset.attribute.labels.mdm_device_id` UDM field. If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `threatgraph_indicators.0.host_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_host_id` UDM field.   
Otherwise if the `host_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{host_id}`, where `%{host_id}` is replaced with the value of the `host_id` log field. If the `device.device_id` log field value is _not_ empty, then The `device.device_id` log field is mapped to the `principal.asset.attribute.labels.device_id` UDM field. If the `mdm_device_id` log field value is _not_ empty, then The `mdm_device_id` log field is mapped to the `principal.asset.attribute.labels.mdm_device_id` UDM field. If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `threatgraph_indicators.0.host_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_host_id` UDM field.   
Otherwise if the `device.device_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{device.device_id}`, where `%{device.device_id}` is replaced with the value of the `device.device_id` log field. If the `mdm_device_id` log field value is _not_ empty, then The `mdm_device_id` log field is mapped to the `principal.asset.attribute.labels.mdm_device_id` UDM field. If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `threatgraph_indicators.0.host_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_host_id` UDM field.   
Otherwise if the `mdm_device_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{mdm_device_id}`, where `%{mdm_device_id}` is replaced with the value of the `mdm_device_id` log field. If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `threatgraph_indicators.0.host_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicator_host_id` UDM field.   
Otherwise if the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `principal.asset_id` UDM field is set to a value generated from the template `CS:%{threatgraph_indicators.0.host_id}`, where `%{threatgraph_indicators.0.host_id}` is replaced with the value of the `threatgraph_indicators.0.host_id` log field.  
`agent_id, threatgraph_indicators.host_id, host_id, mdm_device_id, device.device_id, source_asset.id` | `principal.asset.asset_id`  
If the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{threatgraph_indicators.0.host_id}`, where `%{threatgraph_indicators.0.host_id}` is replaced with the value of the `threatgraph_indicators.0.host_id` log field.   
Otherwise if the `host_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{host_id}`, where `%{host_id}` is replaced with the value of the `host_id` log field.   
Otherwise if the `agent_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the value of the `agent_id` log field.   
Otherwise if the `mdm_device_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{mdm_device_id}`, where `%{mdm_device_id}` is replaced with the value of the `mdm_device_id` log field.   
Otherwise if the `device.device_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{device.device_id}`, where `%{device.device_id}` is replaced with the value of the `device.device_id` log field. | `principal.asset.asset_id, about.asset.asset_id`  
If the `agent_id` log field value is _not_ empty, then the `agent_id` log field value is split into multiple values using the `|` separator. Iterate through the split `agent_id` values:  
if the `index` value is equal to `"0"`, then the `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the split `agent_id` value.   
Otherwise, the `about.asset.asset_id` UDM field is set to a value generated from the template `CS:%{agent_id}`, where `%{agent_id}` is replaced with the split `agent_id` value.   
Otherwise if the `source_asset.id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{source_asset.id}`, where `%{source_asset.id}` is replaced with the value of the `source_asset.id` log field.   
Otherwise if the `host_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{host_id}`, where `%{host_id}` is replaced with the value of the `host_id` log field.   
Otherwise if the `device.device_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{device.device_id}`, where `%{device.device_id}` is replaced with the value of the `device.device_id` log field.   
Otherwise if the `mdm_device_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{mdm_device_id}`, where `%{mdm_device_id}` is replaced with the value of the `mdm_device_id` log field.   
Otherwise if the `threatgraph_indicators.0.host_id` log field value is _not_ empty, then The `principal.asset.asset_id` UDM field is set to a value generated from the template `CS:%{threatgraph_indicators.0.host_id}`, where `%{threatgraph_indicators.0.host_id}` is replaced with the value of the `threatgraph_indicators.0.host_id` log field.  
`cid, agent_id, process_id` | `target.process.product_specific_process_id`  
If the `cid` log field value is _not_ empty and the `agent_id` log field value is _not_ empty and the `process_id` log field value is _not_ empty, then the `target.process.product_specific_process_id` UDM field is set to a value generated from the template `PRODUCT_SPECIFIC_PROCESS_ID: %{cid}:%{agent_id}:%{process_id}`, where `%{cid}`, `%{agent_id}`, and `%{process_id}` are replaced with the values of the `cid`, `agent_id`, and `process_id` log fields, respectively. | `target.process.product_specific_process_id, about.process.product_specific_process_id`  
If the `agent_id` log field value is _not_ empty, then the `agent_id` log field value is split into multiple values using the `|` separator. Iterate through the split `agent_id` values:  
if the `index` value is equal to `"0"`, then if the `cid` log field value is _not_ empty and the split `agent_id` value is _not_ empty and the `process_id` log field value is _not_ empty, then the `target.process.product_specific_process_id` UDM field is set to a value generated from the template `PRODUCT_SPECIFIC_PROCESS_ID: %{cid}:%{agent_id}:%{process_id}`, where `%{agent_id}` is replaced with the split `agent_id` value, and `%{cid}` and `%{process_id}` are replaced with the values of the `cid` and `process_id` log fields, respectively.   
Otherwise, if the `cid` log field value is _not_ empty and the split `agent_id` value is _not_ empty and the `process_id` log field value is _not_ empty, then the `about.process.product_specific_process_id` UDM field is set to a value generated from the template `PRODUCT_SPECIFIC_PROCESS_ID: %{cid}:%{agent_id}:%{process_id}`, where `%{agent_id}` is replaced with the split `agent_id` value, and `%{cid}` and `%{process_id}` are replaced with the values of the `cid` and `process_id` log fields, respectively.  
`isp_domain` | `security_result.detection_fields[isp_domain]` | `principal.asset.network_domain`  
`target_endpoint_address_ip4` | `security_result.detection_fields[target_endpoint_address_ip4]` | `target.ip`  
`target_endpoint_address_ip4` | `security_result.detection_fields[target_endpoint_address_ip4]` | `target.asset.ip`  
`target_endpoint_address_ip6` | `security_result.detection_fields[target_endpoint_address_ip6]` | `target.ip`  
`target_endpoint_address_ip6` | `security_result.detection_fields[target_endpoint_address_ip6]` | `target.asset.ip`  
`start_time` | `security_result.first_discovered_time` | `security_result.detection_fields[start_time]`  
`end_time` | `security_result.last_discovered_time` | `security_result.detection_fields[end_time]`  
`severity, incident.score` | `security_result.severity_details`  
If the `product` log field value is equal to `"epp"`, then If the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise if the `product` log field value is equal to `"mobile"`, then If the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise if the `product` log field value is equal to `"xdr"`, then If the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise, if the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field. | `security_result.severity_details`  
If the `product` log field value is equal to `"epp"`, then If the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise if the `product` log field value is equal to `"mobile"`, then If the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise if the `product` log field value contain one of the following values:

  * `xdr`
  * `automated-lead-context`

, then If the `incident.score` log field value is _not_ empty, then The `incident.score` log field is mapped to the `security_result.severity_details` UDM field. Otherwise if the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field.   
Otherwise, if the `severity` log field value is _not_ empty, then The `severity` log field is mapped to the `security_result.severity_details` UDM field.  
`target_account_domain, entities.domain, domain_name, saas_domain` | `target.domain.name`  
Iterate through log field `entities.domain`  
if the `index` value is equal to `0`, then The `entities.domain` log field is mapped to the `target.domain.name` UDM field.   
Otherwise, The `entities.domain` log field is mapped to the `security_result.detection_fields.entities_domain` UDM field. | `target.domain.name`  
If the `saas_domain` log field value is _not_ empty, then The `saas_domain` log field is mapped to the `target.domain.name` UDM field. If the `target_account_domain` log field value is _not_ empty, then The `target_account_domain` log field is mapped to the `target.user.attribute.labels.target_account_domain` UDM field. If the `entities.domain.0` log field value is _not_ empty, then The `entities.domain.0` log field is mapped to the `target.user.attribute.labels.entities_domain` UDM field. If the `domain_name` log field value is _not_ empty, then The `domain_name` log field is mapped to the `target.user.attribute.labels.domain_name` UDM field.   
Otherwise if the `target_account_domain` log field value is _not_ empty, then The `target_account_domain` log field is mapped to the `target.domain.name` UDM field. If the `entities.domain.0` log field value is _not_ empty, then The `entities.domain.0` log field is mapped to the `target.user.attribute.labels.entities_domain` UDM field. If the `domain_name` log field value is _not_ empty, then The `domain_name` log field is mapped to the `target.user.attribute.labels.domain_name` UDM field.   
Otherwise if the `entities.domain.0` log field value is _not_ empty, then The `entities.domain.0` log field is mapped to the `target.domain.name` UDM field. If the `domain_name` log field value is _not_ empty, then The `domain_name` log field is mapped to the `target.user.attribute.labels.domain_name` UDM field.   
Otherwise if the `domain_name` log field value is _not_ empty, then The `domain_name` log field is mapped to the `target.domain.name` UDM field.  
`entities.domain` | `security_result.detection_fields[entities_domain]`  
Iterate through log field `entities.domain`  
if the `index` value is _not_ equal to `"0"`, then the `entities.domain` log field is mapped to the `security_result.detection_fields.entities_domain` UDM field. | `target.user.attribute.labels[entities_domain]`  
Iterate through log field `entities.domain`  
if the `index` value is _not_ equal to `"0"`, then the `entities.domain` log field is mapped to the `target.user.attribute.labels.entities_domain` UDM field.  
`target_account_upn` | `target.user.attribute.labels[target_account_upn]` | `target.user.email_addresses`  
If the `target_account_upn` log field value is _not_ empty, then If the `target_account_upn` log field value matches the regular expression pattern: `(^.+@.+$)`, then The `target_account_upn` log field is mapped to the `target.user.email_addresses` UDM field. Otherwise, The `target_account_upn` log field is mapped to the `target.user.attribute.labels.target_account_upn` UDM field.  
`documents_accessed.filename` | `security_result.about.process.file.names` | `security_result.about.file.names`  
`documents_accessed.filepath` | `security_result.about.process.file.full_path` | `security_result.about.file.full_path`  
`documents_accessed.timestamp` | `security_result.about.process.file.first_seen_time` | `security_result.about.file.last_access_time`  
`executables_written.filename` | `security_result.about.process.file.names` | `security_result.about.file.names`  
`executables_written.filepath` | `security_result.about.process.file.full_path` | `security_result.about.file.full_path`  
`executables_written.timestamp` | `security_result.about.process.file.last_modification_time` | `security_result.about.file.last_modification_time`  
`network_accesses.local_address` | `security_result.detection_fields[network_accesses_local_address]` | `principal.ip, target.ip`  
Iterate through log field `network_accesses`  
if the `network_accesses.local_address` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.local_address` log field is mapped to the `target.ip` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.local_address` log field is mapped to the `principal.ip` UDM field. Otherwise, The `network_accesses.local_address` log field is mapped to the `security_result.detection_fields.network_accesses_local_address` UDM field.  
`network_accesses.local_address` | `security_result.detection_fields[network_accesses_local_address]` | `principal.asset.ip, target.asset.ip`  
Iterate through log field `network_accesses`  
if the `network_accesses.local_address` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.local_address` log field is mapped to the `target.asset.ip` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.local_address` log field is mapped to the `principal.asset.ip` UDM field. Otherwise, The `network_accesses.local_address` log field is mapped to the `security_result.detection_fields.network_accesses_local_address` UDM field.  
`network_accesses.local_port` | `security_result.detection_fields[network_accesses_local_port]` | `principal.port, target.port`  
Iterate through log field `network_accesses`  
if the `index` value is equal to `"0"`, then If the `network_accesses.local_port` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.local_port` log field is mapped to the `target.port` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.local_port` log field is mapped to the `principal.port` UDM field. Otherwise, The `network_accesses.local_port` log field is mapped to the `security_result.detection_fields.network_accesses_local_port` UDM field.   
Otherwise, if the `network_accesses.local_port` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.local_port` log field is mapped to the `target.asset.attribute.labels.network_accesses_local_port` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.local_port` log field is mapped to the `principal.asset.attribute.labels.network_accesses_local_port` UDM field. Otherwise, The `network_accesses.local_port` log field is mapped to the `security_result.detection_fields.network_accesses_local_port` UDM field.  
`network_accesses.protocol` | `security_result.detection_fields[network_accesses_protocol]` | `network.ip_protocol`  
Iterate through log field `network_accesses.protocol`  
if the `index` value is equal to `"0"`, then The `network_accesses.protocol` log field is mapped to the `network.ip_protocol` UDM field.   
Otherwise, The `network_accesses.protocol` log field is mapped to the `security_result.detection_fields.network_accesses_protocol` UDM field.  
`network_accesses.remote_address` | `security_result.detection_fields[network_accesses_remote_address]` | `principal.ip, target.ip`  
Iterate through log field `network_accesses`  
if the `network_accesses.remote_address` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.remote_address` log field is mapped to the `principal.ip` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.remote_address` log field is mapped to the `target.ip` UDM field. Otherwise, The `network_accesses.remote_address` log field is mapped to the `security_result.detection_fields.network_accesses_remote_address` UDM field.  
`network_accesses.remote_address` | `security_result.detection_fields[network_accesses_remote_address]` | `principal.asset.ip, target.asset.ip`  
Iterate through log field `network_accesses`  
if the `network_accesses.remote_address` log field value is _not_ empty, then If the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_accesses.remote_address` log field is mapped to the `principal.asset.ip` UDM field. Otherwise if the `network_accesses` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_accesses.remote_address` log field is mapped to the `target.asset.ip` UDM field. Otherwise, The `network_accesses.remote_address` log field is mapped to the `security_result.detection_fields.network_accesses_remote_address` UDM field.  
`resource_name, bucket_name` | `target.resource.name` | `target.resource.name`  
If the `resource_name` log field value is _not_ empty, then The `resource_name` log field is mapped to the `target.resource.name` UDM field. If the `bucket_name` log field value is _not_ empty, then The `bucket_name` log field is mapped to the `target.resource.attribute.labels[bucket_name]` UDM field.   
Otherwise if the `bucket_name` log field value is _not_ empty, then The `bucket_name` log field is mapped to the `target.resource.name` UDM field.  
`image_id` | `target.resource.product_object_id` | `target.resource.attribute.labels[image_id]`  
`image_file_name` | `target.process.file.full_path` | `security_result.detection_fields[image_file_name]`  
`incident.host_ids, destination_asset.id, destination.usb_combined_id` | `target.asset_id`  
Iterate through log field `incident.host_ids`  
if the `index` value is equal to `"0"`, then The `target.asset_id` UDM field is set to a value generated from the template `CS:%{incident.host_ids}`, where `%{incident.host_ids}` is replaced with the value of the `incident.host_ids` log field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"incident_host_id"` and The `incident.host_ids` log field is mapped to the `security_result.detection_fields.value` UDM field. | `target.asset_id`  
If the `destination_asset.id` log field value is _not_ empty, then The `target.asset_id` UDM field is set to a value generated from the template `CS:%{destination_asset.id}`, where `%{destination_asset.id}` is replaced with the value of the `destination_asset.id` log field. If the `incident.host_ids.0` log field value is _not_ empty, then The `incident.host_ids.0` log field is mapped to the `security_result.detection_fields.incident_host_id` UDM field. If the `destination.usb_combined_id` log field value is _not_ empty, then The `destination.usb_combined_id` log field is mapped to the `target.asset.attribute.labels.destination_usb_combined_id` UDM field.   
Otherwise if the `incident.host_ids.0` log field value is _not_ empty, then The `target.asset_id` UDM field is set to a value generated from the template `CS:%{incident.host_ids.0}`, where `%{incident.host_ids.0}` is replaced with the value of the `incident.host_ids.0` log field. If the `destination.usb_combined_id` log field value is _not_ empty, then The `destination.usb_combined_id` log field is mapped to the `target.asset.attribute.labels.destination_usb_combined_id` UDM field.   
Otherwise if the `destination.usb_combined_id` log field value is _not_ empty, then The `target.asset_id` UDM field is set to a value generated from the template `CS:%{destination.usb_combined_id}`, where `%{destination.usb_combined_id}` is replaced with the value of the `destination.usb_combined_id` log field.  
Iterate through log field `incident.host_ids`  
if the `index` value is _not_ equal to `"0"`, then The `security_result.detection_fields.key` UDM field is set to `"incident_host_ids"` and The `incident.host_ids` log field is mapped to the `security_result.detection_fields.value` UDM field.  
`incident.host_ids, destination_asset.id, destination.usb_combined_id` | `target.asset.asset_id`  
Iterate through log field `incident.host_ids`  
if the `index` value is equal to `"0"`, then The `target.asset.asset_id` UDM field is set to a value generated from the template `CS:%{incident.host_ids}`, where `%{incident.host_ids}` is replaced with the value of the `incident.host_ids` log field.  | `target.asset.asset_id`  
If the `destination_asset.id` log field value is _not_ empty, then The `target.asset.asset_id` UDM field is set to a value generated from the template `CS:%{destination_asset.id}`, where `%{destination_asset.id}` is replaced with the value of the `destination_asset.id` log field.   
Otherwise if the `incident.host_ids.0` log field value is _not_ empty, then The `target.asset.asset_id` UDM field is set to a value generated from the template `CS:%{incident.host_ids.0}`, where `%{incident.host_ids.0}` is replaced with the value of the `incident.host_ids.0` log field.   
Otherwise if the `destination.usb_combined_id` log field value is _not_ empty, then The `target.asset.asset_id` UDM field is set to a value generated from the template `CS:%{destination.usb_combined_id}`, where `%{destination.usb_combined_id}` is replaced with the value of the `destination.usb_combined_id` log field.  
`entities.file_name` | `target.process.file.names`  
Iterate through log field `entities.file_name`   
The `entities.file_name` log field is mapped to the `target.process.file.names` UDM field.  | `security_result.detection_fields[entities_file_name]`  
Iterate through log field `entities.file_name`  
if the `entities.file_name` log field value is _not_ empty, then The `entities.file_name` log field is mapped to the `security_result.detection_fields.entities_file_name` UDM field.  
`entities.image_file_name` | `target.process.file.full_path`  
Iterate through log field `entities.image_file_name`  
if the `index` value is equal to `0`, then The `entities.image_file_name` log field is mapped to the `target.process.file.full_path` UDM field.   
Otherwise, The `entities.image_file_name` log field is mapped to the `security_result.detection_fields.entities_image_file_name` UDM field.  | `security_result.detection_fields[entities_image_file_name]`  
Iterate through log field `entities.image_file_name`  
if the `entities.image_file_name` log field value is _not_ empty, then The `entities.image_file_name` log field is mapped to the `security_result.detection_fields.entities_image_file_name` UDM field.  
`entities.process` | `target.process.pid`  
Iterate through log field `entities.process`  
if the `index` value is equal to `0`, then The `entities.process` log field is mapped to the `target.process.pid` UDM field.   
Otherwise, The `entities.process` log field is mapped to the `security_result.detection_fields.entities_process` UDM field. | `security_result.detection_fields[entities_process]`  
Iterate through log field `entities.process`  
if the `entities.process` log field value is _not_ empty, then The `entities.process` log field is mapped to the `security_result.detection_fields.entities_process` UDM field.  
`entities.sha256` | `target.process.file.sha256`  
Iterate through log field `entities.sha256`  
if the `index` value is equal to `0`, then The `entities.sha256` log field is mapped to the `target.process.file.sha256` UDM field.   
Otherwise, The `entities.sha256` log field is mapped to the `security_result.detection_fields.entities_sha256` UDM field. | `security_result.detection_fields[entities_sha256]`  
Iterate through log field `entities.sha256`  
if the `entities.sha256` log field value is _not_ empty, then The `entities.sha256` log field is mapped to the `security_result.detection_fields.entities_sha256` UDM field.  
`entities.username` | `target.user.user_display_name`  
Iterate through log field `entities.username`  
if the `index` value is equal to `0`, then The `entities.username` log field is mapped to the `target.user.user_display_name` UDM field.   
Otherwise, The `entities.username` log field is mapped to the `security_result.detection_fields.entities_username` UDM field. | `security_result.detection_fields[entities_username]`  
Iterate through log field `entities.username`  
if the `entities.username` log field value is _not_ empty, then The `entities.username` log field is mapped to the `security_result.detection_fields.entities_username` UDM field.  
`application_name, destination.name` | `target.application` | `target.application`  
If the `destination.name` log field value is _not_ empty, then The `destination.name` log field is mapped to the `target.application` UDM field. If the `application_name` log field value is _not_ empty, then The `application_name` log field is mapped to the `security_result.detection_fields[application_name]` UDM field.   
Otherwise if the `application_name` log field value is _not_ empty, then The `application_name` log field is mapped to the `target.application` UDM field.  
`network_info.local_address` | `security_result.detection_fields[network_info_local_address]` | `principal.ip, target.ip`  
Iterate through log field `network_info`  
if the `network_info.local_address` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.local_address` log field is mapped to the `target.ip` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.local_address` log field is mapped to the `principal.ip` UDM field. Otherwise, The `network_info.local_address` log field is mapped to the `security_result.detection_fields.network_info_local_address` UDM field.  
`network_info.local_address` | `security_result.detection_fields[network_info_local_address]` | `principal.asset.ip, target.asset.ip`  
Iterate through log field `network_info`  
if the `network_info.local_address` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.local_address` log field is mapped to the `target.asset.ip` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.local_address` log field is mapped to the `principal.asset.ip` UDM field. Otherwise, The `network_info.local_address` log field is mapped to the `security_result.detection_fields.network_info_local_address` UDM field.  
`network_info.protocol` | `security_result.detection_fields[network_info_protocol]` | `network.ip_protocol`  
Iterate through log field `network_info.protocol`  
if the `index` value is equal to `"0"`, then The `network_info.protocol` log field is mapped to the `network.ip_protocol` UDM field.   
Otherwise, The `network_info.protocol` log field is mapped to the `security_result.detection_fields.network_info_protocol` UDM field.  
`app_certificate_thumbprints_sha1` | `target.file.sha1` | `security_result.detection_fields[app_certificate_thumbprints_sha1]`  
`app_certificate_thumbprints_sha256` | `target.file.sha256` | `security_result.detection_fields[app_certificate_thumbprints_sha256]`  
`app_image_filename, debuggable_app_image_filename, duplicated_app_image_filename, harmful_app_image_filename, sideloaded_app_image_filename, suspicious_activities_apps.image_filename, suspicious_apps.image_filename, unexpected_dynamic_library_loaded.target_file_name, unexpected_files` | `target.file.full_path` | `target.file.full_path`  
If the `unexpected_dynamic_library_loaded.0.target_file_name` log field value is _not_ empty, then The `unexpected_dynamic_library_loaded.0.target_file_name` log field is mapped to the `target.file.full_path` UDM field. If the `harmful_app_image_filename` log field value is _not_ empty, then The `harmful_app_image_filename` log field is mapped to the `security_result.detection_fields.harmful_app_image_filename` UDM field. If the `sideloaded_app_image_filename` log field value is _not_ empty, then The `sideloaded_app_image_filename` log field is mapped to the `security_result.detection_fields.sideloaded_app_image_filename` UDM field. If the `duplicated_app_image_filename` log field value is _not_ empty, then The `duplicated_app_image_filename` log field is mapped to the `security_result.detection_fields.duplicated_app_image_filename` UDM field. If the `debuggable_app_image_filename` log field value is _not_ empty, then The `debuggable_app_image_filename` log field is mapped to the `security_result.detection_fields.debuggable_app_image_filename` UDM field. If the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `security_result.detection_fields.unexpected_files` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `harmful_app_image_filename` log field value is _not_ empty, then The `harmful_app_image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `sideloaded_app_image_filename` log field value is _not_ empty, then The `sideloaded_app_image_filename` log field is mapped to the `security_result.detection_fields.sideloaded_app_image_filename` UDM field. If the `duplicated_app_image_filename` log field value is _not_ empty, then The `duplicated_app_image_filename` log field is mapped to the `security_result.detection_fields.duplicated_app_image_filename` UDM field. If the `debuggable_app_image_filename` log field value is _not_ empty, then The `debuggable_app_image_filename` log field is mapped to the `security_result.detection_fields.debuggable_app_image_filename` UDM field. If the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `security_result.detection_fields.unexpected_files` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `sideloaded_app_image_filename` log field value is _not_ empty, then The `sideloaded_app_image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `duplicated_app_image_filename` log field value is _not_ empty, then The `duplicated_app_image_filename` log field is mapped to the `security_result.detection_fields.duplicated_app_image_filename` UDM field. If the `debuggable_app_image_filename` log field value is _not_ empty, then The `debuggable_app_image_filename` log field is mapped to the `security_result.detection_fields.debuggable_app_image_filename` UDM field. If the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `security_result.detection_fields.unexpected_files` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `duplicated_app_image_filename` log field value is _not_ empty, then The `duplicated_app_image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `debuggable_app_image_filename` log field value is _not_ empty, then The `debuggable_app_image_filename` log field is mapped to the `security_result.detection_fields.debuggable_app_image_filename` UDM field. If the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `security_result.detection_fields.unexpected_files` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `debuggable_app_image_filename` log field value is _not_ empty, then The `debuggable_app_image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `security_result.detection_fields.unexpected_files` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `unexpected_files.0` log field value is _not_ empty, then The `unexpected_files.0` log field is mapped to the `target.file.full_path` UDM field. If the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `security_result.detection_fields.app_image_filename` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `app_image_filename` log field value is _not_ empty, then The `app_image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_apps_image_filename` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `suspicious_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_apps.0.image_filename` log field is mapped to the `target.file.full_path` UDM field. If the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `security_result.detection_fields.suspicious_activities_apps_image_filename` UDM field.   
Otherwise if the `suspicious_activities_apps.0.image_filename` log field value is _not_ empty, then The `suspicious_activities_apps.0.image_filename` log field is mapped to the `target.file.full_path` UDM field.  
`app_label` | `target.application` | `security_result.detection_fields[app_label]`  
`correlation_rule_user_id` | `security_result.rule_author` | `security_result.rule_labels[correlation_rule_user_id]`  
`debuggable_app_label` | `target.application` | `security_result.detection_fields[debuggable_app_label]`  
`debuggable_certificate_thumbprints_sha1` | `target.file.sha1` | `security_result.detection_fields[debuggable_certificate_thumbprints_sha1]`  
`debuggable_certificate_thumbprints_sha256` | `target.file.sha256` | `security_result.detection_fields[debuggable_certificate_thumbprints_sha256]`  
`duplicated_app_label` | `target.application` | `security_result.detection_fields[duplicated_app_label]`  
`harmful_app_certificate_thumbprints_sha1` | `target.file.sha1` | `security_result.detection_fields[harmful_app_certificate_thumbprints_sha1]`  
`harmful_app_certificate_thumbprints_sha256` | `target.file.sha256` | `security_result.detection_fields[harmful_app_certificate_thumbprints_sha256]`  
`harmful_app_label` | `target.application` | `security_result.detection_fields[harmful_app_label]`  
`indicator_process_id` | `target.process.pid` | `security_result.detection_fields[indicator_process_id]`  
`intrusive_package.target_package_name` | `target.application`  
Iterate through log field `intrusive_package`  
if the `index` value is equal to `"0"`, then The `intrusive_package.target_package_name` log field is mapped to the `target.application` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"intrusive_package_target_package_name"` and The `intrusive_package.target_package_name` log field is mapped to the `security_result.detection_fields.value` UDM field. | `security_result.detection_fields[intrusive_package_target_package_name]`  
Iterate through log field `intrusive_package`  
if the `intrusive_package.target_package_name` log field value is _not_ empty, then The `intrusive_package.target_package_name` log field is mapped to the `security_result.detection_fields.intrusive_package_target_package_name` UDM field.  
`intrusive_process.target_process_name` | `target.process.file.names`  
Iterate through log field `intrusive_process`  
if the `index` value is equal to `"0"`, then The `intrusive_process.target_process_name` log field is mapped to the `target.process.file.names` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"intrusive_process_target_process_name"` and The `intrusive_process.target_process_name` log field is mapped to the `security_result.detection_fields.value` UDM field. | `security_result.detection_fields[intrusive_process_target_process_name]`  
Iterate through log field `intrusive_process`  
if the `intrusive_process.target_process_name` log field value is _not_ empty, then The `intrusive_process.target_process_name` log field is mapped to the `security_result.detection_fields.intrusive_process_target_process_name` UDM field.  
`intrusive_process.target_process_path` | `target.process.file.full_path`  
Iterate through log field `intrusive_process`  
if the `index` value is equal to `"0"`, then The `intrusive_process.target_process_path` log field is mapped to the `target.process.file.full_path` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"intrusive_process_target_process_path"` and The `intrusive_process.target_process_path` log field is mapped to the `security_result.detection_fields.value` UDM field. | `security_result.detection_fields[intrusive_process_target_process_path]`  
Iterate through log field `intrusive_process`  
if the `intrusive_process.target_process_path` log field value is _not_ empty, then The `intrusive_process.target_process_path` log field is mapped to the `security_result.detection_fields.intrusive_process_target_process_path` UDM field.  
`network_info.local_port` | `security_result.detection_fields[network_info_local_port]` | `principal.port, target.port`  
Iterate through log field `network_info`  
if the `index` value is equal to `"0"`, then If the `network_info.local_port` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.local_port` log field is mapped to the `target.port` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.local_port` log field is mapped to the `principal.port` UDM field. Otherwise, The `network_info.local_port` log field is mapped to the `security_result.detection_fields.network_info_local_port` UDM field.   
Otherwise, if the `network_info.local_port` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.local_port` log field is mapped to the `target.asset.attribute.labels.network_info_local_port` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.local_port` log field is mapped to the `principal.asset.attribute.labels.network_info_local_port` UDM field. Otherwise, The `network_info.local_port` log field is mapped to the `security_result.detection_fields.network_info_local_port` UDM field.  
`network_info.remote_address` | `security_result.detection_fields[network_info_remote_address]` | `principal.ip, target.ip`  
Iterate through log field `network_info`  
if the `network_info.remote_address` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.remote_address` log field is mapped to the `principal.ip` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.remote_address` log field is mapped to the `target.ip` UDM field. Otherwise, The `network_info.remote_address` log field is mapped to the `security_result.detection_fields.network_info_remote_address` UDM field.  
`network_info.remote_address` | `security_result.detection_fields[network_info_remote_address]` | `principal.asset.ip, target.asset.ip`  
Iterate through log field `network_info`  
if the `network_info.remote_address` log field value is _not_ empty, then If the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)inbound`, then The `network_info.remote_address` log field is mapped to the `principal.asset.ip` UDM field. Otherwise if the `network_info` log field valuethe `connection_direction` log field value matches the regular expression pattern: `(?i)outbound`, then The `network_info.remote_address` log field is mapped to the `target.asset.ip` UDM field. Otherwise, The `network_info.remote_address` log field is mapped to the `security_result.detection_fields.network_info_remote_address` UDM field.  
`sideloaded_app_certificate_thumbprints_sha1` | `target.file.sha1` | `security_result.detection_fields[sideloaded_app_certificate_thumbprints_sha1]`  
`sideloaded_app_certificate_thumbprints_sha256` | `target.file.sha256` | `security_result.detection_fields[sideloaded_app_certificate_thumbprints_sha256]`  
`sideloaded_app_label` | `target.application` | `security_result.detection_fields[sideloaded_app_label]`  
`suspicious_activities_apps.app_label` | `target.application`  
Iterate through log field `suspicious_activities_apps`  
if the `index` value is equal to `"0"`, then The `suspicious_activities_apps.app_label` log field is mapped to the `target.application` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"suspicious_activities_apps_app_label"` and The `suspicious_activities_apps.app_label` log field is mapped to the `security_result.detection_fields.value` UDM field. | `target.resource.attribute.labels[suspicious_activities_apps_app_label]`  
`suspicious_apps.app_label` | `target.application`  
Iterate through log field `suspicious_apps`  
if the `index` value is equal to `"0"`, then The `suspicious_apps.app_label` log field is mapped to the `target.application` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"suspicious_apps_app_label"` and The `suspicious_apps.app_label` log field is mapped to the `security_result.detection_fields.value` UDM field. | `target.resource.attribute.labels[suspicious_apps_app_label]`  
`suspicious_apps.certificate_thumbprints_sha1` | `target.file.sha1`  
Iterate through log field `suspicious_apps`  
if the `index` value is equal to `"0"`, then The `suspicious_apps.certificate_thumbprints_sha1` log field is mapped to the `target.file.sha1` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"suspicious_apps_certificate_thumbprints_sha1"` and The `suspicious_apps.certificate_thumbprints_sha1` log field is mapped to the `security_result.detection_fields.value` UDM field. | `security_result.detection_fields[suspicious_apps_certificate_thumbprints_sha1]`  
`suspicious_apps.certificate_thumbprints_sha256` | `target.file.sha256`  
Iterate through log field `suspicious_apps`  
if the `index` value is equal to `"0"`, then The `suspicious_apps.certificate_thumbprints_sha256` log field is mapped to the `target.file.sha256` UDM field.   
Otherwise, The `security_result.detection_fields.key` UDM field is set to `"suspicious_apps_certificate_thumbprints_sha256"` and The `suspicious_apps.certificate_thumbprints_sha256` log field is mapped to the `security_result.detection_fields.value` UDM field. | `security_result.detection_fields[suspicious_apps_certificate_thumbprints_sha256]`  
`system_partition_altered.volume_mount_point` | `target.resource.name`  
Iterate through log field `system_partition_altered`  
if the `index` value is equal to `"0"`, then The `system_partition_altered.volume_mount_point` log field is mapped to the `target.resource.name` UDM field.   
Otherwise, The `system_partition_altered.volume_mount_point` log field is mapped to the `target.resource_ancestors.name` UDM field. | `target.resource.attribute.labels[system_partition_altered_volume_mount_point]`  
`` | `target.resource.resource_type`  
Iterate through log field `system_partition_altered`  
if the `system_partition_altered.volume_mount_point` log field value is _not_ empty, then If the `index` value is equal to `"0"`, then The `target.resource.resource_type` UDM field is set to `"VOLUME"`. Otherwise, The `target.resource_ancestors.resource_type` UDM field is set to `"VOLUME"`. |   
`system_partition_altered.volume_type` | `target.resource.resource_subtype`  
Iterate through log field `system_partition_altered`  
if the `index` value is equal to `"0"`, then The `system_partition_altered.volume_type` log field is mapped to the `target.resource.resource_subtype` UDM field.   
Otherwise, The `system_partition_altered.volume_type` log field is mapped to the `target.resource_ancestors.resource_subtype` UDM field. | `target.resource.attribute.labels[system_partition_altered_volume_type]`  
`system_updates_blocked_by_dns.domain_name` | `network.dns.questions.name`  
Iterate through log field `system_updates_blocked_by_dns`   
The `system_updates_blocked_by_dns.domain_name` log field is mapped to the `network.dns.questions.name` UDM field. | `about.domain.name`  
Iterate through log field `system_updates_blocked_by_dns`   
The `system_updates_blocked_by_dns.domain_name` log field is mapped to the `about.domain.name` UDM field.  
`system_updates_blocked_by_filesystem.file_name` | `target.file.names`  
Iterate through log field `system_updates_blocked_by_filesystem`   
The `system_updates_blocked_by_filesystem.file_name` log field is mapped to the `target.file.names` UDM field. | `about.file.full_path`  
Iterate through log field `system_updates_blocked_by_filesystem`   
The `system_updates_blocked_by_filesystem.file_name` log field is mapped to the `about.file.full_path` UDM field.  
`system_updates_blocked_by_http.url` | `target.url`  
If the `url` log field value is empty, then  
Iterate through log field `system_updates_blocked_by_http`   
if the `index` value is equal to `"0"`, then The `system_updates_blocked_by_http.url` log field is mapped to the `target.url` UDM field. Otherwise, The `security_result.detection_fields.key` UDM field is set to `"system_updates_blocked_by_http_url"` and The `system_updates_blocked_by_http.url` log field is mapped to the `security_result.detection_fields.value` UDM field. | `about.url`  
Iterate through log field `system_updates_blocked_by_http`   
The `system_updates_blocked_by_http.url` log field is mapped to the `about.url` UDM field.   
`threatgraph_indicators.process_id` | `target.process.pid`  
Iterate through log field `threatgraph_indicators`  
if the `index` value is equal to `"0"`, then The `threatgraph_indicators.process_id` log field is mapped to the `target.process.pid` UDM field.   
Otherwise, if the `threatgraph_indicators.process_id` log field value is _not_ empty, then The `threatgraph_indicators.process_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicators_process_id` UDM field. | `security_result.detection_fields[threatgraph_indicators_process_id]`  
Iterate through log field `threatgraph_indicators`  
if the `threatgraph_indicators.process_id` log field value is _not_ empty, then The `threatgraph_indicators.process_id` log field is mapped to the `security_result.detection_fields.threatgraph_indicators_process_id` UDM field.  
`agent_id` | `principal.asset.attribute.labels[agent_id]`  
If the `device.device_id` log field value is _not_ empty or the `mdm_device_id` log field value is _not_ empty or the `host_id` log field value is _not_ empty, then If the `agent_id` log field value is _not_ empty, then The `agent_id` log field is mapped to the `principal.asset.attribute.labels.agent_id` UDM field. |   
`event_timestamp, timestamp` | `metadata.event_timestamp`  
If the `timestamp` log field value is _not_ empty, then The `timestamp` log field is mapped to the `metadata.event_timestamp` UDM field. | `metadata.event_timestamp`  
If the `event_timestamp` log field value is _not_ empty, then The `event_timestamp` log field is mapped to the `metadata.event_timestamp` UDM field.   
Otherwise if the `timestamp` log field value is _not_ empty, then The `timestamp` log field is mapped to the `metadata.event_timestamp` UDM field.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
