---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-fusion/
title: Collect Oracle Fusion Cloud Applications logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:44.118179+00:00
---

# Collect Oracle Fusion Cloud Applications logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-fusion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle Fusion Cloud Applications logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Oracle Fusion Cloud Applications logs to Google Security Operations using Google Cloud Storage V2.

**Note:** This method collects sign-in activity through the Oracle Fusion **Sign In - Sign Out Audit REST API** (`/oam/services/rest/access/api/v1/audit/events`), which the `ORACLE_FUSION` parser reads directly. It records **Credential Validation** and **Logout** events and retains only the **last 7 days** of data. Important: Oracle has **deprecated** this API on **Fusion 25B and later** (after the Fusion Identity Upgrade); on those releases, sign-in activity must be ingested from **OCI Audit Logs** instead (see MOS KB181606). Confirm your Fusion release before deploying.

Oracle Fusion Cloud Applications is Oracle's comprehensive suite of cloud-based enterprise resource planning (ERP), human capital management (HCM), supply chain management (SCM), and customer experience (CX) applications. The platform provides extensive audit logging capabilities through REST APIs, capturing user authentication events, transaction changes, administrative actions, and security-related activities across all Fusion modules. A Cloud Run function queries the Oracle Fusion Audit REST API to retrieve this data and writes it to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to Oracle Fusion Cloud Applications
  * Administrator access to the Oracle Cloud Infrastructure (OCI) Identity and Access Management (IAM) identity domain associated with your Fusion Applications instance
  * A Fusion Applications user account with the **FND_VIEW_AUDIT_HISTORY_PRIV** privilege or **Fusion Apps Administrator** role



## Configure Oracle Fusion Cloud Applications OAuth 2.0 API access

To enable Google SecOps to retrieve audit logs, you need to create an OAuth 2.0 confidential application using the Client Credentials grant type and configure the client ID as a user in Fusion Applications.

### Create OAuth 2.0 confidential application

  1. Sign in to the **Oracle Cloud Infrastructure Console** with your identity domain administrator credentials.
  2. In the menu bar, click **Identity & Security > Domains**.
  3. Select your compartment.
  4. Click the identity domain associated with your Fusion Applications instance.
  5. In the menu bar, click **Integrated applications > Add application**.
  6. On the **Add application** dialog box, select **Confidential Application** and click **Launch workflow**.
  7. On the **Add Confidential Application** page, in the **Name** field, enter a descriptive name (for example, `Chronicle SIEM Integration`).
  8. Click **Next**.
  9. In the **Configure OAuth** section, select the **Configure this application as a client now** checkbox.
  10. In the **Authorization** section, select the **Client credentials** checkbox.
  11. Clear all other grant type checkboxes.
  12. Scroll down to the **Token issuance policy** section.
  13. In the **Authorized resources** section, select **Specific**.
  14. Select the **Add resources** checkbox.
  15. In the **Resources** subsection, click **Add scope**.
  16. On the **Add scope** dialog box, locate and select the **Fusion Applications** resource application.
  17. Select the appropriate scope for your Fusion Applications instance.

**Note:** The scope is typically in the format `urn:opc:resource:fusion:<podname>:<scope>`. To find the exact scope, navigate to **Integrated applications** , search for **Fusion Applications** , click the application, go to **OAuth configuration > Configure application APIs that need to be OAuth Protected > Scopes**, and note the scope value.
  18. Click **Add**.

  19. Click **Next**.

  20. On the **Web tier policy** page, accept the default settings and click **Finish**.

  21. A confirmation dialog box appears displaying the auto-generated **Client ID** and **Client Secret** values.

  22. Copy and save both the **Client ID** and **Client Secret** immediately.

**Note:** The client secret cannot be retrieved after closing this dialog. Store these credentials securely.
  23. Click **Close**.

  24. On the application details page, click **Activate**.

  25. On the confirmation dialog, click **Activate application**.




### Record identity domain URL

  1. In the Oracle Cloud Infrastructure Console, while viewing your identity domain, note the **Domain URL** displayed at the top of the page.
  2. The domain URL is in the format `https://idcs-<idcs-id>.identity.oraclecloud.com`.
  3. Save this URL for later use.

**Note:** You can also retrieve the token endpoint URL from `https://idcs-<idcs-id>.identity.oraclecloud.com/.well-known/idcs-configuration`.



### Create user account for OAuth client

In Client Credentials flows, API calls are invoked in the context of the application itself, not a user. You must create a user account in Fusion Applications with the same username as the OAuth client ID.

  1. Sign in to **Oracle Fusion Cloud Applications**.
  2. Click the **Navigator** icon in the top-left corner.
  3. Under **Tools** , select **Security Console**.
  4. Click **Users**.
  5. Click **Add User Account**.
  6. In the **User Information** section, in the **User Name** field, enter the **Client ID** value from the OAuth application.

**Note:** The username must exactly match the Client ID. Any discrepancy will cause authentication failures.
  7. Complete the remaining required fields:

     * **First Name** : Enter `Google SecOps` or a descriptive name
     * **Last Name** : Enter `Integration` or a descriptive name
     * **Email** : Enter a valid email address (for example, `chronicle-integration@yourcompany.com`)
  8. Click **Add Role**.

  9. Search for and add the following role:

     * **Fusion Apps Administrator**
**Note:** Alternatively, you can create a custom role with the **FND_VIEW_AUDIT_HISTORY_PRIV** privilege for least-privilege access. The Fusion Apps Administrator role includes this privilege along with broader permissions.
  10. Click **Save and Close**.

**Note:** User creation may take a few minutes to complete. Wait for the user to be fully provisioned before proceeding.



### Record Fusion Applications base URL

  1. While signed in to Oracle Fusion Cloud Applications, note the URL in your browser's address bar.
  2. The base URL is in the format `https://<instance>.<service>.<datacenter>.oraclecloud.com`.
  3. Extract the hostname portion only (for example, `mycompany.fa.us2.oraclecloud.com`).
  4. Save this hostname for later use.

**Note:** Do not include `https://` or any path components. Use only the hostname.



### Verify permissions

To verify the OAuth client has the required permissions:

  1. Sign in to **Oracle Fusion Cloud Applications**.
  2. Click the **Navigator** icon > **Tools** > **Security Console**.
  3. Click **Users** and search for the user account matching the Client ID.
  4. Verify the user has the **Fusion Apps Administrator** role or the **FND_VIEW_AUDIT_HISTORY_PRIV** privilege assigned.
  5. If you cannot locate the user or the privilege is missing, contact your Fusion Applications administrator to grant the required role.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        IDENTITY_DOMAIN_URL="https://idcs-xxxxxxxxxxxx.identity.oraclecloud.com"
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        FUSION_HOST="mycompany.fa.us2.oraclecloud.com"
        OAUTH_SCOPE="urn:opc:resource:fusion:podname:boss/"
        FUSION_USERNAME="svc_secops_audit"
        FUSION_PASSWORD="your-user-password"
        
        # Step 1: Obtain OAuth access token (only needed if you use bearer auth instead of Basic)
        TOKEN=$(curl -s -u "${CLIENT_ID}:${CLIENT_SECRET}" \
            -H "Content-Type: application/x-www-form-urlencoded;charset=UTF-8" \
            -X POST "${IDENTITY_DOMAIN_URL}/oauth2/v1/token" \
            -d "grant_type=client_credentials&scope=${OAUTH_SCOPE}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        echo "Token obtained: ${TOKEN:0:20}..."
        
        # Step 2: Test the Sign In - Sign Out Audit REST API (last 7 days of data)
        # The API is documented with HTTP Basic auth (-u "<user>:<password>").
        # If your tenant accepts the bearer token instead, replace -u with
        # -H "Authorization: Bearer ${TOKEN}".
        curl -s -X GET "https://${FUSION_HOST}/oam/services/rest/access/api/v1/audit/events/1?fromDate=$(date -u -v-7d '+%Y-%m-%dT%H:%M:%S.000Z')&toDate=$(date -u '+%Y-%m-%dT%H:%M:%S.000Z')&pageSize=5" \
            -u "${FUSION_USERNAME}:${FUSION_PASSWORD}" \
            -H "Accept: application/json" \
            | python3 -m json.tool
        




A successful response returns a JSON object with an `Events.eventData` array of sign-in and sign-out records (each with fields such as `eventID`, `userID`, `ipAddress`, `type`, `status`, and `accessTime`).

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `oracle-fusion-audit-logs`)  
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
     * **Service account name** : Enter `oracle-fusion-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Oracle Fusion Cloud Applications audit logs`
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
  2. Click on your bucket name (`oracle-fusion-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`oracle-fusion-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `oracle-fusion-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit data from the Oracle Fusion Cloud Applications Audit REST API and write it to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `oracle-fusion-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `oracle-fusion-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `oracle-fusion-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `oracle-fusion-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `oracle-fusion-audit` | Prefix for log files  
`STATE_KEY` | `oracle-fusion-audit/state.json` | State file path  
`FUSION_HOST` | `mycompany.fa.us2.oraclecloud.com` | Fusion Applications hostname  
`IDENTITY_DOMAIN_URL` | `https://idcs-xxxx.identity.oraclecloud.com` | Identity domain URL  
`CLIENT_ID` | `your-client-id` | OAuth 2.0 client ID  
`CLIENT_SECRET` | `your-client-secret` | OAuth 2.0 client secret  
`OAUTH_SCOPE` | `urn:opc:resource:fusion:podname:boss/` | OAuth scope for Fusion Applications  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `100` | Records per page  
`FUSION_USERNAME` | `svc_secops_audit` | Optional. User for HTTP Basic auth to the Sign In/Sign Out Audit API. If empty, the OAuth 2.0 bearer token is used  
`FUSION_PASSWORD` | `your-user-password` | Optional. Password for `FUSION_USERNAME` (store as a Secret Manager secret)  
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
    import base64
    import urllib.parse
    
    http = urllib3.PoolManager(
      timeout=urllib3.Timeout(connect=10.0, read=60.0),
      retries=False,
    )
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'oracle-fusion-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'oracle-fusion-audit/state.json')
    FUSION_HOST = os.environ.get('FUSION_HOST', '').strip()
    IDENTITY_DOMAIN_URL = os.environ.get('IDENTITY_DOMAIN_URL', '').rstrip('/')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    OAUTH_SCOPE = os.environ.get('OAUTH_SCOPE', '')
    # The Sign In - Sign Out Audit REST API is documented with HTTP Basic auth.
    # Set FUSION_USERNAME / FUSION_PASSWORD to use it; otherwise the function falls
    # back to the OAuth 2.0 bearer token configured above.
    FUSION_USERNAME = os.environ.get('FUSION_USERNAME', '')
    FUSION_PASSWORD = os.environ.get('FUSION_PASSWORD', '')
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    
    # Sign In - Sign Out Audit REST API. Returns {"Events": {"eventData": [...]}},
    # which the ORACLE_FUSION parser reads directly. Data is retained for 7 days.
    AUDIT_PATH = '/oam/services/rest/access/api/v1/audit/events'
    
    def get_oauth_token():
      token_url = f"{IDENTITY_DOMAIN_URL}/oauth2/v1/token"
      auth_b64 = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('utf-8')).decode('utf-8')
      body = f"grant_type=client_credentials&scope={urllib.parse.quote(OAUTH_SCOPE, safe='')}"
      try:
        response = http.request(
          'POST', token_url,
          body=body.encode('utf-8'),
          headers={
            'Authorization': f'Basic {auth_b64}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
          }
        )
        if response.status != 200:
          print(f"OAuth token request failed: {response.status} {response.data.decode('utf-8')}")
          return None
        return json.loads(response.data.decode('utf-8')).get('access_token')
      except Exception as e:
        print(f"Error obtaining OAuth token: {e}")
        return None
    
    def get_auth_header():
      """Use HTTP Basic auth when FUSION_USERNAME/PASSWORD are set, else OAuth bearer."""
      if FUSION_USERNAME and FUSION_PASSWORD:
        creds_b64 = base64.b64encode(f"{FUSION_USERNAME}:{FUSION_PASSWORD}".encode('utf-8')).decode('utf-8')
        return f"Basic {creds_b64}"
      token = get_oauth_token()
      return f"Bearer {token}" if token else None
    
    def fetch_signin_audit(auth_header, start_time, end_time):
      """Page through the Sign In - Sign Out Audit REST API.
    
      Returns (pages, newest_time). Each item in pages is a raw
      {"Events": {"eventData": [...]}} object, written unchanged for the parser.
      """
      base_url = f"https://{FUSION_HOST}{AUDIT_PATH}"
      from_date = start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
      to_date = end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    
      headers = {'Authorization': auth_header, 'Accept': 'application/json'}
    
      pages = []
      newest_time = None
      page_num = 1
      backoff = 1.0
    
      while True:
        query_string = urllib.parse.urlencode({
          'fromDate': from_date,
          'toDate': to_date,
          'pageSize': str(PAGE_SIZE),
        })
        # The page number is a path segment: /audit/events/{page}
        request_url = f"{base_url}/{page_num}?{query_string}"
    
        try:
          response = http.request('GET', request_url, headers=headers)
    
          if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
            print(f"Rate limited (429). Retrying after {retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 60.0)
            continue
          backoff = 1.0
    
          if response.status != 200:
            print(f"HTTP Error {response.status}: {response.data.decode('utf-8')}")
            break
    
          data = json.loads(response.data.decode('utf-8'))
          event_list = data.get('Events', {}).get('eventData', [])
          if isinstance(event_list, dict):
            event_list = [event_list]
    
          if not event_list:
            print(f"No more sign-in events (empty page {page_num})")
            break
    
          # Preserve the exact {"Events": {"eventData": [...]}} shape the parser
          # consumes; do not rename or flatten individual records.
          pages.append({'Events': {'eventData': event_list}})
          print(f"Page {page_num}: retrieved {len(event_list)} sign-in events")
    
          for event in event_list:
            access_time = event.get('accessTime')
            if access_time and (newest_time is None or access_time > newest_time):
              newest_time = access_time
    
          if len(event_list) < PAGE_SIZE:
            break
          page_num += 1
    
        except Exception as e:
          print(f"Error fetching sign-in audit: {e}")
          break
    
      print(f"Retrieved {len(pages)} page(s) of sign-in audit events")
      return pages, newest_time
    
    @functions_framework.cloud_event
    def main(cloud_event):
      if not all([GCS_BUCKET, FUSION_HOST]):
        print('Error: Missing required environment variables (GCS_BUCKET, FUSION_HOST)')
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
            last_time = datetime.fromisoformat(last_val) - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: could not parse last_event_time: {e}")
            last_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        # The API retains only 7 days of data; never look back further.
        earliest = now - timedelta(days=7)
        if last_time < earliest:
          last_time = earliest
    
        print(f"Fetching sign-in audit from {last_time.isoformat()} to {now.isoformat()}")
    
        auth_header = get_auth_header()
        if not auth_header:
          print("Error: could not build authorization header")
          return
    
        pages, newest_time = fetch_signin_audit(auth_header, last_time, now)
    
        if not pages:
          print("No new sign-in audit events found.")
          save_state(bucket, now.isoformat())
          return
    
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/oracle_fusion_audit_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(p, ensure_ascii=False, default=str) for p in pages]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
        print(f"Wrote {len(pages)} page(s) to gs://{GCS_BUCKET}/{object_key}")
    
        save_state(bucket, newest_time if newest_time else now.isoformat())
        print("Successfully processed sign-in audit events")
    
      except Exception as e:
        print(f'Error processing logs: {str(e)}')
        raise
    
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
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state, indent=2), content_type='application/json')
        print(f"Saved state: last_event_time={last_event_time_iso}")
      except Exception as e:
        print(f"Warning: Could not save state: {e}")
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

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
**Name** | `oracle-fusion-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `oracle-fusion-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`oracle-fusion-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `oracle-fusion-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained OAuth access token
         Page 1: Retrieved X audit events
         Wrote X records to gs://oracle-fusion-audit-logs/oracle-fusion-audit/oracle_fusion_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `oracle-fusion-audit-logs`.

  10. Navigate to the `oracle-fusion-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `CLIENT_ID` and `CLIENT_SECRET` environment variables are correct and the OAuth application is activated
  * **HTTP 403** : Verify the Fusion Applications user (matching Client ID) has the **FND_VIEW_AUDIT_HISTORY_PRIV** privilege or **Fusion Apps Administrator** role
  * **HTTP 429** : Rate limiting -- the function will automatically retry with exponential backoff
  * **API status FAIL** : Verify the `FUSION_HOST` environment variable is correct and the Fusion Applications instance is accessible
  * **OAuth token error** : Verify the `IDENTITY_DOMAIN_URL` and `OAUTH_SCOPE` environment variables are correct



## Required API permissions

  * The OAuth client requires the following permissions:

Permission/Scope | Access Level | Purpose  
---|---|---  
**FND_VIEW_AUDIT_HISTORY_PRIV** | Read | Retrieve audit history data from Fusion Applications  
**Fusion Applications scope** | Application | Access Fusion Applications REST API resources  
**Note:** The Fusion Apps Administrator role includes the FND_VIEW_AUDIT_HISTORY_PRIV privilege. For production deployments, consider creating a custom role with only the FND_VIEW_AUDIT_HISTORY_PRIV privilege to follow the principle of least privilege.**Note:** The **Sign In - Sign Out Audit REST API** used by this function is documented with **HTTP Basic authentication** and requires the account to hold the sign-in-audit viewing privilege (confirm the exact privilege for your release in Oracle Support Doc ID 2661308.1). The `FND_VIEW_AUDIT_HISTORY_PRIV` privilege applies to the legacy transaction-audit API and may not be sufficient on its own.



## Regional endpoints

Oracle Fusion Cloud Applications uses different data center regions. The base URL format varies by region:

Region | Data Center Code | Example Hostname  
---|---|---  
**US West (Phoenix)** | us-phoenix-1 | `instance.fa.us-phoenix-1.oraclecloud.com`  
**US East (Ashburn)** | us-ashburn-1 | `instance.fa.us-ashburn-1.oraclecloud.com`  
**US Commercial 2** | us2 | `instance.fa.us2.oraclecloud.com`  
**EU West (Frankfurt)** | eu-frankfurt-1 | `instance.fa.eu-frankfurt-1.oraclecloud.com`  
**EU West (Amsterdam)** | eu-amsterdam-1 | `instance.fa.eu-amsterdam-1.oraclecloud.com`  
**UK South (London)** | uk-london-1 | `instance.fa.uk-london-1.oraclecloud.com`  
**Canada Southeast (Toronto)** | ca-toronto-1 | `instance.fa.ca-toronto-1.oraclecloud.com`  
**APAC Southeast (Sydney)** | ap-sydney-1 | `instance.fa.ap-sydney-1.oraclecloud.com`  
**APAC Northeast (Tokyo)** | ap-tokyo-1 | `instance.fa.ap-tokyo-1.oraclecloud.com`  
  
Use the hostname that corresponds to your Oracle Fusion Cloud Applications instance region. You can identify your region from the URL displayed when accessing your Fusion Applications environment.

## API rate limits

Oracle Fusion Cloud Applications Audit REST API has the following characteristics:

Limit Type | Value  
---|---  
**Token lifetime** | 3600 seconds (1 hour)  
**Audit history query range** | Maximum 1 month per request  
**Sign-in/sign-out audit retention** | 7 days  
**Transaction audit retention** | 30-365 days (varies by product)  
  
The Cloud Run function automatically handles OAuth token refresh, pagination, and query range chunking. The function splits time ranges exceeding one month into monthly chunks and handles token expiration with automatic re-authentication.
    
    
    Note: For sign-in and sign-out audit events, the retention period is limited to 7 days. Configure the scheduler to poll frequently to avoid data loss. Transaction audit retention varies by Fusion Applications product and configuration.
    

## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Oracle Fusion Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Oracle Fusion Cloud Applications** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://oracle-fusion-audit-logs/oracle-fusion-audit/
           

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
  2. Click on `oracle-fusion-audit-logs`.
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
type | extensions.auth.type | Authentication type  
type | metadata.event_type | Event type  
ipAddress | metadata.event_type |   
eventID | metadata.product_log_id | Product log ID  
attributeMap.attribute.value | network.http.user_agent | HTTP user agent  
ipAddress | principal.asset.ip | IP address of the asset associated with the principal  
ipAddress | principal.ip | IP address of the principal  
userID.userDN | principal.user.attribute.labels | Labels for user attributes  
userID.userDN | principal.user.email_addresses | Email addresses of the user  
userID.loginID | principal.user.userid | User ID  
status | security_result.action | Security action  
oracleECID | target.user.userid | User ID of the target  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-fusion-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
