---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf/
title: Collect Edgio WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:22.041259+00:00
---

# Collect Edgio WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Edgio WAF logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to ingest Edgio Web Application Firewall (WAF) logs to Google Security Operations using Google Cloud Storage. Edgio's Real-Time Log Delivery (RTLD) service can automatically deliver compressed WAF log data directly to a Cloud Storage bucket, which Google SecOps can then ingest for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to Google Cloud Platform.
  * Privileged access to Edgio Console.
  * An active Edgio property with WAF enabled.



## Configure a Google Cloud Storage bucket

  1. Sign in to the **Google Cloud console**.
  2. Go to **Cloud Storage > Buckets**.
  3. Click **Create**.
  4. Provide the following configuration details: 
     * **Name** : Enter a unique bucket name (for example, `edgio-waf-logs`).
     * **Location type** : Select **Region** or **Multi-region** based on your requirements.
     * **Location** : Select the location closest to your Edgio deployment.
     * **Storage class** : Select **Standard**.
     * **Access control** : Select **Uniform**.
     * **Encryption** : Select **Google-owned and Google-managed encryption key**.
  5. Click **Create**.



## Configure bucket permissions for Edgio

  1. In the **Google Cloud console** , go to your newly created bucket.
  2. Click **Permissions**.
  3. Click **Grant Access**.
  4. In the **New principals** field, add: `real-time-log-delivery@durable-firefly-334516.iam.gserviceaccount.com`
  5. In the **Select a role** list, select **Storage Object Creator**.
  6. Click **Save**.



## Configure Edgio Real-Time Log Delivery

  1. Sign in to the **Edgio Console**.
  2. Select your **private space** or **organization**.
  3. Select the required **property**.
  4. From the left pane, select the required **environment**.
  5. From the left pane, click **Realtime Log Delivery**.
  6. Click **\+ New Log Delivery Profile**.
  7. Select **WAF** as the log type.
  8. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps WAF Logs`).
     * **Destination** : Select **Google Cloud Storage**.
     * **Bucket** : Enter your GCS bucket name (for example, `edgio-waf-logs`).
     * **Prefix** : Optional. Enter a prefix for log organization (for example, `waf/`).
     * **Log Format** : Select **JSON** (default).
     * **Downsample the Logs** : Leave unchecked for full log delivery.
  9. In the **Fields** section, ensure all required fields are selected. Key fields include: 
     * account_number
     * action_type
     * client_city
     * client_country_code
     * client_ip
     * client_tls_ja3_md5
     * host
     * referer
     * rule_message
     * rule_tags
     * server_port
     * sub_events
     * sub_events_count
     * timestamp
     * URL
     * user_agent
     * uuid
     * waf_instance_name
     * waf_profile_name
     * waf_profile_type
  10. Click **Save**.



## Configure a feed in Google SecOps to ingest Edgio WAF logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add new**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Edgio WAF Logs`).
  4. Select **Google Cloud Storage V2** as the **Source type**.
  5. Select **Edgio WAF** as the **Log type**.
  6. Click **Get Service Account**.
  7. Copy the service account email displayed.
  8. Click **Next**.
  9. Specify values for the following input parameters: 
     * **Storage Bucket URI** : Enter your Cloud Storage bucket URI (format: `gs://edgio-waf-logs/waf/`).
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  10. Click **Next**.
  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Grant permissions to the Google SecOps service account

  1. Return to the **Google Cloud console**.
  2. Go to your Cloud Storage bucket.
  3. Click **Permissions**.
  4. Click **Grant Access**.
  5. In the **New principals** field, paste the service account email you copied from Google SecOps.
  6. In the **Select a role** list, select **Storage Object Viewer**.
  7. If you selected delete options in the feed configuration, also grant **Storage Object Admin**.
  8. Click **Save**.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/edgio-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
