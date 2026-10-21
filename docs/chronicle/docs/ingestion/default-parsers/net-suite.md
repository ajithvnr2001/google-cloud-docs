---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/net-suite/
title: Collect Oracle NetSuite - NetSuite Applications Suite logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:59:58.408966+00:00
---

# Collect Oracle NetSuite - NetSuite Applications Suite logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/net-suite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle NetSuite - NetSuite Applications Suite logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Oracle NetSuite - NetSuite Applications Suite logs to Google Security Operations using Google Cloud Storage V2.

Oracle NetSuite is a cloud-based enterprise resource planning (ERP) platform that provides comprehensive business management capabilities including financial management, customer relationship management (CRM), e-commerce, and inventory management. NetSuite generates extensive audit logs including user login trails, system notes tracking record changes, and API access logs that can be retrieved via the SuiteQL REST API for security monitoring and compliance purposes.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A NetSuite account with Administrator access
  * NetSuite REST Web Services enabled
  * Permissions to create integration records and access tokens in NetSuite



## Configure NetSuite API access

To enable log collection via the SuiteQL REST API, you must enable REST Web Services, create an integration record, and generate Token-Based Authentication (TBA) credentials in NetSuite.

### Enable required NetSuite features

  1. Sign in to your NetSuite account as an Administrator.
  2. Go to **Setup > Company > Enable Features**.
  3. Click the **SuiteCloud** tab.
  4. In the **SuiteScript** section, check the following boxes: 
     * **Client SuiteScript**
     * **Server SuiteScript**
  5. In the **SuiteTalk (Web Services)** section, check the following box: 
     * **REST Web Services**
  6. In the **Manage Authentication** section, check the **Token-Based Authentication** box.
  7. Click **I Agree** on the SuiteCloud Terms of Service page.
  8. Click **Save**.



### Create an integration record

  1. In NetSuite, go to **Setup > Integration > Manage Integrations > New**.
  2. In the **Name** field, enter `Google SecOps Integration`.
  3. In the **Description** field, enter `Integration for Google Security Operations log collection`.
  4. In the **State** field, leave the default **Enabled** option selected.
  5. Click the **Authentication** tab.
  6. In the **Token-based Authentication** section, check the **Token-based Authentication** box.
  7. Leave the **TBA: Authorization Flow** box unchecked.
  8. Check the **TBA: ISSUETOKEN ENDPOINT** box.
  9. Click **Save**.
  10. On the confirmation page, copy and save the **Consumer Key/Client ID** and **Consumer Secret/Client Secret**.

**Note:** The Consumer Key and Consumer Secret are displayed only once. If you lose these credentials, you must regenerate them on the integration record page.



### Create a custom role for API access

  1. Go to **Setup > Users/Roles > Manage Roles > New**.
  2. In the **Name** field, enter `Google SecOps API Role`.
  3. In the **ID** field, enter `google_secops_api_role`.
  4. Click the **Permissions** subtab.
  5. Click the **Setup** subtab.
  6. Add the following permissions with **Full** access level: 
     * **Log in using Access Tokens**
     * **User Access Tokens**
     * **REST Web Services**
  7. Click the **Reports** subtab.
  8. Add the following permissions with **View** access level: 
     * **SuiteAnalytics Workbook**
  9. Click the **Lists** subtab.
  10. Add the following permissions with **View** access level: 
     * **Login Audit Trail**
  11. Click **Save**.



### Assign the role to a user

  1. Go to **Lists > Employees > Employees**.
  2. Select the user account that will be used for the integration (or create a new dedicated integration user).
  3. Click **Edit**.
  4. Click the **Access** tab.
  5. In the **Roles** section, click **Add**.
  6. Select **Google SecOps API Role** from the dropdown list.
  7. Click **Save**.



### Create an access token

  1. Sign in to NetSuite as the user assigned the Google SecOps API Role.
  2. Go to **Setup > Users/Roles > Access Tokens > New**.
  3. On the **Access Token** page: 
     * In the **Application Name** dropdown list, select **Google SecOps Integration**.
     * In the **User** dropdown list, select the user account assigned the Google SecOps API Role.
     * In the **Role** dropdown list, select **Google SecOps API Role**.
     * The **Token Name** field is automatically populated. You can modify it if preferred.
  4. Click **Save**.
  5. On the confirmation page, copy and save the **Token ID** and **Token Secret**.

**Note:** The Token ID and Token Secret are displayed only once. If you lose these credentials, you must create a new access token.



### Find your NetSuite Account ID

  1. In NetSuite, go to **Setup > Company > Company Information**.
  2. Locate the **Account ID** field (displayed below the **Time Zone** setting).
  3. Copy and save your Account ID (for example, `1234567` or `1234567_SB1` for sandbox accounts).



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to NetSuite with the user assigned the Google SecOps API Role.
  2. Go to **Setup > Users/Roles > View Login Audit Trail**.
  3. If you can see the Login Audit Trail page, the account has the required permissions.
  4. If you cannot see this option, contact your NetSuite administrator to grant the **Login Audit Trail** permission under the **Lists** subtab.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        ACCOUNT_ID="your-account-id"
        
        # Replace underscores with hyphens in the account ID for the URL
        # For example: 1234567_SB1 becomes 1234567-sb1
        URL_ACCOUNT_ID=$(echo "$ACCOUNT_ID" | tr '_' '-' | tr '[:upper:]' '[:lower:]')
        
        CONSUMER_KEY="your-consumer-key"
        CONSUMER_SECRET="your-consumer-secret"
        TOKEN_ID="your-token-id"
        TOKEN_SECRET="your-token-secret"
        
        # Test SuiteQL API access using OAuth 1.0 TBA
        # Note: This example requires the oauth1 CLI tool or Postman.
        # Use the following endpoint and headers to verify connectivity:
        # POST https://${URL_ACCOUNT_ID}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql?limit=5
        # Headers:
        #   Authorization: OAuth (with consumer key, token, HMAC-SHA256 signature)
        #   Content-Type: application/json
        #   Prefer: transient
        # Body: {"q": "SELECT id, date, status, user, emailaddress FROM LoginAudit ORDER BY date DESC"}
        




A successful response returns a JSON object containing LoginAudit records.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netsuite-audit-logs`)  
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
     * **Service account name** : Enter `netsuite-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect NetSuite audit logs`
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

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`netsuite-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`netsuite-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netsuite-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the NetSuite SuiteQL REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netsuite-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `netsuite-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `netsuite-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netsuite-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `netsuite-audit` | Prefix for log files  
`STATE_KEY` | `netsuite-audit/state.json` | State file path  
`NS_ACCOUNT_ID` | `1234567` | NetSuite Account ID  
`NS_CONSUMER_KEY` | `your-consumer-key` | Consumer Key from integration record  
`NS_CONSUMER_SECRET` | `your-consumer-secret` | Consumer Secret from integration record  
`NS_TOKEN_ID` | `your-token-id` | Token ID from access token  
`NS_TOKEN_SECRET` | `your-token-secret` | Token Secret from access token  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per SuiteQL page  
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
    import hashlib
    import hmac
    import base64
    import time
    import secrets
    import urllib.parse
    from datetime import datetime, timezone, timedelta
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
      timeout=urllib3.Timeout(connect=10.0, read=60.0),
      retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netsuite-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'netsuite-audit/state.json')
    NS_ACCOUNT_ID = os.environ.get('NS_ACCOUNT_ID')
    NS_CONSUMER_KEY = os.environ.get('NS_CONSUMER_KEY')
    NS_CONSUMER_SECRET = os.environ.get('NS_CONSUMER_SECRET')
    NS_TOKEN_ID = os.environ.get('NS_TOKEN_ID')
    NS_TOKEN_SECRET = os.environ.get('NS_TOKEN_SECRET')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def get_netsuite_base_url(account_id):
      """Build the NetSuite REST API base URL from the account ID."""
      url_account = account_id.replace('_', '-').lower()
      return f"https://{url_account}.suitetalk.api.netsuite.com"
    
    def generate_oauth_header(method, url, account_id, consumer_key,
      consumer_secret, token_id, token_secret):
      """Generate OAuth 1.0 Authorization header using HMAC-SHA256."""
      timestamp = str(int(time.time()))
      nonce = secrets.token_hex(16)
    
      # Parse URL to separate base URL and query parameters
      parsed = urllib.parse.urlparse(url)
      base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
      query_params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    
      # Build parameter string (OAuth params + query params)
      params = {
        'oauth_consumer_key': consumer_key,
        'oauth_token': token_id,
        'oauth_nonce': nonce,
        'oauth_timestamp': timestamp,
        'oauth_signature_method': 'HMAC-SHA256',
        'oauth_version': '1.0',
      }
      for key, values in query_params.items():
        params[key] = values[0]
    
      # Sort parameters and create parameter string
      sorted_params = sorted(params.items())
      param_string = '&'.join(
        f"{urllib.parse.quote(k, safe='')}={urllib.parse.quote(v, safe='')}"
        for k, v in sorted_params
      )
    
      # Create signature base string
      signature_base = (
        f"{method.upper()}&"
        f"{urllib.parse.quote(base_url, safe='')}&"
        f"{urllib.parse.quote(param_string, safe='')}"
      )
    
      # Create signing key
      signing_key = (
        f"{urllib.parse.quote(consumer_secret, safe='')}&"
        f"{urllib.parse.quote(token_secret, safe='')}"
      )
    
      # Generate HMAC-SHA256 signature
      signature = base64.b64encode(
        hmac.new(
          signing_key.encode('utf-8'),
          signature_base.encode('utf-8'),
          hashlib.sha256
        ).digest()
      ).decode('utf-8')
    
      # Build realm from account ID
      realm = account_id.replace('-', '_').upper()
    
      # Build Authorization header
      auth_header = (
        f'OAuth realm="{realm}",'
        f'oauth_consumer_key="{consumer_key}",'
        f'oauth_token="{token_id}",'
        f'oauth_nonce="{nonce}",'
        f'oauth_timestamp="{timestamp}",'
        f'oauth_signature_method="HMAC-SHA256",'
        f'oauth_version="1.0",'
        f'oauth_signature="{urllib.parse.quote(signature, safe="")}"'
      )
      return auth_header
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch NetSuite
      LoginAudit logs via SuiteQL and write to GCS.
      """
      if not all([GCS_BUCKET, NS_ACCOUNT_ID, NS_CONSUMER_KEY,
        NS_CONSUMER_SECRET, NS_TOKEN_ID, NS_TOKEN_SECRET]):
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
            print(f"Warning: Could not parse last_event_time: {e}")
            last_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        records, newest_time = fetch_login_audit(last_time, now)
    
        if not records:
          print("No new log records found.")
          save_state(bucket, now.isoformat())
          return
    
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/netsuite_audit_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join(
          [json.dumps(r, ensure_ascii=False, default=str) for r in records]
        ) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        if newest_time:
          save_state(bucket, newest_time)
        else:
          save_state(bucket, now.isoformat())
    
        print(f"Successfully processed {len(records)} records")
    
      except Exception as e:
        print(f'Error processing logs: {str(e)}')
        raise
    
    def fetch_login_audit(start_time, end_time):
      """
      Fetch LoginAudit records from NetSuite SuiteQL API with pagination.
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      base_url = get_netsuite_base_url(NS_ACCOUNT_ID)
      suiteql_endpoint = f"{base_url}/services/rest/query/v1/suiteql"
    
      start_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
      end_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    
      query = (
        "SELECT id, date, status, user, role, emailaddress, "
        "ipaddress, useragent, detail, requesturi, "
        "oauthaccesstokenname, oauthappname "
        "FROM LoginAudit "
        f"WHERE date BETWEEN TO_DATE('{start_str}', 'YYYY-MM-DD HH24:MI:SS') "
        f"AND TO_DATE('{end_str}', 'YYYY-MM-DD HH24:MI:SS') "
        "ORDER BY date ASC"
      )
    
      records = []
      newest_time = None
      offset = 0
      backoff = 1.0
    
      while True:
        if len(records) >= MAX_RECORDS:
          print(f"Reached max_records limit ({MAX_RECORDS})")
          break
    
        remaining = min(PAGE_SIZE, MAX_RECORDS - len(records))
        url = f"{suiteql_endpoint}?limit={remaining}&offset={offset}"
    
        auth_header = generate_oauth_header(
          'POST', url, NS_ACCOUNT_ID, NS_CONSUMER_KEY,
          NS_CONSUMER_SECRET, NS_TOKEN_ID, NS_TOKEN_SECRET
        )
    
        headers = {
          'Authorization': auth_header,
          'Content-Type': 'application/json',
          'Prefer': 'transient',
          'User-Agent': 'GoogleSecOps-NetSuiteCollector/1.0',
        }
    
        body = json.dumps({'q': query}).encode('utf-8')
    
        try:
          response = http.request('POST', url, headers=headers, body=body)
    
          if response.status == 429:
            retry_after = int(
              response.headers.get('Retry-After', str(int(backoff)))
            )
            print(f"Rate limited (429). Retrying after {retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 60.0)
            continue
    
          backoff = 1.0
    
          if response.status != 200:
            print(f"HTTP Error: {response.status}")
            response_text = response.data.decode('utf-8')
            print(f"Response body: {response_text}")
            return records, newest_time
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('items', [])
    
          if not page_results:
            print("No more results (empty page)")
            break
    
          page_num = (offset // PAGE_SIZE) + 1
          print(f"Page {page_num}: Retrieved {len(page_results)} records")
          records.extend(page_results)
    
          for event in page_results:
            try:
              event_time = event.get('date')
              if event_time:
                if newest_time is None or event_time > newest_time:
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          has_more = data.get('hasMore', False)
          if not has_more:
            print("Reached last page (hasMore=false)")
            break
    
          offset += len(page_results)
    
        except Exception as e:
          print(f"Error fetching logs: {e}")
          return records, newest_time
    
      print(f"Retrieved {len(records)} total records")
      return records, newest_time
    
    def load_state(bucket):
      """Load state from GCS."""
      try:
        blob = bucket.blob(STATE_KEY)
        if blob.exists():
          return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
      except Exception as e:
        print(f"Warning: Could not load state: {e}")
      return {}
    
    def save_state(bucket, last_event_time_iso):
      """Save the last event timestamp to GCS state file."""
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

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `netsuite-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `netsuite-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`netsuite-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `netsuite-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X records
         Wrote X records to gs://netsuite-audit-logs/netsuite-audit/netsuite_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `netsuite-audit-logs`.

  10. Navigate to the `netsuite-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the OAuth credentials (`NS_CONSUMER_KEY`, `NS_CONSUMER_SECRET`, `NS_TOKEN_ID`, `NS_TOKEN_SECRET`) and `NS_ACCOUNT_ID` environment variables are correct
  * **HTTP 403** : Verify the NetSuite role has the required permissions (REST Web Services, Login Audit Trail, SuiteAnalytics Workbook)
  * **HTTP 429** : Rate limiting — the function will automatically retry with exponential backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `NetSuite Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Oracle NetSuite - NetSuite Applications Suite** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://netsuite-audit-logs/netsuite-audit/
           

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

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `netsuite-audit-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## NetSuite API rate limits

NetSuite API has the following concurrency and rate limits:

Limit Type | Default Value | Notes  
---|---|---  
**Concurrent requests** | 15 requests | Applies to combined SOAP and REST API requests per account  
**SuiteQL query results** | 100,000 rows maximum | Maximum rows returned per SuiteQL query  
**Objects per request** | 1,000 objects maximum | Maximum objects returned per API request  
  
The Cloud Run function automatically handles rate limiting with exponential backoff. If you encounter persistent rate limit errors (HTTP 429), contact NetSuite support to increase your API limits or adjust the Cloud Scheduler frequency.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
user | extensions.auth.type | Type of authentication mechanism used  
date | metadata.event_timestamp | Timestamp when the event occurred  
event_type | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
security_result | security_result | Details about the security result of the event  
oauthaccesstokenname | security_result.about.resource.attribute.labels | Key-value labels describing attributes of the resource involved in the security result  
secchallenge | security_result.about.resource.attribute.labels |   
status | security_result.summary | Summary description of the security result  
oauthappname | target.application | Name of the target application  
useragent | target.application |   
ipaddress | target.ip | IP address of the target  
requesturi | target.url | URL of the target resource  
emailaddress | target.user.email_addresses | Email addresses associated with the target user  
role | target.user.role_name | Role name assigned to the target user  
user | target.user.userid | Unique identifier for the target user  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/net-suite-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
