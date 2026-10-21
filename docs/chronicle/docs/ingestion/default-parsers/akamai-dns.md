---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns/
title: Collect Akamai DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:22:21.834687+00:00
---

# Collect Akamai DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai DNS logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Akamai DNS logs to Google Security Operations using Google Cloud Storage V2.

Akamai Edge DNS is an authoritative DNS service that provides fast, highly available, and secure DNS resolution. It leverages the Akamai Intelligent Edge Platform to deliver DNS responses from the closest point of presence, offering built-in DDoS protection and DNSSEC support. You can use Akamai DataStream 2 to stream Edge DNS query logs to a Google Cloud Storage bucket, which Google SecOps then ingests.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * An Akamai Control Center account with DataStream access
  * An Akamai contract that includes Edge DNS and DataStream 2
  * Edge DNS zones configured and active in your Akamai account



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `akamai-dns-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a GCS service account for DataStream 2

DataStream 2 requires a GCS service account with write permissions to deliver logs to your bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `akamai-datastream-sa`
     * **Service account description** : Enter `Service account for Akamai DataStream 2 to write Edge DNS logs to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following role: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Creator**.
  6. Click **Continue**.
  7. Click **Done**.



### Create and download a service account key

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click on the service account (`akamai-datastream-sa`).
  3. Go to the **Keys** tab.
  4. Click **Add Key > Create new key**.
  5. Select **JSON** as the key type.
  6. Click **Create**.
  7. Save the downloaded JSON key file securely. You will need the **service account name** and **private key** values when configuring DataStream 2.



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `akamai-dns-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `akamai-datastream-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Creator**
  6. Click **Save**.



## Configure DataStream 2 for Edge DNS

DataStream 2 replaces the legacy Log Delivery Service (LDS) for streaming Edge DNS logs. Use DataStream 2 to create a stream that collects Edge DNS query logs and delivers them to your GCS bucket.

**Note:** As of March 31, 2023, the Akamai Log Delivery Service (LDS) is no longer available for new purchases. Use DataStream 2 for all new Edge DNS log delivery configurations.

### Create an Edge DNS stream

  1. Sign in to [Akamai Control Center](https://control.akamai.com/).
  2. Go to **☰ > COMMON SERVICES > DataStream**.
  3. Click **Create stream**.
  4. Select **Edge DNS** from the drop-down list.
  5. In the **Configuration** tab, provide the following configuration details: 
     * **Display Name** : Enter a name for the stream (for example, `Edge DNS to GCS`)
     * **Group** : Select the relevant account control group
     * **Contract ID** : Verify the contract number associated with the group
  6. In **Select zones** , choose the Edge DNS zones you want the stream to collect log data for.
  7. Click **Next**.



### Choose data parameters

  1. On the **Data Sets** tab, select the data set fields you want to include in the stream. The following fields are available for Edge DNS:

Data Element | JSON Key | Description  
---|---|---  
Epoch timestamp | `timeStamp` | Unix epoch timestamp of the log entry  
Date | `date` | UTC date for the log entry  
Resolver IP | `requestIP` | IP address of the DNS resolver making the request  
Request port | `requestPort` | Port number of the DNS resolver  
Request name | `requestName` | Query name of the request  
Class | `dnsClass` | DNS class of the request  
Request type | `requestType` | DNS record type of the request  
EDNS0 flag | `edns0Flag` | EDNS0 Client Subnet (ECS) indicator  
EDNS0 size | `edns0Size` | ECS field size in bytes  
DNSSEC flag | `dnssecFlag` | DNSSEC indicator  
TCP flag | `tcpFlag` | TCP indicator  
Answers | `answers` | Request answers for a request query name  
Time | `time` | UTC time for the log entry  
  2. Click **Next**.




### Configure Google Cloud Storage destination

  1. On the **Destination** tab, select **Google Cloud Storage**.
  2. Provide the following configuration details:

     * **Display name** : Enter a name for the destination (for example, `GCS Edge DNS Logs`)
     * **Bucket** : Enter the name of the GCS bucket (for example, `akamai-dns-logs`)
     * **Project ID** : Enter your GCP project ID
     * **Path** (optional): Enter a folder path for log files (for example, `akamai-dns`)
     * **Service account name** : Enter the service account name from the JSON key file (`akamai-datastream-sa`)
     * **Private key** : Enter the `private_key` value from the JSON key file in PEM format with line break symbols
           
           -----BEGIN PRIVATE KEY-----\nprivate_key_content\n-----END PRIVATE KEY-----\n
           

  3. Click **Validate & Save** to test the connection to your GCS bucket.

**Note:** The validation process creates a verification file in your GCS bucket in the format `Akamai_access_verification_[TimeStamp].txt`. This file confirms successful connectivity.
  4. Optionally, in the **Delivery options** menu:

     * Edit the **Filename** field to change the prefix and suffix for log files
     * Change the **Push frequency** to receive bundled logs every 30 or 60 seconds
  5. Click **Next** to go to the **Summary** tab.




### Review and activate

  1. On the **Summary** tab, review the stream configuration.
  2. Click **Activate stream**.
  3. Wait for the stream status to change to **Active** (this may take a few minutes).



### Verify log delivery

  1. After the stream is active, wait for the configured push frequency interval (30 or 60 seconds).
  2. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  3. Go to **Cloud Storage > Buckets**.
  4. Click on your bucket name (for example, `akamai-dns-logs`).
  5. Navigate to the path folder (for example, `akamai-dns/`).
  6. Verify that new log files are being created.



If log files are not appearing:

  * Verify the stream status is **Active** in the DataStream dashboard
  * Check that the service account has **Storage Object Creator** permissions on the bucket
  * Verify the bucket name and project ID are correct in the stream configuration
  * Check for validation errors in the DataStream dashboard



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Akamai DNS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **AKAMAI_DNS** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://akamai-dns-logs/akamai-dns/
           

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
  2. Click on your bucket name (for example, `akamai-dns-logs`).
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
`timestamp` | `metadata.event_timestamp` | Parsed from the `timestamp` field in the raw log.  
`source_ip` | `principal.ip` | The value is taken from the `source_ip` field.  
`source_port` | `principal.port` | The value is taken from the `source_port` field and converted to an integer.  
`query` | `network.dns.questions.name` | The value is taken from the `query` field.  
`query_type` | `network.dns.questions.type` | The value is taken from the `query_type` field and mapped to DNS record type.  
`response_code` | `network.dns.response_code` | The value is taken from the `response_code` field.  
| `metadata.event_type` | Set to `NETWORK_DNS` if principal information is present; otherwise set to `GENERIC_EVENT`.  
| `metadata.product_name` | Set to `Akamai DNS`.  
| `metadata.vendor_name` | Set to `Akamai`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-dns-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
