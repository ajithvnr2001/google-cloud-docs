---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it/
title: Collect Snipe-IT logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:13:50.321495+00:00
---

# Collect Snipe-IT logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snipe-it/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Snipe-IT logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Snipe-IT logs to Google Security Operations using Google Cloud Storage. Snipe-IT is an open-source IT asset management system that tracks hardware, software licenses, accessories, consumables, and other IT assets throughout their lifecycle.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Snipe-IT tenant



## Collect Snipe-IT prerequisites (API token and base URL)

  1. Sign in to Snipe-IT.
  2. Open your user menu (top-right avatar) and click **Manage API keys**.
  3. Click **Create New Token** : 
     * **Name/Label** : Enter a descriptive label (for example, `Google SecOps export`).
  4. Click **Generate**.
  5. Copy the API token (it will be shown only once). Store it securely.
  6. Determine your API base URL, typically: `https://<your-domain>/api/v1`
     * Example: `https://snipeit.example.com/api/v1`



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `snipe-it-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `snipeit-assets-to-gcs-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Snipe-IT logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
     3. Click **\+ Add another role**.
     4. Search for and select **Cloud Run Invoker**.
     5. Click **\+ Add another role**.
     6. Search for and select **Cloud Functions Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



These roles are required for:

  * **Storage Object Admin** : Write logs to GCS bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



#### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `snipeit-assets-to-gcs-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `snipeit-assets-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch hardware assets from Snipe-IT API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `snipeit-assets-to-gcs`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic (`snipeit-assets-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`snipeit-assets-to-gcs-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `snipe-it-logs`  
`GCS_PREFIX` | `snipeit/assets`  
`SNIPE_BASE_URL` | `https://snipeit.example.com/api/v1`  
`SNIPE_API_TOKEN` | `your-api-token`  
`PAGE_SIZE` | `500`  
`MAX_PAGES` | `200`  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** opens automatically.




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
               import urllib.parse
           
               # Initialize HTTP client
               http = urllib3.PoolManager()
           
               # Initialize Storage client
               storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
               @functions_framework.cloud_event
               def main(cloud_event):
                   """
                   Cloud Run function triggered by Pub/Sub to fetch hardware assets from Snipe-IT API and write to GCS.
           
                   Args:
                       cloud_event: CloudEvent object containing Pub/Sub message
                   """
           
                   # Get environment variables
                   bucket_name = os.environ.get('GCS_BUCKET')
                   prefix = os.environ.get('GCS_PREFIX', 'snipeit/assets')
                   base_url = os.environ.get('SNIPE_BASE_URL', '').rstrip('/')
                   token = os.environ.get('SNIPE_API_TOKEN')
                   page_size = int(os.environ.get('PAGE_SIZE', '500'))
                   max_pages = int(os.environ.get('MAX_PAGES', '200'))
           
                   if not all([bucket_name, base_url, token]):
                       print('Error: Missing required environment variables')
                       return
           
                   try:
                       # Get GCS bucket
                       bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
           
                       # Fetch and write pages
                       ts = datetime.now(timezone.utc)
                       offset = 0
                       page = 0
                       total = 0
           
                       headers = {
                           'Authorization': f'Bearer {token}',
                           'Accept': 'application/json',
                           'Content-Type': 'application/json'
                       }
           
                       while page < max_pages:
                           # Fetch page from Snipe-IT API
                           params = {
                               'limit': page_size,
                               'offset': offset,
                               'sort': 'id',
                               'order': 'asc'
                           }
                           qs = urllib.parse.urlencode(params)
                           url = f"{base_url}/hardware?{qs}"
           
                           print(f'Fetching page {page} from {url}')
           
                           response = http.request('GET', url, headers=headers, timeout=60.0)
           
                           if response.status != 200:
                               print(f'Error: API returned status {response.status}')
                               break
           
                           data = json.loads(response.data.decode('utf-8'))
           
                           # Get rows from response (Snipe-IT uses 'rows' field)
                           rows = data.get('rows', [])
                           total_available = data.get('total', 0)
           
                           # Write page to GCS
                           blob_name = f"{prefix}/{ts.strftime('%Y/%m/%d')}/snipeit-hardware-{page:05d}.json"
                           blob = bucket.blob(blob_name)
                           body = json.dumps(data, separators=(',', ':')).encode('utf-8')
                           blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(body, content_type='application/json')
           
                           print(f'Wrote page {page} with {len(rows)} rows to {blob_name}')
           
                           total += len(rows)
           
                           # Check if we've reached the end
                           # Snipe-IT returns empty rows array when no more data
                           if len(rows) == 0:
                               print(f'No more results (empty rows array)')
                               break
           
                           # Also check if we've fetched all available records
                           if offset + len(rows) >= total_available:
                               print(f'Reached end of data (offset {offset + len(rows)} >= total {total_available})')
                               break
           
                           page += 1
                           offset += page_size
           
                       print(f'Successfully processed {page + 1} pages with {total} total objects')
           
                   except Exception as e:
                       print(f'Error processing logs: {str(e)}')
                       raise
               ```
           

     * Second file: **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `snipeit-assets-to-gcs-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic (`snipeit-assets-trigger`)  
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



### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > snipeit-assets-to-gcs > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snipe-IT logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snipe-IT** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest Snipe-IT logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snipe-IT logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snipe-IT** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://snipe-it-logs/snipeit/assets/
           

       * Replace:

         * `snipe-it-logs`: Your GCS bucket name.
         * `snipeit/assets`: Prefix/folder path where logs are stored.
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

Log field | UDM mapping | Logic  
---|---|---  
`created_at.datetime` | `entity.asset.attribute.creation_time` | Parsed as `UNIX_MS`  
`age` | `entity.asset.attribute.labels.value` | Directly mapped  
`alt_barcode` | `entity.asset.attribute.labels.value` | Directly mapped  
`asset_eol_date` | `entity.asset.attribute.labels.value` | Directly mapped  
`asset_tag` | `entity.asset.attribute.labels.value` | Directly mapped  
`asset_type_value` | `entity.asset.attribute.labels.value` | Directly mapped  
`assets_classification_value` | `entity.asset.attribute.labels.value` | Directly mapped  
`category.id` | `entity.asset.attribute.labels.value` | Directly mapped  
`custom_fields.RAM.value` | `entity.asset.attribute.labels.value` | Directly mapped  
`custom_fields.SSD.value` | `entity.asset.attribute.labels.value` | Directly mapped  
`last_update_time.formatted` | `entity.asset.attribute.labels.value` | Directly mapped  
`manufacturer.id` | `entity.asset.attribute.labels.value` | Directly mapped  
`model_id` | `entity.asset.attribute.labels.value` | Directly mapped  
`model_number` | `entity.asset.attribute.labels.value` | Directly mapped  
`updated_at.datetime` | `entity.asset.attribute.last_update_time` | Parsed as `UNIX_MS`  
`category.name` | `entity.asset.category` | Directly mapped  
`custom_fields.Processor.value` | `entity.asset.hardware.cpu_model` | Directly mapped  
`manufacturer.name` | `entity.asset.hardware.manufacturer` | Directly mapped  
`model.name` | `entity.asset.hardware.model` | Directly mapped  
`serial` | `entity.asset.hardware.serial_number` | Directly mapped  
`name` | `entity.asset.hostname` | Directly mapped  
`location.name` | `entity.asset.location.name` | Directly mapped  
`id` | `entity.asset.product_object_id` | Directly mapped  
`custom_fields.Owner.value` | `entity.labels.value` | Directly mapped  
`deleted_at` | `entity.labels.value` | Directly mapped  
`eol` | `entity.labels.value` | Directly mapped  
`expected_checkin` | `entity.labels.value` | Directly mapped  
`image` | `entity.labels.value` | Directly mapped  
`last_audit_date` | `entity.labels.value` | Directly mapped  
`next_audit_date.date` | `entity.labels.value` | Directly mapped  
`notes` | `entity.labels.value` | Directly mapped  
`order_number` | `entity.labels.value` | Directly mapped  
`purchase_cost` | `entity.labels.value` | Directly mapped  
`purchase_date.date` | `entity.labels.value` | Directly mapped  
`purchase_date.formatted` | `entity.labels.value` | Directly mapped  
`qr` | `entity.labels.value` | Directly mapped  
`requestable` | `entity.labels.value` | Directly mapped  
`requests_counter` | `entity.labels.value` | Directly mapped  
`rtd_location.id` | `entity.labels.value` | Directly mapped  
`status_label.id` | `entity.labels.value` | Directly mapped  
`status_label.status_meta` | `entity.labels.value` | Directly mapped  
`status_label.status_type` | `entity.labels.value` | Directly mapped  
`supplier.id` | `entity.labels.value` | Directly mapped  
`supplier.name` | `entity.labels.value` | Directly mapped  
`updated_at.formatted` | `entity.labels.value` | Directly mapped  
`warranty_expires.date` | `entity.labels.value` | Directly mapped  
`warranty_expires.formatted` | `entity.labels.value` | Directly mapped  
`warranty_months` | `entity.labels.value` | Directly mapped  
`assigned_to.username` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.checkin` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.checkout` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.clone` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.delete` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.restore` | `entity.user.attribute.labels.value` | Directly mapped  
`available_actions.update` | `entity.user.attribute.labels.value` | Directly mapped  
`checkin_counter` | `entity.user.attribute.labels.value` | Directly mapped  
`checkout_counter` | `entity.user.attribute.labels.value` | Directly mapped  
`company.id` | `entity.user.attribute.labels.value` | Directly mapped  
`created_by.id` | `entity.user.attribute.labels.value` | Directly mapped  
`created_by.name` | `entity.user.attribute.labels.value` | Directly mapped  
`last_checkin.datetime` | `entity.user.attribute.labels.value` | Directly mapped  
`last_checkin.formatted` | `entity.user.attribute.labels.value` | Directly mapped  
`last_checkout.formatted` | `entity.user.attribute.labels.value` | Directly mapped  
`assigned_to.type` | `entity.user.attribute.roles.name` | Directly mapped  
`company.name` | `entity.user.company_name` | Directly mapped  
`assigned_to_email` | `entity.user.email_addresses` | Merged  
`assigned_to.employee_number` | `entity.user.employee_id` | Directly mapped  
`assigned_to.first_name` | `entity.user.first_name` | Directly mapped  
`last_checkout.datetime` | `entity.user.last_login_time` | Parsed as `UNIX_MS`  
`assigned_to.last_name` | `entity.user.last_name` | Directly mapped  
`assigned_to.name` | `entity.user.user_display_name` | Directly mapped  
`assigned_to.id` | `entity.user.userid` | Directly mapped  
`has_asset` | `metadata.entity_type` | Mapped: `true` → `ASSET`  
`has_user` | `metadata.entity_type` | Mapped: `true` → `USER`  
`has_asset` | `metadata.product_name` | Mapped: `true` → `CMDB`  
`has_user` | `metadata.product_name` | Mapped: `true` → `CMDB`  
`has_asset` | `metadata.vendor_name` | Mapped: `true` → `Snipe-IT`  
`has_user` | `metadata.vendor_name` | Mapped: `true` → `Snipe-IT`  
N/A | `entity.asset.attribute.labels.key` | Constant: `model_id`  
N/A | `entity.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `entity.labels.key` | Constant: `purchase_date`  
N/A | `entity.user.attribute.labels.key` | Constant: `checkout`  
N/A | `metadata.entity_type` | Constant: `ASSET`  
N/A | `metadata.product_name` | Constant: `CMDB`  
N/A | `metadata.vendor_name` | Constant: `Snipe-IT`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snipe-it-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
