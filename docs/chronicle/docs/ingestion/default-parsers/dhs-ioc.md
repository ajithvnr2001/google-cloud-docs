---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dhs-ioc/
title: Collect DHS IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:51.691025+00:00
---

# Collect DHS IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dhs-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect DHS IOC logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Department of Homeland Security (DHS) IOC logs to Google Security Operations using Google Cloud Storage V2.

DHS distributes threat intelligence through the Automated Indicator Sharing (AIS) program, providing indicators of compromise such as malicious IP addresses, domains, URLs, and file hashes in STIX/TAXII format. Because AIS delivers IOC data as downloadable STIX bundles, you must export those files to a Google Cloud Storage (GCS) bucket and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * An active DHS AIS participant account with access to the TAXII server or AIS portal
  * AIS client certificate and private key files for TAXII server authentication



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `dhs-ioc-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Configure an automated export of DHS IOC data to GCS

DHS distributes STIX-formatted IOC data through its AIS TAXII server. Configure an automated pipeline to pull indicators on a schedule and write them directly to GCS.

### Option 1: Cloud Scheduler with Cloud Build (recommended)

Use Cloud Build triggered by Cloud Scheduler to run a containerized job that fetches STIX bundles from the AIS TAXII server and writes them to GCS.

  1. Store the AIS client certificate and key in Secret Manager:

     1. In the **GCP Console** , go to **Security > Secret Manager**.
     2. Click **Create Secret**.
     3. Create two secrets: 
        * **Name** : `ais-client-cert`, **Value** : Contents of your AIS client certificate PEM file.
        * **Name** : `ais-client-key`, **Value** : Contents of your AIS client private key PEM file.
  2. Create a service account for the export job:

     1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
     2. Click **Create Service Account**.
     3. Provide the following configuration details: 
        * **Service account name** : Enter `dhs-ioc-export-sa`
        * **Service account description** : Enter `Service account for automated DHS IOC export to GCS`
     4. Click **Create and Continue**.
     5. Add the following roles: 
        * **Storage Object Admin** (to write files to GCS)
        * **Cloud Build Editor** (to run Cloud Build jobs)
        * **Secret Manager Secret Accessor** (to read AIS certificates)
     6. Click **Done**.
  3. Create a Cloud Build configuration file (`cloudbuild.yaml`):
         
         steps:
           - name: 'gcr.io/cloud-builders/gcloud'
             entrypoint: 'bash'
             args:
               - '-c'
               - |
                 apt-get update && apt-get install -y curl
                 # Retrieve AIS certificates from Secret Manager
                 gcloud secrets versions access latest --secret=ais-client-cert > /tmp/ais-cert.pem
                 gcloud secrets versions access latest --secret=ais-client-key > /tmp/ais-key.pem
                 # Fetch IOC data from AIS TAXII server
                 TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
                 FROM=$(date -u -d '-60 minutes' +"%Y-%m-%dT%H:%M:%SZ")
                 curl -s --cert /tmp/ais-cert.pem --key /tmp/ais-key.pem \
                   -H "Accept: application/taxii+json;version=2.1" \
                   "https://ais2.cisa.dhs.gov/taxii2/ais2/collections/${_COLLECTION_ID}/objects?added_after=$${FROM}" \
                   -o /workspace/dhs_ioc_$${TIMESTAMP}.json
                 # Upload to GCS
                 gcloud storage cp /workspace/dhs_ioc_$${TIMESTAMP}.json \
                   gs://${_BUCKET_NAME}/ioc-data/
                 # Clean up certificates
                 rm -f /tmp/ais-cert.pem /tmp/ais-key.pem
         substitutions:
           _BUCKET_NAME: 'dhs-ioc-logs'
           _COLLECTION_ID: 'YOUR_AIS_COLLECTION_ID'
         

**Note:** Replace `YOUR_AIS_COLLECTION_ID` with your AIS collection ID.
  4. Create a Cloud Scheduler job to trigger the build:

     1. In the **GCP Console** , go to **Cloud Scheduler**.
     2. Click **Create Job**.
     3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `dhs-ioc-export-hourly`  
**Region** | Select the same region as your GCS bucket  
**Frequency** | `0 * * * *` (every hour)  
**Timezone** | UTC (recommended)  
**Target type** | HTTP  
**URL** | `https://cloudbuild.googleapis.com/v1/projects/YOUR_PROJECT_ID/builds`  
**HTTP method** | POST  
**Auth header** | Add OAuth token  
**Service account** | `dhs-ioc-export-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com`  
     4. Click **Create**.




### Option 2: Compute Engine VM with cron (alternative)

If Cloud Build is not available, use a small Compute Engine VM with a cron job to pull IOC data and write to GCS.

  1. Create a Compute Engine VM:

     1. In the **GCP Console** , go to **Compute Engine > VM instances**.
     2. Click **Create instance**.
     3. Select a small machine type (for example, `e2-micro`).
     4. Under **Identity and API access** , select a service account with **Storage Object Admin** role.
     5. Click **Create**.
  2. SSH into the VM and create an export script (`/opt/dhs-ioc/export.sh`):
         
         #!/usr/bin/env bash
         set -euo pipefail
         
         TAXII_URL="https://ais2.cisa.dhs.gov/taxii2"
         API_ROOT="ais2"
         COLLECTION_ID="YOUR_AIS_COLLECTION_ID"
         CERT="/etc/ais/client-cert.pem"
         KEY="/etc/ais/client-key.pem"
         BUCKET="dhs-ioc-logs"
         
         TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
         FROM=$(date -u -d '-60 minutes' +"%Y-%m-%dT%H:%M:%SZ")
         
         curl -s --cert "$CERT" --key "$KEY" \
           -H "Accept: application/taxii+json;version=2.1" \
           "${TAXII_URL}/${API_ROOT}/collections/${COLLECTION_ID}/objects?added_after=${FROM}" \
           -o "/tmp/dhs_ioc_${TIMESTAMP}.json"
         
         gcloud storage cp "/tmp/dhs_ioc_${TIMESTAMP}.json" "gs://${BUCKET}/ioc-data/"
         rm -f "/tmp/dhs_ioc_${TIMESTAMP}.json"
         

**Note:** Replace `YOUR_AIS_COLLECTION_ID` with your AIS collection ID. Copy the AIS client certificate and key to `/etc/ais/` on the VM.
  3. Make the script executable and schedule it with cron:
         
         chmod +x /opt/dhs-ioc/export.sh
         (crontab -l ; echo "0 * * * * /opt/dhs-ioc/export.sh >> /var/log/dhs-ioc-export.log 2>&1") | crontab -
         




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `DHS IOC Feed`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Department of Homeland Security** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `dhs-ioc-logs`).
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
  4. In the **Feed name** field, enter a name for the feed (for example, `DHS IOC Feed`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Department of Homeland Security** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://dhs-ioc-logs/ioc-data/
           

       * Replace `dhs-ioc-logs` with your GCS bucket name.
       * Replace `ioc-data` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
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
| entity.application | Application name or identifier  
observable_id | entity.asset.asset_id | Asset identifier  
object_id | entity.asset.product_object_id | Product object identifier  
hash_value | entity.file.md5 | MD5 hash of the file  
hash_value | entity.file.sha1 | SHA1 hash of the file  
hash_value | entity.file.sha256 | SHA256 hash of the file  
file_size | entity.file.size | Size of the file in bytes  
fuzzy_hash_value | entity.file.ssdeep | SSDEEP hash of the file  
file_path | entity.file.full_path | Full file path  
ip_address_value | entity.ip | IP address  
country | entity.location.country_or_region | Country or region  
administrativeArea | entity.location.state | State or province  
port | entity.port | Port number  
file_name_label | entity.resource.attribute.labels | Attribute labels for the resource  
url | entity.url | URL  
organisationInfo | entity.user.department | Department  
email_address, email | entity.user.email_addresses | Email addresses  
organisationName | entity.user.userid | User ID  
| ioc.domain_and_ports.domain | Domain name  
indicator_type, confidence_value | ioc.feed_name | Feed name  
ip_address_value, target_ip | ioc.ip_and_ports.ip_address | IP address  
port | ioc.ip_and_ports.ports | Ports  
description, desc1, ttp_description | metadata.description | Description  
entity_type | metadata.entity_type | Type of entity  
start_time | metadata.interval.start_time | Start time of the interval  
object_id | metadata.product_entity_id | Product entity identifier  
sightings_count_label | metadata.source_labels | Source labels  
security_result_data, ttp_security_result | metadata.threat | Threat information  
| metadata.vendor_name | Vendor or company name  
| metadata.product_name | Product name  
address_label, subject_label, file_label | security_result.about.labels | Labels about the security result  
indicator_type | security_result_data.category_details | Category details  
desc1 | security_result_data.description | Description  
confidence_value | security_result_data.severity | Severity level  
host, domain_name | target.hostname | Target hostname  
target_ip | target.ip | Target IP address  
domain_name | target.url | Target URL  
malware_category | ttp_security_result.category_details | Category details for TTP  
ttp_id_label | ttp_security_result.detection_fields | Detection fields for TTP  
ttp_description | ttp_security_result.description | Description for TTP  
ttp_summary | ttp_security_result.summary | Summary for TTP  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dhs-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
