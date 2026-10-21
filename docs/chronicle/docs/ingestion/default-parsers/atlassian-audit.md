---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit/
title: Collect Atlassian Organization Audit Log logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:41:14.673155+00:00
---

# Collect Atlassian Organization Audit Log logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/atlassian-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Atlassian Organization Audit Log logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Atlassian Organization Audit Log logs to Google Security Operations using Google Cloud Storage V2.

Atlassian Organization Audit Log provides a centralized record of administrative activities across your Atlassian organization at [admin.atlassian.com](https://admin.atlassian.com). It captures events such as user provisioning, group membership changes, authentication policy updates, and API key management, enabling security teams to monitor and investigate changes made by organization administrators.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Atlassian organization administration at [admin.atlassian.com](https://admin.atlassian.com)
  * An Atlassian organization with an [Atlassian Guard](https://support.atlassian.com/security-and-access-policies/docs/understand-atlassian-guard/) subscription (Standard or Premium) or at least one Enterprise plan (required for organization audit logs)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `atlassian-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Atlassian API credentials

### Create API key

  1. Sign in to [admin.atlassian.com](https://admin.atlassian.com).
  2. Select your organization if you have more than one.
  3. Go to **Settings > API keys**.
  4. Click **Create API key**.
  5. Enter a descriptive **Name** for the key (for example, `SecOps-Audit-Collector`).
  6. Set the **Expires on** date.

**Note:** API keys can last no longer than one year. Plan to rotate the key before expiration.
  7. Click **Create**.

  8. Copy and save your **API key** value securely. You cannot recover the API key value after you close this dialog.

  9. Note your **Organization ID** from the URL in the browser address bar (the UUID in `https://admin.atlassian.com/o/{orgId}/...`).

  10. Click **Done**.




### Verify permissions

To access organization audit logs through the API, you must be an organization administrator:

  1. Sign in to [admin.atlassian.com](https://admin.atlassian.com).
  2. Go to **Settings > API keys**.
  3. If you can see the **API keys** page and create keys, you have the required organization administrator permissions.
  4. If you cannot see this option, contact your Atlassian organization administrator to grant organization admin access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        API_KEY="<your-atlassian-api-key>"
        ORG_ID="<your-organization-id>"
        
        # Test API access using the events-stream endpoint
        curl -v \
            --header "Authorization: Bearer ${API_KEY}" \
            --header "Accept: application/json" \
            "https://api.atlassian.com/admin/v1/orgs/${ORG_ID}/events-stream?limit=1"
        




A successful response returns HTTP 200 with a JSON body containing a `data` array of event objects.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `atlassian-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Atlassian Organization Audit logs`
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
  2. Click on your bucket name (for example, `atlassian-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `atlassian-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `atlassian-audit-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to poll audit log events from the [Atlassian Organizations REST API](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-events/) and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `atlassian-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`atlassian-audit-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`atlassian-audit-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `atlassian-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `atlassian-audit` | Prefix for log files  
`STATE_KEY` | `atlassian-audit/state.json` | State file path  
`ATL_TOKEN` | `your-atlassian-api-key` | Atlassian API key  
`ATL_ORG_ID` | `your-organization-id` | Atlassian organization ID  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `200` | Records per page (max 500)  
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
    from urllib.parse import urlparse, parse_qs
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'atlassian-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'atlassian-audit/state.json')
    ATL_TOKEN = os.environ.get('ATL_TOKEN')
    ATL_ORG_ID = os.environ.get('ATL_ORG_ID')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '200'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def parse_datetime(value):
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Atlassian Organization
      Audit logs via the events-stream endpoint and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, ATL_TOKEN, ATL_ORG_ID]):
        print('Error: Missing required environment variables')
        return
    
      try:
        # Get GCS bucket
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
        # Load state
        state = load_state(bucket, STATE_KEY)
    
        # Determine time window
        now = datetime.now(timezone.utc)
        last_time = None
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
          try:
            last_time = parse_datetime(state["last_event_time"])
            # Overlap by 2 minutes to catch any delayed events
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
    
        if last_time is None:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        # Fetch logs using the events-stream polling endpoint
        records, newest_event_time = fetch_logs(
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No new log records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp_str = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp_str}.ndjson"
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
    
    def save_state(bucket, key, last_event_time_iso):
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
    
    def fetch_logs(start_time, end_time, page_size, max_records):
      """
      Fetch audit logs from Atlassian Organization events-stream API
      with cursor-based pagination.
    
      The events-stream endpoint is designed for polling use cases and
      supports higher throughput than the /events query endpoint.
    
      API reference:
      https://developer.atlassian.com/cloud/admin/organization/rest/api-group-events/
    
      Args:
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page (max 500)
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      endpoint = f"https://api.atlassian.com/admin/v1/orgs/{ATL_ORG_ID}/events-stream"
    
      headers = {
        'Authorization': f'Bearer {ATL_TOKEN}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-AtlassianAuditCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
      cursor = None
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        # Build request URL with query parameters
        params = [
          f"from={start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')}",
          f"to={end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')}",
          f"limit={min(page_size, max_records - len(records))}",
        ]
        if cursor:
          params.append(f"cursor={cursor}")
    
        url = f"{endpoint}?{'&'.join(params)}"
    
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
    
          # Track newest event time from attributes
          for event in page_results:
            try:
              attrs = event.get('attributes', {})
              event_time = attrs.get('time')
              if event_time:
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Check for next page using links.next or meta.next cursor
          next_link = data.get('links', {}).get('next')
          if not next_link:
            next_cursor = data.get('meta', {}).get('next')
            if not next_cursor:
              print("No more pages (no next cursor)")
              break
            cursor = next_cursor
          else:
            # Extract cursor from next link URL
            parsed = urlparse(next_link)
            query_params = parse_qs(parsed.query)
            cursor = query_params.get('cursor', [None])[0]
            if not cursor:
              break
    
        except Exception as e:
          print(f"Error fetching logs: {e}")
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
**Name** | `atlassian-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`atlassian-audit-logs-trigger`)  
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
  5. Click on your function name (`atlassian-audit-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://atlassian-audit-logs/atlassian-audit/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`atlassian-audit-logs`).

  10. Navigate to the prefix folder (`atlassian-audit/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API key in environment variables
  * **HTTP 403** : Verify organization admin permissions and Atlassian Guard subscription
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Atlassian Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ATLASSIAN_AUDIT** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://atlassian-audit-logs/atlassian-audit/
           

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
  2. Click on your bucket name (`atlassian-audit-logs`).
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
`attributes.time` | `metadata.event_timestamp` | Parsed from the `attributes.time` field in the raw log.  
`attributes.action` | `metadata.product_event_type` | The value is taken from the `attributes.action` field.  
`attributes.actor.id` | `principal.user.product_object_id` | The value is taken from the `attributes.actor.id` field.  
`attributes.actor.name` | `principal.user.user_display_name` | The value is taken from the `attributes.actor.name` field.  
`attributes.actor.email` | `principal.user.email_addresses` | The value is taken from the `attributes.actor.email` field.  
`attributes.location.ip` | `principal.ip` | The value is taken from the `attributes.location.ip` field.  
`attributes.location.geo` | `principal.location.country_or_region` | The value is taken from the `attributes.location.geo` field.  
`attributes.location.countryName` | `principal.location.name` | The value is taken from the `attributes.location.countryName` field.  
`attributes.context[].id` | `target.resource.product_object_id` | The value is taken from the context `id` field.  
`attributes.context[].type` | `target.resource.resource_subtype` | The value is taken from the context `type` field.  
`attributes.container[].id` | `target.resource.attribute.labels` | The container `id` is added as a label.  
`attributes.container[].type` | `target.resource.attribute.labels` | The container `type` is added as a label.  
`message.content` | `security_result.summary` | The value is taken from the `message.content` field.  
| `metadata.event_type` | Mapped based on available fields: `USER_RESOURCE_UPDATE_CONTENT` for resource modifications; otherwise `GENERIC_EVENT`.  
| `metadata.product_name` | Set to `Atlassian Admin`.  
| `metadata.vendor_name` | Set to `Atlassian`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
