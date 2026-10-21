---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonrai/
title: Collect Sonrai Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:20:25.098538+00:00
---

# Collect Sonrai Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonrai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sonrai Security logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Sonrai Security logs to Google Security Operations using Google Cloud Storage V2.

Sonrai Security is an enterprise cloud security platform for identity, data, and access governance across multi-cloud environments. It provides security findings, tickets, and audit data through a GraphQL API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Sonrai Security with administrator permissions and API key access



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sonrai-security-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Sonrai Security API credentials

### Generate API key

  1. Sign in to the **Sonrai Security** platform as an administrator.
  2. Go to **Settings > API Keys**.
  3. Click **Create API Key**.
  4. Enter a name for the key (for example, `Google Security Operations Integration`).
  5. Copy and save the generated **API key** in a secure location.



### Determine organization URL

The API endpoint is based on your Sonrai Security organization. The format is:

Component | Value  
---|---  
**GraphQL endpoint** | `https://YOUR_ORG.sonraisecurity.com/graphql`  
**Note:** Replace `YOUR_ORG` with your organization's Sonrai subdomain.

### Verify permissions

To verify the API key has the required access:

  1. Sign in to the **Sonrai Security** platform.
  2. Go to **Settings > API Keys**.
  3. Verify the API key is listed and active.
  4. Confirm the key has permissions to query Tickets, Findings, and Audit data.
  5. If permissions are restricted, contact your Sonrai Security administrator.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        API_KEY="your-api-key"
        ORG_URL="https://YOUR_ORG.sonraisecurity.com"
        
        # Test API access - query tickets
        curl -v -X POST \
          -H "Authorization: Bearer ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d '{"query": "{ Tickets(where: {createdDate: {op: GT, value: \"2024-01-01T00:00:00Z\"}}) { count } }"}' \
          "${ORG_URL}/graphql"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sonrai-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Sonrai Security logs`.
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

  * **Storage Object Admin** : Write logs to GCS bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `sonrai-security-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `sonrai-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sonrai-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Sonrai Security GraphQL API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sonrai-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sonrai-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sonrai-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sonrai-security-logs` | GCS bucket name  
`GCS_PREFIX` | `sonrai` | Prefix for log files  
`STATE_KEY` | `sonrai/state.json` | State file path  
`API_KEY` | `your-api-key` | Sonrai Security API key  
`ORG_URL` | `https://YOUR_ORG.sonraisecurity.com` | Sonrai organization URL  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `500` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sonrai')
           STATE_KEY = os.environ.get('STATE_KEY', 'sonrai/state.json')
           API_KEY = os.environ.get('API_KEY', '')
           ORG_URL = os.environ.get('ORG_URL', '').rstrip('/')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '500'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Sonrai Security logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, API_KEY, ORG_URL]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               # Determine time window
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching tickets from {last_time.isoformat()} to {now.isoformat()}")
           
               # Fetch tickets/findings
               records, newest_event_time = fetch_tickets(
                 start_time=last_time,
                 end_time=now,
                 page_size=PAGE_SIZE,
                 max_records=MAX_RECORDS,
               )
           
               if not records:
                 print("No new records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def load_state(bucket, key):
             """Load state from GCS."""
             try:
               blob = bucket.blob(key)
               if blob.exists():
                 state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                 return json.loads(state_data)
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
           
             return {}
           
           def save_state(bucket, key, last_event_time_iso: str):
             """Save the last event timestamp to GCS state file."""
             try:
               state = {'last_event_time': last_event_time_iso}
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_event_time={last_event_time_iso}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           
           def graphql_query(query: str):
             """Execute a GraphQL query against Sonrai Security API with rate limiting."""
             endpoint = f"{ORG_URL}/graphql"
           
             headers = {
               'Authorization': f'Bearer {API_KEY}',
               'Content-Type': 'application/json',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-SonraiCollector/1.0'
             }
           
             body = json.dumps({'query': query})
           
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               response = http.request('POST', endpoint, body=body.encode('utf-8'), headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429). Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 continue
           
               if response.status != 200:
                 print(f"HTTP Error: {response.status} - {response.data.decode('utf-8')}")
                 return None
           
               data = json.loads(response.data.decode('utf-8'))
           
               if 'errors' in data:
                 print(f"GraphQL errors: {json.dumps(data['errors'])}")
                 return None
           
               return data.get('data')
           
             print(f"Failed after {max_retries} retries due to rate limiting")
             return None
           
           def fetch_tickets(start_time: datetime, end_time: datetime, page_size: int, max_records: int):
             """
             Fetch tickets from Sonrai Security GraphQL API with pagination and rate limiting.
             """
             records = []
             newest_time = None
             page_num = 0
             offset = 0
           
             start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               current_limit = min(page_size, max_records - len(records))
           
               query = f"""{{
                         Tickets(
                           where: {{createdDate: {{op: GT, value: \"{start_iso}\"}}}}
                   limit: {current_limit}
                   offset: {offset}
                 ) {{
                           count
                           items {{
                             srn
                             title
                             severity
                             status
                             createdDate
                             updatedDate
                             resourceSrn
                             eventName
                             actionType
                             sourceIp
                             actor {{
                               profile {{
                                 srn
                                 name
                               }}
                     }}
                     message
                   }}
                 }}
               }}"""
           
               data = graphql_query(query)
               if not data:
                 break
           
               tickets_data = data.get('Tickets', {})
               page_results = tickets_data.get('items', [])
           
               if not page_results:
                 print(f"No more results (empty page)")
                 break
           
               print(f"Page {page_num}: Retrieved {len(page_results)} tickets")
               records.extend(page_results)
           
               # Track newest event time
               for ticket in page_results:
                 try:
                   event_time = ticket.get('createdDate')
                   if event_time:
                     if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                       newest_time = event_time
                 except Exception as e:
                   print(f"Warning: Could not parse event time: {e}")
           
               if len(page_results) < current_limit:
                 print(f"Reached last page (size={len(page_results)} < limit={current_limit})")
                 break
           
               offset += len(page_results)
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_time
           

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
**Name** | `sonrai-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sonrai-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`sonrai-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > sonrai-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching tickets from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X tickets
         Wrote X records to gs://sonrai-security-logs/sonrai/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  5. Check the GCS bucket (`sonrai-security-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check API key in environment variables
  * **HTTP 403** : Verify API key has required permissions in Sonrai Security platform
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **GraphQL errors** : Verify the query syntax and available fields



## Configure a feed in Google SecOps to ingest Sonrai Security logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Sonrai Security Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Sonrai Enterprise Cloud Security Solution** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sonrai-security-logs/sonrai/
           

       * Replace: 
         * `sonrai-security-logs`: Your GCS bucket name.
         * `sonrai`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`sonrai-security-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
actor.profile | principal.resource.attribute.labels | Labels associated with the resource  
actor.profile.srn | target.user.product_object_id | Product-specific object ID for the user  
actor.profile.srn | target.user.userid | User ID  
actorSrn, variables, gql, type | additional.fields | Additional fields not captured elsewhere in the UDM schema  
actionType | security_result.action_details | Details of the action taken  
createdDate | metadata.event_timestamp | Timestamp of the event  
event_type | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
eventName | metadata.product_event_type | Product-specific event type  
message | security_result.summary | Summary of the security result  
metadata | metadata | Metadata about the event  
principal | principal | Information about the principal (actor)  
resourceSrn | principal.resource.name | Name of the resource  
security_result | security_result | Security result information  
sourceIp | principal.asset.ip | IP address of the asset  
sourceIp | principal.ip | IP address associated with the principal  
target | target | Information about the target  
| extensions.auth.type | Authentication type used in the event  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor/company name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonrai-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
