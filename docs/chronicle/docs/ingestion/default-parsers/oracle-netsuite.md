---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite/
title: Collect Oracle NetSuite logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:45.067498+00:00
---

# Collect Oracle NetSuite logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-netsuite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle NetSuite logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Oracle NetSuite logs to Google Security Operations using Cloud Storage V2.

Oracle NetSuite is a cloud-based enterprise resource planning (ERP) platform that provides comprehensive business management capabilities including financial management, CRM, ecommerce, and inventory management. NetSuite generates audit logs for user logins, system changes, and API activity that can be queried through the SuiteQL REST API and ingested into Google SecOps for security monitoring and compliance.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to your Oracle NetSuite account
  * REST Web Services and OAuth 2.0 features enabled in your NetSuite account
  * Your NetSuite account ID (found at **Setup > Company > Company Information**)



## Enable required NetSuite features

  1. Sign in to your **NetSuite account** as an Administrator.
  2. Go to **Setup > Company > Enable Features**.
  3. Click the **SuiteCloud** subtab.
  4. In the **SuiteTalk (Web Services)** section, select the following box: 
     * **REST Web Services**
  5. In the **Manage Authentication** section, select the following box: 
     * **OAuth 2.0**
  6. Click **Save**.



## Configure Oracle NetSuite OAuth 2.0 credentials

To enable the Cloud Run function to retrieve audit logs from NetSuite, you need to create an integration record with OAuth 2.0 client credentials authentication.

### Create an integration record

  1. Sign in to your **NetSuite account** as an Administrator.
  2. Go to **Setup > Integration > Manage Integrations > New**.
  3. In the **Name** field, enter `Google SecOps Integration`.
  4. In the **Description** field, enter `Integration with Google SecOps for audit log ingestion`.
  5. In the **State** field, select **Enabled**.
  6. Click the **Authentication** subtab.
  7. In the **OAuth 2.0** section, configure the following: 
     * Select **Client Credentials (Machine to Machine) Grant**
     * Select **REST Web Services**
  8. Clear all boxes in the **Token-based Authentication** section.
  9. Click **Save**.



### Record OAuth 2.0 credentials

After saving the integration record, NetSuite displays your OAuth 2.0 credentials:

  * **Client ID** : Your unique client identifier
  * **Client Secret** : Your API secret key

**Note:** Copy and save both the Client ID and Client Secret immediately. NetSuite displays these values only once. If you lose them, you must reset the credentials on the integration record.



### Generate a certificate for OAuth 2.0 client credentials

The OAuth 2.0 client credentials flow requires a certificate for JWT signing. Generate an ECDSA certificate using OpenSSL:

  1. On a machine with OpenSSL installed, run the following command to generate a private key and certificate:
         
         openssl req -new -x509 -newkey ec \
             -pkeyopt ec_paramgen_curve:prime256v1 \
             -pkeyopt ec_param_enc:named_curve \
             -nodes -days 730 \
             -out public.pem -keyout private.pem
         

  2. When prompted, enter the certificate subject fields (Country, State, Organization, and so on). For **Common Name** , enter `Google SecOps Integration`.

  3. The command generates two files:

     * `private.pem`: Private key (keep this secure; used for JWT signing in the Cloud Run function)
     * `public.pem`: Public certificate (upload to NetSuite)
**Note:** NetSuite supports ECDSA (ES256, ES512) and RSA-PSS (PS256) certificates. This document uses ECDSA with the prime256v1 curve (ES256). Certificates have a maximum validity of 2 years.



### Create OAuth 2.0 client credential mapping

  1. In NetSuite, go to **Setup > Integration > Manage Authentication > OAuth 2.0 Client Credentials (M2M) Setup**.
  2. Click **Create New**.
  3. In the dialog, configure the following: 
     * **Entity** : Select the employee or user that will be associated with API requests.
     * **Role** : Select a role that has the **Log in using OAuth 2.0 Access Tokens** permission (see Required permissions). Without this permission, the role does not appear in this list.
     * **Application** : Select `Google SecOps Integration`.
  4. Click **Choose File** and upload the `public.pem` certificate file.
  5. Click **Save**.
  6. After saving, note the **Certificate ID** value displayed in the mapping list. This value is used as the `kid` (Key ID) in the JWT header.



### Required permissions

The role assigned to the OAuth 2.0 mapping must have the following permissions:

Permission | Access Level | Purpose  
---|---|---  
**Log in using OAuth 2.0 Access Tokens** | Full | Allow the role to use OAuth 2.0 token login  
**REST Web Services** | Full | Execute REST API requests  
**Login Audit Trail** | Full | Access login audit trail data  
**SuiteAnalytics Workbook** | View | Access analytics data via SuiteQL  
**System Notes for Analytics and REST** | View | Query SystemNote records through SuiteQL  
**Note:** Without **System Notes for Analytics and REST** , a SuiteQL query on `SystemNote` returns only the system notes for changes the integration user made themselves. The request still succeeds, so nothing reports an error while the change records never arrive.

### Create a custom role for the integration

  1. Go to **Setup > Users/Roles > Manage Roles > New**.
  2. In the **Name** field, enter `Google SecOps Integration Role`.
  3. Click the **Permissions** subtab.
  4. Click the **Setup** sub-subtab.
  5. Add the following permissions: 
     * **Log in using OAuth 2.0 Access Tokens** : Set to **Full**
     * **REST Web Services** : Set to **Full**
     * **Login Audit Trail** : Set to **Full**
  6. Click the **Reports** sub-subtab.
  7. Add the following permission: 
     * **SuiteAnalytics Workbook** : Set to **View**
  8. Click the **Lists** sub-subtab.
  9. Add the following permission: 
     * **System Notes for Analytics and REST** : Set to **View**
  10. Click **Save**.



### Verify permissions

To verify the role has the required permissions, do the following:

  1. Sign in to NetSuite.
  2. Go to **Setup > Users/Roles > Manage Roles**.
  3. Find the `Google SecOps Integration Role` and click **Edit**.
  4. Verify the permissions listed in Required permissions are present on the **Permissions** subtab.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        ACCOUNT_ID="your-account-id"
        CLIENT_ID="your-client-id"
        CERTIFICATE_ID="your-certificate-id"
        PRIVATE_KEY_FILE="private.pem"
        
        # Generate JWT (requires Python 3 with PyJWT and cryptography)
        pip install PyJWT cryptography
        
        TOKEN=$(python3 -c "
        import jwt, time, json
        with open('${PRIVATE_KEY_FILE}', 'r') as f:
            key = f.read()
        now = int(time.time())
        payload = {
            'iss': '${CLIENT_ID}',
            'scope': ['restlets', 'rest_webservices'],
            'aud': 'https://${ACCOUNT_ID}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token',
            'iat': now,
            'exp': now + 3600
        }
        print(jwt.encode(payload, key, algorithm='ES256', headers={'kid': '${CERTIFICATE_ID}', 'typ': 'JWT'}))
        ")
        
        # Obtain access token
        ACCESS_TOKEN=$(curl -s -X POST \
            "https://${ACCOUNT_ID}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -d "grant_type=client_credentials&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=${TOKEN}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test SuiteQL query against the login audit trail
        curl -s -X POST \
            "https://${ACCOUNT_ID}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql?limit=5" \
            -H "Authorization: Bearer ${ACCESS_TOKEN}" \
            -H "Content-Type: application/json" \
            -H "Prefer: transient" \
            -d '{"q": "SELECT Date, Status, User, IPAddress FROM LoginAudit ORDER BY Date DESC"}' \
            | python3 -m json.tool
        
        # Test SuiteQL query against system notes
        curl -s -X POST \
            "https://${ACCOUNT_ID}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql?limit=5" \
            -H "Authorization: Bearer ${ACCESS_TOKEN}" \
            -H "Content-Type: application/json" \
            -H "Prefer: transient" \
            -d '{"q": "SELECT Date, RecordID, Field, BUILTIN.DF(SystemNote.Name) AS EmployeeName FROM SystemNote ORDER BY Date DESC"}' \
            | python3 -m json.tool
        




A successful response returns a JSON object with an `items` array containing login audit records.

The second query must return recent system notes, including changes made by users other than the integration user. An empty `items` array, or one that lists only the integration user in `EmployeeName`, means the role is missing the **System Notes for Analytics and REST** permission.

## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
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




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to a Cloud Storage bucket and be invoked by Pub/Sub.

### Create service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `netsuite-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Oracle NetSuite audit logs`
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

  * **Storage Object Admin** : Write logs to the Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on the Cloud Storage bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`netsuite-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`netsuite-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netsuite-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit logs from the Oracle NetSuite SuiteQL REST API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netsuite-audit-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `netsuite-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Select **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `netsuite-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netsuite-audit-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `netsuite-audit` | Prefix for log files  
`STATE_KEY` | `netsuite-audit-state.json` | State path, outside the log prefix  
`NS_ACCOUNT_ID` | `123456` | NetSuite account ID  
`NS_CLIENT_ID` | `your-client-id` | OAuth 2.0 Client ID  
`NS_CERTIFICATE_ID` | `your-certificate-id` | Certificate ID (kid) from M2M mapping  
`NS_PRIVATE_KEY` | `-----BEGIN EC PRIVATE KEY-----...` | ECDSA private key contents  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `1000` | Records per SuiteQL page (max 1000)  
`MAX_RECORDS` | `50000` | Max records per run  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
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




### Add the function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           import urllib.parse
           import jwt
           import time
           import hashlib
           from datetime import datetime, timezone, timedelta
           
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=10.0, read=60.0),
               retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netsuite-audit')
           STATE_KEY = os.environ.get('STATE_KEY', 'netsuite-audit-state.json')
           NS_ACCOUNT_ID = os.environ.get('NS_ACCOUNT_ID')
           NS_CLIENT_ID = os.environ.get('NS_CLIENT_ID')
           NS_CERTIFICATE_ID = os.environ.get('NS_CERTIFICATE_ID')
           NS_PRIVATE_KEY = os.environ.get('NS_PRIVATE_KEY', '').replace('\\n', '\n')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '50000'))
           
           # Neither SuiteQL query selects a unique row identifier, so the content hash
           # is the only identity available.
           ID_FIELDS = ()
           
           def event_keys(event):
               """Return every identity this event can be recognised by."""
               keys = {'sha256:' + hashlib.sha256(
                   json.dumps(event, sort_keys=True, ensure_ascii=False).encode('utf-8')
               ).hexdigest()}
               for field in ID_FIELDS:
                   value = event.get(field)
                   if value:
                       keys.add(f'{field}:{[value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value)}')
               return keys
           
           @functions_framework.cloud_event
           def main(cloud_event):
               if not all([GCS_BUCKET, NS_ACCOUNT_ID, NS_CLIENT_ID, NS_CERTIFICATE_ID, NS_PRIVATE_KEY]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                   state = load_state(bucket)
                   seen_keys = load_seen(bucket)
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
           
                   access_token = get_access_token()
           
                   login_audits = fetch_login_audit(access_token, last_time, now)
                   system_notes = fetch_system_notes(access_token, last_time, now)
           
                   all_records = []
                   for record in login_audits:
                       record['_netsuite_record_type'] = 'login_audit'
                       all_records.append(record)
                   for record in system_notes:
                       record['_netsuite_record_type'] = 'system_note'
                       all_records.append(record)
           
                   if not all_records:
                       print("No new records found.")
                       save_state(bucket, now.isoformat())
                       return
           
                   # Drop the rows the overlap window re-read from the previous run
                   fresh = [r for r in all_records if not (event_keys(r) & seen_keys)]
                   all_keys = set()
                   for record in all_records:
                       all_keys |= event_keys(record)
           
                   if not fresh:
                       print("No new records found. Watermark left unchanged.")
                       return
           
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/netsuite_audit_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                       [json.dumps(r, ensure_ascii=False, default=str) for r in fresh]
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Remember every fetched row so the next overlap window skips it
                   save_seen(bucket, all_keys)
           
                   newest = find_newest_time(login_audits, system_notes)
                   save_state(bucket, newest if newest else now.isoformat())
           
                   print(f"Successfully processed {len(fresh)} records "
                           f"(login_audit: {len(login_audits)}, system_note: {len(system_notes)})")
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def get_access_token():
               token_url = (
                   f"https://{NS_ACCOUNT_ID}.suitetalk.api.netsuite.com"
                   f"/services/rest/auth/oauth2/v1/token"
               )
           
               now = int(time.time())
               payload = {
                   'iss': NS_CLIENT_ID,
                   'scope': ['restlets', 'rest_webservices'],
                   'aud': token_url,
                   'iat': now,
                   'exp': now + 3600,
               }
           
               client_assertion = jwt.encode(
                   payload,
                   NS_PRIVATE_KEY,
                   algorithm='ES256',
                   headers={'kid': NS_CERTIFICATE_ID, 'typ': 'JWT'},
               )
           
               body = urllib.parse.urlencode({
                   'grant_type': 'client_credentials',
                   'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
                   'client_assertion': client_assertion,
               }).encode('utf-8')
           
               response = http.request(
                   'POST', token_url,
                   body=body,
                   headers={'Content-Type': 'application/x-www-form-urlencoded'},
               )
           
               if response.status != 200:
                   raise Exception(
                       f"Token request failed: {response.status} - "
                       f"{response.data.decode('utf-8')}"
                   )
           
               data = json.loads(response.data.decode('utf-8'))
               access_token = data.get('access_token')
               if not access_token:
                   raise Exception("No access_token in token response")
           
               print("Successfully obtained NetSuite OAuth 2.0 access token")
               return access_token
           
           def run_suiteql(access_token, query, page_size=1000, max_records=50000):
               base_url = (
                   f"https://{NS_ACCOUNT_ID}.suitetalk.api.netsuite.com"
                   f"/services/rest/query/v1/suiteql"
               )
           
               headers = {
                   'Authorization': f'Bearer {access_token}',
                   'Content-Type': 'application/json',
                   'Prefer': 'transient',
               }
           
               all_items = []
               offset = 0
               backoff = 1.0
           
               while True:
                   if len(all_items) >= max_records:
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   url = f"{base_url}?limit={page_size}&offset={offset}"
                   body = json.dumps({'q': query}).encode('utf-8')
           
                   try:
                       response = http.request('POST', url, body=body, headers=headers)
           
                       if response.status == 429:
                           retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                           print(f"Rate limited (429). Retrying after {retry_after}s...")
                           time.sleep(retry_after)
                           backoff = min(backoff * 2, 60.0)
                           continue
           
                       backoff = 1.0
           
                       if response.status != 200:
                           print(f"SuiteQL error: {response.status} - "
                                   f"{response.data.decode('utf-8')}")
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
                       items = data.get('items', [])
           
                       if not items:
                           break
           
                       all_items.extend(items)
                       page_num = (offset // page_size) + 1
                       print(f"Page {page_num}: Retrieved {len(items)} records "
                               f"(total: {len(all_items)})")
           
                       has_more = data.get('hasMore', False)
                       if not has_more:
                           break
           
                       offset += len(items)
           
                   except Exception as e:
                       print(f"Error executing SuiteQL query: {e}")
                       break
           
               return all_items
           
           def fetch_login_audit(access_token, start_time, end_time):
               start_str = start_time.strftime('%m/%d/%Y %H:%M:%S')
               end_str = end_time.strftime('%m/%d/%Y %H:%M:%S')
           
               query = (
                   "SELECT "
                   "LoginAudit.Date, "
                   "LoginAudit.Status, "
                   "LoginAudit.User, "
                   "BUILTIN.DF(LoginAudit.User) AS Username, "
                   "LoginAudit.EmailAddress, "
                   "LoginAudit.Role, "
                   "BUILTIN.DF(LoginAudit.Role) AS Rolename, "
                   "LoginAudit.IPAddress, "
                   "LoginAudit.UserAgent, "
                   "LoginAudit.Detail, "
                   "LoginAudit.oAuthAppName, "
                   "LoginAudit.oAuthAccessTokenName, "
                   "LoginAudit.requestUri "
                   "FROM LoginAudit "
                   f"WHERE LoginAudit.Date >= TO_DATE('{start_str}', 'MM/DD/YYYY HH24:MI:SS') "
                   f"AND LoginAudit.Date <= TO_DATE('{end_str}', 'MM/DD/YYYY HH24:MI:SS') "
                   "ORDER BY LoginAudit.Date ASC"
               )
           
               print("Fetching LoginAudit records...")
               return run_suiteql(access_token, query, PAGE_SIZE, MAX_RECORDS)
           
           def fetch_system_notes(access_token, start_time, end_time):
               start_str = start_time.strftime('%m/%d/%Y %H:%M:%S')
               end_str = end_time.strftime('%m/%d/%Y %H:%M:%S')
           
               query = (
                   "SELECT "
                   "SystemNote.Date, "
                   "SystemNote.RecordTypeID, "
                   "BUILTIN.DF(SystemNote.RecordTypeID) AS RecordType, "
                   "SystemNote.RecordID, "
                   "SystemNote.Field, "
                   "SystemNote.OldValue, "
                   "SystemNote.NewValue, "
                   "SystemNote.Name AS EmployeeID, "
                   "BUILTIN.DF(SystemNote.Name) AS EmployeeName, "
                   "SystemNote.Role, "
                   "BUILTIN.DF(SystemNote.Role) AS RoleName, "
                   "SystemNote.Context, "
                   "BUILTIN.DF(SystemNote.Context) AS ContextName "
                   "FROM SystemNote "
                   f"WHERE SystemNote.Date >= TO_DATE('{start_str}', 'MM/DD/YYYY HH24:MI:SS') "
                   f"AND SystemNote.Date <= TO_DATE('{end_str}', 'MM/DD/YYYY HH24:MI:SS') "
                   "ORDER BY SystemNote.Date ASC"
               )
           
               print("Fetching SystemNote records...")
               return run_suiteql(access_token, query, PAGE_SIZE, MAX_RECORDS)
           
           def find_newest_time(login_audits, system_notes):
               newest = None
               for r in login_audits:
                   t = r.get('date')
                   if t and (newest is None or t > newest):
                       newest = t
               for r in system_notes:
                   t = r.get('date')
                   if t and (newest is None or t > newest):
                       newest = t
               return newest
           
           def load_state(bucket):
               try:
                   blob = bucket.blob(STATE_KEY)
                   if blob.exists():
                       return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
               except Exception as e:
                   print(f"Warning: Could not load state: {e}")
                   raise
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
                   raise
           
           def load_seen(bucket):
               try:
                   blob = bucket.blob(STATE_KEY + '.seen')
                   if blob.exists():
                       return set(json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()))
               except Exception as e:
                   print(f"Warning: Could not load seen keys: {e}")
                   raise
               return set()
           
           def save_seen(bucket, keys):
               try:
                   blob = bucket.blob(STATE_KEY + '.seen')
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(sorted(keys)),
                       content_type='application/json'
                   )
                   print(f"Saved {len(keys)} event keys for deduplication")
               except Exception as e:
                   print(f"Warning: Could not save seen keys: {e}")
                   raise
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           PyJWT[crypto]>=2.8.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

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
Every 15 minutes | `*/15 * * * *` | High-volume, low-latency  
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
         Successfully obtained NetSuite OAuth 2.0 access token
         Fetching LoginAudit records...
         Page 1: Retrieved X records (total: X)
         Fetching SystemNote records...
         Page 1: Retrieved X records (total: X)
         Wrote X records to gs://netsuite-audit-logs/netsuite-audit/netsuite_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records (login_audit: X, system_note: X)
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click `netsuite-audit-logs`.

  10. Navigate to the `netsuite-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs, or a record type is missing from the output:

  * **HTTP 401** : Verify the `NS_CLIENT_ID`, `NS_CERTIFICATE_ID`, and `NS_PRIVATE_KEY` environment variables are correct.
  * **HTTP 403** : Verify the NetSuite role has sign in permissions using OAuth 2.0 Access Tokens (Full), REST Web Services (Full), and Login Audit Trail (Full) permissions.
  * **No`system_note` records in the output**: The role is missing the System Notes for Analytics and REST (View) permission. The SuiteQL query still succeeds and returns only the notes for changes the integration user made itself, so no error reaches the logs.
  * **HTTP 429** : Rate limiting - the function will automatically retry with exponential backoff.
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration.



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `NetSuite Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Oracle NetSuite** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click `netsuite-audit-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



## Complete the Google SecOps feed configuration

  1. Return to the Google SecOps feed creation wizard.
  2. Click **Next**.
  3. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://netsuite-audit-logs/netsuite-audit/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  4. Click **Next**.

  5. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## NetSuite API rate limits

The NetSuite REST API has the following governance limits:

Limit Type | Value  
---|---  
**Concurrency limit** | 10 concurrent requests per integration  
**SuiteQL query results per page** | 1,000 rows maximum  
**SuiteQL total results** | 100,000 rows per query  
  
The Cloud Run function automatically handles rate limiting with exponential backoff.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Login_Audit_Trail_Access_Token_Name_label` | `additional.fields` | Merged  
`Login_Audit_Trail_Detail_label` | `additional.fields` | Merged  
`additional_preview` | `additional.fields` | Merged  
`detail_label` | `additional.fields` | Merged  
`role_change_label` | `additional.fields` | Merged  
`sec_challenge_label` | `additional.fields` | Merged  
`oauthaccesstokenname` | `extensions.auth.auth_details` | Directly mapped  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`column7` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`Role_Change_Date` | `metadata.event_timestamp` | Parsed as `M/d/yyyy h:mm a`  
`date` | `metadata.event_timestamp` | Parsed as `M/d/yyyy h:mm:ss a`  
`result.Login_Audit_Trail_Date` | `metadata.event_timestamp` | Parsed as `LDAP`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`column1` | `metadata.product_event_type` | Directly mapped  
`log_type` | `metadata.product_event_type` | Directly mapped  
`useragent` | `network.http.parsed_user_agent` | Directly mapped  
`Login_Audit_Trail_User_Agent` | `network.http.user_agent` | Directly mapped  
`result.Login_Audit_Trail_User_Agent` | `network.http.user_agent` | Directly mapped  
`useragent` | `network.http.user_agent` | Directly mapped  
`Login_Audit_Trail_Application` | `principal.application` | Directly mapped  
`column10` | `principal.application` | Directly mapped  
`oauthappname` | `principal.application` | Directly mapped  
`result.host` | `principal.asset.hostname` | Directly mapped  
`column3` | `principal.asset.ip` | Merged  
`ipaddress` | `principal.asset.ip` | Merged  
`result.Login_Audit_Trail_IP_Address` | `principal.asset.ip` | Directly mapped  
`src_ip` | `principal.asset.ip` | Merged  
`result.host` | `principal.hostname` | Directly mapped  
`column3` | `principal.ip` | Merged  
`ipaddress` | `principal.ip` | Merged  
`result.Login_Audit_Trail_IP_Address` | `principal.ip` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`Login_Audit_Trail_Role_label` | `principal.user.attribute.labels` | Merged  
`login_audits_role_label` | `principal.user.attribute.labels` | Merged  
`supervisor_label` | `principal.user.attribute.labels` | Merged  
`role` | `principal.user.attribute.roles` | Merged  
`Email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `Email`  
`column2` | `principal.user.email_addresses` | Merged  
`emailaddress` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `emailaddress`  
`result.Login_Audit_Trail_Email_Address` | `principal.user.email_addresses` | Merged  
`Job_Title` | `principal.user.title` | Directly mapped  
`Name` | `principal.user.user_display_name` | Directly mapped  
`Login_Audit_Trail_User` | `principal.user.userid` | Directly mapped  
`result.Login_Audit_Trail_User` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`Login_Audit_Trail_Security_Challenge_label` | `security_result.about.resource.attribute.labels` | Merged  
`security_result_action` | `security_result.action` | Merged  
`Login_Audit_Trail_Status` | `security_result.summary` | Directly mapped  
`result.Login_Audit_Trail_Status` | `security_result.summary` | Directly mapped  
`api_type_label` | `target.resource.attribute.labels` | Merged  
`Login_Audit_Trail_Request_URI` | `target.url` | Directly mapped  
`result.Login_Audit_Trail_Request_URI` | `target.url` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-netsuite-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
