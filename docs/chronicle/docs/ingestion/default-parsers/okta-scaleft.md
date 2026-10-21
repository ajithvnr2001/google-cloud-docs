---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-scaleft/
title: Collect Okta Advanced Server Access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:27:08.989982+00:00
---

# Collect Okta Advanced Server Access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/okta-scaleft/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Okta Advanced Server Access logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Okta Advanced Server Access logs to Google Security Operations using Google Cloud Storage V2.

Okta Advanced Server Access (formerly ScaleFT) is a privileged access management solution that provides SSH and RDP access to servers with ephemeral certificates and comprehensive audit logging. The platform retains audit events for 90 days and provides an API to retrieve these events for long-term storage and analysis in SIEM platforms.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to your Okta Advanced Server Access team
  * Ability to create service users and API keys in Advanced Server Access



## Configure Okta Advanced Server Access API access

To enable Google SecOps to retrieve audit events, you need to create a service user and generate an API key. Service users are special accounts designed for automation and API integrations.

### Create a service user

  1. Sign in to the [Advanced Server Access dashboard](https://app.scaleft.com).
  2. Go to **Users**.
  3. Select the **Service Users** tab.
  4. Click **Create Service User**.
  5. In the **Username** field, enter a descriptive name for the service user (for example, `chronicle-integration`).

**Note:** The system automatically creates corresponding Linux and Windows usernames based on the username you provide.
  6. Click **Create Service User**.




### Generate an API key

  1. On the service user details page, click **Create API Key**.
  2. Copy and save the following credentials immediately:

     * **API Key ID** : A UUID that identifies the API key (for example, `6052868b-1b04-4a14-8288-e6496d7f2f4b`)
     * **API Key Secret** : A base64-encoded secret string used to authenticate API requests
**Note:** You cannot retrieve the API key secret after closing this window. If you lose this information, you must generate a new API key.
  3. Click **Done**.




### Assign the service user to a group with appropriate permissions

Service users must be members of a group with appropriate team-wide roles to access the Audits API.

  1. In the Advanced Server Access dashboard, go to **Groups**.
  2. Select an existing group or create a new group for API access.
  3. Click the group name to open the group details.
  4. Select the **Users** tab.
  5. Click **Add User**.
  6. Search for and select the service user (for example, `chronicle-integration`).
  7. Click **Add**.
  8. Select the **Roles** tab.
  9. Ensure the group has one of the following team-wide roles:

     * **reporting_user** : Read-only access to all endpoints (recommended for log ingestion)
     * **access_admin** : Full administrative access (grants all CRUD permissions)
**Note:** For least-privilege access, use the **reporting_user** role. This role provides read-only access to audit events without granting administrative permissions.
  10. If the required role is not assigned, click **Add Role** , select **reporting_user** or **access_admin** , and click **Save**.




### Verify permissions

To verify the service user has the required permissions:

  1. In the Advanced Server Access dashboard, go to **Groups**.
  2. Click on the group containing the service user (for example, `chronicle-integration`).
  3. Select the **Roles** tab.
  4. Confirm the **reporting_user** or **access_admin** role is listed.
  5. If you cannot see the Roles tab, contact your administrator to grant appropriate access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        TEAM_NAME="your-team-name"
        KEY_ID="your-api-key-id"
        KEY_SECRET="your-api-key-secret"
        
        # Obtain bearer token
        TOKEN=$(curl -s -X POST "https://app.scaleft.com/v1/teams/${TEAM_NAME}/service_token" \
            -H "Content-Type: application/json" \
            -d "{\"key_id\": \"${KEY_ID}\", \"key_secret\": \"${KEY_SECRET}\"}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['bearer_token'])")
        
        # Test audit events access
        curl -s -H "Authorization: Bearer ${TOKEN}" \
            "https://app.scaleft.com/v1/teams/${TEAM_NAME}/auditsV2?count=5" \
            | python3 -m json.tool
        




A successful response returns a JSON array of recent audit events.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `okta-asa-audit-logs`)  
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
     * **Service account name** : Enter `okta-asa-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Okta Advanced Server Access audit logs`
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
  2. Click on your bucket name (`okta-asa-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`okta-asa-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `okta-asa-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Okta Advanced Server Access Audits API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `okta-asa-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `okta-asa-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `okta-asa-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `okta-asa-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `okta-asa-audit` | Prefix for log files  
`STATE_KEY` | `okta-asa-audit/state.json` | State file path  
`ASA_TEAM_NAME` | `your-team-name` | Advanced Server Access team name  
`ASA_KEY_ID` | `your-api-key-id` | Service user API key ID  
`ASA_KEY_SECRET` | `your-api-key-secret` | Service user API key secret  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per API page (max 1000)  
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
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'okta-asa-audit')
           STATE_KEY = os.environ.get('STATE_KEY', 'okta-asa-audit/state.json')
           ASA_TEAM_NAME = os.environ.get('ASA_TEAM_NAME')
           ASA_KEY_ID = os.environ.get('ASA_KEY_ID')
           ASA_KEY_SECRET = os.environ.get('ASA_KEY_SECRET')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           ASA_API_BASE = 'https://app.scaleft.com'
           
           @functions_framework.cloud_event
           def main(cloud_event):
             if not all([GCS_BUCKET, ASA_TEAM_NAME, ASA_KEY_ID, ASA_KEY_SECRET]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket)
               now = datetime.now(timezone.utc)
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_offset'):
                 last_offset = state['last_offset']
               else:
                 last_offset = None
           
               print(f"Starting audit log collection (last_offset={last_offset})")
           
               token = get_bearer_token()
           
               records, newest_offset = fetch_audit_events(
                 token=token,
                 last_offset=last_offset,
                 page_size=PAGE_SIZE,
                 max_records=MAX_RECORDS,
               )
           
               if not records:
                 print("No new audit records found.")
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/okta_asa_audit_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               if newest_offset:
                 save_state(bucket, newest_offset)
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def get_bearer_token():
             url = f"{ASA_API_BASE}/v1/teams/{ASA_TEAM_NAME}/service_token"
             body = json.dumps({
               'key_id': ASA_KEY_ID,
               'key_secret': ASA_KEY_SECRET
             }).encode('utf-8')
           
             response = http.request(
               'POST', url,
               body=body,
               headers={'Content-Type': 'application/json'}
             )
           
             if response.status != 200:
               raise Exception(
                 f"Service token request failed: {response.status} - "
                 f"{response.data.decode('utf-8')}"
               )
           
             data = json.loads(response.data.decode('utf-8'))
             token = data.get('bearer_token')
             if not token:
               raise Exception("No bearer_token in service token response")
           
             print("Successfully obtained ASA bearer token")
             return token
           
           def fetch_audit_events(token, last_offset, page_size, max_records):
             endpoint = f"{ASA_API_BASE}/v1/teams/{ASA_TEAM_NAME}/auditsV2"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
             }
           
             records = []
             page_num = 0
             backoff = 1.0
             current_offset = last_offset
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               params = [f"count={page_size}"]
               if current_offset:
                 params.append(f"offset={current_offset}")
           
               url = f"{endpoint}?{'&'.join(params)}"
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status == 401:
                   print("Token expired (401). Refreshing bearer token...")
                   token = get_bearer_token()
                   headers['Authorization'] = f'Bearer {token}'
                   continue
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return records, current_offset
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 page_results = data.get('list', [])
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 # Extract next offset from Link header for pagination
                 link_header = response.headers.get('Link', '')
                 next_offset = extract_next_offset(link_header)
           
                 if next_offset:
                   current_offset = next_offset
                 else:
                   print("No more pages (no next link)")
                   break
           
               except Exception as e:
                 print(f"Error fetching audit events: {e}")
                 return records, current_offset
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, current_offset
           
           def extract_next_offset(link_header):
             if not link_header:
               return None
           
             parts = link_header.split(',')
             for part in parts:
               if 'rel="next"' in part:
                 url_part = part.split(';')[0].strip().strip('<>')
                 if 'offset=' in url_part:
                   for param in url_part.split('?')[-1].split('&'):
                     if param.startswith('offset='):
                       return param.split('=', 1)[1]
             return None
           
           def load_state(bucket):
             try:
               blob = bucket.blob(STATE_KEY)
               if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
             return {}
           
           def save_state(bucket, last_offset):
             try:
               state = {
                 'last_offset': last_offset,
                 'last_run': datetime.now(timezone.utc).isoformat()
               }
               blob = bucket.blob(STATE_KEY)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_offset={last_offset}")
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
**Name** | `okta-asa-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `okta-asa-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`okta-asa-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `okta-asa-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Starting audit log collection (last_offset=None)
         Successfully obtained ASA bearer token
         Page 1: Retrieved X events
         Wrote X records to gs://okta-asa-audit-logs/okta-asa-audit/okta_asa_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `okta-asa-audit-logs`.

  10. Navigate to the `okta-asa-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `ASA_KEY_ID` and `ASA_KEY_SECRET` environment variables are correct
  * **HTTP 403** : Verify the service user has the **reporting_user** or **access_admin** role
  * **HTTP 429** : Rate limiting — the function will automatically retry with exponential backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Okta ASA Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Okta Advanced Server Access** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email is displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://okta-asa-audit-logs/okta-asa-audit/
           

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

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `okta-asa-audit-logs`.
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
details.actor.details.email | principal.user.email_addresses | Value copied directly  
details.actor.details.first_name | principal.user.first_name | Value copied directly  
details.actor.details.full_name | principal.user.user_display_name | Value copied directly  
details.actor.details.last_name | principal.user.last_name | Value copied directly  
details.actor.details.user_type | principal.user.attribute.roles | Value copied directly  
details.actor.id | principal.user.employee_id | Value copied directly  
details.actor.name | principal.user.userid | Value from details.actor.name if not empty, else details.unix_user_name  
details.unix_user_name | principal.user.userid |   
details.actor.status | principal.user.attribute.labels | Merged as label with key "actor_status"  
details.actor.team_name | principal.user.department | Value copied directly  
details.actor.user_type | principal.user.attribute.labels | Merged as label with key "actor_user_type"  
details.client.description | principal.application | Value copied directly  
details.client.encrypted | principal.asset.attribute.labels | Converted to string, merged as label with key "details_client_encrypted"  
details.client.hostname | principal.hostname, principal.asset.hostname | Value copied directly  
details.client.id | principal.user.product_object_id | Value copied directly  
details.client.os | principal.platform | Set to WINDOWS if matches (?i)Win|win; LINUX if matches (?i)Lin|lin; MAC if matches (?i)Mac|ios|mac; ANDROID if matches (?i)Android|android  
details.client.os | principal.platform_version | Extracted major.minor.patch from os string using grok  
details.client.state | principal.resource.attribute.labels | Merged as label with key "client_state"  
details.client.user_name | target.user.userid | Value copied directly  
details.client_ip | principal.ip, principal.asset.ip | Extracted IP using grok pattern  
details.from_address | principal.ip, principal.asset.ip | Extracted IP using grok pattern  
details.project.create_server_users | target.resource.attribute.labels | Converted to string, merged as label with key "project_create_server_users"  
details.project.force_shared_ssh_users | target.resource.attribute.labels | Converted to string, merged as label with key "project_force_shared_ssh_users"  
details.project.forward_traffic | target.resource.attribute.labels | Converted to string, merged as label with key "project_forward_traffic"  
details.project.id | target.resource.id | Value copied directly  
details.project.name | target.resource.name | Value copied directly  
details.project.next_unix_gid | target.resource.attribute.labels | Converted to string, merged as label with key "next_unix_gid"  
details.project.next_unix_uid | target.resource.attribute.labels | Converted to string, merged as label with key "next_unix_uid"  
details.project.rdp_session_recording | target.resource.attribute.labels | Converted to string, merged as label with key "project_rdp_session_recording"  
details.project.require_preauth_for_creds | target.resource.attribute.labels | Converted to string, merged as label with key "project_require_preauth_for_creds"  
details.project.ssh_certificate_type | target.resource.attribute.labels | Merged as label with key "project_ssh_certificate_type"  
details.project.ssh_session_recording | target.resource.attribute.labels | Converted to string, merged as label with key "project_ssh_session_recording"  
details.project.team | target.resource.attribute.labels | Merged as label with key "project_team"  
details.server.alt_names | target.hostname, target.asset.hostname, target.resource.attribute.labels | First alt_name set to target.hostname and target.asset.hostname, others merged as labels with key "alt_name"  
details.server.hostname | intermediary_value.hostname | Value copied directly  
details.server.id | intermediary_value.resource.attribute.labels | Merged as label with key "details_server_id"  
details.server.os | intermediary_value.platform_version | Value copied directly  
details.server.os | intermediary_value.resource.attribute.labels | Merged as label with key "details_server_os"  
details.server.os_type | intermediary_value.platform | Set to LINUX if matches (?i)linux; WINDOWS if matches (?i)windows; MAC if matches (?i)mac  
details.server.services | intermediary_value.resource.attribute.labels | Merged as labels with key "server_services {index}"  
details.server.source | intermediary_value.resource.attribute.labels | Merged as label with key "server_source"  
details.server.source_details.cloud_account | intermediary_value.resource.attribute.labels | Merged as label with key "server_source_details_cloud_account"  
details.server.source_details.cloud_provider | intermediary_value.resource.attribute.labels | Merged as label with key "server_source_details_cloud_provider"  
details.server.source_details.instance_id | intermediary_value.resource.attribute.labels | Merged as label with key "server_source_details_instance_id"  
details.server.state | target.asset.attribute.labels | Converted to string, merged as label with key "server_state"  
details.server.team_name | intermediary_value.user.department | Value copied directly  
details.server_hostnames | target.hostname, target.resource.attribute.labels | First hostname set to target.hostname, others merged as labels with key "server_hostname {index}"  
details.server_id | target.resource.attribute.labels | Merged as label with key "details_server_id"  
details.server_os | target.platform_version | Value copied directly  
details.server_os_type | target.platform | Set to LINUX if matches (?i)linux; WINDOWS if matches (?i)windows; MAC if matches (?i)mac  
details.server_state | target.resource.attribute.labels | Merged as label with key "details_server_state"  
details.session_type | extensions.auth.auth_details | Value copied directly  
details.session_type | security_result.detection_fields | Merged as label with key "session_type"  
details.servers | intermediary | Processed and merged as intermediary object  
details.ssh_algorithm | network.tls.cipher | Value copied directly  
details.ssh_key_fingerprint | target.asset.attribute.labels | Merged as label with key "ssh_key_fingerprint"  
details.ssh_public_key | security_result.detection_fields | Merged as label with key "ssh_public_key"  
details.target_server | target.application | Value copied directly  
details.team_id | principal.resource.id | Value copied directly  
details.team_id | target.resource.id | Value copied directly  
details.team_name | additional.fields | Merged as label with key "team_name"  
details.trace_id | network.session_id | Value copied directly  
details.type | metadata.product_event_type | Value copied directly  
details.username | target.user.user_display_name | Value copied directly  
details.via | network.session_id | Value copied directly  
details_server | intermediary_value | Processed and merged as intermediary_value object  
id | additional.fields | Merged as label with key "id"  
timestamp | metadata.event_timestamp | Converted using ISO8601 format  
extensions.auth.type | extensions.auth.type | Set to "SSO" if metadata.event_type is USER_LOGIN  
intermediary_value | intermediary | Merged from intermediary_value if not empty  
has_principal_user | metadata.event_type | Set to USER_LOGIN if has_principal_user and has_target_user or has_principal_user and has_target and details_type matches login; else USER_UNCATEGORIZED if has_principal_user; else STATUS_UPDATE if has_principal  
has_target_user | metadata.event_type |   
metadata.product_name | metadata.product_name | Set to "OKTA_SCALEFT"  
metadata.vendor_name | metadata.vendor_name | Set to "OKTA_SCALEFT"  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`asset_id` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`details.hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`details.actor` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`details.client` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`details.username` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`details.server.server_accounts.username` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`details.project` | `event.idm.read_only_udm.target.resource.attribute.cloud.project.name` | Mapped from changelog  
`details.server.server_accounts` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`"id"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"details.from_address"` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`"details.client_ip"` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`"details.from_address"` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`"details.client_ip"` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`"details.type"` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`"details.actor.status"` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`"details.actor.user_type"` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`"details.session_type"` | `event.idm.read_only_udm.extensions.auth.auth_details` | Mapped from changelog  
`"details.actor.name"` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`"details.unix_user_name"` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`"details.actor.details.full_name"` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`"details.actor.details.first_name"` | `event.idm.read_only_udm.principal.user.first_name` | Mapped from changelog  
`"details.actor.details.last_name"` | `event.idm.read_only_udm.principal.user.last_name` | Mapped from changelog  
`"details.actor.id"` | `event.idm.read_only_udm.principal.user.employee_id` | Mapped from changelog  
`"details.actor.team_name"` | `event.idm.read_only_udm.principal.user.department` | Mapped from changelog  
`"details.client.hostname"` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`"details.client.hostname"` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`"details.client.id"` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`"details.client.description"` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`"details.client.os"` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`"details_client_os"` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`"details.actor.details.email"` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`"details.team_id"` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`"details.project.id"` | `event.idm.read_only_udm.target.resource.id` | Mapped from changelog  
`"details.team_name"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"details.client.state"` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`"details.target_server"` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`"details.via"` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`"details.trace_id"` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`"details_session_type"` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`"details.ssh_public_key"` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`"details.actor.details.user_type"` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`"details.project.name"` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`"details.server.id"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.server.state"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.team"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.create_server_users"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.force_shared_ssh_users"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.forward_traffic"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.next_unix_gid"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.next_unix_uid"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.rdp_session_recording"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.require_preauth_for_creds"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.ssh_certificate_type"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.project.ssh_session_recording"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"serverhostname"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"alt_name"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.ssh_key_fingerprint"` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`"details.server.os"` | `event.idm.read_only_udm.target.platform_version` | Mapped from changelog  
`"detailsserver.os"` | `event.idm.read_only_udm.target.platform_version` | Mapped from changelog  
`"details.server.os_type"` | `event.idm.read_only_udm.target.platform` | Mapped from changelog  
`"detailsserver.os_type"` | `event.idm.read_only_udm.target.platform` | Mapped from changelog  
`"details_team_id"` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`"details.client.encrypted"` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`"details.client.user_name"` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`"timestamp"` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`"serverhostname"` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`"alt_name"` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`"alt_name"` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`"intermediary"` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`"intermediary_value"` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`"detailsserver.sftd_version"` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`"details.server.sftd_version"` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`"detailsserver.state"` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`"detailsserver.managed"` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`"detailsserver.ssh_key_fingerprint"` | `event.idm.read_only_udm.target.asset.attribute.labels` | Mapped from changelog  
`"details.username"` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`"details.ssh_algorithm"` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-scaleft-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
