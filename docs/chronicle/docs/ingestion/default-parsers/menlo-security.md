---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security/
title: Collect Menlo Security Isolation Platform (MSIP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:03:43.044448+00:00
---

# Collect Menlo Security Isolation Platform (MSIP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/menlo-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Menlo Security Isolation Platform (MSIP) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how you can ingest Menlo Security Isolation Platform (MSIP) logs to Google SecOps using Google Cloud Storage.

Menlo Security's isolation-centric approach splits web browsing and document retrieval between the user's device and an isolated, Disposable Virtual Container (DVC) away from the endpoint. All risky code is executed in the isolated DVC and never reaches the endpoint. Only safe display data is sent to the user's browser. The platform provides comprehensive logging for web access, audit events, email security, DLP violations, and SMTP activity.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Menlo Security Admin Portal**
  * Permissions to create API tokens in Menlo Security
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled



## Configure Menlo Security API access

To enable the Cloud Run function to retrieve logs, you need to create an API token with the Log Export API permission.

### Create API token

  1. Sign in to the **Menlo Security Admin Portal** at `https://admin.menlosecurity.com`.
  2. Go to **Settings > Authentication > API Tokens**.
  3. Click **Create Token**.
  4. In the **Token Name** field, enter a descriptive name (for example, `Chronicle GCS Integration`).
  5. In the **Permissions** section, select **Log Export API**.
  6. Click **Create** or **Save**.
  7. Copy and securely store the generated API token.



**Important** : The API token is displayed only once. Store it in a secure location immediately after creation.

### Required API permissions

  * The API token requires the following permission:

Permission/Scope | Access Level | Purpose  
---|---|---  
**Log Export API** | Read | Retrieve logs from Menlo Security API  
**Note:** Only the Log Export API permission is required for log ingestion. No additional permissions are needed.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `menlo-security-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `menlo-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Menlo Security logs`
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
  2. Click on your bucket name (`menlo-security-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`menlo-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `menlo-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `menlo-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `menlo-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `menlo-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `menlo-security-logs` | GCS bucket name  
`GCS_PREFIX` | `menlo-logs` | Prefix for log files  
`STATE_KEY` | `menlo-logs/state.json` | State file path  
`MENLO_API_TOKEN` | `your-menlo-api-token` | Menlo Security API token  
`MENLO_API_HOST` | `logs.menlosecurity.com` | Menlo Security API host  
`MENLO_LOG_TYPES` | `web,audit,email,dlp` | Comma-separated log types  
`LOOKBACK_HOURS` | `1` | Initial lookback period  
**Note:** The `MENLO_LOG_TYPES` variable accepts a comma-separated list of log types to collect. Supported values are: `web`, `audit`, `email`, `dlp`, `attachment`, `smtp`.
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
    import os
    import json
    import urllib3
    import time
    import uuid
    from datetime import datetime, timezone, timedelta
    
    http = urllib3.PoolManager(
      timeout=urllib3.Timeout(connect=5.0, read=60.0),
      retries=False,
    )
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'menlo-logs')
    STATE_KEY = os.environ.get('STATE_KEY', 'menlo-logs/state.json')
    API_TOKEN = os.environ.get('MENLO_API_TOKEN')
    API_HOST = os.environ.get('MENLO_API_HOST', 'logs.menlosecurity.com')
    LOG_TYPES = os.environ.get('MENLO_LOG_TYPES', 'web').split(',')
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '1'))
    
    @functions_framework.cloud_event
    def main(cloud_event):
      if not all([GCS_BUCKET, API_TOKEN, API_HOST]):
        print('Error: Missing required environment variables')
        return
    
      try:
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        state = load_state(bucket)
        now = datetime.now(timezone.utc).replace(microsecond=0)
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
          try:
            last_val = state['last_event_time']
            if last_val.endswith('Z'):
              last_val = last_val[:-1] + '+00:00'
            last_time = datetime.fromisoformat(last_val)
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
            last_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        total = 0
        newest_time = None
    
        for log_type in LOG_TYPES:
          log_type = log_type.strip()
          print(f"Fetching {log_type} logs...")
          events = fetch_logs(log_type, API_TOKEN, API_HOST, last_time, now)
    
          if events:
            object_key = f"{GCS_PREFIX}/{now:%Y/%m/%d}/menlo-{log_type}-{uuid.uuid4()}.ndjson"
            blob = bucket.blob(object_key)
    
            ndjson = '\n'.join(
              [json.dumps(ev, ensure_ascii=False) for ev in events]
            ) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Uploaded {len(events)} {log_type} events to gs://{GCS_BUCKET}/{object_key}")
            total += len(events)
    
            for ev in events:
              ev_time = ev.get('timestamp') or ev.get('time') or ev.get('created_at')
              if ev_time and (newest_time is None or str(ev_time) > str(newest_time)):
                newest_time = str(ev_time)
          else:
            print(f"No {log_type} events found")
    
        save_state(bucket, newest_time if newest_time else now.isoformat())
        print(f"Successfully processed {total} total events")
    
      except Exception as e:
        print(f'Error processing logs: {str(e)}')
        raise
    
    def fetch_logs(log_type, token, api_host, start, end):
      url = f"https://{api_host}/api/v1/logs/{log_type}"
      headers = {
        'Authorization': f'Token {token}',
        'Accept': 'application/json',
      }
      params = {
        'start': start.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'end': end.strftime('%Y-%m-%dT%H:%M:%SZ'),
      }
      query = '&'.join(f'{k}={v}' for k, v in params.items())
      full_url = f'{url}?{query}'
    
      all_events = []
      backoff = 1.0
    
      while full_url:
        response = http.request('GET', full_url, headers=headers)
    
        if response.status == 429:
          retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
          print(f"Rate limited. Waiting {retry_after}s...")
          time.sleep(retry_after)
          backoff = min(backoff * 2, 60.0)
          continue
    
        if response.status != 200:
          print(f"API error {response.status}: {response.data.decode('utf-8')}")
          break
    
        backoff = 1.0
        data = json.loads(response.data.decode('utf-8'))
        events = data if isinstance(data, list) else data.get('events', data.get('data', []))
        all_events.extend(events)
    
        full_url = data.get('next') if isinstance(data, dict) else None
    
      print(f"Total {log_type} events fetched: {len(all_events)}")
      return all_events
    
    def load_state(bucket):
      try:
        blob = bucket.blob(STATE_KEY)
        if blob.exists():
          return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
      except Exception as e:
        print(f"Warning: Could not load state: {e}")
      return {}
    
    def save_state(bucket, last_event_time_iso):
      try:
        state = {
          'last_event_time': last_event_time_iso,
          'last_run': datetime.now(timezone.utc).isoformat()
        }
        blob = bucket.blob(STATE_KEY)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
          json.dumps(state, indent=2),
          content_type='application/json'
        )
        print(f"Saved state: last_event_time={last_event_time_iso}")
      except Exception as e:
        print(f"Warning: Could not save state: {e}")
    

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
**Name** | `menlo-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `menlo-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`menlo-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `menlo-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Fetching web logs...
         Total web events fetched: X
         Uploaded X web events to gs://menlo-security-logs/menlo-logs/YYYY/MM/DD/menlo-web-UUID.ndjson
         Successfully processed X total events
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `menlo-security-logs`.

  10. Navigate to the `menlo-logs/` folder.

  11. Verify that new `.ndjson` files were created with the current date.




If you see errors in the logs:

  * **HTTP 401** : Verify the `MENLO_API_TOKEN` environment variable is correct
  * **HTTP 403** : Verify the API token has the **Log Export API** permission
  * **HTTP 429** : Rate limiting — the function will automatically retry with backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Menlo Security MSIP Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Menlo Security** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://menlo-security-logs/menlo-logs/
           

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

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `menlo-security-logs`.
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
customer_name | intermediary.hostname | Set if customer_name not IP  
customer_name | intermediary.ip | Extracted from customer_name if IP, or from xff_ip IPs  
xff_ip | intermediary.ip |   
event_data.event_time | metadata.event_timestamp | Parsed using grok and date filter  
request_type | metadata.event_type | Conditional logic based on these fields  
has_principal | metadata.event_type |   
has_top_url | metadata.event_type |   
has_dest | metadata.event_type |   
log_type | metadata.log_type | Value copied directly  
event_data.name | metadata.product_event_type | Value copied directly  
reqId | metadata.product_log_id | Value copied directly  
event_data.version | metadata.product_version | Value copied directly  
event_data.protocol | network.application_protocol | Mapped using predefined protocol list  
request_type | network.http.method | Value copied directly  
referer | network.http.referral_url | Value copied directly  
response_code | network.http.response_code | Converted to integer  
event_data.user-agent | network.http.user_agent | Value copied directly  
full_session_id | network.session_id | Value copied directly  
browser_and_version | principal.application | Value copied directly  
event_data.x-client-ip | principal.asset.ip | Value from event_data.x-client-ip if not empty, else src_ip  
src_ip | principal.asset.ip |   
groups | principal.group.product_object_id | Value copied directly  
event_data.x-client-ip | principal.ip | Value from event_data.x-client-ip if not empty, else src_ip  
src_ip | principal.ip |   
region | principal.location.country_or_region | Value from region if not empty, else egress_country  
egress_country | principal.location.country_or_region |   
region_name | principal.location.name | Value copied directly  
egress_ip | principal.nat_ip | Value copied directly  
event_data.userid | principal.user.email_addresses | Merged if matches email regex  
event_data.userid | principal.user.userid | Value copied directly  
event_data.domain | security_result.about.administrative_domain | Value copied directly  
event_data.url | security_result.about.url | Value copied directly  
event_data.pe_action | security_result.action | Mapped to ALLOW, BLOCK, or ALLOW_WITH_MODIFICATION  
event_data.categories | security_result.category_details | Merged from event_data.categories (extracted or direct) and casb_cat_name  
casb_cat_name | security_result.category_details |   
event_data.risk_score | security_result.confidence_details | Value copied directly  
content-type | security_result.detection_fields | Merged from various label fields  
product | security_result.detection_fields |   
threats | security_result.detection_fields |   
virusDetails | security_result.detection_fields |   
sandboxResult | security_result.detection_fields |   
fullScanResult | security_result.detection_fields |   
tab_id | security_result.detection_fields |   
pe_reason | security_result.detection_fields |   
ua_type | security_result.detection_fields |   
email_isolation_state | security_result.detection_fields |   
document_url | security_result.detection_fields |   
archive_path | security_result.detection_fields |   
casb_app_name | security_result.detection_fields |   
casb_fun_name | security_result.detection_fields |   
casb_org_name | security_result.detection_fields |   
casb_profile_id | security_result.detection_fields |   
casb_profile_name | security_result.detection_fields |   
casb_profile_type | security_result.detection_fields |   
casb_risk_score | security_result.detection_fields |   
connId | security_result.detection_fields |   
origin_country | security_result.detection_fields |   
egress_country | security_result.detection_fields |   
is_casb_ddl | security_result.detection_fields |   
is_iframe | security_result.detection_fields |   
parent_file_id | security_result.detection_fields |   
parent_filename | security_result.detection_fields |   
parent_sha256 | security_result.detection_fields |   
parent_tid | security_result.detection_fields |   
root_file_id | security_result.detection_fields |   
root_filename | security_result.detection_fields |   
root_sha256 | security_result.detection_fields |   
casb_risk_score | security_result.risk_score | Converted to float  
casb_profile_id | security_result.rule_id | Value copied directly  
pe_rulename | security_result.rule_name | Value copied directly  
casb_profile_name | security_result.rule_set | Value copied directly  
casb_profile_type | security_result.rule_type | Value copied directly  
event_data.severity | security_result.severity_details | Value copied directly  
magicName | security_result.summary | Concatenated as "%{magicName} is %{threats}."  
threats | security_result.summary |   
threat_types | security_result.threat_name | Value copied directly  
origin_ip | src.ip | Value copied directly  
origin_country | src.location.country_or_region | Value copied directly  
event_data.dst | target.asset.ip | Extracted from event_data.dst or dst using grok IP pattern  
dst | target.asset.ip |   
filename | target.file.full_path | Value copied directly  
mimeType | target.file.mime_type | Value copied directly  
sha256 | target.file.sha256 | Value copied directly  
file_size | target.file.size | Converted to float then uinteger  
event_data.dst | target.ip | Extracted from event_data.dst or dst using grok IP pattern  
dst | target.ip |   
top_url | target.url | Extracted using URI grok pattern  
metadata.product_name | metadata.product_name | Set to "MENLO SECURITY"  
metadata.vendor_name | metadata.vendor_name | Set to "MENLO SECURITY"  
`region` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`region_name` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`groups` | `event.idm.read_only_udm.principal.group.product_object_id` | Mapped from changelog  
`content-type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`product` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mimeType` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/menlo-security-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
