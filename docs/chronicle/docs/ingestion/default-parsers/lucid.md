---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid/
title: Collect Lucid audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:52.477548+00:00
---

# Collect Lucid audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lucid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Lucid audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Lucid audit logs to Google Security Operations using Google Cloud Storage V2.

Lucid Software provides a visual collaboration suite including Lucidchart, Lucidspark, and Lucidscale. The Audit Logs API, available exclusively to Enterprise Shield customers, captures security and compliance events across the organization, including account access, document activity, user management, admin actions, and team operations.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Lucid Enterprise Shield account with admin or account owner privileges
  * Access to the [Lucid Developer Portal](https://lucid.app/developer) with developer tools enabled



## Enable developer tools in Lucid

Before creating API credentials, you must have access to the Lucid Developer Portal. There are two ways to enable developer tools:

### Option 1: Enable via user settings

  1. Sign in to [lucid.app](https://lucid.app).
  2. Click your profile icon in the upper right corner.
  3. Select **Account Settings**.
  4. Check the **Enable developer tools** checkbox.

**Note:** This checkbox may be disabled by your Lucid admin. If it is disabled, use Option 2.



### Option 2: Enable via admin role assignment

  1. Sign in to [lucid.app](https://lucid.app) as an account owner or team admin.
  2. Navigate to the admin panel.
  3. Go to the **Users** section.
  4. Select the target user.
  5. Edit the user's roles and assign the **Developer** role.

**Note:** Assigning the developer role unlocks developer tools for that user, even if they have not enabled developer features in their user settings.



## Configure Lucid API access

To enable Google SecOps to retrieve audit logs, you need to create an OAuth 2.0 client and generate an account-level access token with the `account.audit.logs` scope.

### Create an OAuth 2.0 application and client

  1. Navigate to the [Lucid Developer Portal](https://lucid.app/developer).
  2. Click **Create Application**.
  3. Enter a name for your application (for example, `Chronicle SIEM Integration`).
  4. Click on the newly created application to access its settings.
  5. Navigate to the **OAuth 2.0** tab.
  6. Enter a name for your OAuth 2.0 client (for example, `Chronicle Audit Log Collector`).

**Note:** The OAuth 2.0 client name is publicly visible when users grant access and cannot be changed after creation.
  7. Click **Create OAuth 2.0 client**.




### Record the client credentials

After creating the OAuth 2.0 client, the portal displays your credentials:

  * **Client ID** : Your unique client identifier.
  * **Client Secret** : Your API secret key.



**Important** : Copy and save the client secret immediately. If the client secret is compromised, click the **Reset Client Secret** button on the OAuth 2.0 settings page. Resetting the secret immediately revokes access until the new secret is updated in your integration.

### Register a redirect URI

  1. On the OAuth 2.0 settings page, click **Add Redirect URI**.
  2. Enter the redirect URI for your integration. If using the Lucid-provided test redirect, enter:
         
         https://lucid.app/oauth2/clients/<CLIENT_ID>/redirect
         

Replace `<CLIENT_ID>` with your actual client ID.




### Obtain an account-level access token

The Audit Logs API requires an account token (not a user token). An account admin must authorize the OAuth 2.0 client to create a token on behalf of the account.

  1. Direct an account admin to the following authorization URL in a browser:
         
         https://lucid.app/oauth2/authorizeAccount?client_id=<CLIENT_ID>&redirect_uri=<REDIRECT_URI>&scope=account.audit.logs
         

Replace `<CLIENT_ID>` and `<REDIRECT_URI>` with your actual values.

  2. The admin reviews the requested permissions on the consent screen and clicks **Allow**.

  3. Lucid redirects to the redirect URI with an authorization `code` query parameter.

  4. Exchange the authorization code for an access token by making a POST request to the token endpoint:
         
         curl --request POST \
           --url https://api.lucid.co/oauth2/token \
           --header 'Content-Type: application/json' \
           --data '{
             "grant_type": "authorization_code",
             "client_id": "<CLIENT_ID>",
             "client_secret": "<CLIENT_SECRET>",
             "code": "<AUTHORIZATION_CODE>",
             "redirect_uri": "<REDIRECT_URI>"
           }'
         

  5. The response includes an `access_token` and a `refresh_token`. Record both values securely.

**Note:** The authorization code is valid for two minutes. Exchange it promptly.



### Verify API access

  * Confirm that the access token works by making a test request:
        
        curl --request GET \
          --url 'https://api.lucid.co/auditLogs?pageSize=1' \
          --header 'Authorization: Bearer <ACCESS_TOKEN>' \
          --header 'Lucid-Api-Version: 1' \
          --header 'Accept: application/json'
        




A successful response returns a JSON array of audit log events.

### Required API permissions

  * The OAuth 2.0 client requires the following scope:

Scope | Token Type | Purpose  
---|---|---  
**account.audit.logs** | Account | Retrieve audit log events for the account  
**Note:** Only read access is required. The `account.audit.logs` scope is valid for both Account tokens and User tokens, but Account tokens are recommended for SIEM integrations because they are not tied to an individual user session.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `lucid-audit-logs-gcs`)  
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
     * **Service account name** : Enter `lucid-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Lucid audit logs`
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
  2. Click on your bucket name (`lucid-audit-logs-gcs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`lucid-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `lucid-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Lucid Audit Logs API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `lucid-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `lucid-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `lucid-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `lucid-audit-logs-gcs` | GCS bucket name  
`GCS_PREFIX` | `lucid-audit` | Prefix for log files  
`STATE_KEY` | `lucid-audit/state.json` | State file path  
`LUCID_CLIENT_ID` | `your-oauth-client-id` | Lucid OAuth 2.0 Client ID  
`LUCID_CLIENT_SECRET` | `your-oauth-client-secret` | Lucid OAuth 2.0 Client Secret  
`LUCID_REFRESH_TOKEN` | `your-refresh-token` | Lucid OAuth 2.0 Refresh Token  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `200` | Records per API page (max 200)  
`MAX_PAGES` | `50` | Max pages per run  
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
        import re
        
        http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=10.0, read=60.0),
            retries=False,
        )
        
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        
        GCS_BUCKET = os.environ.get('GCS_BUCKET')
        GCS_PREFIX = os.environ.get('GCS_PREFIX', 'lucid-audit')
        STATE_KEY = os.environ.get('STATE_KEY', 'lucid-audit/state.json')
        LUCID_CLIENT_ID = os.environ.get('LUCID_CLIENT_ID')
        LUCID_CLIENT_SECRET = os.environ.get('LUCID_CLIENT_SECRET')
        LUCID_REFRESH_TOKEN = os.environ.get('LUCID_REFRESH_TOKEN')
        LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
        PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '200'))
        MAX_PAGES = int(os.environ.get('MAX_PAGES', '50'))
        
        API_BASE = 'https://api.lucid.co'
        
        @functions_framework.cloud_event
        def main(cloud_event):
            if not all([GCS_BUCKET, LUCID_CLIENT_ID, LUCID_CLIENT_SECRET, LUCID_REFRESH_TOKEN]):
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
        
                print(f"Fetching audit logs from {last_time.isoformat()} to {now.isoformat()}")
        
                access_token, new_refresh_token = refresh_access_token()
        
                if new_refresh_token:
                    save_refresh_token(bucket, new_refresh_token)
        
                records, newest_event_time = fetch_audit_logs(access_token, last_time, now)
        
                if not records:
                    print("No new audit log records found.")
                    save_state(bucket, now.isoformat())
                    return
        
                timestamp = now.strftime('%Y%m%d_%H%M%S')
                object_key = f"{GCS_PREFIX}/lucid_audit_{timestamp}.ndjson"
                blob = bucket.blob(object_key)
        
                ndjson = '\n'.join(
                    [json.dumps(record, ensure_ascii=False) for record in records]
                ) + '\n'
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
        
                print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
        
                if newest_event_time:
                    save_state(bucket, newest_event_time)
                else:
                    save_state(bucket, now.isoformat())
        
                print(f"Successfully processed {len(records)} audit log records")
        
            except Exception as e:
                print(f'Error processing logs: {str(e)}')
                raise
        
        def refresh_access_token():
            url = f"{API_BASE}/oauth2/token"
            body = json.dumps({
                'grant_type': 'refresh_token',
                'refresh_token': LUCID_REFRESH_TOKEN,
                'client_id': LUCID_CLIENT_ID,
                'client_secret': LUCID_CLIENT_SECRET
            }).encode('utf-8')
        
            response = http.request(
                'POST', url,
                body=body,
                headers={'Content-Type': 'application/json'}
            )
        
            if response.status != 200:
                raise Exception(
                    f"Token refresh failed: {response.status} - "
                    f"{response.data.decode('utf-8')}"
                )
        
            data = json.loads(response.data.decode('utf-8'))
            access_token = data.get('access_token')
            new_refresh_token = data.get('refresh_token')
        
            if not access_token:
                raise Exception("No access_token in token refresh response")
        
            print("Successfully refreshed Lucid API access token")
            return access_token, new_refresh_token
        
        def fetch_audit_logs(access_token, start_time, end_time):
            records = []
            newest_time = None
            page_num = 0
            next_page_url = None
        
            since_str = start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            until_str = end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        
            while page_num < MAX_PAGES:
                page_num += 1
        
                if next_page_url:
                    url = next_page_url
                else:
                    url = (
                        f"{API_BASE}/auditLogs"
                        f"?pageSize={PAGE_SIZE}"
                        f"&since={since_str}"
                        f"&until={until_str}"
                    )
        
                headers = {
                    'Authorization': f'Bearer {access_token}',
                    'Lucid-Api-Version': '1',
                    'Accept': 'application/json'
                }
        
                response = http.request('GET', url, headers=headers)
        
                if response.status == 429:
                    print(f"Rate limited on page {page_num}. Stopping pagination.")
                    break
        
                if response.status != 200:
                    print(
                        f"API error on page {page_num}: {response.status} - "
                        f"{response.data.decode('utf-8')}"
                    )
                    break
        
                page_results = json.loads(response.data.decode('utf-8'))
        
                if not page_results:
                    print(f"No more results at page {page_num}")
                    break
        
                records.extend(page_results)
                print(f"Page {page_num}: Retrieved {len(page_results)} events "
                      f"(total: {len(records)})")
        
                for event in page_results:
                    try:
                        event_time = event.get('eventTimestamp')
                        if event_time:
                            if newest_time is None or event_time > newest_time:
                                newest_time = event_time
                    except Exception as e:
                        print(f"Warning: Could not parse event time: {e}")
        
                link_header = response.headers.get('Link', '')
                next_page_url = parse_link_header(link_header)
        
                if not next_page_url:
                    print(f"No next page link found. Pagination complete.")
                    break
        
                if len(page_results) < PAGE_SIZE:
                    break
        
            print(f"Total audit log records fetched: {len(records)} from {page_num} pages")
            return records, newest_time
        
        def parse_link_header(link_header):
            if not link_header:
                return None
        
            match = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
            if match:
                return match.[group](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_group)(1)
            return None
        
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
        
        def save_refresh_token(bucket, new_refresh_token):
            try:
                token_key = f"{GCS_PREFIX}/refresh_token.json"
                blob = bucket.blob(token_key)
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                    json.dumps({'refresh_token': new_refresh_token}, indent=2),
                    content_type='application/json'
                )
                print("Saved new refresh token to GCS")
            except Exception as e:
                print(f"Warning: Could not save refresh token: {e}")
        

  * **requirements.txt:**
        
        functions-framework==3.*
          google-cloud-storage==2.*
          urllib3>=2.0.0
          ```
        



  1. Click **Deploy** to save and deploy the function.
  2. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `lucid-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `lucid-audit-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`lucid-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `lucid-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully refreshed Lucid API access token
         Page 1: Retrieved X events (total: X)
         Wrote X records to gs://lucid-audit-logs-gcs/lucid-audit/lucid_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X audit log records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `lucid-audit-logs-gcs`.

  10. Navigate to the `lucid-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `LUCID_CLIENT_ID`, `LUCID_CLIENT_SECRET`, and `LUCID_REFRESH_TOKEN` environment variables are correct
  * **HTTP 403** : Verify the OAuth 2.0 client has the `account.audit.logs` scope and the token is an account token
  * **HTTP 429** : Rate limiting — the function will stop pagination and resume on the next scheduled run
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Audit log event categories

Lucid audit logs are organized into the following event categories:

Category | Description  
---|---  
**Logins** | Events associated with user logins  
**Content** | Events associated with document and folder access and modification  
**Administration** | Events associated with admin activity and account changes  
**User** | Events associated with user actions on personal settings  
**Team** | Events associated with team operations  
  
For a complete list of event types and their schemas, see the [Lucid Audit Log Events](https://lucid.readme.io/reference/audit-log-events) documentation.

## FedRAMP environment

Users in the Lucid FedRAMP environment use different authorization and API endpoints. See the [Lucid FedRAMP environment](https://lucid.readme.io/reference/lucids-fedramp-environment) documentation for the correct endpoint URLs.

## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Lucid Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Lucid** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://lucid-audit-logs-gcs/lucid-audit/
           

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
  2. Click on `lucid-audit-logs-gcs`.
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
document_opened | additional.fields | Merged with labels created from each source field if not empty  
share_link_enable | additional.fields |   
restricted_account_enable | additional.fields |   
event1.documentIds | additional.fields |   
team_folder | additional.fields |   
method_type | additional.fields |   
extensions.auth.type | extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" for login/logout events  
eventTimestamp | metadata.event_timestamp | Converted using date match ISO8601 or yyyy-MM-ddTHH:mm:ss.SSSSSSZ  
has_user_login | metadata.event_type | Set based on has_* flags: USER_LOGIN if has_user_login and has_target_user, USER_LOGOUT if has_user_logout and has_target_user, USER_RESOURCE_UPDATE_CONTENT if has_user_resource_updated and has_target_resource and has_principal_user, USER_CREATION if has_principal_user and has_target_application and has_target_user, USER_RESOURCE_CREATION if has_target_resource and has_principal_user, FILE_CREATION if has_target_file and has_principal and has_target, USER_RESOURCE_ACCESS if has_target_resource, USER_COMMUNICATION if has_principal_user, STATUS_UPDATE if has_principal and has_target false, else GENERIC_EVENT  
has_user_logout | metadata.event_type |   
has_user_resource_updated | metadata.event_type |   
has_principal_user | metadata.event_type |   
has_target_resource | metadata.event_type |   
has_target_file | metadata.event_type |   
has_principal | metadata.event_type |   
has_target_user | metadata.event_type |   
has_target_application | metadata.event_type |   
has_target | metadata.event_type |   
event1.event1Type | metadata.product_event_type | Value copied directly  
actor.actorIp | principal.asset.ip | Value copied directly if not empty  
actor.actorIp | principal.ip | Value copied directly if not empty  
actor.actorAccountId | principal.resource.id | Value copied directly if not empty  
actor.actorClient | principal.resource.name | Value copied directly if not empty  
flowId | principal.resource.product_object_id | Value copied directly if not empty  
actor.actorType | principal.user.attribute.roles | Merged from actor_type if eventType not login/logout and actor_type not empty  
actor.actorEmail | principal.user.email_addresses | Merged if actor_email not empty and valid email and eventType not login/logout  
actor.actorUserId | principal.user.userid | Value copied directly if not empty and eventType not login/logout  
event1.registrationMethod | security_result.description | Value copied directly if not empty  
event1.source | target.application | Value copied directly if not empty  
event1.publishedLink.link | target.file.full_path | Value copied directly if not empty  
event1.filename | target.file.names | Merged if not empty  
targetData._targetType | target.resource.attribute.labels | Merged with labels created from each source field if not empty  
targetData._targetId | target.resource.attribute.labels |   
event1.format | target.resource.attribute.labels |   
event1.method | target.resource.attribute.labels |   
event1.publishedLink.format | target.resource.attribute.labels |   
accountId | target.resource.id | Value copied directly if not empty  
event1.destinationFolderName | target.resource.name | Set to destinationFolderName if not empty, else folderName if not empty, else publishedLink.name if not empty  
event1.folderName | target.resource.name |   
event1.publishedLink.name | target.resource.name |   
event1.documentId | target.resource.product_object_id | Value copied directly if not empty  
actor.actorType | target.user.attribute.roles | Merged from actor_type if eventType is login/logout, and from event_role if not empty  
event1.role | target.user.attribute.roles |   
actor.actorEmail | target.user.email_addresses | Merged from actor_email if login/logout and valid, and from userEmail in _target  
targetData.userEmail | target.user.email_addresses |   
event1.destinationFolderId | target.user.product_object_id | Set to destinationFolderId if not empty, else folderId if not empty  
event1.folderId | target.user.product_object_id |   
targetData.displayName | target.user.user_display_name | Value copied directly if not empty  
actor.actorUserId | target.user.userid | Value copied directly if not empty and eventType is login/logout  
event1.product | metadata.product_name | Value from product if not empty, else "LUCID"  
metadata.vendor_name | metadata.vendor_name | Set to "LUCID"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lucid-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
