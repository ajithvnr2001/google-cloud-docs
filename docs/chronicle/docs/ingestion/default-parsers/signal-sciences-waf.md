---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf/
title: Collect Fastly Next-Gen WAF (formerly Signal Sciences) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:49.933118+00:00
---

# Collect Fastly Next-Gen WAF (formerly Signal Sciences) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fastly Next-Gen WAF (formerly Signal Sciences) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fastly Next-Gen WAF (formerly known as Signal Sciences) logs to Google Security Operations using Google Cloud Storage V2.

Fastly Next-Gen WAF is a cloud-based web application firewall that provides real-time threat detection and blocking for web applications, APIs, and microservices. It uses a signal-based approach to identify and mitigate attacks such as SQL injection, cross-site scripting, account takeover, and application abuse. The Signal Sciences REST API provides programmatic access to request feed data, which contains detailed information about flagged and blocked requests.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Fastly Next-Gen WAF dashboard with API access permissions
  * A Fastly Next-Gen WAF account with a corp name and at least one site configured



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sigsci-waf-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Fastly Next-Gen WAF API credentials

### Get API access token

  1. Sign in to the [Fastly Next-Gen WAF dashboard](https://dashboard.signalsciences.net/).
  2. Click your username in the upper-right corner, then select **My Profile**.
  3. Go to **API Access Tokens**.
  4. Click **Add API access token**.
  5. Enter a descriptive name for the token (for example, `Google SecOps Integration`).
  6. Click **Create API access token**.
  7. Copy and save the following details in a secure location:

     * **API token** : The generated token value (shown only once)
     * **Email address** : Your account email address used for authentication
**Note:** The API token is displayed only once at the time of creation. If you lose it, you must create a new token.



### Get corp and site names

  1. Sign in to the [Fastly Next-Gen WAF dashboard](https://dashboard.signalsciences.net/).
  2. Click **Manage > Corp > Corp Overview**.
  3. Note the **Corp short name** displayed on the page (for example, `my_corp`).
  4. Go to **Manage > Sites**.
  5. Note the **Site short name** for the site you want to collect logs from (for example, `my_site`).



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the [Fastly Next-Gen WAF dashboard](https://dashboard.signalsciences.net/).
  2. Go to **Manage > Corp > Corp Users**.
  3. Find your user account in the list.
  4. Verify that your role is **Admin** , **Owner** , or **Observer**. These roles have the required API access to retrieve request feed data.
  5. If your role does not have API access, contact your Fastly Next-Gen WAF administrator to grant the appropriate role.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SIGSCI_EMAIL="your-email@example.com"
        SIGSCI_TOKEN="your-api-token"
        SIGSCI_CORP="your-corp-name"
        SIGSCI_SITE="your-site-name"
        
        # Test API access - get site overview
        curl -v \
          -H "x-api-user:${SIGSCI_EMAIL}" \
          -H "x-api-token:${SIGSCI_TOKEN}" \
          "[https://dashboard.signalsciences.net/api/v0/corps/$](https://dashboard.signalsciences.net/api/v0/corps/$){SIGSCI_CORP}/sites/${SIGSCI_SITE}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details:

     * **Service account name** : Enter `sigsci-waf-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Fastly Next-Gen WAF logs`
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
  2. Click on your bucket name (for example, `sigsci-waf-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Enter the service account email (for example, `sigsci-waf-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.




## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details:

     * **Topic ID** : Enter `sigsci-waf-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.




## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch request feed data from the Fastly Next-Gen WAF API and write the logs to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sigsci-waf-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sigsci-waf-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sigsci-waf-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sigsci-waf-logs` | GCS bucket name  
`GCS_PREFIX` | `sigsci-waf` | Prefix for log files  
`STATE_KEY` | `sigsci-waf/state.json` | State file path  
`SIGSCI_EMAIL` | `your-email@example.com` | Signal Sciences API email  
`SIGSCI_TOKEN` | `your-api-token` | Signal Sciences API token  
`SIGSCI_CORP` | `your-corp-name` | Signal Sciences corp short name  
`SIGSCI_SITE` | `your-site-name` | Signal Sciences site short name  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page (max 1000)  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load)
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
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
      timeout=urllib3.Timeout(connect=5.0, read=30.0),
      retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sigsci-waf')
    STATE_KEY = os.environ.get('STATE_KEY', 'sigsci-waf/state.json')
    SIGSCI_EMAIL = os.environ.get('SIGSCI_EMAIL')
    SIGSCI_TOKEN = os.environ.get('SIGSCI_TOKEN')
    SIGSCI_CORP = os.environ.get('SIGSCI_CORP')
    SIGSCI_SITE = os.environ.get('SIGSCI_SITE')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    # Signal Sciences API base URL
    API_BASE = '[https://dashboard.signalsciences.net/api/v0](https://dashboard.signalsciences.net/api/v0)'
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Fastly Next-Gen WAF
      request feed data and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, SIGSCI_EMAIL, SIGSCI_TOKEN, SIGSCI_CORP, SIGSCI_SITE]):
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
            last_time = datetime.fromisoformat(state["last_event_time"])
            # Overlap by 2 minutes to catch any delayed events
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
    
        if last_time is None:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        # Convert to Unix epoch seconds (Signal Sciences API uses seconds)
        from_epoch = int(last_time.timestamp())
        until_epoch = int(now.timestamp())
    
        print(f"Fetching request feed from {last_time.isoformat()} to {now.isoformat()}")
        print(f"Corp: {SIGSCI_CORP}, Site: {SIGSCI_SITE}")
    
        # Fetch request feed
        records, newest_event_time = fetch_request_feed(
          corp=SIGSCI_CORP,
          site=SIGSCI_SITE,
          from_epoch=from_epoch,
          until_epoch=until_epoch,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No new request feed records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        # Update state with newest event time
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
    
    def fetch_request_feed(corp: str, site: str, from_epoch: int, until_epoch: int, page_size: int, max_records: int):
      """
      Fetch request feed from Fastly Next-Gen WAF (Signal Sciences) API
      with cursor-based pagination and rate limiting.
    
      Args:
        corp: Signal Sciences corp short name
        site: Signal Sciences site short name
        from_epoch: Start time as Unix epoch seconds
        until_epoch: End time as Unix epoch seconds
        page_size: Number of records per page (max 1000)
        max_records: Maximum total records to fetch (max 10000)
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      headers = {
        'x-api-user': SIGSCI_EMAIL,
        'x-api-token': SIGSCI_TOKEN,
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-SignalSciencesWAFCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
    
      # Initial URL with time range parameters
      url = f"{API_BASE}/corps/{corp}/sites/{site}/feed/requests?from={from_epoch}&until={until_epoch}&limit={min(page_size, 1000)}"
    
      while url:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        try:
          response = http.request('GET', url, headers=headers)
    
          # Handle rate limiting with exponential backoff
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
    
          # Track newest event time
          for event in page_results:
            try:
              event_timestamp = event.get('timestamp')
              if event_timestamp:
                event_dt = datetime.fromtimestamp(event_timestamp, tz=timezone.utc)
                event_time = event_dt.isoformat()
                if newest_time is None or event_dt > datetime.fromisoformat(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Cursor-based pagination using next URI
          next_url = data.get('next', {}).get('uri', '')
          if next_url:
            url = f"[https://dashboard.signalsciences.net](https://dashboard.signalsciences.net){next_url}"
          else:
            print("No more pages (no next cursor)")
            break
    
        except Exception as e:
          print(f"Error fetching request feed: {e}")
          return [], None
    
      print(f"Retrieved {len(records)} total records from {page_num} pages")
      return records, newest_time
    

     * **requirements.txt:**
    
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
**Name** | `sigsci-waf-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sigsci-waf-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `sigsci-waf-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching request feed from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Corp: my_corp, Site: my_site
         Page 1: Retrieved X events
         Wrote X records to gs://sigsci-waf-logs/sigsci-waf/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`sigsci-waf-logs`).

  10. Navigate to the `sigsci-waf/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API email and token in environment variables
  * **HTTP 403** : Verify the account has Admin, Owner, or Observer role in the Fastly Next-Gen WAF dashboard
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Fastly Next-Gen WAF logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Signal Sciences WAF Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Signal Sciences WAF** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sigsci-waf-logs/sigsci-waf/
           

       * Replace: 
         * `sigsci-waf-logs`: Your GCS bucket name.
         * `sigsci-waf`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
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
| metadata.event_type | Set to "NETWORK_HTTP"  
| metadata.vendor_name | Set to "Signal Sciences"  
| metadata.product_name | Set to "WAF"  
id | metadata.product_log_id | Value copied directly  
timestamp | metadata.event_timestamp | Converted from Unix epoch seconds  
remoteIP | principal.ip | Value copied directly  
remoteHostname | principal.hostname | Value copied directly  
remoteCountryCode | principal.location.country_or_region | Value copied directly  
serverHostname | target.hostname | Value copied directly  
serverName | target.asset.hostname | Value copied directly  
method | network.http.method | Value copied directly  
protocol | network.application_protocol | Value copied directly  
path | target.url | Value copied directly  
uri | network.http.referral_url | Value copied directly  
userAgent | network.http.user_agent | Value copied directly  
responseCode | network.http.response_code | Converted to integer  
responseSize | network.received_bytes | Converted to unsigned integer  
responseMillis | additional.fields | Mapped as response_millis label  
tags | security_result.category_details | Array of tag objects mapped to categories  
headersIn | additional.fields | Request headers mapped as key-value pairs  
headersOut | additional.fields | Response headers mapped as key-value pairs  
`created` | `metadata.timestamp` | Mapped from changelog  
`eventType` | `metadata.product_event_type` | Mapped from changelog  
`message_data` | `metadata.description` | Mapped from changelog  
`username` | `target.user.user_display_name` | Mapped from changelog  
`userid` | `target.user.userid` | Mapped from changelog  
`attachments.Fields.Title" , "attachments.Fields.Value` | `metadata.ingestion_labels` | Mapped from changelog  
`msgData.detailLink` | `network.http.referral_url` | Mapped from changelog  
`msgData.name` | `target.resource.name` | Mapped from changelog  
`msgData.changes` | `target.resource.attribute.labels` | Mapped from changelog  
`msgData.reason` | `security_result.summary` | Mapped from changelog  
`msgData.conditions` | `security_result.description` | Mapped from changelog  
`msgData.sites` | `network.http.user_agent` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/signal-sciences-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
