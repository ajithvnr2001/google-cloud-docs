---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-identity-and-auth-data/
title: Collect SAP Cloud Identity Services logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:52:36.762845+00:00
---

# Collect SAP Cloud Identity Services logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-identity-and-auth-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP Cloud Identity Services logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SAP Cloud Identity Services logs to Google Security Operations using Google Cloud Storage V2.

SAP Cloud Identity Services is a cloud-based identity and access management (IAM) solution that provides authentication, single sign-on (SSO), and user provisioning for SAP and third-party applications. The Audit Log Service in SAP BTP records authentication events, data changes, and configuration changes for Identity Authentication tenants. These audit logs can be retrieved through the SAP BTP Audit Log Retrieval API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An SAP BTP global account with a Cloud Foundry subaccount
  * An SAP Cloud Identity Services tenant (Identity Authentication)
  * A user with the Space Developer role in the SAP BTP Cloud Foundry subaccount
  * The Audit Log Management service entitlement added to the subaccount



## Create an auditlog-management service instance

Create a service instance of the `auditlog-management` service in your SAP BTP Cloud Foundry subaccount to obtain the credentials required to access the Audit Log Retrieval API.

### Configure the service entitlement

  1. Sign in to the [SAP BTP cockpit](https://cockpit.btp.cloud.sap/).
  2. Navigate to your subaccount.
  3. Go to **Entitlements**.
  4. Click **Edit > Add Service Plans**.
  5. Search for **Audit Log Management** and select the **default** checkbox.
  6. Click **Add 1 service plan**.
  7. Click **Save**.



### Create the service instance and key

  1. Install the [Cloud Foundry CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html) if not already installed.
  2. Log in to the Cloud Foundry environment:
         
         cf login -a <CF_API_ENDPOINT> -o <ORG> -s <SPACE> -u <USER>
         

  3. Create the `auditlog-management` service instance with mTLS authentication (recommended):
         
         cf create-service auditlog-management default sap-ias-auditlog \
           -c '{"xs-security": {"xsappname": "sap-ias-auditlog", "oauth2-configuration": {"credential-types": ["x509"], "grant-types": ["client_credentials"]}}}'
         

  4. Create a service key with an X.509 certificate:
         
         cf create-service-key sap-ias-auditlog sap-ias-auditlog-key \
           -c '{"xsuaa": {"credential-type": "x509", "x509": {"key-length": 2048, "validity": 365, "validity-type": "DAYS"}}}'
         

**Note:** For production use, set a validity period appropriate for your security policy. Recreate the service key before it expires.
  5. Retrieve the service key:
         
         cf service-key sap-ias-auditlog sap-ias-auditlog-key
         

  6. From the service key output, note the following values:

     * **uaa.certurl** : The OAuth2 token endpoint URL (for example, `https://yoursubaccount.authentication.eu10.hana.ondemand.com`)
     * **uaa.clientid** : The OAuth2 client ID
     * **uaa.certificate** : The X.509 certificate (PEM format)
     * **uaa.key** : The RSA private key (PEM format)
     * **url** : The Audit Log Retrieval API base URL (for example, `https://auditlog-management.cfapps.eu10.hana.ondemand.com`)
  7. Extract and save the certificate and private key to PEM files:
         
         cf service-key sap-ias-auditlog sap-ias-auditlog-key | sed '/Getting key/d' | jq --raw-output .credentials.uaa.certificate > certificate.pem
         cf service-key sap-ias-auditlog sap-ias-auditlog-key | sed '/Getting key/d' | jq --raw-output .credentials.uaa.key > private-key.pem
         




### Configure Identity Authentication audit log delivery

  1. Sign in to the **administration console for SAP Cloud Identity Services** at `https://<tenant-id>.accounts.ondemand.com/admin`.
  2. Go to the **Audit and Change Logs** tile.
  3. Choose the **Audit Logs** tab (or **Cloud Foundry** tab if your tenant is on the SAP infrastructure).
  4. Click **+Add**.
  5. Provide the following configuration details:

     * **Tenant ID** : Enter the tenant ID of your Cloud Foundry subaccount
     * **Region** : Select the SAP BTP Cloud Foundry region that maps to your Identity Authentication region
     * **Subdomain** (optional): Enter the subaccount subdomain to enable a direct link to the Audit Log Viewer
**Note:** The subaccount region must match your Identity Authentication tenant region. You can find the region in the header of the administration console.
  6. Click **Save**.




### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Extract values from the service key
        CERT_URL="<uaa.certurl value>"
        CLIENT_ID="<uaa.clientid value>"
        API_URL="<url value>"
        
        # Get OAuth access token using mTLS
        TOKEN=$(curl -s --cert certificate.pem --key private-key.pem \
          -X POST "${CERT_URL}/oauth/token?grant_type=client_credentials&client_id=${CLIENT_ID}" \
          | python3 -c "import sys,json; print(json.load(sys.stdin).get('access_token',''))")
        
        echo "Token: ${TOKEN:0:50}..."
        
        # Test audit log retrieval
        curl -v -H "Authorization: Bearer ${TOKEN}" \
          "${API_URL}/auditlog/v2/auditlogrecords?time_from=$(date -u -v-1d '+%Y-%m-%dT%H:%M:%S')&time_to=$(date -u '+%Y-%m-%dT%H:%M:%S')"
        

**Note:** The OAuth access token is valid for 1 hour. The API returns HTTP 429 when rate limits are exceeded (4-8 requests per second depending on region).



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sap-ias-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sap-ias-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect SAP Cloud Identity Services audit logs`
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
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `sap-ias-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sap-ias-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit logs from the SAP BTP Audit Log Retrieval API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sap-ias-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sap-ias-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sap-ias-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sap-ias-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `sap-ias` | Prefix for log files  
`STATE_KEY` | `sap-ias/state.json` | State file path  
`SAP_CERT_URL` | `https://sub.authentication.eu10.hana.ondemand.com` | OAuth2 token endpoint (uaa.certurl)  
`SAP_CLIENT_ID` | `sb-sap-ias-auditlog!t12345` | OAuth2 client ID (uaa.clientid)  
`SAP_CERTIFICATE` | PEM certificate content | X.509 certificate (uaa.certificate)  
`SAP_PRIVATE_KEY` | PEM private key content | RSA private key (uaa.key)  
`SAP_API_URL` | `https://auditlog-management.cfapps.eu10.hana.ondemand.com` | Audit Log Retrieval API base URL  
`MAX_RECORDS` | `10000` | Max records per run  
`LOOKBACK_HOURS` | `2` | Initial lookback period  
**Note:** For the `SAP_CERTIFICATE` and `SAP_PRIVATE_KEY` variables, paste the full PEM content including the `-----BEGIN CERTIFICATE-----` and `-----BEGIN RSA PRIVATE KEY-----` headers. Alternatively, use Secret Manager to store these values securely.
  10. Scroll down in the **Variables & Secrets** section to **Requests** :

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

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           import tempfile
           from datetime import datetime, timezone, timedelta
           import time
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sap-ias').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           SAP_CERT_URL = os.environ.get('SAP_CERT_URL', '').rstrip('/')
           SAP_CLIENT_ID = os.environ.get('SAP_CLIENT_ID')
           SAP_CERTIFICATE = os.environ.get('SAP_CERTIFICATE', '')
           SAP_PRIVATE_KEY = os.environ.get('SAP_PRIVATE_KEY', '')
           SAP_API_URL = os.environ.get('SAP_API_URL', '').rstrip('/')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '2'))
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if not value:
               return None
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             try:
               return datetime.fromisoformat(value)
             except Exception:
               return None
           
           def write_pem_to_tempfile(pem_content, suffix='.pem'):
             """Write PEM content to a temporary file and return the path."""
             tmp = tempfile.NamedTemporaryFile(
               mode='w', suffix=suffix, delete=False
             )
             tmp.write(pem_content)
             tmp.flush()
             tmp.close()
             return tmp.name
           
           def get_oauth_token(cert_file, key_file):
             """Get OAuth2 access token using mTLS client credentials."""
             http = urllib3.PoolManager(
               cert_file=cert_file,
               key_file=key_file,
               timeout=urllib3.Timeout(connect=10.0, read=30.0),
               retries=False,
             )
           
             token_url = (
               f"{SAP_CERT_URL}/oauth/token"
               f"?grant_type=client_credentials"
               f"&client_id={SAP_CLIENT_ID}"
             )
           
             response = http.request('POST', token_url)
           
             if response.status != 200:
               raise Exception(
                 f"Failed to get OAuth token: HTTP {response.status} - "
                 f"{response.data.decode('utf-8')}"
               )
           
             token_data = json.loads(response.data.decode('utf-8'))
             return token_data['access_token']
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch
             SAP Cloud Identity Services audit logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([
               GCS_BUCKET, SAP_CERT_URL, SAP_CLIENT_ID,
               SAP_CERTIFICATE, SAP_PRIVATE_KEY, SAP_API_URL
             ]):
               print('Error: Missing required environment variables')
               return
           
             cert_file = None
             key_file = None
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Write certificate and key to temp files for mTLS
               cert_file = write_pem_to_tempfile(SAP_CERTIFICATE)
               key_file = write_pem_to_tempfile(SAP_PRIVATE_KEY)
           
               # Get OAuth2 access token
               access_token = get_oauth_token(cert_file, key_file)
               print("Successfully obtained OAuth2 access token")
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               # Determine time window
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                   # Overlap by 2 minutes to catch delayed events
                   if last_time:
                     last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               time_from = last_time.strftime('%Y-%m-%dT%H:%M:%S')
               time_to = now.strftime('%Y-%m-%dT%H:%M:%S')
           
               print(f"Fetching audit logs from {time_from} to {time_to}")
           
               # Fetch audit logs
               records, newest_event_time = fetch_audit_logs(
                 access_token=access_token,
                 time_from=time_from,
                 time_to=time_to,
               )
           
               if not records:
                 print("No new audit log records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 ndjson, content_type='application/x-ndjson'
               )
           
               print(
                 f"Wrote {len(records)} records to "
                 f"gs://{GCS_BUCKET}/{object_key}"
               )
           
               # Update state
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing audit logs: {str(e)}')
               raise
             finally:
               # Clean up temp files
               for f in [cert_file, key_file]:
                 if f:
                   try:
                     os.unlink(f)
                   except OSError:
                     pass
           
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
           
           def fetch_audit_logs(access_token, time_from, time_to):
             """
             Fetch audit logs from SAP BTP Audit Log Retrieval API
             with handle-based pagination.
           
             Args:
               access_token: OAuth2 bearer token
               time_from: Start time in YYYY-MM-DDTHH:MM:SS format (UTC)
               time_to: End time in YYYY-MM-DDTHH:MM:SS format (UTC)
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
             )
           
             headers = {
               'Authorization': f'Bearer {access_token}',
               'Accept': 'application/json',
             }
           
             endpoint = f"{SAP_API_URL}/auditlog/v2/auditlogrecords"
           
             records = []
             newest_time = None
             page_num = 0
             handle = None
             backoff = 1.0
           
             while True:
               if len(records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               # Build URL with parameters
               if handle:
                 url = f"{endpoint}?handle={handle}"
               else:
                 url = (
                   f"{endpoint}"
                   f"?time_from={time_from}"
                   f"&time_to={time_to}"
                 )
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get(
                       'Retry-After', str(int(backoff))
                     )
                   )
                   print(
                     f"Rate limited (429). "
                     f"Retrying after {retry_after}s..."
                   )
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status == 204:
                   print("No more audit log records (HTTP 204)")
                   break
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return [], None
           
                 page_results = json.loads(
                   response.data.decode('utf-8')
                 )
           
                 if not page_results:
                   print("No more results (empty response)")
                   break
           
                 # Handle single record vs list
                 if isinstance(page_results, dict):
                   page_results = [page_results]
           
                 page_num += 1
                 print(
                   f"Page {page_num}: "
                   f"Retrieved {len(page_results)} events"
                 )
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_time = event.get('time')
                     if event_time:
                       if newest_time is None:
                         newest_time = event_time
                       else:
                         current_dt = parse_datetime(event_time)
                         newest_dt = parse_datetime(newest_time)
                         if (current_dt and newest_dt
                             and current_dt > newest_dt):
                           newest_time = event_time
                   except Exception as e:
                     print(
                       f"Warning: Could not parse event time: {e}"
                     )
           
                 # Check for pagination handle in response header
                 paging_header = response.headers.get('Paging', '')
                 if paging_header and 'handle=' in paging_header:
                   handle = paging_header.split('handle=')[1].strip()
                   print(f"Next page handle: {handle[:50]}...")
                 else:
                   print("No more pages (no paging handle)")
                   break
           
               except Exception as e:
                 print(f"Error fetching audit logs: {e}")
                 return [], None
           
             print(
               f"Retrieved {len(records)} total records "
               f"from {page_num} pages"
             )
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. The SAP BTP Audit Log Retrieval API rate limits vary by region (4-8 requests per second). The function handles rate limiting with exponential backoff.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `sap-ias-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sap-ias-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every hour | `0 * * * *` | Standard (recommended)  
Every 2 hours | `0 */2 * * *` | Lower volume  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `sap-ias-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Successfully obtained OAuth2 access token
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS to YYYY-MM-DDTHH:MM:SS
         Page 1: Retrieved X events
         Wrote X records to gs://sap-ias-audit-logs/sap-ias/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `sap-ias/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **Failed to get OAuth token: HTTP 401** : Check the certificate and private key in environment variables. Verify they match the service key. Ensure the service key has not expired.
  * **HTTP 401 on audit log retrieval** : The OAuth access token may have expired. The function obtains a fresh token on each invocation.
  * **HTTP 403** : Verify the auditlog-management service instance is correctly created and the service key is valid.
  * **HTTP 429** : Rate limiting - the function automatically retries with exponential backoff. Consider increasing the schedule interval if this occurs frequently.
  * **HTTP 204** : No audit log records found for the specified time window. This is normal for tenants with low activity.
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration.



## Configure a feed in Google SecOps to ingest SAP Cloud Identity Services logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SAP Cloud Identity Services Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **SAP Identity and Authentication Data** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sap-ias-audit-logs/sap-ias/
           

       * Replace: 
         * `sap-ias-audit-logs`: Your GCS bucket name.
         * `sap-ias`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click your bucket name.
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
`childAgr` | `about.group.group_display_name` | Directly mapped  
`field1` | `additional.fields` | Merged  
`has_principal_hostname` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_CHANGE_PASSWORD`, `true` → `GROUP_MODIFICATION`  
`has_target_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`field1` | `principal.asset.attribute.labels` | Merged  
`key` | `principal.asset.attribute.labels` | Mapped: `"systemid", "partype"` → `field1`  
`hostname` | `principal.hostname` | Directly mapped  
`repid` | `principal.process.file.full_path` | Directly mapped  
`aname` | `principal.user.userid` | Directly mapped  
`changeUsr` | `principal.user.userid` | Directly mapped  
`modbe` | `principal.user.userid` | Directly mapped  
`modifier` | `principal.user.userid` | Directly mapped  
`uname` | `principal.user.userid` | Directly mapped  
`field1` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `"direct", "uflag","securityPolicy"` → `field1`  
`agrName` | `target.group.group_display_name` | Directly mapped  
`field1` | `target.resource.attribute.labels` | Merged  
`key` | `target.resource.attribute.labels` | Mapped: `"field","struct","mandt","parentAgr","type","fromDat","toDat","ustyp","langu","iana...  
`tcode` | `target.resource.name` | Directly mapped  
`class` | `target.user.group_identifiers` | Merged  
`profile` | `target.user.group_identifiers` | Merged  
`bname` | `target.user.userid` | Directly mapped  
`username` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `SAP_IDENTITY_AND_AUTH_DATA`  
N/A | `metadata.vendor_name` | Constant: `SAP`  
`changeUsr` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`uname` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`aname` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`modifier` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`modbe` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`bname` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`username` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`agrName` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`childAgr` | `event.idm.read_only_udm.about.group.group_display_name` | Mapped from changelog  
`tcode` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`class` | `event.idm.read_only_udm.target.user.group_identifiers` | Mapped from changelog  
`profile` | `event.idm.read_only_udm.target.user.group_identifiers` | Mapped from changelog  
`repid` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`field` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`struct` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`mandt` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`parentAgr` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`type` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`fromDat` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`toDat` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`ustyp` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`langu` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`ianatzonecode` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`trdat` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`ltime` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pwdchgdate` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pwdlgndate` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pwdlockdate` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`pwdsaltedhash` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`systemid` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`partype` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`direct` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`uflag` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`securityPolicy` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-identity-and-auth-data-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
