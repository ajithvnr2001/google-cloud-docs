---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-bluexp/
title: Collect NetApp Console (formerly BlueXP) audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:50:31.294536+00:00
---

# Collect NetApp Console (formerly BlueXP) audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-bluexp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NetApp Console (formerly BlueXP) audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest NetApp Console (formerly BlueXP) audit logs to Google Security Operations using Google Cloud Storage V2.

NetApp Console is a unified control plane for managing hybrid multi-cloud storage and data services across on-premises and cloud environments. The Audit service records operations performed by Console services, including originating IP addresses, workspaces, Console agents used, and other telemetry data useful for forensic analysis and compliance requirements.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrative access to NetApp Console with permissions to create service accounts
  * Your NetApp Console account ID



## Configure NetApp Console API access

To enable Google SecOps to retrieve audit logs, you need to create a service account with appropriate permissions and generate API credentials.

### Get your account ID

  1. Navigate to the [NetApp Console](https://console.bluexp.netapp.com/) using a browser.
  2. Sign in using your NetApp Console credentials or NetApp Support Site credentials.
  3. Click the **Account** drop-down at the top of the page.
  4. Click **Manage Account** for the selected account.
  5. In the **Overview** section, copy the **Account ID** value.

**Note:** The account ID is a unique identifier required for API calls. It appears in the format of a UUID (for example, `account-AbCdEfGh`).



### Create a service account

  1. In the NetApp Console, go to **Administration > Identity and access**.
  2. Select **Members**.
  3. Select **Add a member**.
  4. For **Member Type** , select **Service account**.
  5. Enter a name for the service account (for example, `Google SecOps Integration`).
  6. Leave **Use private key JWT authentication** unchecked to use client secret authentication.

**Note:** Client secret authentication is recommended for simplicity. Private key JWT authentication provides enhanced security but requires managing RSA key pairs or X.509 certificates.
  7. In the **Select an organization, folder, or project** section, select your organization.

  8. For **Category** , select **Organization**.

  9. For **Role** , select **Organization viewer**.

**Note:** The Organization viewer role provides read-only access to audit logs. This follows the principle of least privilege, as write permissions are not required for log ingestion.
  10. Click **Add**.




### Record API credentials

After creating the service account, a dialog displays your credentials:

  * **Client ID** : Your unique client identifier (for example, `TvPPs4SeM5smEElsGmdDUznljhN3YY8s`)
  * **Client Secret** : Your API secret key

**Important:** Copy and save the client secret immediately. The Console displays it only once and does not allow you to retrieve it later. If you lose the client secret, you must delete the service account and create a new one.

  1. Download or copy both the **Client ID** and **Client Secret** to a secure location.
  2. Click **Close**.



### Verify permissions

To verify the service account has the required permissions:

  1. Sign in to the [NetApp Console](https://console.bluexp.netapp.com/).
  2. Go to **Administration > Identity and access**.
  3. Select **Members**.
  4. Locate the service account you created and verify it has the **Organization viewer** role.
  5. If the role is not assigned, click the service account name and update the role to **Organization viewer**.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        ACCOUNT_ID="your-account-id"
        
        # Obtain access token
        TOKEN=$(curl -s -X POST "https://netapp-cloud-account.auth0.com/oauth/token" \
            -H "Content-Type: application/json" \
            -d '{
                "grant_type": "client_credentials",
                "client_id": "'"${CLIENT_ID}"'",
                "client_secret": "'"${CLIENT_SECRET}"'",
                "audience": "https://api.cloud.netapp.com"
            }' | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test audit API access
        curl -s -H "Authorization: Bearer ${TOKEN}" \
            "https://cloudmanager.cloud.netapp.com/audit/${ACCOUNT_ID}?offset=0" \
            | python3 -m json.tool
        




A successful response returns a JSON object containing audit records for the specified account.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netapp-bluexp-audit-logs`)  
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
     * **Service account name** : Enter `netapp-bluexp-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect NetApp Console audit logs`
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
  2. Click on your bucket name (`netapp-bluexp-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`netapp-bluexp-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netapp-bluexp-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit logs from the NetApp Console Audit API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netapp-bluexp-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `netapp-bluexp-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `netapp-bluexp-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netapp-bluexp-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `netapp-bluexp-audit` | Prefix for log files  
`STATE_KEY` | `netapp-bluexp-audit/state.json` | State file path  
`NETAPP_CLIENT_ID` | `your-client-id` | NetApp Console service account Client ID  
`NETAPP_CLIENT_SECRET` | `your-client-secret` | NetApp Console service account Client Secret  
`NETAPP_ACCOUNT_ID` | `account-AbCdEfGh` | NetApp Console account ID  
`MAX_RECORDS` | `5000` | Max records per run  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netapp-bluexp-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'netapp-bluexp-audit/state.json')
    NETAPP_CLIENT_ID = os.environ.get('NETAPP_CLIENT_ID')
    NETAPP_CLIENT_SECRET = os.environ.get('NETAPP_CLIENT_SECRET')
    NETAPP_ACCOUNT_ID = os.environ.get('NETAPP_ACCOUNT_ID')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    TOKEN_URL = 'https://netapp-cloud-account.auth0.com/oauth/token'
    API_BASE = 'https://cloudmanager.cloud.netapp.com'
    AUDIENCE = 'https://api.cloud.netapp.com'
    
    def to_unix_millis(dt):
      if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
      dt = dt.astimezone(timezone.utc)
      return int(dt.timestamp() * 1000)
    
    def parse_datetime(value):
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith('Z'):
        value = value[:-1] + '+00:00'
      return datetime.fromisoformat(value)
    
    def get_access_token():
      body = json.dumps({
        'grant_type': 'client_credentials',
        'client_id': NETAPP_CLIENT_ID,
        'client_secret': NETAPP_CLIENT_SECRET,
        'audience': AUDIENCE,
      }).encode('utf-8')
    
      response = http.request(
        'POST', TOKEN_URL,
        body=body,
        headers={'Content-Type': 'application/json'}
      )
    
      if response.status != 200:
        raise Exception(
          f"Token request failed: {response.status} - "
          f"{response.data.decode('utf-8')}"
        )
    
      data = json.loads(response.data.decode('utf-8'))
      token = data.get('access_token')
      if not token:
        raise Exception('No access_token in token response')
    
      print('Successfully obtained NetApp Console access token')
      return token
    
    @functions_framework.cloud_event
    def main(cloud_event):
      if not all([GCS_BUCKET, NETAPP_CLIENT_ID, NETAPP_CLIENT_SECRET, NETAPP_ACCOUNT_ID]):
        print('Error: Missing required environment variables')
        return
    
      try:
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        state = load_state(bucket)
        now = datetime.now(timezone.utc)
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
          try:
            last_val = state['last_event_time']
            if last_val.endswith('Z'):
              last_val = last_val[:-1] + '+00:00'
            last_time = datetime.fromisoformat(last_val)
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f'Warning: Could not parse last_event_time: {e}')
            last_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f'Fetching audit logs from {last_time.isoformat()} to {now.isoformat()}')
    
        token = get_access_token()
    
        records, newest_time = fetch_audit_logs(token, last_time, now)
    
        if not records:
          print('No new audit records found.')
          save_state(bucket, now.isoformat())
          return
    
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f'{GCS_PREFIX}/netapp_bluexp_audit_{timestamp}.ndjson'
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join(
          [json.dumps(r, ensure_ascii=False, default=str) for r in records]
        ) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f'Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}')
    
        save_state(bucket, newest_time if newest_time else now.isoformat())
    
        print(f'Successfully processed {len(records)} audit records')
    
      except Exception as e:
        print(f'Error processing audit logs: {str(e)}')
        raise
    
    def fetch_audit_logs(token, start_time, end_time):
      endpoint = f'{API_BASE}/audit/{NETAPP_ACCOUNT_ID}'
    
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-NetAppBlueXPCollector/1.0',
      }
    
      start_millis = to_unix_millis(start_time)
      end_millis = to_unix_millis(end_time)
    
      records = []
      newest_time = None
      offset = 0
      page_num = 0
      backoff = 1.0
    
      while True:
        page_num += 1
    
        if len(records) >= MAX_RECORDS:
          print(f'Reached max_records limit ({MAX_RECORDS})')
          break
    
        url = (
          f'{endpoint}'
          f'?fromLastModified={start_millis}'
          f'&toLastModified={end_millis}'
          f'&offset={offset}'
        )
    
        try:
          response = http.request('GET', url, headers=headers)
    
          if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
            print(f'Rate limited (429). Retrying after {retry_after}s...')
            time.sleep(retry_after)
            backoff = min(backoff * 2, 30.0)
            continue
    
          backoff = 1.0
    
          if response.status != 200:
            print(f'HTTP Error: {response.status}')
            response_text = response.data.decode('utf-8')
            print(f'Response body: {response_text}')
            return [], None
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('auditEntries', [])
    
          if not page_results:
            print('No more results (empty page)')
            break
    
          print(f'Page {page_num}: Retrieved {len(page_results)} audit records')
          records.extend(page_results)
    
          for entry in page_results:
            try:
              last_modified = entry.get('lastModified')
              if last_modified:
                entry_dt = datetime.fromtimestamp(
                  last_modified / 1000, tz=timezone.utc
                )
                entry_time = entry_dt.isoformat()
                if newest_time is None or parse_datetime(entry_time) > parse_datetime(newest_time):
                  newest_time = entry_time
            except Exception as e:
              print(f'Warning: Could not parse entry time: {e}')
    
          count = data.get('count', len(page_results))
          if count < 100:
            print(f'Reached last page (count={count})')
            break
    
          offset += count
    
        except Exception as e:
          print(f'Error fetching audit logs: {e}')
          return [], None
    
      print(f'Retrieved {len(records)} total audit records from {page_num} pages')
      return records, newest_time
    
    def load_state(bucket):
      try:
        blob = bucket.blob(STATE_KEY)
        if blob.exists():
          return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
      except Exception as e:
        print(f'Warning: Could not load state: {e}')
      return {}
    
    def save_state(bucket, last_event_time_iso):
      try:
        state = {
          'last_event_time': last_event_time_iso,
          'last_run': datetime.now(timezone.utc).isoformat(),
        }
        blob = bucket.blob(STATE_KEY)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
          json.dumps(state, indent=2),
          content_type='application/json'
        )
        print(f'Saved state: last_event_time={last_event_time_iso}')
      except Exception as e:
        print(f'Warning: Could not save state: {e}')
    

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
**Name** | `netapp-bluexp-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `netapp-bluexp-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`netapp-bluexp-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `netapp-bluexp-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained NetApp Console access token
         Page 1: Retrieved X audit records
         Wrote X records to gs://netapp-bluexp-audit-logs/netapp-bluexp-audit/netapp_bluexp_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X audit records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `netapp-bluexp-audit-logs`.

  10. Navigate to the `netapp-bluexp-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `NETAPP_CLIENT_ID` and `NETAPP_CLIENT_SECRET` environment variables are correct
  * **HTTP 403** : Verify the service account has the **Organization viewer** role in NetApp Console
  * **HTTP 429** : Rate limiting — the function will automatically retry with exponential backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `NetApp Console Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **NetApp Console (formerly BlueXP)** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://netapp-bluexp-audit-logs/netapp-bluexp-audit/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `netapp-bluexp-audit-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
endTime | additional.fields | Merged with labels from each if not empty  
responseData | additional.fields |   
weHash | additional.fields |   
wePublicId | additional.fields |   
hasFailedRecord | additional.fields |   
action | additional.fields |   
service | additional.fields |   
hasRecords | additional.fields |   
workspaceId | additional.fields |   
lastModified | additional.fields |   
startTime | additional.fields |   
agentName | metadata.event_type | Set to STATUS_UPDATE if agentName not empty, else GENERIC_EVENT  
agentId | metadata.product_deployment_id | Value copied directly if not empty  
requestId | metadata.product_log_id | Value copied directly if not empty  
network | network | Renamed directly if not empty  
agentName | principal.asset.hostname | Value copied directly if not empty  
fileName | principal.file.names | Merged if not empty  
agentName | principal.hostname | Value copied directly if not empty  
accountId | principal.resource.id | Value copied directly if not empty  
resourceName | principal.resource.name | Value copied directly if not empty  
accountId | principal.resource.product_object_id | Value from accountId if not empty, else from resourceId if not empty  
resourceId | principal.resource.product_object_id |   
principalId | principal.user.userid | Value copied directly if not empty  
status | security_result.action | Set to ALLOW if status =~ (?i)SUCCESS, BLOCK if in FAILURE or UNSUCCESSFUL_ATTEMPT  
status | security_result.action_details | Value copied directly if not empty  
target | target | Renamed directly if not empty  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-bluexp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
