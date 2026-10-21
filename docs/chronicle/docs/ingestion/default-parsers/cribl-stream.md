---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream/
title: Collect Cribl Stream logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:18:16.616881+00:00
---

# Collect Cribl Stream logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cribl Stream logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cribl Stream logs to Google Security Operations using the built-in Google SecOps destination. Cribl Stream produces operational data in the form of logs, metrics, and events. This integration lets you send these logs to Google SecOps for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Access to Cribl Stream management console or cluster.
  * Google Cloud service account credentials.



## Get Google SecOps credentials

To authenticate Cribl Stream to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `cribl-stream-ingest`).
     * **Service account description** : Enter a description (for example, `Cribl Stream log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file securely for use in the Cribl Stream destination configuration.

**Note:** The JSON key is a credential. Restrict access to the file and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely for use in the Cribl Stream destination configuration.

**Note:** This file authenticates to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Configure Google SecOps destination in Cribl Stream

  1. Sign in to the **Cribl Stream Management Console**.
  2. Go to **Data > Destinations**.
  3. Click **Add Destination**.
  4. Select **Google Cloud > Security Operations (SecOps)**.
  5. Provide the following configuration details: 
     * **Output ID** : Enter a unique name (for example, `google-secops-destination`).
     * **Description** : Enter a description for this destination.
     * **Send events as** : Select **Unstructured** (recommended for standard log parsing).
     * **API version** : Select **V2**.
     * **Default log type** : Select **CRIBL_STREAM** from the list.
     * Optional: **Namespace** : Enter a namespace to identify logs from this source (for example, `cribl-logs`).
  6. In the **Authentication** section: 
     * **Authentication method** : Service account (JSON).
     * **Service account key** : Upload or paste the JSON credentials file content.
  7. In the **Processing** section: 
     * **Log text field** : Optionally enter `_raw`. If not set, Cribl will send JSON representation of the entire event; use `_raw` only if you actually store raw text in this field.
  8. Click **Save**.



## Create a route to send Cribl Stream logs

  1. Go to **Data > Routes**.
  2. Click **Add Route**.
  3. Provide the following configuration details: 
     * **Route name** : Enter a meaningful name (for example, `cribl-logs-to-secops`).
     * **Filter** : Enter `source.match(/cribl.*/)` to capture Cribl internal logs (operational logs from Cribl itself).
     * **Output** : Select the Google SecOps destination created in the previous section.
     * **Pipeline** : Select **passthru** or create a custom pipeline for log enrichment.
  4. Click **Save**.
  5. **Commit & Deploy** the configuration to apply changes.



## Configure log filtering and enrichment (Optional)

If you need to filter or enrich Cribl Stream logs before sending to Google SecOps:

  1. Go to **Data > Pipelines** in Cribl Stream.
  2. Click **Add Pipeline**.
  3. Provide the following configuration details: 
     * **Pipeline ID** : Enter a meaningful name (for example, `cribl-log-processing`).
     * **Description** : Enter a description for the pipeline.
  4. Add functions as needed: 
     * **Eval** : Add metadata fields or modify existing fields.
     * **Regex Extract** : Extract specific information from log messages.
     * **Drop** : Remove unnecessary events or fields.
     * **Mask** : Redact sensitive information.
  5. Click **Save**.
  6. Update your route to use this pipeline instead of **passthru**.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cribl-stream-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
