---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc/
title: Collect CSV Custom IOC files \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:49.678138+00:00
---

# Collect CSV Custom IOC files  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/csv-custom-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CSV Custom IOC files

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CSV Custom IOC files to Google Security Operations using Google Cloud Storage, it then maps these fields to the UDM, handling various data types like IPs, domains, and hashes, and enriching the output with threat details, entity information, and severity levels.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Access to one or more CSV IOC feed URLs (HTTPS) or an internal endpoint that serves CSV



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `csv-ioc-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `csv-ioc-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect CSV IOC files`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
     3. Click **\+ Add another role**.
     4. Search for and select **Cloud Run Invoker**.
     5. Click **\+ Add another role**.
     6. Search for and select **Cloud Functions Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



These roles are required for:

  * **Storage Object Admin** : Write logs to GCS bucket
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `csv-ioc-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `csv-ioc-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect CSV IOC files

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch CSV IOC files from HTTPS endpoints and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `csv-ioc-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`csv-ioc-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`csv-ioc-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `csv-ioc-logs` | GCS bucket name  
`GCS_PREFIX` | `csv-ioc` | Prefix for log files  
`IOC_URLS` | `https://ioc.example.com/feed.csv,https://another.example.org/iocs.csv` | Comma-separated HTTPS URLs  
`AUTH_HEADER` | `Authorization: Bearer <token>` | Optional authentication header  
`TIMEOUT` | `60` | Request timeout in seconds  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone
    import time
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch CSV IOC feeds over HTTPS and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'csv-ioc').strip('/')
        ioc_urls_str = os.environ.get('IOC_URLS', '')
        auth_header = os.environ.get('AUTH_HEADER', '')
        timeout = int(os.environ.get('TIMEOUT', '60'))
    
        ioc_urls = [u.strip() for u in ioc_urls_str.split(',') if u.strip()]
    
        if not bucket_name:
            print('Error: GCS_BUCKET environment variable is required')
            return
    
        if not ioc_urls:
            print('Error: IOC_URLS must contain at least one HTTPS URL')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            run_ts = int(time.time())
            written = []
    
            for i, url in enumerate(ioc_urls):
                print(f'Processing URL {i+1}/{len(ioc_urls)}: {url}')
    
                # Build request
                req_headers = {'Accept': 'text/csv, */*'}
    
                # Add authentication header if provided
                if auth_header:
                    if ':' in auth_header:
                        k, v = auth_header.split(':', 1)
                        req_headers[k.strip()] = v.strip()
                    else:
                        req_headers['Authorization'] = auth_header.strip()
    
                # Fetch data with retries
                data = fetch_with_retries(url, req_headers, timeout)
    
                if data:
                    # Write to GCS
                    key = generate_blob_name(prefix, url, run_ts, i)
                    blob = bucket.blob(key)
                    blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(data, content_type='text/csv')
    
                    written.append({
                        'url': url,
                        'gcs_key': key,
                        'bytes': len(data)
                    })
    
                    print(f'Wrote {len(data)} bytes to gs://{bucket_name}/{key}')
                else:
                    print(f'Warning: No data retrieved from {url}')
    
            print(f'Successfully processed {len(written)} URLs')
            print(json.dumps({'ok': True, 'written': written}, indent=2))
    
        except Exception as e:
            print(f'Error processing CSV IOC feeds: {str(e)}')
            raise
    
    def fetch_with_retries(url, headers, timeout, max_retries=5):
        """Fetch data from URL with retry logic for 429/5xx errors."""
        if not url.lower().startswith('https://'):
            raise ValueError('Only HTTPS URLs are allowed in IOC_URLS')
    
        attempt = 0
        backoff = 1.0
    
        while attempt < max_retries:
            try:
                response = http.request('GET', url, headers=headers, timeout=timeout)
    
                if response.status == 200:
                    return response.data.decode('utf-8')
                elif response.status == 429 or (500 <= response.status < 600):
                    print(f'Received status {response.status}, retrying in {backoff}s (attempt {attempt+1}/{max_retries})')
                    time.sleep(backoff)
                    attempt += 1
                    backoff *= 2
                else:
                    print(f'Error: Received unexpected status {response.status} from {url}')
                    return None
    
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f'Request failed: {str(e)}, retrying in {backoff}s (attempt {attempt+1}/{max_retries})')
                    time.sleep(backoff)
                    attempt += 1
                    backoff *= 2
                else:
                    raise
    
        print(f'Max retries exceeded for {url}')
        return None
    
    def generate_blob_name(prefix, url, run_ts, idx):
        """Generate a unique blob name for the CSV file."""
        # Create a short, filesystem-safe token for the URL
        safe_url = url.replace('://', '_').replace('/', '_').replace('?', '_').replace('&', '_')[:100]
    
        # Generate timestamp-based path
        timestamp_path = time.strftime('%Y/%m/%d/%H%M%S', time.gmtime(run_ts))
    
        return f"{prefix}/{timestamp_path}-url{idx:03d}-{safe_url}.csv"
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `csv-ioc-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`csv-ioc-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  



### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`csv-ioc-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (`csv-ioc-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Processing URL 1/X: https://...
         Wrote X bytes to gs://csv-ioc-logs/csv-ioc/YYYY/MM/DD/HHMMSS-url000-...csv
         Successfully processed X URLs
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`csv-ioc-logs`).

  10. Navigate to the prefix folder (`csv-ioc/`).

  11. Verify that new `.csv` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401/403** : Check AUTH_HEADER environment variable
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set
  * **Only HTTPS URLs are allowed** : Verify IOC_URLS contains only HTTPS URLs



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CSV Custom IOC`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CSV Custom IOC** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`csv-ioc-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest CSV Custom IOC files

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CSV Custom IOC`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CSV Custom IOC** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://csv-ioc-logs/csv-ioc/
           

       * Replace:

         * `csv-ioc-logs`: Your GCS bucket name.
         * `csv-ioc`: Optional prefix/folder path where logs are stored.
       * **Examples:**

         * Root bucket: `gs://csv-ioc-logs/`
         * With prefix: `gs://csv-ioc-logs/csv-ioc/`
         * With subfolder: `gs://csv-ioc-logs/ioc-feeds/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
asn | entity.metadata.threat.detection_fields.asn_label.value | Directly mapped from the "asn" field.  
category | entity.metadata.threat.category_details | Directly mapped from the "category" field.  
classification | entity.metadata.threat.category_details | Appended to "classification - " and mapped to the "entity.metadata.threat.category_details" field.  
column2 | entity.entity.hostname | Mapped to "entity.entity.hostname" if [category] matches ". ?ip" or ". ?proxy" and [not_ip] is true.  
column2 | entity.entity.ip | Merged into "entity.entity.ip" if [category] matches ". ?ip" or ". ?proxy" and [not_ip] is false.  
confidence | entity.metadata.threat.confidence_score | Converted to float and mapped to the "entity.metadata.threat.confidence_score" field.  
country | entity.entity.location.country_or_region | Directly mapped from the "country" field.  
date_first | entity.metadata.threat.first_discovered_time | Parsed as ISO8601 and mapped to the "entity.metadata.threat.first_discovered_time" field.  
date_last | entity.metadata.threat.last_updated_time | Parsed as ISO8601 and mapped to the "entity.metadata.threat.last_updated_time" field.  
detail | entity.metadata.threat.summary | Directly mapped from the "detail" field.  
detail2 | entity.metadata.threat.description | Directly mapped from the "detail2" field.  
domain | entity.entity.hostname | Directly mapped from the "domain" field.  
email | entity.entity.user.email_addresses | Merged into the "entity.entity.user.email_addresses" field.  
id | entity.metadata.product_entity_id | Appended to "id - " and mapped to the "entity.metadata.product_entity_id" field.  
import_session_id | entity.metadata.threat.detection_fields.import_session_id_label.value | Directly mapped from the "import_session_id" field.  
itype | entity.metadata.threat.detection_fields.itype_label.value | Directly mapped from the "itype" field.  
lat | entity.entity.location.region_latitude | Converted to float and mapped to the "entity.entity.location.region_latitude" field.  
lon | entity.entity.location.region_longitude | Converted to float and mapped to the "entity.entity.location.region_longitude" field.  
maltype | entity.metadata.threat.detection_fields.maltype_label.value | Directly mapped from the "maltype" field.  
md5 | entity.entity.file.md5 | Directly mapped from the "md5" field.  
media | entity.metadata.threat.detection_fields.media_label.value | Directly mapped from the "media" field.  
media_type | entity.metadata.threat.detection_fields.media_type_label.value | Directly mapped from the "media_type" field.  
org | entity.metadata.threat.detection_fields.org_label.value | Directly mapped from the "org" field.  
resource_uri | entity.entity.url | Mapped to "entity.entity.url" if [itype] does not match "(ip  
resource_uri | entity.metadata.threat.url_back_to_product | Mapped to "entity.metadata.threat.url_back_to_product" if [itype] matches "(ip  
score | entity.metadata.threat.confidence_details | Directly mapped from the "score" field.  
severity | entity.metadata.threat.severity | Converted to uppercase and mapped to the "entity.metadata.threat.severity" field if it matches "LOW", "MEDIUM", "HIGH", or "CRITICAL".  
source | entity.metadata.threat.detection_fields.source_label.value | Directly mapped from the "source" field.  
source_feed_id | entity.metadata.threat.detection_fields.source_feed_id_label.value | Directly mapped from the "source_feed_id" field.  
srcip | entity.entity.ip | Merged into "entity.entity.ip" if [srcip] is not empty and not equal to [value].  
state | entity.metadata.threat.detection_fields.state_label.value | Directly mapped from the "state" field.  
trusted_circle_ids | entity.metadata.threat.detection_fields.trusted_circle_ids_label.value | Directly mapped from the "trusted_circle_ids" field.  
update_id | entity.metadata.threat.detection_fields.update_id_label.value | Directly mapped from the "update_id" field.  
value | entity.entity.file.full_path | Mapped to "entity.entity.file.full_path" if [category] matches ".*?file".  
value | entity.entity.file.md5 | Mapped to "entity.entity.file.md5" if [category] matches ".*?md5" and [value] is a 32-character hexadecimal string.  
value | entity.entity.file.sha1 | Mapped to "entity.entity.file.sha1" if ([category] matches ". ?md5" and [value] is a 40-character hexadecimal string) or ([category] matches ". ?sha1" and [value] is a 40-character hexadecimal string).  
value | entity.entity.file.sha256 | Mapped to "entity.entity.file.sha256" if ([category] matches ". ?md5" and [value] is a hexadecimal string and [file_type] is not "md5") or ([category] matches ". ?sha256" and [value] is a hexadecimal string).  
value | entity.entity.hostname | Mapped to "entity.entity.hostname" if ([category] matches ". ?domain") or ([category] matches ". ?ip" or ".*?proxy" and [not_ip] is true).  
value | entity.entity.url | Mapped to "entity.entity.url" if ([category] matches ".*?url") or ([category] matches "url" and [resource_uri] is not empty).  
N/A | entity.metadata.collected_timestamp | Populated with the event timestamp.  
N/A | entity.metadata.interval.end_time | Set to a constant value of 253402300799 seconds.  
N/A | entity.metadata.interval.start_time | Populated with the event timestamp.  
N/A | entity.metadata.vendor_name | Set to a constant value of "Custom IOC".  
`asn", "import_session_id", "itype", "maltype", "media", "media_type", "org", "source", "source_feed_id", "state", "trusted_circle_ids" and "update_id` | `threat.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/csv-custom-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
