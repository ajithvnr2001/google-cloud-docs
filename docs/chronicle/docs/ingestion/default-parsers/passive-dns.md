---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/passive-dns/
title: Collect Passive DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:47:50.411741+00:00
---

# Collect Passive DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/passive-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Passive DNS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Passive DNS logs to Google Security Operations using Google Cloud Storage V2.

Passive DNS is a DNS intelligence data source that captures historical DNS resolution records for threat analysis and domain investigation. Because the data is typically collected and stored as files, you must upload those files to a Google Cloud Storage (GCS) bucket, and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Google Cloud project with Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets.
  * Permissions to manage IAM policies on GCS buckets.
  * Access to Passive DNS data files (for example, DNSDB, Farsight, or another Passive DNS provider).
  * Passive DNS data exported in a supported format (for example, JSON or CSV).



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `passive-dns-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Configure automated export of Passive DNS data to GCS

Passive DNS data is typically available as exported files from a DNS intelligence provider (for example, Farsight DNSDB, DomainTools, or Cisco Umbrella Investigate). To keep the data in GCS current, configure an automated export pipeline using one of the following approaches.

### Option 1: Cloud Scheduler with Cloud Build (recommended)

Use Cloud Build triggered by Cloud Scheduler to run a containerized job that fetches Passive DNS data from your provider and writes it to GCS.

  1. Create a service account for the export job:

     1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
     2. Click **Create Service Account**.
     3. Provide the following configuration details: 
        * **Service account name** : Enter `passive-dns-export-sa`
        * **Service account description** : Enter `Service account for automated Passive DNS data export to GCS`
     4. Click **Create and Continue**.
     5. Add the following roles: 
        * **Storage Object Admin** (to write files to GCS)
        * **Cloud Build Editor** (to run Cloud Build jobs)
     6. Click **Done**.
  2. Create a Cloud Build configuration file (`cloudbuild.yaml`):
         
         steps:
           - name: 'gcr.io/cloud-builders/gcloud'
             entrypoint: 'bash'
             args:
               - '-c'
               - |
                 apt-get update && apt-get install -y curl jq
                 # Fetch Passive DNS data from your provider
                 # Replace with the actual API call for your provider
                 # Example for Farsight DNSDB:
                 TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
                 curl -s -H "X-API-Key: $${PDNS_API_KEY}" \
                   "https://api.dnsdb.info/dnsdb/v2/lookup/rrset/name/*.example.com" \
                   -o /workspace/passive_dns_$${TIMESTAMP}.json
                 # Upload to GCS
                 gcloud storage cp /workspace/passive_dns_$${TIMESTAMP}.json \
                   gs://${_BUCKET_NAME}/passive-dns/
         substitutions:
           _BUCKET_NAME: 'passive-dns-logs'
         

**Note:** Replace the `curl` command with the actual API call for your Passive DNS provider. Consult your provider documentation for the correct endpoint, authentication method, and query parameters.
  3. Store the API key as a Secret Manager secret:

     1. In the **GCP Console** , go to **Security > Secret Manager**.
     2. Click **Create Secret**.
     3. Enter `pdns-api-key` as the secret name.
     4. Enter your Passive DNS provider API key as the secret value.
     5. Click **Create**.
  4. Create a Cloud Scheduler job to trigger the build:

     1. In the **GCP Console** , go to **Cloud Scheduler**.
     2. Click **Create Job**.
     3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `passive-dns-export-daily`  
**Region** | Select the same region as your GCS bucket  
**Frequency** | `0 3 * * *` (daily at 3:00 AM UTC)  
**Timezone** | UTC (recommended)  
**Target type** | HTTP  
**URL** | `https://cloudbuild.googleapis.com/v1/projects/YOUR_PROJECT_ID/builds`  
**HTTP method** | POST  
**Auth header** | Add OAuth token  
**Service account** | `passive-dns-export-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com`  
     4. Click **Create**.




### Option 2: Storage Transfer Service (for on-premise data stores)

If Passive DNS data is stored on an on-premise file system, use Storage Transfer Service with a Transfer Agent.

  1. In the **GCP Console** , go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **POSIX filesystem** as the source.
  4. Follow the instructions to install the [Storage Transfer Agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) on a machine with access to the Passive DNS data files.
  5. Configure the transfer job:

Setting | Value  
---|---  
**Source directory** | Path to the directory containing Passive DNS data files  
**Destination bucket** | `passive-dns-logs`  
**Destination path** | `passive-dns/`  
**Schedule** | Set a recurring schedule (for example, daily)  
  6. Click **Create**.




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Passive DNS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Passive DNS** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `passive-dns-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure the Google SecOps feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Passive DNS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Passive DNS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://passive-dns-logs/passive-dns/
           

       * Replace `passive-dns-logs` with your GCS bucket name.
       * Replace `passive-dns` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
hostname | intermediary.hostname | Value copied directly  
timestamp_s | metadata.event_timestamp | Parsed as UNIX timestamp  
| metadata.event_type | Set to "NETWORK_DNS"  
| network.application_protocol | Set to "DNS"  
answer | network.dns.answers.data | Value from answer after removing trailing dot  
ttl | network.dns.answers.ttl | Converted to integer  
class | network.dns.questions.class | Mapped to numeric value (1 for IN, 3 for CH, 4 for HS)  
query | network.dns.questions.name | Value from query after removing trailing dot  
type | network.dns.questions.type | Mapped from type (uppercased) to numeric value using DNS type mapping  
client | principal.ip | Value copied directly  
server | target.ip | Value copied directly  
| metadata.product_name | Set to "Passive DNS"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
