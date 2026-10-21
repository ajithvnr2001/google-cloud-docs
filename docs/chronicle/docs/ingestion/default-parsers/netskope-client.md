---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-client/
title: Collect Netskope Client logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:43:54.068039+00:00
---

# Collect Netskope Client logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netskope Client logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Netskope Client logs into Google Security Operations using Google Cloud Storage V2. Netskope Client is a SASE/SSE endpoint agent that generates telemetry covering device posture, steering decisions, tunnel status, and client-side security events.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets and IAM policies
  * Privileged access to the Netskope tenant admin console



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netskope-client-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Export Netskope Client logs to Google Cloud Storage

Netskope supports exporting log data to cloud storage via the Cloud Log Shipping (CLS) feature in the Netskope admin console.

  1. Sign in to the **Netskope** tenant admin console.
  2. Navigate to the **Cloud Log Shipping** configuration. Depending on your Netskope version, this may be under **Settings > Tools > Cloud Log Shipping** in the admin console, or configured through the **Netskope Cloud Exchange** platform.
  3. Click **New Cloud Log Shipping Configuration** (or edit an existing one).
  4. Select **Google Cloud Storage** as the destination.
  5. Provide the following configuration details: 
     * **Bucket name** : Enter the bucket name (for example, `netskope-client-logs`)
     * **Path prefix** : Enter a folder prefix (for example, `netskope-client/`)
     * **Service account credentials** : Upload or paste the GCP service account JSON key with write access to the bucket
  6. Select the log types to export: 
     * Client events (steering, tunnel, posture)
  7. Set the export interval and format (JSON recommended for Chronicle ingestion).
  8. Click **Save**.
  9. Verify that log files begin appearing in the GCS bucket under the specified prefix.

     * Ensure that the GCP service account used for the export has the **Storage Object Creator** role on the target bucket.
     * Log files are written in JSON format, with each file containing one or more event records.



## Retrieve the Google SecOps service account

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Feeds**.
  3. Click **Add New Feed**.
  4. Click **Configure a single feed**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Netskope Client** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

     * Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

     * If you plan to use the deletion option (delete transferred files), grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest Netskope Client logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Netskope Client logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Netskope Client** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

Field | Value  
---|---  
**Storage bucket URI** | `gs://netskope-client-logs/netskope-client/`  
**Source Deletion Option** | Select the deletion option according to your preference  
**Maximum File Age (Days)** | Default is 180 days  
**Asset namespace** | The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)  
**Ingestion labels** | The label to be applied to the events from this feed  
     * Replace `netskope-client-logs` with your actual GCS bucket name.
     * Always include the trailing slash (`/`) at the end of the URI.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM field mapping reference

Log Field | UDM Mapping | Logic  
---|---|---  
timestamp | metadata.event_timestamp | Timestamp when the event occurred  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
clientBytes | network.sent_bytes | Number of bytes sent by the client  
serverBytes | network.received_bytes | Number of bytes received by the server  
clientPackets | network.sent_packets | Number of packets sent by the client  
sessionDuration | network.session_duration.seconds | Duration of the network session in seconds  
networkSessionId | network.session_id | Unique identifier for the network session  
proto | network.application_protocol | Application protocol used in the network connection  
os | principal.platform | Platform of the principal device  
osVersion | principal.platform_version | Version of the platform  
requestClientApplication | principal.application | Application associated with the principal  
suser | principal.user.userid | User ID of the principal  
sourceServiceName, shost | principal.hostname | Hostname of the principal  
shost | principal.asset.hostname | Hostname of the principal's asset  
sourceServiceName | principal.ip | IP address of the principal  
spt | principal.port | Port number used by the principal  
action | security_result.action | Action taken by the security system  
ccl | security_result.confidence_details | Confidence level or details of the security result  
cci, policy, proto, requestMethod, trafficType, tunnelId, tunnelType, tunnelUpTime, start, end | security_result.detection_fields | Additional detection fields from the security result  
dst | target.ip | IP address of the target  
dpt | target.port | Port number of the target  
| metadata.product_name | Product name of the security vendor  
| metadata.vendor_name | Vendor/company name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-client-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
