---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openai-auditlog/
title: Collect OpenAI Audit Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:45.942022+00:00
---

# Collect OpenAI Audit Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openai-auditlog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OpenAI Audit Logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest OpenAI Audit Logs to Google Security Operations using Google Cloud Storage V2.

OpenAI provides the Audit Logs API for organizations using the OpenAI API Platform. The API tracks user actions and configuration changes within an organization, including API key lifecycle events, user management, project changes, invitations, service account activity, login and logout events, and organization configuration changes.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Organization Owner role in your OpenAI API Platform organization



## Enable OpenAI audit logging

Before you can access audit logs, you must enable audit logging in your organization.

  1. Sign in to the **OpenAI Platform** at <https://platform.openai.com>.
  2. Go to **Settings > Organization > Data controls**.
  3. Scroll down to the **Audit logging** section.
  4. Click **Enable** under **Audit logging**.
  5. Click **Save**.

**Note:** Once enabled, audit logging cannot be disabled for security reasons. All authenticated requests to the Admin API are logged for security and compliance purposes.



## Create OpenAI Admin API key

  1. Sign in to the **OpenAI Platform** at <https://platform.openai.com>.
  2. In the left-hand panel, click **Admin keys**.
  3. Alternatively, navigate directly to <https://platform.openai.com/settings/organization/admin-keys>.
  4. Click **Create new admin key**.
  5. In the **Name** field, enter a descriptive name (for example, `Google SecOps Integration`).
  6. Click **Create**.
  7. Copy the API key immediately and store it securely.

**Note:** The Admin API key is displayed only once. If you lose the key, you must delete it and create a new one. Only Organization Owners can create and use Admin API keys.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual Admin API key
        OPENAI_ADMIN_KEY="your-admin-api-key"
        
        # Test audit logs API access
        curl -s -H "Authorization: Bearer ${OPENAI_ADMIN_KEY}" \
            -H "Content-Type: application/json" \
            "https://api.openai.com/v1/organization/audit_logs?limit=5" \
            | python3 -m json.tool
        




A successful response returns a JSON object with an `object` field set to `list` and a `data` array containing audit log entries.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `openai-auditlog-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `openai-auditlog-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect OpenAI audit logs`
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



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`openai-auditlog-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`openai-auditlog-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `openai-auditlog-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the OpenAI Audit Logs API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `openai-auditlog-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `openai-auditlog-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `openai-auditlog-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `openai-auditlog-logs` | GCS bucket name  
`GCS_PREFIX` | `openai-auditlog` | Prefix for log files  
`STATE_KEY` | `openai-auditlog/state.json` | State file path  
`OPENAI_ADMIN_KEY` | `your-admin-api-key` | OpenAI Admin API key  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `100` | Records per API page (max 100)  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100`
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'openai-auditlog')
           STATE_KEY = os.environ.get('STATE_KEY', 'openai-auditlog/state.json')
           OPENAI_ADMIN_KEY = os.environ.get('OPENAI_ADMIN_KEY')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           API_BASE = 'https://api.openai.com'
           AUDIT_LOGS_ENDPOINT = '/v1/organization/audit_logs'
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch OpenAI audit logs
             and write them to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, OPENAI_ADMIN_KEY]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket)
               now = datetime.now(timezone.utc)
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_effective_at'):
                 try:
                   last_effective_at = int(state['last_effective_at'])
                   last_time = datetime.fromtimestamp(last_effective_at, tz=timezone.utc)
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_effective_at: {e}")
                   last_time = now - timedelta(hours=LOOKBACK_HOURS)
               else:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               start_unix = int(last_time.timestamp())
               end_unix = int(now.timestamp())
           
               print(f"Fetching audit logs from {last_time.isoformat()} to {now.isoformat()}")
           
               records, newest_effective_at = fetch_audit_logs(
                 start_unix=start_unix,
                 end_unix=end_unix,
                 page_size=PAGE_SIZE,
                 max_records=MAX_RECORDS,
               )
           
               if not records:
                 print("No new audit log records found.")
                 save_state(bucket, end_unix)
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/openai_auditlog_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               if newest_effective_at:
                 save_state(bucket, newest_effective_at)
               else:
                 save_state(bucket, end_unix)
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing audit logs: {str(e)}')
               raise
           
           def load_state(bucket):
             """Load state from GCS."""
             try:
               blob = bucket.blob(STATE_KEY)
               if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
             return {}
           
           def save_state(bucket, last_effective_at):
             """Save the last effective_at Unix timestamp to GCS state file."""
             try:
               state = {
                 'last_effective_at': last_effective_at,
                 'last_run': datetime.now(timezone.utc).isoformat()
               }
               blob = bucket.blob(STATE_KEY)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_effective_at={last_effective_at}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           
           def fetch_audit_logs(start_unix, end_unix, page_size, max_records):
             """
             Fetch audit logs from the OpenAI API with pagination and rate limiting.
           
             Args:
               start_unix: Start time as Unix seconds
               end_unix: End time as Unix seconds
               page_size: Number of records per page (max 100)
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest effective_at Unix timestamp)
             """
             headers = {
               'Authorization': f'Bearer {OPENAI_ADMIN_KEY}',
               'Content-Type': 'application/json',
             }
           
             records = []
             newest_effective_at = None
             page_num = 0
             backoff = 1.0
             cursor = None
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               params = []
               params.append(f"effective_at[gte]={start_unix}")
               params.append(f"effective_at[lte]={end_unix}")
               params.append(f"limit={min(page_size, max_records - len(records))}")
               if cursor:
                 params.append(f"after={cursor}")
           
               url = f"{API_BASE}{AUDIT_LOGS_ENDPOINT}?{'&'.join(params)}"
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return [], None
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 page_results = data.get('data', [])
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 for event in page_results:
                   try:
                     effective_at = event.get('effective_at')
                     if effective_at is not None:
                       if newest_effective_at is None or effective_at > newest_effective_at:
                         newest_effective_at = effective_at
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 has_more = data.get('has_more', False)
                 if not has_more:
                   print("No more pages (has_more=false)")
                   break
           
                 last_id = data.get('last_id')
                 if not last_id:
                   print("No more pages (no last_id)")
                   break
           
                 cursor = last_id
           
               except Exception as e:
                 print(f"Error fetching audit logs: {e}")
                 return [], None
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_effective_at
           

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `openai-auditlog-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `openai-auditlog-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`openai-auditlog-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `openai-auditlog-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://openai-auditlog-logs/openai-auditlog/openai_auditlog_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `openai-auditlog-logs`.

  10. Navigate to the `openai-auditlog/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `OPENAI_ADMIN_KEY` environment variable is correct and the key has not been revoked
  * **HTTP 403** : Verify the API key is an Admin API key created by an Organization Owner
  * **HTTP 429** : Rate limiting — the function will automatically retry with exponential backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OpenAI Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **OpenAI Audit Logs** as the **Log type**. Click **Get Service Account**. A unique service account email is displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  7. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  8. Click **Next**.

  9. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://openai-auditlog-logs/openai-auditlog/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `openai-auditlog-logs`.
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
actor.session.ip_address_details.region_code | additional.fields | Merged as key-value pairs  
actor.session.ip_address_details.asn | additional.fields |   
effective_at | metadata.event_timestamp | Converted from UNIX timestamp  
has_principal | metadata.event_type | Set to "STATUS_UPDATE" if has_principal is true; "NETWORK_CONNECTION" if has_principal and has_target are true; "FILE_COPY" if has_principal, has_file, and has_source_file are true; "FILE_UNCATEGORIZED" if has_principal and has_file are true; "USER_UNCATEGORIZED" if has_user is true; else "GENERIC_EVENT"  
has_user | metadata.event_type |   
has_target | metadata.event_type |   
has_file | metadata.event_type |   
has_source_file | metadata.event_type |   
actor.session.user_agent | network.http.parsed_user_agent | Value copied directly and converted to parsed user agent  
actor.session.ja3 | network.tls.client.ja3 | Value copied directly  
actor.session.ip_address | principal.asset.ip | Value copied directly  
actor.session.ip_address | principal.ip | Value copied directly  
actor.session.ip_address_details.city | principal.location.city | Value copied directly  
actor.session.ip_address_details.country | principal.location.country_or_region | Value copied directly  
actor.session.ip_address_details.latitude | principal.location.region_latitude | Converted to float  
actor.session.ip_address_details.longitude | principal.location.region_longitude | Converted to float  
actor.session.ip_address_details.region | principal.location.state | Value copied directly  
actor.session.user.email | principal.user.email_addresses | Value copied directly  
actor.session.user.id | principal.user.userid | Extracted using grok pattern  
actor.session.ja4 | security_result.detection_fields | Merged as key-value pair with key "ja4"  
type | security_result.summary | Value copied directly  
metadata.product_name | metadata.product_name | Set to "OPENAI_AUDITLOG"  
metadata.vendor_name | metadata.vendor_name | Set to "OPENAI_AUDITLOG"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
