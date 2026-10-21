---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centrify-sso/
title: Collect Delinea Single Sign-On (SSO) (formerly Centrify) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:31:51.246831+00:00
---

# Collect Delinea Single Sign-On (SSO) (formerly Centrify) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/centrify-sso/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Delinea Single Sign-On (SSO) (formerly Centrify) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Delinea Single Sign-On (SSO) (formerly known as Centrify) logs to Google Security Operations using Google Cloud Storage. The parser extracts the logs, handling both JSON and syslog formats. It parses key-value pairs, timestamps, and other relevant fields, mapping them to the UDM model, with specific logic for handling login failures, user agents, severity levels, authentication mechanisms, and various event types. It prioritizes FailUserName over NormalizedUser for target email addresses in failure events.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Delinea (Centrify) SSO tenant



## Collect Delinea (Centrify) SSO credentials

### Create OAuth2 client application

  1. Sign in to the **Delinea Admin Portal**.
  2. Go to **Apps > Add Web Apps**.
  3. Click the **Custom** tab.
  4. Search for **OAuth2 Client** and click **Add**.
  5. Click **Yes** in the **Add Web App** dialog.
  6. Click **Close** in the **Add Web Apps** dialog.
  7. On the **Application Configuration** page, configure the following: 
     * **Settings** tab: 
       * **Application ID** : Enter a unique identifier (for example, `secops-oauth-client`).
       * **Application Name** : Enter a descriptive name (for example, `SecOps Data Export`).
       * **Application Description** : Enter description (for example, `OAuth client for exporting audit events to SecOps`).
     * **General Usage** section: 
       * **Client ID Type** : Select **Confidential**.
       * **Issued Client ID** : Copy and save this value.
       * **Issued Client Secret** : Copy and save this value.
     * **Tokens** tab: 
       * **Auth Methods** : Select **Client Creds**.
       * **Token Type** : Select **JwtRS256**.
     * **Scope** tab: 
       * Add scope `redrock/query` with the description `Query API Access`.
  8. Click **Save** to create the OAuth client.
  9. Copy and save in a secure location the following details: 
     * **Tenant URL** : Your Centrify tenant URL (for example, `https://yourtenant.my.centrify.com`).
     * **Client ID** : From step 7.
     * **Client Secret** : From step 7.
     * **OAuth Application ID** : From the Application Configuration.



### Verify permissions

To verify the OAuth client has the required permissions:

  1. Sign in to the **Delinea Admin Portal**.
  2. Go to **Settings > Resources > Roles**.
  3. Verify that the role assigned to the OAuth client includes **Report: Audit Events: View** permission.
  4. If the permission is missing, contact your Delinea administrator to grant the required permission.

**Note:** The OAuth client must have **Report: Audit Events: View** permission to access audit events via the Redrock Query API.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        TENANT_URL="https://yourtenant.my.centrify.com"
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        OAUTH_APP_ID="your-oauth-application-id"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${TENANT_URL}/oauth2/token/${OAUTH_APP_ID}" \
          -H "Authorization: Basic $(echo -n "${CLIENT_ID}:${CLIENT_SECRET}" | base64)" \
          -H "X-CENTRIFY-NATIVE-CLIENT: True" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&scope=redrock/query" | jq -r '.access_token')
        
        # Test query API access
        curl -v -X POST "${TENANT_URL}/Redrock/query" \
          -H "Authorization: Bearer ${TOKEN}" \
          -H "X-CENTRIFY-NATIVE-CLIENT: True" \
          -H "Content-Type: application/json" \
          -d '{"Script":"Select * from Event where WhenOccurred > datefunc('"'"'now'"'"', '"'"'-1'"'"') ORDER BY WhenOccurred ASC","args":{"PageNumber":1,"PageSize":10,"Limit":10,"Caching":-1}}'
        




If successful, you should see a JSON response with audit events. If you receive a 401 or 403 error, verify your credentials and permissions.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `delinea-centrify-logs-bucket`)  
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
     * **Service account name** : Enter `delinea-sso-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Delinea SSO logs`.
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
  2. Click your bucket name (for example, `delinea-centrify-logs-bucket`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `delinea-sso-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `delinea-sso-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Delinea SSO API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `delinea-sso-log-export`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic `delinea-sso-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `delinea-sso-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `delinea-centrify-logs-bucket` | GCS bucket name  
`GCS_PREFIX` | `centrify-sso-logs` | Prefix for log files  
`STATE_KEY` | `centrify-sso-logs/state.json` | State file path  
`TENANT_URL` | `https://yourtenant.my.centrify.com` | Delinea tenant URL  
`CLIENT_ID` | `your-client-id` | OAuth client ID  
`CLIENT_SECRET` | `your-client-secret` | OAuth client secret  
`OAUTH_APP_ID` | `your-oauth-application-id` | OAuth application ID  
`PAGE_SIZE` | `1000` | Records per page  
`MAX_PAGES` | `10` | Maximum pages to fetch  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab:

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

  1. Enter **main** in **Function entry point**
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
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Delinea Centrify SSO audit events and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'centrify-sso-logs')
        state_key = os.environ.get('STATE_KEY', 'centrify-sso-logs/state.json')
    
        # Centrify API credentials
        tenant_url = os.environ.get('TENANT_URL')
        client_id = os.environ.get('CLIENT_ID')
        client_secret = os.environ.get('CLIENT_SECRET')
        oauth_app_id = os.environ.get('OAUTH_APP_ID')
    
        # Optional parameters
        page_size = int(os.environ.get('PAGE_SIZE', '1000'))
        max_pages = int(os.environ.get('MAX_PAGES', '10'))
    
        if not all([bucket_name, tenant_url, client_id, client_secret, oauth_app_id]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (last processed timestamp)
            state = load_state(bucket, state_key)
            last_timestamp = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_timestamp')
    
            print(f'Processing logs since {last_timestamp if last_timestamp else "24 hours ago"}')
    
            # Get OAuth access token
            access_token = get_oauth_token(tenant_url, client_id, client_secret, oauth_app_id)
    
            # Fetch audit events
            events = fetch_audit_events(tenant_url, access_token, last_timestamp, page_size, max_pages)
    
            if events:
                # Write events to GCS
                current_timestamp = datetime.now(timezone.utc)
                blob_name = f"{prefix}/centrify-sso-events-{current_timestamp.strftime('%Y%m%d_%H%M%S')}.json"
                blob = bucket.blob(blob_name)
    
                # Convert to JSONL format (one JSON object per line)
                jsonl_content = '\n'.join([json.dumps(event, default=str) for event in events])
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(jsonl_content, content_type='application/x-ndjson')
    
                print(f'Wrote {len(events)} events to {blob_name}')
    
                # Update state with latest timestamp
                latest_timestamp = get_latest_event_timestamp(events)
                save_state(bucket, state_key, {'last_timestamp': latest_timestamp, 'updated_at': current_timestamp.isoformat() + 'Z'})
    
                print(f'Successfully processed {len(events)} events')
            else:
                print('No new events found')
    
        except Exception as e:
            print(f'Error processing Centrify SSO logs: {str(e)}')
            raise
    
    def get_oauth_token(tenant_url, client_id, client_secret, oauth_app_id):
        """Get OAuth access token using client credentials flow."""
        credentials = f"{client_id}:{client_secret}"
        basic_auth = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
        token_url = f"{tenant_url}/oauth2/token/{oauth_app_id}"
        headers = {
            'Authorization': f'Basic {basic_auth}',
            'X-CENTRIFY-NATIVE-CLIENT': 'True',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    
        data = {
            'grant_type': 'client_credentials',
            'scope': 'redrock/query'
        }
    
        response = http.request('POST', token_url, headers=headers, fields=data)
    
        if response.status != 200:
            raise Exception(f"OAuth token request failed: {response.status} {response.data.decode('utf-8')}")
    
        token_data = json.loads(response.data.decode('utf-8'))
        return token_data['access_token']
    
    def fetch_audit_events(tenant_url, access_token, last_timestamp, page_size, max_pages):
        """Fetch audit events from Centrify using the Redrock/query API with proper pagination."""
        query_url = f"{tenant_url}/Redrock/query"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'X-CENTRIFY-NATIVE-CLIENT': 'True',
            'Content-Type': 'application/json'
        }
    
        # Build SQL query with timestamp filter
        if last_timestamp:
            sql_query = f"Select * from Event where WhenOccurred > '{last_timestamp}' ORDER BY WhenOccurred ASC"
        else:
            # First run - get events from last 24 hours
            sql_query = "Select * from Event where WhenOccurred > datefunc('now', '-1') ORDER BY WhenOccurred ASC"
    
        all_events = []
        page_num = 1
        backoff = 1.0
    
        while page_num <= max_pages:
            payload = {
                "Script": sql_query,
                "args": {
                    "PageNumber": page_num,
                    "PageSize": page_size,
                    "Limit": page_size * max_pages,
                    "Caching": -1
                }
            }
    
            try:
                response = http.request('POST', query_url, headers=headers, body=json.dumps(payload))
    
                # Handle rate limiting with exponential backoff
                if response.status == 429:
                    retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                    print(f"Rate limited (429). Retrying after {retry_after}s...")
                    time.sleep(retry_after)
                    backoff = min(backoff * 2, 30.0)
                    continue
    
                backoff = 1.0
    
                if response.status != 200:
                    raise Exception(f"API query failed: {response.status} {response.data.decode('utf-8')}")
    
                response_data = json.loads(response.data.decode('utf-8'))
    
                if not response_data.get('success', False):
                    raise Exception(f"API query failed: {response_data.get('Message', 'Unknown error')}")
    
                # Parse the response
                result = response_data.get('Result', {})
                columns = {col['Name']: i for i, col in enumerate(result.get('Columns', []))}
                raw_results = result.get('Results', [])
    
                if not raw_results:
                    print(f"No more results on page {page_num}")
                    break
    
                print(f"Page {page_num}: Retrieved {len(raw_results)} events")
    
                for raw_event in raw_results:
                    event = {}
                    row_data = raw_event.get('Row', {})
    
                    # Map column names to values
                    for col_name, col_index in columns.items():
                        if col_name in row_data and row_data[col_name] is not None:
                            event[col_name] = row_data[col_name]
    
                    # Add metadata
                    event['_source'] = 'centrify_sso'
                    event['_collected_at'] = datetime.now(timezone.utc).isoformat() + 'Z'
    
                    all_events.append(event)
    
                # Check if we've reached the end
                if len(raw_results) < page_size:
                    print(f"Reached last page (page {page_num} returned {len(raw_results)} < {page_size})")
                    break
    
                page_num += 1
    
            except Exception as e:
                print(f"Error fetching page {page_num}: {e}")
                raise
    
        print(f"Retrieved {len(all_events)} total events from {page_num} pages")
        return all_events
    
    def get_latest_event_timestamp(events):
        """Get the latest timestamp from the events for state tracking."""
        if not events:
            return datetime.now(timezone.utc).isoformat() + 'Z'
    
        latest = None
        for event in events:
            when_occurred = event.get('WhenOccurred')
            if when_occurred:
                if latest is None or when_occurred > latest:
                    latest = when_occurred
    
        return latest or datetime.now(timezone.utc).isoformat() + 'Z'
    
    def load_state(bucket, key):
        """Load state from GCS."""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(state_data)
        except Exception as e:
            print(f'Warning: Could not load state: {str(e)}')
        return {}
    
    def save_state(bucket, key, state):
        """Save state to GCS."""
        try:
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click Send Feedback > Google SecOps Security Product Feedback on this page.
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
**Name** | `delinea-sso-log-export-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic `delinea-sso-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (for example, `delinea-sso-log-export-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `delinea-sso-log-export`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Processing logs since YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X events to centrify-sso-logs/centrify-sso-events_YYYYMMDD_HHMMSS.json
         Successfully processed X events
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (for example, `delinea-centrify-logs-bucket`).

  10. Navigate to the prefix folder `centrify-sso-logs/`.

  11. Verify that a new `.json` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables (CLIENT_ID, CLIENT_SECRET, OAUTH_APP_ID)
  * **HTTP 403** : Verify the OAuth client has **Report: Audit Events: View** permission
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration



## Configure a feed in Google SecOps to ingest Delinea (Centrify) SSO logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Delinea Centrify SSO logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Centrify** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
    
    gs://delinea-centrify-logs-bucket/centrify-sso-logs/
    

     * Replace:

       * `delinea-centrify-logs-bucket`: Your GCS bucket name.
       * `centrify-sso-logs`: Optional prefix/folder path where logs are stored (leave empty for root).

**Examples:**

     * Root bucket: `gs://company-logs/`
     * With prefix: `gs://company-logs/centrify-sso-logs/`
     * With subfolder: `gs://company-logs/delinea/sso/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `delinea-centrify-logs-bucket`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
AccountID | security_result.detection_fields.value | The value of AccountID from the raw log is assigned to a security_result.detection_fields object with key: Account ID.  
ApplicationName | target.application | The value of ApplicationName from the raw log is assigned to the target.application field.  
AuthorityFQDN | target.asset.network_domain | The value of AuthorityFQDN from the raw log is assigned to the target.asset.network_domain field.  
AuthorityID | target.asset.asset_id | The value of AuthorityID from the raw log is assigned to the target.asset.asset_id field, prefixed with "AuthorityID:".  
AzDeploymentId | security_result.detection_fields.value | The value of AzDeploymentId from the raw log is assigned to a security_result.detection_fields object with key: AzDeploymentId.  
AzRoleId | additional.fields.value.string_value | The value of AzRoleId from the raw log is assigned to an additional.fields object with key: AzRoleId.  
AzRoleName | target.user.attribute.roles.name | The value of AzRoleName from the raw log is assigned to the target.user.attribute.roles.name field.  
ComputerFQDN | principal.asset.network_domain | The value of ComputerFQDN from the raw log is assigned to the principal.asset.network_domain field.  
ComputerID | principal.asset.asset_id | The value of ComputerID from the raw log is assigned to the principal.asset.asset_id field, prefixed with "ComputerId:".  
ComputerName | about.hostname | The value of ComputerName from the raw log is assigned to the about.hostname field.  
CredentialId | security_result.detection_fields.value | The value of CredentialId from the raw log is assigned to a security_result.detection_fields object with key: Credential Id.  
DirectoryServiceName | security_result.detection_fields.value | The value of DirectoryServiceName from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Name.  
DirectoryServiceNameLocalized | security_result.detection_fields.value | The value of DirectoryServiceNameLocalized from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Name Localized.  
DirectoryServiceUuid | security_result.detection_fields.value | The value of DirectoryServiceUuid from the raw log is assigned to a security_result.detection_fields object with key: Directory Service Uuid.  
EventMessage | security_result.summary | The value of EventMessage from the raw log is assigned to the security_result.summary field.  
EventType | metadata.product_event_type | The value of EventType from the raw log is assigned to the metadata.product_event_type field. It is also used to determine the metadata.event_type.  
FailReason | security_result.summary | The value of FailReason from the raw log is assigned to the security_result.summary field when present.  
FailUserName | target.user.email_addresses | The value of FailUserName from the raw log is assigned to the target.user.email_addresses field when present.  
FromIPAddress | principal.ip | The value of FromIPAddress from the raw log is assigned to the principal.ip field.  
ID | security_result.detection_fields.value | The value of ID from the raw log is assigned to a security_result.detection_fields object with key: ID.  
InternalTrackingID | metadata.product_log_id | The value of InternalTrackingID from the raw log is assigned to the metadata.product_log_id field.  
JumpType | additional.fields.value.string_value | The value of JumpType from the raw log is assigned to an additional.fields object with key: Jump Type.  
NormalizedUser | target.user.email_addresses | The value of NormalizedUser from the raw log is assigned to the target.user.email_addresses field.  
OperationMode | additional.fields.value.string_value | The value of OperationMode from the raw log is assigned to an additional.fields object with key: Operation Mode.  
ProxyId | security_result.detection_fields.value | The value of ProxyId from the raw log is assigned to a security_result.detection_fields object with key: Proxy Id.  
RequestUserAgent | network.http.user_agent | The value of RequestUserAgent from the raw log is assigned to the network.http.user_agent field.  
SessionGuid | network.session_id | The value of SessionGuid from the raw log is assigned to the network.session_id field.  
Tenant | additional.fields.value.string_value | The value of Tenant from the raw log is assigned to an additional.fields object with key: Tenant.  
ThreadType | additional.fields.value.string_value | The value of ThreadType from the raw log is assigned to an additional.fields object with key: Thread Type.  
UserType | principal.user.attribute.roles.name | The value of UserType from the raw log is assigned to the principal.user.attribute.roles.name field.  
WhenOccurred | metadata.event_timestamp | The value of WhenOccurred from the raw log is parsed and assigned to the metadata.event_timestamp field. This field also populates the top-level timestamp field.  
Hardcoded value | metadata.product_name | "SSO".  
Hardcoded value | metadata.event_type | Determined by the EventType field. Defaults to STATUS_UPDATE if EventType is not present or doesn't match any specific criteria. Can be USER_LOGIN, USER_CREATION, USER_RESOURCE_ACCESS, USER_LOGOUT, or USER_CHANGE_PASSWORD.  
Hardcoded value | metadata.vendor_name | "CENTRIFY_SSO".  
Hardcoded value | metadata.product_version | "SSO".  
Hardcoded value | metadata.log_type | "Centrify".  
Extracted from message field | network.session_id | If message field contains a session ID, it is extracted and used. Otherwise defaults to "1".  
Extracted from host field | principal.hostname | Extracted from the host field if available, which comes from the syslog header.  
Extracted from pid field | principal.process.pid | Extracted from the pid field if available, which comes from the syslog header.  
UserGuid or extracted from message | target.user.userid | If UserGuid is present, its value is used. Otherwise, if message field contains a user ID, it is extracted and used.  
Determined by Level and FailReason | security_result.action | Set to "ALLOW" if Level is "Info", and "BLOCK" if FailReason is present.  
Determined by FailReason | security_result.category | Set to "AUTH_VIOLATION" if FailReason is present.  
Determined by Level field | security_result.severity | Determined by the Level field. Set to "INFORMATIONAL" if Level is "Info", "MEDIUM" if Level is "Warning", and "ERROR" if Level is "Error".  
`msg` | `metadata.description` | Mapped from changelog  
`UserGuid` | `principal.user.userid` | Mapped from changelog  
`ComputerName` | `principal.asset.hostname` | Mapped from changelog  
`TokenType` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/centrify-sso-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
